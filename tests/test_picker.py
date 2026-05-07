from __future__ import annotations

import subprocess
from unittest.mock import patch

import pytest

from huemiliator.picker import (
    PickerCancelled,
    PickerError,
    parse_osascript_rgb,
    pick_hex,
)


def test_parse_osascript_rgb_returns_lowercase_hex() -> None:
    assert parse_osascript_rgb("65535, 32768, 0\n") == "#ff8000"


def test_parse_osascript_rgb_rejects_wrong_shape() -> None:
    with pytest.raises(PickerError, match="Unexpected picker output"):
        parse_osascript_rgb("65535, 0")


def test_pick_hex_requires_macos() -> None:
    with patch("huemiliator.picker.sys.platform", "linux"):
        with pytest.raises(PickerError, match="only supported on macOS"):
            pick_hex()


def test_pick_hex_returns_hex_from_osascript_output() -> None:
    completed = subprocess.CompletedProcess(
        args=["osascript"],
        returncode=0,
        stdout="65535, 0, 65535\n",
        stderr="",
    )

    with patch("huemiliator.picker.sys.platform", "darwin"):
        with patch(
            "huemiliator.picker.shutil.which", return_value="/usr/bin/osascript"
        ):
            with patch("huemiliator.picker.subprocess.run", return_value=completed):
                assert pick_hex() == "#ff00ff"


def test_pick_hex_raises_cancelled_on_user_cancel() -> None:
    completed = subprocess.CompletedProcess(
        args=["osascript"],
        returncode=1,
        stdout="",
        stderr="User canceled.\n",
    )

    with patch("huemiliator.picker.sys.platform", "darwin"):
        with patch(
            "huemiliator.picker.shutil.which", return_value="/usr/bin/osascript"
        ):
            with patch("huemiliator.picker.subprocess.run", return_value=completed):
                with pytest.raises(PickerCancelled, match="canceled"):
                    pick_hex()
