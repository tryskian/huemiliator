from __future__ import annotations

import json
import os
import re
import sqlite3
from contextlib import closing
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from huemiliator.config import EVAL_DB_PATH
from huemiliator.eval_scope import resolve_eval_scope_families
from huemiliator.pipeline import OneUpState

VERDICTS: tuple[str, ...] = ("pass", "fail")
LIST_VERDICTS: tuple[str, ...] = VERDICTS + ("pending",)
PULSE_LABELS: tuple[str, ...] = ("anchor", "counted_seam", "excluded_noise")
PULSE_EXCLUSION_REASONS: tuple[str, ...] = (
    "operator_artifact",
    "off_target_failure",
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS eval_outputs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_hex TEXT NOT NULL,
    nearest_swatch_name TEXT NOT NULL,
    nearest_swatch_hex TEXT NOT NULL,
    nearest_source_order INTEGER NOT NULL,
    distance_cie76 REAL NOT NULL,
    family TEXT NOT NULL,
    current_rank INTEGER NOT NULL,
    family_size INTEGER NOT NULL,
    replacement_shade_name TEXT NOT NULL,
    replacement_shade_hex TEXT NOT NULL,
    replacement_rank INTEGER NOT NULL,
    loss_line TEXT NOT NULL,
    current_verdict TEXT DEFAULT NULL
        CHECK (current_verdict IN ('pass', 'fail') OR current_verdict IS NULL),
    current_note TEXT NOT NULL DEFAULT '',
    pulse_label TEXT DEFAULT NULL
        CHECK (
            pulse_label IN ('anchor', 'counted_seam', 'excluded_noise')
            OR pulse_label IS NULL
        ),
    pulse_reason TEXT NOT NULL DEFAULT ''
        CHECK (pulse_reason IN ('', 'operator_artifact', 'off_target_failure')),
    created_at TEXT NOT NULL
);
"""


@dataclass(frozen=True)
class PulseSummary:
    start_output_id: int
    end_output_id: int
    raw_rows: int
    anchors: int
    counted_seams: int
    excluded_noise: int
    excluded_by_reason: dict[str, int]
    unlabeled_rows: int
    counted_total: int
    verdict: str | None


@dataclass(frozen=True)
class QuarantineResult:
    archive_path: Path
    meta_path: Path
    total_rows: int
    first_output_id: int
    last_output_id: int


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_eval_db_path() -> Path:
    return EVAL_DB_PATH


def _render_meta_source_db_path(db_path: Path, parked_dir: Path) -> str:
    return os.path.relpath(db_path.resolve(), parked_dir.parent.parent.resolve())


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    resolved = default_eval_db_path() if db_path is None else db_path
    resolved.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(resolved)
    conn.row_factory = sqlite3.Row
    return conn


def _ensure_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    columns = {
        row["name"]
        for row in conn.execute("PRAGMA table_info(eval_outputs)").fetchall()
    }
    if "pulse_label" not in columns:
        conn.execute(
            """
            ALTER TABLE eval_outputs
            ADD COLUMN pulse_label TEXT DEFAULT NULL
                CHECK (
                    pulse_label IN ('anchor', 'counted_seam', 'excluded_noise')
                    OR pulse_label IS NULL
                )
            """
        )
    if "pulse_reason" not in columns:
        conn.execute(
            """
            ALTER TABLE eval_outputs
            ADD COLUMN pulse_reason TEXT NOT NULL DEFAULT ''
                CHECK (
                    pulse_reason IN ('', 'operator_artifact', 'off_target_failure')
                )
            """
        )


def init_db(db_path: Path | None = None) -> Path:
    resolved = default_eval_db_path() if db_path is None else db_path
    with closing(connect(resolved)) as conn, conn:
        _ensure_schema(conn)
    return resolved


def record_one_up_state(db_path: Path | None, state: OneUpState) -> int:
    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        cursor = conn.execute(
            """
            INSERT INTO eval_outputs (
                input_hex,
                nearest_swatch_name,
                nearest_swatch_hex,
                nearest_source_order,
                distance_cie76,
                family,
                current_rank,
                family_size,
                replacement_shade_name,
                replacement_shade_hex,
                replacement_rank,
                loss_line,
                created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                state.resolution.input_hex,
                state.current.swatch.name,
                state.current.swatch.hex,
                state.current.swatch.source_order,
                state.resolution.distance,
                state.current.family,
                state.current.family_rank,
                state.current.family_size,
                state.replacement.swatch.name,
                state.replacement.swatch.hex,
                state.replacement.family_rank,
                state.loss_line,
                utc_now(),
            ),
        )
        if cursor.lastrowid is None:
            raise RuntimeError("Failed to retrieve inserted output id.")
        return cursor.lastrowid


