# Huemiliator

[![Research Phase](https://img.shields.io/badge/research_phase-contract%20lock-E15759)](./docs/research/README.md)
[![Polinko toy factory](https://img.shields.io/badge/polinko_toy_factory-active-4C956C)](https://github.com/tryskian/polinko)

## pick a colour. hue's is better.

Huemiliator is a small, local colour toy using the **[Polinko research model](https://github.com/tryskian/polinko)**.

It is a colour one-up spinoff of **[Probaboracle](https://github.com/tryskian/probaboracle)** built from the current **[Scorey](https://github.com/tryskian/scorey)** baseline. It inherits the same narrow toy architecture, but its runtime contract is different:

- user picks a colour through a native colour picker
- the runtime receives a hex code
- the runtime resolves that hex to the nearest Pantone entry
- the runtime stays in the same family
- the runtime picks a deterministic one-up colour
- hue outputs the replacement shade and one short loss line

Current state:

- public repo live
- protected `main` plus PR flow in place
- docs spine in place
- package scaffold in place
- runtime not yet implemented

## What This Repo Will Demonstrate

- closed picker input instead of freeform prompt text
- deterministic catalogue resolution against a fixed Pantone inventory
- runtime-owned family mapping and one-up rules
- binary PASS/FAIL evaluation of matching, routing, and output

## Run It

```sh
make install
huemiliator
```

Right now the command reports the current contract and scaffold state.

## Read Next

- [docs/governance/CHARTER.md](./docs/governance/CHARTER.md)
- [docs/runtime/ARCHITECTURE.md](./docs/runtime/ARCHITECTURE.md)
- [docs/research/README.md](./docs/research/README.md)

## License

Apache-2.0. See [LICENSE](./LICENSE).

---

*Huemiliator is not a resource for colour theory, collaboration, or grey areas.*
