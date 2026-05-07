# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with picker kernel, frozen swatch snapshot, and nearest
  swatch resolution
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Resolve picker hex against the frozen swatch snapshot and leave family routing next.

Done in this kernel:

- ignored local `.vscode/` editor noise from the tracked repo surface
- added the nearest-swatch resolver against the frozen local snapshot
- fixed the resolution rule to `delta-e cie76`
- preserved source order as the tie-break for equal-distance matches
- exposed `huemiliator resolve <hex>` as the verification surface for this kernel
- added runtime tests for normalization, distance, and tie-break behavior
- synced tracked docs and diagram to the new resolution truth

## Current Contract

- platform: macOS local only
- input: native colour picker
- canonical user state: hex code
- inventory: swatch reference from
  [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
  frozen locally at `data/margaret2_swatches.json`, with Pantone as a
  secondary naming layer
- swatch resolution: nearest frozen swatch match by `delta-e cie76` with
  source-order tie-break
- Huemiliator-owned structure:
  - family assignment
  - within-family rank
  - deterministic same-family one-up
- current output target:
  - replacement shade
  - one short loss line

## Next Kernel

- define the first family taxonomy
- define the first one-up ranking rule inside each family
- connect nearest swatch results to family-preserving replacement shade selection

## Stop State

- `main` is clean and protected
- public repo is live
- license surface is in place
- GitHub automation surface is in place
- first picker kernel is in place
- archived swatch snapshot is in place
- nearest swatch resolution is in place
- next work should start from a fresh `codex/bigbrain/...` branch
