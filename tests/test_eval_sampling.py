from __future__ import annotations

from pathlib import Path

from huemiliator.eval_db import counts, list_outputs
from huemiliator.eval_sampling import sample_local_eval_outputs
from huemiliator.swatches import SwatchDataset, SwatchEntry, SwatchSource


def _dataset(*swatches: SwatchEntry) -> SwatchDataset:
    return SwatchDataset(
        source=SwatchSource(
            name="test",
            url="https://example.com",
            snapshot_date="2026-05-07",
            upstream_status="test",
            source_format="test",
        ),
        swatches=swatches,
    )


def test_sample_local_eval_outputs_records_count_based_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="egret", name="Egret", hex="#f3ece0"),
        SwatchEntry(source_order=2, slug="woodsmoke", name="Woodsmoke", hex="#947764"),
    )

    summary = sample_local_eval_outputs(count=3, dataset=dataset, db_path=db_path)
    rows = list_outputs(db_path, limit=10)

    assert summary.recorded == 3
    assert summary.first_output_id == 1
    assert summary.last_output_id == 3
    assert len(rows) == 3
    assert rows[0]["input_hex"] == "#f3ece0"
    assert rows[1]["input_hex"] == "#947764"


def test_sample_local_eval_outputs_rejects_missing_stop_condition() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="egret", name="Egret", hex="#f3ece0"),
    )

    try:
        sample_local_eval_outputs(dataset=dataset)
    except ValueError as exc:
        assert "Provide count or duration_seconds." in str(exc)
    else:
        raise AssertionError("Expected ValueError for missing stop condition.")


def test_sample_local_eval_outputs_honors_start_source_order(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="egret", name="Egret", hex="#f3ece0"),
        SwatchEntry(source_order=2, slug="woodsmoke", name="Woodsmoke", hex="#947764"),
    )

    sample_local_eval_outputs(
        count=1,
        start_source_order=2,
        dataset=dataset,
        db_path=db_path,
    )
    summary = counts(db_path)
    rows = list_outputs(db_path, limit=1)

    assert summary["total"] == 1
    assert rows[0]["input_hex"] == "#947764"


def test_sample_local_eval_outputs_filters_to_one_family(tmp_path: Path) -> None:
    db_path = tmp_path / "evals.sqlite"
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="egret", name="Egret", hex="#f3ece0"),
        SwatchEntry(source_order=2, slug="woodsmoke", name="Woodsmoke", hex="#947764"),
        SwatchEntry(source_order=3, slug="loud-red", name="Loud Red", hex="#d22345"),
    )

    sample_local_eval_outputs(count=2, family="brown", dataset=dataset, db_path=db_path)
    rows = list_outputs(db_path, limit=10)

    assert len(rows) == 2
    assert all(row["family"] == "brown" for row in rows)
