# Decisions

This file stores durable runtime, docs, and eval decisions.

## Active Decisions

### D-001: Scorey is the active baseline

- date: `2026-05-05`
- status: active

Huemiliator starts from the current Scorey house architecture rather than
reconstructing from Probaboracle directly.

### D-002: Pantone is the canonical colour inventory

- date: `2026-05-05`
- status: active

The Pantone repo surface is the canonical matching library for colour names and
hex codes.

Huemiliator supplies the missing structure on top:

- family assignment
- within-family rank
- deterministic one-up rule

### D-003: V1 input is picker-first

- date: `2026-05-05`
- status: active

The first runtime lane should use a native colour picker as the primary input.

The picker hex is the canonical user input state. Freeform text does not belong
in v1.

### D-004: Runtime owns colour resolution

- date: `2026-05-05`
- status: active

Matching, family assignment, and one-up selection should be runtime-owned and
PASS/FAIL-testable.

If generation is used later, it should not own the final colour decision.

### D-005: Repo initialisation is docs-first

- date: `2026-05-05`
- status: active

The current repo state is an honest scaffold:

- git repo initialised
- docs spine created
- package skeleton created
- no implemented runtime yet

### D-006: The repo is public during contract lock

- date: `2026-05-05`
- status: active

Huemiliator is public before runtime implementation.

The tracked docs should therefore stay honest about the current scaffold state
and avoid machine-specific local details.

### D-007: `main` is protected and work lands through `codex/bigbrain/...`

- date: `2026-05-05`
- status: active

The default branch uses the toy-family ruleset shape:

- PR required
- squash is the only allowed merge method
- no force pushes
- no branch deletion

Tracked work should happen on `codex/bigbrain/...` branches and land back in
`main` through squash PRs.
