from __future__ import annotations

from huemiliator.resolution import (
    ResolutionError,
    delta_e_cie76,
    normalise_runtime_hex,
    resolve_nearest_swatch,
)
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


def test_normalise_runtime_hex_accepts_hashless_uppercase() -> None:
    assert normalise_runtime_hex("F3ECE0") == "#f3ece0"


def test_normalise_runtime_hex_rejects_invalid_input() -> None:
    try:
        normalise_runtime_hex("not-a-hex")
    except ResolutionError as exc:
        assert "Invalid hex value" in str(exc)
    else:
        raise AssertionError("Expected ResolutionError for invalid hex input.")


def test_delta_e_cie76_is_zero_for_exact_match() -> None:
    assert delta_e_cie76("#f3ece0", "#f3ece0") == 0.0


def test_resolve_nearest_swatch_picks_smallest_distance() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="black", name="Black", hex="#000000"),
        SwatchEntry(source_order=2, slug="white", name="White", hex="#ffffff"),
    )

    resolution = resolve_nearest_swatch("#101010", dataset)

    assert resolution.matched.name == "Black"
    assert resolution.input_hex == "#101010"


def test_resolve_nearest_swatch_uses_source_order_tie_break() -> None:
    dataset = _dataset(
        SwatchEntry(
            source_order=300, slug="woodsmoke", name="Woodsmoke", hex="#947764"
        ),
        SwatchEntry(source_order=307, slug="burro", name="Burro", hex="#947764"),
    )

    resolution = resolve_nearest_swatch("#947764", dataset)

    assert resolution.matched.name == "Woodsmoke"
    assert resolution.matched.source_order == 300
