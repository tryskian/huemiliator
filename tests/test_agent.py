from huemiliator.agent import (
    BEHAVIOUR_CONTRACT_LINES,
    COMPOSITION_DIRECTIONS,
    RUNTIME_CONTRACT_LINES,
    TAGLINE,
)

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


def test_behaviour_contract_separates_language_eval_from_colour_facts() -> None:
    contract = "\n".join(BEHAVIOUR_CONTRACT_LINES)

    assert "substrate: fixed runtime colour facts" in contract
    assert "response truth: colour claims trace to the fact packet" in contract
    assert "model-owned wording, connections and sentence construction" in contract
    assert "behaviour pulses: staging" in contract
    assert "fixed family loss line" not in contract
    assert "polinko handoff: score visible response language" in contract

    lower_contract = contract.lower()
    for directive in PROHIBITION_DIRECTIVES:
        assert directive not in lower_contract


def test_composition_directions_keep_character_and_colour_responsibilities() -> None:
    directions = "\n".join(COMPOSITION_DIRECTIONS)
    assert len(COMPOSITION_DIRECTIONS) == 5
    assert "crisp, brief delivery" in directions
    assert "supplied replacement" in directions
    assert "Shape your own" in directions
    assert "library" not in directions
    assert "response template" not in directions
    for directive in PROHIBITION_DIRECTIVES:
        assert directive not in directions.lower()
