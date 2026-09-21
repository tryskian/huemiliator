# Hugh's Language Composer

`huemiliator compose <hex>` gives Hugh five positive directions and the existing
deterministic colour facts. He composes one free-text response through the OpenAI
Responses API. Composer `0.5.2` uses instructions `2.2.0` under
[D-063](../governance/DECISIONS.md#d-063-leave-response-construction-to-hugh).

The [supplied authorial prompt](../research/340_HUGH_PROMPT.md) provides Hugh (Hue)'s
identity and five verbatim character points. The
[runtime text](../../src/huemiliator/agent.py) leaves sentence construction to Hugh.
Picker context names the user's colour by family and Hugh's supplied replacement
by its Pantone name. The engine supplies his colour; golden cases guide evaluation.
Behaviour judgment and timed pulses remain separate work.

## Setup and Use

Copy [`.env.example`](../../.env.example) to the ignored `.env` for a fresh setup:

```dotenv
OPENAI_API_KEY=your-key
HUEMILIATOR_MODEL=gpt-5.6-luna
HUEMILIATOR_REASONING_EFFORT=medium
HUEMILIATOR_VERBOSITY=low
HUEMILIATOR_TOP_P=0.98
```

Exported settings take precedence over `.env`. The selected defaults are Luna,
medium reasoning, low verbosity and Top P `0.98`; dry-run and saved requests
show the actual values. The live request sends colour facts to OpenAI.

```sh
huemiliator compose '#d9a6a1' --dry-run
huemiliator compose '#d9a6a1'
huemiliator compose '#d9a6a1' --format json
```

Dry-run prints the exact request packet without an API key or model call. Text
mode prints two labelled swatches and Hugh's response after mechanical checks.
Colour-capable terminals show the actual colours; redirected output, `NO_COLOR`
and `TERM=dumb` use plain square markers and labels. JSON mode prints the full
local inspection record. Redirect stdout to preserve a candidate; the command
creates no files or database rows itself.

## Selection and Composition

1. The colour engine resolves the input's family and deterministic replacement.
2. The API receives the adapted directions and a JSON input carrying colour facts
   and one picker interaction.
3. Hugh returns ordinary text, using the user's family name and the supplied
   replacement's Pantone name.
4. The CLI preserves that original text and renders the two swatches from the
   deterministic facts.

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

The request uses text output; JSON is the local evidence format. Its input retains
`input` and `runtime_facts` for inspection and import. Bank versions, bank hashes,
language IDs and connector annotations belong to historical v1 records.
The request hash covers canonical `api_request` JSON with sorted keys, compact
separators, UTF-8 and unescaped Unicode. It identifies what ran without promising
repeatable model output.

[Behaviour records and the read-only notebook](BEHAVIOUR_RECORDS.md) accept both
record versions, preserve original bytes and keep attributed judgments separate
from mechanical checks.

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

Each invocation makes one API attempt with a 60-second timeout and an 8,192-token
output budget, including reasoning tokens. `store=false` is explicit. Reasoning
summary is omitted from the request as an observability choice; reasoning effort
defaults to medium. Failed candidates stay observable without automatic retries or
output repair.

## Next Method Step

[Prompt validation](../research/340_HUGH_PROMPT.md) covers this adaptation;
[bank-free integration](../research/320_BANK_FREE_ALIGNMENT.md) records the earlier
change. Fresh behavioural judgment follows the agreed Peanut-first
method. Case selection, timing, in-flight handling and pulse-wide aggregation
still need alignment before the first 15-minute behaviour pulse.
