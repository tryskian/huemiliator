from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from huemiliator.config import EVAL_DB_PATH  # noqa: E402
from huemiliator.eval_db import counts  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report Huemiliator eval totals and enforce pending=0 when needed."
    )
    parser.add_argument(
        "--require-zero-pending",
        action="store_true",
        help="Fail if the live eval surface has pending rows.",
    )
    return parser.parse_args()


def load_counts() -> dict[str, int] | None:
    if not EVAL_DB_PATH.exists():
        return None
    return counts(EVAL_DB_PATH)


def render_counts(summary: dict[str, int]) -> str:
    return (
        f"total={summary['total']} pass={summary['pass']} "
        f"fail={summary['fail']} pending={summary['pending']}"
    )


def main() -> int:
    args = parse_args()
    summary = load_counts()

    if not args.require_zero_pending:
        if summary is None:
            print(f"evals: no db at {EVAL_DB_PATH}")
            return 0
        print(f"evals: {render_counts(summary)}")
        return 0

    if summary is None:
        print(f"end-pending-check: PASS (no eval db at {EVAL_DB_PATH}; pending=0)")
        return 0

    if summary["pending"] != 0:
        print("end-pending-check: FAIL", file=sys.stderr)
        print(f"- eval pending count is {summary['pending']}", file=sys.stderr)
        print(f"- totals: {render_counts(summary)}", file=sys.stderr)
        print(
            "Resolve or quarantine pending eval rows before rerunning make end.",
            file=sys.stderr,
        )
        return 1

    print(f"end-pending-check: PASS ({render_counts(summary)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
