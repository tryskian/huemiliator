from __future__ import annotations

import copy
import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import httpx
import pytest
from openai import AuthenticationError, OpenAI
from openai.types.responses import Response

from huemiliator.agent import COMPOSITION_INSTRUCTIONS
from huemiliator.composition import (
    CompositionError,
    build_composition_request,
    check_composition,
    generate_composition,
)
from huemiliator.main import build_behaviour_fact_packet, main, render_composition


@pytest.fixture
def request_packet() -> dict[str, Any]:
    return build_composition_request(
        build_behaviour_fact_packet("#d9a6a1"), "test-model"
    )


@pytest.fixture
def candidate() -> str:
    return "Red, admirably assured. Ash rose is superior: measured, warm and composed."


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
            "top_p": 0.98,
            "usage": None,
        }
    )


@pytest.mark.parametrize("hex_value", ["#d9a6a1", "#947764", "#eee2dd"])
def test_request_keeps_colour_facts_and_frees_model_language(hex_value: str) -> None:
    original = build_behaviour_fact_packet(hex_value)
    saved = copy.deepcopy(original)
    request = build_composition_request(original, "chosen-model")
    api = request["api_request"]
    material = json.loads(api["input"])
    assert original == saved
    assert set(material) == {"input", "runtime_facts", "context", "display_swatches"}
    assert material["runtime_facts"] == {
        k: v for k, v in original["runtime_facts"].items() if k != "loss_line"
    }
    assert material["input"] == original["input"]
    assert material["display_swatches"] == request["display_swatches"]
    assert "mapped family" in material["context"]
    assert "supplied same-family replacement" in material["context"]
    assert "Pantone name alone" in material["context"]
    assert api["instructions"] == COMPOSITION_INSTRUCTIONS
    assert api["text"] == {"format": {"type": "text"}, "verbosity": "medium"}
    assert api["reasoning"] == {
        "context": "all_turns",
        "effort": "medium",
        "summary": "detailed",
    }
    assert api["top_p"] == 0.98
    assert api["model"] == "chosen-model"
    assert api["store"] is True
    assert api["max_output_tokens"] is None
    assert request["schema"] == "huemiliator.composition_request.v2"
    assert request["composer_version"] == "0.7.2"
    assert request["instructions_version"] == "2.2.0"
    assert "bank_version" not in request and "bank_sha256" not in request
    assert request == build_composition_request(original, "chosen-model")
    variations: list[dict[str, Any]] = [
        {"model": "other-model"},
        {"reasoning_effort": "low"},
        {"verbosity": "high"},
        {"top_p": 0.7},
    ]
    for options in variations:
        other = build_composition_request(
            original, **{"model": "chosen-model", **options}
        )
        assert other["request_sha256"] != request["request_sha256"]


