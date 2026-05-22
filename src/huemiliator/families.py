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
BROWN_BRIGHT_EDGE_HUE_MIN = 33.0
BROWN_BRIGHT_EDGE_LIGHTNESS_MIN = 0.50
BROWN_BRIGHT_EDGE_CHROMA_MIN = 38.0
BROWN_WARM_EDGE_HUE_MIN = 18.0
BROWN_WARM_EDGE_HUE_MAX = 36.0
BROWN_WARM_EDGE_LIGHTNESS_MIN = 0.48
BROWN_WARM_EDGE_CHROMA_MIN = 50.0
BROWN_EXTREME_CHROMA_HUE_MIN = 30.0
BROWN_EXTREME_CHROMA_MIN = 70.0
BROWN_LIGHTNESS_MAX = 0.56
BROWN_DARK_LIGHTNESS_MAX = 0.40
BROWN_CHROMA_MIN = 14.0
BROWN_GOLD_EDGE_HUE_MIN = 36.0
BROWN_GOLD_EDGE_LIGHTNESS_MIN = 0.44
BROWN_GOLD_EDGE_CHROMA_MIN = 30.0
BROWN_OLIVE_EDGE_HUE_MIN = 38.0
BROWN_OLIVE_EDGE_LIGHTNESS_MIN = 0.28
BROWN_OLIVE_EDGE_CHROMA_MIN = 8.0
RED_HUE_MAX = 15.0
RED_PINK_EDGE_LIGHTNESS_MIN = 0.74
RED_PINK_EDGE_CHROMA_MAX = 19.5
RED_HIGH_LIGHTNESS_LOW_CHROMA_PINK_LIGHTNESS_MIN = 0.80
RED_HIGH_LIGHTNESS_LOW_CHROMA_PINK_CHROMA_MAX = 23.0
RED_SOFT_PINK_PEACH_HUE_MIN = 6.5
RED_SOFT_PINK_PEACH_LIGHTNESS_MIN = 0.69
RED_SOFT_PINK_PEACH_LIGHTNESS_MAX = 0.80
RED_SOFT_PINK_PEACH_CHROMA_MAX = 24.0
RED_MODERATE_PINK_PEACH_LIGHTNESS_MIN = 0.58
RED_MODERATE_PINK_PEACH_LIGHTNESS_MAX = 0.76
RED_MODERATE_PINK_PEACH_CHROMA_MIN = 24.0
RED_MODERATE_PINK_PEACH_CHROMA_MAX = 33.5
RED_LOW_CHROMA_ROSE_LIGHTNESS_MIN = 0.55
RED_LOW_CHROMA_ROSE_LIGHTNESS_MAX = 0.72
RED_LOW_CHROMA_ROSE_CHROMA_MAX = 22.0
RED_LIGHT_PINK_EDGE_LIGHTNESS_MIN = 0.78
RED_LIGHT_PINK_EDGE_CHROMA_MIN = 25.0
RED_SATURATED_PINK_EDGE_LIGHTNESS_MIN = 0.68
RED_SATURATED_PINK_EDGE_CHROMA_MIN = 34.0
RED_MID_PINK_EDGE_LIGHTNESS_MIN = 0.58
RED_MID_PINK_EDGE_CHROMA_MIN = 45.0
RED_HOT_PINK_EDGE_LIGHTNESS_MIN = 0.54
RED_HOT_PINK_EDGE_CHROMA_MIN = 66.0
RED_BROWN_EDGE_LIGHTNESS_MAX = 0.45
RED_BROWN_EDGE_CHROMA_MAX = 19.0
RED_EXPANDED_BROWN_EDGE_LIGHTNESS_MAX = 0.47
RED_EXPANDED_BROWN_EDGE_CHROMA_MAX = 31.5
RED_SOFT_BROWN_EDGE_LIGHTNESS_MIN = 0.35
RED_SOFT_BROWN_EDGE_LIGHTNESS_MAX = 0.41
RED_SOFT_BROWN_EDGE_CHROMA_MAX = 33.0
RED_DARK_BROWN_EXTENSION_LIGHTNESS_MAX = 0.35
RED_DARK_BROWN_EXTENSION_CHROMA_MAX = 28.0
RED_WINE_EDGE_LIGHTNESS_MAX = 0.34
RED_WINE_EDGE_CHROMA_MIN = 30.0
RED_WINE_EDGE_CHROMA_MAX = 33.0
RED_DARK_BROWN_EDGE_LIGHTNESS_MAX = 0.30
RED_DARK_BROWN_EDGE_CHROMA_MAX = 24.0
ORANGE_HUE_MAX = 45.0
ORANGE_WARM_NEUTRAL_LIGHTNESS_MIN = 0.60
ORANGE_WARM_NEUTRAL_CHROMA_MAX = 20.0
ORANGE_TAUPE_EDGE_HUE_MAX = 34.0
ORANGE_TAUPE_EDGE_LIGHTNESS_MAX = 0.66
ORANGE_TAUPE_EDGE_CHROMA_MAX = 26.0
ORANGE_SOFT_BEIGE_EDGE_HUE_MIN = 32.0
ORANGE_SOFT_BEIGE_EDGE_LIGHTNESS_MIN = 0.67
ORANGE_SOFT_BEIGE_EDGE_CHROMA_MAX = 23.0
ORANGE_OLIVE_EDGE_HUE_MIN = 35.5
ORANGE_OLIVE_EDGE_LIGHTNESS_MAX = 0.65
ORANGE_OLIVE_EDGE_CHROMA_MAX = 30.0
YELLOW_HUE_MAX = 70.0
GREEN_HUE_MAX = 170.0
BLUE_HUE_MAX = 255.0
PURPLE_HUE_MAX = 320.0
RED_TO_ORANGE_EDGE_SWATCH_NAMES = frozenset(
    {
        "Burnt henna",
        "Tawny orange",
        "Crabapple",
        "Desert rose",
        "Burnt brick",
        "Dusted clay",
        "Ginger",
    }
)
YELLOW_TO_GREEN_EDGE_SWATCH_NAMES = frozenset(
    {
        "Green sheen",
        "Golden palm",
        "Cress green",
        "Willow",
        "Oasis",
        "Golden olive",
        "Woodbine",
        "Dark citron",
        "Daiquiri green",
        "Wild lime",
        "Linden green",
        "Bright chartreuse",
        "Tender shoots",
        "Lime punch",
        "Sulphur spring",
        "Citronelle",
        "Sunny lime",
        "Limeade",
        "Lime sherbet",
        "Apple green",
        "Warm olive",
        "Antique moss",
        "Citron",
        "Charlock",
        "Golden lime",
        "Mellow green",
        "Shadow green",
        "Celery green",
        "Green banana",
        "Winter pear",
        "Sylvan green",
        "Green essence",
        "Ethereal green",
        "Garden glade",
        "Pale green",
        "Pale lime yellow",
        "Green oasis",
        "Leek green",
        "Weeping willow",
        "Palm",
        "Moss",
        "Green moss",
        "Spinach green",
        "Luminary green",
        "Split pea",
    }
)
BLUE_TO_GREEN_EDGE_SWATCH_NAMES = frozenset(
    {
        "Caneel bay",
        "Pool green",
        "Aqua green",
        "Lake blue",
        "Hydro",
        "Porcelain green",
        "Tropical green",
        "Lapis",
        "Cockatoo",
        "Island paradise",
        "Arcadia",
    }
)


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


