# Start / End Reference

This is the compact operator sheet for the canonical day-open/day-close
commands.

## Start

Command:

```bash
make start
```

Sequence:

1. Print the canonical docs to read:
  - `README.md`
  - `docs/governance/CHARTER.md`
  - `docs/governance/DECISIONS.md`
  - `docs/runtime/RUNBOOK.md`
  - `docs/runtime/ARCHITECTURE.md`
  - `docs/governance/SESSION_HANDOFF.md`
  - local `docs/peanut/governance/SESSION_HANDOFF.md` if present
2. Print workspace context:
  - repo root
  - active branch
  - `git status --short --branch`
3. Run the startup safety path:
  - `make doctor-env`
  - `make session-status`

Source of truth:

- [Makefile](../../Makefile)

## End

Command:

```bash
make end
```

Sequence:

1. Run the closeout validation path:
  - `make end-docs-check`
  - `make doctor-env`
  - `make check`
  - `make session-status`
2. Enforce the final git state:
  - `make end-git-check`

Preflight:

- `make end-preflight`
- runs the docs and validation path without requiring a clean synced `main`

Expected result:

- `make end` should exit successfully only when:
  - the required stop-state docs were updated today
  - the validation path passes
  - the repo ends on clean synced `main`
- `make session-status` is only a snapshot line inside the routine
- the actual stop-state failure comes from `make end-git-check`

Source of truth:

- [Makefile](../../Makefile)
