from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from huemiliator.config import EVAL_DB_PATH, SWATCH_SNAPSHOT_PATH
from huemiliator.eval_db import record_one_up_state
from huemiliator.families import FAMILY_NAMES, classify_family
from huemiliator.pipeline import build_one_up_state
from huemiliator.swatches import SwatchDataset, SwatchEntry, load_swatch_snapshot

LOCAL_SAMPLE_PATTERNS: tuple[str, ...] = ("source-order",)


@dataclass(frozen=True)
class EvalSampleSummary:
    recorded: int
    first_output_id: int | None
    last_output_id: int | None
    elapsed_seconds: float


def _default_dataset() -> SwatchDataset:
    return load_swatch_snapshot(SWATCH_SNAPSHOT_PATH)


def _sample_swatches_for_pattern(
    dataset: SwatchDataset,
    pattern: str,
) -> tuple[SwatchEntry, ...]:
    if pattern == "source-order":
        return dataset.swatches
    raise ValueError(
        "Unsupported local sample pattern "
        f"'{pattern}'. Choose one of: {', '.join(LOCAL_SAMPLE_PATTERNS)}."
    )


def sample_local_eval_outputs(
    *,
    count: int | None = None,
    duration_seconds: float | None = None,
    interval_seconds: float = 0.0,
    pattern: str = "source-order",
    family: str | None = None,
    start_source_order: int = 1,
    dataset: SwatchDataset | None = None,
    db_path: Path | None = None,
    time_fn: Callable[[], float] = time.monotonic,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> EvalSampleSummary:
    if count is None and duration_seconds is None:
        raise ValueError("Provide count or duration_seconds.")
    if count is not None and count < 1:
        raise ValueError("Count must be at least 1.")
    if duration_seconds is not None and duration_seconds <= 0:
        raise ValueError("Duration must be greater than 0.")
    if interval_seconds < 0:
        raise ValueError("Interval must be at least 0.")
    if start_source_order < 1:
        raise ValueError("Start source order must be at least 1.")
    if family is not None and family not in FAMILY_NAMES:
        raise ValueError(
            f"Unsupported family '{family}'. Choose one of: {', '.join(FAMILY_NAMES)}."
        )

    snapshot = _default_dataset() if dataset is None else dataset
    sample_swatches = _sample_swatches_for_pattern(snapshot, pattern)
    if family is not None:
        sample_swatches = tuple(
            swatch
            for swatch in sample_swatches
            if classify_family(swatch.hex).family == family
        )
    if not sample_swatches:
        raise ValueError("Sample pattern produced no swatches.")
    if start_source_order > len(sample_swatches):
        raise ValueError(
            f"Start source order exceeds the snapshot size ({len(sample_swatches)})."
        )

    resolved_db_path = EVAL_DB_PATH if db_path is None else db_path
    start = time_fn()
    deadline = None if duration_seconds is None else start + duration_seconds
    output_ids: list[int] = []
    index = 0
    start_index = start_source_order - 1

    while True:
        if count is not None and index >= count:
            break
        if deadline is not None and time_fn() >= deadline:
            break

        swatch = sample_swatches[(start_index + index) % len(sample_swatches)]
        state = build_one_up_state(swatch.hex, snapshot)
        output_id = record_one_up_state(resolved_db_path, state)
        output_ids.append(output_id)
        index += 1

        if interval_seconds <= 0:
            continue

        if deadline is None:
            if count is None or index < count:
                sleep_fn(interval_seconds)
            continue

        remaining = deadline - time_fn()
        if remaining <= 0:
            break
        sleep_fn(min(interval_seconds, remaining))

    elapsed_seconds = time_fn() - start
    return EvalSampleSummary(
        recorded=index,
        first_output_id=output_ids[0] if output_ids else None,
        last_output_id=output_ids[-1] if output_ids else None,
        elapsed_seconds=elapsed_seconds,
    )
