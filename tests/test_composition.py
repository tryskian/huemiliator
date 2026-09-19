from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import httpx
import pytest
from openai import AuthenticationError, OpenAI
from openai.types.responses import Response

from huemiliator.agent import COMPOSITION_DIRECTIONS
from huemiliator.composition import (
    CompositionError,
    build_composition_request,
    check_composition,
    generate_composition,
)
from huemiliator.config import SOURCE_ROOT
from huemiliator.main import build_behaviour_fact_packet, main, render_composition


@pytest.fixture
def request_packet() -> dict[str, Any]:
    return build_composition_request(
        build_behaviour_fact_packet("#d9a6a1"), "test-model"
    )


@pytest.fixture
def candidate() -> dict[str, Any]:
    return {
        "response": "Excellent red... but Ash rose is just more satisfying.",
        "entry_ids": ["appraisal.excellent", "verdict.just_more_satisfying"],
        "relationships": [
            {
                "connector_id": "but.contrast",
                "claim_a": "The chosen red receives Hugh's approval.",
                "claim_b": "Ash rose is just more satisfying.",
                "basis": (
                    "Approval of the input contrasted with Ash rose's superiority."
                ),
            }
        ],
    }


def api_result(text: str, status: str = "completed", refusal: bool = False) -> Response:
    content = (
        {"type": "refusal", "refusal": "Test refusal"}
        if refusal
        else {"type": "output_text", "text": text, "annotations": [], "logprobs": []}
    )
    return Response.model_validate(
        {
            "id": "resp_test",
            "created_at": 123,
            "model": "test-model-snapshot",
            "object": "response",
            "status": status,
            "output": [
                {
                    "id": "msg_test",
                    "type": "message",
                    "role": "assistant",
                    "status": "completed",
                    "content": [content],
                }
            ],
            "error": None,
            "incomplete_details": None,
            "instructions": None,
            "metadata": {},
            "parallel_tool_calls": True,
            "tools": [],
            "tool_choice": "auto",
            "temperature": 1,
            "top_p": 1,
            "usage": None,
        }
    )


def test_five_directions_match_the_staged_authorial_setup() -> None:
    note = (SOURCE_ROOT / "docs/research/030_PB_BEHAVIOUR.md").read_text()
    directions = re.findall(r"^[1-5]\. (.+)$", note, re.M)
    assert tuple(directions) == COMPOSITION_DIRECTIONS
    assert len(directions) == 5


@pytest.mark.parametrize("hex_value", ["#d9a6a1", "#947764", "#eee2dd"])
def test_request_filters_only_fact_conflicts_and_keeps_semantics(
    hex_value: str,
) -> None:
    original = build_behaviour_fact_packet(hex_value)
    saved = copy.deepcopy(original)
    request = build_composition_request(original, "chosen-model")
    material = json.loads(request["api_request"]["input"])
    entries = {entry["id"]: entry for entry in material["library"]["entries"]}
    assert original == saved
    assert "loss_line" not in material["runtime_facts"]
    assert "response_contract" not in material
    assert material["input"]["hex"] == original["input"]["hex"]
    assert set(material["slot_values"]) == {"input_family", "replacement_name"}
    assert (
        material["runtime_facts"]["replacement"]
        == original["runtime_facts"]["replacement"]
    )
    same_hex = (
        original["input"]["hex"] == original["runtime_facts"]["replacement"]["hex"]
    )
    assert ("colour.same_colour" in entries) == same_hex
    assert ("colour.different_shade" in entries) != same_hex
    assert "opening.popular_fragment" in entries
    assert "familiarity_appraisal" in entries["opening.popular_fragment"]["requires"]
    assert "popular_completion" in entries["opening.popular_fragment"]["requires"]
    assert {
        "appraisal.bold",
        "appraisal.lovely",
        "appraisal.excellent",
        "appraisal.divine",
        "appraisal.sublime",
        "appraisal.exceptional",
        "opening.crowd_pleaser",
        "opening.popular_fragment",
    } <= entries.keys()
    for entry in entries.values():
        assert all(
            material["factual_conditions"].get(key, True) for key in entry["requires"]
        )
    assert len(material["library"]["connectors"]) == 14
    properties = request["api_request"]["text"]["format"]["schema"]["properties"]
    assert set(properties["entry_ids"]["items"]["enum"]) == set(entries)
    relation_properties = properties["relationships"]["items"]["properties"]
    assert set(relation_properties["connector_id"]["enum"]) == {
        connector["id"] for connector in material["library"]["connectors"]
    }
    assert request["api_request"]["model"] == "chosen-model"
    assert request == build_composition_request(original, "chosen-model")
    other = build_composition_request(original, "different-model")
    assert request["request_sha256"] != other["request_sha256"]
    assert request["bank_sha256"] == other["bank_sha256"]
    assert request["api_request"]["reasoning"] == {"effort": "medium"}
    other_effort = build_composition_request(original, "chosen-model", "low")
    assert other_effort["api_request"]["reasoning"] == {"effort": "low"}
    assert request["request_sha256"] != other_effort["request_sha256"]


