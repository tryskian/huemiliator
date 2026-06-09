from __future__ import annotations

import argparse
import sqlite3
import sys

from huemiliator.agent import RUNTIME_CONTRACT_LINES, TAGLINE
from huemiliator.config import load_settings
from huemiliator.eval_db import (
    LIST_VERDICTS,
    PULSE_EXCLUSION_REASONS,
    PULSE_LABELS,
    counts,
    get_output,
    init_db,
    judge_output,
    label_pulse_row,
    list_outputs,
    quarantine_live_surface,
    record_one_up_state,
    summarize_pulse_range,
)
from huemiliator.eval_sampling import (
    LOCAL_SAMPLE_PATTERNS,
    sample_input_hex_eval_outputs,
    sample_local_eval_outputs,
)
from huemiliator.eval_scope import EVAL_SCOPE_NAMES, describe_eval_scope
from huemiliator.picker import PickerError, pick_hex
from huemiliator.pipeline import build_one_up_state
from huemiliator.resolution import ResolutionError
from huemiliator.swatches import SwatchDatasetError, load_swatch_snapshot


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="huemiliator")
    subparsers = parser.add_subparsers(dest="command", required=False)

    subparsers.add_parser("status", help="Show the current runtime state.")
    subparsers.add_parser("contract", help="Show the current runtime contract.")
    subparsers.add_parser("pick", help="Open the native macOS colour picker.")

    resolve_parser = subparsers.add_parser(
        "resolve",
        help="Resolve a hex value to the nearest frozen swatch.",
    )
    resolve_parser.add_argument("hex_value", help="Hex value to resolve.")

    replace_parser = subparsers.add_parser(
        "replace",
        help="Resolve a hex value and emit the deterministic replacement swatch.",
    )
    replace_parser.add_argument("hex_value", help="Hex value to replace.")

    one_up_parser = subparsers.add_parser(
        "one-up",
        help="Emit the deterministic replacement shade and short loss line.",
    )
    one_up_parser.add_argument("hex_value", help="Hex value to one-up.")

    subparsers.add_parser(
        "eval-init",
        help="Initialise the local SQLite eval database.",
    )

    eval_log_parser = subparsers.add_parser(
        "eval-log",
        help="Record a deterministic one-up output in the local eval database.",
    )
    eval_log_parser.add_argument("hex_value", help="Hex value to log.")

    eval_list_parser = subparsers.add_parser(
        "eval-list",
        help="List recent deterministic one-up outputs from the local eval database.",
    )
    eval_list_parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of rows to show.",
    )
    eval_list_parser.add_argument(
        "--verdict",
        choices=LIST_VERDICTS,
        default=None,
        help="Filter rows by verdict state.",
    )
    eval_list_parser.add_argument(
        "--family",
        choices=EVAL_SCOPE_NAMES,
        default=None,
        help="Filter rows by Huemiliator family or local cohort.",
    )

    eval_judge_parser = subparsers.add_parser(
        "eval-judge",
        help="Apply a human PASS/FAIL verdict to one logged eval output.",
    )
    eval_judge_parser.add_argument("output_id", type=int, help="Eval output id.")
    eval_judge_parser.add_argument("verdict", choices=("pass", "fail"))
    eval_judge_parser.add_argument("--note", default="", help="Optional human note.")

    eval_pulse_start_parser = subparsers.add_parser(
        "eval-pulse-start",
        help="Quarantine the current live surface if needed and seed a bounded pulse.",
    )
    eval_pulse_start_parser.add_argument(
        "--count",
        type=int,
        default=None,
        help="Number of rows to seed into the bounded pulse.",
    )
    eval_pulse_start_parser.add_argument(
        "--input-hex",
        action="append",
        default=None,
        help=(
            "Seed this exact input hex into the bounded pulse. Repeat for "
            "the target pulse rows."
        ),
    )
    eval_pulse_start_parser.add_argument(
        "--interval-seconds",
        type=float,
        default=0.0,
        help="Pause between seeded rows. Defaults to 0 seconds.",
    )
    eval_pulse_start_parser.add_argument(
        "--pattern",
        choices=LOCAL_SAMPLE_PATTERNS,
        default="source-order",
        help="Local swatch sampling pattern.",
    )
    eval_pulse_start_parser.add_argument(
        "--family",
        choices=EVAL_SCOPE_NAMES,
        default="red",
        help="Restrict the seeded pulse to one Huemiliator family or local cohort.",
    )
    eval_pulse_start_parser.add_argument(
        "--start-source-order",
        type=int,
        default=1,
        help="First swatch source-order position to sample from.",
    )
    eval_pulse_start_parser.add_argument(
        "--quarantine-label",
        default=None,
        help=(
            "Required when a live proof surface already exists and must be "
            "archived locally first."
        ),
    )

    eval_pulse_label_parser = subparsers.add_parser(
        "eval-pulse-label",
        help="Label one pulse row as anchor, counted seam, or excluded noise.",
    )
    eval_pulse_label_parser.add_argument("output_id", type=int, help="Eval output id.")
    eval_pulse_label_parser.add_argument("label", choices=PULSE_LABELS)
    eval_pulse_label_parser.add_argument(
        "--reason",
        choices=PULSE_EXCLUSION_REASONS,
        default="",
        help="Required when label=excluded_noise.",
    )

    eval_pulse_report_parser = subparsers.add_parser(
        "eval-pulse-report",
        help="Summarize one bounded pulse by output-id range.",
    )
    eval_pulse_report_parser.add_argument(
        "start_output_id", type=int, help="First output id in the pulse."
    )
    eval_pulse_report_parser.add_argument(
        "end_output_id", type=int, help="Last output id in the pulse."
    )

    eval_sample_local_parser = subparsers.add_parser(
        "eval-sample-local",
        help="Append deterministic local eval rows over time.",
    )
    eval_sample_local_group = eval_sample_local_parser.add_mutually_exclusive_group(
        required=True
    )
    eval_sample_local_group.add_argument("--count", type=int)
    eval_sample_local_group.add_argument("--duration-seconds", type=float)
    eval_sample_local_parser.add_argument(
        "--interval-seconds",
        type=float,
        default=3.0,
        help="Pause between logged rows. Defaults to 3 seconds.",
    )
    eval_sample_local_parser.add_argument(
        "--pattern",
        choices=LOCAL_SAMPLE_PATTERNS,
        default="source-order",
        help="Local swatch sampling pattern.",
    )
    eval_sample_local_parser.add_argument(
        "--family",
        choices=EVAL_SCOPE_NAMES,
        default=None,
        help="Restrict the sampler to one Huemiliator family or local cohort.",
    )
    eval_sample_local_parser.add_argument(
        "--start-source-order",
        type=int,
        default=1,
        help="First swatch source-order position to sample from.",
    )
    return parser


