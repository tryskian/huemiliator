from __future__ import annotations

import io
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from huemiliator.main import main, render_contract, render_status
from huemiliator.picker import PickerError
from huemiliator.resolution import ResolutionError
from huemiliator.swatches import SwatchDatasetError


def test_render_status_includes_contract_lines() -> None:
    text = render_status()
    assert "pick a colour. hue's is better." in text
    assert "runtime: native colour picker -> canonical hex" in text
    assert "swatch snapshot: frozen local margaret2 reference" in text
    assert "swatch resolution: nearest snapshot match" in text
    assert (
        "same-family rank: fixed strength ladder with neutral undertone buckets" in text
    )
    assert (
        "transform: next same-family rank with neutral undertone/top-rank clamp" in text
    )
    assert "line: fixed family loss bank" in text
    assert "evidence: local sqlite eval db" in text
    assert "sampler: long-run local source-order or scoped cohort cycle" in text


def test_render_contract_exposes_runtime_contract_without_banner() -> None:
    text = render_contract()

    assert "status: partial runtime" in text
    assert "runtime: native colour picker -> canonical hex" in text
    assert "pick a colour. hue's is better." not in text


def test_main_contract_prints_runtime_contract() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_contract",
        return_value="status: partial runtime",
    ):
        with redirect_stdout(stdout):
            result = main(["contract"])

    assert result == 0
    assert stdout.getvalue().strip() == "status: partial runtime"


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


def test_main_eval_init_prints_db_path() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_init",
        return_value="Initialised /tmp/evals.sqlite",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-init"])

    assert result == 0
    assert "Initialised /tmp/evals.sqlite" in stdout.getvalue()


def test_main_eval_log_prints_logged_output() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_log",
        return_value="logged output: 7\nreplacement shade: Loud Red",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-log", "#d22345"])

    assert result == 0
    assert "logged output: 7" in stdout.getvalue()


def test_main_eval_list_prints_recent_rows() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_list",
        return_value="eval counts: total=1 pass=0 fail=0 pending=1\n\nid: 1",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-list", "--limit", "5"])

    assert result == 0
    assert "id: 1" in stdout.getvalue()


def test_main_eval_list_accepts_family_filter() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_list",
        return_value="eval counts (family=brown): total=1 pass=0 fail=0 pending=1",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-list", "--family", "brown"])

    assert result == 0
    assert "family=brown" in stdout.getvalue()


def test_main_eval_list_accepts_warm_scope() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_list",
        return_value="eval counts (scope=warm): total=4 pass=0 fail=0 pending=4",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-list", "--family", "warm"])

    assert result == 0
    assert "scope=warm" in stdout.getvalue()


def test_main_eval_judge_prints_updated_row() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_judge",
        return_value="judged output 1: pass\n\nid: 1",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-judge", "1", "pass", "--note", "looks right"])

    assert result == 0
    assert "judged output 1: pass" in stdout.getvalue()


def test_main_eval_pulse_start_prints_summary() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_pulse_start",
        return_value="bounded pulse start: count=15\noutput_ids=1-15",
    ) as render:
        with redirect_stdout(stdout):
            result = main(
                [
                    "eval-pulse-start",
                    "--count",
                    "15",
                    "--family",
                    "red",
                    "--start-source-order",
                    "20",
                    "--quarantine-label",
                    "closed red rerun",
                ]
            )

    assert result == 0
    assert render.call_args.kwargs["count"] == 15
    assert render.call_args.kwargs["input_hexes"] == ()
    assert "bounded pulse start: count=15" in stdout.getvalue()


def test_main_eval_pulse_start_accepts_input_hexes() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_pulse_start",
        return_value="bounded pulse start: input_hexes=3\noutput_ids=1-3",
    ) as render:
        with redirect_stdout(stdout):
            result = main(
                [
                    "eval-pulse-start",
                    "--input-hex",
                    "#dccdbc",
                    "--input-hex",
                    "#dbccb5",
                    "--input-hex",
                    "#f2e2e0",
                    "--quarantine-label",
                    "neutral pulse split source",
                ]
            )

    assert result == 0
    assert render.call_args.kwargs["count"] is None
    assert render.call_args.kwargs["input_hexes"] == (
        "#dccdbc",
        "#dbccb5",
        "#f2e2e0",
    )
    assert "bounded pulse start: input_hexes=3" in stdout.getvalue()


def test_main_eval_pulse_start_errors_cleanly() -> None:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_pulse_start",
        side_effect=ValueError("Live eval surface is not empty."),
    ):
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["eval-pulse-start", "--count", "15"])

    assert result == 1
    assert stdout.getvalue() == ""
    assert "Live eval surface is not empty." in stderr.getvalue()


def test_main_eval_pulse_label_prints_updated_row() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_pulse_label",
        return_value="pulse labeled output 2: anchor\n\nid: 2",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-pulse-label", "2", "anchor"])

    assert result == 0
    assert "pulse labeled output 2: anchor" in stdout.getvalue()


def test_main_eval_pulse_report_prints_summary() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_pulse_report",
        return_value="pulse ids: 20-34\npulse verdict: pass",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-pulse-report", "20", "34"])

    assert result == 0
    assert "pulse verdict: pass" in stdout.getvalue()


def test_main_eval_sample_local_prints_summary() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_eval_sample_local",
        return_value="local eval sample complete: count=3",
    ):
        with redirect_stdout(stdout):
            result = main(["eval-sample-local", "--count", "3"])

    assert result == 0
    assert "local eval sample complete: count=3" in stdout.getvalue()


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
