from __future__ import annotations

import copy
import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any
from unittest.mock import patch

import httpx
import pytest
from openai import OpenAI

from huemiliator import behaviour_pulse as pulse
from huemiliator.agent import COMPOSITION_INSTRUCTIONS
from huemiliator.behaviour_db import import_mini, judge_output
from huemiliator.composition import build_composition_request
from huemiliator.feedback import (
    feedback_context,
    freeze_feedback,
    load_feedback,
    validate_feedback,
)
from huemiliator.main import build_behaviour_fact_packet, main


def save(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


@pytest.fixture
def source(tmp_path: Path) -> tuple[Path, Path, list[int]]:
    directory = tmp_path / "source-pulse"
    directory.mkdir()
    manifest: dict[str, Any] = {"run_id": "source-pulse", "cases": []}
    for case, colour in (("pink", "#ffc0cb"), ("green", "#7fff00")):
        request = build_composition_request(build_behaviour_fact_packet(colour), "test")
        text = f"  Synthetic {case} response with its own wording.\n"
        record = {
            "schema": "huemiliator.composition_record.v2",
            "request": request,
            "composition": {"response": text},
            "api_response": {"id": f"resp_{case}", "output_text": text},
            "completed_at": "2026-09-21T12:00:00+00:00",
            "mechanical_checks": {"ok": True, "issues": []},
            "behaviour_verdict": None,
        }
        path = directory / f"{case}.record.json"
        save(path, record)
        manifest["cases"].append(
            {
                "case_id": case,
                "record_file": path.name,
                "record_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    save(directory / "manifest.json", manifest)
    save(directory / "finished.json", {"responses": 2})
    db = tmp_path / "behaviour.sqlite"
    ids = import_mini(directory, db)
    for output_id, verdict, note in zip(
        ids,
        ("fail", "pass"),
        ("Synthetic observation with 'context'.", ""),
        strict=True,
    ):
        judge_output(
            db,
            output_id,
            verdict,
            evaluator="primary assistant",
            note=note,
            source="Synthetic test review",
        )
    return directory, db, ids


@pytest.fixture
def prepared(source: tuple[Path, Path, list[int]], tmp_path: Path) -> tuple[Path, Path]:
    directory, db, _ = source
    snapshot = tmp_path / "feedback.json"
    save(snapshot, freeze_feedback([directory], db))
    protocol = {
        "run_id": "next-pulse",
        "evaluator": "primary assistant",
        "settings": {
            "model": "test",
            "reasoning_effort": "medium",
            "verbosity": "low",
            "top_p": 0.98,
        },
        "limits": {
            "duration_seconds": 900,
            "max_attempts": 2,
            "spacing_seconds": 75,
            "request_timeout_seconds": 60,
            "retries": 0,
        },
        "cases": [{"case": "pink", "hex": "#ffc0cb"}],
    }
    run = tmp_path / "next-pulse"
    pulse.prepare_pulse(run, protocol, snapshot)
    return run, db


def test_snapshot_is_readonly_attributed_and_survives_later_revision(
    source: tuple[Path, Path, list[int]],
) -> None:
    directory, db, ids = source
    judge_output(
        db,
        ids[0],
        "pass",
        evaluator="Peanut",
        note="Different evaluator",
        source="Synthetic independent review",
    )
    original_db = db.read_bytes()
    snapshot = freeze_feedback([directory], db)
    assert db.read_bytes() == original_db
    original = copy.deepcopy(snapshot)
    entry = snapshot["entries"][0]
    assert entry["response"] == "  Synthetic pink response with its own wording.\n"
    assert entry["verdict"] == "fail"
    assert (
        feedback_context(snapshot)["observations"][0]["observation"]
        == "Synthetic observation with 'context'."
    )
    assert len(snapshot["entries"]) == 2
    assert len(feedback_context(snapshot)["observations"]) == 1
    judge_output(
        db,
        ids[0],
        "pass",
        evaluator="primary assistant",
        note="Revised synthetic observation",
        source="Synthetic later review",
    )
    newer = freeze_feedback([directory], db)
    assert newer["snapshot_sha256"] != snapshot["snapshot_sha256"]
    assert newer["entries"][0]["verdict"] == "pass"
    assert snapshot == original
    validate_feedback(snapshot)


def test_feedback_uses_exact_notes_without_replacing_facts_or_brief(
    source: tuple[Path, Path, list[int]],
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    directory, db, ids = source
    snapshot = freeze_feedback([directory], db, observation_output_ids=[ids[0]])
    path = tmp_path / "feedback.json"
    save(path, snapshot)
    before_db = db.read_bytes()
    with patch("huemiliator.main.generate_composition") as generate:
        assert main(["compose", "#808000", "--feedback", str(path), "--dry-run"]) == 0
        generate.assert_not_called()
    packet = json.loads(capsys.readouterr().out)
    baseline = build_composition_request(
        build_behaviour_fact_packet("#808000"), packet["api_request"]["model"]
    )
    material = json.loads(packet["api_request"]["input"])
    context = material.pop("pulse_feedback")
    assert material == json.loads(baseline["api_request"]["input"])
    assert packet["api_request"]["instructions"] == COMPOSITION_INSTRUCTIONS
    assert packet["feedback_snapshot"] == snapshot
    assert packet["request_sha256"] != baseline["request_sha256"]
    assert "Synthetic pink response" not in packet["api_request"]["input"]
    assert context["observations"][0]["verdict"] == "fail"
    assert db.read_bytes() == before_db


@pytest.mark.parametrize("damage", ["record", "pending", "unfinished", "selection"])
def test_invalid_feedback_sources_fail_without_database_writes(
    source: tuple[Path, Path, list[int]], damage: str
) -> None:
    directory, db, ids = source
    if damage == "record":
        with (directory / "pink.record.json").open("a") as handle:
            handle.write(" ")
    elif damage == "unfinished":
        (directory / "finished.json").unlink()
    before = db.read_bytes()
    with pytest.raises((ValueError, FileNotFoundError)):
        freeze_feedback(
            [directory],
            db,
            evaluator="unrecorded evaluator"
            if damage == "pending"
            else "primary assistant",
            observation_output_ids=[ids[1]] if damage == "selection" else None,
        )
    assert db.read_bytes() == before


def test_feedback_changes_are_detected(source: tuple[Path, Path, list[int]]) -> None:
    directory, db, _ = source
    snapshot = freeze_feedback([directory], db)
    snapshot["entries"][0]["observation"] = "Rewritten without preserving provenance"
    with pytest.raises(ValueError, match="hash mismatch"):
        validate_feedback(snapshot)


def response(text: str, index: int) -> dict[str, Any]:
    return {
        "id": f"resp_{index}",
        "created_at": 123,
        "model": "test",
        "object": "response",
        "status": "completed",
        "output": [
            {
                "id": f"msg_{index}",
                "type": "message",
                "role": "assistant",
                "status": "completed",
                "content": [
                    {
                        "type": "output_text",
                        "text": text,
                        "annotations": [],
                        "logprobs": [],
                    }
                ],
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


def install_clock(
    monkeypatch: pytest.MonkeyPatch, run: Path, db: Path, *, judge: bool
) -> None:
    elapsed = [0.0]
    reviewed: set[str] = set()

    def sleep(seconds: float) -> None:
        elapsed[0] += seconds
        if judge and (run / "manifest.json").exists():
            manifest = json.loads((run / "manifest.json").read_bytes())
            for case in manifest["cases"]:
                if case["case_id"] not in reviewed:
                    pulse.judge_pulse(
                        run,
                        case["case_id"],
                        "pass",
                        note="Synthetic live test judgment",
                        db_path=db,
                    )
                    reviewed.add(case["case_id"])

    monkeypatch.setattr(pulse.time, "monotonic", lambda: elapsed[0])
    monkeypatch.setattr(pulse.time, "sleep", sleep)


@pytest.mark.parametrize("judge", [True, False])
def test_pulse_preserves_feedback_and_waits_for_primary_review(
    prepared: tuple[Path, Path],
    source: tuple[Path, Path, list[int]],
    monkeypatch: pytest.MonkeyPatch,
    judge: bool,
) -> None:
    run, db = prepared
    install_clock(monkeypatch, run, db, judge=judge)
    calls: list[dict[str, Any]] = []

    def respond(request: httpx.Request) -> httpx.Response:
        api = json.loads(request.content)
        if calls:
            assert pulse._judged(db, "next-pulse", "01-pink")
            assert api == calls[0]
        calls.append(api)
        facts = json.loads(api["input"])["runtime_facts"]
        return httpx.Response(
            200,
            json=response(
                f"Synthetic reply with {facts['replacement']['name']}.", len(calls)
            ),
        )

    with OpenAI(
        api_key="unit-test-key",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    ) as client:
        finished = pulse.run_pulse(run, db, client=client)
    assert len(calls) == (2 if judge else 1)
    assert len(finished["judged_cases"]) == (2 if judge else 0)
    assert finished["elapsed_seconds"] == 900
    record = json.loads((run / "01-pink.record.json").read_bytes())
    assert record["request"]["api_request"] == calls[0]
    assert record["request"]["feedback_snapshot"] == load_feedback(
        run / "feedback.json"
    )
    assert record["behaviour_verdict"] is None
    raw = json.loads((run / "01-pink.response.json").read_bytes())
    assert (
        raw["output"][0]["content"][0]["text"] == record["api_response"]["output_text"]
    )
    if judge:
        following = freeze_feedback([run], db)
        assert len(following["entries"]) == 2
        combined = freeze_feedback(
            [source[0], run],
            db,
            observation_output_ids=[source[2][0], following["entries"][0]["output_id"]],
        )
        assert len(combined["entries"]) == 4
        selected = feedback_context(combined)["observations"]
        assert [entry["run_id"] for entry in selected] == ["source-pulse", "next-pulse"]
        with sqlite3.connect(db) as conn:
            saved = conn.execute(
                "SELECT record_json FROM eval_outputs "
                "WHERE run_id='next-pulse' ORDER BY id"
            ).fetchall()
        assert (
            json.loads(saved[0][0])["request"]["feedback_snapshot"]
            == record["request"]["feedback_snapshot"]
        )
    else:
        with pytest.raises(ValueError, match="Missing primary assistant judgment"):
            freeze_feedback([run], db)


def test_api_failure_is_preserved_without_retry_or_verdict(
    prepared: tuple[Path, Path],
) -> None:
    run, db = prepared
    before = db.read_bytes()
    calls: list[httpx.Request] = []

    def fail(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(
            401,
            json={
                "error": {
                    "message": "sensitive-provider-text",
                    "type": "authentication_error",
                }
            },
            headers={"x-request-id": "failed-request"},
        )

    with OpenAI(
        api_key="unit-test-key",
        max_retries=0,
        http_client=httpx.Client(transport=httpx.MockTransport(fail)),
    ) as client:
        finished = pulse.run_pulse(run, db, client=client)
    assert len(calls) == 1
    assert finished["responses"] == 0
    assert finished["stop_reason"] == "request_or_recording_error"
    receipt = (run / "01-pink.receipt.json").read_text()
    assert "sensitive-provider-text" not in receipt
    assert json.loads(receipt)["error"]["status_code"] == 401
    assert db.read_bytes() == before


def test_prepared_request_drift_blocks_generation(prepared: tuple[Path, Path]) -> None:
    run, db = prepared
    with (run / "01-pink.request.json").open("a") as handle:
        handle.write(" ")
    with patch("huemiliator.behaviour_pulse.OpenAI") as client:
        with pytest.raises(ValueError, match="Prepared request changed"):
            pulse.run_pulse(run, db)
        client.assert_not_called()
    assert not (run / "started.json").exists()
