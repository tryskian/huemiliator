# Decisions Log

This file is the durable archive of Huemiliator's engineering, runtime, and
repo-surface decisions.

## How To Use This File

- Need the current durable rules:
  - start with `docs/governance/CHARTER.md`
- Need the current system shape:
  - use `docs/runtime/ARCHITECTURE.md`
- Need the current checkpoint:
  - use `docs/governance/SESSION_HANDOFF.md`
- Need the reasoning behind a repo choice:
  - use this file

Keep entries short, but informative enough to show what changed and why.

## Taxonomy

- `runtime_engineering`
- `eval_quality`
- `collaboration_method`
- `workflow_environment`

## Provenance Rule

Each decision should read as one of these:

- `human-led method decision`
  - the theory, bridge logic, or eval meaning came from the human lead
- `repo formalization`
  - the repo later encoded an already-active method or contract
- `implementation decision`
  - the engineering layer chose mechanics after the method was already set

If a decision crosses layers, say so plainly instead of flattening the method
into implementation authorship.

## D-001: Start from the current Scorey baseline

- Date: `2026-05-05`
- Category: `runtime_engineering`
- Tags: `scorey_lineage`, `baseline`, `house_architecture`
- Provenance: `human-led method decision`
- Decision:
  - start Huemiliator from the current Scorey house architecture
  - do not reconstruct the toy outward from Probaboracle directly
- Why: Huemiliator inherits the current narrow toy architecture from Scorey,
  even though its input contract and runtime logic are different.

## D-002: The archived `margaret2/pantone-colors` source is primary

