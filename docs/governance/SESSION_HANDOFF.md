# Session Handoff

Last updated: 2026-05-13

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
swatch resolution, family rank, replacement step, loss-line layer, and the
first local evidence, judgment, and long-run sampler surface, plus the first
completed contextual brown evidence slice, plus explicit `make start` /
`make end` operator rituals
- branch ruleset: active on default branch
- GitHub automation: CI, dependency review, Python audit, and weekly
  Dependabot updates aligned to the current toy-family baseline
- local hook hygiene: tracked `pre-commit` and `pre-push` baselines now live
  through native repo commands

## Active Kernel

Pause runtime expansion again and end from a truthful clean-main stop state
after parking the unfinished `red` correction lane off-branch.

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
- added a conservative orange family-first classifier cut on this branch:
  - demotes pale low-chroma warm shoulder colours out of `orange` and into
  `neutral`
  - demotes the darker muted olive shoulder out of `orange` and into `yellow`
  - evicts `68` unique orange fail pairs from the closed warm slice
  - evicts `0` unique orange pass pairs from the closed warm slice
- added a tracked special finding note:
  - `docs/research/FINDING_1_CONTEXTUAL_BROWN.md`
- kept the evidence write path downstream of the deterministic colour decision
- synced tracked docs and diagram to the evidence surface truth
- added the compact day-open/day-close operator surface:
  - `docs/runtime/START_END_REFERENCE.md`
  - `make start`
  - `make rituals`
  - `make end`
- resumed runtime work long enough to draft the first `red` family-first
  correction in a local branch
- ran a fresh `red`-only rerun against that parked correction at `id > 15325`
- stopped before packaging the lane because the repo/operator quality was too
  unstable to trust a clean runtime closeout on-branch
- archived the unfinished red lane into local recovery artifacts:
  - local patch backup from the original checkout:
    `.local/parked/2026-05-12-red-family-correction.patch`
  - local patch backup from the retired worktree lane:
    `.local/parked/2026-05-12-red-family-correction-automation.patch`
  - local stash:
    `stash@{0}` with the duplicate checkout copy
- captured the exact parked red-lane stop state in this tracked handoff so the
  repo no longer depends on a dirty worktree as an implicit source of truth

## Current Contract

- platform: macOS local only
- input: native UI colour picker
- canonical user state: hex code
- inventory: swatch reference from
the archived
`[margaret2/pantone-colors](https://github.com/margaret2/pantone-colors)`
source, surfaced at
`[margaret2.github.io/pantone-colors](https://margaret2.github.io/pantone-colors/)`,
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

## Next Kernel

- the `2` hour warm-cohort run is complete
- the fresh warm slice is `2374` rows at `id > 5831`
- the warm slice is now fully judged:
  - `1824` pass
  - `550` fail
  - `0` pending
- row-level family totals:
  - `brown`: `332` pass / `69` fail
  - `orange`: `513` pass / `337` fail
  - `red`: `676` pass / `100` fail
  - `yellow`: `303` pass / `44` fail
- pair-level family totals:
  - `brown`: `117` pass / `29` fail
  - `orange`: `181` pass / `120` fail
  - `red`: `264` pass / `44` fail
  - `yellow`: `127` pass / `20` fail
- the loudest residual warm failure lane was `orange`
- the orange family-first correction is now live:
  - `68` unique orange fail pairs evicted
  - `0` unique orange pass pairs evicted
- the orange-only rerun is now complete
- the fresh orange slice is `2374` rows at `id > 8205`
- the orange slice is now fully judged:
  - `1826` pass
  - `548` fail
  - `0` pending
- pair-level orange totals are now:
  - `181` pass
  - `52` fail
  - `0` mixed
- the conservative orange family-first cut validated cleanly against the closed
warm audit:
  - all `181` previously judged orange pass pairs stayed in-lane
  - unique orange fail pairs dropped from `120` to `52`
  - the full `68` pair reduction matches the pre-rerun eviction estimate
- the residual orange failure signal is now much narrower:
  - main seam: low-chroma beige, latte, and cream shoulder
  - smaller seam: muted olive carry-through
  - repeated beige and cream failures include:
    - `Natural -> Roebuck`
    - `Cafe au lait -> Appleblossom`
    - `Bellini -> Beige`
    - `Tan -> Latte`
    - `Almond cream -> Double cream`
  - repeated olive failures include:
    - `Rattan -> Ecru olive`
    - `Ecru olive -> Bronze mist`
    - `Amberglow -> Tawny olive`
    - `Tawny olive -> Ceylon yellow`
- the second orange family-first correction is now live:
  - low-chroma taupe shoulder colours fall back into `neutral`
  - soft beige and cream shoulder colours fall back into `neutral`
  - it evicts `19` unique orange fail pairs from the closed orange rerun
  - it evicts `0` unique orange pass pairs from the closed orange rerun
