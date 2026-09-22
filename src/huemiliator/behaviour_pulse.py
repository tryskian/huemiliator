"""Prepare, run and judge a pulse with frozen feedback and live primary review."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import time
from contextlib import closing, nullcontext
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, cast
from uuid import uuid4

from openai import OpenAI

from huemiliator.behaviour_db import DEFAULT_DB, _check_schema, _connect, import_mini
from huemiliator.composition import build_composition_request, generate_composition
from huemiliator.config import SOURCE_ROOT, SWATCH_SNAPSHOT_PATH, load_settings
from huemiliator.feedback import load_feedback
from huemiliator.main import build_behaviour_fact_packet


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _save(path: Path, value: Any) -> None:
    with path.open("x") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def _index(run_dir: Path, manifest: dict[str, Any]) -> None:
    temporary = run_dir / "manifest.tmp"
    temporary.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(run_dir / "manifest.json")


def _check_protocol(protocol: dict[str, Any]) -> None:
    limits = protocol["limits"]
    if (
        not protocol["run_id"]
        or protocol["evaluator"] != "primary assistant"
        or not 0 < limits["duration_seconds"] <= 900
        or not 0 < limits["max_attempts"] <= 12
        or limits["request_timeout_seconds"] != 60
        or limits["retries"] != 0
        or limits["spacing_seconds"] < 0
        or not protocol["cases"]
    ):
        raise ValueError("Expected a bounded pulse with live primary judgments.")
    for case in protocol["cases"]:
        if not re.fullmatch(r"[a-z0-9_-]+", case["case"]):
            raise ValueError("Case labels must be lowercase filename-safe names.")


def prepare_pulse(
    run_dir: Path, protocol: dict[str, Any], feedback_path: Path
) -> dict[str, Any]:
    """Freeze all requests and their feedback before any generation or judgment."""
    _check_protocol(protocol)
    feedback = load_feedback(feedback_path)
    if protocol["run_id"] in {source["run_id"] for source in feedback["sources"]}:
        raise ValueError("The next pulse needs its own run ID.")
    requests = []
    for number in range(protocol["limits"]["max_attempts"]):
        case = protocol["cases"][number % len(protocol["cases"])]
        requests.append(
            (
                f"{number + 1:02d}-{case['case']}",
                build_composition_request(
                    build_behaviour_fact_packet(case["hex"]),
                    **protocol["settings"],
                    feedback=feedback,
                ),
            )
        )
    run_dir.mkdir(parents=True, exist_ok=False)
    _save(run_dir / "protocol.json", protocol)
    _save(run_dir / "feedback.json", feedback)
    prepared: dict[str, Any] = {
        "schema": "huemiliator.prepared_pulse.v1",
        "protocol_sha256": _hash(run_dir / "protocol.json"),
        "feedback_sha256": _hash(run_dir / "feedback.json"),
        "feedback_snapshot_sha256": feedback["snapshot_sha256"],
        "source_hashes": {
            str(path.relative_to(SOURCE_ROOT)): _hash(path)
            for path in [
                *sorted((SOURCE_ROOT / "src/huemiliator").glob("*.py")),
                SWATCH_SNAPSHOT_PATH,
            ]
        },
        "requests": [],
    }
    for case_id, request in requests:
        path = run_dir / f"{case_id}.request.json"
        _save(path, request)
        prepared["requests"].append(
            {"case_id": case_id, "request_file": path.name, "sha256": _hash(path)}
        )
    _save(run_dir / "prepared.json", prepared)
    return prepared


def verify_pulse(run_dir: Path) -> dict[str, Any]:
    prepared = json.loads((run_dir / "prepared.json").read_bytes())
    for name in ("protocol", "feedback"):
        if _hash(run_dir / f"{name}.json") != prepared[f"{name}_sha256"]:
            raise ValueError(f"Prepared {name} changed; prepare a new pulse.")
    for path, expected in prepared["source_hashes"].items():
        if _hash(SOURCE_ROOT / path) != expected:
            raise ValueError(f"Runtime source changed: {path}; prepare a new pulse.")
    for request in prepared["requests"]:
        if _hash(run_dir / request["request_file"]) != request["sha256"]:
            raise ValueError(f"Prepared request changed: {request['case_id']}.")
    return prepared


def _judged(db_path: Path, run_id: str, case_id: str) -> bool:
    if not db_path.exists():
        return False
    with closing(_connect(db_path, readonly=True)) as conn:
        return (
            conn.execute(
                """SELECT 1 FROM eval_outputs o
               JOIN latest_judgments j ON j.output_id=o.id
               WHERE o.run_id=? AND o.case_id=? AND j.evaluator='primary assistant'""",
                (run_id, case_id),
            ).fetchone()
            is not None
        )


class _Capture:
    def __init__(self, client: OpenAI, run_dir: Path, case_id: str) -> None:
        self.client = client
        self.path = run_dir / f"{case_id}.response.json"
        self.responses = self
        self.metadata: dict[str, Any] = {}

    def create(self, **request: Any) -> Any:
        try:
            raw = self.client.responses.with_raw_response.create(**request)
        except Exception as error:
            self.metadata["error"] = {
                "type": type(error).__name__,
                "status_code": getattr(error, "status_code", None),
                "request_id": getattr(error, "request_id", None),
            }
            raise
        with self.path.open("xb") as handle:
            handle.write(raw.content)
        self.metadata = {
            "response_file": self.path.name,
            "response_sha256": _hash(self.path),
            "request_id": raw.headers.get("x-request-id"),
        }
        return raw.parse()


def _attempt(
    client: OpenAI, run_dir: Path, item: dict[str, Any], elapsed: float
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    request = json.loads((run_dir / item["request_file"]).read_bytes())
    capture = _Capture(client, run_dir, item["case_id"])
    receipt: dict[str, Any] = {
        "case_id": item["case_id"],
        "started_at": _now(),
        "pulse_elapsed_seconds": elapsed,
        "request_file": item["request_file"],
        "record_file": None,
    }
    record = None
    try:
        record = generate_composition(request, client=cast(OpenAI, capture))
        path = run_dir / f"{item['case_id']}.record.json"
        _save(path, record)
        receipt.update(
            record_file=path.name,
            record_sha256=_hash(path),
            response_id=record["api_response"]["id"],
            mechanical_ok=record["mechanical_checks"]["ok"],
        )
    except Exception as error:
        # Provider text can include credentials; preserve safe failure metadata only.
        receipt["error"] = {"type": type(error).__name__}
        record = None
    finally:
        receipt.update(capture.metadata)
        receipt["completed_at"] = _now()
        _save(run_dir / f"{item['case_id']}.receipt.json", receipt)
    return receipt, record


def run_pulse(
    run_dir: Path, db_path: Path = DEFAULT_DB, *, client: OpenAI | None = None
) -> dict[str, Any]:
    """Run frozen requests, waiting for an imported primary verdict between them."""
    prepared = verify_pulse(run_dir)
    protocol = json.loads((run_dir / "protocol.json").read_bytes())
    if (run_dir / "started.json").exists():
        raise ValueError("Pulse already started; its evidence remains preserved.")
    if db_path.exists():
        with closing(_connect(db_path, readonly=True)) as conn:
            _check_schema(conn)
            if conn.execute(
                "SELECT 1 FROM eval_outputs WHERE run_id=?", (protocol["run_id"],)
            ).fetchone():
                raise ValueError("Run ID already has saved outputs; use a new run ID.")
    limits = protocol["limits"]
    load_settings()
    connection = (
        nullcontext(client)
        if client is not None
        else OpenAI(timeout=limits["request_timeout_seconds"], max_retries=0)
    )
    with connection as active_client:
        manifest: dict[str, Any] = {
            "run_id": protocol["run_id"],
            "schema": "huemiliator.pulse_manifest.v1",
            "protocol_file": "protocol.json",
            "protocol_sha256": prepared["protocol_sha256"],
            "feedback_file": "feedback.json",
            "feedback_sha256": prepared["feedback_sha256"],
            "cases": [],
            "attempts": [],
        }
        start = time.monotonic()
        deadline = start + limits["duration_seconds"]
        _save(
            run_dir / "started.json",
            {"started_at": _now(), "duration_seconds": limits["duration_seconds"]},
        )
        _index(run_dir, manifest)
        stop = "deadline_reached"
        previous = None
        try:
            for number, item in enumerate(prepared["requests"]):
                scheduled = start + number * limits["spacing_seconds"]
                while time.monotonic() < deadline:
                    if (run_dir / "STOP").exists():
                        stop = "operator_stopped"
                        break
                    if time.monotonic() >= scheduled and (
                        previous is None
                        or _judged(db_path, protocol["run_id"], previous)
                    ):
                        break
                    time.sleep(0.5)
                if stop == "operator_stopped":
                    break
                if deadline - time.monotonic() < limits["request_timeout_seconds"]:
                    stop = "insufficient_request_window"
                    break
                receipt, record = _attempt(
                    active_client, run_dir, item, round(time.monotonic() - start, 3)
                )
                manifest["attempts"].append(receipt)
                if record is not None:
                    manifest["cases"].append(
                        {
                            key: receipt[key]
                            for key in ("case_id", "record_file", "record_sha256")
                        }
                    )
                _index(run_dir, manifest)
                print(
                    json.dumps(
                        {
                            "case_id": item["case_id"],
                            "response": record["api_response"]["output_text"]
                            if record
                            else None,
                            "swatches": record["request"]["display_swatches"]
                            if record
                            else None,
                            "mechanical_checks": record["mechanical_checks"]
                            if record
                            else None,
                            "error": receipt.get("error"),
                        },
                        ensure_ascii=False,
                    ),
                    flush=True,
                )
                if record is None:
                    stop = "request_or_recording_error"
                    break
                previous = item["case_id"]
            if stop == "deadline_reached":
                while time.monotonic() < deadline and not (run_dir / "STOP").exists():
                    time.sleep(0.5)
                if (run_dir / "STOP").exists():
                    stop = "operator_stopped"
        except BaseException:
            stop = "interrupted"
            raise
        finally:
            finished = {
                "finished_at": _now(),
                "stop_reason": stop,
                "elapsed_seconds": round(time.monotonic() - start, 3),
                "attempts": len(manifest["attempts"]),
                "responses": len(manifest["cases"]),
                "judged_cases": [
                    case["case_id"]
                    for case in manifest["cases"]
                    if _judged(db_path, protocol["run_id"], case["case_id"])
                ],
            }
            _save(run_dir / "finished.json", finished)
    return finished


def judge_pulse(
    run_dir: Path,
    case_id: str,
    verdict: str,
    *,
    note: str = "",
    db_path: Path = DEFAULT_DB,
) -> list[int]:
    """Record the primary's actual judgment; no automatic behaviour verdict."""
    if verdict not in {"pass", "fail"}:
        raise ValueError("Supply pass or fail.")
    manifest = json.loads((run_dir / "manifest.json").read_bytes())
    cases = [case for case in manifest["cases"] if case["case_id"] == case_id]
    if len(cases) != 1:
        raise ValueError("Judge one recorded case from this pulse.")
    case = cases[0]
    ledger = run_dir / "judgments.jsonl"
    source = ledger.resolve()
    if source.is_relative_to(SOURCE_ROOT):
        source = source.relative_to(SOURCE_ROOT)
    event = {
        "event_id": str(uuid4()),
        "recorded_at": _now(),
        "evaluator": "primary assistant",
        "verdict": verdict,
        "source_text": note,
        "source": str(source),
        "case_ids": [case_id],
        "record_sha256": {case["record_file"]: case["record_sha256"]},
    }
    with ledger.open("a") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    return import_mini(run_dir, db_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare", help="Freeze a pulse offline.")
    prepare.add_argument("run_dir", type=Path)
    prepare.add_argument("--protocol", type=Path, required=True)
    prepare.add_argument("--feedback", type=Path, required=True)
    verify = commands.add_parser("verify", help="Check prepared files offline.")
    verify.add_argument("run_dir", type=Path)
    run = commands.add_parser("run", help="Run one live pulse with primary review.")
    run.add_argument("run_dir", type=Path)
    run.add_argument("--db", type=Path, default=DEFAULT_DB)
    judge = commands.add_parser("judge", help="Append the primary's live judgment.")
    judge.add_argument("run_dir", type=Path)
    judge.add_argument("case_id")
    judge.add_argument("verdict", choices=("pass", "fail"))
    judge.add_argument("--note", default="")
    judge.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            result = prepare_pulse(
                args.run_dir, json.loads(args.protocol.read_bytes()), args.feedback
            )
        elif args.command == "verify":
            result = verify_pulse(args.run_dir)
        elif args.command == "run":
            result = run_pulse(args.run_dir, args.db)
        else:
            result = {
                "output_ids": judge_pulse(
                    args.run_dir,
                    args.case_id,
                    args.verdict,
                    note=args.note,
                    db_path=args.db,
                )
            }
        print(json.dumps(result, ensure_ascii=False))
    except (OSError, ValueError, KeyError, sqlite3.Error) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
