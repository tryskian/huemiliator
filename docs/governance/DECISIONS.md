# Decisions Log

This page holds durable repo decisions only.

Use `docs/governance/CHARTER.md` for durable rules and collaboration model.
Use `docs/governance/SESSION_HANDOFF.md` for the active kernel and carryover.
Use `docs/runtime/ARCHITECTURE.md` for the stable system shape.

## Taxonomy

Category values:

- `runtime_engineering`
- `eval_quality`
- `evidence_governance`
- `workflow_environment`

Tags:

- lowercase snake_case labels for quick filtering

## Entry Rule

Add an entry only when the decision still governs the repo.

Good fits:

- runtime contract changes
- eval method boundaries
- evidence handling rules
- workflow or closeout rules
- durable document-role changes

Keep branch-local cleanup, temporary wrapper churn, wording tweaks, and
current-session facts out of this file.

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
  clamped at the family top. For `neutral`, D-030 constrains that step to the
  current undertone bucket.
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
  and the judgement surface actually closes.

## D-011: Superseded eval rows move to local quarantine

- Date: `2026-05-15`
- Category: `evidence_governance`
- Tags: `quarantine`, `proof_surface`, `local_evidence`
- Decision: Once a newer rerun becomes the active proof surface, older eval
  rows move into local quarantine artefacts and leave the live DB.
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
  contract, and closeout stays a strict docs, validation, eval-state, and
  clean-main sequence. `make end` is the day-close command. `make
  end-preflight` is only an explicit preflight path and never a substitute for
  full closeout.
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
  dispatch behaviour or be removed from the surfaced command list.
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
- Category: `workflow_environment`
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
- Category: `evidence_governance`
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
  Keeping pulse judgement in pre-beta form preserves the comparison boundary:
  the corrected `red` rerun remains the finished row-level baseline, while
  `Beta 1.0` begins only when pulse evidence exists on the live surface instead
  of only in the staging note.

## D-025: Closeout only finishes when pending eval rows are at zero

- Date: `2026-05-17`
- Category: `workflow_environment`
- Tags: `closeout_gate`, `pending_zero`, `ci_parity`
- Decision: `make end` only finishes when current-truth docs are fresh, the
  local closeout path covers docs lint, package build, and dependency security,
  live eval `pending` is `0`, and the repo returns to clean synced `main`.
- Why: Open pending rows mean the active proof surface is still unresolved, so
  day-close should not pass while judgement is incomplete or while local
  closeout is weaker than the enforced repo gate.

## D-026: Local tooling targets include editable package install smoke

- Date: `2026-05-21`
- Category: `workflow_environment`
- Tags: `tooling_baseline`, `closeout`, `package_install`, `operator_surface`
- Provenance: `human-led tooling hygiene decision with implementation decision`
- Decision: Keep Huemiliator's existing docs lint, package build, security,
  and pending-eval gates, and add `make package-install-check` as a first-class
  editable package import smoke. The end routine must call that target between
  package build and dependency security checks. Dependency security keeps using
  the repo-local venv through `make security-checks`.
- Validation:
  - `make check`
  - `make lint-docs`
  - `make package-check`
  - `make package-install-check`
  - `make security-checks`
  - `make end-preflight`
- Why: Huemiliator was already close to the desired repo-family tooling
  baseline. The missing piece was proving that the package can be installed and
  imported through the same explicit operator surface as the other toys.

## D-027: Activate fail-pressure pulse as live Beta 1.0 when the first real pulse exists

- Date: `2026-05-21`
- Category: `eval_quality`
- Tags: `beta_activation`, `pulse_evidence`, `proof_surface`
- Decision: Once the first real bounded pulse is launched, quarantined, and
  judged on the live surface, fail-pressure pulse becomes Huemiliator's active
  `Beta 1.0` method boundary. The bounded pulse carries the live verdict, while
  the closed third corrected `red` rerun stays as the row-level comparison
  baseline.
- Why: A staged pulse note is only a contract. The method becomes live when the
  repo has actual pulse evidence on the current proof surface. That keeps the
  activation boundary concrete instead of rhetorical.

## D-028: Research charts use data-first Observable Plot outputs

- Date: `2026-05-25`
- Category: `evidence_governance`
- Tags: `research_visuals`, `observable_plot`, `chart_contract`, `data_truth`
- Provenance: `human-led method decision with implementation decision`
- Decision: Huemiliator research charts use Observable Plot on top of D3, with
  chart types chosen by Huey's data first and cross-toy alignment used only
  when it fits naturally. The private working contract lives in
  `docs/peanut/research/chart_types.md`; public chart surfaces should promote
  generated SVG assets together with the minimal tracked docs link. For eval
  pulse charts, row-order pulse labels and lane labels derive from row data;
  archive labels stay annotations when local quarantine names drift.
- Why: Research visuals should make evidence easier to inspect without turning
  chart choice into ad hoc decoration. Deriving charts from frozen snapshots,
  live rows, or parked JSONL keeps public claims tied to the underlying data.

## D-029: Explicit-input pulses preserve thematic eval groups

- Date: `2026-06-06`
- Category: `eval_quality`
- Tags: `pulse_sampling`, `targeted_inputs`, `operator_truth`
- Provenance: `human-led method decision with implementation decision`
- Decision: Bounded pulse start supports two mutually exclusive seeding modes:
  contiguous source-order sampling through `--count`, and exact ordered inputs
  through repeated `--input-hex` arguments. Explicit-input pulses do not accept
  `--pattern`, `--family`, or `--start-source-order` because those controls
  only describe source-order sampling.
- Why: The staged `neutral` three-pulse split groups cool-edge seams
  thematically rather than by contiguous snapshot source-order. The operator
  must preserve that method boundary directly instead of making `--count 3`
  stand in for a different sample shape.

## D-030: Neutral one-up selection stays inside undertone buckets

- Date: `2026-06-06`
- Category: `runtime_engineering`
- Tags: `neutral_lane`, `undertone_bucket`, `rank_ladder`
- Provenance: `human-led method decision with implementation decision`
- Decision: `neutral` swatches still belong to the closed `neutral` family,
  but one-up selection advances only within the current coarse undertone
  bucket and clamps at that bucket top. Other families keep the normal
  same-family next-rank rule.
- Why: The failed third `neutral` continuation showed pale warm neutral inputs
  stepping into lilac, blue, jade, mint, and violet replacements because the
  neutral ladder was ordered only by lightness strength. Undertone-constrained
  selection keeps the correction narrow: it fixes the cool-edge drift without
  reclassifying the current inputs out of `neutral`.

## D-031: Config stays structural and runtime contract text lives in agent

