# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
  swatch resolution, first family rank layer, and first replacement step
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Select the replacement shade from the ranked family path and leave the loss
line next.

Done in this kernel:

- added a dedicated `huemiliator replace <hex>` runtime surface
- selected the replacement shade as the next higher same-family rank
- clamped the replacement step at the family top rank
- kept `resolve` as the lower-level verification surface
- added runtime tests for one-up selection and replace command behavior
- synced tracked docs and diagram to the new replacement truth

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
  - deterministic same-family replacement by next rank with top-rank clamp
- current output target:
  - replacement shade
  - one short loss line

## Next Kernel

- add the short loss line after the deterministic replacement shade
- add PASS/FAIL evidence around replacement correctness
- keep the language layer downstream of the colour decision

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
- next work should start from a fresh `codex/bigbrain/...` branch
