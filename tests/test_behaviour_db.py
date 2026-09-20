from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

import pytest

from huemiliator.behaviour_db import import_mini, init_db, judge_output
from huemiliator.composition import build_composition_request
from huemiliator.main import build_behaviour_fact_packet


@pytest.fixture
def mini(tmp_path: Path) -> Path:
    run = tmp_path / "mini"
    run.mkdir()
    record = {
        "schema": "huemiliator.composition_record.v1",
        "request": build_composition_request(
            build_behaviour_fact_packet("#d9a6a1"), "test-model"
        ),
        "composition": {"response": "Original failed output: #b5817d"},
        "api_response": {"output_text": "original API output"},
        "completed_at": "2026-09-19T12:00:00+00:00",
        "mechanical_checks": {"ok": False, "issues": ["Visible hex"]},
        "behaviour_verdict": None,
    }
    raw = (json.dumps(record, indent=3) + "\n").encode()
    (run / "red.record.json").write_bytes(raw)
    (run / "manifest.json").write_text(
        json.dumps(
            {
                "run_id": "test-mini",
                "cases": [
                    {
                        "case_id": "red",
                        "record_file": "red.record.json",
                        "record_sha256": hashlib.sha256(raw).hexdigest(),
                    }
                ],
            }
        )
    )
    event = {
        "event_id": "peanut-001",
        "evaluator": "Peanut",
        "verdict": "FAIL",
        "source_text": "My exact reason.\nSecond line.",
        "source": "User message",
        "recorded_at": "2026-09-19T12:01:00+00:00",
        "case_ids": ["red"],
        "record_sha256": {"red.record.json": hashlib.sha256(raw).hexdigest()},
    }
    (run / "judgments.jsonl").write_text(json.dumps(event) + "\n")
    return run


def test_import_preserves_failure_bytes_and_attribution_idempotently(
    mini: Path,
    tmp_path: Path,
) -> None:
    db = tmp_path / "behaviour.sqlite"
    ids = import_mini(mini, db)
    first_bytes = db.read_bytes()
    assert import_mini(mini, db) == ids
    assert db.read_bytes() == first_bytes
    with sqlite3.connect(db) as conn:
        output = conn.execute(
            "SELECT record_json, mechanical_ok, response_text FROM eval_outputs"
        ).fetchone()
        assert output == (
            (mini / "red.record.json").read_bytes(),
            0,
            "Original failed output: #b5817d",
        )
        judgment = conn.execute(
            "SELECT evaluator, verdict, note, source_event_json FROM eval_judgments"
        ).fetchone()
        assert judgment == (
            "Peanut",
            "fail",
            "My exact reason.\nSecond line.",
            (mini / "judgments.jsonl").read_bytes(),
        )
        assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"


def test_history_is_append_only_and_latest_is_per_evaluator(
    mini: Path,
    tmp_path: Path,
) -> None:
    db = tmp_path / "behaviour.sqlite"
    output_id = import_mini(mini, db)[0]
    judge_output(
        db,
        output_id,
        "pass",
        evaluator="primary assistant",
        note="Assistant reason",
        source="Assistant message",
    )
    judge_output(
        db,
        output_id,
        "pass",
        evaluator="Peanut",
        note="Revised judgment",
        source="Later user message",
    )
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM eval_judgments").fetchone()[0] == 3
        assert conn.execute(
            "SELECT evaluator, verdict FROM latest_judgments ORDER BY evaluator"
        ).fetchall() == [("Peanut", "pass"), ("primary assistant", "pass")]
        for table in ("eval_outputs", "eval_judgments"):
            with pytest.raises(sqlite3.IntegrityError):
                conn.execute(f"DELETE FROM {table}")
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute("UPDATE eval_outputs SET response_text='rewritten'")
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute("UPDATE eval_judgments SET note='rewritten'")


def test_import_rejects_conflicts_and_rolls_back_the_entire_batch(
    mini: Path,
    tmp_path: Path,
) -> None:
    db = tmp_path / "behaviour.sqlite"
    event = json.loads((mini / "judgments.jsonl").read_text())
    event["record_sha256"]["red.record.json"] = "incorrect"
    (mini / "judgments.jsonl").write_text(json.dumps(event) + "\n")
    with pytest.raises(ValueError, match="hash mismatch"):
        import_mini(mini, db)
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM eval_outputs").fetchone()[0] == 0


def test_existing_colour_database_is_rejected_unchanged(tmp_path: Path) -> None:
    db = tmp_path / "colour.sqlite"
    with sqlite3.connect(db) as conn:
        conn.execute("CREATE TABLE eval_outputs (id INTEGER PRIMARY KEY)")
    original = db.read_bytes()
    with pytest.raises(ValueError, match="Expected a Huey behaviour database"):
        init_db(db)
    assert db.read_bytes() == original


def test_empty_ledger_leaves_all_evaluators_pending(mini: Path, tmp_path: Path) -> None:
    (mini / "judgments.jsonl").write_text("")
    db = tmp_path / "behaviour.sqlite"
    import_mini(mini, db)
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM latest_judgments").fetchone()[0] == 0


def test_invalid_judgment_does_not_change_history(mini: Path, tmp_path: Path) -> None:
    db = tmp_path / "behaviour.sqlite"
    output_id = import_mini(mini, db)[0]
    before = db.read_bytes()
    with pytest.raises(ValueError, match="evaluator, source"):
        judge_output(db, output_id, "pass", evaluator="Peanut", note="", source="")
    assert db.read_bytes() == before
