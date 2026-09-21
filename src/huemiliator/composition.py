from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from typing import Any

from openai import APIError, OpenAI

from huemiliator.agent import (
    COMPOSITION_INSTRUCTIONS,
    COMPOSITION_INSTRUCTIONS_VERSION,
)
from huemiliator.config import (
    DEFAULT_REASONING_EFFORT,
    DEFAULT_TOP_P,
    DEFAULT_VERBOSITY,
)

COMPOSER_VERSION = "0.5.2"
MAX_OUTPUT_TOKENS = 8192
REQUEST_TIMEOUT_SECONDS = 60.0


class CompositionError(RuntimeError):
    """An API request could not produce an inspectable composition record."""


def _digest(value: object) -> str:
    text = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()


def build_composition_request(
    fact_packet: dict[str, Any],
    model: str,
    reasoning_effort: str = DEFAULT_REASONING_EFFORT,
    verbosity: str = DEFAULT_VERBOSITY,
    top_p: float | str = DEFAULT_TOP_P,
) -> dict[str, Any]:
    """Prepare a free-text request from Hugh's directions and fixed colour facts."""
    if reasoning_effort not in {"none", "low", "medium", "high", "xhigh", "max"}:
        raise ValueError(
            "HUEMILIATOR_REASONING_EFFORT must be "
            "none, low, medium, high, xhigh or max."
        )
    if verbosity not in {"low", "medium", "high"}:
        raise ValueError("HUEMILIATOR_VERBOSITY must be low, medium or high.")
    try:
        sampling_probability = float(top_p)
    except ValueError:
        raise ValueError(
            "HUEMILIATOR_TOP_P must be a number between 0 and 1."
        ) from None
    if not 0 <= sampling_probability <= 1:
        raise ValueError("HUEMILIATOR_TOP_P must be a number between 0 and 1.")
    facts = {k: v for k, v in fact_packet["runtime_facts"].items() if k != "loss_line"}
    input_hex = fact_packet["input"]["hex"]
    replacement = facts["replacement"]
    display_swatches = [
        {"role": "chosen", "label": facts["family"], "hex": input_hex},
        {
            "role": "replacement",
            "label": replacement["name"],
            "hex": replacement["hex"],
        },
    ]
    material = {
        "input": fact_packet["input"],
        "runtime_facts": facts,
        "context": (
            "A person chose this colour in the picker. The user's colour is named "
            "by its mapped family; Hugh's colour is the supplied same-family "
            "replacement, using its Pantone name alone. Hugh responds once "
            "alongside the two labelled display swatches; hex codes are rendering data."
        ),
        "display_swatches": display_swatches,
    }
    api_request = {
        "model": model,
        "reasoning": {"effort": reasoning_effort},
        "instructions": COMPOSITION_INSTRUCTIONS,
        "input": json.dumps(material, ensure_ascii=False),
        "text": {"format": {"type": "text"}, "verbosity": verbosity},
        "top_p": sampling_probability,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "store": False,
    }
    return {
        "schema": "huemiliator.composition_request.v2",
        "composer_version": COMPOSER_VERSION,
        "instructions_version": COMPOSITION_INSTRUCTIONS_VERSION,
        "request_sha256": _digest(api_request),
        "display_swatches": display_swatches,
        "api_request": api_request,
    }


def check_composition(response: object, request: dict[str, Any]) -> list[str]:
    """Check concrete output integrity; voice and meaning need attributed evaluation."""
    if not isinstance(response, str) or not response.strip():
        return ["Output must contain a non-empty response."]
    material = json.loads(request["api_request"]["input"])
    errors = []
    replacement = material["runtime_facts"]["replacement"]
    replacement_pattern = rf"(?<!\w){re.escape(replacement['name'])}(?!\w)"
    if not re.search(replacement_pattern, response, re.I):
        errors.append("The visible response is missing the supplied replacement name.")
    supplied_hexes = {
        value.lstrip("#").lower()
        for value in (
            material["input"]["hex"],
            material["runtime_facts"]["nearest_swatch"]["hex"],
            replacement["hex"],
        )
    }
    hex_tokens = re.findall(
        r"(?<!\w)(?:#[0-9a-f]{3,8}|0x[0-9a-f]{3,8}|"
        r"[0-9a-f]{8}\b|[0-9a-f]{6}\b)",
        response,
        re.I,
    )
    if any(
        value.startswith("#")
        or value.lower().startswith("0x")
        or any(char.isdigit() for char in value)
        or value.lower() in supplied_hexes
        for value in hex_tokens
    ):
        errors.append("The visible response contains a hex code.")
    return errors


def generate_composition(
    request: dict[str, Any], *, client: OpenAI | None = None
) -> dict[str, Any]:
    """Make one request and retain its visible output, including mechanical failures."""
    if client is None:
        if not os.getenv("OPENAI_API_KEY", "").strip():
            raise CompositionError("OPENAI_API_KEY is required for live composition.")
        with OpenAI(timeout=REQUEST_TIMEOUT_SECONDS, max_retries=0) as owned_client:
            return generate_composition(request, client=owned_client)
    started_at = datetime.now(timezone.utc).isoformat()
    try:
        result = client.responses.create(**request["api_request"])
    except APIError as exc:
        # Provider messages can echo credentials or request data. Keep CLI errors safe.
        status = getattr(exc, "status_code", None)
        detail = f" (HTTP {status})" if status is not None else ""
        raise CompositionError(
            f"OpenAI composition request failed: {type(exc).__name__}{detail}."
        ) from None
    completed_at = datetime.now(timezone.utc).isoformat()
    refusals = [
        content.refusal
        for item in result.output
        if item.type == "message"
        for content in item.content
        if content.type == "refusal"
    ]
    raw_text = result.output_text
    composition = {"response": raw_text}
    errors = []
    if result.status != "completed":
        errors.append("The API response did not complete.")
    if refusals:
        errors.append("The model returned a refusal.")
    errors.extend(check_composition(raw_text, request))
    return {
        "schema": "huemiliator.composition_record.v2",
        "request": request,
        "started_at": started_at,
        "completed_at": completed_at,
        "api_response": {
            "id": result.id,
            "model": result.model,
            "status": result.status,
            "usage": result.usage.model_dump() if result.usage else None,
            "incomplete_details": (
                result.incomplete_details.model_dump()
                if result.incomplete_details
                else None
            ),
            "refusals": refusals,
            "output_text": raw_text,
        },
        "composition": composition,
        "mechanical_checks": {"ok": not errors, "issues": errors},
        "behaviour_verdict": None,
    }
