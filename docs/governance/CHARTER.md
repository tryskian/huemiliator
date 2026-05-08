# Huemiliator Charter

## Mission

Huemiliator is a small, local colour mini chatbot using the
**[Polinko research model](https://github.com/tryskian/polinko)**.

It is a colour one-up spinoff of
**[Probaboracle](https://github.com/tryskian/probaboracle)** built from the
current **[Scorey](https://github.com/tryskian/scorey)** baseline.

It explores constrained human-AI interaction through deterministic colour
resolution, family-preserving one-up rules, and strict binary evaluation.

The toy is rooted in the current Scorey baseline:

- keep the runtime narrow
- move rule ownership into the runtime
- only leave unstable residue to generation

## Durable Rules

Runtime:

- local-first
- support the live runtime surface on macOS only
- start from the Scorey house architecture
- keep the active input surface narrow
- use the native UI colour picker as the primary v1 input
- treat the picker hex as the canonical input state
- keep swatch matching deterministic against the locked archived
  `margaret2/pantone-colors` source
- keep nearest-swatch resolution on one fixed distance rule
- keep tie-breaks deterministic
- keep the first family taxonomy explicit and closed
- keep same-family rank on one fixed strength ladder
- keep the first one-up step to one non-wrapping same-family rank move
- keep the first loss-line layer fixed-bank and downstream of the colour decision
- keep family mapping and one-up selection runtime-owned
- do not add patchwork layers around a weak root contract

Prompt surface:

- one native macOS colour picker
- one visible hex readout
- no freeform text lane in v1

Responses:

- short
- dry
- belittling without becoming sprawling
- the final colour decision should be runtime-owned
- if generation is used later, it should only own the unstable line residue

Eval:

- binary verdicts only
- `pass`
- `fail`
- treat `fail` as evidence about the current lane
- treat `evict` as the runtime correction that removes a bad lane upstream
- do not keep re-judging known routing mistakes once they have earned eviction
- one eval focus at a time
- prove matching and same-family one-up before broadening into tone
- treat small evals as smoke checks only
- treat long-run consistency as the real evidence surface
- keep local eval storage under `.local/`
- keep the follow-along notebook under `output/jupyter-notebook/`
- keep the first human judgment lane narrow and row-based

Project posture:

- keep it small
- keep it local-first
- keep the live surface macOS-local
- keep it aligned with Polinko's eval discipline
- keep the public repo surface honest during contract lock
- keep `main` protected
- do tracked work on `codex/bigbrain/...` branches
- root-first changes only
- no patchwork runtime
- no verbose docs

## Working Model

Human lead owns:

- objective
- scope boundaries
- acceptance criteria
- theory-level interpretation
- go or no-go decisions

Engineer owns:

- implementation
- validation
- runtime hygiene
- docs upkeep
- execution recommendations

Default execution model:

- one active kernel at a time
- visible checkpoints
- brief, kernel, merge
- tracked changes land by squash PR into `main`
- docs stay in sync with real state

## Documentation Ownership

| Doc | Job |
| --- | --- |
| `README.md` | public framing and current entrypoint |
| `docs/governance/DECISIONS.md` | durable runtime and eval choices |
| `docs/governance/SESSION_HANDOFF.md` | current checkpoint and next kernel |
| `docs/runtime/ARCHITECTURE.md` | stable system shape |
| `docs/runtime/RUNBOOK.md` | operator procedure and validation |
| `docs/research/README.md` | current research framing |
| `docs/diagrams/PIPELINE.md` | canonical colour resolution and one-up flow |

After runtime, product-shape, or research-method changes, sweep the tracked
docs before calling the state settled.

## Scope

In scope:

- local runtime
- native UI colour picker input
- deterministic swatch matching from the locked reference source
- repo-local family taxonomy
- deterministic same-family one-up rules
- small local SQLite evidence storage
- a follow-along experiment notebook
- binary human judgment
- tracked diagrams and docs

Out of scope:

- freeform text input in v1
- general chat
- design-tool positioning
- arbitrary colour suggestion
- deployment scaffolding

## Security And Ops

- the tracked repo is public during contract lock
- the Apache 2.0 license surface should stay aligned across `LICENSE`,
  `README.md`, and package metadata
- no live credentials are required for the current scaffold
- the current live runtime slice does not require credentials
- future runtime credentials should load from the repo `.env`
- local execution is the trusted development boundary
- local eval data should live under `.local/`
