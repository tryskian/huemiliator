# Huemiliator Charter

## Mission

Build a small, local, CLI-first mini chatbot for inspecting deterministic
colour one-up behaviour through picker-first input, fixed family rules, and
fail-first evaluation.

## Character Profile

Generated dialogue, visual design, and behaviour evaluation use this durable
authorial character reference
([D-040](DECISIONS.md#d-040-hue-is-a-courteous-snob-who-opens-with-a-backhanded-compliment)).
The [supplied authorial prompt](../research/340_HUGH_PROMPT.md) now provides the
five character points, with sentence construction left to Hugh under
[D-063](DECISIONS.md#d-063-leave-response-construction-to-hugh).
The earlier [v10 benchmark](../research/470_V10_BENCHMARK.md) retains its source history.

| Aspect | Character direction |
| --- | --- |
| Identity | His name is **Hugh (Hue)**. “Huey” is our affectionate nickname; he is unaware of it and would be infuriated to hear it. Character-facing instructions and self-reference use Hugh. |
| Disposition | **A snob but not snide.** A pretentious and celebrated colour theory academic who just happens to lack awareness. |
| Voice | Eloquent and matter-of-fact, with sharp taste, wit and immaculate coherence. Graceful, empty and generic compliments accompany meaningful colour rationale, expressed in crisp, brief exacting statements or rhetorical questions. |
| Punctuation | Serves Hugh's character, grammar and meaning. Peanut's personal-writing canaries belong to Peanut's voice; an em dash alone is not a Hugh failure ([D-057](DECISIONS.md#d-057-scope-punctuation-canaries-to-peanuts-writing)). |
| Visual direction | Mid-century modern illustration; tall, slender silhouette, long nose, black turtleneck, controlled posture, and restrained airs and graces. He flourishes an outrageously rotund snifter of burgundy. |
| Nickname reaction | The author's reference is a slow sweep upward to lock eyes, followed by a stiff but polite “I beg your pardon?” |

His backhanded opening conveys a judgment of taste through apparent praise.
The author said Hugh's assertion “has to be objective”: Hugh delivers aesthetic
judgments with the certainty of fact, while literal colour properties come from
supplied facts. [D-044](DECISIONS.md#d-044-hugh-delivers-aesthetic-verdicts-as-settled-fact)
preserves the worked examples. The author's “something like that. not that exactly”
leaves wording open; “he's an intellectual” frames the “fine / finer” echo as wit.

The user's actual selected swatch carries its mapped family label; Hugh's
replacement swatch carries its supplied Pantone name. His sentence accompanies
both. Colour names provide the nouns; hex codes serve rendering and internal
evidence, while the input's matched Pantone name stays internal
([D-045](DECISIONS.md#d-045-speak-in-family-and-pantone-names)).

The [historical visual reference](../research/450_LOCAL_LANGUAGE.md#visual-character-reference)
preserves the private style-image source. Its depicted figure is a separate
character; it supplies illustration style, with no additional requirements for
Hugh beyond the direction above.

### Opening Reference Material

The [historical language note](../research/450_LOCAL_LANGUAGE.md#character-direction-write-hues-voice)
preserves exact openings, worked lines and meanings, plus the
[later adjective and phrase list](../research/450_LOCAL_LANGUAGE.md#authorial-reference-material)
(D-047). These remain development references. D-048 places connective language
within Hugh's reasoning; D-060 leaves composition to Hugh.

## Behaviour Method

Sequential 15-minute pulses carry useful, attributed observations forward under
[D-065](DECISIONS.md#d-065-connect-sequential-pulses-through-attributed-feedback).
The primary reviews patterns between pulses and freezes the selected feedback
for the next pulse. Hugh's character brief and colour ownership stay intact;
the exact context and source judgments remain inspectable.

The first authorized current-app behaviour pulse uses a 15-minute local/API
window. Peanut authorized HUE-4's primary assistant to record an
explicit `PASS` or `FAIL` for every response in real time. A concise observation
is optional only when it adds value; there is no required Peanut-verdict column.
The pulse uses six fixed hex inputs in listed order, repeated twice, with at
most twelve attempts inside 900 seconds and the current frozen instructions and
settings. The engine supplies replacements. This bounded delegation does not
promote the method or change Huey's human ownership of scope, meaning,
acceptance and go/no-go.

[D-063](DECISIONS.md#d-063-leave-response-construction-to-hugh)
continues D-056's bank-free direction: five authorial points on stable colour
facts and picker context. The response template, bank and connector scaffold
are retired. Hugh owns wording and reasoning; the colour engine owns replacement.
Under [D-064](DECISIONS.md#d-064-authorize-live-per-response-judging-for-the-first-current-app-pulse),
the first pulse completed with bounded live primary-assistant judging; broader
pulse promotion remains separate. The completed pulse is carried by the
[current handoff](SESSION_HANDOFF.md#pulse-result-and-next-slice) and
[behaviour records](../runtime/BEHAVIOUR_RECORDS.md). The [behaviour boundary](../research/030_PB_BEHAVIOUR.md)
owns judgment choices and method promotion; runtime directions live in `agent.py`.

## Durable Rules

- The canonical picker runtime stays macOS-local, with one native colour picker
  and one canonical hex code.
- The frozen `margaret2` snapshot stays the primary colour reference. Runtime
  owns swatch matching, family assignment, same-family rank and one-up selection.
  Swatch matching uses fixed `delta-e cie76` and source-order tie-breaks.
- Replacement stays same-family, next-rank, and non-wrapping; `neutral`
  selection is constrained to its undertone bucket.
- The carried `one-up` loss line remains downstream of the colour decision.
- Eval semantics stay binary: `PASS` or `FAIL`. In the carried `Beta 1.0`
  non-OCR colour baseline, the fail-pressure pulse carries the verdict and rows
  remain evidence within it; pressure stays on one family lane at a time.
  `warm` stays an audit cohort rather than a runtime family.
- The live DB keeps only the current proof surface. Tracked docs, code, tests,
  and local eval evidence are canonical repo truth; `docs/peanut/` stays private.
- Small, testable changes are the default. Evidence inspection comes before
  interpretation; evidence chains stay preserved through archive-first handling.

## Working Model

The human lead owns hypotheses, scope boundaries, acceptance criteria,
meaning-level trade-offs and go/no-go. The engineer owns implementation,
validation, Git and PR flow, proactive hygiene and execution recommendations.
Use one feature branch per change set, protected-main PR flow and clean synced
`main` as the tracked stop state. Parallel implementation uses dedicated worktrees.

## Documentation Governance

Keep every document concise and easy to scan, with one clear job and links to
supporting detail. Research notes and diagrams receive equal care. Capture
substantive reasoning, findings, method clarifications, and agreed decisions as
they emerge, using the [research templates](../runtime/templates/README.md).
Preserve source and chronology; distinguish direction, interpretation,
hypothesis, implementation, and evidence. Keep notes and diagrams aligned as
the meaning or method changes. D-049 records this standing practice.

The research develops through iteration. When material is unfamiliar, use
existing source indexes to trace its lineage and carry its context forward.

The required startup [handoff](SESSION_HANDOFF.md) carries setup, eval method,
roles, open choices and next step. Refresh it when these change, linking completed
work to its owning records. Startup understanding remains independent of private
reports and conversation history under D-053.

### Documentation Delegation

Under [D-050](DECISIONS.md#d-050-use-a-continuing-documentation-task)
and [D-051](DECISIONS.md#d-051-assign-documentation-roles-from-source-audits),
a four-role continuing-task method now handles assigned work in the shared
checkout; the current registry and IDs live in the handoff.
Assignments specify full reading scope, source versions, owned files, allowed
operations and result.

The four roles are documentation, runtime records, research records and
transcript keeper. The collaboration guide owns their file mapping; the handoff
owns their current IDs and status.

Each task may delegate bounded readles inside its exact ownership, reviews their
returns, and returns one checked result to HUE-4. The primary personally reads
sources and returns, resolves cross-owner gaps, and owns meaning review,
integration, runtime implementation, evaluation under Huey's agreed method,
canonical evidence and Git.
The human lead owns hypotheses, scope, acceptance, meaning-level trade-offs and
go/no-go; broader shared-judgment rules remain under D-052.

Checkpoints preserve sources, changes, checks and handoff as work progresses.
The primary groups related edits into commits at meaningful boundaries rather
than committing every edit.

The [collaboration guide](../diagrams/COLLABORATION.md) owns role and assignment
detail; the [handoff](SESSION_HANDOFF.md#documentation-task) carries the current
registry and assignment. Source captures preserve exact wording, attribution,
order, locations, gaps and distinct capture/discourse dates; summaries,
interpretations and later corrections retain attribution. Implementation
requires separate assignment; worktrees share primary-coordinated `.local`
evidence. Supporting work stays within the active scope.

### Document Homes

| Home | Owns |
| --- | --- |
| `docs/governance/CHARTER.md` | mission, durable rules and character |
| `docs/governance/DECISIONS.md` | durable decisions |
| `docs/governance/SESSION_HANDOFF.md` | active slice and carryover |
| `docs/runtime/RUNBOOK.md` | operator procedure |
| `docs/runtime/ARCHITECTURE.md` | stable system shape |
| `docs/runtime/START_END_REFERENCE.md` | command card |
| `docs/research/` | research notes and proof-surface reads |
| `docs/diagrams/` | runtime and eval diagrams |
| `docs/peanut/` | local and private working lane |

## Current Scope

Local picker-first interaction, deterministic matching and replacement, Hugh’s
free-text composition, and bounded behaviour review on the carried colour baseline.
Single-purpose research notes and diagrams stay aligned with live repo behaviour.

## Security / Ops Baseline

- Local `.venv` is the canonical development environment.
- Local terminal execution is the trusted development boundary.
- `.local/evals.sqlite` is the live colour eval evidence store.
- `make doctor-env` reports the environment diagnostic snapshot.
- `make end` requires live eval `pending` of `0` on clean synced `main`.
- Mac-wide keep-awake state is owned by the Coffee Codex plugin;
  `make start` and `make end` do not control it.
