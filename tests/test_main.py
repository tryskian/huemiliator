from huemiliator.main import render_status


def test_render_status_includes_contract_lines() -> None:
    text = render_status()
    assert "pick a colour. hue's is better." in text
    assert "resolution: nearest swatch match from locked reference" in text
    assert "transform: same-family deterministic one-up" in text
