from __future__ import annotations

import argparse
import sys

from huemiliator.config import TAGLINE, load_settings
from huemiliator.picker import PickerError, pick_hex

STATUS_LINES: tuple[str, ...] = (
    "status: partial runtime",
    "platform: macos local only",
    "runtime: native colour picker -> canonical hex",
    "input: native colour picker hex",
    "swatch resolution: not implemented yet",
    "transform: not implemented yet",
    "eval: binary pass/fail",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="huemiliator")
    parser.add_argument(
        "command",
        nargs="?",
        choices=("status", "contract", "pick"),
        default="status",
        help="Show the current runtime state or open the native picker.",
    )
    return parser


def render_status() -> str:
    settings = load_settings()
    lines = [settings.app_name.lower(), TAGLINE, ""]
    lines.extend(STATUS_LINES)
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

    print(render_status())
    return 0
