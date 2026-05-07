from __future__ import annotations

import colorsys
import math
import re
from dataclasses import dataclass

HEX_PATTERN = re.compile(r"#[0-9a-fA-F]{6}")


@dataclass(frozen=True)
class ColourMetrics:
    hex_value: str
    hue_degrees: float
    lightness: float
    saturation: float
    lab_lightness: float
    lab_a: float
    lab_b: float
    lab_chroma: float


def normalise_hex(value: str) -> str:
    compact = value.strip()
    if not compact.startswith("#"):
        compact = f"#{compact}"
    if not HEX_PATTERN.fullmatch(compact):
        raise ValueError(f"Invalid hex value: {value!r}")
    return compact.lower()


def rgb_channels(value: str) -> tuple[float, float, float]:
    normalised = normalise_hex(value)
    return (
        int(normalised[1:3], 16) / 255.0,
        int(normalised[3:5], 16) / 255.0,
        int(normalised[5:7], 16) / 255.0,
    )


def _srgb_to_linear(value: float) -> float:
    if value <= 0.04045:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4


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


def lab_from_hex(value: str) -> tuple[float, float, float]:
    red, green, blue = (_srgb_to_linear(channel) for channel in rgb_channels(value))

    x = red * 0.4124564 + green * 0.3575761 + blue * 0.1804375
    y = red * 0.2126729 + green * 0.7151522 + blue * 0.0721750
    z = red * 0.0193339 + green * 0.1191920 + blue * 0.9503041

    return _xyz_to_lab(x, y, z)


def build_colour_metrics(value: str) -> ColourMetrics:
    normalised = normalise_hex(value)
    red, green, blue = rgb_channels(normalised)
    hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
    lab_lightness, lab_a, lab_b = lab_from_hex(normalised)
    lab_chroma = math.sqrt(lab_a**2 + lab_b**2)
    return ColourMetrics(
        hex_value=normalised,
        hue_degrees=hue * 360.0,
        lightness=lightness,
        saturation=saturation,
        lab_lightness=lab_lightness,
        lab_a=lab_a,
        lab_b=lab_b,
        lab_chroma=lab_chroma,
    )
