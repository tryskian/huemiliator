# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `codex/bigbrain/brown-family-correction`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
  swatch resolution, family rank, replacement step, loss-line layer, and the
  first local evidence, judgment, and long-run sampler surface, plus the first
  completed contextual brown evidence slice
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Run one extended warm-cohort eval as the only active sampler.

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
- added `--family warm` as a local warm-cohort alias over:
  - `brown`
  - `red`
  - `orange`
  - `yellow`
- locked the live-review method:
  - keep exactly one live sampler active in the repo at a time
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
- the closed rerun now has full judgment coverage:
  - `2368` brown rows
  - `1394` row-level `pass`
  - `974` row-level `fail`
  - `0` pending
  - `201` unique deterministic brown pairs
  - `117` pair-level `pass`
  - `84` pair-level `fail`
- the closed signal shows two real family seams:
  - muted green and olive seam
  - orange, yellow, and gold shoulder
- added a conservative family-first classifier cut on this branch:
  - evicts `55` unique fail pairs from the brown lane
  - evicts `0` unique pass pairs from the brown lane
  - targets warm orange-yellow shoulder colours and the muted olive seam
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
  - bright gold, warm orange-yellow, and muted olive shoulder colours can fall
    through to non-brown families instead of staying in `brown`
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

## Next Kernel

- the warm-cohort eval is live with `--family warm`
- keep that warm run as the only active sampler while it is being judged
- judge only fresh warm-scope rows while the queue is still filling
- measure how the warm shoulders behave once brown is not isolated
- decide whether the next correction belongs in warm-scope routing or inside a
  narrower family lane

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
- the next live check is the active warm-cohort run against the same
  conservative family-first cut
