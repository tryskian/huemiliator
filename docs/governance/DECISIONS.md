# Decisions Log

## Taxonomy

- `Category` values:
  - `runtime_engineering`
  - `eval_quality`
  - `collaboration_method`
  - `evidence_governance`
  - `workflow_environment`
- `Tags`:
  - lowercase snake_case labels for quick filtering

## Entry Criteria

Add an entry only when the change is durable and still governs the repo.

Good fits:

- repo workflow rules
- runtime contract changes
- eval contract changes
- evidence handling rules
- documentation governance rules

Keep current-session carryover, wrapper wording churn, stale classifier
history, and branch-local cleanup facts in the handoff or branch history.

## Entry Style

- keep entries short and operational
- one durable decision per entry
- use one category
- use 3 to 5 tags
- keep `Decision` and `Why` tight

## D-001: Local picker runtime remains canonical

- Date: `2026-05-15`
- Category: `runtime_engineering`
- Tags: `local_first`, `macos_picker`, `mini_chatbot`
- Decision: Huemiliator remains a small, local, CLI mini chatbot with a
  macOS-native picker as the canonical input surface.
- Why: This keeps the runtime narrow and keeps the colour one-up loop inside a
  constrained local instrument.

## D-002: The archived swatch snapshot is the primary colour reference

- Date: `2026-05-15`
- Category: `runtime_engineering`
- Tags: `swatch_snapshot`, `primary_reference`, `pantone_secondary`
- Decision: The frozen `margaret2` swatch snapshot remains the primary colour
  reference, with Pantone kept as a secondary naming layer.
- Why: The repo needs one grounded reference surface before any one-up logic or
  naming layer sits on top of it.

## D-003: Swatch matching stays deterministic

- Date: `2026-05-15`
- Category: `runtime_engineering`
- Tags: `deterministic_matching`, `delta_e_cie76`, `source_order`
- Decision: Nearest-swatch matching stays deterministic through fixed
  `delta-e cie76` distance and source-order tie-breaks.
- Why: Stable matching is the root contract for every later family and
  replacement decision.

## D-004: Runtime owns family assignment, rank, and one-up selection

- Date: `2026-05-15`
- Category: `runtime_engineering`
- Tags: `runtime_ownership`, `family_mapping`, `rank_ladder`
- Decision: Runtime owns family assignment, same-family rank, and one-up
  selection.
- Why: The stable colour decision path should stay deterministic and directly
  testable.

## D-005: Replacement stays same-family, next-rank, and non-wrapping

- Date: `2026-05-15`
- Category: `runtime_engineering`
- Tags: `same_family`, `next_rank`, `non_wrapping`
- Decision: The replacement rule remains one same-family step upward by rank,
  clamped at the family top.
- Why: This keeps the one-up move simple, legible, and comparable across
  families.

## D-006: The loss line stays fixed-bank and downstream of the colour decision

- Date: `2026-05-15`
- Category: `runtime_engineering`
- Tags: `loss_line`, `fixed_bank`, `downstream_output`
- Decision: The short loss line remains a fixed-bank output layer that sits
  after the deterministic colour decision.
- Why: This keeps any expressive residue downstream of the stable replacement
  contract.

## D-007: Eval verdicts stay binary

- Date: `2026-05-15`
- Category: `eval_quality`
- Tags: `binary_gate`, `pass_fail`, `verdict_unit`
- Decision: Tracked eval verdicts remain `PASS` or `FAIL`. When the active
  method uses bounded pulses, the pulse carries that binary verdict and rows
  remain evidence inside it.
- Why: This keeps failure pressure real and keeps evidence interpretation
  separate from later implementation work.

## D-008: One active family lane at a time stays the main eval frame

- Date: `2026-05-15`
- Category: `eval_quality`
- Tags: `family_lane`, `pulse_method`, `single_lane`
- Decision: Active eval pressure stays on one family lane at a time. New method
  boundaries, whether row-level or pulse-level, stay attributable to one active
  lane at a time too.
- Why: Huemiliator learns cleanly when lane attribution stays narrow and each
  comparison surface stays small enough to inspect.

## D-009: `warm` stays an audit cohort rather than a runtime family

- Date: `2026-05-15`
- Category: `eval_quality`
- Tags: `warm_audit`, `cohort_alias`, `review_scope`
- Decision: `warm` remains a local audit cohort for `brown`, `red`, `orange`,
  and `yellow`, rather than becoming a runtime family.
- Why: This preserves a useful wider audit surface without widening the runtime
  classification contract.

## D-010: One active sampler and a closed queue are required for lane truth

- Date: `2026-05-15`
- Category: `eval_quality`
- Tags: `single_sampler`, `queue_discipline`, `closed_lane`
- Decision: Keep one active sampler per repo and close the active queue before
  landing tracked work from that lane.
- Why: A lane only stays interpretable when its rows belong to one active run
  and the judgment surface actually closes.

## D-011: Superseded eval rows move to local quarantine

- Date: `2026-05-15`
- Category: `evidence_governance`
- Tags: `quarantine`, `proof_surface`, `local_evidence`
- Decision: Once a newer rerun becomes the active proof surface, older eval
  rows move into local quarantine artifacts and leave the live DB.
- Why: This preserves recovery while keeping the active evidence surface clean.

## D-012: The live DB keeps only the current proof surface

- Date: `2026-05-15`
- Category: `evidence_governance`
- Tags: `live_db`, `current_truth`, `proof_surface`
- Decision: `eval_outputs` holds only the current active proof surface rather
  than mixed historical lanes.
- Why: Live repo truth should point at the current signal, not a pile of
  obsolete runs.

## D-013: `docs/peanut` is the local-only lane

