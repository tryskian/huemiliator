from __future__ import annotations

import io
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from huemiliator.main import main, render_status
from huemiliator.picker import PickerError
from huemiliator.resolution import ResolutionError
from huemiliator.swatches import SwatchDatasetError


def test_render_status_includes_contract_lines() -> None:
    text = render_status()
    assert "pick a colour. hue's is better." in text
    assert "runtime: native colour picker -> canonical hex" in text
    assert "swatch snapshot: frozen local margaret2 reference" in text
    assert "swatch resolution: nearest snapshot match" in text
    assert "same-family rank: fixed strength ladder" in text
    assert "transform: next same-family rank with top-rank clamp" in text
    assert "line: fixed family loss bank" in text


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


def test_main_resolve_prints_nearest_swatch() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_resolution",
        return_value="input: #f3ece0\nnearest swatch: Egret\nfamily: neutral",
    ):
        with redirect_stdout(stdout):
            result = main(["resolve", "#f3ece0"])

    assert result == 0
    assert "nearest swatch: Egret" in stdout.getvalue()
    assert "family: neutral" in stdout.getvalue()


def test_main_resolve_errors_cleanly() -> None:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with patch(
        "huemiliator.main.render_resolution",
        side_effect=ResolutionError("invalid resolve input"),
    ):
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["resolve", "oops"])

    assert result == 1
    assert stdout.getvalue() == ""
    assert "invalid resolve input" in stderr.getvalue()


def test_main_replace_prints_replacement() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_replacement",
        return_value="replacement shade: Loud red\nreplacement hex: #d22345",
    ):
        with redirect_stdout(stdout):
            result = main(["replace", "#b79494"])

    assert result == 0
    assert "replacement shade: Loud red" in stdout.getvalue()


def test_main_replace_errors_cleanly() -> None:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with patch(
        "huemiliator.main.render_replacement",
        side_effect=ResolutionError("invalid replace input"),
    ):
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["replace", "oops"])

    assert result == 1
    assert stdout.getvalue() == ""
    assert "invalid replace input" in stderr.getvalue()


def test_main_one_up_prints_loss_line() -> None:
    stdout = io.StringIO()
    output = (
        "replacement shade: High risk red\nthe idea was right. the nerve was missing."
    )
    with patch(
        "huemiliator.main.render_one_up",
        return_value=output,
    ):
        with redirect_stdout(stdout):
            result = main(["one-up", "#d22345"])

    assert result == 0
    assert "replacement shade: High risk red" in stdout.getvalue()
    assert "the nerve was missing." in stdout.getvalue()


def test_main_one_up_errors_cleanly() -> None:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with patch(
        "huemiliator.main.render_one_up",
        side_effect=ValueError("unknown loss-line family"),
    ):
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["one-up", "oops"])

    assert result == 1
    assert stdout.getvalue() == ""
    assert "unknown loss-line family" in stderr.getvalue()


def test_main_resolve_snapshot_errors_cleanly() -> None:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with patch(
        "huemiliator.main.render_resolution",
        side_effect=SwatchDatasetError("snapshot load failed"),
    ):
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["resolve", "#f3ece0"])

    assert result == 1
    assert stdout.getvalue() == ""
    assert "snapshot load failed" in stderr.getvalue()
