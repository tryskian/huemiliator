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
- Why: Huemiliator is a constrained colour mini chatbot, not a loose design
  utility. The picker choice itself came from the human lead before the repo
  later formalized it as the live macOS runtime surface.

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

## D-018: The first loss-line layer is a fixed family bank

- Date: `2026-05-07`
- Category: `runtime_engineering`
- Tags: `loss_line`, `fixed_bank`, `family_keyed`, `final_output_shape`
- Provenance: `implementation decision`
- Decision:
  - expose `huemiliator one-up <hex>` as the first full reply surface
  - keep `replace` as the lower-level deterministic replacement inspection lane
  - emit one short fixed line from a family-keyed bank after the replacement
    shade
  - keep the line layer deterministic and model-free
  - keep the line layer downstream of the colour decision
- Why: Huemiliator needed a final reply surface without weakening the runtime
  contract. A tiny fixed family bank preserves the short snark layer while
  keeping the colour choice fully separable and PASS/FAIL-testable.

## D-019: The first local evidence lane is SQLite plus one experiment notebook

- Date: `2026-05-07`
- Category: `eval_quality`
- Tags: `sqlite`, `local_evidence`, `notebook`, `follow_along`
- Provenance: `human-led method decision with repo formalization`
- Decision:
  - keep the first local evidence surface in a repo-local SQLite file at
    `.local/evals.sqlite`
  - expose a narrow operator surface for that lane:
    - `huemiliator eval-init`
    - `huemiliator eval-log <hex>`
    - `huemiliator eval-list --limit <n>`
  - record the deterministic output state after the colour decision:
    - input hex
    - nearest swatch
    - family and rank
    - replacement shade and rank
    - loss line
  - keep the first follow-along notebook at
    `output/jupyter-notebook/huemiliator-eval-surface.ipynb`
- Why: Huemiliator now has enough deterministic runtime surface to inspect real
  outputs. A tiny SQLite lane plus one notebook keeps that evidence local,
  legible, and downstream of the colour decision without bloating the toy into
  a larger eval system.

## D-020: The first PASS/FAIL lane is human judgment on stored rows

- Date: `2026-05-07`
- Category: `eval_quality`
- Tags: `pass_fail`, `human_judgment`, `sqlite`, `pending_review`
- Provenance: `human-led method decision with repo formalization`
- Decision:
  - keep the first PASS/FAIL surface human-owned
  - apply verdicts directly to stored eval rows:
    - `pass`
    - `fail`
  - expose that lane through:
    - `huemiliator eval-list --verdict <state>`
    - `huemiliator eval-judge <id> <pass|fail> --note "<note>"`
  - keep verdict notes short and row-local
- Why: Huemiliator already has deterministic output storage, so the smallest
  honest next step is human review on those rows. That gives the repo a real
  binary eval lane without jumping early into a larger judging system.

## D-021: Brown should catch dark earthy warms before the neutral gate

- Date: `2026-05-07`
- Category: `runtime_engineering`
- Tags: `brown_boundary`, `earthy_warms`, `neutral_shoulder`, `family_routing`
- Provenance: `implementation decision`
- Decision:
  - tighten the brown lane before the neutral chroma gate
  - widen brown slightly toward darker earthy warms by:
    - lowering the brown hue floor
    - allowing a darker warm override before the neutral check
    - allowing slightly lighter warm browns when their chroma is already strong
  - keep pale creams, parchment shades, and warm low-chroma neutrals out of
    brown
- Why: The evidence lane showed that the weak spot was not the whole
  beige-parchment shoulder. It was darker earthy warms collapsing into
  `neutral` or staying `orange` even when the colour read more like brown.
  Tightening that boundary is a smaller and cleaner correction than trying to
  reclassify all warm neutrals.

## D-022: Long-run local evals sample the frozen snapshot in source order

