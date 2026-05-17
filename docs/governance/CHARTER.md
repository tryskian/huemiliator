# Huemiliator Charter

## Mission

Build a small, local, CLI-first mini chatbot for inspecting deterministic
colour one-up behaviour through picker-first input, fixed family rules, and
fail-first evaluation.

## Durable Rules

- Local picker runtime is canonical.
- The live runtime surface stays macOS-local.
- Prompt surface stays fixed to:
  - one native colour picker
  - one canonical hex code
- The frozen `margaret2` snapshot stays the primary colour reference.
- Swatch matching stays deterministic through:
  - fixed `delta-e cie76`
  - source-order tie-breaks
- Runtime owns:
  - swatch matching
  - family assignment
  - same-family rank
  - one-up selection
- Replacement stays same-family, next-rank, and non-wrapping.
- The loss line stays fixed-bank and downstream of the colour decision.
- Eval semantics stay binary:
  - `PASS`
  - `FAIL`
- Fail-pressure pulse is the staged pre-`Beta 1.0` candidate for the next
  non-OCR eval boundary:
  - the pulse would carry the verdict
  - the rows would stay evidence inside the pulse
- Active eval pressure stays on one family lane at a time.
- `warm` stays an audit cohort rather than a runtime family.
- The live DB keeps only the current proof surface.
- Tracked docs, code, tests, and local eval evidence are canonical repo truth.
- `docs/peanut/` stays the local and private lane.
- Small, testable changes are the default delivery shape.
- Evidence inspection comes before interpretation.
- Evidence chains stay preserved through archive-first handling.

## Working Model

- Human lead owns:
  - hypotheses
  - scope boundaries
  - acceptance criteria
  - meaning-level trade-offs
  - go or no-go decisions
- Engineer owns:
  - implementation
  - validation
  - Git and PR flow
  - proactive hygiene
  - execution recommendations
- Default execution model:
  - one feature branch per change set
  - protected-main PR flow
  - clean synced `main` as the tracked stop state
- Parallel implementation uses dedicated worktrees.

## Documentation Governance

- `docs/governance/DECISIONS.md`
  - durable repo decisions
- `docs/governance/SESSION_HANDOFF.md`
  - active slice and carryover
- `docs/runtime/RUNBOOK.md`
  - operator procedure
- `docs/runtime/ARCHITECTURE.md`
  - stable system shape
- `docs/runtime/START_END_REFERENCE.md`
  - compact command card
- `docs/research/`
  - tracked research notes and current proof-surface reads
- `docs/diagrams/`
  - tracked runtime and eval diagrams
- `docs/peanut/`
  - local and private working lane

## Current Scope

- local picker-first runtime and operator surface
- deterministic swatch matching against the frozen local snapshot
- runtime-owned family assignment and same-family rank
- deterministic same-family replacement and short loss-line output
- the current row-level family proof surface plus a staged fail-pressure pulse
  boundary for the next non-OCR method change
- tracked research notes and diagrams aligned with the active proof surface
- smaller, single-purpose docs aligned with live repo behaviour

## Security / Ops Baseline

- Local `.venv` is the canonical development environment.
- Local terminal execution is the trusted development boundary.
- `.local/evals.sqlite` is the live eval evidence store.
- `make doctor-env` is the environment confirmation entrypoint.
- Default branch changes land through protected-main PR flow.
