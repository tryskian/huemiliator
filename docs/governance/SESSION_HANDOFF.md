# Session Handoff

Last updated: 2026-05-16

## Start Here

1. Run:
   - `make start`
2. Read:
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
picker runtime, deterministic one-up logic, and a closed family-by-family eval
surface.

The core tracked shape is:

- bare `huemiliator` keeps the runtime local and CLI-first
- the active input surface is the native macOS colour picker
- the canonical user state is one hex code
- the runtime owns swatch matching, family assignment, same-family rank, and
  deterministic one-up selection
- the loss line stays downstream of the colour decision
- route and family correctness stay binary
- `evict` remains the upstream correction path once a bad lane is proven

Canonical live work stays on the repo `.local` surface. Superseded eval rows
stay quarantined locally instead of mixing back into the live DB.

## Active Kernel

- choose the next narrow proof-surface kernel from the live `pre-beta` colour
  evidence
- keep the startup and closeout contract small, truthful, and aligned with the
  actual operator flow

## Next Slice

1. Inspect:
   - `docs/research/README.md`
   - `docs/research/brown-context-dependence.md`
   - `docs/research/red-to-orange-edge-drift.md`
2. Inspect the live repo snapshot:
   - `make session-status`
   - current local proof-surface artefacts under `.local/`
3. Confirm the next narrow `red` correction against the live proof surface.
4. Cut one bounded correction kernel only after the proof surface still earns
   that same `red` edge escape.

## Research Snapshot

- phase: `pre-beta`
- active proof surface: closed third corrected `red` rerun at `id > 18423`
- current question: what is the next narrow `red` correction?
- next family lane: `red` first, `yellow` queued behind it
- tracked research notes:
  - `brown-context-dependence`
  - `red-to-orange-edge-drift`
- live DB rule: keep only the current proof surface in `eval_outputs`

## Guardrails

- keep the repo small and local
- keep the live runtime surface macOS-local
- keep one active kernel at a time
- keep one active sampler at a time
- keep family-by-family eval pressure as the default method
- keep the live DB limited to the current proof surface
- keep `.local/` and `docs/peanut/` local unless explicitly promoted
- keep tracked docs truthful to the current repo surface
- keep tracked research-note names descriptive, topic-first, and aligned with
  the current claim

## Close A Session

1. Run:
   - `make end-docs-check`
   - `make doctor-env`
   - `make path-leak-check`
   - `make path-leak-audit-local`
   - `make check`
   - `make decaffeinate`
   - `make session-status`
2. Finish on clean synced `main`:
   - `make end-git-check`

## Copy/Paste Refresh Prompt

`Run make start. Then read README.md, docs/governance/CHARTER.md, docs/governance/DECISIONS.md, docs/runtime/ARCHITECTURE.md, docs/runtime/RUNBOOK.md, and docs/governance/SESSION_HANDOFF.md. In 5 bullets: current state, risks, next kernel, repo or worktree context, and active branch. Confirm environment/workspace context: canonical repo path is /abs/path/to/huemiliator, host vs devcontainer mode, active git branch, and clean main or feature branch. Apply no-guessing controls: prefer repo-scoped edits and preserve user shell profile files and global VS Code settings unless explicitly approved in-chat. Run one active kernel at a time. Then execute the Next Slice from SESSION_HANDOFF with minimal behavior drift and full validation.`
