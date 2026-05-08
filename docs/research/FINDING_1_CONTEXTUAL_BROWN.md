# Finding 1: Contextual Brown

## Core Claim

Brown does not behave like a clean spectral category in Huemiliator's
deterministic family-plus-rank system.

In practice, `brown` behaves more like a contextual bucket that overlaps with:

- dark orange
- muted orange
- gold
- olive
- warm neutral

That matters because Huemiliator is not allowed to hide behind taste or
inference. It has to:

- classify deterministically
- rank deterministically
- replace deterministically

So if `brown` is only stable when a human quietly supplies context, the toy
has to surface that break directly in the runtime and eval lanes.

## What Exposed It

The first brown-family long run made the problem visible.

The broad early failure cluster was not random noise. It repeated in one
direction:

- replacements drifting toward `yellow`
- replacements drifting toward `gold`
- replacements drifting toward `olive`

Examples from that first judged lane included:

- `Puffin's bill -> Spectra yellow`
- `Hazel -> Antique gold`
- `Leather brown -> Spruce yellow`
- `Amber brown -> Ecru olive`
- `Ginger bread -> Tapenade`
- `Bombay brown -> Tinsel`
- `Carob brown -> Boa`

So the failure was not simply "brown is hard." The useful signal was narrower:
the deterministic ladder was treating loud yellow/gold/olive shoulders as
better browns than the earthy core.

## What Changed In The Runtime

Two different corrections followed from that evidence.

### 1. Brown boundary refinement

The first correction was routing-level:

- darker earthy warm tones could enter `brown` earlier
- pale warm neutrals still stayed out of `brown`

That fixed the first obvious routing mistake, where some earthy warms were
collapsing into `neutral` or staying `orange`.

### 2. Brown rank refinement

The second correction was ranking-level:

- the yellow/gold/olive shoulder was demoted below the earthy brown core
- brown replacements stopped climbing by raw chroma alone

That narrowed the first big failure cluster, but it also exposed a second
question: some bright gold shoulder colours probably should not be in `brown`
at all.

### 3. Bright gold shoulder reclassification

The next correction moved part of that shoulder out of `brown` at
classification time.

That shifted colours like these away from the brown lane:

- `Amber gold`
- `Mineral yellow`
- `Mustard gold`
- `Narcissus`
- `Golden spice`
- `Ceylon yellow`

After that change, the remaining problem was no longer the loud gold shoulder.

## What The Data Says Now

The post-fix rerun is materially stronger than the first brown pass.

At an early judged checkpoint from the fresh rerun:

- `680` new brown rows had been recorded after the restart
- `12` had been judged `pass`
- `6` had been judged `fail`
- `662` remained pending at that check

The judged passes are now much more in-lane:

- `Major brown -> Chocolate brown`
- `Bungee cord -> Tarmac`
- `Lead gray -> Pinecone`
- `Dull gold -> Tortoise shell`
- `Antique bronze -> Camel`
- `Indian tan -> Thrush`

The early residual failures were much narrower than the first run:

- `Black ink -> Grape leaf`
- `Beech -> Covert green`
- `Capers -> Dusky green`
- `Covert green -> Aloe`
- `Military olive -> Gray green`
- `Nutria -> Khaki`

So the main failure shape changed quickly once the loud gold shoulder was
trimmed back.

The earlier broad `yellow/gold/olive` shoulder problem was reduced.

The remaining early problem was a more specific muted green and khaki edge
inside the brown lane.

## What The Completed Rerun Added

The completed post-classification rerun made the next boundary clearer.

At the completed-run checkpoint:

- `2368` brown rows had been recorded in the rerun
- `45` had been judged `pass`
- `28` had been judged `fail`
- `2295` remained unjudged in the local queue

The stronger signal held:

- the earthy core now behaves much better than it did in the first run
- the primary residual failure cluster is still the muted green and olive seam

Repeated failures still center on:

- `Beech -> Covert green`
- `Capers -> Dusky green`
- `Black ink -> Grape leaf`
- `Covert green -> Aloe`

But the completed tail also showed a smaller remaining orange shoulder:

- `Orange popsicle -> Orange tiger`
- `Persimmon orange -> Puffin's bill`
- `Autumn glory -> Turmeric`

So the completed rerun did two useful things at once:

- it confirmed that the brown-core fix was real, not luck
- it showed that contextual brown still leaks at both edges:
  - muted green and olive on one side
  - orange and ochre on the other

## Why This Matters

This finding changes what Huemiliator is testing.

The toy is not only testing whether a fixed colour catalog can support
deterministic matching. It is also testing whether human colour categories can
survive deterministic routing without hidden human context.

`Brown` is the first place where the answer is visibly "not by default."

That makes this a theory-level finding, not just one failure cluster:

- some colour categories are context-dependent enough to break clean ladder
  logic
- deterministic eval does not smooth that over; it exposes it
- Huemiliator therefore needs category-specific handling where the category
  itself is unstable

## What This Finding Is Not

This note is not:

- a release note
- a package-version note
- a branch log
- a beta page by itself

It is a special research finding that explains why the brown lane matters and
why the runtime had to change around it.

## What It Points To Next

The next likely correction is not another broad gold fix.

The remaining pressure is still strongest at the muted green and khaki edge
around names like:

- `Covert green`
- `Dusky green`
- `Grape leaf`
- `Gray green`
- `Khaki`

But the completed tail also says the orange shoulder is not fully gone yet.

So the next runtime correction has to choose between two real residual seams:

- muted green and khaki inside the contextual brown bucket
- a smaller remaining orange shoulder beyond the bright-gold trim

## Follow-On Classifier Correction

The next correction chose the family-boundary path first.

Using the fully judged closed brown rerun as the evidence base:

- `201` unique brown pairs were judged
- `117` passed
- `84` failed
- the dominant residual failures split between:
  - muted green and olive misroutes
  - a smaller orange, yellow, and gold shoulder

The runtime now excludes those shoulders before brown ranking:

- muted olive and khaki cases leave `brown` before the dark earthy shortcut
- loud orange, yellow, and gold cases leave `brown` before replacement ranking
- the active brown subset in the frozen snapshot drops from `202` swatches to
  `125` swatches

This is still a classifier correction, not a completed finding by itself. It
needs a fresh two-hour judged brown run before the new boundary can be treated
as settled evidence.
