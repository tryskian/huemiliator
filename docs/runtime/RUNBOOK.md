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
| open the native macOS UI picker | `huemiliator pick` |
| resolve a hex to the nearest frozen swatch | `huemiliator resolve <hex>` |
| emit the deterministic replacement shade | `huemiliator replace <hex>` |
| emit the full deterministic one-up reply | `huemiliator one-up <hex>` |
| initialise the local eval DB | `huemiliator eval-init` |
| log one deterministic output | `huemiliator eval-log <hex>` |
| list recent eval rows | `huemiliator eval-list --limit 10` |
| list pending eval rows | `huemiliator eval-list --verdict pending` |
| list one family only | `huemiliator eval-list --family brown` |
| judge one eval row | `huemiliator eval-judge <id> <pass\|fail>` |
| run the long local sampler | `huemiliator eval-sample-local` |
| run one family only | `huemiliator eval-sample-local --family brown` |
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
- the repo is docs-first with a small live picker-plus-resolution kernel
- the current live runtime surface is macOS-only
- the archived swatch source is frozen into the repo
- nearest-swatch resolution is live against the frozen local snapshot
- family routing and same-family rank are live against fixed runtime rules
- deterministic same-family replacement is live with a top-rank clamp
- deterministic short loss lines are live from a fixed family bank
- local SQLite evidence storage is live under `.local/`
- human PASS/FAIL judgment is live against stored rows
- long-run local source-order sampling is live against the frozen snapshot
- one follow-along experiment notebook is tracked under `output/jupyter-notebook/`
- no runtime claims should outrun the actual tree
- use the docs to lock the contract before widening the code

## Evidence Surface

- `huemiliator eval-init` creates the local DB at `.local/evals.sqlite`
- `huemiliator eval-log <hex>` records the deterministic output state after the
  colour decision
- `huemiliator eval-list --limit 10` prints recent rows for quick inspection
- `huemiliator eval-list --verdict pending` narrows the review queue
- `huemiliator eval-list --family brown` narrows the review queue to one family
- `huemiliator eval-judge <id> <pass|fail> --note "<note>"` applies a human
  binary verdict to one row
- `huemiliator eval-sample-local --duration-seconds 7200` starts the long-run
  local sampler
- add `--family <name>` to isolate one family while preserving source order in
  that subset
- the follow-along notebook lives at
  `output/jupyter-notebook/huemiliator-eval-surface.ipynb`

Recommended long run:

```sh
PYTHONPATH=src .venv/bin/python -m huemiliator eval-sample-local \
  --duration-seconds 7200
```

Default pacing is one row every `3` seconds so the queue can be judged while
it is still filling.

Example family run:

```sh
PYTHONPATH=src .venv/bin/python -m huemiliator eval-sample-local \
  --duration-seconds 7200 \
  --family brown
```

Judgment method:

- start review while the long run is still active
- do not wait for the run to finish before judging rows
- keep the queue on the active lane with `--verdict pending`
- add `--family <name>` when the live run is family-isolated

## Snapshot Refresh

```sh
PYTHONPATH=src .venv/bin/python scripts/freeze_margaret2_swatches.py
```

## Pull Request Hygiene

- default to `gh pr create --body-file <path>` for multiline PR descriptions
- avoid inline `--body "..."` when the content includes Markdown backticks or
  shell-sensitive characters
- if a body file is awkward, use a quoted heredoc rather than raw inline shell
  interpolation

Example:

```sh
gh pr create --title "<title>" \
  --body-file <path>
```

## Validation

For docs, picker-kernel, snapshot, resolution, or scaffold changes:

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