def test_invalid_reasoning_is_rejected_before_building_request() -> None:
    with pytest.raises(ValueError, match="HUEMILIATOR_REASONING_EFFORT"):
        build_composition_request(
            build_behaviour_fact_packet("#d9a6a1"), "test", "typo"
        )


def test_identity_condition_uses_actual_input_not_nearest_swatch() -> None:
    packet = build_behaviour_fact_packet("#947764")
    packet["input"]["hex"] = "#947765"
    request = build_composition_request(packet, "test")
    material = json.loads(request["api_request"]["input"])
    assert material["factual_conditions"]["same_hex"] is False


def test_sdk_serializes_request_and_record_retains_actual_output(
    request_packet: dict[str, Any], candidate: dict[str, Any]
) -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        assert json.loads(request.content) == request_packet["api_request"]
        return httpx.Response(200, json=api_result(json.dumps(candidate)).model_dump())

    with OpenAI(
        api_key="unit-test-key",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    ) as client:
        record = generate_composition(request_packet, client=client)
    assert record["composition"] == candidate
    assert record["request"] == request_packet
    assert record["api_response"]["model"] == "test-model-snapshot"
    assert record["api_response"]["output_text"] == json.dumps(candidate)
    assert record["started_at"] <= record["completed_at"]
    assert record["mechanical_checks"] == {"ok": True, "issues": []}
    assert record["behaviour_verdict"] is None


@pytest.mark.parametrize(
    "problem",
    [
        "missing_name",
        "visible_hex",
        "ineligible_entry",
        "duplicate_entry",
        "no_opening_reference",
        "missing_relationship",
        "unknown_connector",
        "missing_basis",
        "absent_connector",
        "broken_shape",
    ],
)
def test_mechanical_checks_catch_concrete_failures(
    problem: str, candidate: dict[str, Any], request_packet: dict[str, Any]
) -> None:
    if problem == "missing_name":
        candidate["response"] = candidate["response"].replace(
            "Ash rose", "Something else"
        )
    elif problem == "visible_hex":
        candidate["response"] += " #b5817d"
    elif problem == "ineligible_entry":
        candidate["entry_ids"].append("colour.green")
    elif problem == "duplicate_entry":
        candidate["entry_ids"].append(candidate["entry_ids"][0])
    elif problem == "no_opening_reference":
        candidate["entry_ids"] = ["verdict.just_more_satisfying"]
    elif problem == "missing_relationship":
        candidate["relationships"] = []
    elif problem == "unknown_connector":
        candidate["relationships"][0]["connector_id"] = "because.contrast"
    elif problem == "missing_basis":
        candidate["relationships"][0]["basis"] = ""
    elif problem == "absent_connector":
        candidate["response"] = candidate["response"].replace(" but ", " ")
    elif problem == "broken_shape":
        candidate["entry_ids"] = [1]
    assert check_composition(candidate, request_packet)


def test_mechanical_checks_do_not_pretend_to_validate_meaning(
    candidate: dict[str, Any], request_packet: dict[str, Any]
) -> None:
    candidate["relationships"][0]["basis"] = "A deliberately unsupported explanation."
    assert check_composition(candidate, request_packet) == []