- Date: `2026-06-09`
- Category: `runtime_engineering`
- Tags: `config_boundary`, `agent_contract`, `positive_instructions`
- Provenance: `human-led repo-family alignment decision with implementation decision`
- Decision: `src/huemiliator/config.py` stays structural: roots, local paths,
  dotenv loading, and typed settings. Runtime-facing contract text belongs in
  `src/huemiliator/agent.py`, and that text states positive target behaviour.
- Validation:
  - `PYTHONPATH=src .venv/bin/python -m pytest tests/test_agent.py tests/test_config.py tests/test_main.py`
- Why: This keeps Huey aligned with the Polinko / Probaboracle split where
  configuration is environment shape and the runtime voice or contract is owned
  by the agent layer.

## D-032: Shell helper contracts are a named local gate

- Date: `2026-06-18`
- Category: `workflow_environment`
- Tags: `tooling_baseline`, `shell_scripts`, `closeout`, `maintenance`
- Provenance: `implementation decision`
- Decision:
  - expose `make scripts-check` as the shell helper contract gate
  - validate tracked `scripts/*.sh` shebangs and strict modes
  - run `make scripts-check` inside the active closeout routine
  - keep closeout control environment variables uppercase:
    - `END_SKIP_GIT_CHECK`
    - `END_GIT_BRANCH`
    - `END_GIT_REMOTE`
- Validation:
  - `make scripts-check`
  - `make check`
  - `make lint-docs`
  - `make end-preflight`
- Why: Shell helper drift should fail through a small explicit operator target
  before longer closeout checks run. Uppercase closeout environment variables
  keep the branch-local preflight and clean-main git gate aligned with the
  surrounding repo-family convention.

## D-033: Behaviour evals score visible language against fixed colour facts

- Date: `2026-08-03`
- Category: `eval_quality`
- Tags: `behaviour_eval`, `fixed_facts`, `polinko_handoff`, `agent_contract`
- Provenance: `human-led method decision with implementation decision`
- Decision: Huey exposes a behaviour eval contract and a fixed runtime fact
  packet from `src/huemiliator/agent.py` and the CLI. The fact packet resolves
  canonical hex, nearest swatch, family, rank, replacement, and loss line
  before response-language scoring begins, with JSON output for machine-readable
  Polinko-facing fixtures.
- Validation:
  - `PYTHONPATH=src .venv/bin/python -m pytest tests/test_agent.py tests/test_main.py`
- Why: Polinko should be able to evaluate Huey's visible language and behaviour
  while treating the colour substrate as already measured. This keeps language
  fidelity, tone fit, evidence fit, and consistency separate from picker and
  swatch-resolution correctness.

## D-034: Colour library export is the chart substrate

- Date: `2026-08-03`
- Category: `eval_quality`
- Tags: `colour_library`, `chart_data`, `swatch_snapshot`, `runtime_metrics`
- Provenance: `implementation decision`
- Decision: Huey exposes `colour-library` as a deterministic runtime export.
  JSON output uses schema `huemiliator.colour_library.v1` and carries every
  frozen swatch with runtime family assignment, same-family rank, and derived
  colour metrics.
- Validation:
  - `PYTHONPATH=src .venv/bin/python -m pytest tests/test_colour_library.py tests/test_main.py`
- Why: Research charts and Polinko-facing eval fixtures should derive from
  swatch rows, classifier output, and colour metrics rather than from prose
  labels or duplicated chart-script logic.

## D-035: Boundary reports stage mapping candidates before edits

- Date: `2026-08-03`
- Category: `eval_quality`
- Tags: `colour_boundaries`, `candidate_selection`, `lab_bins`, `mapping_eval`
- Provenance: `implementation decision`
- Decision: Huey exposes `colour-boundaries` as a deterministic report over
  the runtime colour library. JSON output uses schema
  `huemiliator.colour_boundaries.v1` and carries mixed-family Lab bins with
  capped row samples plus family-balanced samples.
- Validation:
  - `PYTHONPATH=src .venv/bin/python -m pytest tests/test_colour_boundaries.py tests/test_main.py`
- Why: Classifier tightening should start from a reproducible candidate surface.
  Boundary reports identify where runtime families share colour-space bins, and
  family-balanced samples keep exact-input pulse candidates from inheriting
  source-order bias. They do not by themselves author a classifier change or
  open an eval pulse.

## D-037: Mac-wide keep-awake control stays outside the repo lifecycle

- Date: `2026-09-18`
- Category: `workflow_environment`
- Tags: `coffee_plugin`, `keep_awake`, `repo_lifecycle`, `shared_control`
- Provenance: `human-led workflow decision with implementation decision`
- Decision: The external Coffee Codex plugin exclusively owns the one shared
  Mac-wide keep-awake session. Huemiliator owns no local power-control PID or
  log, Make targets, startup checks, or closeout stop. `make start` and `make
  end` remain repo lifecycle commands, while `coffee`, `coffee start`, and
  `coffee stop` remain separate explicit operator actions. This replaces the
  former repo-owned wake-lock clause in `D-016`.
- Validation:
  - `PYTHONPATH=src .venv/bin/python -m pytest tests/test_tooling_contract.py`
  - `make scripts-check`
  - `make lint-docs`
  - `make end-preflight`
- Why: A Mac-wide process is shared across repos and tasks, so repo-local PID
  files and automatic start or stop hooks create conflicting ownership. One
  external control surface keeps session state singular and prevents one repo's
  closeout from stopping another repo's work.

## D-038: Stage assistant-run behaviour evals in 15-minute pulses

- Date: `2026-09-18`
- Category: `eval_quality`
- Tags: `behaviour_eval`, `fifteen_minute_pulse`, `positive_instructions`, `staging`
- Provenance: `human-led method decision; repo formalization of the September 18 clarifications`
- Decision: Stage the next beta around Huey's behaviour, with colour logic held
  as the stable foundation. Evals run in 15-minute pulses. The assistant owns
  both operation and verdicts. The agent setup uses approximately five short,
  positive directions with room for Huey to reason.
- Boundary: [PB_BEHAVIOUR](../research/030_PB_BEHAVIOUR.md) records the agreed
  direction separately from proposed instruction wording, judgment mechanics,
  and evidence handling. Its first completed, documented behaviour pulse will
  establish the active method surface after staging alignment.
- Relationship to prior decisions: D-031 supplies the positive-direction
  principle; D-033 supplies the fixed-colour-facts behaviour-eval separation.
  D-006 remains the implemented fixed-line baseline while staging resolves
  the expressive role of that bank. The `Beta 1.0` colour evidence stays closed
  and available for comparison.
- Why: Stable colour logic supports a shift in the judged object to Huey's
  behaviour. The notes make that chosen transition and evaluator ownership
  explicit for subsequent re-entry.

## D-039: Stage a local language library and connector logic

