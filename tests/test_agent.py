from huemiliator.agent import RUNTIME_CONTRACT_LINES, TAGLINE

PROHIBITION_DIRECTIVES = (
    "never",
    "do not",
    "don't",
    "not ",
    "without",
    "avoid",
    "instead of",
    "no ",
)


def test_runtime_contract_uses_positive_target_shape() -> None:
    contract = "\n".join(RUNTIME_CONTRACT_LINES)

    assert TAGLINE == "pick a colour. hue's is better."
    assert "runtime: native colour picker -> canonical hex" in contract
    assert "swatch resolution: nearest snapshot match" in contract
    assert "transform: next same-family rank" in contract
    assert "line: fixed family loss bank" in contract

    lower_contract = contract.lower()
    for directive in PROHIBITION_DIRECTIVES:
        assert directive not in lower_contract