def classify_swatch(swatch: SwatchEntry) -> FamilyAssignment:
    assignment = classify_family(swatch.hex)
    if assignment.family == "red" and swatch.name in RED_TO_ORANGE_EDGE_SWATCH_NAMES:
        return FamilyAssignment(family="orange", metrics=assignment.metrics)
    if (
        assignment.family == "yellow"
        and swatch.name in YELLOW_TO_GREEN_EDGE_SWATCH_NAMES
    ):
        return FamilyAssignment(family="green", metrics=assignment.metrics)
    if assignment.family == "blue" and swatch.name in BLUE_TO_GREEN_EDGE_SWATCH_NAMES:
        return FamilyAssignment(family="green", metrics=assignment.metrics)
    return assignment


def build_family_rank_index(dataset: SwatchDataset) -> dict[int, RankedSwatch]:
    grouped: dict[str, list[tuple[SwatchEntry, ColourMetrics]]] = {
        family: [] for family in FAMILY_NAMES
    }
    for swatch in dataset.swatches:
        assignment = classify_swatch(swatch)
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
        if _is_brown_family_edge(metrics):
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
        if _is_red_pink_edge(metrics):
            return "pink"
        if _is_red_high_lightness_low_chroma_pink_edge(metrics):
            return "pink"
        if _is_red_soft_pink_peach_edge(metrics):
            return "pink"
        if _is_red_moderate_pink_peach_edge(metrics):
            return "pink"
        if _is_red_low_chroma_rose_edge(metrics):
            return "pink"
        if _is_red_saturated_pink_edge(metrics):
            return "pink"
        if _is_red_brown_edge(metrics):
            return "brown"
        return "red"
    if hue < ORANGE_HUE_MAX:
        if _is_orange_warm_neutral_edge(metrics):
            return "neutral"
        if _is_orange_taupe_edge(metrics):
            return "neutral"
        if _is_orange_soft_beige_edge(metrics):
            return "neutral"
        if _is_orange_olive_edge(metrics):
            return "yellow"
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
    # yellow/olive edge below the earthy core so one-up replacements stay
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
        metrics.hue_degrees >= BROWN_BRIGHT_EDGE_HUE_MIN
        and metrics.lightness >= BROWN_BRIGHT_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_BRIGHT_EDGE_CHROMA_MIN
    ):
        return True
    return (
        metrics.hue_degrees >= BROWN_EXTREME_CHROMA_HUE_MIN
        and metrics.lab_chroma >= BROWN_EXTREME_CHROMA_MIN
    )


