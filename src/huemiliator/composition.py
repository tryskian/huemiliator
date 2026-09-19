from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from typing import Any

from openai import APIError, OpenAI

from huemiliator.agent import (
    COMPOSITION_DIRECTIONS,
    COMPOSITION_INSTRUCTIONS_VERSION,
)
from huemiliator.config import DEFAULT_REASONING_EFFORT
from huemiliator.language_bank import load_language_bank

COMPOSER_VERSION = "0.2.0"
MAX_OUTPUT_TOKENS = 8192
REQUEST_TIMEOUT_SECONDS = 60.0


class CompositionError(RuntimeError):
    """An API request could not produce an inspectable composition record."""


def _digest(value: object) -> str:
    text = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()


def _output_schema() -> dict[str, Any]:
    relationship = {
        "type": "object",
        "properties": {
            "connector_id": {"type": "string"},
            "claim_a": {"type": "string"},
            "claim_b": {"type": "string"},
            "basis": {
                "type": "string",
                "description": (
                    "Brief supporting fact or contextual basis for this relationship; "
                    "for concession, the expectation and its source."
                ),
            },
        },
        "required": ["connector_id", "claim_a", "claim_b", "basis"],
        "additionalProperties": False,
    }
    return {
        "type": "object",
        "properties": {
            "response": {
                "type": "string",
                "description": "Hugh's complete visible line.",
            },
            "entry_ids": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Library entries used or adapted in the visible line.",
            },
            "relationships": {
                "type": "array",
                "items": relationship,
                "description": (
                    "Relationships between claims joined by a connector word in the "
                    "visible line. Separate sentences can use an empty list."
                ),
            },
        },
        "required": ["response", "entry_ids", "relationships"],
        "additionalProperties": False,
    }


def build_composition_request(
    fact_packet: dict[str, Any],
    model: str,
    reasoning_effort: str = DEFAULT_REASONING_EFFORT,
) -> dict[str, Any]:
    """Prepare the exact model request using fixed facts and a local bank snapshot."""
    if reasoning_effort not in {"none", "low", "medium", "high", "xhigh", "max"}:
        raise ValueError(
            "HUEMILIATOR_REASONING_EFFORT must be "
            "none, low, medium, high, xhigh or max."
        )
    bank = load_language_bank()
    facts = {k: v for k, v in fact_packet["runtime_facts"].items() if k != "loss_line"}
    input_hex = fact_packet["input"]["hex"]
    replacement = facts["replacement"]
    same_hex = input_hex == replacement["hex"]
    same_name = facts["nearest_swatch"]["name"] == replacement["name"]
    factual_conditions = {
        "same_hex": same_hex,
        "different_hex": not same_hex,
        "same_name": same_name,
        "different_name": not same_name,
    }
    factual_conditions.update(
        {
            name: name == f"family_{facts['family']}"
            for name in bank["conditions"]
            if name.startswith("family_")
        }
    )
    eligible = [
        entry
        for entry in bank["entries"]
        if all(
            factual_conditions.get(condition, True) for condition in entry["requires"]
        )
    ]
    slot_values = {}
    for slot, binding in bank["slots"].items():
        value: Any = fact_packet
        for part in binding.split("."):
            value = value[part]
        slot_values[slot] = value

    material = {
        "input": fact_packet["input"],
        "runtime_facts": facts,
        "context": "A person chose this colour in the picker. Hugh responds once.",
        "factual_conditions": factual_conditions,
        "slot_values": slot_values,
        "library": {**bank, "entries": eligible},
    }
    api_request = {
        "model": model,
        "reasoning": {"effort": reasoning_effort},
        "instructions": "\n".join(
            f"{i}. {line}" for i, line in enumerate(COMPOSITION_DIRECTIONS, start=1)
        ),
        "input": json.dumps(material, ensure_ascii=False),
        "text": {
            "format": {
                "type": "json_schema",
                "name": "hue_composition",
                "strict": True,
                "schema": _output_schema(),
            }
        },
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "store": False,
    }
    return {
        "schema": "huemiliator.composition_request.v1",
        "composer_version": COMPOSER_VERSION,
        "instructions_version": COMPOSITION_INSTRUCTIONS_VERSION,
        "bank_version": bank["version"],
        "bank_sha256": _digest(bank),
        "request_sha256": _digest(api_request),
        "api_request": api_request,
    }