def list_outputs(
    db_path: Path | None,
    *,
    limit: int = 20,
    verdict: str | None = None,
    family: str | None = None,
) -> list[sqlite3.Row]:
    if limit < 1:
        raise ValueError("Limit must be at least 1.")
    if verdict is not None and verdict not in LIST_VERDICTS:
        raise ValueError(f"Unsupported verdict '{verdict}'.")
    selected_families = resolve_eval_scope_families(family)

    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        where_clauses: list[str] = []
        params: list[object] = []
        if verdict in VERDICTS:
            where_clauses.append("current_verdict = ?")
            params.append(verdict)
        elif verdict == "pending":
            where_clauses.append("current_verdict IS NULL")
        if selected_families is not None:
            if len(selected_families) == 1:
                where_clauses.append("family = ?")
            else:
                placeholders = ", ".join("?" for _ in selected_families)
                where_clauses.append(f"family IN ({placeholders})")
            params.extend(selected_families)

        where_sql = ""
        if where_clauses:
            where_sql = "WHERE " + " AND ".join(where_clauses)

        cursor = conn.execute(
            f"""
            SELECT
                id,
                input_hex,
                nearest_swatch_name,
                nearest_swatch_hex,
                nearest_source_order,
                distance_cie76,
                family,
                current_rank,
                family_size,
                replacement_shade_name,
                replacement_shade_hex,
                replacement_rank,
                loss_line,
                current_verdict,
                current_note,
                pulse_label,
                pulse_reason,
                created_at
            FROM eval_outputs
            {where_sql}
            ORDER BY id DESC
            LIMIT ?
            """,
            (*params, limit),
        )
        return list(cursor.fetchall())


def get_output(db_path: Path | None, output_id: int) -> sqlite3.Row:
    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        row = conn.execute(
            """
            SELECT
                id,
                input_hex,
                nearest_swatch_name,
                nearest_swatch_hex,
                nearest_source_order,
                distance_cie76,
                family,
                current_rank,
                family_size,
                replacement_shade_name,
                replacement_shade_hex,
                replacement_rank,
                loss_line,
                current_verdict,
                current_note,
                pulse_label,
                pulse_reason,
                created_at
            FROM eval_outputs
            WHERE id = ?
            """,
            (output_id,),
        ).fetchone()
        if row is None:
            raise ValueError(f"Output id {output_id} does not exist.")
        return row


def judge_output(
    db_path: Path | None,
    output_id: int,
    verdict: str,
    note: str,
) -> None:
    if verdict not in VERDICTS:
        raise ValueError(f"Unsupported verdict '{verdict}'.")

    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        row = conn.execute(
            "SELECT id FROM eval_outputs WHERE id = ?",
            (output_id,),
        ).fetchone()
        if row is None:
            raise ValueError(f"Output id {output_id} does not exist.")

        conn.execute(
            """
            UPDATE eval_outputs
            SET current_verdict = ?, current_note = ?
            WHERE id = ?
            """,
            (verdict, note, output_id),
        )


def label_pulse_row(
    db_path: Path | None,
    output_id: int,
    label: str,
    reason: str = "",
) -> None:
    if label not in PULSE_LABELS:
        raise ValueError(f"Unsupported pulse label '{label}'.")
    if label == "excluded_noise":
        if reason not in PULSE_EXCLUSION_REASONS:
            raise ValueError(
                "Excluded noise rows require one pulse reason: "
                f"{', '.join(PULSE_EXCLUSION_REASONS)}."
            )
    elif reason:
        raise ValueError("Only excluded_noise rows may set a pulse reason.")

    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        row = conn.execute(
            "SELECT id FROM eval_outputs WHERE id = ?",
            (output_id,),
        ).fetchone()
        if row is None:
            raise ValueError(f"Output id {output_id} does not exist.")

        conn.execute(
            """
            UPDATE eval_outputs
            SET pulse_label = ?, pulse_reason = ?
            WHERE id = ?
            """,
            (label, reason, output_id),
        )