@pytest.mark.parametrize(
    ("options", "message"),
    [
        ({"reasoning_effort": "typo"}, "HUEMILIATOR_REASONING_EFFORT"),
        ({"verbosity": "typo"}, "HUEMILIATOR_VERBOSITY"),
        ({"top_p": "typo"}, "HUEMILIATOR_TOP_P"),
        ({"top_p": -0.1}, "HUEMILIATOR_TOP_P"),
        ({"top_p": 1.1}, "HUEMILIATOR_TOP_P"),
        ({"top_p": float("nan")}, "HUEMILIATOR_TOP_P"),
        ({"top_p": float("inf")}, "HUEMILIATOR_TOP_P"),
    ],
)
def test_invalid_settings_are_rejected_before_request(
    options: dict[str, Any], message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        build_composition_request(
            build_behaviour_fact_packet("#d9a6a1"), "test", **options
        )


def test_sdk_serializes_request_and_record_retains_exact_plain_text(
    request_packet: dict[str, Any], candidate: str
) -> None:
    original = f"  {candidate}\n"
    calls = []

    def respond(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        assert json.loads(request.content) == request_packet["api_request"]
        return httpx.Response(200, json=api_result(original).model_dump())

    with OpenAI(
        api_key="unit-test-key",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    ) as client:
        record = generate_composition(request_packet, client=client)
    assert len(calls) == 1
    assert record["schema"] == "huemiliator.composition_record.v2"
    assert record["composition"] == {"response": original}
    assert record["request"] == request_packet
    assert record["api_response"]["model"] == "test-model-snapshot"
    assert record["api_response"]["output_text"] == original
    assert record["started_at"] <= record["completed_at"]
    assert record["mechanical_checks"] == {"ok": True, "issues": []}
    assert record["behaviour_verdict"] is None


@pytest.mark.parametrize("stream", [False, True])
def test_request_matches_selected_platform_settings(stream: bool) -> None:
    reference = json.loads(
        (Path(__file__).parent / "fixtures" / "platform_v13_settings.json").read_text()
    )
    request = build_composition_request(
        build_behaviour_fact_packet("#a46f44"),
        reference["settings"]["model"],
        stream=stream,
    )
    actual = {
        key: value
        for key, value in request["api_request"].items()
        if key not in {"instructions", "input"}
    }
    expected = copy.deepcopy(reference["settings"])
    assert expected["reasoning"]["summary"] == "detailed"
    if stream:
        expected["stream"] = True
    assert actual == expected
    assert "mode" not in actual["reasoning"]
    assert "frequency_penalty" not in actual
    assert "presence_penalty" not in actual


def test_top_p_environment_text_becomes_a_numeric_api_setting() -> None:
    request = build_composition_request(
        build_behaviour_fact_packet("#d9a6a1"), "test-model", top_p="0.98"
    )
    assert request["api_request"]["top_p"] == 0.98
    assert isinstance(request["api_request"]["top_p"], float)


def test_invalid_top_p_only_blocks_composition(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv("HUEMILIATOR_TOP_P", "typo")
    with (
        patch("huemiliator.config.load_dotenv"),
        patch("huemiliator.main.generate_composition") as generate,
    ):
        assert main(["compose", "#d9a6a1"]) == 1
        composition_output = capsys.readouterr()
        assert composition_output.out == ""
        assert composition_output.err.strip() == (
            "HUEMILIATOR_TOP_P must be a number between 0 and 1."
        )
        assert main(["resolve", "#d9a6a1"]) == 0
        resolution_output = capsys.readouterr()
        assert "nearest swatch: Mellow rose" in resolution_output.out
        assert resolution_output.err == ""
        generate.assert_not_called()


@pytest.mark.parametrize("response", [None, "", " \n", {"response": "Ash rose"}])
def test_response_needs_nonempty_text(
    response: object, request_packet: dict[str, Any]
) -> None:
    assert check_composition(response, request_packet) == [
        "Output must contain a non-empty response."
    ]


def test_mechanical_name_check_preserves_supplied_colour_responsibility(
    request_packet: dict[str, Any], candidate: str
) -> None:
    assert check_composition(candidate, request_packet) == []
    assert check_composition(
        candidate.replace("Ash rose", "Mimosa"), request_packet
    ) == ["The visible response is missing the supplied replacement name."]


@pytest.mark.parametrize(
    "hex_code", ["#b5817d", "#B5817D", "#abc", "#12345678", "0x79c753", "79c753"]
)
def test_visible_hex_codes_fail_while_facts_remain_inspectable(
    hex_code: str, candidate: str, request_packet: dict[str, Any]
) -> None:
    assert "The visible response contains a hex code." in check_composition(
        f"{candidate} ({hex_code})", request_packet
    )
    material = json.loads(request_packet["api_request"]["input"])
    assert material["runtime_facts"]["replacement"]["hex"] == "#b5817d"


def test_mechanical_checks_leave_language_and_meaning_to_evaluation(
    request_packet: dict[str, Any],
) -> None:
    response = (
        "Red, if one insists; although Ash rose is superior—because a decade of "
        "moonlight taught it rhetoric. Surely?"
    )
    assert check_composition(response, request_packet) == []


@pytest.mark.parametrize(
    ("text", "status", "refusal"),
    [
        ("Ash rose, incompletely", "incomplete", False),
        ("", "completed", False),
        ("", "completed", True),
        ("A different name", "completed", False),
        ("Ash rose (#b5817d)", "completed", False),
    ],
)
def test_failed_outputs_are_retained_without_behaviour_verdict(
    request_packet: dict[str, Any], text: str, status: str, refusal: bool
) -> None:
    client = MagicMock(spec=OpenAI)
    client.responses.create.return_value = api_result(text, status, refusal)
    record = generate_composition(request_packet, client=client)
    assert record["mechanical_checks"]["ok"] is False
    assert record["api_response"]["output_text"] == text
    assert record["composition"] == {"response": text}
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


def test_owned_client_uses_one_attempt_and_bounded_timeout(
    request_packet: dict[str, Any], candidate: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "unit-test-key")
    with patch("huemiliator.composition.OpenAI") as client:
        owned = client.return_value.__enter__.return_value
        owned.responses.create.return_value = api_result(candidate)
        generate_composition(request_packet)
    client.assert_called_once_with(timeout=60.0, max_retries=0)
    owned.responses.create.assert_called_once()


def test_dry_run_works_without_credentials_or_state_writes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("HUEMILIATOR_MODEL", "configured-model")
    monkeypatch.setenv("HUEMILIATOR_REASONING_EFFORT", "high")
    monkeypatch.setenv("HUEMILIATOR_VERBOSITY", "medium")
    monkeypatch.setenv("HUEMILIATOR_TOP_P", "0.7")
    with (
        patch("huemiliator.config.load_dotenv"),
        patch("huemiliator.main.generate_composition") as generate,
    ):
        assert main(["compose", "#d9a6a1", "--dry-run"]) == 0
    request = json.loads(capsys.readouterr().out)
    assert request["api_request"]["model"] == "configured-model"
    assert request["api_request"]["reasoning"] == {
        "context": "all_turns",
        "effort": "high",
        "summary": "detailed",
    }
    assert request["api_request"]["text"]["verbosity"] == "medium"
    assert request["api_request"]["top_p"] == 0.7
    assert "OPENAI_API_KEY" not in json.dumps(request)
    assert not list(tmp_path.iterdir())
    generate.assert_not_called()


@pytest.mark.parametrize("output_format", ["text", "json"])
def test_cli_preserves_failed_record_and_returns_distinct_status(
    output_format: str, capsys: pytest.CaptureFixture[str]
) -> None:
    record = {
        "mechanical_checks": {"ok": False, "issues": ["Missing supplied name"]},
        "api_response": {"output_text": "original output"},
        "behaviour_verdict": None,
    }
    with patch("huemiliator.main.generate_composition", return_value=record):
        assert main(["compose", "#d9a6a1", "--format", output_format]) == 2
    output = capsys.readouterr()
    assert json.loads(output.out) == record
    assert "Missing supplied name" in output.err


def test_cli_prints_visible_response_on_success(
    candidate: str,
    request_packet: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    record = {
        "request": request_packet,
        "composition": {"response": candidate},
        "mechanical_checks": {"ok": True, "issues": []},
    }
    with patch("huemiliator.main.generate_composition", return_value=record):
        assert main(["compose", "#d9a6a1"]) == 0
    assert capsys.readouterr().out.strip() == "■ red    ■ Ash rose\n\n" + candidate


@pytest.mark.parametrize("colour", [False, True])
def test_swatch_rendering_keeps_selection_separate_from_exact_speech(
    colour: bool, candidate: str
) -> None:
    packet = build_behaviour_fact_packet("#d9a6a1")
    packet["input"]["hex"] = "#d9a6a2"
    request = build_composition_request(packet, "test")
    assert request["display_swatches"] == [
        {"role": "chosen", "label": "red", "hex": "#d9a6a2"},
        {"role": "replacement", "label": "Ash rose", "hex": "#b5817d"},
    ]
    output = render_composition(
        {"request": request, "composition": {"response": candidate}}, colour=colour
    )
    assert "red" in output.splitlines()[0]
    assert "Ash rose" in output.splitlines()[0]
    assert "#" not in output
    assert output.endswith(candidate)
    if colour:
        assert "\x1b[48;2;217;166;162m" in output
        assert "\x1b[48;2;181;129;125m" in output
    else:
        assert "\x1b" not in output


def _summary_event(
    kind: str, sequence: int, text: str, part: int = 0
) -> dict[str, Any]:
    return {
        "type": f"response.reasoning_summary_text.{kind}",
        "item_id": "rs_test",
        "output_index": 0,
        "summary_index": part,
        "sequence_number": sequence,
        "delta" if kind == "delta" else "text": text,
    }


def _sse(event: dict[str, Any]) -> bytes:
    return ("data: " + json.dumps(event) + "\n\n").encode()


def _result_with_summaries(text: str, status: str = "completed") -> Response:
    result = api_result(text, status).model_dump()
    result["output"].insert(
        0,
        {
            "id": "rs_test",
            "type": "reasoning",
            "summary": [
                {"type": "summary_text", "text": "I compare the colours."},
                {"type": "summary_text", "text": "Then I consider the replacement."},
            ],
        },
    )
    return Response.model_validate(result)


def test_stream_flag_is_hashed_without_changing_model_or_input() -> None:
    from huemiliator.composition import _digest

    facts = build_behaviour_fact_packet("#a46f44")
    ordinary = build_composition_request(facts, "test-model")
    streaming = build_composition_request(facts, "test-model", stream=True)
    assert streaming["api_request"] == {**ordinary["api_request"], "stream": True}
    assert streaming["request_sha256"] == _digest(streaming["api_request"])
    assert ordinary["request_sha256"] != streaming["request_sha256"]
    assert ordinary["display_swatches"] == streaming["display_swatches"]


@pytest.mark.parametrize("status", ["completed", "incomplete", "failed"])
def test_stream_preserves_summaries_before_each_terminal_response(
    candidate: str, status: str
) -> None:
    request = build_composition_request(
        build_behaviour_fact_packet("#d9a6a1"), "test-model", stream=True
    )
    observed: list[dict[str, Any]] = []
    terminal = _result_with_summaries(candidate, status)
    events = [
        _summary_event("delta", 1, "I compare "),
        _summary_event("delta", 2, "the colours."),
        _summary_event("done", 3, "I compare the colours."),
        _summary_event("delta", 4, "Then I consider the replacement.", 1),
        _summary_event("done", 5, "Then I consider the replacement.", 1),
    ]

    class Body(httpx.SyncByteStream):
        closed = False

        def __iter__(self) -> Iterator[bytes]:
            for event in events:
                yield _sse(event)
            assert len(observed) == 5
            yield _sse(
                {
                    "type": f"response.{status}",
                    "sequence_number": 6,
                    "response": terminal.model_dump(),
                }
            )

        def close(self) -> None:
            self.closed = True

    body = Body()

    def respond(http_request: httpx.Request) -> httpx.Response:
        assert json.loads(http_request.content) == request["api_request"]
        return httpx.Response(
            200, headers={"Content-Type": "text/event-stream"}, stream=body
        )

    with OpenAI(
        api_key="unit-test-key",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    ) as client:
        record = generate_composition(
            request, client=client, on_reasoning=observed.append
        )
    assert body.closed
    assert observed[0]["delta"] == "I compare "
    assert observed[2]["text"] == "I compare the colours."
    assert observed[4]["summary_index"] == 1
    assert record["api_response"]["status"] == status
    assert record["api_response"]["reasoning_summaries"] == [
        {
            "item_id": "rs_test",
            "output_index": 0,
            "summary_index": 0,
            "text": "I compare the colours.",
        },
        {
            "item_id": "rs_test",
            "output_index": 0,
            "summary_index": 1,
            "text": "Then I consider the replacement.",
        },
    ]
    assert record["composition"]["response"] == candidate
    assert record["mechanical_checks"]["ok"] is (status == "completed")
    assert record["behaviour_verdict"] is None


@pytest.mark.parametrize("failure", ["eof", "http", "sse", "typed"])
def test_interrupted_stream_keeps_emitted_parts_and_never_fabricates_completion(
    failure: str,
) -> None:
    request = build_composition_request(
        build_behaviour_fact_packet("#d9a6a1"), "test-model", stream=True
    )
    observed: list[dict[str, Any]] = []

    class Body(httpx.SyncByteStream):
        closed = False

        def __iter__(self) -> Iterator[bytes]:
            yield _sse(_summary_event("delta", 1, "An observed partial summary."))
            if failure == "http":
                raise httpx.ReadTimeout("secret-marker")
            if failure == "sse":
                yield _sse({"error": {"message": "secret-marker"}})
            if failure == "typed":
                yield _sse(
                    {
                        "type": "error",
                        "sequence_number": 2,
                        "code": "server_error",
                        "message": "secret-marker",
                        "param": None,
                    }
                )
                yield _sse(
                    {
                        "type": "response.completed",
                        "sequence_number": 3,
                        "response": api_result(
                            "A later terminal must not be accepted."
                        ).model_dump(),
                    }
                )

        def close(self) -> None:
            self.closed = True

    body = Body()
    with OpenAI(
        api_key="unit-test-key",
        max_retries=0,
        http_client=httpx.Client(
            transport=httpx.MockTransport(
                lambda _: httpx.Response(
                    200, headers={"Content-Type": "text/event-stream"}, stream=body
                )
            )
        ),
    ) as client:
        with pytest.raises(CompositionError) as raised:
            generate_composition(request, client=client, on_reasoning=observed.append)
    assert "secret-marker" not in str(raised.value)
    assert observed[0]["delta"] == "An observed partial summary."
    assert body.closed


def test_nonstream_record_captures_summaries_without_progress_callback(
    request_packet: dict[str, Any], candidate: str
) -> None:
    client = MagicMock(spec=OpenAI)
    client.responses.create.return_value = _result_with_summaries(candidate)
    observed: list[dict[str, Any]] = []
    record = generate_composition(
        request_packet, client=client, on_reasoning=observed.append
    )
    assert observed == []
    assert len(record["api_response"]["reasoning_summaries"]) == 2
    assert record["composition"]["response"] == candidate
    client.responses.create.assert_called_once_with(**request_packet["api_request"])


def test_stream_with_no_summary_does_not_invent_progress(candidate: str) -> None:
    request = build_composition_request(
        build_behaviour_fact_packet("#d9a6a1"), "test-model", stream=True
    )
    terminal = {
        "type": "response.completed",
        "sequence_number": 1,
        "response": api_result(candidate).model_dump(),
    }
    observed: list[dict[str, Any]] = []
    with OpenAI(
        api_key="unit-test-key",
        http_client=httpx.Client(
            transport=httpx.MockTransport(
                lambda _: httpx.Response(
                    200,
                    headers={"Content-Type": "text/event-stream"},
                    content=_sse(terminal),
                )
            )
        ),
    ) as client:
        record = generate_composition(
            request, client=client, on_reasoning=observed.append
        )
    assert observed == []
    assert record["api_response"]["reasoning_summaries"] == []
    assert record["composition"]["response"] == candidate