def render_status() -> str:
    settings = load_settings()
    lines = [settings.app_name.lower(), TAGLINE, ""]
    lines.extend(RUNTIME_CONTRACT_LINES)
    return "\n".join(lines)


def render_contract() -> str:
    return "\n".join(RUNTIME_CONTRACT_LINES)


def render_resolution(hex_value: str) -> str:
    settings = load_settings()
    dataset = load_swatch_snapshot(settings.swatch_snapshot_path)
    state = build_one_up_state(hex_value, dataset)
    lines = [
        f"input: {state.resolution.input_hex}",
        f"nearest swatch: {state.resolution.matched.name}",
        f"swatch hex: {state.resolution.matched.hex}",
        f"family: {state.current.family}",
        f"family rank: {state.current.family_rank}/{state.current.family_size}",
        f"source order: {state.resolution.matched.source_order}",
        f"distance (delta-e-cie76): {state.resolution.distance:.4f}",
    ]
    return "\n".join(lines)


def render_replacement(hex_value: str) -> str:
    settings = load_settings()
    dataset = load_swatch_snapshot(settings.swatch_snapshot_path)
    state = build_one_up_state(hex_value, dataset)
    lines = [
        f"input: {state.resolution.input_hex}",
        f"nearest swatch: {state.current.swatch.name}",
        f"family: {state.current.family}",
        f"current rank: {state.current.family_rank}/{state.current.family_size}",
        f"replacement shade: {state.replacement.swatch.name}",
        f"replacement hex: {state.replacement.swatch.hex}",
        (
            "replacement rank: "
            f"{state.replacement.family_rank}/{state.replacement.family_size}"
        ),
    ]
    return "\n".join(lines)


