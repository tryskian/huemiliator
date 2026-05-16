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


def test_classify_family_demotes_bright_gold_edge_out_of_brown() -> None:
    assert classify_family("#c19552").family == "orange"
    assert classify_family("#d39c43").family == "orange"
    assert classify_family("#b08e51").family == "orange"
    assert classify_family("#cda323").family == "yellow"


def test_classify_family_demotes_warm_orange_yellow_edge_out_of_brown() -> None:
    assert classify_family("#c86b3c").family == "orange"
    assert classify_family("#d08344").family == "orange"
    assert classify_family("#ff8812").family == "orange"
    assert classify_family("#ee9626").family == "orange"


def test_classify_family_demotes_olive_seam_out_of_brown() -> None:
    assert classify_family("#80765f").family == "yellow"
    assert classify_family("#746c57").family == "neutral"
    assert classify_family("#817a60").family == "yellow"
    assert classify_family("#927b3c").family == "orange"
    assert classify_family("#a39264").family == "yellow"


def test_classify_family_keeps_earthy_brown_core_inside_brown() -> None:
    assert classify_family("#9a7352").family == "brown"
    assert classify_family("#6e4f3a").family == "brown"
    assert classify_family("#704822").family == "brown"
    assert classify_family("#97572b").family == "brown"


def test_classify_family_demotes_pale_low_chroma_orange_edge_to_neutral() -> None:
    assert classify_family("#f3e6c9").family == "neutral"
    assert classify_family("#f0debd").family == "neutral"
    assert classify_family("#f1ceb3").family == "neutral"
    assert classify_family("#d7b8ab").family == "neutral"
    assert classify_family("#ecddbe").family == "neutral"


def test_classify_family_demotes_taupe_orange_edge_to_neutral() -> None:
    assert classify_family("#aa907d").family == "neutral"
    assert classify_family("#ae8774").family == "neutral"
    assert classify_family("#b69574").family == "neutral"
    assert classify_family("#ba8671").family == "neutral"


def test_classify_family_demotes_soft_beige_orange_edge_to_neutral() -> None:
    assert classify_family("#ccb390").family == "neutral"
    assert classify_family("#d5ba98").family == "neutral"
    assert classify_family("#d1be9b").family == "neutral"
    assert classify_family("#d2c29d").family == "neutral"


def test_classify_family_demotes_muted_olive_orange_edge_to_yellow() -> None:
    assert classify_family("#80765f").family == "yellow"
    assert classify_family("#c4ab86").family == "yellow"
    assert classify_family("#be9e6f").family == "yellow"
    assert classify_family("#998456").family == "yellow"
    assert classify_family("#a39264").family == "yellow"


def test_classify_family_keeps_stronger_orange_core_inside_orange() -> None:
    assert classify_family("#fed1bd").family == "orange"
    assert classify_family("#f8d5b8").family == "orange"
    assert classify_family("#e6bd8f").family == "orange"
    assert classify_family("#b19664").family == "orange"
    assert classify_family("#d2b04c").family == "orange"


def test_classify_family_demotes_dusty_red_pink_edge_to_pink() -> None:
    assert classify_family("#f5d1c8").family == "pink"
    assert classify_family("#ddb6ab").family == "pink"
    assert classify_family("#dbb0a2").family == "pink"
    assert classify_family("#dcb1af").family == "pink"
    assert classify_family("#f4cec5").family == "pink"


def test_classify_family_demotes_pink_peach_red_edge_to_pink() -> None:
    assert classify_family("#efa6aa").family == "pink"
    assert classify_family("#eea0a6").family == "pink"
    assert classify_family("#f2b2ae").family == "pink"
    assert classify_family("#f4a6a3").family == "pink"
    assert classify_family("#f8a39d").family == "pink"


def test_classify_family_demotes_midlight_peach_red_edge_to_pink() -> None:
    assert classify_family("#ea6676").family == "pink"
    assert classify_family("#ee5c6c").family == "pink"
    assert classify_family("#dc7178").family == "pink"
    assert classify_family("#e4445e").family == "pink"
    assert classify_family("#dc3855").family == "pink"


def test_classify_family_demotes_moderate_red_peach_edge_to_pink() -> None:
    assert classify_family("#e8a798").family == "pink"
    assert classify_family("#d29380").family == "pink"
    assert classify_family("#e29a86").family == "pink"
    assert classify_family("#bd7b74").family == "pink"
    assert classify_family("#dd9289").family == "pink"


def test_classify_family_demotes_low_chroma_rose_edge_to_pink() -> None:
    assert classify_family("#d19c97").family == "pink"
    assert classify_family("#a4777e").family == "pink"
    assert classify_family("#ecb2b3").family == "pink"
    assert classify_family("#fdc3c6").family == "pink"


def test_classify_family_demotes_dark_red_brown_wine_seam_to_brown() -> None:
    assert classify_family("#503130").family == "brown"
    assert classify_family("#593c39").family == "brown"
    assert classify_family("#5d3c43").family == "brown"
    assert classify_family("#56352d").family == "brown"
    assert classify_family("#58363d").family == "brown"


def test_classify_family_demotes_low_chroma_red_brown_edge_to_brown() -> None:
    assert classify_family("#844b4d").family == "brown"
    assert classify_family("#884344").family == "brown"
    assert classify_family("#7e3940").family == "brown"
    assert classify_family("#77333b").family == "brown"
    assert classify_family("#702f3b").family == "brown"
    assert classify_family("#5c2c35").family == "brown"


def test_classify_family_demotes_expanded_red_brown_edge_to_brown() -> None:
    assert classify_family("#8f5f50").family == "brown"
    assert classify_family("#98594b").family == "brown"
    assert classify_family("#9a6051").family == "brown"
    assert classify_family("#714a41").family == "brown"
    assert classify_family("#6e403c").family == "brown"
    assert classify_family("#6b4139").family == "brown"
    assert classify_family("#683b39").family == "brown"
    assert classify_family("#6a3331").family == "brown"


def test_classify_family_keeps_stronger_red_core_inside_red() -> None:
    assert classify_family("#a73340").family == "red"
    assert classify_family("#884332").family == "red"
    assert classify_family("#b93a32").family == "red"
    assert classify_family("#7b3539").family == "red"
    assert classify_family("#973443").family == "red"


def test_classify_family_keeps_soft_red_boundary_lane_inside_red() -> None:
    assert classify_family("#70393f").family == "red"
    assert classify_family("#c08a80").family == "red"
    assert classify_family("#ffc4bc").family == "red"
    assert classify_family("#d9a6a1").family == "red"
    assert classify_family("#ed9ca8").family == "red"


def test_build_family_rank_index_orders_chromatic_strength_ascending() -> None:
    dataset = _dataset(
        SwatchEntry(source_order=1, slug="muted-red", name="Muted red", hex="#d9a6a1"),
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


def test_build_family_rank_index_routes_bright_gold_edge_out_of_brown() -> None:
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


def test_select_one_up_keeps_earthy_brown_over_yellow_edge() -> None:
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
        SwatchEntry(source_order=1, slug="muted-red", name="Muted red", hex="#d9a6a1"),
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
