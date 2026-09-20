# Bank-Free Composer Alignment

| Field | Value |
| --- | --- |
| Code | `320_BANK_FREE_ALIGNMENT` |
| Category | `validation` |
| Status | snapshot |
| Last evidence | `2026-09-20` |
| Owns | audit findings, adaptation boundary and mechanical validation |

## Question and Boundary

Can Hugh compose freely from his character and supplied colour facts while the
existing colour engine and original evidence remain intact?

Peanut clarified: “that's what i meant by we use the prompt as a base--not as it
is for huey”. [V10](470_V10_BENCHMARK.md) supplies the behavioural foundation.
The runtime adapts its directions; its exact template remains source evidence.

## Audit and Assignment

Three read-only readers reported before the primary assigned implementation.

| Reader | Finding | Assigned change |
| --- | --- | --- |
| Runtime | bank material, connector IDs and JSON response schema constrain composition | remove scaffolding; adapt five positive directions; retain deterministic facts and paired swatches |
| Settings and records | Luna/medium already configured; low verbosity and Top P omitted; importer assumes v1 bank records | explicit settings; v2 text records with v1 compatibility; read-only notebook |
| Documentation | active guides still prescribe the bank; startup notes wrongly leave shade ownership open | concise current docs and adaptation decision; preserve historical sources |

The primary coordinates isolated worktrees, reviews the combined result and
owns integration. The [composer guide](../runtime/COMPOSITION.md) owns the
implemented contract; [D-060](../governance/DECISIONS.md#d-060-adapt-the-v10-foundation-to-hughs-colour-flow)
records the clarified scope.

## Validation

| Check | Result |
| --- | --- |
| Actual local dry-run | Luna / medium / low verbosity / Top P `0.98`; five adapted directions and colour facts |
| Mock request through v2 record and temporary DB | exact text/bytes preserved; repeat import idempotent; judgments unassigned |
| Historical/current records and read-only notebook | mixed v1/v2 imports pass; all notebook code cells execute; temporary DB hash unchanged |
| Cross-review regression | malformed Top P fails composition cleanly while colour resolution remains usable |
| Original SQLite evidence | both canonical hashes unchanged |
| Branch integration | `make check`: 213 tests, formatting, lint, types and diff checks pass |

The [local receipt](../../.local/bank-free-composer-20260920/validation.json)
records checks and original hashes. Final clean-main closeout is recorded there
after protected-main integration; the branch checks above are mechanical proof.

## Next Move

Judge fresh responses together under the Peanut-first method. No live generation
or timed pulse belongs to this change;
mechanical success supplies no behavioural verdict.