def _is_brown_family_edge(metrics: ColourMetrics) -> bool:
    return (
        _is_brown_gold_edge(metrics)
        or _is_brown_warm_edge(metrics)
        or _is_brown_olive_edge(metrics)
    )


def _is_brown_gold_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees >= BROWN_GOLD_EDGE_HUE_MIN
        and metrics.lightness >= BROWN_GOLD_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_GOLD_EDGE_CHROMA_MIN
    )


def _is_brown_warm_edge(metrics: ColourMetrics) -> bool:
    return (
        BROWN_WARM_EDGE_HUE_MIN <= metrics.hue_degrees < BROWN_WARM_EDGE_HUE_MAX
        and metrics.lightness >= BROWN_WARM_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_WARM_EDGE_CHROMA_MIN
    )


def _is_brown_olive_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees >= BROWN_OLIVE_EDGE_HUE_MIN
        and metrics.lightness >= BROWN_OLIVE_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= BROWN_OLIVE_EDGE_CHROMA_MIN
    )


def _is_orange_warm_neutral_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.lightness >= ORANGE_WARM_NEUTRAL_LIGHTNESS_MIN
        and metrics.lab_chroma <= ORANGE_WARM_NEUTRAL_CHROMA_MAX
    )


def _is_red_pink_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.lightness >= RED_PINK_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma <= RED_PINK_EDGE_CHROMA_MAX
    )


def _is_red_high_lightness_low_chroma_pink_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.lightness >= RED_HIGH_LIGHTNESS_LOW_CHROMA_PINK_LIGHTNESS_MIN
        and metrics.lab_chroma <= RED_HIGH_LIGHTNESS_LOW_CHROMA_PINK_CHROMA_MAX
    )


def _is_red_soft_pink_peach_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees >= RED_SOFT_PINK_PEACH_HUE_MIN
        and RED_SOFT_PINK_PEACH_LIGHTNESS_MIN
        <= metrics.lightness
        <= RED_SOFT_PINK_PEACH_LIGHTNESS_MAX
        and metrics.lab_chroma <= RED_SOFT_PINK_PEACH_CHROMA_MAX
    )


def _is_red_moderate_pink_peach_edge(metrics: ColourMetrics) -> bool:
    return (
        RED_MODERATE_PINK_PEACH_LIGHTNESS_MIN
        <= metrics.lightness
        <= RED_MODERATE_PINK_PEACH_LIGHTNESS_MAX
        and RED_MODERATE_PINK_PEACH_CHROMA_MIN
        <= metrics.lab_chroma
        <= RED_MODERATE_PINK_PEACH_CHROMA_MAX
    )


