from __future__ import annotations

import os
from pathlib import Path

from huemiliator.eval_db import (
    PULSE_EXCLUSION_REASONS,
    counts,
    get_output,
    init_db,
    judge_output,
    label_pulse_row,
    list_outputs,
    quarantine_live_surface,
    record_one_up_state,
    summarize_pulse_range,
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


def test_list_outputs_can_filter_to_warm_scope(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    neutral_state = _state()
    brown_state = OneUpState(
        resolution=neutral_state.resolution,
        current=RankedSwatch(
            swatch=neutral_state.current.swatch,
            family="brown",
            family_rank=neutral_state.current.family_rank,
            family_size=neutral_state.current.family_size,
        ),
        replacement=RankedSwatch(
            swatch=neutral_state.replacement.swatch,
            family="brown",
            family_rank=neutral_state.replacement.family_rank,
            family_size=neutral_state.replacement.family_size,
        ),
        loss_line=neutral_state.loss_line,
    )
    red_state = OneUpState(
        resolution=neutral_state.resolution,
        current=RankedSwatch(
            swatch=neutral_state.current.swatch,
            family="red",
            family_rank=neutral_state.current.family_rank,
            family_size=neutral_state.current.family_size,
        ),
        replacement=RankedSwatch(
            swatch=neutral_state.replacement.swatch,
            family="red",
            family_rank=neutral_state.replacement.family_rank,
            family_size=neutral_state.replacement.family_size,
        ),
        loss_line=neutral_state.loss_line,
    )
    record_one_up_state(db_path, neutral_state)
    record_one_up_state(db_path, brown_state)
    record_one_up_state(db_path, red_state)

    rows = list_outputs(db_path, limit=10, family="warm")

    assert len(rows) == 2
    assert {row["family"] for row in rows} == {"brown", "red"}


def test_counts_can_filter_to_warm_scope(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    neutral_state = _state()
    brown_state = OneUpState(
        resolution=neutral_state.resolution,
        current=RankedSwatch(
            swatch=neutral_state.current.swatch,
            family="brown",
            family_rank=neutral_state.current.family_rank,
            family_size=neutral_state.current.family_size,
        ),
        replacement=RankedSwatch(
            swatch=neutral_state.replacement.swatch,
            family="brown",
            family_rank=neutral_state.replacement.family_rank,
            family_size=neutral_state.replacement.family_size,
        ),
        loss_line=neutral_state.loss_line,
    )
    red_state = OneUpState(
        resolution=neutral_state.resolution,
        current=RankedSwatch(
            swatch=neutral_state.current.swatch,
            family="red",
            family_rank=neutral_state.current.family_rank,
            family_size=neutral_state.current.family_size,
        ),
        replacement=RankedSwatch(
            swatch=neutral_state.replacement.swatch,
            family="red",
            family_rank=neutral_state.replacement.family_rank,
            family_size=neutral_state.replacement.family_size,
        ),
        loss_line=neutral_state.loss_line,
    )
    record_one_up_state(db_path, neutral_state)
    record_one_up_state(db_path, brown_state)
    record_one_up_state(db_path, red_state)
    judge_output(db_path, 2, "pass", "")
    judge_output(db_path, 3, "fail", "")

    summary = counts(db_path, family="warm")

    assert summary == {"total": 2, "pass": 1, "fail": 1, "pending": 0}


def test_label_pulse_row_updates_label_and_reason(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    output_id = record_one_up_state(db_path, _state())

    label_pulse_row(db_path, output_id, "excluded_noise", "off_target_failure")
    row = get_output(db_path, output_id)

    assert row["pulse_label"] == "excluded_noise"
    assert row["pulse_reason"] == "off_target_failure"


def test_label_pulse_row_rejects_reason_for_anchor(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    output_id = record_one_up_state(db_path, _state())

    try:
        label_pulse_row(db_path, output_id, "anchor", "operator_artifact")
    except ValueError as exc:
        assert "Only excluded_noise rows may set a pulse reason." in str(exc)
    else:
        raise AssertionError("Expected ValueError for anchor reason.")


def test_summarize_pulse_range_counts_labels_and_verdict(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    first_id = record_one_up_state(db_path, _state())
    second_id = record_one_up_state(db_path, _state())
    third_id = record_one_up_state(db_path, _state())

    label_pulse_row(db_path, first_id, "anchor")
    label_pulse_row(db_path, second_id, "counted_seam")
    label_pulse_row(db_path, third_id, "excluded_noise", "operator_artifact")
    summary = summarize_pulse_range(db_path, first_id, third_id)

    assert summary.raw_rows == 3
    assert summary.anchors == 1
    assert summary.counted_seams == 1
    assert summary.excluded_noise == 1
    assert summary.excluded_by_reason == {
        reason: 1 if reason == "operator_artifact" else 0
        for reason in PULSE_EXCLUSION_REASONS
    }
    assert summary.unlabeled_rows == 0
    assert summary.counted_total == 2
    assert summary.verdict == "fail"


def test_summarize_pulse_range_reports_incomplete_until_all_rows_labeled(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "evals.sqlite"
    first_id = record_one_up_state(db_path, _state())
    second_id = record_one_up_state(db_path, _state())

    label_pulse_row(db_path, first_id, "anchor")
    summary = summarize_pulse_range(db_path, first_id, second_id)

    assert summary.unlabeled_rows == 1
    assert summary.verdict is None


def test_quarantine_live_surface_exports_rows_and_clears_live_db(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "evals.sqlite"
    parked_dir = tmp_path / "parked"
    record_one_up_state(db_path, _state())
    record_one_up_state(db_path, _state())

    result = quarantine_live_surface(
        db_path,
        parked_dir=parked_dir,
        label="closed third corrected red rerun",
    )

    assert result.total_rows == 2
    assert result.first_output_id == 1
    assert result.last_output_id == 2
    assert result.archive_path.exists()
    assert result.meta_path.exists()
    expected_source_db = os.path.relpath(
        db_path.resolve(),
        parked_dir.parent.parent.resolve(),
    )
    meta_text = result.meta_path.read_text()
    assert f"source_db: {expected_source_db}" in meta_text
    assert str(db_path) not in meta_text
    assert counts(db_path) == {"total": 0, "pass": 0, "fail": 0, "pending": 0}
