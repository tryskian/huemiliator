from __future__ import annotations

import io
import json
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from huemiliator.main import (
    main,
    render_behaviour_contract,
    render_behaviour_facts,
    render_colour_boundaries,
    render_colour_library,
    render_contract,
    render_status,
)
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


def test_render_behaviour_contract_exposes_language_eval_boundary() -> None:
    text = render_behaviour_contract()

    assert "status: behaviour eval ready" in text
    assert "substrate: fixed runtime colour facts" in text
    assert "eval target: language fidelity, tone fit, evidence fit, consistency" in text


def test_main_behaviour_contract_prints_contract() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_behaviour_contract",
        return_value="status: behaviour eval ready",
    ):
        with redirect_stdout(stdout):
            result = main(["behaviour-contract"])

    assert result == 0
    assert stdout.getvalue().strip() == "status: behaviour eval ready"


def test_render_colour_library_prints_text_summary() -> None:
    text = render_colour_library()

    assert "colour library" in text
    assert "schema: huemiliator.colour_library.v1" in text
    assert "swatches: 2310" in text
    assert "families:" in text
    assert "- neutral:" in text


def test_render_colour_library_can_emit_json_packet() -> None:
    packet = json.loads(render_colour_library("json"))

    assert packet["schema"] == "huemiliator.colour_library.v1"
    assert packet["source"]["swatch_count"] == 2310
    assert len(packet["swatches"]) == 2310
    assert packet["swatches"][0]["name"] == "Egret"
    assert packet["swatches"][0]["family"] == "neutral"
    assert "lab_chroma" in packet["swatches"][0]["metrics"]


def test_main_colour_library_prints_text_summary() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_colour_library",
        return_value="colour library\nswatches: 2310",
    ) as render:
        with redirect_stdout(stdout):
            result = main(["colour-library"])

    assert result == 0
    assert render.call_args.args == ("text",)
    assert "swatches: 2310" in stdout.getvalue()


def test_main_colour_library_accepts_json_format() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_colour_library",
        return_value='{"schema": "huemiliator.colour_library.v1"}',
    ) as render:
        with redirect_stdout(stdout):
            result = main(["colour-library", "--format", "json"])

    assert result == 0
    assert render.call_args.args == ("json",)
    assert "huemiliator.colour_library.v1" in stdout.getvalue()


def test_render_colour_boundaries_prints_text_report() -> None:
    text = render_colour_boundaries(limit=1)

    assert "colour boundaries" in text
    assert "schema: huemiliator.colour_boundaries.v1" in text
    assert "minimum families: 3" in text
    assert "shown bins: 1" in text
    assert "Lab a*" in text
    assert "samples:" in text
    assert "family samples:" in text


def test_render_colour_boundaries_can_emit_json_packet() -> None:
    packet = json.loads(render_colour_boundaries(output_format="json", limit=2))

    assert packet["schema"] == "huemiliator.colour_boundaries.v1"
    assert packet["bin_step"] == 10
    assert packet["min_family_count"] == 3
    assert packet["samples_per_family"] == 3
    assert packet["shown_bin_count"] == 2
    assert packet["bins"][0]["family_count"] >= 3
    assert "samples" in packet["bins"][0]
    assert "family_samples" in packet["bins"][0]


def test_main_colour_boundaries_prints_text_report() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_colour_boundaries",
        return_value="colour boundaries\nshown bins: 2",
    ) as render:
        with redirect_stdout(stdout):
            result = main(["colour-boundaries", "--limit", "2"])

    assert result == 0
    assert render.call_args.kwargs == {
        "output_format": "text",
        "limit": 2,
        "bin_step": 10,
        "min_families": 3,
        "samples_per_family": 3,
    }
    assert "shown bins: 2" in stdout.getvalue()


def test_main_colour_boundaries_accepts_json_and_parameters() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_colour_boundaries",
        return_value='{"schema": "huemiliator.colour_boundaries.v1"}',
    ) as render:
        with redirect_stdout(stdout):
            result = main(
                [
                    "colour-boundaries",
                    "--format",
                    "json",
                    "--limit",
                    "4",
                    "--bin-step",
                    "20",
                    "--min-families",
                    "2",
                    "--samples-per-family",
                    "1",
                ]
            )

    assert result == 0
    assert render.call_args.kwargs == {
        "output_format": "json",
        "limit": 4,
        "bin_step": 20,
        "min_families": 2,
        "samples_per_family": 1,
    }
    assert "huemiliator.colour_boundaries.v1" in stdout.getvalue()


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


def test_render_behaviour_facts_exposes_fixed_runtime_fact_packet() -> None:
    text = render_behaviour_facts("#d9a6a1")

    assert "behaviour eval facts" in text
    assert "input: #d9a6a1" in text
    assert "nearest swatch:" in text
    assert "family:" in text
    assert "replacement shade:" in text
    assert "loss line:" in text
    assert "eval target: language fidelity, tone fit, evidence fit, consistency" in text


def test_render_behaviour_facts_can_emit_json_packet() -> None:
    packet = json.loads(render_behaviour_facts("#d9a6a1", "json"))

    assert packet["schema"] == "huemiliator.behaviour_facts.v1"
    assert packet["input"]["hex"] == "#d9a6a1"
    assert packet["runtime_facts"]["nearest_swatch"]["name"] == "Mellow rose"
    assert packet["runtime_facts"]["family"] == "red"
    assert packet["runtime_facts"]["replacement"]["name"] == "Ash rose"
    assert packet["runtime_facts"]["loss_line"]
    assert packet["response_contract"]["eval_targets"] == [
        "language fidelity",
        "tone fit",
        "evidence fit",
        "consistency",
    ]


def test_main_behaviour_facts_prints_fact_packet() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_behaviour_facts",
        return_value="behaviour eval facts\nfamily: red",
    ) as render:
        with redirect_stdout(stdout):
            result = main(["behaviour-facts", "#d9a6a1"])

    assert result == 0
    assert render.call_args.args == ("#d9a6a1", "text")
    assert "family: red" in stdout.getvalue()


def test_main_behaviour_facts_accepts_json_format() -> None:
    stdout = io.StringIO()
    with patch(
        "huemiliator.main.render_behaviour_facts",
        return_value='{"schema": "huemiliator.behaviour_facts.v1"}',
    ) as render:
        with redirect_stdout(stdout):
            result = main(["behaviour-facts", "#d9a6a1", "--format", "json"])

    assert result == 0
    assert render.call_args.args == ("#d9a6a1", "json")
    assert "huemiliator.behaviour_facts.v1" in stdout.getvalue()


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
