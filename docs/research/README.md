# Research

Huemiliator keeps the tracked research lane small on purpose.

The repo is still in pre-beta, but the first runtime slice now exists.

Raw notes and private scratch material stay in the local `docs/peanut/` lane.

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
- `brown` is proving to be a good pressure lane because it is a contextual
  colour bucket rather than a clean spectral one:
  - it often behaves more like dark orange, muted orange, or olive-adjacent
    warm neutral than a single stable hue
  - that makes brown-family drift a useful research signal, not just a bug
- the first judged brown run exposed a broad replacement drift cluster:
  - loud `yellow`
  - `gold`
  - `olive`
- the fresh post-fix brown rerun is already narrower at the early judged edge:
  - at last check: `247` new rows, `8` pass, `2` fail, `237` pending
  - the loud yellow/gold shoulder is no longer the main issue
  - the remaining early failures are muted green-edge cases like
    `Beech -> Covert green` and `Capers -> Dusky green`

## Next Clean Lane

Current clean lane:

- `2` hour local source-order runs
- `2` hour one-family runs when a boundary needs isolated pressure
- ongoing judgment while the queue is still filling
- small count-based runs only for smoke checks

The next meaningful runtime kernel should prove:

- whether the revised brown boundary and brown rank now hold up under a fresh
  long-run judged pass
- whether the remaining muted green edge needs its own brown-rank correction
- whether a tighter first gate should split family correctness from shade
  correctness

That first evidence lane should stay binary:

- `pass`
- `fail`

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. continue judging the fresh brown rerun while the queue is still filling
2. inspect whether the revised brown boundary and rank keep holding as the
   judged sample grows
3. decide whether the muted green edge needs its own brown-rank correction
4. decide whether the first human gate should judge family only or full
   replacement correctness

## Probaboracle And Scorey Context

Huemiliator belongs to the same toy line, but its progression is different:

- `probaboracle`: closed prompt surface to reasoned generation
- `scorey`: closed prompt surface to deterministic routing plus reasoned
  fragments
- `huemiliator`: open colour selection to deterministic resolution plus
  deterministic transform
