from __future__ import annotations

import io
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from huemiliator.main import main, render_status
from huemiliator.picker import PickerError


def test_render_status_includes_contract_lines() -> None:
    text = render_status()
    assert "pick a colour. hue's is better." in text
    assert "runtime: native colour picker -> canonical hex" in text
    assert "transform: not implemented yet" in text


def test_main_pick_prints_selected_hex() -> None:
    stdout = io.StringIO()
    with patch("huemiliator.main.pick_hex", return_value="#112233"):
        with redirect_stdout(stdout):
            result = main(["pick"])

    assert result == 0
    assert stdout.getvalue().strip() == "#112233"


def test_main_pick_errors_cleanly() -> None:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with patch("huemiliator.main.pick_hex", side_effect=PickerError("picker failed")):
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["pick"])

    assert result == 1
    assert stdout.getvalue() == ""
    assert "picker failed" in stderr.getvalue()
