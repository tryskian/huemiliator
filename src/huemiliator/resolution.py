from __future__ import annotations

import math
import re
from dataclasses import dataclass

from huemiliator.swatches import SwatchDataset, SwatchDatasetError, SwatchEntry

HEX_PATTERN = re.compile(r"#?[0-9a-fA-F]{6}")


class ResolutionError(RuntimeError):
    """Raised when a hex value cannot be resolved against the swatch snapshot."""


@dataclass(frozen=True)
class SwatchResolution:
    input_hex: str
    matched: SwatchEntry
    distance: float


def normalise_runtime_hex(value: str) -> str:
    compact = value.strip()
    if not HEX_PATTERN.fullmatch(compact):
        raise ResolutionError(f"Invalid hex value: {value!r}")
    if not compact.startswith("#"):
        compact = f"#{compact}"
    return compact.lower()


def _hex_to_rgb(value: str) -> tuple[float, float, float]:
    normalised = normalise_runtime_hex(value)
    return (
        int(normalised[1:3], 16) / 255.0,
        int(normalised[3:5], 16) / 255.0,
        int(normalised[5:7], 16) / 255.0,
    )


def _srgb_to_linear(value: float) -> float:
    if value <= 0.04045:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4


def _rgb_to_lab(value: str) -> tuple[float, float, float]:
    red, green, blue = (_srgb_to_linear(channel) for channel in _hex_to_rgb(value))

    x = red * 0.4124564 + green * 0.3575761 + blue * 0.1804375
    y = red * 0.2126729 + green * 0.7151522 + blue * 0.0721750
    z = red * 0.0193339 + green * 0.1191920 + blue * 0.9503041

    return _xyz_to_lab(x, y, z)


def _xyz_to_lab(x: float, y: float, z: float) -> tuple[float, float, float]:
    x_ref = 0.95047
    y_ref = 1.0
    z_ref = 1.08883

    def transform(value: float) -> float:
        if value > 216 / 24389:
            return value ** (1 / 3)
        return ((24389 / 27) * value + 16) / 116

    fx = transform(x / x_ref)
    fy = transform(y / y_ref)
    fz = transform(z / z_ref)

    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e_cie76(left_hex: str, right_hex: str) -> float:
    left_lab = _rgb_to_lab(left_hex)
    right_lab = _rgb_to_lab(right_hex)
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
