# Huemiliator

[![Research Phase](https://img.shields.io/badge/research_phase-contract%20lock-E15759)](./docs/research/README.md)
[![Polinko toy factory](https://img.shields.io/badge/polinko_toy_factory-active-4C956C)](https://github.com/tryskian/polinko)

## pick a colour. hue's is better

Huemiliator is a small, local colour toy using the **[Polinko research model](https://github.com/tryskian/polinko)**.

It is a colour one-up spinoff of
**[Probaboracle](https://github.com/tryskian/probaboracle)** built from the
current **[Scorey](https://github.com/tryskian/scorey)** baseline. It keeps the
same narrow toy-family shape, but turns it into deterministic colour one-upping
instead of oracle or round play:

- user picks a colour through a native colour picker
- the runtime receives a hex code
- the runtime resolves that hex against the swatch reference at
  [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
- Pantone stays a secondary naming layer on top of that reference surface
- the runtime stays in the same family
- the runtime picks a deterministic one-up colour
- hue outputs the replacement shade and one short loss line

Current state:

- public repo live
- protected `main` plus PR flow in place
- GitHub automation in place
- docs spine in place
- package scaffold in place
- runtime not yet implemented

## What This Repo Will Demonstrate

- closed picker input instead of freeform prompt text
- deterministic catalogue resolution against a fixed swatch reference, with
  Pantone as a secondary layer
- runtime-owned family mapping and one-up rules
- binary PASS/FAIL evaluation of matching, routing, and output

## Current Surface

There is no runnable Huemiliator runtime yet. Right now this repo contains the
locked contract, docs spine, and package scaffold for the first implementation
kernel.

## Read Next

- [docs/governance/CHARTER.md](./docs/governance/CHARTER.md)
- [docs/runtime/ARCHITECTURE.md](./docs/runtime/ARCHITECTURE.md)
- [docs/research/README.md](./docs/research/README.md)

## License

Apache-2.0. See [LICENSE](./LICENSE).

---

*Huemiliator is not a resource for colour theory, collaboration, or grey areas.*
