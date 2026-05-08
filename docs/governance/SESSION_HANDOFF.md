# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `codex/bigbrain/brown-family-correction-continue`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
  swatch resolution, family rank, replacement step, loss-line layer, and the
  first local evidence, judgment, and long-run sampler surface, plus the first
  completed contextual brown evidence slice
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Continue the brown-family classifier correction from the completed contextual
brown rerun.

Done in this kernel:

- used the fully judged closed brown rerun as the evidence base:
  - `201` unique brown pairs
  - `117` pass
  - `84` fail
  - dominant residual seams split between muted green and olive misroutes and
    the orange, yellow, and gold shoulder
- tightened brown classification so non-brown shoulders leave before ranking:
  - muted green and olive-leaning colours
  - high-chroma gold and yellow-orange colours
  - light apricot-orange colours
- preserved the darker earthy brown core in `brown`
- started fresh brown-family queues after each coherent classifier cut and
  judged while they filled
- stopped intermediate queues when they exposed a material repeated shoulder,
  then reset the local DB for a clean next queue
- the current fresh queue shows the old green/gold/orange shoulders leaving
  `brown`
- the current residual pressure is the low-chroma neutral-gray edge around
  `Pewter`, `Stone gray`, and `Canteen`
- stopped the latest fresh queue at an early judged checkpoint:
  - `55` brown rows recorded
  - `51` pass
  - `4` fail
  - `0` pending
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
- reclassified the bright gold shoulder so obvious loud gold and ochre cases
  can fall through to `orange` or `yellow`
- completed the fresh post-classification brown-family rerun
- the completed rerun kept the brown core stronger than the first pass:
  - `2368` brown rows were recorded
  - `45` were judged `pass`
  - `28` were judged `fail`
  - `2295` remain unjudged in the local queue
  - the primary residual failure shape is the muted green and olive seam
  - a smaller orange shoulder still leaks through at the tail
- added a tracked special finding note:
  - `docs/research/FINDING_1_CONTEXTUAL_BROWN.md`
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
  - bright gold and ochre shoulder colours can fall through to `orange` or
    `yellow` instead of staying in `brown`
  - muted green, olive, light apricot-orange, and high-chroma gold/yellow-orange
    shoulders can leave `brown` before ranking
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

- finish the fresh post-correction brown queue
- decide whether the low-chroma neutral-gray edge needs a family-boundary trim
- rerun the full validation suite after any further docs or classifier edits

## Stop State

- branch is `codex/bigbrain/brown-family-correction-continue`
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
- the current classifier correction is in progress on this branch