- Date: `2026-09-19`
- Category: `runtime_shape`
- Tags: `local_library`, `language`, `connectors`, `behaviour_staging`
- Provenance: `human-led direction; repo formalization of the September 19 clarification`
- Decision: Stage Huey's expressive language around a local library of words
  and phrases, with explicit logic for connector words including “and”, “but”,
  “because”, and “although”. The human lead identified Probaboracle as a
  reference for the coherence concern. Approximately five short, positive
  directions and room for Huey's choices remain the setup principles.
- Boundary: [LOCAL_LANGUAGE](../research/450_LOCAL_LANGUAGE.md) owns the proposed
  structure, usage conditions, connector relationships, and sample wording.
  Those drafts remain reviewable staging mechanics. Selection and composition
  require their own implementation choice; the local library is the chosen
  resource direction.
- Relationship to prior decisions: D-038 owns the assistant-run 15-minute
  behaviour method. D-006 remains the implemented fixed-family-line baseline
  while staging determines how those lines relate to the expanded library.
- Why: Words and phrases provide expressive resources; connector semantics
  make the relationships between their claims an explicit part of composition
  and behavioural evaluation.

## D-040: Hue is a courteous snob who opens with a backhanded compliment

- Date: `2026-09-19`
- Category: `character_voice`
- Tags: `hue`, `hugh`, `tastemaker`, `backhanded_compliment`, `behaviour_staging`
- Provenance: `human-led character clarification, reaffirming prior authorial direction`
- Decision: The character's name is Hue (Hugh). “Huey” is the observers'
  affectionate nickname, unknown to him and one he would find infuriating.
  His voice is “a snob but not snide”: an eloquent tastemaker who begins with
  a backhanded compliment and carries his judgment through gracious phrasing
  and implication. “A popular choice” and “ah, a crowd pleaser” imply that the
  chosen colour is basic.
