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
BROWN_HUE_MIN = 15.0
BROWN_HUE_MAX = 50.0
BROWN_EARTHY_HUE_MAX = 37.0
BROWN_BRIGHT_SHOULDER_HUE_MIN = 33.0
BROWN_BRIGHT_SHOULDER_LIGHTNESS_MIN = 0.50
BROWN_BRIGHT_SHOULDER_CHROMA_MIN = 38.0
BROWN_EXTREME_CHROMA_HUE_MIN = 30.0
BROWN_EXTREME_CHROMA_MIN = 70.0
BROWN_LIGHTNESS_MAX = 0.56
BROWN_DARK_LIGHTNESS_MAX = 0.40
BROWN_CHROMA_MIN = 14.0
BROWN_GOLD_SHOULDER_HUE_MIN = 36.0
BROWN_GOLD_SHOULDER_LIGHTNESS_MIN = 0.44
BROWN_GOLD_SHOULDER_CHROMA_MIN = 30.0
BROWN_OLIVE_SHOULDER_HUE_MIN = 37.0
BROWN_OLIVE_SHOULDER_CHROMA_MAX = 20.0
BROWN_OLIVE_SHOULDER_GREEN_CHROMA_MIN = 8.0
BROWN_STRONG_OLIVE_SHOULDER_HUE_MIN = 40.0
BROWN_STRONG_OLIVE_SHOULDER_LAB_LIGHTNESS_MIN = 50.0
BROWN_STRONG_OLIVE_SHOULDER_CHROMA_MIN = 25.0
BROWN_ORANGE_SHOULDER_HUE_MAX = 33.0
BROWN_ORANGE_SHOULDER_LIGHTNESS_MIN = 0.50
BROWN_ORANGE_SHOULDER_CHROMA_MIN = 60.0
BROWN_GOLD_YELLOW_SHOULDER_HUE_MIN = 29.0
BROWN_GOLD_YELLOW_SHOULDER_LAB_LIGHTNESS_MIN = 55.0
BROWN_GOLD_YELLOW_SHOULDER_CHROMA_MIN = 43.0
BROWN_APRICOT_SHOULDER_HUE_MIN = 20.0
BROWN_APRICOT_SHOULDER_HUE_MAX = 28.0
BROWN_APRICOT_SHOULDER_LAB_LIGHTNESS_MIN = 55.0
BROWN_APRICOT_SHOULDER_CHROMA_MIN = 47.0
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
    hue = metrics.hue_degrees
    if BROWN_HUE_MIN <= hue < BROWN_HUE_MAX:
        if _is_brown_apricot_shoulder(metrics):
            return "orange"
        if _is_brown_orange_shoulder(metrics):
            return "orange"
        if _is_brown_gold_yellow_shoulder(metrics):
            pass
        elif _is_brown_olive_shoulder(metrics):
            if metrics.lab_chroma >= BROWN_OLIVE_SHOULDER_GREEN_CHROMA_MIN:
                return "green"
            return "neutral"
        elif (
            hue >= BROWN_GOLD_SHOULDER_HUE_MIN
            and metrics.lightness >= BROWN_GOLD_SHOULDER_LIGHTNESS_MIN
            and metrics.lab_chroma >= BROWN_GOLD_SHOULDER_CHROMA_MIN
        ):
            pass
        elif metrics.lightness < BROWN_DARK_LIGHTNESS_MAX:
            return "brown"
        elif (
            metrics.lightness < BROWN_LIGHTNESS_MAX
            and metrics.lab_chroma >= BROWN_CHROMA_MIN
        ):
            return "brown"
    if metrics.lab_chroma < NEUTRAL_CHROMA_MAX:
        return "neutral"
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


def _would_enter_brown(metrics: ColourMetrics) -> bool:
    return metrics.lightness < BROWN_DARK_LIGHTNESS_MAX or (
        metrics.lightness < BROWN_LIGHTNESS_MAX
        and metrics.lab_chroma >= BROWN_CHROMA_MIN
    )


def _is_brown_olive_shoulder(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees >= BROWN_OLIVE_SHOULDER_HUE_MIN
        and _would_enter_brown(metrics)
        and (
            metrics.lab_chroma <= BROWN_OLIVE_SHOULDER_CHROMA_MAX
            or (
                metrics.hue_degrees >= BROWN_STRONG_OLIVE_SHOULDER_HUE_MIN
                and metrics.lab_lightness
                >= BROWN_STRONG_OLIVE_SHOULDER_LAB_LIGHTNESS_MIN
                and metrics.lab_chroma >= BROWN_STRONG_OLIVE_SHOULDER_CHROMA_MIN
            )
        )
    )


def _is_brown_orange_shoulder(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees < BROWN_ORANGE_SHOULDER_HUE_MAX
        and metrics.lightness >= BROWN_ORANGE_SHOULDER_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_ORANGE_SHOULDER_CHROMA_MIN
    )


def _is_brown_gold_yellow_shoulder(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees >= BROWN_GOLD_YELLOW_SHOULDER_HUE_MIN
        and metrics.lab_lightness >= BROWN_GOLD_YELLOW_SHOULDER_LAB_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_GOLD_YELLOW_SHOULDER_CHROMA_MIN
    )


def _is_brown_apricot_shoulder(metrics: ColourMetrics) -> bool:
    return (
        BROWN_APRICOT_SHOULDER_HUE_MIN
        <= metrics.hue_degrees
        < BROWN_APRICOT_SHOULDER_HUE_MAX
        and metrics.lab_lightness >= BROWN_APRICOT_SHOULDER_LAB_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_APRICOT_SHOULDER_CHROMA_MIN
    )


def _family_rank_key(
    family: str,
    item: tuple[SwatchEntry, ColourMetrics],
) -> tuple[float, float, float, int]:
    swatch, metrics = item
    if family == "neutral":
        return (
            abs(metrics.lab_lightness - 50.0),
            metrics.lab_lightness,
            0.0,
            swatch.source_order,
        )
    if family == "brown":
        return _brown_rank_key(swatch, metrics)
    return (
        metrics.lab_chroma,
        abs(metrics.lab_lightness - 50.0),
        0.0,
        swatch.source_order,
    )


def _brown_rank_key(
    swatch: SwatchEntry,
    metrics: ColourMetrics,
) -> tuple[float, float, float, int]:
    # Brown behaves more like a contextual bucket than a single hue. Keep the
    # yellow/olive shoulder below the earthy core so one-up replacements stay
    # in the brown lane instead of drifting into gold.
    earthy_bucket = 0.0 if _is_brown_drift(metrics) else 1.0
    return (
        earthy_bucket,
        metrics.lab_chroma,
        abs(metrics.lab_lightness - 45.0),
        swatch.source_order,
    )


def _is_brown_drift(metrics: ColourMetrics) -> bool:
    if metrics.hue_degrees >= BROWN_EARTHY_HUE_MAX:
        return True
    if (
        metrics.hue_degrees >= BROWN_BRIGHT_SHOULDER_HUE_MIN
        and metrics.lightness >= BROWN_BRIGHT_SHOULDER_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_BRIGHT_SHOULDER_CHROMA_MIN
    ):
        return True
    return (
        metrics.hue_degrees >= BROWN_EXTREME_CHROMA_HUE_MIN
        and metrics.lab_chroma >= BROWN_EXTREME_CHROMA_MIN
    )