def _is_red_low_chroma_rose_edge(metrics: ColourMetrics) -> bool:
    return (
        RED_LOW_CHROMA_ROSE_LIGHTNESS_MIN
        <= metrics.lightness
        <= RED_LOW_CHROMA_ROSE_LIGHTNESS_MAX
        and metrics.lab_chroma <= RED_LOW_CHROMA_ROSE_CHROMA_MAX
    )


def _is_red_saturated_pink_edge(metrics: ColourMetrics) -> bool:
    if (
        metrics.lightness >= RED_LIGHT_PINK_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= RED_LIGHT_PINK_EDGE_CHROMA_MIN
    ):
        return True
    if (
        metrics.lightness >= RED_SATURATED_PINK_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= RED_SATURATED_PINK_EDGE_CHROMA_MIN
    ):
        return True
    if (
        metrics.lightness >= RED_MID_PINK_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= RED_MID_PINK_EDGE_CHROMA_MIN
    ):
        return True
    return (
        metrics.lightness >= RED_HOT_PINK_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma >= RED_HOT_PINK_EDGE_CHROMA_MIN
    )


def _is_red_brown_edge(metrics: ColourMetrics) -> bool:
    if (
        metrics.lightness <= RED_BROWN_EDGE_LIGHTNESS_MAX
        and metrics.lab_chroma <= RED_BROWN_EDGE_CHROMA_MAX
    ):
        return True
    if (
        metrics.hue_degrees < RED_HUE_MAX
        and metrics.lightness <= RED_EXPANDED_BROWN_EDGE_LIGHTNESS_MAX
        and metrics.lab_chroma <= RED_EXPANDED_BROWN_EDGE_CHROMA_MAX
    ):
        return True
    if (
        RED_SOFT_BROWN_EDGE_LIGHTNESS_MIN
        <= metrics.lightness
        <= RED_SOFT_BROWN_EDGE_LIGHTNESS_MAX
        and metrics.lab_chroma <= RED_SOFT_BROWN_EDGE_CHROMA_MAX
    ):
        return True
    if (
        metrics.hue_degrees < RED_HUE_MAX
        and metrics.lightness <= RED_DARK_BROWN_EXTENSION_LIGHTNESS_MAX
        and metrics.lab_chroma <= RED_DARK_BROWN_EXTENSION_CHROMA_MAX
    ):
        return True
    if (
        metrics.lightness <= RED_WINE_EDGE_LIGHTNESS_MAX
        and RED_WINE_EDGE_CHROMA_MIN <= metrics.lab_chroma <= RED_WINE_EDGE_CHROMA_MAX
    ):
        return True
    return (
        metrics.lightness <= RED_DARK_BROWN_EDGE_LIGHTNESS_MAX
        and metrics.lab_chroma <= RED_DARK_BROWN_EDGE_CHROMA_MAX
    )


def _is_orange_taupe_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees < ORANGE_TAUPE_EDGE_HUE_MAX
        and metrics.lightness <= ORANGE_TAUPE_EDGE_LIGHTNESS_MAX
        and metrics.lab_chroma <= ORANGE_TAUPE_EDGE_CHROMA_MAX
    )


def _is_orange_soft_beige_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees >= ORANGE_SOFT_BEIGE_EDGE_HUE_MIN
        and metrics.lightness >= ORANGE_SOFT_BEIGE_EDGE_LIGHTNESS_MIN
        and metrics.lab_chroma <= ORANGE_SOFT_BEIGE_EDGE_CHROMA_MAX
    )


def _is_orange_olive_edge(metrics: ColourMetrics) -> bool:
    return (
        metrics.hue_degrees >= ORANGE_OLIVE_EDGE_HUE_MIN
        and metrics.lightness <= ORANGE_OLIVE_EDGE_LIGHTNESS_MAX
        and metrics.lab_chroma <= ORANGE_OLIVE_EDGE_CHROMA_MAX
    )
