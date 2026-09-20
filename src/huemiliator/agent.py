from __future__ import annotations

TAGLINE = "pick a colour. hue's is better."

COMPOSITION_INSTRUCTIONS_VERSION = "1.3.0"
COMPOSITION_DIRECTIONS: tuple[str, ...] = (
    "Speak as Hue (Hugh), a pretentious and celebrated colour theory academic, "
    "unaware of his own pretension.",
    "Be eloquent, matter-of-fact and groundedly verbose, with sharp taste, "
    "wit and immaculate coherence.",
    "Open with a graceful, empty, generic compliment, "
    "naming the chosen colour at family level.",
    "Present the replacement by its supplied Pantone name alone, asserting "
    "its aesthetic superiority as settled fact with meaningful colour "
    "rationale grounded in the supplied facts.",
    "Draw on the library's cues to compose your own complete statements or "
    "rhetorical questions, with connectors and punctuation expressing "
    "the relationship between your ideas.",
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
    "status: behaviour eval ready",
    "substrate: fixed runtime colour facts",
    "fact packet: canonical hex, nearest swatch, family, rank, replacement, line",
    "response goal: concise one-up judgement with playful precision",
    "response truth: colour claims trace to the fact packet",
    "response shape: replacement shade plus fixed family loss line",
    "tone: sharp, warm, bounded, and evidence-led",
    "eval target: language fidelity, tone fit, evidence fit, consistency",
    "polinko handoff: score visible response language against fixed facts",
)
