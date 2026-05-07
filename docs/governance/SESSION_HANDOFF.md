# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
  swatch resolution, and first family rank layer
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Classify resolved swatches into fixed families and leave one-up selection next.

Done in this kernel:

- added shared colour-metric helpers for deterministic runtime routing
- fixed the first Huemiliator family taxonomy to a closed family set
- added same-family rank across the frozen snapshot with one fixed strength ladder
- exposed family and family rank through `huemiliator resolve <hex>`
- updated `make doctor-env` to reflect the live runtime truth
- added runtime tests for family routing and same-family rank
- synced tracked docs and diagram to the new family-rank truth

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
  - deterministic same-family one-up
- current output target:
  - replacement shade
  - one short loss line

## Next Kernel

- connect ranked swatches to family-preserving replacement shade selection
- define the first deterministic one-up step inside each family
- add PASS/FAIL evidence around replacement correctness

## Stop State

- `main` is clean and protected
- public repo is live
- license surface is in place
- GitHub automation surface is in place
- first picker kernel is in place
- archived swatch snapshot is in place
- nearest swatch resolution is in place
- first family taxonomy and rank are in place
- next work should start from a fresh `codex/bigbrain/...` branch
