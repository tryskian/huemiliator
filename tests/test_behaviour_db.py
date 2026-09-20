from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

import pytest

from huemiliator.behaviour_db import import_mini, init_db, judge_output

V1_FIXTURE = Path(__file__).parent / "fixtures/composition_record_v1.json"


@pytest.fixture
def mini(tmp_path: Path) -> Path:
    run = tmp_path / "mini"
    run.mkdir()
    # Frozen with composer 0.4.0; later builders must not rewrite the v1 contract.
    raw = V1_FIXTURE.read_bytes()
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


@pytest.fixture
def mixed_mini(mini: Path) -> Path:
    legacy = json.loads(V1_FIXTURE.read_bytes())
    material = json.loads(legacy["request"]["api_request"]["input"])
    material = {
        key: material[key]
        for key in ("input", "runtime_facts", "context", "display_swatches")
    }
    api_request = {
        "model": "gpt-5.6-luna",
        "reasoning": {"effort": "medium"},
        "instructions": "Synthetic test directions; Hugh owns the wording.",
        "input": json.dumps(material, ensure_ascii=False),
        "text": {"format": {"type": "text"}, "verbosity": "low"},
        "top_p": 0.98,
        "store": False,
    }
    response = "Red, a commanding choice.\nAsh rose has a cultivated warmth.  "
    record = {
        "schema": "huemiliator.composition_record.v2",
        "request": {
            "schema": "huemiliator.composition_request.v2",
            "composer_version": "0.5.0",
            "instructions_version": "2.0.0",
            "api_request": api_request,
            "request_sha256": hashlib.sha256(
                json.dumps(
                    api_request,
                    sort_keys=True,
                    ensure_ascii=False,
                    separators=(",", ":"),
                ).encode()
            ).hexdigest(),
            "display_swatches": material["display_swatches"],
        },
        "composition": {"response": response},
        "api_response": {"output_text": response},
        "completed_at": "2026-09-20T12:00:00+00:00",
        "mechanical_checks": {"ok": True, "issues": []},
        "behaviour_verdict": None,
    }
    raw = (json.dumps(record, ensure_ascii=False, indent=2) + "\n").encode()
    (mini / "bank-free.record.json").write_bytes(raw)
    manifest = json.loads((mini / "manifest.json").read_bytes())
    manifest["cases"].append(
        {
            "case_id": "bank-free",
            "record_file": "bank-free.record.json",
            "record_sha256": hashlib.sha256(raw).hexdigest(),
        }
    )
    (mini / "manifest.json").write_text(json.dumps(manifest))
    return mini


def test_mixed_versions_preserve_bytes_settings_and_pending_judgments(
    mixed_mini: Path, tmp_path: Path
) -> None:
    db = tmp_path / "behaviour.sqlite"
    ids = import_mini(mixed_mini, db)
    before = db.read_bytes()
    assert import_mini(mixed_mini, db) == ids
    assert db.read_bytes() == before
    with sqlite3.connect(db) as conn:
        assert conn.execute("PRAGMA user_version").fetchone()[0] == 1
        outputs = conn.execute(
            """SELECT record_json, source_sha256, bank_version, response_text
            FROM eval_outputs ORDER BY id"""
        ).fetchall()
        for output, filename in zip(
            outputs, ("red.record.json", "bank-free.record.json"), strict=True
        ):
            raw = (mixed_mini / filename).read_bytes()
            assert output[:2] == (raw, hashlib.sha256(raw).hexdigest())
        assert outputs[0][2] == "0.5.1"
        assert outputs[1][2] == "not applicable"
        record = json.loads(outputs[1][0])
        assert "bank_version" not in record["request"]
        assert outputs[1][3] == record["api_response"]["output_text"]
        assert outputs[1][3].endswith("  ")
        assert record["request"]["api_request"]["text"]["verbosity"] == "low"
        assert record["request"]["api_request"]["top_p"] == 0.98
        assert record["behaviour_verdict"] is None
        assert conn.execute(
            "SELECT output_id, evaluator, verdict FROM latest_judgments"
        ).fetchall() == [(ids[0], "Peanut", "fail")]
        assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    judge_output(
        db,
        ids[1],
        "fail",
        evaluator="Peanut",
        note="Exact v2 judgment.",
        source="Synthetic test judgment",
    )
    with sqlite3.connect(db) as conn:
        assert (
            conn.execute(
                "SELECT record_json, source_sha256, bank_version, response_text "
                "FROM eval_outputs ORDER BY id"
            ).fetchall()
            == outputs
        )
        assert conn.execute(
            "SELECT output_id, evaluator, verdict, note "
            "FROM latest_judgments ORDER BY output_id"
        ).fetchall() == [
            (ids[0], "Peanut", "fail", "My exact reason.\nSecond line."),
            (ids[1], "Peanut", "fail", "Exact v2 judgment."),
        ]


def test_mixed_import_conflict_rolls_back_new_rows(
    mixed_mini: Path, tmp_path: Path
) -> None:
    db = tmp_path / "behaviour.sqlite"
    manifest_path = mixed_mini / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    first_case, new_case = manifest["cases"]
    manifest_path.write_text(json.dumps({**manifest, "cases": [first_case]}))
    import_mini(mixed_mini, db)
    before = db.read_bytes()
    changed = (mixed_mini / "red.record.json").read_bytes() + b"\n"
    (mixed_mini / "red.record.json").write_bytes(changed)
    first_case["record_sha256"] = hashlib.sha256(changed).hexdigest()
    manifest_path.write_text(json.dumps({**manifest, "cases": [new_case, first_case]}))
    with pytest.raises(ValueError, match="Original record changed"):
        import_mini(mixed_mini, db)
    assert db.read_bytes() == before


def test_unknown_record_version_is_rejected(mini: Path, tmp_path: Path) -> None:
    path = mini / "red.record.json"
    record = json.loads(path.read_bytes())
    record["schema"] = "huemiliator.composition_record.v3"
    raw = json.dumps(record).encode()
    path.write_bytes(raw)
    manifest_path = mini / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["cases"][0]["record_sha256"] = hashlib.sha256(raw).hexdigest()
    manifest_path.write_text(json.dumps(manifest))
    db = tmp_path / "behaviour.sqlite"
    with pytest.raises(ValueError, match="composition_record.v1 or v2"):
        import_mini(mini, db)
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM eval_outputs").fetchone()[0] == 0


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
