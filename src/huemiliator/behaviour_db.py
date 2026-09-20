"""Saved composition records and attributed judgment history for local review."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from huemiliator.config import SOURCE_ROOT

DEFAULT_DB = SOURCE_ROOT / ".local/behaviour.sqlite"
APPLICATION_ID = 1213547842
SCHEMA_VERSION = 1
SCHEMA = """
CREATE TABLE eval_outputs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    case_id TEXT NOT NULL,
    input_hex TEXT NOT NULL,
    family TEXT NOT NULL,
    replacement_name TEXT NOT NULL,
    replacement_hex TEXT NOT NULL,
    response_text TEXT,
    model TEXT NOT NULL,
    reasoning_effort TEXT NOT NULL,
    instructions_version TEXT NOT NULL,
    bank_version TEXT NOT NULL,
    mechanical_ok INTEGER NOT NULL CHECK (mechanical_ok IN (0, 1)),
    source_path TEXT NOT NULL,
    source_sha256 TEXT NOT NULL UNIQUE,
    record_json BLOB NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE (run_id, case_id)
);
CREATE TABLE eval_judgments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    output_id INTEGER NOT NULL REFERENCES eval_outputs(id) ON DELETE RESTRICT,
    evaluator TEXT NOT NULL CHECK (length(trim(evaluator)) > 0),
    verdict TEXT NOT NULL CHECK (verdict IN ('pass', 'fail')),
    note TEXT NOT NULL,
    source TEXT NOT NULL CHECK (length(trim(source)) > 0),
    event_id TEXT NOT NULL,
    source_event_json BLOB NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE (output_id, evaluator, event_id)
);
CREATE VIEW latest_judgments AS
SELECT j.* FROM eval_judgments j
WHERE j.id = (
    SELECT MAX(newer.id) FROM eval_judgments newer
    WHERE newer.output_id = j.output_id AND newer.evaluator = j.evaluator
);
CREATE TRIGGER preserve_output_update BEFORE UPDATE ON eval_outputs
BEGIN SELECT RAISE(ABORT, 'Original outputs are immutable'); END;
CREATE TRIGGER preserve_output_delete BEFORE DELETE ON eval_outputs
BEGIN SELECT RAISE(ABORT, 'Original outputs are immutable'); END;
CREATE TRIGGER preserve_judgment_update BEFORE UPDATE ON eval_judgments
BEGIN SELECT RAISE(ABORT, 'Append a new attributed judgment'); END;
CREATE TRIGGER preserve_judgment_delete BEFORE DELETE ON eval_judgments
BEGIN SELECT RAISE(ABORT, 'Append a new attributed judgment'); END;
"""


def _connect(path: Path, *, readonly: bool = False) -> sqlite3.Connection:
    mode = "ro" if readonly else "rw"
    conn = sqlite3.connect(path.resolve().as_uri() + f"?mode={mode}", uri=True)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _check_schema(conn: sqlite3.Connection) -> None:
    if (
        conn.execute("PRAGMA application_id").fetchone()[0] != APPLICATION_ID
        or conn.execute("PRAGMA user_version").fetchone()[0] != SCHEMA_VERSION
    ):
        raise ValueError("Expected a Huey behaviour database, schema version 1.")


def init_db(path: Path = DEFAULT_DB) -> Path:
    """Create a behaviour database, or validate an existing one unchanged."""
    if path.exists():
        with closing(_connect(path, readonly=True)) as conn:
            _check_schema(conn)
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(path)) as conn:
        conn.executescript(
            f"BEGIN; {SCHEMA}\nPRAGMA application_id = {APPLICATION_ID};"
            f"PRAGMA user_version = {SCHEMA_VERSION}; COMMIT;"
        )
    return path


def _insert_output(
    conn: sqlite3.Connection, run_id: str, case_id: str, path: Path, raw: bytes
) -> int:
    record = json.loads(raw)
    if record["schema"] != "huemiliator.composition_record.v1":
        raise ValueError("Expected an original composition_record.v1 record.")
    request = record["request"]
    material = json.loads(request["api_request"]["input"])
    facts = material["runtime_facts"]
    digest = hashlib.sha256(raw).hexdigest()
    existing = conn.execute(
        "SELECT id, source_sha256 FROM eval_outputs WHERE run_id=? AND case_id=?",
        (run_id, case_id),
    ).fetchone()
    if existing is not None:
        if existing["source_sha256"] != digest:
            raise ValueError(f"Original record changed for {run_id}/{case_id}.")
        return int(existing["id"])
    source_path = path.resolve()
    if SOURCE_ROOT in source_path.parents:
        source_path = source_path.relative_to(SOURCE_ROOT)
    composition = record["composition"]
    # Malformed or incomplete returned output remains evidence, too.
    response = composition.get("response") if isinstance(composition, dict) else None
    cursor = conn.execute(
        """INSERT INTO eval_outputs (
            run_id, case_id, input_hex, family, replacement_name, replacement_hex,
            response_text, model, reasoning_effort, instructions_version,
            bank_version, mechanical_ok, source_path, source_sha256, record_json,
            created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            run_id,
            case_id,
            material["input"]["hex"],
            facts["family"],
            facts["replacement"]["name"],
            facts["replacement"]["hex"],
            response if isinstance(response, str) else None,
            request["api_request"]["model"],
            request["api_request"]["reasoning"]["effort"],
            request["instructions_version"],
            request["bank_version"],
            int(record["mechanical_checks"]["ok"]),
            str(source_path),
            digest,
            raw,
            record["completed_at"],
        ),
    )
    assert cursor.lastrowid is not None
    return cursor.lastrowid