@pytest.mark.parametrize(
    "hex_code", ["#b5817d", "#B5817D", "#abc", "#12345678", "0x79c753", "79c753"]
)
def test_visible_hex_codes_fail_while_facts_remain_inspectable(
    hex_code: str, candidate: dict[str, Any], request_packet: dict[str, Any]
) -> None:
    candidate["response"] += f" ({hex_code})"
    assert "The visible response contains a hex code." in check_composition(
        candidate, request_packet
    )
    material = json.loads(request_packet["api_request"]["input"])
    assert material["runtime_facts"]["replacement"]["hex"] == "#b5817d"


def test_ordinary_words_are_not_mistaken_for_bare_hex_codes(
    candidate: dict[str, Any], request_packet: dict[str, Any]
) -> None:
    candidate["response"] += " A decade of assured taste."
    assert check_composition(candidate, request_packet) == []


def test_generic_opening_works_with_the_family_on_the_swatch_label(
    candidate: dict[str, Any], request_packet: dict[str, Any]
) -> None:
    candidate["response"] = "A popular one... but Ash rose is just more satisfying."
    candidate["entry_ids"] = ["opening.popular_one", "verdict.just_more_satisfying"]
    assert check_composition(candidate, request_packet) == []
    assert request_packet["display_swatches"][0]["label"] == "red"


@pytest.mark.parametrize(
    ("word", "connector_id"),
    [
        ("therefore", "therefore.consequence"),
        ("however", "however.contrast"),
        ("yet", "yet.contrast"),
        ("nevertheless", "nevertheless.concession"),
    ],
)
def test_rhetorical_question_keeps_its_connector_and_implied_claim(
    word: str, connector_id: str, request_packet: dict[str, Any]
) -> None:
    candidate = {
        "response": f"A lovely red; {word}, is Ash rose not the finer choice?",
        "entry_ids": ["appraisal.lovely", "verdict.finer"],
        "relationships": [
            {
                "connector_id": connector_id,
                "claim_a": "The chosen red receives Hugh's approval.",
                "claim_b": "Hugh judges Ash rose the finer choice.",
                "basis": "Test annotation; the evaluator must judge the relationship.",
            }
        ],
    }
    assert check_composition(candidate, request_packet) == []


@pytest.mark.parametrize(
    ("response", "entry_id"),
    [
        ("A lovely red. Ash rose is rather finer.", "modifier.rather"),
        ("A lovely red. Which is finer than Ash rose?", "question.which"),
        ("A lovely red. Ash rose is yet finer.", "modifier.yet"),
        (
            "A lovely red. Ash rose is essentially the finer choice.",
            "modifier.essentially",
        ),
    ],
)
def test_lexical_uses_do_not_require_invented_two_claim_relationships(
    response: str, entry_id: str, request_packet: dict[str, Any]
) -> None:
    candidate = {
        "response": response,
        "entry_ids": ["appraisal.lovely", entry_id, "verdict.finer"],
        "relationships": [],
    }
    assert check_composition(candidate, request_packet) == []
    candidate["entry_ids"] = ["appraisal.lovely", "verdict.finer"]
    assert any(
        "needs a relationship record" in issue
        for issue in check_composition(candidate, request_packet)
    )


def test_unambiguous_conclusion_marker_requires_a_relationship(
    candidate: dict[str, Any], request_packet: dict[str, Any]
) -> None:
    candidate["response"] = (
        "A lovely red. Therefore, why settle for less than Ash rose?"
    )
    candidate["relationships"] = []
    assert "The visible connector 'therefore' needs a relationship record." in (
        check_composition(candidate, request_packet)
    )


@pytest.mark.parametrize(
    ("text", "status", "refusal"),
    [
        ('{"response":', "incomplete", False),
        ("not JSON", "completed", False),
        ("", "completed", True),
        ("null", "completed", False),
    ],
)
def test_incomplete_refused_and_malformed_outputs_are_retained(
    request_packet: dict[str, Any], text: str, status: str, refusal: bool
) -> None:
    client = MagicMock(spec=OpenAI)
    client.responses.create.return_value = api_result(text, status, refusal)
    record = generate_composition(request_packet, client=client)
    assert record["mechanical_checks"]["ok"] is False
    assert record["api_response"]["output_text"] == text
    assert record["behaviour_verdict"] is None
    client.responses.create.assert_called_once()


