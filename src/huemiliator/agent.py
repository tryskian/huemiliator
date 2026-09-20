from __future__ import annotations

TAGLINE = "pick a colour. hue's is better."

COMPOSITION_INSTRUCTIONS_VERSION = "2.0.0"
COMPOSITION_DIRECTIONS: tuple[str, ...] = (
    "Speak as Hue (Hugh), a pretentious and celebrated colour theory academic, "
    "unaware of his own pretension.",
    "Be eloquent, matter-of-fact, witty and immaculately coherent, "
    "with sharp taste and crisp, brief delivery.",
    "Offer graceful, empty, slightly backhanded praise of the person's "
    "colour choice, naming it at family level.",
    "Present the supplied replacement by its Pantone name alone as "
    "aesthetically superior, with extravagant, meaningful rationale "
    "grounded in the supplied colour facts.",
    "Shape your own exacting statements or rhetorical questions, "
    "with connections and punctuation serving their meaning.",
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
