# Start / End Reference

This is the compact operator sheet for the canonical day-open/day-close
commands.

## Start

Command:

```bash
make start
```

Sequence:

1. Print workspace context:
   - repo root
   - active branch
   - `git status --short --branch`
2. Run the startup safety path:
   - `make doctor-env`
   - `make startup-docs-read`
   - `make session-status`
3. Inspect the tracked startup docs in-band:
   - `README.md`
   - `docs/governance/CHARTER.md`
   - `docs/governance/DECISIONS.md`
   - `docs/runtime/RUNBOOK.md`
   - `docs/runtime/ARCHITECTURE.md`
   - `docs/governance/SESSION_HANDOFF.md`
   - local peanut handoff if present
4. Print the startup gate:
   - `make start` completed the mechanical bootstrap and startup-doc read
5. Complete rehydrate before repo action:
   - use the inspected startup-doc surface
   - return 5 bullets covering current state, risks, next kernel, repo or
     worktree context, and active branch
   - confirm repo path, host vs devcontainer mode, active branch, and whether
     the thread is on clean `main` or a feature branch
   - apply the no-guessing controls
   - run one active kernel at a time
   - execute the `Next Kernel` from `SESSION_HANDOFF` with full validation

Source of truth:

- [Makefile](../../Makefile)
- [scripts/start_of_day_routine.sh](../../scripts/start_of_day_routine.sh)

Power-control boundary:

- the repo lifecycle does not start, inspect, or stop Mac-wide keep-awake state
- the external Coffee Codex plugin owns the one shared Mac-wide session
- use `coffee`, `coffee start`, and `coffee stop` as separate explicit actions
- `make start` and `make end` never invoke those actions

Startup completion rule:

- `make start` only finishes the mechanical bootstrap
- startup completes when the next repo update proves the inspected doc surface
  was used and names one active kernel

## End

Command:

```bash
make end
```

Sequence:

1. Run the closeout validation path:
  - `make end-docs-check`
  - `make doctor-env`
  - tracked path leak check
  - local path leak audit
  - `make lint-docs`
  - `make scripts-check`
  - `make check`
  - `make package-check`
  - `make package-install-check`
  - `make security-checks`
  - `make end-pending-check`
  - `make session-status`
2. Enforce the final git state:
  - `make end-git-check`

Preflight:

- `make end-preflight`
- runs the docs and validation path without requiring a clean synced `main`
- use it only when an explicit branch-local preflight was requested
- it does not close the day and it does not replace `make end`

Dependency maintenance:

- `make refresh-deps`
- run it after merged Dependabot or dependency metadata work, then run
  `make security-checks`

Expected result:

- when the operator says `close out the day`, the command is `make end`
- `make end` should exit successfully only when:
  - the required stop-state docs were updated today
  - the validation path passes
  - eval `pending` is `0`
  - the repo ends on clean synced `main`
- `make session-status` is only a snapshot line inside the routine
- the actual stop-state failure comes from `make end-git-check`

Source of truth:

- [Makefile](../../Makefile)