- Date: `2026-05-07`
- Category: `eval_quality`
- Tags: `long_run`, `local_sampler`, `source_order`, `consistency`
- Provenance: `human-led method decision with implementation decision`
- Decision:
  - expose `huemiliator eval-sample-local` as the long-run local sampler
  - cycle deterministically through the frozen swatch snapshot in source order
  - default the sampler to human-judgable pacing with a `3` second interval
  - use small runs as smoke checks only
  - treat long-run consistency as the real evidence surface
- Why: Huey does not need clever spot samples. The signal comes from sustained,
  consistent accumulation of deterministic rows that can be judged while the
  queue is still growing.

## D-023: Long runs can isolate one family without changing the sampler method

- Date: `2026-05-07`
- Category: `eval_quality`
- Tags: `family_runs`, `brown_lane`, `sampler_scope`, `source_order`
- Provenance: `implementation decision`
- Decision:
  - keep `huemiliator eval-sample-local` as the one long-run entrypoint
  - allow `--family <name>` to restrict the run to one Huemiliator family
  - preserve source order inside that family subset instead of inventing a new
    family-specific sampling method
- Why: Once the eval runner existed, the next useful move was to isolate
  pressure on one family without creating a parallel runner design. The family
  filter keeps the method stable while focusing the evidence lane.

## D-024: The review lane can filter to one family too

- Date: `2026-05-07`
- Category: `eval_quality`
- Tags: `family_filter`, `review_lane`, `brown_lane`, `pending_queue`
- Provenance: `implementation decision`
- Decision:
  - allow `huemiliator eval-list --family <name>` in the human review lane
  - apply the family filter to both the row list and the printed summary counts
  - keep the family filter composable with `--verdict`
- Why: Once family-specific runs became a real method surface, the review lane
  also needed a matching filter so the queue could be judged without mixing in
  unrelated families.

## D-025: Human judgment starts while the long run is still filling

- Date: `2026-05-07`
- Category: `eval_quality`
- Tags: `live_review`, `long_run`, `judgment_method`, `queue_discipline`
- Provenance: `human-led method decision with repo formalization`
- Decision:
  - start human PASS/FAIL review while the long-run sampler is still active
  - do not wait for the run to finish before judging rows
  - keep review on the active lane:
    - use `--verdict pending` for the open queue
    - add `--family <name>` when the run is family-isolated
- Why: In Huemiliator, the data itself is the signal. Small spot samples are
  only smoke checks. The real method is long-run accumulation plus live human
  judgment against the growing queue, so drift can be seen and tightened while
  the evidence is still arriving.

## D-026: Brown rank should demote the yellow and gold shoulder

- Date: `2026-05-08`
- Category: `runtime_engineering`
- Tags: `brown_rank`, `replacement_drift`, `gold_shoulder`, `olive_shoulder`
- Provenance: `implementation decision`
- Decision:
  - keep the brown family on its own rank rule instead of the generic chroma
    ladder
  - demote the yellow, gold, and olive shoulder below the earthy brown core
  - treat bright high-chroma warm shoulders as lower brown rank even when their
    chroma is strong
- Why: The first judged brown run showed a narrow but repeated failure cluster:
  replacements such as `Spectra yellow`, `Antique gold`, `Spruce yellow`,
  `Ecru olive`, `Tapenade`, `Tinsel`, and `Boa` were being treated as better
  browns than the earthy core. A brown-specific rank rule is a smaller and
  cleaner fix than widening family labels or adding special-case replacement
  exceptions.

## D-027: Bright gold shoulder should exit brown at classification time

- Date: `2026-05-08`
- Category: `runtime_engineering`
- Tags: `brown_classification`, `gold_shoulder`, `family_routing`, `orange_boundary`
- Provenance: `implementation decision`
- Decision:
  - route the bright gold and ochre shoulder out of `brown` during family
    classification
  - let those colours fall through to `orange` or `yellow` instead of relying
    on brown ranking to contain them
  - keep the brown ladder focused on the earthy core plus the narrower muted
    olive seam that still needs pressure
- Why: After `D-026`, the early brown rerun improved, but the louder gold
  shoulder still did not belong in the brown lane at all. Classification is a
  cleaner place to remove obvious gold cases than asking the brown rank rule to
  absorb them downstream.

