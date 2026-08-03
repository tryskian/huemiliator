from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from huemiliator.colour_math import ColourMetrics
from huemiliator.families import (
    FAMILY_NAMES,
    build_family_rank_index,
    classify_swatch,
)
from huemiliator.swatches import SwatchDataset


@dataclass(frozen=True)
class ColourLibraryRow:
    source_order: int
    slug: str
    name: str
    hex: str
    family: str
    family_rank: int
    family_size: int
    metrics: ColourMetrics


def build_colour_library_rows(dataset: SwatchDataset) -> tuple[ColourLibraryRow, ...]:
    ranked_index = build_family_rank_index(dataset)
    rows: list[ColourLibraryRow] = []
    for swatch in dataset.swatches:
        ranked = ranked_index[swatch.source_order]
        assignment = classify_swatch(swatch)
        rows.append(
            ColourLibraryRow(
                source_order=swatch.source_order,
                slug=swatch.slug,
                name=swatch.name,
                hex=swatch.hex,
                family=ranked.family,
                family_rank=ranked.family_rank,
                family_size=ranked.family_size,
                metrics=assignment.metrics,
            )
        )
    return tuple(rows)


def build_colour_library_packet(dataset: SwatchDataset) -> dict[str, Any]:
    rows = build_colour_library_rows(dataset)
    return {
        "schema": "huemiliator.colour_library.v1",
        "source": {
            "name": dataset.source.name,
            "url": dataset.source.url,
            "snapshot_date": dataset.source.snapshot_date,
            "upstream_status": dataset.source.upstream_status,
            "source_format": dataset.source.source_format,
            "swatch_count": len(rows),
        },
        "families": _family_count_payloads(rows),
        "swatches": [_row_payload(row) for row in rows],
    }


def _family_count_payloads(rows: tuple[ColourLibraryRow, ...]) -> list[dict[str, Any]]:
    counts = {family: 0 for family in FAMILY_NAMES}
    for row in rows:
        counts[row.family] += 1
    return [
        {
            "family": family,
            "count": counts[family],
        }
        for family in FAMILY_NAMES
    ]


def _row_payload(row: ColourLibraryRow) -> dict[str, Any]:
    return {
        "source_order": row.source_order,
        "slug": row.slug,
        "name": row.name,
        "hex": row.hex,
        "family": row.family,
        "family_rank": row.family_rank,
        "family_size": row.family_size,
        "metrics": {
            "hex_value": row.metrics.hex_value,
            "hue_degrees": round(row.metrics.hue_degrees, 6),
            "lightness": round(row.metrics.lightness, 6),
            "saturation": round(row.metrics.saturation, 6),
            "lab_lightness": round(row.metrics.lab_lightness, 6),
            "lab_a": round(row.metrics.lab_a, 6),
            "lab_b": round(row.metrics.lab_b, 6),
            "lab_chroma": round(row.metrics.lab_chroma, 6),
        },
    }
