from __future__ import annotations

TAGLINE = "pick a colour. hue's is better."

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