## D-028: Family correctness comes before another brown rank tweak

- Date: `2026-05-08`
- Category: `runtime_engineering`
- Tags: `brown_classifier`, `family_correctness`, `orange_shoulder`, `olive_seam`
- Provenance: `implementation decision`
- Decision:
  - apply the next brown correction at classification time instead of stacking
    another brown-rank exception
  - evict two shoulder shapes upstream before they enter the brown ladder:
    - bright warm orange-yellow shoulder colours
    - the muted olive seam that was still being treated as brown
  - keep the earthy brown core untouched while making that cut
- Why: Once the completed brown rerun was fully judged, the queue stopped
  looking like one vague brown problem. The closed `201` pair signal showed two
  repeat seams, and the conservative classifier cut removed `55` unique fail
  pairs from the brown lane while evicting `0` unique pass pairs. That made
  family-correctness cleanup the root-first move.

## D-029: Keep one active eval sampler per repo

- Date: `2026-05-08`
- Category: `eval_quality`
- Tags: `single_run`, `queue_discipline`, `attribution`, `long_run`
- Provenance: `human-led method decision with repo formalization`
- Decision:
  - keep exactly one live eval sampler active in the repo at a time
  - do not overlap family runs or general runs in the same checkout
  - finish or stop the current run before starting the next long-run lane
- Why: The data is the signal only when the queue stays attributable to one
  active run. Overlapping samplers split judgment attention, muddy attribution,
  and weaken the value of long-run evidence.

## D-030: Warm is a local eval cohort alias

- Date: `2026-05-08`
- Category: `eval_quality`
- Tags: `warm_scope`, `local_cohort`, `sampler_scope`, `review_lane`
- Provenance: `human-led method decision with repo formalization`
- Decision:
  - keep `--family <name>` as the one sampler and review flag
  - allow `warm` as a local eval cohort alias on that flag
  - define `warm` as:
    - `brown`
    - `red`
    - `orange`
    - `yellow`
  - let `warm` work in both:
    - `huemiliator eval-sample-local`
    - `huemiliator eval-list`
- Why: The next evidence lane needs one extended warm run, but `warm` is not a
  runtime family. A local cohort alias keeps the eval surface narrow, reuses
  the same sampler and review lane, and avoids inventing a second runner or
  API-owned scope.

## D-031: Fail is evidence and evict is the runtime correction

- Date: `2026-05-08`
- Category: `eval_quality`
- Tags: `fail_vs_evict`, `boundary_fix`, `queue_discipline`, `routing_errors`
- Provenance: `implementation decision`
- Decision:
  - treat `fail` as evidence that the current routing or replacement lane is
    wrong
  - treat `evict` as the upstream classifier or boundary correction made
    because of that evidence
  - do not leave known routing mistakes in the queue forever once they have
    earned an eviction fix
- Why: PASS/FAIL should expose where the current behavior is wrong, not become
  a permanent holding pen for rows that no longer belong in the active lane. The
  cleaner move is to let the queue prove the mistake, then move the fix into
  runtime classification or scope.

## D-032: Land eval branches only after the queue is cleared

- Date: `2026-05-09`
- Category: `eval_quality`
- Tags: `closeout`, `pending_queue`, `landing_rule`, `queue_discipline`
- Provenance: `human-led method decision with repo formalization`
- Decision:
  - keep live judgment active while a run is still filling
  - do not land the branch with open eval pendings from that run
  - before merge or end-of-day packaging, clear the active run to:
    - `0` pending
    - closed PASS/FAIL signal
- Why: A live run benefits from overlap between accumulation and judgment, but a
  landed branch should not freeze the evidence surface in a half-judged state.
  Clearing the pending queue before landing keeps each run attributable,
  interpretable, and genuinely closed.

## D-033: Real eval runs are family-by-family

- Date: `2026-05-09`
- Category: `eval_quality`
- Tags: `family_runs`, `warm_audit`, `single_lane`, `closeout`
- Provenance: `human-led method decision with repo formalization`
- Decision:
  - run real eval lanes one family at a time
  - use cross-family scopes like `warm` only as audit surfaces
  - choose the next family run from the closed signal of the prior run instead
    of widening by default
