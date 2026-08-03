from huemiliator.agent import (
    BEHAVIOUR_CONTRACT_LINES,
    RUNTIME_CONTRACT_LINES,
    TAGLINE,
    compose_visible_response,
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
    assert "response shape: replacement shade plus fixed family loss line" in contract
    assert "polinko handoff: score visible response language" in contract

    lower_contract = contract.lower()
    for directive in PROHIBITION_DIRECTIVES:
        assert directive not in lower_contract


def test_compose_visible_response_uses_replacement_then_loss_line() -> None:
    assert (
        compose_visible_response(
            "Ash rose", "the idea was right. the nerve was missing."
        )
        == "Ash rose.\nthe idea was right. the nerve was missing."
    )
