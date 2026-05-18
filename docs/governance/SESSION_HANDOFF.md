# Session Handoff

Last updated: 2026-05-18

## Start Here

1. Run:
   - `make start`
2. Ground on the startup-docs read across:
   - `README.md`
   - `docs/governance/CHARTER.md`
   - `docs/governance/DECISIONS.md`
   - `docs/runtime/ARCHITECTURE.md`
   - `docs/runtime/RUNBOOK.md`
   - `docs/governance/SESSION_HANDOFF.md`
3. Confirm execution context:
   - repo root or dedicated worktree
   - active branch from `git branch --show-current`
   - host or devcontainer mode
   - clean `main` or feature branch
4. Return the startup breakdown:
   - current state
   - risks
   - next kernel
   - repo or worktree context
   - active branch
5. Start one active kernel.

## Current Snapshot

Huemiliator is a small, local, agent-backed colour mini chatbot with a real
picker runtime, deterministic one-up logic, and a staged pre-`Beta 1.0`
fail-pressure pulse lane for the next non-OCR logic method boundary.

The core tracked shape is:

- bare `huemiliator` keeps the runtime local and CLI-first
- the active input surface is the native macOS colour picker
- the canonical user state is one hex code
- the runtime owns swatch matching, family assignment, same-family rank, and
  deterministic one-up selection
- the loss line stays downstream of the colour decision
- route and family correctness stay binary
- the closed third corrected `red` rerun remains the active row-level
  comparison baseline
- fail-pressure pulse is staged for the next method boundary, but `Beta 1.0`
  does not begin until the first real pulse run starts

Canonical live work stays on the repo `.local` surface. Superseded eval rows
stay quarantined locally instead of mixing back into the live DB.

## Active Kernel

- launch the first bounded `red` `Beta 1.0` pulse from the repaired sampler
  surface without widening the lane
- keep the startup and closeout contract small, truthful, and aligned with the
  actual operator flow

## Next Slice

1. Inspect:
   - `docs/research/README.md`
   - `docs/research/pre_beta_1_fail_pressure_pulse_2026-05-16.md`
   - `docs/research/brown_context_dependence_2026-05-08.md`
   - `docs/research/red_orange_edge_drift_2026-05-15.md`
   - `docs/research/red_orange_edge_drift_audit_2026-05-16.md`
2. Inspect the live repo snapshot:
   - `make session-status`
   - current local proof-surface artefacts under `.local/`
3. Launch the first bounded `red` Beta 1.0 pulse against the warm-clay /
   peach edge claim from the repaired sampler surface.
4. Judge the bounded pulse before deciding whether the next `red` move is
   still a family cut or a later rank kernel.

## Research Snapshot

- staged research lane: `pre-Beta 1.0`
- active proof surface: closed third corrected `red` rerun at `id > 18423`
- current staging question: does the first bounded `red` pulse keep the same
  warm-clay / peach seam legible now that sampler truth is repaired
- staged pulse note: `pre_beta_1_fail_pressure_pulse_2026-05-16`
- next family lane: `red` first, `yellow` queued behind it
- tracked research notes:
  - `pre_beta_1_fail_pressure_pulse_2026-05-16`
  - `brown_context_dependence_2026-05-08`
  - `red_orange_edge_drift_2026-05-15`
  - `red_orange_edge_drift_audit_2026-05-16`
- live DB rule: keep only the current proof surface in `eval_outputs`

## Guardrails

- keep the repo small and local
- keep the live runtime surface macOS-local
- keep one active kernel at a time
- keep one active sampler at a time
- keep active eval pressure on one family lane at a time
- do not promote `Beta 1.0` until the first real pulse run starts
- keep the live DB limited to the current proof surface
- keep `.local/` and `docs/peanut/` local unless explicitly promoted
- capture notes, findings, and truth-surface changes as they emerge
- keep tracked docs truthful to the current repo surface
- keep tracked research-note names descriptive, topic-first, and aligned with
  the current claim

## Pinned Later

- when this repo is not in an active work kernel, standardize the
  procedure-first execution contract across the repo family
- carry the same truth order across repos:
  - docs
  - live code
  - live DB
  - then change
- keep command and operator surfaces truthful; do not invent behavior the repo
  does not actually implement

## Close A Session

1. Run:
   - `make end`
2. Treat `make end-preflight` as preflight only:
   - use it only when an explicit branch-local preflight was requested
   - do not treat it as a day-close substitute

## Copy/Paste Refresh Prompt

`Run make start. Use the startup-docs read across README.md, docs/governance/CHARTER.md, docs/governance/DECISIONS.md, docs/runtime/ARCHITECTURE.md, docs/runtime/RUNBOOK.md, docs/governance/SESSION_HANDOFF.md, and local docs/peanut/governance/SESSION_HANDOFF.md if present. In 5 bullets: current state, risks, next kernel, repo or worktree context, and active branch. Confirm environment/workspace context: canonical repo path is /abs/path/to/huemiliator, host vs devcontainer mode, active git branch, and clean main or feature branch. Apply no-guessing controls: prefer repo-scoped edits and preserve user shell profile files and global VS Code settings unless explicitly approved in-chat. Run one active kernel at a time. Then execute the Next Slice from SESSION_HANDOFF with minimal behavior drift and full validation.`
