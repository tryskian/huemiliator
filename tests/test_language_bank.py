from __future__ import annotations

import json
import re
from pathlib import Path
from unittest.mock import patch

import pytest

from huemiliator.config import SOURCE_ROOT
from huemiliator.families import FAMILY_NAMES
from huemiliator.language_bank import (
    LanguageBankError,
    load_language_bank,
    validate_language_bank,
)
from huemiliator.main import main, render_behaviour_facts


def test_authorial_openings_preserve_the_charter_verbatim() -> None:
    charter = (SOURCE_ROOT / "docs/governance/CHARTER.md").read_text()
    reference = re.search(r"```text\n(.*?)\n```", charter, re.DOTALL)
    assert reference is not None
    bank = load_language_bank()
    authorial = [
        entry
        for entry in bank["entries"]
        if bank["sources"][entry["source"]]["authorship"] == "human"
    ]

    assert [entry["text"] for entry in authorial] == reference.group(1).splitlines()
    assert all(entry["role"] == "opening" for entry in authorial)
    for entry in authorial:
        for family in FAMILY_NAMES:
            if re.search(rf"\b{family}\b", entry["text"]):
                assert f"family_{family}" in entry["requires"]


def test_bank_covers_runtime_families_and_evidence_sensitive_relations() -> None:
    bank = load_language_bank()
    entries = {entry["id"]: entry for entry in bank["entries"]}
    for family in FAMILY_NAMES:
        assert f"family_{family}" in entries[f"colour.{family}"]["requires"]
    assert "same_hex" in entries["colour.same_colour"]["requires"]
    assert "different_hex" in entries["colour.different_shade"]["requires"]

    connectors = {entry["id"]: entry for entry in bank["connectors"]}
    assert "explanation_basis" in connectors["because.explanation"]["requires"]
    assert "expectation_basis" in connectors["although.concession"]["requires"]
    assert "contrast_basis" in connectors["but.contrast"]["requires"]
    assert "expectation_basis" in connectors["but.concession"]["requires"]


@pytest.mark.parametrize("hex_value", ["#d9a6a1", "#947764", "#eee2dd"])
def test_slot_bindings_resolve_against_fixed_fact_packets(hex_value: str) -> None:
    bank = load_language_bank()
    facts = json.loads(render_behaviour_facts(hex_value, "json"))
    for binding in bank["slots"].values():
        value = facts
        for key in binding.split("."):
            value = value[key]
        assert isinstance(value, str) and value


def test_loader_rejects_duplicate_json_keys(tmp_path: Path) -> None:
    data = tmp_path / "data"
    data.mkdir()
    (data / "language_bank.json").write_text('{"sources": {}, "sources": {}}')
    with patch("huemiliator.language_bank.files", return_value=tmp_path):
        with pytest.raises(LanguageBankError, match="Duplicate JSON key"):
            load_language_bank()


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("source", "missing_source", "Unknown source"),
        ("requires", ["unrecorded_condition"], "Unknown condition"),
        ("requires", [], "requires usage conditions"),
        ("requires", ["same_hex", "same_hex"], "Duplicate condition"),
        ("requires", [42], "Unknown condition"),
        ("role", "opennig", "Unknown role"),
        ("text", "{replacement_name.upper}", "Unsupported slot"),
        ("text", "{replacement_name!r}", "Unsupported slot"),
        ("text", "{replacement_name:>20}", "Unsupported slot"),
        ("text", "{unknown_slot}", "Unsupported slot"),
        ("text", "{replacement_name", "Invalid template"),
        ("meaning", "", "must be non-empty text"),
    ],
)
def test_bank_rejects_broken_entry_contracts(
    field: str, value: object, message: str
) -> None:
    bank = load_language_bank()
    bank["entries"][0][field] = value

    with pytest.raises(LanguageBankError, match=message):
        validate_language_bank(bank)


def test_bank_rejects_duplicate_ids_and_duplicate_wording() -> None:
    bank = load_language_bank()
    bank["entries"][1]["id"] = bank["entries"][0]["id"]
    with pytest.raises(LanguageBankError, match="duplicate ID"):
        validate_language_bank(bank)

    bank = load_language_bank()
    bank["entries"][1]["text"] = bank["entries"][0]["text"]
    with pytest.raises(LanguageBankError, match="Duplicate wording"):
        validate_language_bank(bank)


@pytest.mark.parametrize("payload", [None, [], {"schema": "unknown"}])
def test_bank_rejects_invalid_payload_shape(payload: object) -> None:
    with pytest.raises(LanguageBankError):
        validate_language_bank(payload)


def test_inspection_works_outside_repo_without_loading_runtime_state(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.chdir(tmp_path)
    with patch("huemiliator.main.load_settings", side_effect=AssertionError):
        assert main(["language-bank", "--format", "json"]) == 0

    bank = validate_language_bank(json.loads(capsys.readouterr().out))
    assert bank["evaluation_status"] == "awaiting_behaviour_evaluation"
    assert not list(tmp_path.iterdir())


def test_text_inventory_identifies_provenance_and_evaluation_status(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert main(["language-bank"]) == 0
    output = capsys.readouterr().out
    assert "[human]: excellent red..." in output
    assert "[assistant]: I prefer {replacement_name}" in output
    assert "awaiting_behaviour_evaluation" in output
    assert "because.explanation" in output


def test_cli_reports_an_invalid_bank_without_a_traceback(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with patch(
        "huemiliator.main.render_language_bank",
        side_effect=LanguageBankError("Unknown source in an entry."),
    ):
        assert main(["language-bank"]) == 1
    output = capsys.readouterr()
    assert output.out == ""
    assert output.err.strip() == "Unknown source in an entry."
