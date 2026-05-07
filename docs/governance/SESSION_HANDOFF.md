# Session Handoff

## Current State

- repo: `huemiliator`
- branch: `main`
- status: public repo with first macOS picker kernel
- branch ruleset: active on default branch
- GitHub automation: aligned with Scorey

## Active Kernel

Ship the first live runtime slice cleanly and leave swatch resolution next.

Done in this kernel:

- macOS-only runtime boundary made explicit
- native picker command added at `huemiliator pick`
- native picker output resolved to canonical hex
- picker parsing and cancellation tests added
- tracked docs and diagram synced to the new partial runtime truth

## Current Contract

- platform: macOS local only
- input: native colour picker
- canonical user state: hex code
- inventory: swatch reference from
  [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
  with Pantone as a secondary naming layer
- Huemiliator-owned structure:
  - family assignment
  - within-family rank
  - deterministic same-family one-up
- current output target:
  - replacement shade
  - one short loss line

## Next Kernel

- choose the swatch-reference ingestion format
- define the first family taxonomy
- define the first one-up ranking rule inside each family
- connect picked hex to nearest swatch resolution

## Stop State

- `main` is clean and protected
- public repo is live
- license surface is in place
- GitHub automation surface is in place
- first picker kernel is in place
- next work should start from a fresh `codex/bigbrain/...` branch
