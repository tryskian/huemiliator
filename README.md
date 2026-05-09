# Huemiliator

[![Research Phase](https://img.shields.io/badge/research_phase-pre%20beta-E15759)](./docs/research/README.md)
[![Polinko toy factory](https://img.shields.io/badge/polinko_toy_factory-active-4C956C)](https://github.com/tryskian/polinko)

## pick a colour. huey's is better

Huemiliator is a small, local, agent-backed CLI mini chatbot using the
**[Polinko research model](https://github.com/tryskian/polinko)**.

It is a colour one-up spinoff of
**[Probaboracle](https://github.com/tryskian/probaboracle)** built from the
current **[Scorey](https://github.com/tryskian/scorey)** baseline. It keeps the
same narrow mini-chatbot family shape, but turns it into deterministic colour
one-upping instead of oracle or round play:

- user picks a colour through a native UI colour picker
- the runtime receives a hex code
- the runtime resolves that hex against the archived
  [`margaret2/pantone-colors`](https://github.com/margaret2/pantone-colors)
  source surfaced at
  [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
- Pantone stays a secondary naming layer on top of that reference surface
- the runtime stays in the same family
- the runtime picks a deterministic one-up colour
- Huey outputs the replacement shade and one short loss line

Current state:

- public repo live
- protected `main` plus PR flow in place
- GitHub automation in place
- docs spine in place
- package scaffold in place
- macOS picker kernel in place
- archived swatch snapshot frozen locally
- nearest swatch resolution in place
- family taxonomy and same-family rank in place
- deterministic replacement shade selection in place
- deterministic short loss line in place
- local SQLite eval DB in place
- human PASS/FAIL judgment lane in place
- long-run local eval sampler in place
- follow-along notebook in place at
  `output/jupyter-notebook/huemiliator-eval-surface.ipynb`

## What This Repo Will Demonstrate

- closed picker input instead of freeform prompt text
- deterministic catalogue resolution against a fixed swatch reference, with
  Pantone as a secondary layer
- runtime-owned family mapping and one-up rules
- binary PASS/FAIL evaluation of matching, routing, and output
- a small local evidence surface for following the deterministic output path

## Current Surface

On macOS, nine runnable Huemiliator runtime and evidence paths now exist:

```sh
huemiliator pick
huemiliator resolve <hex>
huemiliator replace <hex>
huemiliator one-up <hex>
huemiliator eval-init
huemiliator eval-log <hex>
huemiliator eval-list --limit 10
huemiliator eval-judge <id> <pass|fail> --note "<note>"
huemiliator eval-sample-local --duration-seconds 7200
```

`huemiliator pick` opens the native UI colour picker and prints the selected
hex.

`huemiliator resolve <hex>` resolves a hex value to the nearest swatch from the
frozen local snapshot at `data/margaret2_swatches.json`, then prints the
matched family and same-family rank.

`huemiliator replace <hex>` resolves the nearest swatch and emits the
deterministic same-family replacement shade.

`huemiliator one-up <hex>` emits the replacement shade and one short
deterministic loss line from a fixed family bank.

`huemiliator eval-init` creates the local SQLite evidence DB at
`.local/evals.sqlite`.

`huemiliator eval-log <hex>` records the deterministic one-up output fields in
that SQLite DB.

`huemiliator eval-list --limit 10` prints the most recent logged outputs for
quick inspection, with optional verdict and family filtering.

`huemiliator eval-judge <id> <pass|fail> --note "<note>"` applies a human
binary verdict to one logged output and prints the updated row.

`huemiliator eval-sample-local --duration-seconds 7200` runs the local
source-order sampler against the frozen snapshot. Add `--family brown` or
another Huemiliator family name to isolate one family, or use
`--family warm` for the local warm cohort (`brown`, `red`, `orange`,
`yellow`). The default pacing is one row every `3` seconds so the queue can be
judged while it is still filling.

The follow-along notebook lives at
`output/jupyter-notebook/huemiliator-eval-surface.ipynb`.

## Read Next

- [docs/governance/CHARTER.md](./docs/governance/CHARTER.md)
- [docs/runtime/ARCHITECTURE.md](./docs/runtime/ARCHITECTURE.md)
- [docs/research/README.md](./docs/research/README.md)

## License

Apache-2.0. See [LICENSE](./LICENSE).

---

*Huemiliator is not a resource for colour theory, collaboration, or grey areas.*
