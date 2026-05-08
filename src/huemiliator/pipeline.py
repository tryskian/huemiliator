from __future__ import annotations

from dataclasses import dataclass

from huemiliator.families import (
    RankedSwatch,
    build_family_member_index,
    build_family_rank_index,
    select_one_up,
)
from huemiliator.loss_lines import loss_line_for_family
from huemiliator.resolution import SwatchResolution, resolve_nearest_swatch
from huemiliator.swatches import SwatchDataset


@dataclass(frozen=True)
class OneUpState:
    resolution: SwatchResolution
    current: RankedSwatch
    replacement: RankedSwatch
    loss_line: str


def build_one_up_state(hex_value: str, dataset: SwatchDataset) -> OneUpState:
    resolution = resolve_nearest_swatch(hex_value, dataset)
    family_rank_index = build_family_rank_index(dataset)
    current = family_rank_index[resolution.matched.source_order]
    family_member_index = build_family_member_index(family_rank_index)
    selection = select_one_up(current, family_member_index)
    return OneUpState(
        resolution=resolution,
        current=selection.current,
        replacement=selection.replacement,
        loss_line=loss_line_for_family(selection.replacement.family),
    )