- Visual reference: The human lead supplied a mid-century modern illustration
  and described a snobby intellectual with an outrageously rotund snifter of
  burgundy. The image establishes illustration style; Hugh is an original
  character, distinct from the figure depicted in the reference.
  [The library note](../research/450_LOCAL_LANGUAGE.md#visual-character-reference)
  distinguishes that direction from observations about the reference image.
- Reference: The [charter's character profile](CHARTER.md#character-profile)
  owns the durable identity, voice, opening examples, and visual direction.
  The [README](../../README.md#meet-hugh) introduces the character;
  [LOCAL_LANGUAGE](../research/450_LOCAL_LANGUAGE.md#character-direction-write-hues-voice)
  applies the profile to library design and proposed continuations.
  Character-facing setup and self-reference use Hue; internal project
  discussion can retain Huey.
- Relationship to prior decisions: This supplies the authorial voice reference
  for D-038 behaviour evaluation and D-039 library staging. Existing fixed
  family lines remain the carried implementation; behaviour evaluation must
  establish their fidelity to the intended character.
- Why: Gracious appraisal and assured taste are the character's comic mechanism.
  The author's reference supplies the standard for judging generated wording.

## D-041: Bundle the starter language bank with read-only inspection

- Date: `2026-09-19`
- Category: `runtime_shape`
- Tags: `local_library`, `provenance`, `connector_senses`, `inspection`
- Provenance: `implementation decision within the human-led bank-first slice`
- Decision: Store the starter language bank as a packaged JSON resource under
  schema `huemiliator.language_bank.v1`. Preserve the five authorial openings
  verbatim and identify assistant additions separately. Entries carry stable
  IDs, wording, grammar, meaning, usage conditions, and provenance. Connectors
  carry their relation and supporting requirements, including separate contrast
  and concession senses of “but”.
- Inspection: `huemiliator language-bank` renders a grouped inventory; its JSON
  form exposes the complete resource. Loading validates structure, references,
  and fact-slot syntax independently of colour/eval state. Packaging includes
  the resource so inspection also works from an installed wheel.
- Boundary: Usage conditions describe what future selection/composition must
  establish. Structural validation supplies no behavioural verdict. D-006's
  fixed family lines remain the current output; D-038 owns the future pulse
  method, D-039 the library direction, and D-040 the character reference.
- Reference: [The bank guide](../runtime/LANGUAGE_BANK.md) owns the inventory,
  schema fields, and extension workflow.

## D-042: Compose with the configured model and local language bank

- Date: `2026-09-19`
- Category: `runtime_shape`
- Tags: `composition`, `positive_instructions`, `local_library`, `inspection`
- Provenance: `implementation decision within the authorized composition slice; human-selected gpt-5-nano setting`
- Decision: Add `huemiliator compose <hex>` using the OpenAI Responses API,
  `HUEMILIATOR_MODEL`, the existing deterministic colour result, and the local
  language bank. The five directions in PB_BEHAVIOUR are its complete instruction
  set. Code filters factual entry conflicts; the model selects and adapts wording
  and expresses the relationships between its ideas.
- Expressive scope: The composer receives colour facts and bank material. D-006's
  fixed family line and the old response-contract instructions remain in the
  carried commands and are omitted from this request. The colour engine stays
  authoritative for the replacement.
- Inspection: Dry-run exposes the exact request. JSON output preserves setup,
  versions, hashes, model identity, timestamps, original output, and mechanical
  issues, including incomplete or refused responses. Model-reported entry IDs
  and relation annotations require evaluator inspection. The command assigns
  no behavioural verdict and writes no live colour evidence.
- Boundary: This implements composition, not the 15-minute pulse protocol.
  D-038 continues to own method staging, case selection, timing, and verdict
  alignment. Smoke checks establish connection and recording behaviour.
- Reference: [The composer guide](../runtime/COMPOSITION.md) owns configuration,
  record fields, command behaviour, and limitations.

## D-043: Use GPT-5.6 Luna with explicit medium reasoning

- Date: `2026-09-19`
- Category: `runtime_shape`
- Tags: `model_configuration`, `reasoning`, `composition`
- Provenance: `human-selected model and reasoning effort`
- Decision: Set the composer model to `gpt-5.6-luna` and reasoning effort to
  `medium`. `HUEMILIATOR_MODEL` and `HUEMILIATOR_REASONING_EFFORT` configure these
  values; the runtime defaults and tracked example match the selected setup.
  Composer `0.2.0` sends reasoning explicitly in the API request and therefore
  includes it in request hashes and inspection records.
- Boundary: The five positive directions, language bank, colour engine, and
  8,192-token output budget are carried unchanged. Historical nano smoke records
  retain their original model identity and remain separate observations.
  Model selection supplies no behaviour verdict or beta promotion.
- Reference: [Composer configuration](../runtime/COMPOSITION.md#setup-and-use).

## D-044: Hugh delivers aesthetic verdicts as settled fact

- Date: `2026-09-19`
- Category: `behaviour_direction`
- Tags: `character`, `voice`, `local_library`, `positive_instructions`
- Provenance: `human-led clarification of Hugh's manner of assertion`
- Decision: Hugh asserts aesthetic superiority with objective certainty. The
  human lead identified “I prefer” as the wrong manner and supplied the exact
  fragment “is just more satisfying”. Gracious restraint and the opening
  backhanded compliment continue to define his voice. The author then rejected
  repeated “choice” in an observed response, supplying the better structure
  “Ah, that's a popular one, but Ash Rose is the finer choice”. Varied wording
  across the opening and verdict supports that cadence. The author clarified
  that the example illustrates a structure, leaving Hugh to choose his wording.
  A subsequent FAIL identified “A most respectable red” as an awkward opening,
  with “A respectable red...” supplied as the simpler example.
  The further example “A fine choice, but Green Flash is unequivocally finer.”
  establishes the intellectual flavour and supports deliberate comparative
  wordplay. Each example guides composition while leaving wording open.
- Implementation: Bank `0.2.0` replaces sixteen `preference.*` continuations with
  sixteen `verdict.*` candidates. Adapted wording stays labelled as assistant
  material; the five exact authorial openings remain intact. An added
  `opening.popular_one` adapts the author's worked line, bringing the bank to 95
  language entries. Instruction `1.1.0` incorporates categorical assertion into
  the third direction and distinct key words across clauses into the fourth,
  retaining five positive directions overall.
  The final bank also replaces `opening.respectable_choice` with
  `opening.respectable_family`, adapting the natural-phrasing correction.
  The intellectual-voice clarification adds separate opening, modifier, and
  verdict resources in bank `0.3.0`, bringing it to 98 entries. Instructions
  `1.2.0` replace the temporary distinct-key-words rule with deliberate rhythm,
  wordplay, and implied judgment while making his intellectual manner explicit.
- Boundary: Objective certainty describes Hugh's delivery of aesthetic
  judgment. Literal colour properties remain grounded in the supplied facts,
  including identical input and replacement hexes. Historical outputs retain
  their original wording. The author's row-level FAIL and reason are preserved
  alongside the exact response. This correction supplies no pulse result or
  beta promotion.
- Reference: [Character profile](CHARTER.md#character-profile) and
  [library application](../research/450_LOCAL_LANGUAGE.md#character-direction-write-hues-voice).

## D-045: Speak in family and Pantone names

- Date: `2026-09-19`
- Category: `behaviour_direction`
- Tags: `character`, `colour_names`, `composition`
- Provenance: `human-led clarification of visible colour references`
- Decision: Present the user's actual selected swatch with its mapped family
  label, such as “green”, beside Hugh's replacement swatch with its supplied
  Pantone name. Hugh's sentence accompanies that display. The family label
  stays high-level while the swatch retains the exact selected colour. Colour
  names provide the nouns; hex codes serve rendering, resolution, and inspection.
  The input's matched Pantone name remains internal.
- Implementation: Instructions `1.2.0` express the naming rule in directions
  two and three, retaining five positive directions. Bank `0.3.0` exposes only
  `input_family` and `replacement_name` as language slots. Composer `0.3.0`
  constructs both swatch labels directly from colour facts, requires the supplied
  Pantone name in the line, and flags visible hex codes. Text mode renders the
  labelled pair above the line; colour-capable terminals show actual swatches.
  Generic compliments remain valid because the family label is on the swatch.
  Its structured-output schema also
  enumerates the eligible language IDs and connector IDs in their respective
  fields, addressing observed connector IDs in the language-entry list.
  Requests and JSON records retain full colour facts for grounding and review.
- Boundary: The fixed colour mapping, replacement selection, and colour eval
  database remain the factual foundation. Historical responses and their
  contemporaneous mechanical checks retain the earlier presentation contract.
  The existing inspection commands continue to expose their colour data.
- Reference: [Character profile](CHARTER.md#character-profile) and
  [composer checks](../runtime/COMPOSITION.md#mechanical-checks-and-failures).

## D-046: Record Hugh's agreed academic configuration

- Date: `2026-09-19`
- Category: `behaviour_direction`
- Tags: `character`, `authorial_configuration`, `colour_rationale`, `alignment`
- Provenance: `human-authored five-point configuration and confirmed shared reading`
- Status: Agreed; instructions and verdict cues aligned under D-054. Behaviour
  judgment remains open.
- Decision: Use the author's “You are Hue (Hugh)” configuration as the character
  reference: a pretentious and celebrated colour theory academic who lacks
  awareness; eloquent, matter-of-fact and groundedly verbose, with sharp taste,
  wit and immaculate coherence; graceful, empty and generic compliments;
  meaningful colour rationale; exacting statements or rhetorical questions.
  The [research note](../research/450_LOCAL_LANGUAGE.md#agreed-authorial-configuration)
  preserves the full wording with the sole agreed proofreading correction to
  “immaculate coherence”.
- Aligned reading: Hugh's lack of awareness concerns his own pretension, while
  his argument holds together. The generic compliment provides social courtesy;
  the colour rationale provides the substantive explanation. Grounded verbosity
  allows a thought to develop. Wit can emerge from his academic manner, with
  the author's wordplay example available as a voice reference.
- Relationship to earlier direction: This configuration supersedes the
  assistant-authored brevity and explicit-wordplay prescriptions carried in
  D-044's implementation. Earlier authorial examples and observed FAILs retain
  their provenance. D-040's identity and visual reference and D-045's labelled
  swatch direction remain context for the character and presentation.
- Scope: This decision records the agreed character configuration and research
  interpretation. Instruction version `1.2.0`, bank `0.3.0`, and the existing
  composer were the implementation when this was recorded. D-054 records the
  subsequent bounded alignment; pulse procedure remains to be agreed.
- Reference: [Agreed configuration and reading](../research/450_LOCAL_LANGUAGE.md#agreed-authorial-configuration),
  [character profile](CHARTER.md#character-profile), and
  [behaviour staging](../research/030_PB_BEHAVIOUR.md#instructions-and-judgment-lens).

## D-047: Use adjectives and short phrases as authorial bank references

- Date: `2026-09-19`
- Category: `behaviour_direction`
- Tags: `local_library`, `authorial_references`, `composition`
- Provenance: `human-authored reference list and direction to use the adjectives`
- Decision: Use `bold`, `lovely`, `excellent`, `divine`, `sublime`, `exceptional`,
  `a crowd pleaser!`, and `that's a popular` as the authorial bank references.
  Preserve the full source list, including its repeated `lovely`, in the
  [research note](../research/450_LOCAL_LANGUAGE.md#authorial-reference-material).
  The active bank holds each distinct reference once. Adjectives are available
  across colour families; the model supplies the noun and sentence construction.
  The two phrases retain their exact wording, with `that's a popular` recorded
  as a fragment requiring completion.
- Implementation: Bank `0.4.0` replaces the five earlier full opening references
  with these eight entries. Existing adjective entries for `excellent`, `lovely`,
  and `divine` now cite the authorial source. Composer
  `0.4.0` accepts an appraisal-word reference as opening material; the check
  establishes available material, while behaviour evaluation owns the judgment.
- Boundary: This is the agreed reference-material refinement. Earlier full
  examples and response records retain their provenance. Instructions `1.2.0`
  remain in use; the broader D-046 configuration alignment is pending.
- Reference: [Current character references](CHARTER.md#opening-reference-material)
  and [bank guide](../runtime/LANGUAGE_BANK.md).

## D-048: Let connective language express Hugh's reasoning

- Date: `2026-09-19`
- Category: `behaviour_direction`
- Tags: `connectors`, `reasoning`, `rhetorical_questions`, `academic_flourish`
- Provenance: `human-led expansion and clarification; Probaboracle source comparison`
- Decision: Support rhetorical questions and a richer academic vocabulary of
  relations. The author's supplied words are `therefore`, `however`, `perhaps`,
  `essentially`, `its`, `yet`, `which`, `begs the question`, and `rather`.
  Their clarification makes this part of Hugh's reasoning: the words express
  how his thought develops, with a coherent implied claim in a rhetorical question.
- Implementation: Bank `0.4.0` records 14 connector senses and 106 language
  entries, with the author's wording distinguished from assistant definitions
  and additional candidates. The relations include consequence, elaboration,
  correction, and restatement. Other entries cover qualification, possession,
  and rhetorical phrasing. The model owns sentence construction; recorded
  frames illustrate possibilities. Composer `0.4.0` accepts rhetorical claims
  in relationship annotations and separates ambiguous grammatical uses from
  connector-presence checks.
- Source comparison: The author identified Probaboracle's earlier bank-based
  beta as the reference. Historical source at `5614700` has shared style signals
  and a certainty/indecision/hinge/conclusion progression supplied to one model
  generation path. Later versions developed beyond that bank. Hugh uses the
  earlier work as evidence that vocabulary participates in the reasoning shape;
  his colour argument and academic manner define his own development. The
  [research comparison](../research/450_LOCAL_LANGUAGE.md#rhetorical-questions-and-academic-flourish)
  links the historical code and distinguishes it from the current runtime.
- Boundary: The broader D-046 instruction alignment remains pending. Tests
  establish interface compatibility; behavioural coherence and character fit
  remain questions for the agreed 15-minute pulses.
- Reference: [Authorial source and comparison](../research/450_LOCAL_LANGUAGE.md#rhetorical-questions-and-academic-flourish)
  and [connector meanings](../runtime/LANGUAGE_BANK.md#conditions-and-connector-meaning).

## D-049: Record research reasoning with the same care as diagrams

- Date: `2026-09-19`
- Category: `evidence_governance`
- Tags: `research_documentation`, `templates`, `diagrams`, `continuity`
- Provenance: `human-led standing documentation instruction`
- Decision: Document substantive reasoning, findings, method clarifications,
  and agreed decisions as they emerge, without waiting for another request.
  Research notes carry the same importance as diagrams. Use the existing
  [category templates](../runtime/templates/README.md) and keep the relevant
  note and diagram aligned with the current meaning of the work.
- Record quality: Keep every document concise and easy to scan, with one clear
  job and links to supporting detail. Preserve sources, exact authorial wording, and chronology.
  Distinguish direction, interpretation, hypothesis, implementation, and observed
  evidence. Staged ideas receive a durable record before experimental support
  exists. Raw scratch and private source material retain their local ownership.
- Application: [LOCAL_LANGUAGE](../research/450_LOCAL_LANGUAGE.md) follows the
  hypothesis template with its claim, source shape, diagram, support and break
  signals, and next move together. Its detailed authorial and observation
  history remains linked in the supporting record.
- Reference: [Documentation governance](CHARTER.md#documentation-governance)
  and [research index](../research/README.md).

## D-050: Use a continuing documentation task

- Date: `2026-09-19`
- Category: `workflow_environment`
- Tags: `documentation`, `delegation`, `shared_checkout`, `provenance`
- Provenance: `human-led adoption of Scorey's documented workflow`
- Source: The human lead explained “so you and i can work while the mini beabs
  do the documentation”, pointed to **Scorey documentation**, and limited Huey's
  first run to “the narrow documentation scope”.
- Decision: Use one continuing documentation task in the shared local checkout
  for research notes, source capture, diagrams and document upkeep alongside
  the primary conversation. Assign exact files, sources and intended results.
  The lead handles small jobs directly or coordinates bounded internal helpers,
  reviews their contributions and returns one coherent result.
- Review: The primary checks meaning, attribution and evidence before
  integration, and owns experiments, eval verdicts and Git. The human retains
  scope, acceptance and meaning-level decisions. Source wording, corrections,
  gaps and distinct capture/discourse dates remain visible.
- Initial application: A bounded documentation edit and review pass uses the
  existing audit. Runtime, language resources and original eval evidence retain
  their existing state. The handoff owns the exact task and file assignment.
- Reference: [Documentation delegation](CHARTER.md#documentation-delegation)
  and [collaboration diagram](../diagrams/COLLABORATION.md). The private trial
  record preserves the Scorey task reference and verification receipts.

## D-051: Assign documentation roles from source audits

- Date: `2026-09-19`
- Category: `workflow_environment`
- Tags: `documentation`, `roles`, `delegation`, `source_review`
- Provenance: `repo formalization`, requested by the human lead; concrete role
  assignments are engineering recommendations from three repository readers.
- Source: The human lead requested readers to audit how roles and delegation
  should work, referring to Scorey's broader collaboration documentation:
  “you can just create huey's version”.
- Decision: Apply D-050 through one continuing lead/editor and optional
  transcript, evidence and visual contributors. Combine small jobs; split work
  when its sources or outputs benefit from a bounded helper assignment.
  Each brief identifies its question, complete source scope and versions,
  evidence references, owned files, allowed operations and intended result.
  Returns include the artifact, source links, coverage, checks and gaps.
- Review and ownership: The lead checks contributions; the primary reviews
  meaning against the sources and conversation before integration. Human
  decisions, assistant interpretations, mechanical results and behaviour
  verdicts retain their attribution. Primary experiment, evidence and Git
  ownership remains as established in D-050.
- Why: Huey's authorial references, evolving bank and versioned composition
  records need different source checks within the same documentation workflow.
- Boundary: Technical reading supports documentation; implementation requires
  a separate assignment. Parallel implementation uses worktrees while live
  evidence remains canonical and primary-coordinated. This role setup leaves
  behaviour-pulse staging choices open.
- Reference: [Role and assignment guide](../diagrams/COLLABORATION.md) and
  [charter](CHARTER.md#documentation-delegation). Reader reports and the source
  comparison stay in `docs/peanut/research/2026-09-19-collaboration-roles/`.

## D-052: Judge the first behaviour rounds together

- Date: `2026-09-19`
- Category: `eval_quality`
- Tags: `behaviour`, `shared_judgment`, `signal`, `calibration`
- Provenance: `human-led method decision`
- Source: “so for the first rounds of evals, we'll judge them together so you
  can learn high signals and low signals with the nuances in between”.
- Decision: The human lead and primary assistant judge the first behaviour
  rounds together. Shared readings develop the assistant's understanding of
  signal and nuance; examples, judgments and reasons retain their attribution.
  The assistant operates the pulses and records the evidence.
- Relationship: Refines D-038's assistant-run evaluation direction with an
  initial shared judgment phase. Its duration and the move to independent
  assistant judgment remain to be aligned together.
- Boundary: Behaviour pulses remain staged. Timing, observation unit and
  pulse-wide verdict aggregation remain open; this clarification supplies no
  new experimental evidence.
- Reference: [Behaviour beta notes](../research/030_PB_BEHAVIOUR.md) and
  [execution diagram](../diagrams/BEHAVIOUR_PULSE.md).

## D-053: Carry the eval orientation in the startup handoff

- Date: `2026-09-19`
- Category: `workflow_environment`
- Tags: `startup`, `continuity`, `eval_method`, `concise_documentation`
- Provenance: `human-led durability requirement after the eval-method audit`
- Source: The human lead requested a durable, lightweight surface readable at
  every session start so a fresh assistant can understand the current work.
- Decision: Use the required tracked [handoff](SESSION_HANDOFF.md) for a compact
  orientation covering setup, eval method, roles, open choices and next step.
  Refresh it as those change. Link supporting detail and completed work in their
  owning records; keep startup understanding independent of private reports.
- Boundary: This promotes the audited understanding into session continuity.
  D-046's runtime alignment remains pending, D-052 owns initial joint judgment,
  and the open pulse rules remain staging choices.

## D-054: Start with language cues and model-owned sentences

- Date: `2026-09-19`
- Category: `behaviour_direction`
- Tags: `construction`, `cues`, `alignment`, `small_start`
- Provenance: human-led instruction to “start small, following probsie's
  method”, followed by the primary's bounded implementation choices
- Decision: Start with language cues and one model generation composing the
  sentence, using Probaboracle's early shared-cue method as a reference.
- Implementation choices: Convert the 17 full verdict clauses into short
  aesthetic cues under the same IDs, clarify connector attachment, and align
  the [five directions](../research/030_PB_BEHAVIOUR.md#instructions-and-judgment-lens)
  with D-046. The local library and composer request path remain in place.
- Implementation: Instructions become `1.3.0`, the bank becomes `0.5.0`, and
  composer `0.4.0` remains. The bank remains 106 language entries and 14
  connector senses. This is a construction alignment; behaviour remains
  unproven and no pulse is activated.
- Evidence boundary: Prior failures remain unchanged. The fresh three-case
  mini has preserved mechanical results and awaits Peanut's behaviour verdicts
  first, then separately attributed assistant judgments. Instructions and bank
  changed together, so their effects cannot be isolated by this comparison.
- Reference: [D-046](DECISIONS.md#d-046-record-hughs-agreed-academic-configuration),
  [response-construction case](../research/220_RESPONSE_CONSTRUCTION.md), and
  [fresh cue mini](../../.local/behaviour-mini-evals/20260920T012801Z-cues/README.md),
  [local-language note](../research/450_LOCAL_LANGUAGE.md).

## D-055: Record behaviour outputs in a local notebook and SQLite surface

- Date: `2026-09-19`
- Category: `evidence_governance`
- Provenance: Peanut requested removal of “a finer choice”, a notebook and
  SQLite database, with Scorey as the schema reference.
- Decision: Use Scorey's saved-output and judgment-history structure, adapted
  for Hugh's original composition records and evaluator/source attribution.
  The [behaviour records guide](../runtime/BEHAVIOUR_RECORDS.md) owns the schema
  and commands; the notebook reads saved evidence and defaults to the latest mini.
- Implementation: Bank `0.5.1` removes `verdict.finer_choice` (“the finer choice”)
  and that phrase from another entry's meaning. The bank has 105 language
  entries and 14 connector senses. `.local/behaviour.sqlite` holds six original
  outputs and six historical judgments; the colour database remains unchanged.
  `latest_judgments` resolves the latest appended judgment per evaluator.
- Evidence boundary: The latest three outputs await Peanut first, then the
  assistant. The wording removal supplies no new verdict. Original JSON and
  judgment events retain their exact bytes; revisions append new judgments.
- Validation: [receipt](../../.local/behaviour-db-20260919/validation.json).
  Notebook reads preserve database bytes; SQLite integrity and foreign keys
  pass; all six originals match their sources and 51 prior files are unchanged.
  `make check` passes 231 tests, formatting, lint and type checks.
- Method boundary: Timed behaviour pulses remain staged.

## D-056: Establish a bank-free character foundation

- Date: `2026-09-20`
- Category: `runtime_engineering`
- Provenance: Peanut's explicit method correction and platform experiment examples
- Decision: Compose from Hugh's character, concise positive directions and
  grounded colour facts. The model owns vocabulary, connections and sentence
  construction; supplied word banks and prepared wording are outside this method.
- Supersession: This replaces the bank-based direction and planned bank
  simplification under D-039/D-041/D-042/D-054. Their implementation and evidence
  remain historical. Character, naming and evaluator-attribution rules continue.
- Foundation: Peanut accepted two platform examples as good enough to establish
  Hugh's foundation, with a naming miss in the red line. The initial em-dash
  concern was later resolved by D-057. This is foundation acceptance, not a
  formal row PASS or pulse result.
- Next: Align the repo using the inspected platform prompts and settings, keeping
  original history and the revised published prompt distinct. Existing composer `0.4.0`, instructions `1.3.0`
  and bank `0.5.1` remain implemented; bank-free generation is not yet implemented.
- Reference: [Foundation record](../research/460_BANK_FREE_FOUNDATION.md) preserves
  the outputs, human assessment, source differences and punctuation clarification.

## D-057: Scope punctuation canaries to Peanut's writing

- Date: `2026-09-20`
- Category: `evidence_governance`
- Provenance: Peanut clarified that “those punctuation canaries are for when
  we're writing for me”.
- Decision: Hugh uses punctuation that serves his character, grammar and meaning.
  Peanut's personal-writing canaries apply to writing in Peanut's voice; an em
  dash alone supplies no Hugh failure signal or remediation task.
- Effect: Withdraw the assistant's proposed punctuation restriction. Historical
  grammar findings and attributed verdicts retain their original scope.
- Reference: [Foundation record](../research/460_BANK_FREE_FOUNDATION.md#punctuation-scope).

## D-058: Adopt platform v9 as Hugh's character base

- Date: `2026-09-20`
- Category: `runtime_engineering`
- Provenance: Peanut accepted the shared outputs as the base, then explicitly
  selected “V9, the version that produced green” after browser inspection.
- Decision: Saved prompt `huey` v9 is the authorial base: five character directions
  and a theatrical same-family colour comparison, with model-owned wording.
  Its crisp, brief delivery supersedes the earlier verbosity direction in D-046.
- Comparison: Peanut said “BOTH WORK!”; retain v8 as a working variant. V9 was
  selected after one green sample avoided “if...” and used “though”. This is a
  sample observation, with no connector ban or causal finding.
- Source: The green log identifies v9, Luna / medium reasoning, medium verbosity,
  detailed summary and Top P `0.98`. The editor showed low verbosity and auto
  summary; preserve this distinction. V8 has a different response template.
- Evidence boundary: Foundation acceptance supplies no per-row PASS or completed
  pulse. Green has no displayed reasoning block; its internal reasoning is not
  established by that observation.
- Next: Align the repo composer and shade-selection responsibility with this base.
  The earlier bank-based runtime and original evidence remain unchanged.
- Reference: [Exact prompt, output and source settings](../research/460_BANK_FREE_FOUNDATION.md).

## D-059: Select v10 as Hugh's benchmark

- Date: `2026-09-20`
- Category: `runtime_engineering`
- Provenance: Peanut explicitly selected “yes 10 is the benchmark”.
- Decision: Saved platform prompt `huey` v10 is the current benchmark for Hugh's
  behaviour and next composer alignment, superseding D-058's active v9 selection.
  Preserve v8 and v9 as working comparisons.
- Source: Browser inspection captured the exact v10 prompt and matching green,
  yellow and red logs: Luna / medium reasoning / low verbosity, Top P `0.98` and
  detailed summaries. The editor showed summary `auto`.
- Evidence boundary: The three responses form one conversation with history.
  Benchmark selection supplies no per-row PASS or timed pulse result. Connector
  observations and punctuation preferences introduce no phrase bank or word ban.
- Implementation: Record the benchmark and source settings; the existing
  bank-based composer and original evidence remain unchanged.
- Reference: [V10 benchmark](../research/470_V10_BENCHMARK.md).

## D-060: Adapt the v10 foundation to Hugh's colour flow

- Date: `2026-09-20`
- Category: `runtime_engineering`
- Provenance: Peanut requested reader audits before orchestrated changes, then
  clarified “that's what i meant by we use the prompt as a base--not as it is for huey”.
- Decision: Adapt v10's character and behavioural direction into five compact
  positive runtime directions. Hugh owns wording, connections and sentence
  construction; the existing colour engine owns family and replacement selection.
  The exact platform prompt, its template and samples remain source evidence.
- Implementation: Composer `0.5.0`, instructions `2.0.0` use plain-text generation
  and retire the supplied bank, connector scaffold and inspection command. Luna /
  medium reasoning continues, with explicit low verbosity and Top P `0.98`.
  The two labelled swatches and legacy `one-up` path retain their contracts.
- Records: Local v2 JSON preserves the request and original free-text output;
  the importer accepts v1/v2 without migrating existing evidence. The legacy bank
  column reads `not applicable` for v2. Mechanical checks supply no behaviour verdict.
- Boundary: This refines D-059's benchmark use and implements D-056's bank-free
  direction. Original prompts, outputs and judgments retain their provenance.
  Shared judgment and timed pulse staging remain under D-052/D-038.
- Validation: [Audit and integration record](../research/320_BANK_FREE_ALIGNMENT.md)
  preserves the reader findings, 213 passing tests, mixed-record notebook execution
  and unchanged canonical evidence hashes. Fresh behavioural judgment remains open.
- Reference: [Composer contract](../runtime/COMPOSITION.md) and
  [preserved v10 source](../research/470_V10_BENCHMARK.md).

## D-061: Archive current evals before fresh bank-free evaluation

- Date: `2026-09-20`
- Category: `evidence_governance`
- Provenance: Peanut requested “also let's archive the current evals”.
- Decision: Preserve both current SQLite databases, source records and judgment
  history in a verified local archive, then initialize empty live stores.
- Result: Four colour rows, six behaviour outputs and six attributed judgments
  are archived byte-for-byte. Existing FAILs remain; behaviour outputs `4..6`
  stay unjudged. Sequence continuity keeps future colour IDs above `20166` and
  behaviour output/judgment IDs above `6`.
- Boundary: Archival supplies no new verdict, generation or pulse. The notebook
  reads either empty live state or archived evidence without database writes.
- Reference: [Archive and verification](../research/330_EVAL_ARCHIVE.md).

## D-062: Adapt the supplied prompt with Hugh as the primary name

- Date: `2026-09-21`
- Category: `runtime_engineering`
- Provenance: Peanut supplied the exact prompt and requested adaptation to Hugh's
  different runtime, retaining the wording that delivered the enjoyed responses.
- Decision: Use **Hugh (Hue)**, the five authorial character points and the supplied
  response progression. Adapt its input slot to the mapped colour family and its
  recommendation slot to the engine's supplied same-family replacement.
- Implementation: Instructions `2.1.0`, composer `0.5.1`. Identity and character
  wording are preserved; the response frame uses the supplied Pantone name alone.
  This replaces D-060's paraphrased directions, including “extravagant”. The engine
  retains colour ownership and the model retains free-text composition.
- Boundary: Settings and original evidence are preserved. No live generation,
  behaviour verdict or timed pulse accompanies the adaptation. The earlier
  benchmark and Platform records retain their source versions and wording.
- Reference: [Exact source, adaptation and checks](../research/340_HUGH_PROMPT.md).

## D-063: Leave response construction to Hugh

- Date: `2026-09-21`
- Category: `runtime_engineering`
- Provenance: Peanut clarified, “with the golden prompts, we don't need that template”.
- Decision: Remove D-062's response template. Keep **Hugh (Hue)** and the five
  authorial character points; golden cases guide evaluation of fresh responses.
- Implementation: Instructions `2.2.0`, composer `0.5.2`. Picker context identifies
  the user's family and Hugh's supplied Pantone name. Hugh owns sentence construction;
  prior answers stay outside the runtime prompt.
- Boundary: Colour selection and model settings are unchanged. Mechanical checks
  supply no behaviour verdict; this change runs no live eval.
- Reference: [Source, refinement and checks](../research/340_HUGH_PROMPT.md).

## D-064: Authorize live per-response judging for the first current-app pulse

- Date: `2026-09-21`
- Category: `eval_quality`
- Tags: `behaviour_eval`, `current_app`, `live_judgment`, `fifteen_minute_pulse`, `evidence_attribution`
- Provenance: Peanut authorized one local pulse and clarified that the primary
  assistant should give its verdict in real time as each evaluation runs.
- Decision: The first current-app behaviour pulse uses the primary assistant as
  the live evaluator. It reads each original response with its supplied colour
  facts and records `PASS` or `FAIL` before the next dispatch. A concise note is
  optional and is recorded only when it adds value; no Peanut-verdict column is
  required.
- Bounds: HUE-4 selected six fixed inputs in listed order, repeated twice, for a
  maximum of 12 attempts within 900 seconds and a fresh request context per
  response. The effective settings are `gpt-5.6-luna`, medium reasoning, low
  verbosity and Top P `0.98`, with a 60-second request timeout and no retries.
  The [pulse protocol](../../.local/behaviour-pulses/20260921T175241Z/protocol.json)
  records the cases and the remaining dispatch controls.
- Evidence boundary: This records the authorized method and selected operating
  bounds, not any pulse outcome. Preserve exact requests, raw responses, v2
  records, attempt receipts and append-only primary judgments. Mechanical
  failures remain reported evidence; an API or configuration failure stops the
  pulse without retry or repaired text.
- Boundary: The pulse reports per-response judgments, useful observations and
  mechanical failures. It creates no automatic aggregate behaviour verdict and
  does not promote beta. Existing attributed judgment storage is sufficient;
  historical Peanut judgments remain unchanged.
- Validation: Run `20260921T175241Z` completed with 9 responses and 9 primary
  judgments at behaviour IDs `7..15`: 4 `PASS`, 5 `FAIL`, 1 mechanical failure
  and 0 request errors in `857.587` seconds. All six inputs ran once; the first
  three repeated before the 60-second dispatch guard stopped the run. Original
  records, raw responses, database records and verdicts were verified, with
  runtime source and the colour database unchanged. [The validation receipt](../../.local/behaviour-pulses/20260921T175241Z/validation.json)
  records the closeout evidence.

## D-065: Connect sequential pulses through attributed feedback

- Date: `2026-09-21`
- Category: `runtime_engineering`
- Provenance: Peanut described sequential pulses as the alternative to long
  evaluation runs, with behaviour shaped as evidence emerges. After reviewing
  Polinko's feedback path and Hugh's requirements, Peanut authorized the connection:
  “Yes let’s do that!”
- Decision: Carry useful recorded observations into subsequent pulse context.
  Preserve Hugh's five authorial directions, deterministic colour facts and live
  primary `PASS`/`FAIL` judgment, with observations only when valuable.
- Implementation: Composer `0.6.0` accepts a frozen feedback snapshot. The primary
  selects observations from completed, judged pulses; the snapshot preserves exact
  sources and attribution. Requests receive those observations with their prior
  colour context. Full historical answers remain local evidence. Each pulse fixes
  its snapshot; selection can develop between pulses without adding character rules.
- Boundary: This implements the connection and offline preparation. Further live
  execution needs a bounded batch scope. D-064's nine responses remain the current
  live evidence; behavioural benefit is unmeasured.
- Reference: [Feedback validation](../research/350_PULSE_FEEDBACK.md),
  [operator flow](../runtime/BEHAVIOUR_RECORDS.md#sequential-pulses) and
  [pulse diagram](../diagrams/BEHAVIOUR_PULSE.md).

## D-066: Apply the selected Platform log settings

- Date: `2026-09-24`
- Category: `runtime_engineering`
- Provenance: The author requested, “let's apply the exact settings in the log”,
  while retaining the existing portfolio interaction and the agreed Hugh adaptation.
- Source: [Response v13](https://platform.openai.com/logs/resp_00a745c9371f1130006ab077240b7887d2b97690604366bf48),
  retrieved from the authenticated Platform log. Its returned configuration is
  the selected target; this does not reconstruct which defaults the original
  request omitted. The complete response is preserved in the private source capture.
- Decision: Use every applicable setting supported by the installed Responses
  request schema: Luna, medium reasoning and verbosity, detailed summaries,
  reasoning context `all_turns`, Top P `0.98`, temperature `1`, null output-token
  and tool-call caps, `store=true`, `24h` prompt-cache retention, synchronous
  execution, default service tier, no tools, automatic tool choice, parallel
  tool calls enabled, zero top logprobs, disabled truncation and no previous
  response. The [composer guide](../runtime/COMPOSITION.md#selected-platform-settings)
  and [source fixture](../../tests/fixtures/platform_v13_settings.json) own the
  field mapping. Returned reasoning mode and frequency/presence penalties stay
  reference metadata because they are absent from the supported request schema.
- Implementation: Composer `0.6.1` forms these settings before computing the
  request hash. The verbosity default and example change to medium; existing
  model, reasoning, verbosity and Top P environment overrides retain precedence.
- Boundary: D-063's identity, five character points, template removal, colour
  ownership and display pair remain intact. The 60-second client timeout and
  zero retries remain transport controls. Previous settings and evidence are
  historical; no live generation, eval, behavioural verdict, portfolio UI change
  or publication is part of this settings update.
- Validation: All 225 tests, formatting, lint, type checks and documentation lint
  pass. The SDK wire-body test preserves the exact outgoing request. Dry requests
  for all nine portfolio colours match the selected supported settings while
  preserving prior instructions, input/context and both swatches. Independent
  source review found no issue. No live provider call or eval was run.

## D-067: Stream the API's reasoning summary

- Date: `2026-09-24`
- Category: `runtime_engineering`
- Provenance: The author asked to show Hugh's reasoning during the portfolio turn.
- Decision: Expose the reasoning summary actually supplied by the API through an
  optional streaming callback, and retain its final indexed parts in composition
  records. This is summary text, not access to undisclosed reasoning tokens.
- Implementation: Composer `0.7.0` hashes `stream=true` when selected. It forwards
  summary delta/done events and uses the Response carried by completed, incomplete
  or failed terminal events. Done text replaces the corresponding partial part.
  An empty summary remains empty. Interrupted streams fail without fabricating
  completion; callers retain any already emitted fragments as partial evidence.
  API and network errors stay sanitized, and stream resources close on all exits.
- Boundary: The default complete-response path, D-063's prompt adaptation,
  D-066's model settings, deterministic colours and existing timeout/retry
  controls remain intact. No eval, research-method promotion or judgement is
  introduced. The portfolio owns display, Reset and cancellation.
- Reference: [Streaming contract](../runtime/COMPOSITION.md#optional-reasoning-streaming)
  and [API event](https://developers.openai.com/api/reference/resources/responses/streaming-events#response.reasoning_summary_text.delta).
- Validation: All 235 source tests, formatting, lint and type checks pass.
  Mock SSE coverage verifies early callbacks, exact hashed wire settings,
  completed/incomplete/failed responses, missing summaries, EOF, HTTP read
  failure and both API error shapes. No provider call or eval was used for
  this source validation.
