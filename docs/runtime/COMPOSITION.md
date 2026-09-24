# Hugh's Language Composer

`huemiliator compose <hex>` gives Hugh five positive directions and the existing
deterministic colour facts. He composes one free-text response through the OpenAI
Responses API. Composer `0.7.2` uses instructions `2.2.0` under
[D-063](../governance/DECISIONS.md#d-063-leave-response-construction-to-hugh).

The [supplied authorial prompt](../research/340_HUGH_PROMPT.md) provides Hugh (Hue)'s
identity and five verbatim character points. The
[runtime text](../../src/huemiliator/agent.py) leaves sentence construction to Hugh.
Picker context names the user's colour by family and Hugh's supplied replacement
by its Pantone name. The engine supplies his colour; golden cases guide evaluation.
Behaviour judgment follows the current [15-minute behaviour method](../research/030_PB_BEHAVIOUR.md)
and its [Behaviour Records and read-only notebook](BEHAVIOUR_RECORDS.md). Its
first current-app pulse has completed with bounded coverage; a further pulse
requires a separate choice.

## Setup and Use

Copy [`.env.example`](../../.env.example) to the ignored `.env` for a fresh setup:

```dotenv
OPENAI_API_KEY=your-key
HUEMILIATOR_MODEL=gpt-5.6-luna
HUEMILIATOR_REASONING_EFFORT=medium
HUEMILIATOR_VERBOSITY=medium
HUEMILIATOR_TOP_P=0.98
```

Exported settings take precedence over `.env`. The selected defaults are Luna,
medium reasoning, medium verbosity and Top P `0.98`; dry-run and saved requests
show the actual values. The live request sends colour facts to OpenAI.

```sh
huemiliator compose '#d9a6a1' --dry-run
huemiliator compose '#d9a6a1'
huemiliator compose '#d9a6a1' --format json
huemiliator compose '#d9a6a1' --feedback .local/feedback.json --dry-run
```

Dry-run prints the exact request packet without an API key or model call. Text
mode prints two labelled swatches and Hugh's response after mechanical checks.
Colour-capable terminals show the actual colours; redirected output, `NO_COLOR`
and `TERM=dumb` use plain square markers and labels. JSON mode prints the full
local inspection record. Redirect stdout to preserve a candidate; the command
creates no files or database rows itself. Behaviour records reach
`.local/behaviour.sqlite` only through the explicit saved pulse or mini
record/import/judgment path documented in [Behaviour Records](BEHAVIOUR_RECORDS.md).

## Selection and Composition

1. The colour engine resolves the input's family and deterministic replacement.
2. The API receives the adapted directions and a JSON input carrying colour facts
   and one picker interaction.
3. Hugh returns ordinary text, using the user's family name and the supplied
   replacement's Pantone name.
4. The CLI preserves that original text and renders the two swatches from the
   deterministic facts.

Optional `--feedback` loads a hash-checked snapshot from completed pulses.
The model receives selected, exact observations with evaluator, prior family,
replacement and source IDs. Full prior responses stay in the local snapshot.
Selection is the primary's review work, with no automatic pattern classifier or
invented note. [Sequential pulse preparation](BEHAVIOUR_RECORDS.md#sequential-pulses)
freezes this context for the whole pulse under D-065.

The user's swatch retains the actual input hex and mapped family label; Hugh's
swatch carries its supplied Pantone name. Hexes serve rendering and inspection
under [D-045](../governance/DECISIONS.md#d-045-speak-in-family-and-pantone-names).
The earlier word bank, connector IDs and relationship schema are retired.
The legacy `one-up` retains its fixed line, and `behaviour-facts` retains that
historical `loss_line` in its fact packet. Composition omits it from the request.

## Inspection Record

The `huemiliator.composition_record.v2` local JSON wrapper preserves:

- the exact API request, including adapted instructions, colour facts and settings
- composer and instruction versions, request hash and fixed `display_swatches`
- request timestamps, response ID, returned model, status, usage and refusal or
  incomplete details
- original output text, mechanical issues and a `behaviour_verdict` of `null`
- the complete `feedback_snapshot`, when supplied; its selected context is also
  inside the exact API request and therefore covered by the request hash

The request uses text output; JSON is the local evidence format. Its input retains
`input` and `runtime_facts` for inspection and import. Bank versions, bank hashes,
language IDs and connector annotations belong to historical v1 records.
The request hash covers canonical `api_request` JSON with sorted keys, compact
separators, UTF-8 and unescaped Unicode. It identifies what ran without promising
repeatable model output.

[Behaviour records and the read-only notebook](BEHAVIOUR_RECORDS.md) accept both
record versions, preserve original bytes and keep attributed judgments separate
from mechanical checks. The CLI emits stdout for explicit capture; the pulse
runner calls the same composer functions and saves original records. Its live
judgment ledger and records are imported together for notebook review.

## Mechanical Checks and Failures

Checks cover completion, refusal, usable text, the supplied Pantone name and
visible hex codes. They establish a usable response envelope; grammar, coherent
reasoning, meaningful colour rationale and Hugh's character remain behavioural
judgments. Punctuation serves his voice under D-057.

A refused, incomplete or mechanically invalid candidate retains its original
output. The command returns exit `2`, writes the full JSON record even in text
mode and explains the issue on stderr. Successful mechanical checks return `0`;
configuration, input or API failures return `1`. Neither status assigns a
behavioural PASS or FAIL. API errors identify their type and HTTP status without
echoing provider text.

Each invocation makes one API attempt with a 60-second client timeout and zero
retries. Failed candidates stay observable without automatic retries or output
repair. These transport controls are independent of the logged model settings.

## Selected Platform Settings

[D-066](../governance/DECISIONS.md#d-066-apply-the-selected-platform-log-settings)
applies the supported settings from the author's selected
[v13 response log](https://platform.openai.com/logs/resp_00a745c9371f1130006ab077240b7887d2b97690604366bf48).
The source is the returned response configuration, not a reconstructed original
request. [The captured settings fixture](../../tests/fixtures/platform_v13_settings.json)
records the exact comparison values. D-069 restores `detailed` after the author
confirmed that the concise activity headings did not meet the requirement for
the fuller summary shown in the selected log.

| Request fields | Selected values |
| --- | --- |
| `model` | `gpt-5.6-luna` |
| `reasoning` | effort `medium`, summary `detailed` under D-069, context `all_turns` |
| `text` | format `text`, verbosity `medium` |
| `top_p`, `temperature` | `0.98`, `1` |
| `max_output_tokens`, `max_tool_calls` | `null`, `null` |
| `store`, `prompt_cache_retention` | `true`, `24h` |
| `background`, `service_tier` | `false`, `default` |
| `tools`, `tool_choice`, `parallel_tool_calls` | `[]`, `auto`, `true` |
| `top_logprobs`, `truncation`, `previous_response_id` | `0`, `disabled`, `null` |

There is no explicit application output-token cap; provider limits still apply.
Responses are stored by the API. The CLI still writes no local database rows.
The current inspection record retains the exact request and visible output;
reasoning summaries are retained as indexed text parts in
`api_response.reasoning_summaries`; the CLI speech renderer remains unchanged.
Explicit summary selection follows the
[Responses documentation](https://developers.openai.com/api/docs/guides/reasoning#reasoning-summaries).

The returned log also has reasoning mode `standard` and frequency/presence
penalties of `0`. Those fields are not declared in the installed Responses
request schema and stay reference metadata. The original prompt ID, template
and plain `brown` input are source evidence; D-063's five character points,
supplied colour facts and display swatches remain the runtime adaptation.
`all_turns` does not introduce conversation history into this single-turn call.

This supersedes the earlier runtime's low verbosity, omitted summaries,
8,192-token cap and `store=false`. Historical requests and pulse evidence retain
their original settings. Settings parity supplies no behavioural verdict.

## Optional Reasoning Streaming

[D-067](../governance/DECISIONS.md#d-067-stream-the-apis-reasoning-summary)
adds an optional transport for callers that show the API's reasoning summary.
`build_composition_request(..., stream=True)` adds the flag before hashing.
`generate_composition(..., on_reasoning=callback)` forwards actual summary delta
and done events, including item/part indices and sequence numbers. Done events
contain the complete part; callers replace that part rather than append it twice.
The callback never invents reasoning text.

[D-069](../governance/DECISIONS.md#d-069-require-fuller-reasoning-summaries)
requires fuller API summary text, with the original v13 paragraph as the reference.
D-068's concise headings passed transport checks but did not satisfy that request.
The current detailed/medium controls returned empty summaries outside the SDK and
bridge. A temporary high-effort brown control returned a paragraph, but streamed
blue did not; high effort is not adopted as a reliable remedy. The original v13
prompt returned detailed summaries through the same key. The omission is therefore
request-dependent in these observations; its provider-side cause remains unknown.
The current prompt and medium effort are preserved. An empty response stays empty;
there is no automatic retry, fallback summary or separate generated explanation.

The source consumes the SDK's raw event stream and retains terminal responses
for completed, incomplete and failed outcomes. Their visible output and
mechanical checks follow the existing composition path. Final summary parts
are retained in order in JSON records, including non-streaming records; an
absent summary stays empty. API/SSE errors, interrupted reads and EOF without a
terminal event fail explicitly. Already emitted parts remain with the caller
as partial evidence, not a completed response. The stream closes on every exit.

The configured 60-second network-operation timeout and zero retries remain.
For streaming, the read timeout applies while waiting for a body read; it is
not a new overall generation deadline. The portfolio's worker has its separate
120-second elapsed-time limit. There is no artificial waiting time.
Default CLI and pulse callers keep their existing complete-response transport.
Streaming changes no prompt, colour fact, model setting, eval or stored verdict.

## Next Method Step

[Prompt validation](../research/340_HUGH_PROMPT.md) covers this adaptation;
[bank-free integration](../research/320_BANK_FREE_ALIGNMENT.md) records the earlier
change. Fresh behavioural judgment follows the authorized current-app pulse method
documented in [Behaviour Records and the read-only notebook](BEHAVIOUR_RECORDS.md).
The first pulse and its current evidence are recorded there; its bounded result
remains separate from this composer contract, and the next pulse remains a
separate human choice.
