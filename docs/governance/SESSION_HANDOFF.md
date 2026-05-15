# Session Handoff

Last updated: 2026-05-15

## Start Here

- Run `make start` before repo work.
- Read:
  - `README.md`
  - `docs/governance/CHARTER.md`
  - `docs/governance/DECISIONS.md`
  - `docs/runtime/RUNBOOK.md`
  - `docs/runtime/ARCHITECTURE.md`
  - `docs/governance/SESSION_HANDOFF.md`
- Confirm:
  - repo root is `/abs/path/to/huemiliator`
  - active branch
  - whether the thread is on clean `main` or a feature branch
- Name exactly one active kernel before branching, searching, or editing.

## Current State

- repo: `huemiliator`
- branch: `main`
- status: clean stop state with the third `red` family-instruction correction
  landed and the live eval DB narrowed to the current proof surface
- branch ruleset: active on default branch
- GitHub automation: CI, dependency review, Python audit, and weekly
  Dependabot updates aligned to the current toy-family baseline
- local hook hygiene: tracked `pre-commit` and `pre-push` baselines now live
  through native repo commands
- operator surface: aligned with the toy-family start/end contract:
  - `make start`
  - `make end`
  - `make end-preflight`
  - `make end-git-check`
  - `make caffeinate`
  - `make caffeinate-status`
  - `make decaffeinate-status`
  - `make decaffeinate`
  - `make doctor-env`
  - `make session-status`
  - `make rituals`
- wake-lock ownership: unmanaged `caffeinate` processes are reported but not
  adopted or stopped
- active sampler: none
- active Huemiliator automation: none
- active live DB proof surface is now only the fully judged third red rerun at
  `id > 18423`:
  - `1268` rows
  - `1162` pass
  - `106` fail
  - `0` pending
  - `129` pair-level `pass`
  - `13` pair-level `fail`
- superseded eval rows are quarantined locally instead of staying in the live
  DB:
  - cutoff: `id <= 18423`
  - `17371` rows frozen locally
- local archive artifacts for the old-eval quarantine:
  - `.local/parked/2026-05-13-old-evals-pre-third-rerun-quarantine.tsv`
  - `.local/parked/2026-05-13-old-evals-pre-third-rerun-quarantine.sql`
  - `.local/parked/2026-05-13-old-evals-pre-third-rerun-summary.md`
- local archive artifacts for the archived pre-second-correction pending
  residue:
  - `.local/parked/2026-05-13-red-pre-second-correction-pending.tsv`
  - `.local/parked/2026-05-13-red-pre-second-correction-pending.sql`
  - `.local/parked/2026-05-13-red-pre-second-correction-summary.md`

## Active Kernel

Use the fully judged third red rerun as the next proof surface, not the old
mixed eval history and not a fresh rerun yet.

Done in this kernel:

- kept judging the old fresh red queue until the fail shape was clearly
  repetitive instead of noisy
- confirmed that the same duplicate block kept resolving to:
  - red-core and warm-red `pass`
  - peach, pink, and brown shoulder `fail`
- closed the old active queue by archiving the remaining pending rows as local
  pre-fix evidence
- cleared those archived pending rows out of the live DB
- cut the second `red` family correction into runtime instructions:
  - broadened the pink-peach shoulder out of `red` and into `pink`
  - broadened the low-chroma brown and wine seam out of `red` and into `brown`
  - kept the stable soft-red lane and darker red core in `red`
- validated the correction:
  - `PYTHONPATH=src .venv/bin/python -m pytest tests/test_families.py`
  - `make check`
- finished judging the second corrected rerun and confirmed that it still left
  a durable residual seam
- cut a third narrow `red` correction into runtime instructions:
  - stronger muted pink-peach shoulder demotion out of `red`
  - stronger low-chroma brown extension out of `red`
  - stable red-core and coherent muted-red local steps kept in `red`
- validated that third correction:
  - `PYTHONPATH=src .venv/bin/python -m pytest tests/test_families.py`
  - `make check`
- fully judged the fresh third corrected rerun at `id > 18423`
- quarantined every older eval row out of `eval_outputs` so the live DB now
  holds only the closed third-rerun proof surface

Next in this branch:

- use the closed third-rerun fail cluster to decide the next narrow `red`
  instruction cut
- do not start another rerun until that next correction is explicit

## Current Contract

