from __future__ import annotations

from huemiliator.colour_library import (
    build_colour_library_packet,
    build_colour_library_rows,
)
from huemiliator.swatches import SwatchDataset, SwatchEntry, SwatchSource


def _dataset(*swatches: SwatchEntry) -> SwatchDataset:
    return SwatchDataset(
        source=SwatchSource(
            name="test",
            url="https://example.com",
            snapshot_date="2026-08-03",
            upstream_status="test",
            source_format="test",
        ),
        swatches=swatches,
    )


def test_build_colour_library_rows_carries_family_rank_and_metrics() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="egret", name="Egret", hex="#f3ece0"),
        SwatchEntry(source_order=2, slug="coffee", name="Coffee", hex="#6f4e37"),
        SwatchEntry(source_order=3, slug="blue", name="Blue", hex="#2f5da8"),
    )

    rows = build_colour_library_rows(dataset)

    assert len(rows) == 3
    assert rows[0].name == "Egret"
    assert rows[0].family == "neutral"
    assert rows[0].family_rank == 1
    assert rows[0].family_size == 1
    assert rows[0].metrics.hex_value == "#f3ece0"
    assert rows[1].family == "brown"
    assert rows[2].family == "blue"


def test_build_colour_library_packet_preserves_source_counts_and_rows() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="egret", name="Egret", hex="#f3ece0"),
        SwatchEntry(source_order=2, slug="coffee", name="Coffee", hex="#6f4e37"),
        SwatchEntry(source_order=3, slug="blue", name="Blue", hex="#2f5da8"),
    )

    packet = build_colour_library_packet(dataset)
    counts = {item["family"]: item["count"] for item in packet["families"]}
    first_row = packet["swatches"][0]

    assert packet["schema"] == "huemiliator.colour_library.v1"
    assert packet["source"]["swatch_count"] == 3
    assert counts["neutral"] == 1
    assert counts["brown"] == 1
    assert counts["blue"] == 1
    assert counts["green"] == 0
    assert first_row["source_order"] == 1
    assert first_row["metrics"]["hex_value"] == "#f3ece0"
    assert "lab_chroma" in first_row["metrics"]
