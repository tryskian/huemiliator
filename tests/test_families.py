from __future__ import annotations

from huemiliator.colour_math import build_colour_metrics
from huemiliator.families import (
    BROWN_EARTHY_HUE_MAX,
    build_family_member_index,
    build_family_rank_index,
    classify_family,
    select_one_up,
)
from huemiliator.swatches import SwatchDataset, SwatchEntry, SwatchSource


def _dataset(*swatches: SwatchEntry) -> SwatchDataset:
    return SwatchDataset(
        source=SwatchSource(
            name="test",
            url="https://example.com",
            snapshot_date="2026-05-07",
            upstream_status="test",
            source_format="test",
        ),
        swatches=swatches,
    )


def test_classify_family_routes_neutral_brown_and_blue() -> None:
    assert classify_family("#f3ece0").family == "neutral"
    assert classify_family("#8b5e3c").family == "brown"
    assert classify_family("#2f5da8").family == "blue"


def test_classify_family_promotes_dark_earthy_warms_to_brown() -> None:
    assert classify_family("#5b5149").family == "brown"
    assert classify_family("#6c5043").family == "brown"
    assert classify_family("#ab856f").family == "brown"


def test_classify_family_keeps_pale_warm_neutrals_out_of_brown() -> None:
    assert classify_family("#c4b6a6").family == "neutral"


def test_classify_family_demotes_bright_gold_shoulder_out_of_brown() -> None:
    assert classify_family("#c19552").family == "orange"
    assert classify_family("#d39c43").family == "orange"
    assert classify_family("#b08e51").family == "orange"
    assert classify_family("#be8a4a").family == "orange"
    assert classify_family("#cda323").family == "yellow"


def test_classify_family_demotes_muted_olive_shoulder_out_of_brown() -> None:
    assert classify_family("#5b4f3b").family == "neutral"
    assert classify_family("#80765f").family == "neutral"
    assert classify_family("#746c57").family == "neutral"
    assert classify_family("#545144").family == "neutral"
    assert classify_family("#a39264").family == "neutral"


def test_classify_family_demotes_loud_orange_shoulder_out_of_brown() -> None:
    assert classify_family("#ff7913").family == "orange"
    assert classify_family("#f96714").family == "orange"
    assert classify_family("#f47327").family == "orange"
    assert classify_family("#ff8812").family == "orange"


def test_build_family_rank_index_orders_chromatic_strength_ascending() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="muted-red", name="Muted red", hex="#b79494"),
        SwatchEntry(source_order=2, slug="loud-red", name="Loud red", hex="#d22345"),
    )

    ranked = build_family_rank_index(dataset)

    assert ranked[1].family == "red"
    assert ranked[1].family_rank == 1
    assert ranked[2].family == "red"
    assert ranked[2].family_rank == 2
    assert ranked[2].family_size == 2


def test_build_family_rank_index_orders_neutral_strength_ascending() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="mid", name="Mid", hex="#808080"),
        SwatchEntry(source_order=2, slug="light", name="Light", hex="#f3f3f3"),
    )

    ranked = build_family_rank_index(dataset)

    assert ranked[1].family == "neutral"
    assert ranked[1].family_rank == 1
    assert ranked[2].family == "neutral"
    assert ranked[2].family_rank == 2


def test_build_family_rank_index_routes_bright_gold_shoulder_out_of_brown() -> None:
    dataset = _dataset(
        SwatchEntry(
            source_order=1, slug="spectra-yellow", name="Spectra yellow", hex="#f7b718"
        ),
        SwatchEntry(source_order=2, slug="adobe", name="Adobe", hex="#a3623b"),
        SwatchEntry(
            source_order=3, slug="raw-sienna", name="Raw sienna", hex="#b9714f"
        ),
    )

    ranked = build_family_rank_index(dataset)

    assert ranked[1].family == "orange"
    assert ranked[2].family == "brown"
    assert ranked[2].family_rank == 2
    assert ranked[3].family == "brown"
    assert ranked[3].family_rank == 1


def test_select_one_up_keeps_earthy_brown_over_yellow_shoulder() -> None:
    dataset = _dataset(
        SwatchEntry(
            source_order=1, slug="spectra-yellow", name="Spectra yellow", hex="#f7b718"
        ),
        SwatchEntry(
            source_order=2, slug="leather-brown", name="Leather brown", hex="#97572b"
        ),
        SwatchEntry(
            source_order=3, slug="raw-sienna", name="Raw sienna", hex="#b9714f"
        ),
    )

    ranked = build_family_rank_index(dataset)
    members = build_family_member_index(ranked)
    selection = select_one_up(ranked[2], members)

    assert selection.current.swatch.name == "Leather brown"
    assert selection.replacement.swatch.name != "Spectra yellow"
    assert (
        build_colour_metrics(selection.replacement.swatch.hex).hue_degrees
        < BROWN_EARTHY_HUE_MAX
    )


def test_select_one_up_moves_to_next_rank_in_same_family() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="muted-red", name="Muted red", hex="#b79494"),
        SwatchEntry(source_order=2, slug="loud-red", name="Loud red", hex="#d22345"),
    )

    ranked = build_family_rank_index(dataset)
    members = build_family_member_index(ranked)
    selection = select_one_up(ranked[1], members)

    assert selection.current.swatch.name == "Muted red"
    assert selection.replacement.swatch.name == "Loud red"
    assert selection.replacement.family == "red"


def test_select_one_up_clamps_at_top_rank() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="mid", name="Mid", hex="#808080"),
        SwatchEntry(source_order=2, slug="light", name="Light", hex="#f3f3f3"),
    )

    ranked = build_family_rank_index(dataset)
    members = build_family_member_index(ranked)
    selection = select_one_up(ranked[2], members)

    assert selection.current.swatch.name == "Light"
    assert selection.replacement.swatch.name == "Light"
