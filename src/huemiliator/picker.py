from __future__ import annotations

import shutil
import subprocess
import sys


class PickerError(RuntimeError):
    """Raised when the native picker cannot return a usable hex value."""


class PickerCancelled(PickerError):
    """Raised when the user closes the picker without choosing a colour."""


def _channel_16bit_to_8bit(value: int) -> int:
    if not 0 <= value <= 65535:
        raise PickerError(f"Picker channel {value} is out of 16-bit range.")
    return round(value / 257)


def parse_osascript_rgb(value: str) -> str:
    parts = [part.strip() for part in value.strip().split(",")]
    if len(parts) != 3 or any(not part for part in parts):
        raise PickerError(f"Unexpected picker output: {value!r}")

    try:
        red_raw, green_raw, blue_raw = (int(part) for part in parts)
    except ValueError as exc:
        raise PickerError(
            f"Picker output must be integer RGB values: {value!r}"
        ) from exc

    red = _channel_16bit_to_8bit(red_raw)
    green = _channel_16bit_to_8bit(green_raw)
    blue = _channel_16bit_to_8bit(blue_raw)
    return f"#{red:02x}{green:02x}{blue:02x}"


def pick_hex() -> str:
    if sys.platform != "darwin":
        raise PickerError("Native colour picker is only supported on macOS.")

    if shutil.which("osascript") is None:
        raise PickerError("osascript is required for the macOS colour picker.")

    result = subprocess.run(
        [
            "osascript",
            "-e",
            "tell current application to activate",
            "-e",
            "choose color",
        ],
        capture_output=True,
        check=False,
        text=True,
    )

    if result.returncode != 0:
        details = " ".join(
            part.strip() for part in (result.stderr, result.stdout) if part.strip()
        )
        if "user canceled" in details.lower():
            raise PickerCancelled("Colour picker canceled.")
        raise PickerError(
            f"Native colour picker failed: {details or 'unknown osascript failure.'}"
        )

    return parse_osascript_rgb(result.stdout)
