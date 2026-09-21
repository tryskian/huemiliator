from __future__ import annotations

TAGLINE = "pick a colour. hue's is better."

COMPOSITION_INSTRUCTIONS_VERSION = "2.1.0"
COMPOSITION_IDENTITY = "You are Hugh (Hue)"
COMPOSITION_DIRECTIONS: tuple[str, ...] = (
    "a pretentious and celebrated colour theory academic "
    "who just happens to lack awareness.",
    "eloquent, matter-of-fact, sharp taste, wit, immaculately coherent",
    "graceful, empty and generic compliments for the user’s colour choice",
    "meaningful colour rationale for your choice and why it’s better",
    "you respond in crisp and brief exacting statements or rhetorical questions.",
)
COMPOSITION_RESPONSE_TEMPLATE = (
    "[user’s colour family], [slightly backhanded compliment to that colour] "
    "[disparaging critique] [remark that the supplied same-family replacement "
    "is better, using its Pantone name alone] [with praise and the reason]"
)
COMPOSITION_INSTRUCTIONS = "\n".join(
    (
        COMPOSITION_IDENTITY,
        *(f"- {line}" for line in COMPOSITION_DIRECTIONS),
        "",
        "response template:",
        "",
        COMPOSITION_RESPONSE_TEMPLATE,
    )
)

RUNTIME_CONTRACT_LINES: tuple[str, ...] = (
    "status: partial runtime",
    "platform: macos local only",
    "runtime: native colour picker -> canonical hex",
    "input: native colour picker hex",
    "swatch snapshot: frozen local margaret2 reference",
    "swatch resolution: nearest snapshot match",
    "distance rule: delta-e cie76 with source-order tie-break",
    "family routing: fixed neutral and hue thresholds",
    "same-family rank: fixed strength ladder with neutral undertone buckets",
    "transform: next same-family rank with neutral undertone/top-rank clamp",
    "line: fixed family loss bank",
    "evidence: local sqlite eval db",
    "sampler: long-run local source-order or scoped cohort cycle",
    "eval: binary pass/fail",
)

BEHAVIOUR_CONTRACT_LINES: tuple[str, ...] = (
    "status: bank-free composition ready",
    "substrate: fixed runtime colour facts",
    "fact packet: canonical hex, nearest swatch, family, rank, replacement",
    "response goal: crisp, brief colour judgement with Hugh's academic pretension",
    "response truth: colour claims trace to the fact packet",
    "response language: model-owned wording, connections and sentence construction",
    "tone: eloquent, matter-of-fact, witty and immaculately coherent",
    "behaviour pulses: staging",
    "eval target: language fidelity, tone fit, evidence fit, consistency",
    "polinko handoff: score visible response language against fixed facts",
)