def summarize_pulse_range(
    db_path: Path | None,
    start_output_id: int,
    end_output_id: int,
) -> PulseSummary:
    if start_output_id < 1 or end_output_id < 1:
        raise ValueError("Pulse output ids must be at least 1.")
    if end_output_id < start_output_id:
        raise ValueError("Pulse end output id must be greater than or equal to start.")

    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        rows = list(
            conn.execute(
                """
                SELECT id, pulse_label, pulse_reason
                FROM eval_outputs
                WHERE id BETWEEN ? AND ?
                ORDER BY id ASC
                """,
                (start_output_id, end_output_id),
            ).fetchall()
        )

    if not rows:
        raise ValueError(
            f"No eval outputs found in pulse range {start_output_id}-{end_output_id}."
        )

    anchors = 0
    counted_seams = 0
    excluded_by_reason = {reason: 0 for reason in PULSE_EXCLUSION_REASONS}
    unlabeled_rows = 0
    for row in rows:
        label = row["pulse_label"]
        if label == "anchor":
            anchors += 1
            continue
        if label == "counted_seam":
            counted_seams += 1
            continue
        if label == "excluded_noise":
            excluded_by_reason[row["pulse_reason"]] += 1
            continue
        unlabeled_rows += 1

    counted_total = anchors + counted_seams
    verdict: str | None
    if unlabeled_rows != 0:
        verdict = None
    elif anchors > counted_seams:
        verdict = "pass"
    else:
        verdict = "fail"

    return PulseSummary(
        start_output_id=rows[0]["id"],
        end_output_id=rows[-1]["id"],
        raw_rows=len(rows),
        anchors=anchors,
        counted_seams=counted_seams,
        excluded_noise=sum(excluded_by_reason.values()),
        excluded_by_reason=excluded_by_reason,
        unlabeled_rows=unlabeled_rows,
        counted_total=counted_total,
        verdict=verdict,
    )


def quarantine_live_surface(
    db_path: Path | None,
    *,
    parked_dir: Path,
    label: str,
) -> QuarantineResult:
    resolved = default_eval_db_path() if db_path is None else db_path
    slug = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    if not slug:
        raise ValueError("Quarantine label must contain at least one letter or digit.")

    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        rows = list(
            conn.execute(
                """
                SELECT
                    id,
                    input_hex,
                    nearest_swatch_name,
                    nearest_swatch_hex,
                    nearest_source_order,
                    distance_cie76,
                    family,
                    current_rank,
                    family_size,
                    replacement_shade_name,
                    replacement_shade_hex,
                    replacement_rank,
                    loss_line,
                    current_verdict,
                    current_note,
                    pulse_label,
                    pulse_reason,
                    created_at
                FROM eval_outputs
                ORDER BY id ASC
                """
            ).fetchall()
        )
        if not rows:
            raise ValueError("No live eval outputs to quarantine.")

        timestamp = datetime.now(timezone.utc)
        basename = f"eval-surface-{timestamp:%Y%m%dT%H%M%SZ}-{slug}"
        parked_dir.mkdir(parents=True, exist_ok=True)
        archive_path = parked_dir / f"{basename}.jsonl"
        meta_path = parked_dir / f"{basename}.meta.txt"

        archive_path.write_text(
            "\n".join(json.dumps(dict(row), sort_keys=True) for row in rows) + "\n"
        )
        meta_path.write_text(
            "\n".join(
                (
                    f"label: {label}",
                    f"exported_at_utc: {timestamp.isoformat()}",
                    f"source_db: {_render_meta_source_db_path(resolved, parked_dir)}",
                    f"total_rows: {len(rows)}",
                    f"first_output_id: {rows[0]['id']}",
                    f"last_output_id: {rows[-1]['id']}",
                )
            )
            + "\n"
        )

        conn.execute("DELETE FROM eval_outputs")

    return QuarantineResult(
        archive_path=archive_path,
        meta_path=meta_path,
        total_rows=len(rows),
        first_output_id=rows[0]["id"],
        last_output_id=rows[-1]["id"],
    )


def counts(db_path: Path | None, *, family: str | None = None) -> dict[str, int]:
    selected_families = resolve_eval_scope_families(family)

    with closing(connect(db_path)) as conn, conn:
        _ensure_schema(conn)
        params: tuple[object, ...] = ()
        where_sql = ""
        if selected_families is not None:
            if len(selected_families) == 1:
                where_sql = "WHERE family = ?"
            else:
                placeholders = ", ".join("?" for _ in selected_families)
                where_sql = f"WHERE family IN ({placeholders})"
            params = tuple(selected_families)
        totals = conn.execute(
            f"""
            SELECT
                COUNT(*) AS total,
                SUM(CASE WHEN current_verdict = 'pass' THEN 1 ELSE 0 END) AS pass,
                SUM(CASE WHEN current_verdict = 'fail' THEN 1 ELSE 0 END) AS fail,
                SUM(CASE WHEN current_verdict IS NULL THEN 1 ELSE 0 END) AS pending
            FROM eval_outputs
            {where_sql}
            """,
            params,
        ).fetchone()
        if totals is None:
            return {"total": 0, "pass": 0, "fail": 0, "pending": 0}
        return {
            "total": int(totals["total"]),
            "pass": int(totals["pass"] or 0),
            "fail": int(totals["fail"] or 0),
            "pending": int(totals["pending"] or 0),
        }
