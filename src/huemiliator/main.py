from __future__ import annotations

import argparse
import sys

from huemiliator.config import TAGLINE, load_settings
from huemiliator.picker import PickerError, pick_hex
from huemiliator.resolution import ResolutionError, resolve_nearest_swatch
from huemiliator.swatches import SwatchDatasetError, load_swatch_snapshot

STATUS_LINES: tuple[str, ...] = (
    "status: partial runtime",
    "platform: macos local only",
    "runtime: native colour picker -> canonical hex",
    "input: native colour picker hex",
    "swatch snapshot: frozen local margaret2 reference",
    "swatch resolution: nearest snapshot match",
    "distance rule: delta-e cie76 with source-order tie-break",
    "family routing: not implemented yet",
    "transform: not implemented yet",
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
    return parser


def render_status() -> str:
    settings = load_settings()
    lines = [settings.app_name.lower(), TAGLINE, ""]
    lines.extend(STATUS_LINES)
    return "\n".join(lines)


def render_resolution(hex_value: str) -> str:
    settings = load_settings()
    dataset = load_swatch_snapshot(settings.swatch_snapshot_path)
    resolution = resolve_nearest_swatch(hex_value, dataset)
    lines = [
        f"input: {resolution.input_hex}",
        f"nearest swatch: {resolution.matched.name}",
        f"swatch hex: {resolution.matched.hex}",
        f"source order: {resolution.matched.source_order}",
        f"distance (delta-e-cie76): {resolution.distance:.4f}",
    ]
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

    print(render_status())
    return 0
