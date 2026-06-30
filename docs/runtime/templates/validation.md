<!-- @format -->

# Validation Template

Use this for tracked or staged proof docs where the job is to show whether a
bounded eval surface, runtime audit, branch preflight, or repo gate actually
held.

## Metadata

| Field | Value |
| --- | --- |
| Code | `NNN_VALIDATION` |
| Category | `validation` |
| Status | `staged`, `running`, `closed`, `failed`, or `snapshot` |
| Last evidence | `YYYY-MM-DD` |
| Owns | one sentence naming the proof surface or gate this doc covers |

## Headline Shape

- `Validation: Name`
- or `Proof Surface: Name`
- or `Gate Proof: Name`
- or `Closeout Proof: Name`

## Section Order

1. metadata table
2. `Question`
3. `Proof Surface`
4. `Run`
5. `Result Table`
6. `Decision`
7. `Residual Risk`
8. `Next Move`

## Required Validation Moves

- state the exact eval, audit, preflight, or closeout surface being proved
- state the bounded run, command sequence, branch, and repo state explicitly
- state whether the proof is branch-local preflight or final clean-main closeout
- include live DB pending status when eval truth is part of the proof
- keep the proof in a compact table
- state the decision plainly:
  - `pass`
  - `hold`
  - `rerun`
  - `fail`
- state what the validation still does not prove

## Default Run Table

| Check | Surface | Result | Read |
| --- | --- | ---: | --- |
| bounded eval read | ids, range, or pulse label | `pass/fail` | anchors, seams, excluded |
| sampler truth | runtime family and source-order surface | `pass/fail` | one compact note |
| pending eval gate | `.local/evals.sqlite` | `0` | pending rows |
| repo validation | command sequence | `pass/fail` | checks that matter |
| git closeout | branch and sync state | `pass/fail` | clean synced `main` or preflight only |

## Default Decision Table

| Decision | Reason |
| --- | --- |
| `pass`, `hold`, `rerun`, or `fail` | one sentence |

## Validation Questions To Answer

- what exact surface is being proved?
- what bounded run or command sequence produced the evidence?
- did the eval surface, gate, or closeout actually hold?
- is this a branch preflight or the final repo closeout?
- what live DB or proof-surface count matters?
- what still remains outside the proof?
- what is the immediate next move?

## Style Rules

- lead with the metadata table
- keep the run proof in tables
- keep the decision short and operational
- keep residual risk to one or two bullets
- label preflight evidence separately from final clean-main closeout evidence
- do not let the doc drift into a broader lane recap