- platform: macOS local only
- input: native UI colour picker
- canonical user state: hex code
- inventory: swatch reference from the archived
  [`margaret2/pantone-colors`](https://github.com/margaret2/pantone-colors)
  source, surfaced at
  [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/),
  frozen locally at `data/margaret2_swatches.json`, with Pantone as a
  secondary naming layer
- swatch resolution: nearest frozen swatch match by `delta-e cie76` with
source-order tie-break
- Huemiliator-owned structure:
  - family assignment from fixed neutral and hue thresholds
  - within-family rank from one fixed strength ladder
  - brown rank demotes the yellow/gold/olive shoulder below the earthy core
  - bright gold, warm orange-yellow, and muted olive shoulder colours can fall
  through to non-brown families instead of staying in `brown`
  - pale low-chroma warm shoulder colours can fall back out of `orange` and
  into `neutral`
  - darker muted olive shoulder colours can fall out of `orange` and into
  `yellow`
  - deterministic same-family replacement by next rank with top-rank clamp
  - deterministic short loss line from a fixed family bank
- local evidence lane:
  - SQLite storage at `.local/evals.sqlite`
  - human PASS/FAIL verdicts on stored rows
  - long-run local sampler over the frozen snapshot
  - local eval scope alias `warm` = `brown`, `red`, `orange`, `yellow`
  - one follow-along notebook at
  `output/jupyter-notebook/huemiliator-eval-surface.ipynb`
- current output target:
  - replacement shade
  - one short loss line

## Research Snapshot

- Huemiliator is still pre-beta.
- The current live proof surface is the fully judged third `red` rerun at
  `id > 18423`.
- Older eval rows are quarantined locally and should not be mixed back into
  the live truth surface.
- The current next runtime question is still the narrow `red` correction from
  the closed third-rerun proof surface.
- Do not start a new sampler until the next correction is explicit.
- `yellow` stays queued behind the next `red` correction.

## Next Kernel

- the third corrected red rerun is now fully judged at `id > 18423`
- current proof totals:
  - `1268` total rows
  - `1162` pass
  - `106` fail
  - `0` pending
  - `129` pair-level `pass`
  - `13` pair-level `fail`
- the loudest remaining red fail shapes are now:
  - warm-clay or peach shoulder still in `red`
  - brown or brown-orange shoulder still in `red`
  - dark or muted red clusters that still jump into pale rose/pink steps
- repeated fail pairs include:
  - `Desert rose -> Burnt brick`
  - `Garnet rose -> Desert rose`
  - `Slate rose -> Crabapple`
  - `Auburn -> Tawny orange`
  - `Terra cotta -> Burnt henna`
  - `Oxblood red -> Withered rose`
  - `Peony -> Marsala`
  - `Burlwood -> Mellow rose`
  - `Renaissance rose -> Impatiens pink`
- the next live kernel is not `yellow`
- the next live kernel is the next narrow `red` correction derived from this
  closed third-rerun proof surface
- current recommendation from the active proof surface:
  - keep the coherent muted-red local pass cluster in `red`
  - cut a narrow warm-clay or peach shoulder escape from `red` to `orange`
  - rerun `red`
- `yellow` stays queued behind the next `red` correction

## Guardrails

- Keep one active kernel at a time.
- Do not treat old mixed eval history as the live proof surface.
- Do not start another rerun until the next correction is explicit.
- Keep `.local/` artifacts local unless explicitly promoted.
- Land tracked changes through PRs and finish on clean synced `main`.

## Close A Session

- Use `make end-preflight` for branch-local validation before clean-main
  enforcement.
- Merge through the protected-branch PR path.
- Switch back to `main` and pull with `--ff-only`.
- Run `make end` on `main`.
- Treat `make end` failure as a real closeout blocker unless the failure is
  explicitly diagnosed and fixed.

## Copy/Paste Refresh Prompt

`Read README.md, docs/governance/CHARTER.md, docs/governance/DECISIONS.md, docs/runtime/RUNBOOK.md, docs/runtime/ARCHITECTURE.md, docs/governance/SESSION_HANDOFF.md, and local docs/peanut/governance/SESSION_HANDOFF.md if present. In 5 bullets: current state, risks, and next kernel. Before starting implementation, confirm environment/workspace context: canonical repo path is /abs/path/to/huemiliator, confirm host vs devcontainer mode, confirm active git branch, and say whether the thread is on clean main or a feature branch. Apply no-guessing controls: prefer repo-scoped edits and do not modify user shell profile file or global VS Code settings unless explicitly approved in-chat. Run in one active kernel at a time. Then execute the Next Kernel from SESSION_HANDOFF with minimal behavior drift and full validation.`

## Stop State

- `main` is clean and protected
- public repo is live
- license surface is in place
- GitHub automation surface is in place
- first picker kernel is in place
- archived swatch snapshot is in place
- nearest swatch resolution is in place
- first family taxonomy and rank are in place
- first deterministic replacement step is in place
- first deterministic loss-line layer is in place
- first local SQLite evidence surface is in place
- first human PASS/FAIL judgment lane is in place
- first long-run local sampler is in place
- first follow-along notebook is in place
- the fully judged contextual brown evidence slice is in place
- `main` is intentionally back to a clean landed state with no active sampler
- there is currently no active Huemiliator automation
- the active proof surface is the closed third corrected `red` rerun at
  `id > 18423`
- the next runtime family lane is still known:
  - next narrow `red` correction
  - then `yellow`
