from __future__ import annotations

import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

from huemiliator.config import EVAL_DB_PATH, SWATCH_SNAPSHOT_PATH
from huemiliator.eval_db import record_one_up_state
from huemiliator.eval_scope import resolve_eval_scope_families
from huemiliator.families import classify_swatch
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


def _rotate_to_start_source_order(
    swatches: tuple[SwatchEntry, ...],
    start_source_order: int,
) -> tuple[SwatchEntry, ...]:
    highest_source_order = max(swatch.source_order for swatch in swatches)
    if start_source_order > highest_source_order:
        raise ValueError(
            "Start source order exceeds the highest snapshot source order "
            f"({highest_source_order})."
        )

    for index, swatch in enumerate(swatches):
        if swatch.source_order >= start_source_order:
            return swatches[index:] + swatches[:index]

    return swatches


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
    selected_families = resolve_eval_scope_families(family)

    snapshot = _default_dataset() if dataset is None else dataset
    sample_swatches = _sample_swatches_for_pattern(snapshot, pattern)
    if not sample_swatches:
        raise ValueError("Sample pattern produced no swatches.")
    sample_swatches = _rotate_to_start_source_order(
        sample_swatches,
        start_source_order,
    )
    if selected_families is not None:
        sample_swatches = tuple(
            swatch
            for swatch in sample_swatches
            if classify_swatch(swatch).family in selected_families
        )
    if not sample_swatches:
        raise ValueError("Sample pattern produced no swatches.")

    resolved_db_path = EVAL_DB_PATH if db_path is None else db_path
    start = time_fn()
    deadline = None if duration_seconds is None else start + duration_seconds
    output_ids: list[int] = []
    index = 0

    while True:
        if count is not None and index >= count:
            break
        if deadline is not None and time_fn() >= deadline:
            break

        swatch = sample_swatches[index % len(sample_swatches)]
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


def sample_input_hex_eval_outputs(
    *,
    input_hexes: Sequence[str],
    interval_seconds: float = 0.0,
    dataset: SwatchDataset | None = None,
    db_path: Path | None = None,
    time_fn: Callable[[], float] = time.monotonic,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> EvalSampleSummary:
    if not input_hexes:
        raise ValueError("Provide at least one input hex.")
    if interval_seconds < 0:
        raise ValueError("Interval must be at least 0.")

    snapshot = _default_dataset() if dataset is None else dataset
    resolved_db_path = EVAL_DB_PATH if db_path is None else db_path
    start = time_fn()
    output_ids: list[int] = []

    for index, input_hex in enumerate(input_hexes):
        state = build_one_up_state(input_hex, snapshot)
        output_id = record_one_up_state(resolved_db_path, state)
        output_ids.append(output_id)

        if interval_seconds > 0 and index < len(input_hexes) - 1:
            sleep_fn(interval_seconds)

    elapsed_seconds = time_fn() - start
    return EvalSampleSummary(
        recorded=len(output_ids),
        first_output_id=output_ids[0],
        last_output_id=output_ids[-1],
        elapsed_seconds=elapsed_seconds,
    )
