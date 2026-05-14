from __future__ import annotations

from huemiliator.pipeline import build_one_up_state
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


def test_build_one_up_state_returns_replacement_and_loss_line() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="soft-red", name="Soft Red", hex="#d9a6a1"),
        SwatchEntry(source_order=2, slug="loud-red", name="Loud Red", hex="#d22345"),
    )

    state = build_one_up_state("#d9a6a1", dataset)

    assert state.current.swatch.name == "Soft Red"
    assert state.replacement.swatch.name == "Loud Red"
    assert state.loss_line