def test_api_error_does_not_echo_provider_secret_message(
    request_packet: dict[str, Any],
) -> None:
    client = MagicMock(spec=OpenAI)
    client.responses.create.side_effect = AuthenticationError(
        "secret-marker",
        response=httpx.Response(
            401, request=httpx.Request("POST", "https://api.openai.com")
        ),
        body=None,
    )
    with pytest.raises(CompositionError, match="AuthenticationError.*401") as raised:
        generate_composition(request_packet, client=client)
    assert "secret-marker" not in str(raised.value)


def test_missing_key_fails_before_client_creation(
    request_packet: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with patch("huemiliator.composition.OpenAI") as client:
        with pytest.raises(CompositionError, match="OPENAI_API_KEY"):
            generate_composition(request_packet)
    client.assert_not_called()


def test_dry_run_works_without_credentials_or_state_writes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("HUEMILIATOR_MODEL", "configured-model")
    monkeypatch.setenv("HUEMILIATOR_REASONING_EFFORT", "high")
    with (
        patch("huemiliator.config.load_dotenv"),
        patch("huemiliator.main.generate_composition") as generate,
    ):
        assert main(["compose", "#d9a6a1", "--dry-run"]) == 0
    request = json.loads(capsys.readouterr().out)
    assert request["api_request"]["model"] == "configured-model"
    assert request["api_request"]["reasoning"] == {"effort": "high"}
    assert "OPENAI_API_KEY" not in json.dumps(request)
    assert not list(tmp_path.iterdir())
    generate.assert_not_called()


@pytest.mark.parametrize("output_format", ["text", "json"])
def test_cli_preserves_failed_record_and_returns_distinct_status(
    output_format: str, capsys: pytest.CaptureFixture[str]
) -> None:
    record = {
        "mechanical_checks": {"ok": False, "issues": ["Bad reference"]},
        "api_response": {"output_text": "original output"},
        "behaviour_verdict": None,
    }
    with patch("huemiliator.main.generate_composition", return_value=record):
        assert main(["compose", "#d9a6a1", "--format", output_format]) == 2
    output = capsys.readouterr()
    assert json.loads(output.out) == record
    assert "Bad reference" in output.err


def test_cli_prints_visible_response_on_success(
    candidate: dict[str, Any],
    request_packet: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    record = {
        "request": request_packet,
        "composition": candidate,
        "mechanical_checks": {"ok": True, "issues": []},
    }
    with patch("huemiliator.main.generate_composition", return_value=record):
        assert main(["compose", "#d9a6a1"]) == 0
    assert capsys.readouterr().out.strip() == (
        "■ red    ■ Ash rose\n\n" + candidate["response"]
    )


@pytest.mark.parametrize("colour", [False, True])
def test_swatch_rendering_keeps_labels_and_exact_selection_separate_from_speech(
    colour: bool, candidate: dict[str, Any]
) -> None:
    packet = build_behaviour_fact_packet("#d9a6a1")
    packet["input"]["hex"] = "#d9a6a2"
    request = build_composition_request(packet, "test")
    material = json.loads(request["api_request"]["input"])
    assert (
        request["display_swatches"]
        == material["display_swatches"]
        == [
            {"role": "chosen", "label": "red", "hex": "#d9a6a2"},
            {"role": "replacement", "label": "Ash rose", "hex": "#b5817d"},
        ]
    )
    output = render_composition(
        {"request": request, "composition": candidate}, colour=colour
    )
    assert "red" in output.splitlines()[0]
    assert "Ash rose" in output.splitlines()[0]
    assert "#" not in output
    assert output.endswith(candidate["response"])
    if colour:
        assert "\x1b[48;2;217;166;162m" in output
        assert "\x1b[48;2;181;129;125m" in output
    else:
        assert "\x1b" not in output
