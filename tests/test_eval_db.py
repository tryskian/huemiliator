from __future__ import annotations

from pathlib import Path

from huemiliator.eval_db import (
    counts,
    get_output,
    init_db,
    judge_output,
    list_outputs,
    record_one_up_state,
)
from huemiliator.families import RankedSwatch
from huemiliator.pipeline import OneUpState
from huemiliator.resolution import SwatchResolution
from huemiliator.swatches import SwatchEntry


def _state() -> OneUpState:
    current = RankedSwatch(
        swatch=SwatchEntry(
            source_order=10,
            slug="egret",
            name="Egret",
            hex="#f3ece0",
        ),
        family="neutral",
        family_rank=4,
        family_size=8,
    )
    replacement = RankedSwatch(
        swatch=SwatchEntry(
            source_order=11,
            slug="white-swan",
            name="White Swan",
            hex="#e4d7c5",
        ),
        family="neutral",
        family_rank=5,
        family_size=8,
    )
    return OneUpState(
        resolution=SwatchResolution(
            input_hex="#f3ece0",
            matched=current.swatch,
            distance=1.25,
        ),
        current=current,
        replacement=replacement,
        loss_line="neutral but not harmless.",
    )


def test_init_db_creates_sqlite_file(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"

    resolved = init_db(db_path)

    assert resolved == db_path
    assert db_path.exists()


def test_record_one_up_state_persists_row(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"

    output_id = record_one_up_state(db_path, _state())
    rows = list_outputs(db_path, limit=5)

    assert output_id == 1
    assert len(rows) == 1
    assert rows[0]["input_hex"] == "#f3ece0"
    assert rows[0]["nearest_swatch_name"] == "Egret"
    assert rows[0]["replacement_shade_name"] == "White Swan"
    assert rows[0]["current_verdict"] is None


def test_list_outputs_rejects_zero_limit(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    init_db(db_path)

    try:
        list_outputs(db_path, limit=0)
    except ValueError as exc:
        assert "Limit must be at least 1." in str(exc)
    else:
        raise AssertionError("Expected ValueError for limit=0.")


def test_judge_output_updates_current_verdict_and_note(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    output_id = record_one_up_state(db_path, _state())

    judge_output(db_path, output_id, "pass", "family looks right")
    row = get_output(db_path, output_id)

    assert row["current_verdict"] == "pass"
    assert row["current_note"] == "family looks right"


def test_counts_summarise_pending_and_judged_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    first_id = record_one_up_state(db_path, _state())
    second_id = record_one_up_state(db_path, _state())

    judge_output(db_path, first_id, "pass", "")
    judge_output(db_path, second_id, "fail", "too mushy")
    summary = counts(db_path)

    assert summary == {"total": 2, "pass": 1, "fail": 1, "pending": 0}


def test_list_outputs_filters_to_one_family(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    record_one_up_state(db_path, _state())
    row = _state()
    brown_state = OneUpState(
        resolution=row.resolution,
        current=RankedSwatch(
            swatch=row.current.swatch,
            family="brown",
            family_rank=row.current.family_rank,
            family_size=row.current.family_size,
        ),
        replacement=RankedSwatch(
            swatch=row.replacement.swatch,
            family="brown",
            family_rank=row.replacement.family_rank,
            family_size=row.replacement.family_size,
        ),
        loss_line=row.loss_line,
    )
    record_one_up_state(db_path, brown_state)

    rows = list_outputs(db_path, limit=10, family="brown")

    assert len(rows) == 1
    assert rows[0]["family"] == "brown"


def test_counts_can_filter_to_one_family(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    record_one_up_state(db_path, _state())
    row = _state()
    brown_state = OneUpState(
        resolution=row.resolution,
        current=RankedSwatch(
            swatch=row.current.swatch,
            family="brown",
            family_rank=row.current.family_rank,
            family_size=row.current.family_size,
        ),
        replacement=RankedSwatch(
            swatch=row.replacement.swatch,
            family="brown",
            family_rank=row.replacement.family_rank,
            family_size=row.replacement.family_size,
        ),
        loss_line=row.loss_line,
    )
    record_one_up_state(db_path, brown_state)
    judge_output(db_path, 2, "pass", "")

    summary = counts(db_path, family="brown")

    assert summary == {"total": 1, "pass": 1, "fail": 0, "pending": 0}
