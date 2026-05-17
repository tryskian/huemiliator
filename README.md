# Huemiliator

[![Research Stage](https://img.shields.io/badge/research_stage-pre--Beta%201.0%20fail--pressure%20pulse-E15759)](./docs/research/README.md)
[![Polinko toy factory](https://img.shields.io/badge/polinko_toy_factory-active-4C956C)](https://github.com/tryskian/polinko)

## pick a colour. huey's is better

Huemiliator is a small, local, agent-backed CLI mini chatbot using the
**[Polinko research model](https://github.com/tryskian/polinko)**.

It is a colour one-up spinoff of
**[Probaboracle](https://github.com/tryskian/probaboracle)**. The surface stays
tiny: one native macOS colour picker in, one deterministic same-family shade
out. Instead of oracle drift or rigged rounds, Huemiliator turns that narrow
shape into a colour seam instrument.

The surface stays narrow:

- one native macOS colour picker
- one canonical hex code
- one deterministic same-family replacement shade
- one short loss line

That narrow surface is the point. Huemiliator is not trying to be a general
colour utility. It studies whether deterministic colour matching, family
routing, and one-up logic can stay legible under tight runtime rules.

Current staged research lane:

- `pre-Beta 1.0`
- `fail-pressure pulse`

Current closed comparison surface:

- closed third corrected `red` rerun
- row-level family proof surface

In this repo, a new beta gets pinned when the method change alters what the
evidence means, not just when wording or procedure gets tidier. Pre-beta
staging notes can hold the next method boundary before the first real evidence
run starts.

`Beta 1.0` does not begin until the first real fail-pressure pulse run starts.

## What This Repo Demonstrates

- picker-first input instead of freeform text
- deterministic swatch matching against a frozen local reference
- runtime-owned family assignment, same-family rank, and one-up selection
- the current row-level family proof surface as a closed comparison baseline
- the staged fail-pressure pulse boundary for the next non-OCR eval unit
- a small local evidence surface for following deterministic output and pulse
  evidence

## Run It

```sh
make install
huemiliator pick
```

`huemiliator pick` opens the native macOS colour picker and prints the chosen
hex.

For the direct runtime path:

```sh
huemiliator resolve <hex>
huemiliator one-up <hex>
```

The operator commands, eval workflow, and setup checks live in the
[runtime runbook](./docs/runtime/RUNBOOK.md). The compact day-open/day-close
sheet lives in [Start / End Reference](./docs/runtime/START_END_REFERENCE.md).

Core operator commands:

```sh
make start
make end
make caffeinate-status
make decaffeinate
make check
```

Closeout rule:

- when the goal is to end the day, run `make end`
- `make end-preflight` is only for an explicitly requested branch-local
  preflight and does not close the loop
- `make end-git-check` is the final gate inside `make end`, not the normal
  operator entrypoint

## Read Next

- [docs/research/README.md](./docs/research/README.md)
  - proof surface and active research notes
- [docs/governance/DECISIONS.md](./docs/governance/DECISIONS.md)
  - durable runtime and eval decisions

## License

Apache-2.0. See [LICENSE](./LICENSE).

---

*Huemiliator is not a resource for colour theory, collaboration, or grey areas.*