def render_one_up(hex_value: str) -> str:
    settings = load_settings()
    dataset = load_swatch_snapshot(settings.swatch_snapshot_path)
    state = build_one_up_state(hex_value, dataset)
    lines = [
        f"input: {state.resolution.input_hex}",
        f"replacement shade: {state.replacement.swatch.name}",
        f"replacement hex: {state.replacement.swatch.hex}",
        state.loss_line,
    ]
    return "\n".join(lines)


def render_eval_init() -> str:
    settings = load_settings()
    init_db(settings.eval_db_path)
    return f"Initialised {settings.eval_db_path}"


def render_eval_log(hex_value: str) -> str:
    settings = load_settings()
    dataset = load_swatch_snapshot(settings.swatch_snapshot_path)
    state = build_one_up_state(hex_value, dataset)
    output_id = record_one_up_state(settings.eval_db_path, state)
    lines = [
        f"logged output: {output_id}",
        f"db: {settings.eval_db_path}",
        f"input: {state.resolution.input_hex}",
        f"nearest swatch: {state.current.swatch.name}",
        f"family: {state.current.family}",
        f"replacement shade: {state.replacement.swatch.name}",
        state.loss_line,
    ]
    return "\n".join(lines)


def _format_eval_row(row: sqlite3.Row) -> str:
    verdict = row["current_verdict"] or "pending"
    lines = [
        f"id: {row['id']}",
        f"input: {row['input_hex']}",
        f"nearest swatch: {row['nearest_swatch_name']}",
        f"family: {row['family']}",
        f"replacement shade: {row['replacement_shade_name']}",
        f"verdict: {verdict}",
        f"created_at: {row['created_at']}",
    ]
    note = row["current_note"]
    if note:
        lines.append(f"note: {note}")
    pulse_label = row["pulse_label"]
    if pulse_label:
        lines.append(f"pulse label: {pulse_label}")
    pulse_reason = row["pulse_reason"]
    if pulse_reason:
        lines.append(f"pulse reason: {pulse_reason}")
    return "\n".join(lines)


def render_eval_list(limit: int, verdict: str | None, family: str | None) -> str:
    settings = load_settings()
    summary = counts(settings.eval_db_path, family=family)
    rows = list_outputs(
        settings.eval_db_path, limit=limit, verdict=verdict, family=family
    )
    prefix = "eval counts"
    if family is not None:
        prefix += f" ({describe_eval_scope(family)})"
    lines = [
        f"{prefix}: "
        f"total={summary['total']} pass={summary['pass']} "
        f"fail={summary['fail']} pending={summary['pending']}"
    ]
    if not rows:
        if summary["total"] == 0:
            lines.append("")
            lines.append("No eval outputs logged yet.")
        elif verdict is None:
            lines.append("")
            lines.append("No eval outputs found.")
        else:
            lines.append("")
            if family is None:
                lines.append(f"No {verdict} eval outputs.")
            else:
                lines.append(
                    f"No {verdict} eval outputs for {describe_eval_scope(family)}."
                )
        return "\n".join(lines)

    lines.append("")
    lines.extend(
        _format_eval_row(row) if index == 0 else f"\n{_format_eval_row(row)}"
        for index, row in enumerate(rows)
    )
    return "\n".join(lines)


