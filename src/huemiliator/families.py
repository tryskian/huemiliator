from __future__ import annotations

from dataclasses import dataclass

from huemiliator.colour_math import ColourMetrics, build_colour_metrics
from huemiliator.swatches import SwatchDataset, SwatchEntry

FAMILY_NAMES: tuple[str, ...] = (
    "neutral",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
)

NEUTRAL_CHROMA_MAX = 14.0
BROWN_HUE_MIN = 20.0
BROWN_HUE_MAX = 50.0
BROWN_LIGHTNESS_MAX = 0.5
RED_HUE_MAX = 15.0
ORANGE_HUE_MAX = 45.0
YELLOW_HUE_MAX = 70.0
GREEN_HUE_MAX = 170.0
BLUE_HUE_MAX = 255.0
PURPLE_HUE_MAX = 320.0


@dataclass(frozen=True)
class FamilyAssignment:
    family: str
    metrics: ColourMetrics


@dataclass(frozen=True)
class RankedSwatch:
    swatch: SwatchEntry
    family: str
    family_rank: int
    family_size: int


@dataclass(frozen=True)
class OneUpSelection:
    current: RankedSwatch
    replacement: RankedSwatch


def classify_family(value: str) -> FamilyAssignment:
    metrics = build_colour_metrics(value)
    family = _classify_metrics(metrics)
    return FamilyAssignment(family=family, metrics=metrics)


def build_family_rank_index(dataset: SwatchDataset) -> dict[int, RankedSwatch]:
    grouped: dict[str, list[tuple[SwatchEntry, ColourMetrics]]] = {
        family: [] for family in FAMILY_NAMES
    }
    for swatch in dataset.swatches:
        assignment = classify_family(swatch.hex)
        grouped[assignment.family].append((swatch, assignment.metrics))

    ranked: dict[int, RankedSwatch] = {}
    for family in FAMILY_NAMES:
        members = sorted(
            grouped[family], key=lambda item: _family_rank_key(family, item)
        )
        family_size = len(members)
        for family_rank, (swatch, _metrics) in enumerate(members, start=1):
            ranked[swatch.source_order] = RankedSwatch(
                swatch=swatch,
                family=family,
                family_rank=family_rank,
                family_size=family_size,
            )
    return ranked


def build_family_member_index(
    family_rank_index: dict[int, RankedSwatch],
) -> dict[str, tuple[RankedSwatch, ...]]:
    grouped: dict[str, list[RankedSwatch]] = {family: [] for family in FAMILY_NAMES}
    for ranked_swatch in family_rank_index.values():
        grouped[ranked_swatch.family].append(ranked_swatch)

    return {
        family: tuple(sorted(grouped[family], key=lambda item: item.family_rank))
        for family in FAMILY_NAMES
    }


def select_one_up(
    ranked_swatch: RankedSwatch,
    family_member_index: dict[str, tuple[RankedSwatch, ...]],
) -> OneUpSelection:
    members = family_member_index[ranked_swatch.family]
    replacement_rank = min(ranked_swatch.family_rank + 1, ranked_swatch.family_size)
    replacement = members[replacement_rank - 1]
    return OneUpSelection(current=ranked_swatch, replacement=replacement)


def _classify_metrics(metrics: ColourMetrics) -> str:
    if metrics.lab_chroma < NEUTRAL_CHROMA_MAX:
        return "neutral"

    hue = metrics.hue_degrees
    if BROWN_HUE_MIN <= hue < BROWN_HUE_MAX and metrics.lightness < BROWN_LIGHTNESS_MAX:
        return "brown"
    if hue < RED_HUE_MAX or hue >= 345.0:
        return "red"
    if hue < ORANGE_HUE_MAX:
        return "orange"
    if hue < YELLOW_HUE_MAX:
        return "yellow"
    if hue < GREEN_HUE_MAX:
        return "green"
    if hue < BLUE_HUE_MAX:
        return "blue"
    if hue < PURPLE_HUE_MAX:
        return "purple"
    return "pink"


def _family_rank_key(
    family: str,
    item: tuple[SwatchEntry, ColourMetrics],
) -> tuple[float, float, int]:
    swatch, metrics = item
    if family == "neutral":
        return (
            abs(metrics.lab_lightness - 50.0),
            metrics.lab_lightness,
            swatch.source_order,
        )
    return (
        metrics.lab_chroma,
        abs(metrics.lab_lightness - 50.0),
        swatch.source_order,
    )