- Why: Huemiliator learns most cleanly from one attributable colour lane at a
  time. The `warm` cohort was useful as a cross-family audit, but the durable
  method is still hue-by-hue evaluation with one closed family signal before
  moving to the next.

## D-034: Orange shoulder seams should leave the orange lane before rerun

- Date: `2026-05-09`
- Category: `eval_quality`
- Tags: `orange_family`, `family_first`, `warm_neutral_shoulder`, `olive_shoulder`
- Provenance: `implementation decision`
- Decision:
  - keep the next `orange` correction family-first instead of rank-first
  - demote pale low-chroma warm shoulder colours out of `orange` and back into
    `neutral`
  - demote the darker muted olive shoulder out of `orange` and into `yellow`
  - keep the stronger orange core in-lane
  - treat the closed warm audit as the proof surface for that cut:
    - `68` unique orange fail pairs evicted
    - `0` unique orange pass pairs evicted
- Why: The closed warm audit showed that orange was not failing as one noisy
  family. It was failing through two attributable shoulders: a pale warm
  neutral seam and a darker muted olive seam. A conservative family-first cut
  removes those known bad shoulders before the next orange-only rerun without
  sacrificing already-judged orange core pairs.

## D-035: Low-chroma beige and taupe shoulders should also leave orange

- Date: `2026-05-09`
- Category: `eval_quality`
- Tags: `orange_family`, `beige_seam`, `taupe_seam`, `family_first`
- Provenance: `implementation decision`
- Decision:
  - keep the second orange correction family-first instead of rank-first
  - demote the darker taupe shoulder out of `orange` and into `neutral`
  - demote the soft beige and cream shoulder out of `orange` and into
    `neutral`
  - keep the judged orange core in-lane
  - treat the closed orange rerun as the proof surface for that cut:
    - `19` unique orange fail pairs evicted
    - `0` unique orange pass pairs evicted
- Why: The first orange rerun no longer failed through a broad warm shoulder.
  It narrowed into a beige, latte, and cream seam with a smaller muted olive
  carry-through. A second conservative shoulder cut removes the low-chroma
  beige and taupe lane without sacrificing any judged orange-core pairs.

## D-036: Dependency review and Python audit are part of the scaffold baseline

- Date: `2026-05-12`
- Category: `workflow_environment`
- Tags: `github_actions`, `dependabot`, `dependency_review`, `security_gates`
- Provenance: `implementation decision`
- Decision:
  - keep the default-branch required checks to:
    - `markdownlint`
    - `test`
    - `dependency-review`
    - `python-security`
  - keep Dependabot version updates active for:
    - `github-actions`
    - `pip`
  - retire the earlier dependency-PR stale cleanup shape in favor of direct
    review and audit gates
- Why: Huemiliator is still scaffold-light, but its repo-security posture
  should match the current toy-family baseline: explicit review of dependency
  diffs plus a first-class Python audit, without reviving the stale-queue
  automation that the sibling repos already dropped.

## D-037: Keep the tracked eval notebook aligned to the canonical repo env

- Date: `2026-05-13`
- Category: `workflow_environment`
- Tags: `notebook`, `python_env`, `local_evidence`, `repo_hygiene`
- Provenance: `human-led method decision with implementation decision`
- Decision:
  - treat this notebook/env refresh as human-led:
    - the human lead set the direction for the canonical env shape
    - Codex executed, formalized, and validated the repo-facing update
  - keep the tracked eval notebook metadata aligned to the canonical local repo
    environment
  - when local workspace/editor settings exist, they should resolve through the
    repo `.venv`
  - keep the notebook itself legible as a follow-along local evidence surface,
    not a separate runtime contract
- Why: Huemiliator already had the right runtime shape and repo-local `.venv`
  convention. The remaining drift was surface-level: notebook metadata and
  local editor wiring could lag behind the actual repo env and make the
  evidence lane feel less trustworthy than it really was.
