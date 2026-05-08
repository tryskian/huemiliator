from __future__ import annotations

import sys
from pathlib import Path

from huemiliator.config import EVAL_DB_PATH


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    print(f"repo: {root}")
    print(f"python: {sys.version.split()[0]}")
    print(
        f".env.example: {'present' if (root / '.env.example').exists() else 'missing'}"
    )
    print("runtime: picker + swatch resolution + family rank + one-up + eval + sampler")
    print(f"eval db path: {EVAL_DB_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
