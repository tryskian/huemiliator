from __future__ import annotations

import pytest

from huemiliator.colour_boundaries import build_boundary_bins
from huemiliator.colour_library import ColourLibraryRow
from huemiliator.colour_math import ColourMetrics


def _row(
    source_order: int,
    name: str,
    family: str,
    lab_a: float,
    lab_b: float,
) -> ColourLibraryRow:
    return ColourLibraryRow(
        source_order=source_order,
        slug=name.lower().replace(" ", "-"),
        name=name,
        hex=f"#{source_order:06x}",
        family=family,
        family_rank=source_order,
        family_size=10,
        metrics=ColourMetrics(
            hex_value=f"#{source_order:06x}",
            hue_degrees=0.0,
            lightness=0.5,
            saturation=0.5,
            lab_lightness=50.0,
            lab_a=lab_a,
            lab_b=lab_b,
            lab_chroma=abs(lab_a) + abs(lab_b),
        ),
    )


def test_build_boundary_bins_reports_mixed_family_lab_bins() -> None:
    rows = (
        _row(1, "Neutral sample", "neutral", 12.0, 15.0),
        _row(2, "Brown sample", "brown", 15.0, 12.0),
        _row(3, "Pink sample", "pink", 18.0, 16.0),
        _row(4, "Red sample", "red", -22.0, 8.0),
        _row(5, "Orange sample", "orange", -21.0, 7.0),
    )

    bins = build_boundary_bins(rows, bin_step=10, min_family_count=2)

    assert len(bins) == 2
    assert bins[0].lab_a_min == 10
    assert bins[0].lab_b_min == 10
    assert bins[0].swatch_count == 3
    assert [item.family for item in bins[0].family_counts] == [
        "neutral",
        "brown",
        "pink",
    ]
    assert [item.source_order for item in bins[0].samples] == [1, 2, 3]


def test_build_boundary_bins_validates_report_parameters() -> None:
    with pytest.raises(ValueError, match="bin step"):
        build_boundary_bins((), bin_step=0)

    with pytest.raises(ValueError, match="min family count"):
        build_boundary_bins((), min_family_count=1)

    with pytest.raises(ValueError, match="sample limit"):
        build_boundary_bins((), sample_limit=0)