def check_composition(payload: object, request: dict[str, Any]) -> list[str]:
    """Check mechanical integrity. Voice, meaning and attribution need evaluation."""
    if not isinstance(payload, dict) or set(payload) != {
        "response",
        "entry_ids",
        "relationships",
    }:
        return ["Output must contain response, entry_ids and relationships."]
    response = payload["response"]
    entry_ids = payload["entry_ids"]
    relationships = payload["relationships"]
    if (
        not isinstance(response, str)
        or not response.strip()
        or not isinstance(entry_ids, list)
        or not entry_ids
        or not all(isinstance(value, str) for value in entry_ids)
        or not isinstance(relationships, list)
    ):
        return [
            "Output needs a non-empty response, entry ID list and relationship list."
        ]
    material = json.loads(request["api_request"]["input"])
    entries = {entry["id"]: entry for entry in material["library"]["entries"]}
    connectors = {entry["id"]: entry for entry in material["library"]["connectors"]}
    errors = []
    if any(entry_id not in entries for entry_id in entry_ids):
        errors.append("An entry ID is unknown or ineligible for these colour facts.")
    if len(set(entry_ids)) != len(entry_ids):
        errors.append("Entry IDs must be unique.")
    if not any(
        entries.get(entry_id, {}).get("role") == "opening" for entry_id in entry_ids
    ):
        errors.append("The entry references must include an opening.")
    replacement = material["runtime_facts"]["replacement"]
    if not re.search(rf"(?<!\w){re.escape(replacement['name'])}(?!\w)", response, re.I):
        errors.append("The visible response is missing the supplied replacement name.")
    hexes = re.findall(r"#[0-9a-fA-F]{6}\b", response)
    if replacement["hex"].lower() not in [value.lower() for value in hexes]:
        errors.append("The visible response is missing the supplied replacement hex.")
    supplied_hexes = {
        material["input"]["hex"],
        material["runtime_facts"]["nearest_swatch"]["hex"],
        replacement["hex"],
    }
    if any(value.lower() not in supplied_hexes for value in hexes):
        errors.append("The visible response contains a hex outside the supplied facts.")
    recorded_words = set()
    for relationship in relationships:
        fields = {"connector_id", "claim_a", "claim_b", "basis"}
        if (
            not isinstance(relationship, dict)
            or set(relationship) != fields
            or any(
                not isinstance(v, str) or not v.strip() for v in relationship.values()
            )
        ):
            errors.append(
                "Each relationship needs a connector, two claims and a basis."
            )
            continue
        connector = connectors.get(relationship["connector_id"])
        if connector is None:
            errors.append("A connector ID is unknown.")
        else:
            word = connector["word"]
            recorded_words.add(word)
            if not re.search(rf"\b{word}\b", response, re.I):
                errors.append(
                    "A recorded connector is absent from the visible response."
                )
    for word in {connector["word"] for connector in connectors.values()}:
        if re.search(rf"\b{word}\b", response, re.I) and word not in recorded_words:
            errors.append(
                f"The visible connector '{word}' needs a relationship record."
            )
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
    composition = None
    errors = []
    if result.status != "completed":
        errors.append("The API response did not complete.")
    if refusals:
        errors.append("The model returned a refusal.")
    try:
        composition = json.loads(raw_text)
    except (ValueError, TypeError):
        errors.append("The output is not a complete JSON composition.")
    else:
        errors.extend(check_composition(composition, request))
    return {
        "schema": "huemiliator.composition_record.v1",
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
