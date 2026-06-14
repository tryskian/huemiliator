# Huemiliator

[![Research Stage](https://img.shields.io/badge/research_stage-Beta%201.0%20fail--pressure%20pulse-E15759)](./docs/research/README.md)
[![Polinko Model](https://img.shields.io/badge/polinko_model-staged_next_beta-4C956C)](https://github.com/tryskian/polinko)
[![Polinko toy factory](https://img.shields.io/badge/polinko_toy_factory-active-4C956C)](https://github.com/tryskian/polinko)
![Model Refactor](https://img.shields.io/badge/model_refactor-active-F28E2B)

## pick a colour. huey's is better

> [!NOTE]
> **Current status:** The Polinko research model is being staged for the next
> beta.
>
> This is an active refactor window for the model contract, evidence snapshots,
> docs, and supporting tools. Current builds are kept stable while the repo
> surfaces are simplified, tested, and aligned for the next release.

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

Current live research lane:

- `Beta 1.0`
- `fail-pressure pulse`

Current active proof surface:

- broader corrected `neutral` continuation at `20106..20120`
- warm-edge `orange` yellow-gold audit pulse at `20121..20128`
- warm-edge `yellow` green / olive audit pulse at `20129..20139`
- warm-edge `orange` pale straw / buff / blush audit pulse at `20140..20145`
- warm-edge `yellow` residual chartreuse audit pulse at `20146..20150`
- warm-neutral peach / pearl audit pulse at `20151..20153`
- pulse-level proof surface

Current closed comparison surface:

- closed third corrected `red` rerun
- row-level family proof surface

In this repo, a new beta gets pinned when the method change alters what the
evidence means, not just when wording or procedure gets tidier. Pre-beta
staging notes can hold the next method boundary before the first real evidence
run starts.

`Beta 1.0` here names the live research-method boundary, not an app release
version.

## What This Repo Demonstrates

- picker-first input instead of freeform text
- deterministic swatch matching against a frozen local reference
- runtime-owned family assignment, same-family rank, and one-up selection
- the current pulse proof surface plus the closed row-level comparison baseline
- the active fail-pressure pulse boundary for the current non-OCR eval unit
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
make startup-docs-read
make caffeinate-status
make decaffeinate
make check
```

Closeout rule:

- when the goal is to end the day, run `make end`
- `make end-preflight` is only for an explicitly requested branch-local
  preflight and does not close the loop
- `make end` only closes when:
  - current-truth docs are fresh
  - local validation passes
  - eval `pending` is `0`
  - the repo is back on clean synced `main`
- `make end-git-check` is the final gate inside `make end`, not the normal
  operator entrypoint

## Read Next

- [docs/research/README.md](./docs/research/README.md)
  - proof surface and active research notes
- [docs/governance/DECISIONS.md](./docs/governance/DECISIONS.md)
  - durable runtime and eval decisions

## Licence

Apache-2.0. See [LICENSE](./LICENSE).

---

*Huemiliator is not a resource for colour theory, collaboration, or grey areas.*
