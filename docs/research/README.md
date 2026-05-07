# Research

Huemiliator keeps the tracked research lane small on purpose.

The repo is still in pre-beta, but the first runtime slice now exists.

Raw notes and private scratch material stay in the local `docs/peanut/` lane.

## Current Phase

Current phase:

- `pre-beta`
- `deterministic final reply shape`

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

## Next Clean Lane

The next meaningful runtime kernel should prove:

- PASS/FAIL evidence around routing and replacement correctness
- a small local evidence surface for inspecting outputs

That first evidence lane should stay binary:

- `pass`
- `fail`

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. add PASS/FAIL evaluation for routing and transform correctness
2. add a small local evidence surface for storing and inspecting outputs

## Probaboracle And Scorey Context

Huemiliator belongs to the same toy line, but its progression is different:

- `probaboracle`: closed prompt surface to reasoned generation
- `scorey`: closed prompt surface to deterministic routing plus reasoned
  fragments
- `huemiliator`: open colour selection to deterministic resolution plus
  deterministic transform
