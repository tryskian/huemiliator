# Research

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
- long-run eval discipline now says:
  - keep one active sampler in the repo at a time
  - keep judgment on that one live queue until the run is closed
- the eval surface now also has one local cohort alias:
  - `warm` = `brown`, `red`, `orange`, `yellow`
- the special brown finding now has its own tracked note:
  - [Finding 1: Contextual Brown](./FINDING_1_CONTEXTUAL_BROWN.md)

## Next Clean Lane

Current clean lane:

- active warm-cohort run against the new family-first classifier correction
- one active eval sampler at a time
- `2` hour local source-order runs
- `2` hour one-family runs when a boundary needs isolated pressure
- `2` hour warm-cohort runs when the warm shoulder needs one wider lane
- live judgment while the queue is still filling for future long runs
- small count-based runs only for smoke checks

The next meaningful runtime kernel should prove:

- whether the new family-first classifier actually collapses the muted olive
  seam in live brown reruns
- whether the warm orange-yellow shoulder is still loud when the lane widens to
  the `warm` cohort
- whether a tighter first gate should split family correctness from shade
  correctness

That first evidence lane should stay binary:

- `pass`
- `fail`

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. keep the active warm-cohort run as the only live sampler
2. judge the fresh warm queue while it is still filling
3. check whether the closed fail seams still dominate when brown is not
   isolated
4. decide whether the next correction belongs in warm-scope routing or back in
   a narrower family lane

## Probaboracle And Scorey Context

Huemiliator belongs to the same toy line, but its progression is different:

- `probaboracle`: closed prompt surface to reasoned generation
- `scorey`: closed prompt surface to deterministic routing plus reasoned
  fragments
- `huemiliator`: open colour selection to deterministic resolution plus
  deterministic transform
