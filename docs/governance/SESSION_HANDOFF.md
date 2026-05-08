# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `codex/bigbrain/sqlite-evidence-notebook`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
  swatch resolution, family rank, replacement step, loss-line layer, and the
  first local evidence, judgment, and long-run sampler surface
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Judge the fresh brown-family rerun against the revised brown rank and measure
whether the old yellow/gold drift cluster has really collapsed.

Done in this kernel:

- added a shared deterministic one-up state for CLI, storage, and notebook use
- added the first local SQLite evidence lane at `.local/evals.sqlite`
- exposed:
  - `huemiliator eval-init`
  - `huemiliator eval-log <hex>`
  - `huemiliator eval-list --limit <n>`
- added the first human judgment lane:
  - `huemiliator eval-list --verdict <state>`
  - `huemiliator eval-judge <id> <pass|fail> --note "<note>"`
- added the first long-run local sampler:
  - `huemiliator eval-sample-local --count <n>`
  - `huemiliator eval-sample-local --duration-seconds <seconds>`
  - source-order cycle over the frozen snapshot
  - default `3` second interval for judgeable pacing
- added `--family <name>` to isolate one family without changing the sampler
  method
- added `eval-list --family <name>` so review can stay inside the active family
- locked the live-review method:
  - judge rows while the run is still active
  - do not wait for the queue to finish filling
- added the first follow-along notebook at
  `output/jupyter-notebook/huemiliator-eval-surface.ipynb`
- tightened the brown family boundary so darker earthy warms stop collapsing
  into `neutral` or staying `orange`
- revised the brown rank so yellow/gold/olive shoulders sit below the earthy
  brown core
- started a fresh brown-family rerun against the revised brown rank
- the early post-fix signal is stronger:
  - at last check: `247` new brown rows
  - `8` pass
  - `2` fail
  - `237` pending
  - loud yellow/gold drift is no longer the main early failure shape
  - the remaining early failures are muted green-edge cases
- kept the evidence write path downstream of the deterministic colour decision
- synced tracked docs and diagram to the evidence surface truth

## Current Contract

- platform: macOS local only
- input: native UI colour picker
- canonical user state: hex code
- inventory: swatch reference from
  the archived
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
  - deterministic same-family replacement by next rank with top-rank clamp
  - deterministic short loss line from a fixed family bank
- local evidence lane:
  - SQLite storage at `.local/evals.sqlite`
  - human PASS/FAIL verdicts on stored rows
  - long-run local sampler over the frozen snapshot
  - one follow-along notebook at
    `output/jupyter-notebook/huemiliator-eval-surface.ipynb`
- current output target:
  - replacement shade
  - one short loss line

## Next Kernel

- continue judging the fresh `brown` rerun while it is still filling
- keep the family filter in review so the queue stays on the active lane
- decide whether the muted green edge needs its own brown-rank correction
- decide whether the next gate should judge family correctness first or full
  replacement correctness

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
- next work can stay on the current branch until the evidence slice feels
  ready to publish
