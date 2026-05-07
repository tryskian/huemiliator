# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with picker kernel, frozen swatch snapshot, nearest
  swatch resolution, first family rank layer, first replacement step, and
  first loss-line layer
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Attach a deterministic short loss line after the replacement shade and leave
the local evidence surface next.

Done in this kernel:

- added a dedicated `huemiliator one-up <hex>` final reply surface
- kept `replace` as the lower-level replacement inspection lane
- added a short fixed loss-line bank keyed by family
- kept the line layer downstream of the deterministic colour decision
- added runtime tests for one-up command behavior and loss-line lookup
- synced tracked docs and diagram to the new final reply truth

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
  - deterministic short loss line from a fixed family bank
- current output target:
  - replacement shade
  - one short loss line

## Next Kernel

- add PASS/FAIL evidence around replacement correctness
- set up the small local evidence surface
- keep any future language layer downstream of the colour decision

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
- next work should start from a fresh `codex/bigbrain/...` branch