def render_eval_judge(output_id: int, verdict: str, note: str) -> str:
    settings = load_settings()
    judge_output(settings.eval_db_path, output_id, verdict, note)
    row = get_output(settings.eval_db_path, output_id)
    lines = [
        f"judged output {output_id}: {verdict}",
    ]
    if note:
        lines.append(f"note: {note}")
    lines.append("")
    lines.append(_format_eval_row(row))
    return "\n".join(lines)


def render_eval_pulse_start(
    *,
    count: int | None,
    input_hexes: tuple[str, ...] = (),
    interval_seconds: float,
    pattern: str,
    family: str,
    start_source_order: int,
    quarantine_label: str | None,
) -> str:
    settings = load_settings()
    explicit_input_hexes = tuple(input_hexes)
    if count is None and not explicit_input_hexes:
        raise ValueError("Provide --count or at least one --input-hex.")
    if count is not None and explicit_input_hexes:
        raise ValueError("Choose either --count or --input-hex, not both.")
    if explicit_input_hexes and (
        pattern != "source-order" or family != "red" or start_source_order != 1
    ):
        raise ValueError(
            "Explicit input-hex pulses cannot use --pattern, --family, "
            "or --start-source-order."
        )

    live_summary = counts(settings.eval_db_path)
    if explicit_input_hexes:
        lines = [
            f"bounded pulse start: input_hexes={len(explicit_input_hexes)}",
            "mode=explicit-input-hex",
            f"interval_seconds={interval_seconds:g}",
        ]
    else:
        assert count is not None
        lines = [
            f"bounded pulse start: count={count}",
            describe_eval_scope(family),
            f"pattern={pattern}",
            f"start_source_order={start_source_order}",
            f"interval_seconds={interval_seconds:g}",
        ]

    if live_summary["total"] != 0:
        if quarantine_label is None:
            raise ValueError(
                "Live eval surface is not empty. Provide --quarantine-label before "
                "starting a new bounded pulse."
            )
        parked_dir = settings.eval_db_path.parent / "parked"
        archived = quarantine_live_surface(
            settings.eval_db_path,
            parked_dir=parked_dir,
            label=quarantine_label,
        )
        lines.append(
            "quarantined live surface: "
            f"total={archived.total_rows} "
            f"ids={archived.first_output_id}-{archived.last_output_id}"
        )
        lines.append(f"archive={archived.archive_path}")

    if explicit_input_hexes:
        summary = sample_input_hex_eval_outputs(
            input_hexes=explicit_input_hexes,
            interval_seconds=interval_seconds,
        )
    else:
        summary = sample_local_eval_outputs(
            count=count,
            interval_seconds=interval_seconds,
            pattern=pattern,
            family=family,
            start_source_order=start_source_order,
        )
    lines.append(f"recorded={summary.recorded}")
    lines.append(f"elapsed_seconds={summary.elapsed_seconds:.2f}")
    if summary.first_output_id is not None and summary.last_output_id is not None:
        lines.append(
            f"output_ids={summary.first_output_id}-{summary.last_output_id} "
            f"db={settings.eval_db_path}"
        )
    return "\n".join(lines)


def render_eval_pulse_label(output_id: int, label: str, reason: str) -> str:
    settings = load_settings()
    label_pulse_row(settings.eval_db_path, output_id, label, reason)
    row = get_output(settings.eval_db_path, output_id)
    lines = [f"pulse labeled output {output_id}: {label}"]
    if reason:
        lines.append(f"reason: {reason}")
    lines.append("")
    lines.append(_format_eval_row(row))
    return "\n".join(lines)