def _insert_judgment(
    conn: sqlite3.Connection, output_id: int, event: dict[str, Any], raw: bytes
) -> int:
    evaluator = event["evaluator"]
    source = event["source"]
    verdict = event["verdict"].lower()
    if not evaluator.strip() or not source.strip() or verdict not in {"pass", "fail"}:
        raise ValueError("Judgment needs evaluator, source and pass/fail verdict.")
    existing = conn.execute(
        """SELECT id, source_event_json FROM eval_judgments
        WHERE output_id=? AND evaluator=? AND event_id=?""",
        (output_id, evaluator, event["event_id"]),
    ).fetchone()
    if existing is not None:
        if existing["source_event_json"] != raw:
            raise ValueError("Judgment event changed; append a new event instead.")
        return int(existing["id"])
    cursor = conn.execute(
        """INSERT INTO eval_judgments (
            output_id, evaluator, verdict, note, source, event_id,
            source_event_json, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            output_id,
            evaluator,
            verdict,
            event.get("source_text", event.get("reason", "")),
            source,
            event["event_id"],
            raw,
            event["recorded_at"],
        ),
    )
    assert cursor.lastrowid is not None
    return cursor.lastrowid


def import_mini(run_dir: Path, db_path: Path = DEFAULT_DB) -> list[int]:
    """Import a saved mini and its ledger atomically; repeat imports are idempotent."""
    manifest = json.loads((run_dir / "manifest.json").read_bytes())
    records = []
    for case in manifest["cases"]:
        path = run_dir / case["record_file"]
        raw = path.read_bytes()
        expected = case.get("record_sha256")
        if expected is not None and hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError(f"Record hash mismatch for {case['case_id']}.")
        records.append((case["case_id"], path, raw))
    ledger = run_dir / "judgments.jsonl"
    events = (
        [
            (json.loads(raw), raw)
            for raw in ledger.read_bytes().splitlines(keepends=True)
            if raw.strip()
        ]
        if ledger.exists()
        else []
    )
    init_db(db_path)
    with closing(_connect(db_path)) as conn, conn:
        _check_schema(conn)
        ids = {
            case_id: _insert_output(conn, manifest["run_id"], case_id, path, raw)
            for case_id, path, raw in records
        }
        hashes = {
            path.name: hashlib.sha256(raw).hexdigest() for _, path, raw in records
        }
        for event, raw in events:
            for name, expected in event.get("record_sha256", {}).items():
                if hashes.get(name) != expected:
                    raise ValueError("Judgment source record hash mismatch.")
            for case_id in event["case_ids"]:
                _insert_judgment(conn, ids[case_id], event, raw)
        return list(ids.values())


def judge_output(
    db_path: Path,
    output_id: int,
    verdict: str,
    *,
    evaluator: str,
    note: str,
    source: str,
) -> int:
    """Append the evaluator's supplied judgment; preserve previous judgments."""
    event = {
        "event_id": str(uuid4()),
        "evaluator": evaluator,
        "verdict": verdict,
        "source_text": note,
        "source": source,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
    raw = (json.dumps(event, ensure_ascii=False) + "\n").encode()
    with closing(_connect(db_path)) as conn, conn:
        _check_schema(conn)
        return _insert_judgment(conn, output_id, event, raw)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    commands = parser.add_subparsers(dest="command", required=True)
    importer = commands.add_parser("import", help="Import an existing mini receipt.")
    importer.add_argument("run_dir", type=Path)
    judge = commands.add_parser("judge", help="Append a supplied attributed judgment.")
    judge.add_argument("output_id", type=int)
    judge.add_argument("verdict", choices=("pass", "fail"))
    judge.add_argument("--evaluator", required=True)
    judge.add_argument("--note", required=True)
    judge.add_argument("--source", required=True)
    args = parser.parse_args()
    try:
        if args.command == "import":
            print({"output_ids": import_mini(args.run_dir, args.db)})
        else:
            print(
                {
                    "judgment_id": judge_output(
                        args.db,
                        args.output_id,
                        args.verdict,
                        evaluator=args.evaluator,
                        note=args.note,
                        source=args.source,
                    )
                }
            )
    except (OSError, ValueError, KeyError, sqlite3.Error) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
