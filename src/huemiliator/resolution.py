from __future__ import annotations

import math
from dataclasses import dataclass

from huemiliator.colour_math import lab_from_hex, normalise_hex
from huemiliator.swatches import SwatchDataset, SwatchDatasetError, SwatchEntry


class ResolutionError(RuntimeError):
    """Raised when a hex value cannot be resolved against the swatch snapshot."""


@dataclass(frozen=True)
class SwatchResolution:
    input_hex: str
    matched: SwatchEntry
    distance: float


def normalise_runtime_hex(value: str) -> str:
    try:
        return normalise_hex(value)
    except ValueError as exc:
        raise ResolutionError(f"Invalid hex value: {value!r}") from exc


def delta_e_cie76(left_hex: str, right_hex: str) -> float:
    left_lab = lab_from_hex(left_hex)
    right_lab = lab_from_hex(right_hex)
    return math.sqrt(
        (left_lab[0] - right_lab[0]) ** 2
        + (left_lab[1] - right_lab[1]) ** 2
        + (left_lab[2] - right_lab[2]) ** 2
    )


def resolve_nearest_swatch(value: str, dataset: SwatchDataset) -> SwatchResolution:
    input_hex = normalise_runtime_hex(value)
    if not dataset.swatches:
        raise SwatchDatasetError("Swatch dataset is empty.")

    candidates = (
        SwatchResolution(
            input_hex=input_hex,
            matched=swatch,
            distance=delta_e_cie76(input_hex, swatch.hex),
        )
        for swatch in dataset.swatches
    )
    return min(
        candidates,
        key=lambda candidate: (candidate.distance, candidate.matched.source_order),
    )
