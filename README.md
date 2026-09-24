# Huemiliator

[![Research Stage](https://img.shields.io/badge/research_stage-behaviour_pulses_active-E15759)](./docs/research/030_PB_BEHAVIOUR.md)
[![Polinko Model](https://img.shields.io/badge/polinko_model-staged_next_beta-4C956C)](https://github.com/tryskian/polinko)
[![Polinko toy factory](https://img.shields.io/badge/polinko_toy_factory-active-4C956C)](https://github.com/tryskian/polinko)
![Model Refactor](https://img.shields.io/badge/model_refactor-active-F28E2B)

## pick a colour. huey's is better

> [!NOTE]
> **Current status:** The first current-app behaviour pulse completed under
> [D-064](./docs/governance/DECISIONS.md#d-064-authorize-live-per-response-judging-for-the-first-current-app-pulse):
> HUE-4's primary assistant recorded 9 live judgements, 4 `PASS` and 5 `FAIL`,
> with one mechanical failure on olive's printed hexes and no request errors.
> It ran for 857.587 seconds; all six inputs ran once and the first three
> repeated before the dispatch guard stopped the run. This is a bounded evidence
> result, not a beta promotion or aggregate behaviour verdict.
> The [sequential feedback connection](./docs/research/350_PULSE_FEEDBACK.md) is now
> implemented and checked offline. Useful recorded observations can shape the
> following pulse while Hugh's compact brief and colour foundation stay fixed.
> Current reading path: [session handoff](./docs/governance/SESSION_HANDOFF.md)
> → [current behaviour method](./docs/research/030_PB_BEHAVIOUR.md)
> → [composer](./docs/runtime/COMPOSITION.md) → [behaviour records](./docs/runtime/BEHAVIOUR_RECORDS.md) / [review notebook](./output/jupyter-notebook/huemiliator-behaviour-review.ipynb)
> → [behaviour pulse diagram](./docs/diagrams/BEHAVIOUR_PULSE.md).
>
> Colour logic is the stable foundation. The agent setup uses
> approximately five short, positive directions with room for Huey to reason.
> The [supplied authorial prompt](./docs/research/340_HUGH_PROMPT.md)
> provides five character points, with sentence construction left to Hugh.
> The bank-free composer uses the existing deterministic colour facts;
> [D-063](./docs/governance/DECISIONS.md#d-063-leave-response-construction-to-hugh)
> records the template removal and golden cases' evaluation role.
> Start each session with the [compact handoff](./docs/governance/SESSION_HANDOFF.md):
> current setup, eval method, roles, open choices and next step. It links the
> [beta notes](./docs/research/030_PB_BEHAVIOUR.md) and
> [current diagram](./docs/diagrams/BEHAVIOUR_PULSE.md) for supporting detail.

Huemiliator is a small, local, agent-backed CLI mini chatbot using the
**[Polinko research model](https://github.com/tryskian/polinko)**.

It is a colour one-up spinoff of
**[Probaboracle](https://github.com/tryskian/probaboracle)**. The surface stays
tiny: one native macOS colour picker in, one deterministic same-family shade
out. Instead of oracle drift or rigged rounds, Huemiliator turns that narrow
shape into a colour seam instrument.

## Meet Hugh

His name is **Hugh (Hue)**. We call him **Huey** affectionately. He doesn't
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
- one response grounded in that replacement

That narrow surface is the point. Huemiliator is not trying to be a general
colour utility. It studies whether deterministic colour matching, family
routing, and one-up logic can stay legible under tight runtime rules.

Current research direction:

- review the completed bounded 15-minute pulse and its attributed primary
  judgements; any further pulse or method promotion requires separate alignment
- compact positive instructions with room for Huey to reason
- bank-free composition from character direction and grounded colour facts
- historical closed `Beta 1.0` colour evidence carried as the baseline

Historical colour proof surface:

- broader corrected `neutral` continuation at `20106..20120`
- warm-edge `orange` yellow-gold audit pulse at `20121..20128`
- warm-edge `yellow` green / olive audit pulse at `20129..20139`
- warm-edge `orange` pale straw / buff / blush audit pulse at `20140..20145`
- warm-edge `yellow` residual chartreuse audit pulse at `20146..20150`
- warm-neutral peach / pearl audit pulse at `20151..20153`
- colour-boundary audit pulses at `20154..20158`, `20159..20162`, and
  `20163..20166`
- pulse-level proof surface

Historical row-level comparison surface:

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
- the current behaviour pulse records and its attributed primary judgments
- historical colour proof surfaces and the closed row-level comparison baseline
- the historical fail-pressure pulse boundary for the non-OCR colour eval unit
- a small local evidence surface for following deterministic output and pulse
  evidence

## Run It

```sh
make install
huemiliator pick
```

`huemiliator pick` opens the native macOS colour picker and prints the chosen
hex.

Inspect the colour engine and its legacy fixed line:

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

Compose Hugh's response with the model configured by `HUEMILIATOR_MODEL`:

```sh
huemiliator compose '#d9a6a1' --dry-run
huemiliator compose '#d9a6a1' --format json
```

The [composer guide](./docs/runtime/COMPOSITION.md) covers Luna with medium
reasoning, medium verbosity and Top P `0.98`, request inspection, visible response,
and recording of mechanical failures. The [earlier bank](./docs/runtime/LANGUAGE_BANK.md)
remains historical evidence.
The [behaviour review notebook](./output/jupyter-notebook/huemiliator-behaviour-review.ipynb)
shows saved swatches, responses and attributed judgments from the local
[behaviour database](./docs/runtime/BEHAVIOUR_RECORDS.md).
The live colour DB remains empty after the [verified archive](./docs/research/330_EVAL_ARCHIVE.md);
preserved colour rows remain in the archived colour DB. The live behaviour DB
contains current pulse outputs `7..15` and their attributed primary judgments;
historical behaviour outputs `1..6` remain in the archived behaviour DB.

Closeout rule:

- when the goal is to end the day, run `make end`
- `make end-preflight` is only for an explicitly requested branch-local
  preflight and does not close the loop
- `make end` only closes when:
  - current-truth docs are fresh
  - local validation passes
  - colour eval `pending` is `0`; review current behaviour completion through
    [Behaviour Records](./docs/runtime/BEHAVIOUR_RECORDS.md)
  - the repo is back on clean synced `main`
- `make end-git-check` is the final gate inside `make end`, not the normal
  operator entrypoint

## Read Next

- [Pre-Beta: 15-Minute Behaviour Pulses](./docs/research/030_PB_BEHAVIOUR.md)
  - current method, completed pulse, judgment lens and next research step
- [docs/research/README.md](./docs/research/README.md)
  - proof surface and research notes
- [docs/governance/DECISIONS.md](./docs/governance/DECISIONS.md)
  - durable runtime and eval decisions

## Licence

Apache-2.0. See [LICENSE](./LICENSE).

---

*Huemiliator is not a resource for colour theory, collaboration, or grey areas.*