def render_eval_pulse_report(start_output_id: int, end_output_id: int) -> str:
    settings = load_settings()
    summary = summarize_pulse_range(
        settings.eval_db_path,
        start_output_id,
        end_output_id,
    )
    verdict = "incomplete" if summary.verdict is None else summary.verdict
    lines = [
        f"pulse ids: {summary.start_output_id}-{summary.end_output_id}",
        f"raw rows: {summary.raw_rows}",
        f"anchors: {summary.anchors}",
        f"counted seams: {summary.counted_seams}",
        f"excluded noise: {summary.excluded_noise}",
        (
            "excluded by reason: "
            f"operator_artifact={summary.excluded_by_reason['operator_artifact']} "
            f"off_target_failure="
            f"{summary.excluded_by_reason['off_target_failure']}"
        ),
        f"unlabeled rows: {summary.unlabeled_rows}",
        f"counted total: {summary.counted_total}",
        f"pulse verdict: {verdict}",
    ]
    return "\n".join(lines)


def render_eval_sample_local(
    *,
    count: int | None,
    duration_seconds: float | None,
    interval_seconds: float,
    pattern: str,
    family: str | None,
    start_source_order: int,
) -> str:
    summary = sample_local_eval_outputs(
        count=count,
        duration_seconds=duration_seconds,
        interval_seconds=interval_seconds,
        pattern=pattern,
        family=family,
        start_source_order=start_source_order,
    )
    mode_label = (
        f"count={count}"
        if count is not None
        else f"duration_seconds={duration_seconds:g}"
    )
    settings = load_settings()
    lines = [
        f"local eval sample complete: {mode_label}",
        f"pattern={pattern}",
        f"start_source_order={start_source_order}",
        f"interval_seconds={interval_seconds:g}",
        f"recorded={summary.recorded}",
        f"elapsed_seconds={summary.elapsed_seconds:.2f}",
    ]
    if family is not None:
        lines.insert(2, describe_eval_scope(family))
    if summary.first_output_id is not None and summary.last_output_id is not None:
        lines.append(
            f"output_ids={summary.first_output_id}-{summary.last_output_id} "
            f"db={settings.eval_db_path}"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "contract":
        print(render_contract())
        return 0
    if args.command == "pick":
        try:
            print(pick_hex())
        except PickerError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "resolve":
        try:
            print(render_resolution(args.hex_value))
        except (ResolutionError, SwatchDatasetError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "replace":
        try:
            print(render_replacement(args.hex_value))
        except (ResolutionError, SwatchDatasetError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "one-up":
        try:
            print(render_one_up(args.hex_value))
        except (ResolutionError, SwatchDatasetError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-init":
        try:
            print(render_eval_init())
        except OSError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-log":
        try:
            print(render_eval_log(args.hex_value))
        except (ResolutionError, SwatchDatasetError, ValueError, OSError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-list":
        try:
            print(render_eval_list(args.limit, args.verdict, args.family))
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-judge":
        try:
            print(render_eval_judge(args.output_id, args.verdict, args.note))
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-pulse-start":
        try:
            print(
                render_eval_pulse_start(
                    count=args.count,
                    input_hexes=tuple(args.input_hex or ()),
                    interval_seconds=args.interval_seconds,
                    pattern=args.pattern,
                    family=args.family,
                    start_source_order=args.start_source_order,
                    quarantine_label=args.quarantine_label,
                )
            )
        except (ValueError, ResolutionError, SwatchDatasetError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-pulse-label":
        try:
            print(render_eval_pulse_label(args.output_id, args.label, args.reason))
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-pulse-report":
        try:
            print(
                render_eval_pulse_report(
                    args.start_output_id,
                    args.end_output_id,
                )
            )
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.command == "eval-sample-local":
        try:
            print(
                render_eval_sample_local(
                    count=args.count,
                    duration_seconds=args.duration_seconds,
                    interval_seconds=args.interval_seconds,
                    pattern=args.pattern,
                    family=args.family,
                    start_source_order=args.start_source_order,
                )
            )
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0

    print(render_status())
    return 0
