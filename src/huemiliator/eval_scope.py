from __future__ import annotations

from huemiliator.families import FAMILY_NAMES

EVAL_SCOPE_GROUPS: dict[str, tuple[str, ...]] = {
    "warm": ("brown", "red", "orange", "yellow"),
}

EVAL_SCOPE_NAMES: tuple[str, ...] = FAMILY_NAMES + tuple(EVAL_SCOPE_GROUPS)


def resolve_eval_scope_families(scope: str | None) -> tuple[str, ...] | None:
    if scope is None:
        return None
    if scope in FAMILY_NAMES:
        return (scope,)
    try:
        return EVAL_SCOPE_GROUPS[scope]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported eval scope '{scope}'. "
            f"Choose one of: {', '.join(EVAL_SCOPE_NAMES)}."
        ) from exc


def describe_eval_scope(scope: str) -> str:
    if scope in FAMILY_NAMES:
        return f"family={scope}"
    return f"scope={scope}"
