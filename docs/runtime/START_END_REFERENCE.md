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
   - `make caffeinate`
   - `make caffeinate-status`
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

Wake-lock rule:

- `make caffeinate` records only this repo's managed PID
- unmanaged `caffeinate` processes are reported but never adopted or stopped

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
  - `make check`
  - `make package-check`
  - `make package-install-check`
  - `make security-checks`
  - `make end-pending-check`
  - `make decaffeinate`
  - `make session-status`
2. Enforce the final git state:
  - `make end-git-check`

Preflight:

- `make end-preflight`
- runs the docs and validation path without requiring a clean synced `main`
- does not stop background tasks
- use it only when an explicit branch-local preflight was requested
- it does not close the day and it does not replace `make end`

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
