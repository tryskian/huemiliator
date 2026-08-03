from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any

from huemiliator.colour_library import ColourLibraryRow, build_colour_library_rows
from huemiliator.families import FAMILY_NAMES
from huemiliator.swatches import SwatchDataset


@dataclass(frozen=True)
class BoundaryFamilyCount:
    family: str
    count: int


@dataclass(frozen=True)
class BoundarySample:
    source_order: int
    name: str
    hex: str
    family: str


@dataclass(frozen=True)
class BoundaryFamilySamples:
    family: str
    samples: tuple[BoundarySample, ...]


@dataclass(frozen=True)
class BoundaryBin:
    lab_a_min: int
    lab_a_max: int
    lab_b_min: int
    lab_b_max: int
    swatch_count: int
    family_counts: tuple[BoundaryFamilyCount, ...]
    samples: tuple[BoundarySample, ...]
    family_samples: tuple[BoundaryFamilySamples, ...]

    @property
    def family_count(self) -> int:
        return len(self.family_counts)


def build_boundary_bins(
    rows: tuple[ColourLibraryRow, ...],
    *,
    bin_step: int = 10,
    min_family_count: int = 2,
    sample_limit: int = 8,
    samples_per_family: int = 3,
) -> tuple[BoundaryBin, ...]:
    _validate_boundary_params(
        bin_step=bin_step,
        min_family_count=min_family_count,
        sample_limit=sample_limit,
        samples_per_family=samples_per_family,
    )

    grouped: dict[tuple[int, int], list[ColourLibraryRow]] = defaultdict(list)
    for row in rows:
        lab_a_min = math.floor(row.metrics.lab_a / bin_step) * bin_step
        lab_b_min = math.floor(row.metrics.lab_b / bin_step) * bin_step
        grouped[(lab_a_min, lab_b_min)].append(row)

    bins: list[BoundaryBin] = []
    for (lab_a_min, lab_b_min), members in grouped.items():
        family_counts = _family_counts(members)
        if len(family_counts) < min_family_count:
            continue
        samples = tuple(
            BoundarySample(
                source_order=row.source_order,
                name=row.name,
                hex=row.hex,
                family=row.family,
            )
            for row in sorted(members, key=lambda item: item.source_order)[
                :sample_limit
            ]
        )
        bins.append(
            BoundaryBin(
                lab_a_min=lab_a_min,
                lab_a_max=lab_a_min + bin_step,
                lab_b_min=lab_b_min,
                lab_b_max=lab_b_min + bin_step,
                swatch_count=len(members),
                family_counts=family_counts,
                samples=samples,
                family_samples=_family_samples(
                    members,
                    family_counts,
                    samples_per_family=samples_per_family,
                ),
            )
        )

    return tuple(
        sorted(
            bins,
            key=lambda item: (
                -item.family_count,
                -item.swatch_count,
                item.lab_a_min,
                item.lab_b_min,
            ),
        )
    )


def build_colour_boundary_packet(
    dataset: SwatchDataset,
    *,
    bin_step: int = 10,
    min_family_count: int = 3,
    limit: int = 10,
    sample_limit: int = 8,
    samples_per_family: int = 3,
) -> dict[str, Any]:
    rows = build_colour_library_rows(dataset)
    bins = build_boundary_bins(
        rows,
        bin_step=bin_step,
        min_family_count=min_family_count,
        sample_limit=sample_limit,
        samples_per_family=samples_per_family,
    )
    if limit < 1:
        raise ValueError("Boundary report limit must be at least 1.")
    return {
        "schema": "huemiliator.colour_boundaries.v1",
        "source": {
            "name": dataset.source.name,
            "snapshot_date": dataset.source.snapshot_date,
            "swatch_count": len(rows),
        },
        "bin_step": bin_step,
        "min_family_count": min_family_count,
        "samples_per_family": samples_per_family,
        "mixed_bin_count": len(bins),
        "shown_bin_count": min(limit, len(bins)),
        "bins": [_boundary_bin_payload(item) for item in bins[:limit]],
    }


def _validate_boundary_params(
    *,
    bin_step: int,
    min_family_count: int,
    sample_limit: int,
    samples_per_family: int,
) -> None:
    if bin_step < 1:
        raise ValueError("Boundary report bin step must be at least 1.")
    if min_family_count < 2:
        raise ValueError("Boundary report min family count must be at least 2.")
    if sample_limit < 1:
        raise ValueError("Boundary report sample limit must be at least 1.")
    if samples_per_family < 1:
        raise ValueError("Boundary report samples per family must be at least 1.")


def _family_counts(
    members: list[ColourLibraryRow],
) -> tuple[BoundaryFamilyCount, ...]:
    counts = Counter(row.family for row in members)
    return tuple(
        BoundaryFamilyCount(family=family, count=count)
        for family, count in sorted(
            counts.items(),
            key=lambda item: (-item[1], FAMILY_NAMES.index(item[0])),
        )
    )


def _family_samples(
    members: list[ColourLibraryRow],
    family_counts: tuple[BoundaryFamilyCount, ...],
    *,
    samples_per_family: int,
) -> tuple[BoundaryFamilySamples, ...]:
    rows_by_family: dict[str, list[ColourLibraryRow]] = defaultdict(list)
    for row in sorted(members, key=lambda item: item.source_order):
        rows_by_family[row.family].append(row)

    return tuple(
        BoundaryFamilySamples(
            family=item.family,
            samples=tuple(
                BoundarySample(
                    source_order=row.source_order,
                    name=row.name,
                    hex=row.hex,
                    family=row.family,
                )
                for row in rows_by_family[item.family][:samples_per_family]
            ),
        )
        for item in family_counts
    )


def _boundary_bin_payload(boundary_bin: BoundaryBin) -> dict[str, Any]:
    return {
        "lab_a": {
            "min": boundary_bin.lab_a_min,
            "max": boundary_bin.lab_a_max,
        },
        "lab_b": {
            "min": boundary_bin.lab_b_min,
            "max": boundary_bin.lab_b_max,
        },
        "swatch_count": boundary_bin.swatch_count,
        "family_count": boundary_bin.family_count,
        "families": [
            {"family": item.family, "count": item.count}
            for item in boundary_bin.family_counts
        ],
        "samples": [
            {
                "source_order": item.source_order,
                "name": item.name,
                "hex": item.hex,
                "family": item.family,
            }
            for item in boundary_bin.samples
        ],
        "family_samples": [
            {
                "family": item.family,
                "samples": [
                    {
                        "source_order": sample.source_order,
                        "name": sample.name,
                        "hex": sample.hex,
                        "family": sample.family,
                    }
                    for sample in item.samples
                ],
            }
            for item in boundary_bin.family_samples
        ],
    }
