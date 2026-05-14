# Research

Last updated: 2026-05-14

Huemiliator keeps the tracked research lane small on purpose.

The repo is still in pre-beta, but the first runtime slice now exists.

Raw notes and private scratch material stay in the local `docs/peanut/` lane.

## Tracked Findings

- [Finding 1: Contextual Brown](./FINDING_1_CONTEXTUAL_BROWN.md)

## Current Phase

Current phase:

- `pre-beta`
- `deterministic final reply plus local evidence, judgment, and long-run sampler`

Current question:

Can the resolved swatch support a stable Huemiliator-owned family taxonomy and
same-family one-up rule?

Current finding:

- the repo baseline is set
- the input surface is locked to the native UI colour picker for v1
- the first live runtime kernel returns canonical hex from the native picker
- the canonical swatch reference is locked to the archived
  [`margaret2/pantone-colors`](https://github.com/margaret2/pantone-colors)
  source surfaced at
  [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
- the archived source is frozen locally at `data/margaret2_swatches.json`
- nearest swatch resolution now runs against the frozen local snapshot
- the current distance rule is `delta-e cie76` with a source-order tie-break
- Pantone is a secondary naming layer, not the primary source
- the first family taxonomy is now fixed to:
  - `neutral`
  - `brown`
  - `red`
  - `orange`
  - `yellow`
  - `green`
  - `blue`
  - `purple`
  - `pink`
- the first same-family rank ladder is now fixed
- the first deterministic replacement step is now fixed to next-rank,
  same-family, and top-rank clamp
- the short loss line now comes from a fixed family-keyed bank
- the first local SQLite evidence surface is now live
- the first human PASS/FAIL judgment lane is now live
- the first long-run local sampler is now live
- the first follow-along notebook is now tracked
- the first tracked local hook baseline is now live:
  - repo-native `pre-commit` and `pre-push`
  - native repo commands for format, lint, typecheck, and test hygiene
- the first family-boundary refinement is now live:
  - darker earthy warms promote into `brown` earlier
  - pale warm neutrals stay where they are
- the first brown-rank refinement is now live:
  - the yellow/gold/olive shoulder is demoted below the earthy brown core
  - brown replacements no longer climb by raw chroma alone
- the bright gold shoulder reclassification is now live:
  - loud gold and ochre cases can fall through to `orange` or `yellow`
  - the brown lane no longer has to contain obvious bright-gold cases by rank
    alone
- `brown` is proving to be a good pressure lane because it is a contextual
  colour bucket rather than a clean spectral one:
  - it often behaves more like dark orange, muted orange, or olive-adjacent
    warm neutral than a single stable hue
  - that makes brown-family drift a useful research signal, not just a bug
- the first judged brown run exposed a broad replacement drift cluster:
  - loud `yellow`
  - `gold`
  - `olive`
- the completed post-classification brown rerun is materially stronger than the
  first pass:
  - `2368` brown rows were recorded in the rerun
  - the queue is now fully judged:
    - `1394` row-level `pass`
    - `974` row-level `fail`
    - `0` pending
  - the closed deterministic signal is:
    - `201` unique brown pairs
    - `117` pair-level `pass`
    - `84` pair-level `fail`
  - the earthy brown core now holds much better than it did in the first run
  - the closed residual failure signal has two real family seams:
    - muted green and olive seam
    - orange, yellow, and gold shoulder
  - repeated muted green and olive failures include:
    - `Beech -> Covert green`
    - `Capers -> Dusky green`
    - `Black ink -> Grape leaf`
    - `Covert green -> Aloe`
  - repeated warm-shoulder failures include:
    - `Apricot orange -> Yam`
    - `Burnt orange -> Gold flame`
    - `Jaffa orange -> Hawaiian sunset`
    - `Golden ochre -> Autumnal`
    - `Topaz -> Buckthorn brown`
    - `Cadmium yellow -> Orange pepper`
  - the next conservative family-first correction is now live on the current
    branch:
    - it evicts `55` unique fail pairs from the brown lane
    - it evicts `0` unique pass pairs from the brown lane
    - it targets warm orange-yellow shoulder colours and the muted olive seam
- the first family-first correction now says:
  - `fail` is evidence
  - `evict` is the classifier change made because of that evidence
- the orange family-first correction is now live:
  - pale low-chroma warm shoulder shades fall back into `neutral`
  - darker muted olive shoulder shades fall into `yellow`
  - the closed warm audit shows:
    - `68` unique orange fail pairs evicted
    - `0` unique orange pass pairs evicted
- the orange-only rerun is now complete and fully judged at `id > 8205`:
  - `2374` rows
  - `1826` pass
  - `548` fail
  - `0` pending
  - `181` pair-level `pass`
  - `52` pair-level `fail`
  - `0` mixed pairs
  - the conservative orange family-first cut validated exactly against the
    closed warm audit:
    - all `181` previously judged orange pass pairs stayed in-lane
    - unique orange fail pairs dropped from `120` to `52`
    - the observed `68` pair reduction matches the pre-rerun eviction estimate
  - the remaining orange failure signal is no longer a broad shoulder:
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
  - low-chroma taupe shoulder shades fall back into `neutral`
  - soft beige and cream shoulder shades fall back into `neutral`
  - the closed orange rerun shows:
    - `19` unique orange fail pairs evicted
    - `0` unique orange pass pairs evicted
  - the repeated beige and taupe failures targeted by this cut include:
    - `Natural -> Roebuck`
    - `Cafe au lait -> Appleblossom`
    - `Cornstalk -> Incense`
    - `Bellini -> Beige`
    - `Tan -> Latte`
    - `Soybean -> Curds & whey`
- the second orange-only rerun is now complete and fully judged at `id > 10579`:
  - `2372` rows
  - `2033` pass
  - `339` fail
  - `0` pending
  - `184` pair-level `pass`
  - `30` pair-level `fail`
  - `0` mixed pairs
  - the second cut improved the closed orange signal again:
    - pair-level fail count dropped from `52` to `30`
    - pair-level pass count rose from `181` to `184`
  - the residual orange failure signal is still attributable, not broad:
    - soft beige and peach ladder
    - ochre and olive carry-through
  - repeated soft beige and peach failures include:
    - `Autumn blonde -> Winter wheat`
    - `Winter wheat -> Mellow buff`
    - `Mellow buff -> Pink sand`
    - `Pink sand -> Chamomile`
    - `Tender peach -> Curds & whey`
    - `Almond cream -> Double cream`
  - repeated ochre and olive failures include:
    - `Doe -> Golden fleece`
    - `Buff -> Fenugreek`
    - `Desert dust -> Sandstorm`
    - `Ecru olive -> Bronze mist`
    - `Amberglow -> Tawny olive`
    - `Tawny olive -> Ceylon yellow`
- long-run eval discipline now says:
  - keep one active sampler in the repo at a time
  - keep judgment on that one live queue until the run is closed
  - land the branch only after that queue reaches `0` pending
- the eval surface now also has one local cohort alias:
  - `warm` = `brown`, `red`, `orange`, `yellow`
- the special brown finding now has its own tracked note:
  - [Finding 1: Contextual Brown](./FINDING_1_CONTEXTUAL_BROWN.md)
- the old off-main first red correction is no longer the active question by
  itself:
  - its fresh rerun at `id > 15325` was recovered onto
    `codex/bigbrain/red-family-recovery`
  - the recovery branch judged far enough into that queue to expose a durable
    repeat fail pattern:
    - peach and pink shoulder drift
    - low-chroma brown and wine seam
  - once that pattern was clearly repetitive, the branch stopped treating the
    old pending rows as the active lane:
    - `2372` total rows in the recovered slice
    - `843` pass
    - `477` fail
    - `1052` rows archived locally as pre-fix pending evidence
    - `0` pending rows left in the active DB after archive
  - the archived pre-fix pending residue is now frozen locally at:
    - `.local/parked/2026-05-13-red-pre-second-correction-pending.tsv`
    - `.local/parked/2026-05-13-red-pre-second-correction-pending.sql`
    - `.local/parked/2026-05-13-red-pre-second-correction-summary.md`
  - that archived evidence then drove the second red correction now drafted on
    the recovery branch:
    - broader pink-peach demotion from `red` to `pink`
    - broader low-chroma brown and wine demotion from `red` to `brown`
    - stable soft-red lane and darker core kept in `red`

## Next Clean Lane

Current clean lane:

- keep the current `red` proof surface on `main` until the next narrow
  correction is explicit
- one active eval sampler at a time
- use the fully judged third corrected `red` rerun as the active proof surface
- keep older eval lanes quarantined locally instead of leaving them in the live
  DB
- the live DB now holds only the closed third corrected rerun at `id > 18423`
- keep the next correction local until it has its own fresh rerun
- `yellow` still stays queued behind `red`

The next meaningful runtime lane should prove:

- whether a narrow warm-clay and peach shoulder escape out of `red` removes the
  remaining repeat failures
- whether the coherent muted-red local pass cluster stays intact in `red`
- whether `yellow` still stays queued behind `red` once that next corrected
  rerun is closed

Current closed proof surface:

- third corrected `red` rerun at `id > 18423`
  - `1268` total rows
  - `1162` pass
  - `106` fail
  - `0` pending
  - `129` pair-level `pass`
  - `13` pair-level `fail`
- older eval rows are now quarantined locally:
  - cutoff: `id <= 18423`
  - `17371` rows frozen locally
  - `.local/parked/2026-05-13-old-evals-pre-third-rerun-quarantine.tsv`
  - `.local/parked/2026-05-13-old-evals-pre-third-rerun-quarantine.sql`
  - `.local/parked/2026-05-13-old-evals-pre-third-rerun-summary.md`
- dominant remaining fail pairs:
  - `Desert rose -> Burnt brick`
  - `Garnet rose -> Desert rose`
  - `Slate rose -> Crabapple`
  - `Auburn -> Tawny orange`
  - `Terra cotta -> Burnt henna`
  - `Oxblood red -> Withered rose`
  - `Peony -> Marsala`
  - `Burlwood -> Mellow rose`
  - `Renaissance rose -> Impatiens pink`

Until the next rerun closes cleanly, keep the public repo truthful to this
landed state and treat the next correction lane plus its quarantined and
archived red evidence as local-only work.

That first evidence lane should stay binary:

- `pass`
- `fail`

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. treat the fully judged third corrected rerun at `id > 18423` as the only
   active proof surface
2. keep the coherent muted-red local pass cluster in `red`
3. cut a narrow warm-clay and peach-shoulder escape out of `red`
4. rerun `red` again from a fresh boundary on the recovery branch
5. only then decide whether `red` is closed or still needs another pass
6. then decide whether `yellow` stays next

## Probaboracle And Scorey Context

Huemiliator belongs to the same toy line, but its progression is different:

- `probaboracle`: closed prompt surface to reasoned generation
- `scorey`: closed prompt surface to deterministic routing plus reasoned
  fragments
- `huemiliator`: open colour selection to deterministic resolution plus
  deterministic transform
