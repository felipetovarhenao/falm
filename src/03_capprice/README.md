# Track 03: **capprice**

## Musical Output

**Duration:** ~2.5 minutes

A frenetic, rhythmically intricate study exploring additive/subtractive processes and polyrhythmic layering. Built around a 4:3 frequency ratio (perfect fourth) as its tonal center, the piece oscillates between moments of dense, glitchy complexity and sparse, sustained textures. The track employs seven distinct musical "gestures" that recombine in various patterns, creating sections that alternate between chaotic bursts and measured polyrhythmic cycles before culminating in a sudden climactic release.

---

## Structure

**`01_glitch/`** — Eight variably-sized sections (3-16 events each). Seven gesture types (fast arpeggios, crushed crescendos, strummed chords, rests, sustained chords, harmonic glissandi, synthetic chords) combine in weighted random patterns. Duration units drawn from ranked fractional subdivisions of a 2.15-second bar. Voice count increases from 1 to 5; section density grows; gaps between sections gradually close. Minimal reverb processing throughout.

**`02_polyrhythm/`** — Seven polyrhythmic canons (2-9 simultaneous voices). Each voice cycles through a different subdivision (1/8 to 3/4 of the bar duration) with staggered entry delays. Individual notes use staccato strings or sine tones with shaped amplitude envelopes. Total section duration contracts from 3 bars to 1/2 bar.

**`03_loops/`** — Nested loop structure counting down: 9 iterations of object 9, then 8 iterations of object 8, etc., down to 1 iteration of object 1. Each iteration lasts 1/8 bar (268.75ms). Creates accelerating rhythmic cascade as loop size decreases. Uses scrambled gesture sequence.

**`04_trail/`** — 12-stage expanding process. Begins with 4-note sustained chord that grows to full 32-note collection. Each stage adds: (1) sustained strings with time-compression effects, (2) granular fragments from the loops recording read backwards. Subdivisions double every two stages (1, 1, 2, 2, 4, 4...). Final low bass sine tone. Tight rhythm locks to 1/8 bar grid.

**`05_climax/`** — Explosive tutti: 72-note chord played as rapid pizzicato/Bartok attacks (~20ms spacing) with occasional high sine tones. Unmetered, maximally dense. Light reverb creates tight, aggressive space.

**`06_scratch/`** — Brief punctuation: two overlapping crushed crescendos with low sine fundamental, ending with single bass pizzicato. Functions as breath before final section.

**`07_bursts/`** — Extended coda (~50 seconds, quantized to bar grid). Segmented/rearranged string attacks and sine bursts. Duration units gradually expand from short (1/8 bar) to long (5/4 bars). Chord density fixed at 6 notes; reverb wetness increases dramatically, creating decay into space.

**`main.bell`** — Interleaves glitch and polyrhythm sections (sorted by increasing length), then chains loops → trail → scratch → climax (overlapping 1/4 into trail) → bursts. Bass sine reinforces transition into trail. Dynamic compression, arctan saturation, normalization.
