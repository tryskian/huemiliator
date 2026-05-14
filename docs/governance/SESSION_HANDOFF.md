# Session Handoff

Last updated: 2026-05-13

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

- the third corrected red rerun is now fully judged at `id > 18423`
- current proof totals:
  - `1268` total rows
  - `1162` pass
  - `106` fail
  - `0` pending
  - `129` pair-level `pass`
  - `13` pair-level `fail`
- the loudest remaining red fail shapes are now:
  - peach shoulder still in `red`
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
