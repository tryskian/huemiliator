# Runbook

This is the operator guide for local setup, procedure, and validation.

Use `docs/runtime/ARCHITECTURE.md` for system shape.

## Start A Session

1. Read the tracked instruction surface:
   - `README.md`
   - `docs/governance/CHARTER.md`
   - `docs/governance/DECISIONS.md`
   - `docs/runtime/ARCHITECTURE.md`
   - `docs/runtime/RUNBOOK.md`
   - `docs/governance/SESSION_HANDOFF.md`
2. Confirm the repo root:
   - `huemiliator`
3. Treat the tracked docs as current project state.
4. Install or refresh the local environment:
   - `make install`
5. If the kernel will change tracked files, work from a `codex/bigbrain/...`
   branch rather than `main`.
6. State the active kernel before editing tracked files.

## Everyday Commands

| Task | Command |
| --- | --- |
| show the repo file tree | `find . -maxdepth 3 -type f \| sort` |
| show tracked docs | `find docs -maxdepth 3 -type f \| sort` |
| inspect recent history | `git log --stat --oneline --max-count=5` |
| search the current docs surface | `rg -n "<term>" README.md docs src tests` |
| create a work branch | `git switch -c codex/bigbrain/<kernel-slug>` |
| install or refresh the runtime env | `make install` |
| check the environment | `make doctor-env` |
| show session status | `make session-status` |
| open the native macOS picker | `huemiliator pick` |
| run tests | `make test` |
| run lint checks | `make lint` |
| run format checks | `make format-check` |
| format the Python surface | `make format` |
| run static typing | `make typecheck` |
| run the current baseline checks | `make check` |
| build the package | `make package-check` |
| show the current runtime status | `make app` |

## Current Posture

- the repo is public
- `main` is protected by the default-branch ruleset
- tracked changes should land through `codex/bigbrain/...` branches and squash PRs
- the repo is docs-first with a small live picker kernel
- the current live runtime surface is macOS-only
- no runtime claims should outrun the actual tree
- swatch matching and one-up logic are not implemented yet
- use the docs to lock the contract before widening the code

## Validation

For docs, picker-kernel, or scaffold changes:

- read back the changed docs
- keep claims aligned with the actual tree
- run `make doctor-env`
- run `make check`

For later runtime-contract changes:

- sweep `README.md`
- sweep `docs/runtime/ARCHITECTURE.md`
- sweep `docs/research/README.md`
- sweep `docs/diagrams/PIPELINE.md`
- sweep `docs/governance/SESSION_HANDOFF.md`
- record durable choices in `docs/governance/DECISIONS.md`
