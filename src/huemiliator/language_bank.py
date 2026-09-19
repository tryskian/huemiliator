from __future__ import annotations

import json
import re
from collections import Counter
from importlib.resources import files
from string import Formatter
from typing import Any

SCHEMA = "huemiliator.language_bank.v1"
LANGUAGE_ROLES = (
    "opening",
    "appraisal_word",
    "modifier",
    "appraisal_phrase",
    "preference",
    "colour_description",
)
RELATIONS = {"addition", "contrast", "explanation", "concession"}
ID_PATTERN = re.compile(r"[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)*")


class LanguageBankError(ValueError):
    """Raised when the local language bank is unreadable or structurally invalid."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise LanguageBankError(f"Duplicate JSON key: {key!r}.")
        result[key] = value
    return result


def _object(value: object, context: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not all(isinstance(k, str) for k in value):
        raise LanguageBankError(f"{context} must be an object with string keys.")
    return value


def _text(value: object, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise LanguageBankError(f"{context} must be non-empty text.")
    return value


def _fields(item: dict[str, Any], expected: set[str], context: str) -> None:
    if set(item) != expected:
        raise LanguageBankError(
            f"{context} fields differ: missing={sorted(expected - set(item))}, "
            f"unknown={sorted(set(item) - expected)}."
        )


def _registry(value: object, context: str) -> dict[str, Any]:
    registry = _object(value, context)
    if not registry:
        raise LanguageBankError(f"{context} must contain entries.")
    for key in registry:
        if not ID_PATTERN.fullmatch(key):
            raise LanguageBankError(f"Invalid {context} key: {key!r}.")
    return registry


def validate_language_bank(payload: object) -> dict[str, Any]:
    """Validate structure and references, leaving meaning and voice to evaluation."""
    bank = _object(payload, "language bank")
    _fields(
        bank,
        {
            "schema",
            "version",
            "evaluation_status",
            "sources",
            "slots",
            "conditions",
            "entries",
            "connectors",
        },
        "language bank",
    )
    if bank["schema"] != SCHEMA:
        raise LanguageBankError(
            f"Unsupported language bank schema: {bank['schema']!r}."
        )
    _text(bank["version"], "version")
    if bank["evaluation_status"] != "awaiting_behaviour_evaluation":
        raise LanguageBankError("The starter bank awaits behaviour evaluation.")

    sources = _registry(bank["sources"], "sources")
    for key, value in sources.items():
        source = _object(value, f"source {key}")
        _fields(source, {"authorship", "reference", "description"}, f"source {key}")
        if source["authorship"] not in ("human", "assistant"):
            raise LanguageBankError(f"Invalid authorship for source {key!r}.")
        _text(source["reference"], f"source {key} reference")
        _text(source["description"], f"source {key} description")

    slots = _registry(bank["slots"], "slots")
    conditions = _registry(bank["conditions"], "conditions")
    for registry in (slots, conditions):
        for key, value in registry.items():
            _text(value, key)

    seen_ids: set[str] = set()
    seen_text: set[tuple[str, str]] = set()
    common_fields = {"id", "meaning", "requires", "source"}
    for collection in ("entries", "connectors"):
        rows = bank[collection]
        if not isinstance(rows, list) or not rows:
            raise LanguageBankError(f"{collection} must be a non-empty list.")
        specific_fields = (
            {"role", "text", "grammar"}
            if collection == "entries"
            else {"word", "relation", "frame"}
        )
        for index, value in enumerate(rows):
            context = f"{collection}[{index}]"
            item = _object(value, context)
            _fields(item, common_fields | specific_fields, context)
            for key in (common_fields | specific_fields) - {"requires"}:
                _text(item[key], f"{context}.{key}")
            entry_id = item["id"]
            if not ID_PATTERN.fullmatch(entry_id) or entry_id in seen_ids:
                raise LanguageBankError(f"Invalid or duplicate ID: {entry_id!r}.")
            seen_ids.add(entry_id)
            if item["source"] not in sources:
                raise LanguageBankError(f"Unknown source in {entry_id!r}.")
            requirements = item["requires"]
            if not isinstance(requirements, list) or not requirements:
                raise LanguageBankError(f"{entry_id!r} requires usage conditions.")
            for condition in requirements:
                if not isinstance(condition, str) or condition not in conditions:
                    raise LanguageBankError(f"Unknown condition in {entry_id!r}.")
            if len(set(requirements)) != len(requirements):
                raise LanguageBankError(f"Duplicate condition in {entry_id!r}.")

            if collection == "connectors":
                if item["relation"] not in RELATIONS:
                    raise LanguageBankError(f"Unknown relation in {entry_id!r}.")
                continue

            if item["role"] not in LANGUAGE_ROLES:
                raise LanguageBankError(f"Unknown role in {entry_id!r}.")
            text_key = (item["role"], item["text"].casefold().strip())
            if text_key in seen_text:
                raise LanguageBankError(f"Duplicate wording in {entry_id!r}.")
            seen_text.add(text_key)
            try:
                for _, field, spec, conversion in Formatter().parse(item["text"]):
                    if field is not None and (field not in slots or spec or conversion):
                        raise LanguageBankError(f"Unsupported slot in {entry_id!r}.")
            except ValueError as exc:
                raise LanguageBankError(
                    f"Invalid template in {entry_id!r}: {exc}"
                ) from exc
    return bank


def load_language_bank() -> dict[str, Any]:
    """Read the bundled resource without loading colour state or contacting a model."""
    resource = files("huemiliator").joinpath("data").joinpath("language_bank.json")
    try:
        payload = json.loads(
            resource.read_text(encoding="utf-8"), object_pairs_hook=_unique_object
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise LanguageBankError(f"Cannot read language bank: {exc}") from exc
    return validate_language_bank(payload)


def render_language_bank(output_format: str = "text") -> str:
    bank = load_language_bank()
    if output_format == "json":
        return json.dumps(bank, ensure_ascii=False, indent=2)
    if output_format != "text":
        raise ValueError(f"Unsupported language bank format '{output_format}'.")

    entries = bank["entries"]
    roles = Counter(entry["role"] for entry in entries)
    lines = [
        "Hue language bank",
        f"schema: {bank['schema']}",
        f"version: {bank['version']}",
        f"evaluation: {bank['evaluation_status']}",
        f"entries: {len(entries)}",
        f"connector senses: {len(bank['connectors'])}",
        "Usage conditions guide composition and behaviour evaluation.",
        "This inventory performs structural validation; it supplies no eval verdict.",
    ]
    for role in LANGUAGE_ROLES:
        lines.extend(("", f"{role} ({roles[role]}):"))
        for entry in entries:
            if entry["role"] == role:
                author = bank["sources"][entry["source"]]["authorship"]
                lines.append(f"- {entry['id']} [{author}]: {entry['text']}")
    lines.extend(("", "connectors:"))
    for connector in bank["connectors"]:
        lines.append(f"- {connector['id']}: {connector['meaning']}")
    lines.append(
        "\nUse --format json for meanings, grammar, conditions and provenance."
    )
    return "\n".join(lines)
