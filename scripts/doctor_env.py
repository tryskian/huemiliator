from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from huemiliator.config import EVAL_DB_PATH  # noqa: E402


def main() -> int:
    print(f"repo: {ROOT}")
    print(f"python: {sys.version.split()[0]}")
    print(
        f".env.example: {'present' if (ROOT / '.env.example').exists() else 'missing'}"
    )
    print("runtime: picker + swatch resolution + family rank + one-up + eval + sampler")
    print(f"eval db path: {EVAL_DB_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
