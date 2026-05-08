# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
  swatch resolution, family rank, replacement step, loss-line layer, and the
  first local evidence, judgment, and long-run sampler surface, plus the first
  completed contextual brown evidence slice and the residual brown shoulder
  classifier correction
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Decide the next brown-edge correction from the completed contextual brown rerun.

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
- reclassified the bright gold shoulder so obvious loud gold and ochre cases
  can fall through to `orange` or `yellow`
- completed the fresh post-classification brown-family rerun
- tightened the brown classifier again from the fully judged closed brown rerun:
  - evidence base: `201` unique brown pairs, `117` pass, `84` fail
  - muted olive and khaki shoulders now leave `brown`
  - loud orange, yellow, and gold shoulders now leave `brown`
  - the local snapshot's active brown subset is now `125` swatches
- ran a no-interval full-current-brown smoke sample:
  - `125` rows recorded
  - no replacement crossed out of the runtime `brown` family
  - this was not the required two-hour judged run
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

- keep judging the completed brown queue in small focused sweeps
- decide whether the next correction should target:
  - any remaining named gold or ochre cases inside `brown`
  - replacement quality after the family boundary holds
- run the requested fresh two-hour `brown` family eval and judge it while it
  fills before claiming the correction as settled

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
- the first contextual brown evidence slice is ready to publish from this branch
- the residual brown shoulder classifier correction is implemented but still
  needs the requested two-hour judged run before merge confidence
