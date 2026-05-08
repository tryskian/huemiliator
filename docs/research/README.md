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
- the residual brown-family correction is now live:
  - muted olive and khaki shoulders are excluded before the dark earthy brown
    shortcut
  - loud orange, yellow, and gold shoulders are excluded before brown ranking
  - the active brown source subset drops from `202` swatches to `125` swatches
    in the local snapshot
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
  - `45` were judged `pass`
  - `28` were judged `fail`
  - `2295` remain unjudged in the local queue
  - the earthy brown core now holds much better than it did in the first run
  - the main residual failure shape is still the muted green and olive seam:
    - `Beech -> Covert green`
    - `Capers -> Dusky green`
    - `Black ink -> Grape leaf`
    - `Covert green -> Aloe`
  - a smaller orange shoulder still leaks through at the tail:
    - `Orange popsicle -> Orange tiger`
    - `Persimmon orange -> Puffin's bill`
    - `Autumn glory -> Turmeric`
- the special brown finding now has its own tracked note:
  - [Finding 1: Contextual Brown](./FINDING_1_CONTEXTUAL_BROWN.md)

## Next Clean Lane

Current clean lane:

- judgment sweeps over the completed post-classification brown queue
- `2` hour local source-order runs
- `2` hour one-family runs when a boundary needs isolated pressure
- live judgment while the queue is still filling for future long runs
- small count-based runs only for smoke checks

The next meaningful runtime kernel should prove:

- whether the stricter brown boundary preserved the earthy brown core across a
  fresh two-hour judged run
- whether the remaining named gold/ochre cases inside `brown` are acceptable
  contextual browns or still need a narrower trim
- whether a tighter first gate should split family correctness from shade
  correctness

That first evidence lane should stay binary:

- `pass`
- `fail`

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. keep judging the completed brown rerun in focused sweeps
2. decide whether the next correction should target the muted green seam or the
   smaller residual orange shoulder
3. decide whether the first human gate should judge family only or full
   replacement correctness

## Probaboracle And Scorey Context

Huemiliator belongs to the same toy line, but its progression is different:

- `probaboracle`: closed prompt surface to reasoned generation
- `scorey`: closed prompt surface to deterministic routing plus reasoned
  fragments
- `huemiliator`: open colour selection to deterministic resolution plus
  deterministic transform
