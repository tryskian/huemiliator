from __future__ import annotations

from huemiliator.families import build_family_rank_index, classify_family
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


def test_classify_family_routes_neutral_brown_and_blue() -> None:
    assert classify_family("#f3ece0").family == "neutral"
    assert classify_family("#8b5e3c").family == "brown"
    assert classify_family("#2f5da8").family == "blue"


def test_build_family_rank_index_orders_chromatic_strength_ascending() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="muted-red", name="Muted red", hex="#b79494"),
        SwatchEntry(source_order=2, slug="loud-red", name="Loud red", hex="#d22345"),
    )

    ranked = build_family_rank_index(dataset)

    assert ranked[1].family == "red"
    assert ranked[1].family_rank == 1
    assert ranked[2].family == "red"
    assert ranked[2].family_rank == 2
    assert ranked[2].family_size == 2


def test_build_family_rank_index_orders_neutral_strength_ascending() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="mid", name="Mid", hex="#808080"),
        SwatchEntry(source_order=2, slug="light", name="Light", hex="#f3f3f3"),
    )

    ranked = build_family_rank_index(dataset)

    assert ranked[1].family == "neutral"
    assert ranked[1].family_rank == 1
    assert ranked[2].family == "neutral"
    assert ranked[2].family_rank == 2