- Date: `2026-05-05`
- Category: `runtime_engineering`
- Tags: `swatch_reference`, `pantone_secondary`, `deterministic_matching`
- Provenance: `human-led method decision`
- Decision:
  - use the archived
    [`margaret2/pantone-colors`](https://github.com/margaret2/pantone-colors)
    repo, surfaced publicly at
    [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/),
    as the primary swatch reference for colour names and hex codes
  - keep Pantone as a secondary naming layer, not the root truth source
  - layer Huemiliator's own structure on top:
    - family assignment
    - within-family rank
    - deterministic one-up rule
- Why: The toy needs a specific, grounded swatch reference first, then a
  narrower runtime rule set that turns that reference surface into one-up
  behaviour. The source choice itself came from the human lead before the repo
  later froze it locally.

## D-003: V1 input is picker-first

- Date: `2026-05-05`
- Category: `runtime_engineering`
- Tags: `picker_input`, `hex_state`, `constrained_input`
- Provenance: `human-led method decision`
- Decision:
  - use a native UI colour picker as the primary v1 input
  - treat the picker hex as the canonical user input state
  - keep freeform text out of the v1 runtime lane
- Why: Huemiliator is a constrained colour toy, not a chat surface or loose
  design utility. The picker choice itself came from the human lead before the
  repo later formalized it as the live macOS runtime surface.

## D-004: Runtime owns colour resolution

- Date: `2026-05-05`
- Category: `runtime_engineering`
- Tags: `runtime_owned`, `family_mapping`, `one_up_rules`, `generation_boundary`
- Provenance: `human-led method decision with implementation decision`
- Decision:
  - keep matching, family assignment, and one-up selection runtime-owned
  - make that layer PASS/FAIL-testable
  - if generation is used later, keep it out of the final colour decision
- Why: The stable colour decision path needs to stay deterministic and
  evalable, with generation limited to any unstable residue around the final
  line.

## D-005: Repo initialization is docs-first

- Date: `2026-05-05`
- Category: `workflow_environment`
- Tags: `docs_first`, `scaffold`, `honest_surface`
- Provenance: `repo formalization`
- Decision:
  - start the repo as an honest docs-first scaffold:
    - git repo initialized
    - docs spine created
    - package skeleton created
    - no fake runtime surface before code exists
- Why: The repo should state the current truth clearly instead of pretending the
  runtime already exists.

## D-006: The repo stays public during contract lock

- Date: `2026-05-05`
- Category: `workflow_environment`
- Tags: `public_repo`, `contract_lock`, `honest_docs`
- Provenance: `human-led method decision`
- Decision:
  - keep Huemiliator public before runtime implementation
  - keep the tracked docs honest about scaffold state
  - avoid machine-specific local details in the public repo surface
- Why: The public repo is part of the toy surface during contract lock, so the
  docs need to be truthful and legible before the runtime lands.

## D-007: Protected main and Codex working branches

- Date: `2026-05-05`
- Category: `workflow_environment`
- Tags: `branch_protection`, `pr_flow`, `codex_branches`
- Provenance: `repo formalization`
- Decision:
  - protect `main` with the toy-family ruleset shape:
    - PR required
    - squash is the only allowed merge method
    - no force pushes
    - no branch deletion
  - do tracked work on `codex/bigbrain/...` branches and land it through PRs
- Why: Huemiliator should inherit the same small but deliberate repo hygiene as
  the sibling toys.

## D-008: Apache 2.0 is part of the tracked public surface

- Date: `2026-05-05`
- Category: `workflow_environment`
- Tags: `license`, `apache_2_0`, `public_surface`
- Provenance: `repo formalization`
- Decision:
  - keep the Apache 2.0 license surface aligned across:
    - the root `LICENSE` file
    - the README license section
    - SPDX-style package metadata
- Why: The license is part of the public repo contract, not an afterthought.

## D-009: README should not advertise a runtime that does not exist

- Date: `2026-05-05`
- Category: `workflow_environment`
- Tags: `readme`, `truthful_surface`, `runtime_readiness`
- Provenance: `human-led method decision`
- Decision:
  - do not add a `Run It` section until Huemiliator has a real runtime surface
  - keep the top-level docs truthful about current scaffold state
- Why: The README should describe the current repo honestly instead of implying
  product readiness that the toy has not earned yet.

## D-010: Reuse the current Scorey workflow automation surface

- Date: `2026-05-05`
- Category: `workflow_environment`
- Tags: `github_actions`, `dependabot`, `stale_prs`, `scorey_lineage`
- Provenance: `implementation decision`
- Decision:
  - inherit the current Scorey GitHub automation shape during scaffold stage
  - keep the tracked automation surface to:
    - CI on push and pull request
    - weekly Dependabot for pip and GitHub Actions
  - scheduled stale cleanup for dependency PRs
- Why: Huemiliator does not need a repo-specific CI invention while the runtime
  contract is still being locked.

## D-011: The official OpenAI Python SDK is part of the scaffold contract

- Date: `2026-05-06`
- Category: `runtime_engineering`
- Tags: `openai_sdk`, `dependency_pin`, `scaffold_contract`
- Provenance: `implementation decision`
- Decision:
  - pin the official `openai` Python SDK directly in `pyproject.toml`
  - treat that pin as part of the scaffold contract for the future runtime
  - do not let the SDK arrive later as an implicit or transitive dependency
- Why: Huemiliator does not have a live runtime yet, but the repo already knows
  the future one-up surface will use the official OpenAI Python SDK. Making
  that dependency explicit now keeps the package scaffold honest without
  pretending the runtime is already implemented.

## D-012: The first live runtime slice is a macOS native picker

- Date: `2026-05-06`
- Category: `runtime_engineering`
- Tags: `macos_local`, `native_picker`, `canonical_hex`, `first_kernel`
- Provenance: `repo formalization`
- Decision:
  - keep the first live runtime surface macOS-local
  - expose `huemiliator pick` as the first runnable command
  - invoke the native picker through `osascript`
  - print the selected hex as the canonical user state
  - defer swatch resolution and one-up logic to later kernels
- Why: The toy is a small local lab surface, not a cross-platform product. The
  native picker is the cleanest root-first way to honor the earlier human-led
  picker choice without inventing extra UI or premature portability layers.

## D-013: Enforce shell-safe PR body creation via file input

- Date: `2026-05-06`
- Category: `workflow_environment`
- Tags: `github`, `pr_workflow`, `shell_safety`, `quoting`
- Provenance: `repo formalization`
- Decision:
  - use `gh pr create --body-file <path>` as the default path for multiline PR
    descriptions
  - avoid inline `--body "..."` strings when content includes Markdown
    backticks or shell-sensitive characters
  - allow quoted heredoc as fallback when a body file is not practical
- Why: This keeps PR metadata deterministic and prevents shell substitution from
  mangling code spans such as ``huemiliator pick``.

## D-014: Freeze the archived swatch reference into a local snapshot

- Date: `2026-05-06`
- Category: `runtime_engineering`
- Tags: `swatch_snapshot`, `archived_source`, `repo_local_data`, `provenance`
- Provenance: `repo formalization`
- Decision:
  - freeze the archived
    [`margaret2/pantone-colors`](https://github.com/margaret2/pantone-colors)
    source, surfaced at
    [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/),
    into a tracked local dataset at `data/margaret2_swatches.json`
  - preserve source order, source slug, name, and hex from the HTML rows
  - record source metadata in the snapshot itself:
    - source URL
    - snapshot date
    - archived read-only upstream status
  - keep family and rank as Huemiliator-owned layers above the frozen snapshot
- Why: The runtime should be honest about using the archived public source while
  remaining deterministic and repo-local at execution time. The source choice
  itself was already human-led; this kernel only formalized it into repo-local
  data.

## D-015: Resolve nearest swatches with a fixed distance rule

- Date: `2026-05-06`
- Category: `runtime_engineering`
- Tags: `nearest_swatch`, `delta_e_cie76`, `source_order`, `deterministic_resolution`
- Provenance: `implementation decision`
- Decision:
  - normalize runtime hex input to lowercase canonical `#rrggbb` before matching
  - resolve the nearest swatch against `data/margaret2_swatches.json`
  - use `delta-e cie76` as the fixed colour-distance rule
  - break equal-distance ties by the preserved source order from the frozen snapshot
  - expose `huemiliator resolve <hex>` as the narrow verification surface
    for this kernel
- Why: The runtime needs one explicit nearest-swatch rule before family routing
  or one-up logic can be built on top. The frozen snapshot already preserves
  source order, and the reference contains at least one duplicate hex, so the
  tie-break must be fixed instead of improvised.

## D-016: The first family taxonomy and rank ladder are fixed runtime rules

- Date: `2026-05-06`
- Category: `runtime_engineering`
- Tags: `family_taxonomy`, `same_family_rank`, `neutral_family`, `deterministic_routing`
- Provenance: `implementation decision`
- Decision:
  - classify every matched swatch into one closed Huemiliator family set:
    - `neutral`
    - `brown`
    - `red`
    - `orange`
    - `yellow`
    - `green`
    - `blue`
    - `purple`
    - `pink`
  - derive that family from fixed runtime thresholds:
    - Lab chroma threshold for `neutral`
    - hue thresholds for chromatic families
    - a low-lightness warm lane for `brown`
  - assign a same-family rank across the frozen snapshot:
    - chromatic families rank by ascending Lab chroma strength
    - `neutral` ranks by ascending distance from mid-lightness
    - preserved source order breaks equal-strength ties
  - expose the family and family rank through `huemiliator resolve <hex>`
- Why: Huemiliator needs a closed, explicit family surface before the one-up
  kernel can choose a replacement shade. Fixing both the family taxonomy and
  the family rank ladder now keeps the future transform lane deterministic and
  PASS/FAIL-testable.

## D-017: The first one-up step is next-rank, same-family, and non-wrapping

- Date: `2026-05-07`
- Category: `runtime_engineering`
- Tags: `one_up_selection`, `replacement_shade`, `top_rank_clamp`, `deterministic_transform`
- Provenance: `implementation decision`
- Decision:
  - expose `huemiliator replace <hex>` as the first replacement-shade surface
  - resolve the input to the nearest swatch, family, and family rank first
  - choose the next higher rank inside the same family as the replacement step
  - clamp at the top family rank instead of wrapping or improvising
  - leave the short loss line out of this kernel
- Why: Huemiliator needed a real deterministic replacement path before any
  language layer. Using one fixed next-rank step keeps the transform easy to
  test and preserves the same-family contract without adding arbitrary jumps.
