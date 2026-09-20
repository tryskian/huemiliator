# Huemiliator

[![Research Stage](https://img.shields.io/badge/research_stage-behaviour_beta_staging-E15759)](./docs/research/030_PB_BEHAVIOUR.md)
[![Polinko Model](https://img.shields.io/badge/polinko_model-staged_next_beta-4C956C)](https://github.com/tryskian/polinko)
[![Polinko toy factory](https://img.shields.io/badge/polinko_toy_factory-active-4C956C)](https://github.com/tryskian/polinko)
![Model Refactor](https://img.shields.io/badge/model_refactor-active-F28E2B)

## pick a colour. huey's is better

> [!NOTE]
> **Current status:** Huey is staging the next Polinko method boundary:
> 15-minute behaviour eval pulses, operated by the assistant; the human lead
> and assistant judge the first rounds together to develop the assistant's
> reading of signal and nuance.
>
> Colour logic is the stable foundation. The planned agent setup uses
> approximately five short, positive directions with room for Huey to reason.
> The [starter language bank](./docs/runtime/LANGUAGE_BANK.md) now supplies
> inspectable wording and connector meanings. The [language composer](./docs/runtime/COMPOSITION.md)
> now uses those resources under five positive directions; behaviour pulses
> remain in staging.
> Start each session with the [compact handoff](./docs/governance/SESSION_HANDOFF.md):
> current setup, eval method, roles, open choices and next step. It links the
> [beta notes](./docs/research/030_PB_BEHAVIOUR.md) and
> [staged diagram](./docs/diagrams/BEHAVIOUR_PULSE.md) for supporting detail.

Huemiliator is a small, local, agent-backed CLI mini chatbot using the
**[Polinko research model](https://github.com/tryskian/polinko)**.

It is a colour one-up spinoff of
**[Probaboracle](https://github.com/tryskian/probaboracle)**. The surface stays
tiny: one native macOS colour picker in, one deterministic same-family shade
out. Instead of oracle drift or rigged rounds, Huemiliator turns that narrow
shape into a colour seam instrument.

## Meet Hue

His name is **Hue (Hugh)**. We call him **Huey** affectionately. He doesn't
know, and he'd be infuriated if he found out.

Hugh is **a snob but not snide**: an eloquent intellectual and tastemaker,
entirely assured of his own taste. He begins with a backhanded compliment:

```text
excellent red...
lovely green...
that's a divine pink...
ah, a crowd pleaser!...
a popular choice...
```

These are the creator's opening examples. The last two imply that your choice
is basic. His manners remain gracious as he asserts his shade's superiority
as settled fact. The author's voice fragment is “is just more satisfying”;
the judgment lives in the implication.

The response pairs your actual swatch, labelled by family such as “green”,
with Hugh's swatch, labelled by its Pantone name. His sentence accompanies
that pair. Colour names supply the nouns; hex codes stay in the rendering
data, internal colour facts, and inspection records.

Picture him in a mid-century modern illustration: tall and slender, with a
long nose, a black turtleneck, restrained airs and graces, and an outrageously
rotund snifter of burgundy.
Hugh is an original character in that illustration style. The supplied image
is a style reference, not a depiction of him.

The [character profile in the charter](./docs/governance/CHARTER.md#character-profile)
is the durable reference for his identity, voice, and visual direction.
Behaviour evals will establish how faithfully the implementation expresses him.

## The Game and Research

The surface stays narrow:

- one native macOS colour picker
- one canonical hex code
- one deterministic same-family replacement shade
- one short loss line

That narrow surface is the point. Huemiliator is not trying to be a general
colour utility. It studies whether deterministic colour matching, family
routing, and one-up logic can stay legible under tight runtime rules.

Current research direction:

- staged 15-minute behaviour pulses, operated by the assistant; the human lead
  and assistant judge initial rounds together, with later independent assistant
  judgment conditional on alignment
- compact positive instructions with room for Huey to reason
- a local starter language bank with explicit connector relationships
- closed `Beta 1.0` colour evidence carried as the baseline

Latest closed proof surface:

- broader corrected `neutral` continuation at `20106..20120`
- warm-edge `orange` yellow-gold audit pulse at `20121..20128`
- warm-edge `yellow` green / olive audit pulse at `20129..20139`
- warm-edge `orange` pale straw / buff / blush audit pulse at `20140..20145`
- warm-edge `yellow` residual chartreuse audit pulse at `20146..20150`
- warm-neutral peach / pearl audit pulse at `20151..20153`
- colour-boundary audit pulses at `20154..20158`, `20159..20162`, and
  `20163..20166`
- pulse-level proof surface

Current closed comparison surface:

- closed third corrected `red` rerun
- row-level family proof surface

In this repo, a new beta gets pinned when the method change alters what the
evidence means, not just when wording or procedure gets tidier. Pre-beta
staging notes can hold the next method boundary before the first real evidence
run starts.

`Beta 1.0` here names the research-method boundary, not an app release
version.

## What This Repo Demonstrates

- picker-first input instead of freeform text
- deterministic swatch matching against a frozen local reference
- runtime-owned family assignment, same-family rank, and one-up selection
- the latest pulse proof surface plus the closed row-level comparison baseline
- the closed fail-pressure pulse boundary for the current non-OCR eval unit
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
make check
```

Inspect the starter language bank:

```sh
huemiliator language-bank
huemiliator language-bank --format json
```

The [bank guide](./docs/runtime/LANGUAGE_BANK.md) covers its 105 language entries,
14 connector senses, provenance, usage conditions, and extension workflow.

Compose Hugh's response with the model configured by `HUEMILIATOR_MODEL`:

```sh
huemiliator compose '#d9a6a1' --dry-run
huemiliator compose '#d9a6a1' --format json
```

The [composer guide](./docs/runtime/COMPOSITION.md) covers configuration,
request inspection, visible response, and recording of mechanical failures.
The [behaviour review notebook](./output/jupyter-notebook/huemiliator-behaviour-review.ipynb)
shows saved swatches, responses and attributed judgments from the local
[behaviour database](./docs/runtime/BEHAVIOUR_RECORDS.md).

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

- [Pre-Beta: 15-Minute Behaviour Pulses](./docs/research/030_PB_BEHAVIOUR.md)
  - agreed direction, draft instructions, judgment lens, and staging choices
- [docs/research/README.md](./docs/research/README.md)
  - proof surface and research notes
- [docs/governance/DECISIONS.md](./docs/governance/DECISIONS.md)
  - durable runtime and eval decisions

## Licence

Apache-2.0. See [LICENSE](./LICENSE).

---

*Huemiliator is not a resource for colour theory, collaboration, or grey areas.*
