# Validation: Current Eval Archive

| Field | Value |
| --- | --- |
| Code | `330_EVAL_ARCHIVE` |
| Category | `validation` |
| Status | `closed` |
| Last evidence | `2026-09-20` |
| Owns | preservation of current evals and initialization of empty live stores |

## Question and Proof Surface

Peanut requested archival after the bank-free composer integration. Preserve
the current records, exact judgments and unjudged states before fresh evaluation.

## Run and Results

The primary copied both locked databases and 54 source files, verified hashes,
then replaced the live stores with initialized databases retaining their ID
sequences. Source commit: `c81ec9d`; branch: `codex/bigbrain/archive-current-evals`.

| Check | Result |
| --- | --- |
| Colour archive | rows `20163..20166`; four Peanut FAILs, exact notes and historical colour labels preserved |
| Behaviour archive | outputs `1..6`, six attributed judgments; `4..6` remain unjudged |
| Preservation | both archive database hashes match the originals; 54 copied source hashes match; all six original record BLOBs match source bytes |
| SQLite checks | archive and fresh live databases pass integrity and foreign-key checks |
| Live state | both stores empty; colour pending `0`; next colour ID `20167`, behaviour output/judgment IDs `7` |
| Review | notebook reads empty live state and either archived mini without changing database bytes |

Archive: `.local/parked/evals-20260920T214702Z-before-bank-free-evaluation/`.
The [manifest](../../.local/parked/evals-20260920T214702Z-before-bank-free-evaluation/manifest.json)
records hashes, counts, source paths and sequence values; the
[validation receipt](../../.local/parked/evals-20260920T214702Z-before-bank-free-evaluation/validation.json)
records notebook checks and final Git closeout separately. Source folders remain
available at their original paths; archived database files are read-only.

## Decision and Limits

**Pass: preservation and empty-state reset.** [D-061](../governance/DECISIONS.md#d-061-archive-current-evals-before-fresh-bank-free-evaluation)
records the decision. This local archive is not a remote backup or a behaviour
result. Original FAILs and missing judgments retain their meaning.

## Next Move

Judge fresh responses together when Peanut starts that work. For archived
review, use the [notebook database path](../runtime/BEHAVIOUR_RECORDS.md#current-and-archived-evidence).
