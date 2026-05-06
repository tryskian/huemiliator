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

### D-008: The repo is licensed under Apache 2.0

- date: `2026-05-05`
- status: active

Huemiliator uses an explicit Apache 2.0 license surface.

The tracked public repo should keep:

- the root `LICENSE` file
- the README license section
- SPDX-style package metadata aligned with the tracked license file

### D-009: The README should not advertise a runtime that does not exist

- date: `2026-05-05`
- status: active
- decision type: human-led

The README should not carry a `Run It` section until Huemiliator has a real
runtime surface to run.

Before that point, the top-level docs should describe the current scaffold
truthfully instead of implying product readiness.

### D-010: Huemiliator uses the current Scorey workflow automation surface

- date: `2026-05-05`
- status: active

Huemiliator should inherit the current Scorey GitHub automation shape rather
than inventing a repo-specific CI lane during scaffold stage.

The tracked automation surface is:

- CI on push and pull request
- weekly Dependabot for pip and GitHub Actions
- scheduled stale cleanup for dependency PRs
