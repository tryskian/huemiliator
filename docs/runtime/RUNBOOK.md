# Runbook

## When to Read This

Use this doc for operator procedure.

- `README.md`
  - public framing and quick entrypoint
- `docs/governance/CHARTER.md`
  - durable rules and role split
- `docs/runtime/ARCHITECTURE.md`
  - stable system shape
- `docs/governance/SESSION_HANDOFF.md`
  - active slice and carryover
- `docs/governance/DECISIONS.md`
  - durable rationale for repo choices
- `docs/runtime/START_END_REFERENCE.md`
  - compact command card

## Branch, Worktree, and Scope Policy

1. Canonical repo root is:
   - `/abs/path/to/huemiliator`
2. Default workflow is one feature branch per change set:
   - `git switch -c codex/bigbrain/<task-name>`
3. Start tracked edits from a feature branch.
4. Use a dedicated worktree for parallel implementation tracks.
5. Keep one logical task per branch.
6. Keep one active kernel at a time.
7. Secondary worktrees for live eval work should use:
   - local `.venv`
   - canonical repo `.local`

## Command Surface Rule

1. Keep one atomic command per operator action.
2. Keep operator thinking in procedure.
3. Keep wrapper targets mechanical.
4. Use `make session-status` as the live repo and runtime snapshot.
5. Use `make end` as the strict clean-main closeout routine.
6. `make start` opens the session by reading the tracked startup docs and
   printing the startup gate; startup completes after the rehydrate response
   names one active kernel.

## Morning Startup Ritual

1. Run:
   - `make start`
2. Treat `make start` as the mechanical bootstrap plus tracked startup-doc read:
   - workspace context
   - `make doctor-env`
   - `make caffeinate`
   - `make caffeinate-status`
   - `make startup-docs-read`
   - `make session-status`
   - startup gate prompt
3. Use the startup-doc read across:
   - `README.md`
   - `docs/governance/CHARTER.md`
   - `docs/governance/DECISIONS.md`
   - `docs/runtime/ARCHITECTURE.md`
   - `docs/runtime/RUNBOOK.md`
   - `docs/governance/SESSION_HANDOFF.md`
   - local `docs/peanut/governance/SESSION_HANDOFF.md` if present
4. Confirm execution context:
   - canonical repo root or dedicated worktree
   - active branch from `git branch --show-current`
   - host or devcontainer mode
   - clean `main` or feature branch
5. Return the startup breakdown before implementation:
   - current state
   - risks
   - next kernel
   - repo or worktree context
   - active branch
6. Start one active kernel from the tracked handoff.
7. Install or refresh the environment when needed:
   - `make install`

## Environment Doctor

1. Run:
   - `make doctor-env`
2. It checks:
   - Python path
   - venv
   - package imports
   - repo runtime files
   - live credential visibility when credentials are in play
3. Resolve actionable issues before runtime or eval work.

## Inspect-First Rule

1. Inspect named files, logs, reports, screenshots, and notes before
   interpretation.
2. Use source evidence as the basis for interpretation.
3. State inspection status plainly.

## Command Ownership

1. Human lead owns:
   - objective
   - scope
   - acceptance criteria
   - meaning-level trade-offs
   - go or no-go decisions
2. Engineer owns:
   - implementation
   - validation
   - command execution
   - Git and PR flow
   - proactive hygiene
3. Default mode is execution-first:
   - do the work directly when asked

## Protected Main PR Flow

1. Work on a feature branch.
2. Commit locally.
3. Push the branch.
4. Open a PR to `main`.
5. Wait for required checks.
6. Merge through the protected-main flow.
7. Sync local `main`:
   - `git switch main`
   - `git pull --ff-only`
8. Final local repo state is clean and synced with `origin/main`.

## End Of Day

1. When the goal is to close out the day, run:
   - `make end`
2. If `make end` fails on a feature branch, finish the merge path:
   - package the branch when the kernel is ready
   - merge through the protected-main flow
   - switch back to `main`
   - pull fast-forward only
   - rerun `make end`
3. `make end` only passes when:
   - current-truth docs are fresh
   - tracked and local path leak checks pass
   - docs lint, code checks, package build, editable package import, and
     dependency security pass
   - live eval `pending` is `0`
   - the repo ends on clean synced `main`
4. Use `make end-preflight` only when an explicit branch-local preflight was
   requested.
5. End state is:
   - merged
   - clean local `main`
   - synced with `origin/main`

## Local-Only Docs Policy

1. `docs/peanut/` is the local and private lane.
2. Use it for:
   - interface sketches
   - rough notes
   - private scratch material
3. Tracked docs remain canonical project truth.

## Atomic Commands

- `make install`
  - install or refresh the local environment
- `make doctor-env`
  - environment health check
- `make session-status`
  - live repo, runtime, and eval snapshot
- `make startup-docs-read`
  - tracked startup-doc inspection
- `make caffeinate`
  - start repo-managed wake lock
- `make caffeinate-status`
  - report repo-managed wake-lock status
- `make decaffeinate`
  - stop repo-managed wake lock
- `make decaffeinate-status`
  - report closeout wake-lock status
- `make path-leak-check`
  - tracked repo path leak check
- `make path-leak-audit-local`
  - local/private lane path audit
- `make end-docs-check`
  - current-truth docs freshness gate
- `make end-pending-check`
  - fail closeout if eval `pending` is not `0`
- `make lint-docs`
  - tracked markdown validation
- `make check`
  - repo validation suite
- `make package-check`
  - package build validation
- `make package-install-check`
  - editable package import smoke
- `make security-checks`
  - dependency security audit
- `make end-preflight`
  - explicit branch-local validation only; does not stop background tasks or close the day
- `make end-git-check`
  - clean-main closeout check

## Pulse Eval Commands

- `huemiliator eval-pulse-start --count 15 --family red --quarantine-label "<label>"`
  - archive any current live proof surface into local `.local/parked/`
    artefacts, then seed the bounded pulse
- `huemiliator eval-pulse-label <output_id> anchor`
  - label one pulse row as `anchor`, `counted_seam`, or `excluded_noise`
- `huemiliator eval-pulse-label <output_id> excluded_noise --reason operator_artifact`
  - record the narrow exclusion reason when a row should stay visible but not
    counted
- `huemiliator eval-pulse-report <start_id> <end_id>`
  - summarize raw rows, counted total, exclusions by reason, and pulse verdict