- Date: `2026-05-15`
- Category: `workflow_environment`
- Tags: `local_only`, `private_lane`, `working_notes`
- Decision: `docs/peanut/` remains the local and private working lane.
- Why: This keeps tracked project truth separate from private scratch and field
  material.

## D-014: Clean synced `main` is the tracked stop state

- Date: `2026-05-15`
- Category: `workflow_environment`
- Tags: `protected_main`, `feature_branch`, `stop_state`
- Decision: Tracked truth ends on clean synced `main` through feature
  branches, PR checks, and protected-main merges.
- Why: This keeps local and remote tracked truth aligned.

## D-015: Document roles are explicit and non-overlapping

- Date: `2026-05-15`
- Category: `workflow_environment`
- Tags: `docs_roles`, `non_duplication`, `current_truth`
- Decision: `CHARTER` holds durable rules, `SESSION_HANDOFF` holds active
  carryover, `RUNBOOK` holds procedure, `ARCHITECTURE` holds system shape,
  `START_END_REFERENCE` holds the compact command card, `DECISIONS` holds the
  durable ledger, and tracked research notes explain the current proof surface.
- Why: This keeps the docs stack legible and prevents overlap drift.

## D-016: Startup and closeout are operator procedures backed by atomic commands

- Date: `2026-05-15`
- Category: `workflow_environment`
- Tags: `startup`, `closeout`, `atomic_commands`
- Decision: Startup stays a short mechanical bootstrap plus rehydrate
  contract, and closeout stays a strict docs, validation, wake-lock, and
  clean-main sequence.
- Why: This keeps the discipline in the operator procedure while the command
  surface stays small and honest.

## D-017: Tracked research notes stay compact and visual-forward

- Date: `2026-05-15`
- Category: `evidence_governance`
- Tags: `research_notes`, `compact_notes`, `visual_forward`
- Decision: Tracked research notes stay dated, compact, and visual-forward,
  with one active proof-surface read and only the durable note or next cut.
  Research-note names stay descriptive and topic-first, with lowercase
  snake_case filenames plus a `YYYY-MM-DD` suffix and no numbered note
  scaffolding or generic prefixes.
- Why: The research surface should explain the signal quickly without turning
  into another warehouse.

## D-018: Tracked repo surfaces stay free of local path leaks

- Date: `2026-05-15`
- Category: `workflow_environment`
- Tags: `public_surface`, `path_leaks`, `repo_hygiene`
- Decision: Tracked docs, scripts, and operator surfaces stay free of
  hardcoded local machine paths and editor residue.
- Why: This keeps the public repo surface portable and clean.

## D-019: Scoped eval sampling follows effective runtime routing and true source order

- Date: `2026-05-16`
- Category: `eval_quality`
- Tags: `sampler_truth`, `family_routing`, `source_order`
- Decision: Family-scoped and cohort-scoped eval sampling must use the same
  effective family routing as the active runtime ladder, including frozen
  swatch-edge overrides, and `start_source_order` means the real snapshot
  source-order position rather than a filtered-list offset.
- Why: A scoped proof surface stops being interpretable if the sampler drifts
  from the runtime it claims to test or if source-order targeting changes
  meaning after filtering.

## D-020: Advertised CLI commands must dispatch truthfully

- Date: `2026-05-16`
- Category: `workflow_environment`
- Tags: `cli_surface`, `truthful_commands`, `operator_surface`
- Decision: Every documented or parsed CLI subcommand must either have real
  dispatch behavior or be removed from the surfaced command list.
- Why: Fake affordances on the operator surface waste audit time and weaken the
  repo's small-command contract.

## D-021: Bulk local sampling reuses one prepared runtime view and one write session

- Date: `2026-05-16`
- Category: `runtime_engineering`
- Tags: `sampler_performance`, `rank_cache`, `sqlite_session`
- Decision: Long-run local sampling should reuse one prepared family and rank
  view of the frozen snapshot plus one DB write session for the run instead of
  rebuilding indexes and reopening SQLite on every row.
- Why: The sampler is an evidence tool, so avoidable per-row rebuild churn
  should not sit in the hot path.

## D-022: Audit passes begin from a human-led go decision

- Date: `2026-05-16`
- Category: `collaboration_method`
- Tags: `human_lead`, `audit_trigger`, `scope_control`
- Decision: Repo audits and review passes begin when the human lead explicitly
  calls for an audit, and the engineer then owns the inspection, findings,
  implementation follow-through, and durable documentation updates inside that
  approved scope.
- Why: This keeps audit work aligned with human-owned scope and treats audit
  outputs as part of the documentation process rather than orphaned branch
  residue.

## D-023: Findings are documented during the work, not reconstructed later

- Date: `2026-05-16`
- Category: `collaboration_method`
- Tags: `recordkeeping`, `findings_capture`, `contemporaneous_notes`
- Decision: During active kernels, the engineer records notes, findings, and
  truth-surface changes as they are discovered rather than deferring
  documentation until closeout.
- Why: Delayed reconstruction creates cleanup work, weakens handoffs, and makes
  repo truth harder to trust.

## D-024: Stage fail-pressure pulse as pre-Beta 1.0

- Date: `2026-05-16`
- Category: `eval_quality`
- Tags: `pre_beta`, `pulse_measurement`, `staging_boundary`
- Decision: Treat fail-pressure pulse as a staged pre-`Beta 1.0` method lane
  until the first real pulse run starts. The closed third corrected `red`
  rerun stays the row-level comparison baseline.
- Why: This is a real method transition, but it is not active evidence yet.
  Keeping pulse judgment in pre-beta form preserves the comparison boundary:
  the corrected `red` rerun remains the finished row-level baseline, while
  `Beta 1.0` begins only when pulse evidence exists on the live surface instead
  of only in the staging note.
