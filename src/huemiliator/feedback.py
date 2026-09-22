"""Freeze attributed pulse observations for Hugh's next interaction context."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any

from huemiliator.behaviour_db import DEFAULT_DB, _check_schema, _connect

SCHEMA = "huemiliator.pulse_feedback.v1"


def digest(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def _read_pulse(
    source_pulse: Path,
    db_path: Path = DEFAULT_DB,
    *,
    evaluator: str = "primary assistant",
) -> dict[str, Any]:
    """Read a completed pulse and its latest attributed judgments without writes."""
    manifest = json.loads((source_pulse / "manifest.json").read_bytes())
    finished = json.loads((source_pulse / "finished.json").read_bytes())
    cases = manifest["cases"]
    if not cases or finished["responses"] != len(cases):
        raise ValueError("Feedback needs a completed pulse with preserved responses.")
    entries = []
    with closing(_connect(db_path, readonly=True)) as conn:
        _check_schema(conn)
        conn.execute("BEGIN")
        for case in cases:
            row = conn.execute(
                """SELECT o.*, j.id AS judgment_id, j.verdict, j.note,
                          j.source AS judgment_source, j.source_event_json,
                          j.created_at AS judged_at
                   FROM eval_outputs o
                   JOIN latest_judgments j ON j.output_id = o.id
                   WHERE o.run_id = ? AND o.case_id = ? AND j.evaluator = ?""",
                (manifest["run_id"], case["case_id"], evaluator),
            ).fetchone()
            if row is None:
                raise ValueError(f"Missing {evaluator} judgment: {case['case_id']}.")
            raw = (source_pulse / case["record_file"]).read_bytes()
            record_hash = hashlib.sha256(raw).hexdigest()
            if (
                record_hash != case["record_sha256"]
                or record_hash != row["source_sha256"]
                or raw != row["record_json"]
            ):
                raise ValueError(f"Feedback source changed: {case['case_id']}.")
            entries.append(
                {
                    "output_id": row["id"],
                    "run_id": row["run_id"],
                    "case_id": row["case_id"],
                    "family": row["family"],
                    "replacement_name": row["replacement_name"],
                    "response": row["response_text"],
                    "record_sha256": record_hash,
                    "source_path": row["source_path"],
                    "judgment_id": row["judgment_id"],
                    "judgment_sha256": hashlib.sha256(
                        row["source_event_json"]
                    ).hexdigest(),
                    "judgment_source": row["judgment_source"],
                    "judged_at": row["judged_at"],
                    "verdict": row["verdict"],
                    "observation": row["note"],
                }
            )
    return {
        "run_id": manifest["run_id"],
        "finished_sha256": hashlib.sha256(
            (source_pulse / "finished.json").read_bytes()
        ).hexdigest(),
        "entries": entries,
    }


def freeze_feedback(
    source_pulses: list[Path],
    db_path: Path = DEFAULT_DB,
    *,
    evaluator: str = "primary assistant",
    observation_output_ids: list[int] | None = None,
) -> dict[str, Any]:
    """Freeze selected observations; selection is the primary's pulse-boundary work."""
    sources = [
        _read_pulse(path, db_path, evaluator=evaluator) for path in source_pulses
    ]
    entries = [entry for source in sources for entry in source.pop("entries")]
    if len({entry["output_id"] for entry in entries}) != len(entries):
        raise ValueError("Select each source pulse once.")
    selected = (
        [entry["output_id"] for entry in entries if entry["observation"].strip()]
        if observation_output_ids is None
        else observation_output_ids
    )
    body = {
        "schema": SCHEMA,
        "sources": sources,
        "evaluator": evaluator,
        "observation_output_ids": selected,
        "entries": entries,
    }
    snapshot = {**body, "snapshot_sha256": digest(body)}
    validate_feedback(snapshot)
    return snapshot


def validate_feedback(snapshot: dict[str, Any]) -> None:
    """Check the frozen payload before including its observations in a request."""
    body = {k: v for k, v in snapshot.items() if k != "snapshot_sha256"}
    if body.get("schema") != SCHEMA or digest(body) != snapshot.get("snapshot_sha256"):
        raise ValueError("Feedback snapshot schema or hash mismatch.")
    if not body.get("sources") or not body.get("evaluator"):
        raise ValueError("Feedback needs a source run and attributed evaluator.")
    entries = body.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Feedback needs preserved judgment entries.")
    for entry in entries:
        if (
            not isinstance(entry, dict)
            or entry.get("verdict") not in {"pass", "fail"}
            or not isinstance(entry.get("observation"), str)
            or not all(
                entry.get(key)
                for key in (
                    "output_id",
                    "run_id",
                    "case_id",
                    "family",
                    "replacement_name",
                    "record_sha256",
                    "judgment_id",
                    "judgment_sha256",
                )
            )
        ):
            raise ValueError("Invalid attributed feedback entry.")
    selected = body.get("observation_output_ids")
    available = {
        entry["output_id"] for entry in entries if entry["observation"].strip()
    }
    if (
        not isinstance(selected, list)
        or not all(isinstance(item, int) for item in selected)
        or len(set(selected)) != len(selected)
        or not set(selected).issubset(available)
    ):
        raise ValueError("Select unique output IDs with recorded observations.")


def load_feedback(path: Path) -> dict[str, Any]:
    snapshot = json.loads(path.read_bytes())
    if not isinstance(snapshot, dict):
        raise ValueError("Expected a feedback snapshot object.")
    validate_feedback(snapshot)
    return snapshot


def feedback_context(snapshot: dict[str, Any]) -> dict[str, Any]:
    """Expose exact observations with their prior colour context, not full answers."""
    validate_feedback(snapshot)
    return {
        "context": (
            "These attributed observations concern Hugh's earlier picker responses. "
            "Use their meaning to develop the current response in Hugh's own words. "
            "The current picker facts identify the colours for this interaction."
        ),
        "source_run_ids": [source["run_id"] for source in snapshot["sources"]],
        "snapshot_sha256": snapshot["snapshot_sha256"],
        "evaluator": snapshot["evaluator"],
        "observations": [
            {
                key: entry[key]
                for key in (
                    "output_id",
                    "run_id",
                    "case_id",
                    "family",
                    "replacement_name",
                    "verdict",
                    "observation",
                )
            }
            for entry in snapshot["entries"]
            if entry["output_id"] in snapshot["observation_output_ids"]
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_pulses", type=Path, nargs="+")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--evaluator", default="primary assistant")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--observation-output-id", type=int, action="append")
    args = parser.parse_args()
    try:
        snapshot = freeze_feedback(
            args.source_pulses,
            args.db,
            evaluator=args.evaluator,
            observation_output_ids=args.observation_output_id,
        )
        with args.output.open("x") as handle:
            json.dump(snapshot, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(json.dumps({"snapshot_sha256": snapshot["snapshot_sha256"]}))
    except (OSError, ValueError, KeyError, sqlite3.Error) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
