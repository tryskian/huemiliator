from __future__ import annotations

import argparse

from huemiliator.config import TAGLINE, load_settings

STATUS_LINES: tuple[str, ...] = (
    "status: scaffold only",
    "runtime: not implemented yet",
    "input: native colour picker hex",
    "resolution: nearest pantone match",
    "transform: same-family deterministic one-up",
    "eval: binary pass/fail",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="huemiliator")
    parser.add_argument(
        "command",
        nargs="?",
        choices=("status", "contract"),
        default="status",
        help="Show the current scaffold state.",
    )
    return parser


def render_status() -> str:
    settings = load_settings()
    lines = [settings.app_name.lower(), TAGLINE, ""]
    lines.extend(STATUS_LINES)
    return "\n".join(lines)


def main() -> int:
    parser = build_parser()
    parser.parse_args()
    print(render_status())
    return 0
