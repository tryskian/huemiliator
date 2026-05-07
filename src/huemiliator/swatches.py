from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SOURCE_URL = "https://margaret2.github.io/pantone-colors/"

ROW_PATTERN = re.compile(
    r'<tr><td class="(?P<slug>[^"]+)" data-clipboard-text="(?P<hex>#[0-9a-fA-F]{6})">'
    r"\s*</td>\s*<td>\s*(?P<name>[^<]+?)\s*</td></tr>"
)


class SwatchDatasetError(RuntimeError):
    """Raised when the frozen swatch dataset cannot be parsed or loaded."""


@dataclass(frozen=True)
class SwatchEntry:
    source_order: int
    slug: str
    name: str
    hex: str


@dataclass(frozen=True)
class SwatchSource:
    name: str
    url: str
    snapshot_date: str
    upstream_status: str
    source_format: str


@dataclass(frozen=True)
class SwatchDataset:
    source: SwatchSource
    swatches: tuple[SwatchEntry, ...]


def _normalise_hex(value: str) -> str:
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise SwatchDatasetError(f"Invalid swatch hex value: {value!r}")
    return value.lower()


def parse_source_html(html: str) -> tuple[SwatchEntry, ...]:
    rows = tuple(ROW_PATTERN.finditer(html))
    if not rows:
        raise SwatchDatasetError("No swatch rows were found in the source HTML.")

    swatches: list[SwatchEntry] = []
    for source_order, match in enumerate(rows, start=1):
        swatches.append(
            SwatchEntry(
                source_order=source_order,
                slug=match.group("slug").strip(),
                name=match.group("name").strip(),
                hex=_normalise_hex(match.group("hex")),
            )
        )
    return tuple(swatches)


def build_snapshot_payload(
    swatches: tuple[SwatchEntry, ...],
    *,
    snapshot_date: str,
) -> dict[str, Any]:
    return {
        "source": {
            "name": "margaret2 pantone colors",
            "url": SOURCE_URL,
            "snapshot_date": snapshot_date,
            "upstream_status": "archived read-only",
            "source_format": "html table rows with data-clipboard-text hex values",
            "swatch_count": len(swatches),
        },
        "swatches": [
            {
                "source_order": swatch.source_order,
                "slug": swatch.slug,
                "name": swatch.name,
                "hex": swatch.hex,
            }
            for swatch in swatches
        ],
    }


def load_swatch_snapshot(path: Path) -> SwatchDataset:
    payload = json.loads(path.read_text(encoding="utf-8"))
    try:
        source_payload = payload["source"]
        swatch_payloads = payload["swatches"]
    except KeyError as exc:
        raise SwatchDatasetError(
            f"Missing required dataset key: {exc.args[0]}"
        ) from exc

    source = SwatchSource(
        name=str(source_payload["name"]),
        url=str(source_payload["url"]),
        snapshot_date=str(source_payload["snapshot_date"]),
        upstream_status=str(source_payload["upstream_status"]),
        source_format=str(source_payload["source_format"]),
    )
    swatches = tuple(
        SwatchEntry(
            source_order=int(item["source_order"]),
            slug=str(item["slug"]),
            name=str(item["name"]),
            hex=_normalise_hex(str(item["hex"])),
        )
        for item in swatch_payloads
    )
    return SwatchDataset(source=source, swatches=swatches)
