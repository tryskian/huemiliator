from __future__ import annotations

import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

from huemiliator.config import EVAL_DB_PATH
from huemiliator.families import FAMILY_NAMES
from huemiliator.pipeline import OneUpState

VERDICTS: tuple[str, ...] = ("pass", "fail")
LIST_VERDICTS: tuple[str, ...] = VERDICTS + ("pending",)

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
    created_at TEXT NOT NULL
);
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_eval_db_path() -> Path:
    return EVAL_DB_PATH


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    resolved = default_eval_db_path() if db_path is None else db_path
    resolved.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(resolved)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: Path | None = None) -> Path:
    resolved = default_eval_db_path() if db_path is None else db_path
    with closing(connect(resolved)) as conn, conn:
        conn.executescript(SCHEMA)
    return resolved


def record_one_up_state(db_path: Path | None, state: OneUpState) -> int:
    with closing(connect(db_path)) as conn, conn:
        conn.executescript(SCHEMA)
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
    if family is not None and family not in FAMILY_NAMES:
        raise ValueError(f"Unsupported family '{family}'.")

    with closing(connect(db_path)) as conn, conn:
        conn.executescript(SCHEMA)
        where_clauses: list[str] = []
        params: list[object] = []
        if verdict in VERDICTS:
            where_clauses.append("current_verdict = ?")
            params.append(verdict)
        elif verdict == "pending":
            where_clauses.append("current_verdict IS NULL")
        if family is not None:
            where_clauses.append("family = ?")
            params.append(family)

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
        conn.executescript(SCHEMA)
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
        conn.executescript(SCHEMA)
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


def counts(db_path: Path | None, *, family: str | None = None) -> dict[str, int]:
    if family is not None and family not in FAMILY_NAMES:
        raise ValueError(f"Unsupported family '{family}'.")

    with closing(connect(db_path)) as conn, conn:
        conn.executescript(SCHEMA)
        params: tuple[object, ...] = ()
        where_sql = ""
        if family is not None:
            where_sql = "WHERE family = ?"
            params = (family,)
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
