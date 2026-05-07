# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with picker kernel and frozen swatch snapshot
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Freeze the archived swatch source cleanly and leave resolution next.

Done in this kernel:

- renamed the config surface to a truthful swatch snapshot path
- added parser and loader support for the archived `margaret2` source
- froze the archived swatch page into `data/margaret2_swatches.json`
- preserved source order, slug, name, and hex in the local snapshot
- added runtime tests against the real frozen reference
- synced tracked docs and diagram to the new snapshot truth

## Current Contract

- platform: macOS local only
- input: native colour picker
- canonical user state: hex code
- inventory: swatch reference from
  [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
  frozen locally at `data/margaret2_swatches.json`, with Pantone as a
  secondary naming layer
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
- connect picked hex to nearest swatch resolution

## Stop State

- `main` is clean and protected
- public repo is live
- license surface is in place
- GitHub automation surface is in place
- first picker kernel is in place
- archived swatch snapshot is in place
- next work should start from a fresh `codex/bigbrain/...` branch
