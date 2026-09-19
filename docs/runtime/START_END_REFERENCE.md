# Start / End Reference

Compact command card. Use the [runbook](RUNBOOK.md) for the full operator
procedure and ownership boundaries.

## Start

```bash
make start
```

The routine prints workspace context, runs `make doctor-env`, summarizes the
required startup-doc titles/dates with `make startup-docs-read`, runs
`make session-status`, and prints the startup gate. The summary is not a
substitute for substantive reading. Before repo action, read the required
surface named by the [runbook](RUNBOOK.md), confirm path/host/branch/status,
return the five-point rehydrate, and name one active kernel.

Source: [Makefile](../../Makefile) and
[start routine](../../scripts/start_of_day_routine.sh).

### Coffee boundary

Coffee is independent Mac-wide state owned by the external Coffee Codex
plugin. Use `coffee` for status, `coffee start` to begin, and `coffee stop` to
release it. `make start` and `make end` never inspect, start, adopt, or stop it.

## End

```bash
make end
```

`make end` runs the docs freshness, environment snapshot, path-leak, docs,
shell, code, package, security, pending-eval, and session checks, then enforces
the final Git state with `make end-git-check`.

Success requires current-truth docs updated today, all validation passing,
`eval pending=0`, and clean local `main` synced with `origin/main`. Use
`make end-preflight` only for an explicitly requested branch-local preflight;
it does not replace closeout or require clean synced `main`.

`make end` leaves Coffee unchanged. Use `coffee stop` only as a separate,
explicit operator action.

Source: [Makefile](../../Makefile).
