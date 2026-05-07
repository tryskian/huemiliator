from __future__ import annotations

import json
from datetime import date
from urllib.request import urlopen

from huemiliator.config import load_settings
from huemiliator.swatches import SOURCE_URL, build_snapshot_payload, parse_source_html


def fetch_source_html(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode("utf-8")


def main() -> int:
    settings = load_settings()
    target_path = settings.swatch_snapshot_path
    target_path.parent.mkdir(parents=True, exist_ok=True)

    html = fetch_source_html(SOURCE_URL)
    swatches = parse_source_html(html)
    payload = build_snapshot_payload(
        swatches,
        snapshot_date=date.today().isoformat(),
    )
    target_path.write_text(
        json.dumps(payload, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(swatches)} swatches to {target_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
