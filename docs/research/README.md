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
- the current brown-family correction is now classifier-first:
  - muted green and olive shoulders can leave `brown` before ranking
  - high-chroma gold and yellow-orange shoulders can leave `brown` before
    ranking
  - light apricot-orange shoulders can leave `brown` before ranking
  - darker earthy browns still stay in `brown`
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
- the current correction uses that fully judged closed brown rerun as its
  evidence base:
  - `201` unique brown pairs
  - `117` pass
  - `84` fail
  - the dominant residual seams were muted green and olive misroutes plus the
    orange, yellow, and gold shoulder
- fresh in-progress queues after the classifier cuts show the corrected
  shoulders leaving `brown`; the current remaining pressure is smaller and
  centers on a low-chroma neutral-gray edge rather than the earlier
  green/gold/orange shoulders
- the special brown finding now has its own tracked note:
  - [Finding 1: Contextual Brown](./FINDING_1_CONTEXTUAL_BROWN.md)

## Next Clean Lane

Current clean lane:

- continue the current fresh brown-family queue after the classifier cuts
- `2` hour one-family runs when a boundary needs isolated pressure
- live judgment while the queue is still filling for future long runs
- small count-based runs only for smoke checks

The next meaningful runtime kernel should prove:

- whether the low-chroma neutral-gray edge is a real brown-family failure or an
  acceptable dark earthy edge
- whether the current classifier cuts stay stable through a full fresh
  brown-family run

That first evidence lane should stay binary:

- `pass`
- `fail`

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. finish judging the fresh post-correction brown queue
2. decide whether the low-chroma neutral-gray edge needs a family-boundary trim
3. only update the classifier again if the fresh run shows a repeated family
   correctness seam

## Probaboracle And Scorey Context

Huemiliator belongs to the same toy line, but its progression is different:

- `probaboracle`: closed prompt surface to reasoned generation
- `scorey`: closed prompt surface to deterministic routing plus reasoned
  fragments
- `huemiliator`: open colour selection to deterministic resolution plus
  deterministic transform
