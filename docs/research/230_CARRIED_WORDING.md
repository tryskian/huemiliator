# Carried Response Wording

| Field | Value |
| --- | --- |
| Code | `CARRIED_WORDING` |
| Category | `case` |
| Status | four human FAILs; current verdicts corrected |
| Last evidence | `2026-09-20`, review of saved August 3 outputs |
| Owns | wording judgment of `.local/evals.sqlite` rows `20163..20166` |

## Case

Peanut identified the stored passes as inaccurate, confirmed all four rows, and
gave the exact reason: **“the responses are too basic.”** The judged object is
each saved fixed loss line, separate from the later model-composed minis.

| Output | Saved response | Peanut verdict |
| --- | --- | --- |
| `20163` | you brought beige energy. | FAIL |
| `20164` | cute. not convincing. | FAIL |
| `20165` | earthy is not the same as intentional. | FAIL |
| `20166` | the idea was right. the nerve was missing. | FAIL |

## Why It Matters

The old pulse-label helper maps `anchor` to `pass`; the database carries no
evaluator history. The preserved anchors belong to the historical colour audit.
They establish no wording PASS. Current row verdicts now hold the human FAILs,
with evaluator, date, scope and exact reason in `current_note`.

The [correction ledger](../../.local/eval-verdict-review-20260920T165055Z/judgments.jsonl)
preserves source messages and before/after rows beside verified backups. Only
`current_verdict` and `current_note` changed. Original wording, colour facts,
timestamps and historical pulse labels remain intact. The separate behaviour
database and its pending outputs `4..6` are unchanged.

## Follow-Up

Report current wording verdicts separately from historical colour-pulse results.
`eval-pulse-label` can overwrite current row verdicts; use the preserved colour
labels for historical inspection. This correction records a human wording
judgment, with no runtime change or new generation. Resume the
[agreed construction review](220_RESPONSE_CONSTRUCTION.md#agreed-next-slice).
