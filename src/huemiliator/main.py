from __future__ import annotations

import argparse
import sqlite3
import sys

from huemiliator.config import TAGLINE, load_settings
from huemiliator.eval_db import (
    LIST_VERDICTS,
    counts,
    get_output,
    init_db,
    judge_output,
    list_outputs,
    record_one_up_state,
)
from huemiliator.eval_sampling import LOCAL_SAMPLE_PATTERNS, sample_local_eval_outputs
from huemiliator.eval_scope import EVAL_SCOPE_NAMES, describe_eval_scope
from huemiliator.picker import PickerError, pick_hex
from huemiliator.pipeline import build_one_up_state
from huemiliator.resolution import ResolutionError
from huemiliator.swatches import SwatchDatasetError, load_swatch_snapshot

STATUS_LINES: tuple[str, ...] = (
    "status: partial runtime",
    "platform: macos local only",
    "runtime: native colour picker -> canonical hex",
    "input: native colour picker hex",
    "swatch snapshot: frozen local margaret2 reference",
    "swatch resolution: nearest snapshot match",
    "distance rule: delta-e cie76 with source-order tie-break",
    "family routing: fixed neutral and hue thresholds",
    "same-family rank: fixed strength ladder",
    "transform: next same-family rank with top-rank clamp",
    "line: fixed family loss bank",
    "evidence: local sqlite eval db",
    "sampler: long-run local source-order or scoped cohort cycle",
    "eval: binary pass/fail",
)


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
    lines.extend(STATUS_LINES)
    return "\n".join(lines)


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
