from __future__ import annotations

import json
from pathlib import Path

import pytest

from huemiliator.config import load_settings
from huemiliator.swatches import (
    SOURCE_URL,
    SwatchDatasetError,
    build_snapshot_payload,
    load_swatch_snapshot,
    parse_source_html,
)


def test_parse_source_html_extracts_ordered_swatches() -> None:
    html = """
    <table>
      <tr><td class="egret" data-clipboard-text="#F3ECE0"> </td><td> Egret </td></tr>
      <tr><td class="snow-white" data-clipboard-text="#f2f0eb"> </td>
      <td> Snow white </td></tr>
    </table>
    """

    swatches = parse_source_html(html)

    assert len(swatches) == 2
    assert swatches[0].source_order == 1
    assert swatches[0].slug == "egret"
    assert swatches[0].name == "Egret"
    assert swatches[0].hex == "#f3ece0"
    assert swatches[1].source_order == 2
    assert swatches[1].name == "Snow white"


def test_parse_source_html_rejects_missing_rows() -> None:
    with pytest.raises(SwatchDatasetError, match="No swatch rows"):
        parse_source_html("<html></html>")


def test_load_swatch_snapshot_reads_frozen_payload(tmp_path: Path) -> None:
    swatches = parse_source_html(
        '<tr><td class="egret" data-clipboard-text="#f3ece0"> </td>'
        "<td> Egret </td></tr>"
    )
    payload = build_snapshot_payload(swatches, snapshot_date="2026-05-06")
    dataset_path = tmp_path / "swatches.json"
    dataset_path.write_text(json.dumps(payload), encoding="utf-8")

    dataset = load_swatch_snapshot(dataset_path)

    assert dataset.source.url == SOURCE_URL
    assert dataset.source.snapshot_date == "2026-05-06"
    assert len(dataset.swatches) == 1
    assert dataset.swatches[0].name == "Egret"


def test_repo_swatch_snapshot_loads_real_archived_reference() -> None:
    settings = load_settings()
    dataset = load_swatch_snapshot(settings.swatch_snapshot_path)

    assert dataset.source.url == SOURCE_URL
    assert dataset.source.upstream_status == "archived read-only"
    assert len(dataset.swatches) == 2310
    assert dataset.swatches[0].name == "Egret"
    assert dataset.swatches[-1].name == "Rain forest"