- the second orange-only rerun is now complete
- the fresh orange slice is `2372` rows at `id > 10579`
- the orange slice is now fully judged:
  - `2033` pass
  - `339` fail
  - `0` pending
- pair-level orange totals are now:
  - `184` pass
  - `30` fail
  - `0` mixed
- the second cut improved the closed orange signal again:
  - pair-level fail count dropped from `52` to `30`
  - pair-level pass count rose from `181` to `184`
- the residual orange failure signal is still attributable:
  - soft beige and peach ladder
  - ochre and olive carry-through
  - repeated soft beige and peach failures include:
    - `Autumn blonde -> Winter wheat`
    - `Winter wheat -> Mellow buff`
    - `Mellow buff -> Pink sand`
    - `Pink sand -> Chamomile`
    - `Tender peach -> Curds & whey`
  - repeated ochre and olive failures include:
    - `Doe -> Golden fleece`
    - `Buff -> Fenugreek`
    - `Desert dust -> Sandstorm`
    - `Ecru olive -> Bronze mist`
    - `Amberglow -> Tawny olive`
- orange is now materially tighter than the other untouched warm families
- the next family-by-family sampler moved to `red`:
  - warm-audit row totals: `676` pass / `100` fail
  - warm-audit pair totals: `264` pass / `44` fail
- the `red`-only rerun is now complete
- the fresh red slice is `2374` rows at `id > 12951`
- the red slice is now fully judged:
  - `2049` pass
  - `325` fail
  - `0` pending
- pair-level red totals are now:
  - `264` pass
  - `44` fail
  - `0` mixed
- the closed red rerun reproduced the warm-audit red pair totals exactly:
  - `264` pass pairs
  - `44` fail pairs
  - no pair drift across the rerun
- the closed red rerun has now been read by pair cluster
- `red` is stable enough for a direct family correction when runtime work
resumes
- `yellow` stays queued behind `red`
- the residual red failure signal is durable, not noisy:
  - dusty pink and cosmetic rose ladder
  - brown, cocoa, and wine seam
  - repeated dusty pink failures include:
    - `Cloud pink -> Rocky road`
    - `Evening sand -> Silver pink`
    - `Rose cloud -> Clove`
    - `Silver pink -> Rose quartz`
    - `Pearl blush -> Peachy keen`
  - repeated brown and wine failures include:
    - `Bitter chocolate -> Marron`
    - `Brown stone -> Pink dogwood`
    - `English rose -> Chocolate fondant`
    - `Root beer -> Mink`
    - `Veiled rose -> Vineyard wine`
- one unfinished off-main red experiment is preserved but not landed:
  - the first `red` family-first correction was drafted in a parked worktree
  - the fresh rerun against that parked correction stopped with:
    - `2372` rows at `id > 15325`
    - `702` pass
    - `378` fail
    - `1292` pending
    - `78` fully judged pair-level `pass`
    - `42` fully judged pair-level `fail`
    - `151` pair-level still unjudged
  - because that lane never closed to `0` pending and never merged, do not
    treat it as live runtime truth on `main`

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
- the next runtime family lane is known:
  - first `red` correction
  - then `yellow`
- visibility can take priority now without losing the runtime thread
- first long-run local sampler is in place
- first follow-along notebook is in place
- the fully judged contextual brown evidence slice is in place
- the closed warm audit is in place
- the orange family-first correction is in place
- the second orange-only rerun is closed from `id > 10579`
- the red-only rerun is closed from `id > 12951`
- `main` is intentionally back to a clean landed state with no active sampler
- there is currently no active Huemiliator automation
- the only remaining local automations are unrelated paused lanes in sibling
  repos
- the unfinished first red-correction lane is parked locally instead of merged
- the archived red lane currently survives only as local recovery artifacts:
  - `.local/parked/2026-05-12-red-family-correction.patch`
  - `.local/parked/2026-05-12-red-family-correction-automation.patch`
  - `stash@{0}`
  - changed files:
    - `docs/governance/DECISIONS.md`
    - `docs/governance/SESSION_HANDOFF.md`
    - `docs/research/README.md`
    - `docs/runtime/ARCHITECTURE.md`
    - `src/huemiliator/families.py`
    - `tests/test_families.py`
- the current operator/docs kernel is also in progress on a separate branch:
  - branch:
    `codex/bigbrain/exact-parked-red-state`
  - current validation state:
    - `make check`: pass
    - `make end-preflight`: pass
    - `make end`: fail until the branch is merged and rerun from clean synced
      `main`
- the next runtime family lane is still known:
  - resume or discard the parked `red` correction lane
  - then `yellow`
