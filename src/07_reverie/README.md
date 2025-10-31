# Track 07: **reverie**

## Musical Output

**Duration:** ~5 minutes

A dreamlike meditation built on an 11:8 frequency ratio (augmented fourth) using an extended just-intonation lattice spanning 2, 3, 5, 7, 11, 13, and 17 limits. The piece unfolds in three phases: a slowly accumulating accordion/bass drone that's time-stretched 8×, a densely layered piano/plucked foreground with extensive granular processing, and a metrically driven section at 85 BPM that samples and recontextualizes the stretched material before returning to the ethereal opening texture.

---

## Structure

**Tuning System** — Complex just-intonation lattice generating ~30 pitch classes with microtonal deviations. Octave range (64 notes) quantized to this collection, then sorted by proximity to D5 for voice-leading logic.

**`01_background/`** — 25-second foundational layer. 64 notes cycle from lowest (bass) to highest with overlapping entrances, creating gradual spectral accumulation. Accordion samples with velocity-dependent articulation choices (dim/back/regular at low dynamics; staccato/sforzando added above 60). Peak density at 1/3 duration point controlled by overlap factor (1×→8×→1×). Occasional reversals. Individual voices pan-modulate. Bass voice includes reversed sforzando crescendo and final staccato attack. Entire layer then time-stretched 8× via rubberband algorithm with smoothing, creating 200-second drone foundation.

**`02_piano/`** — Dense foreground spanning stretched background's first 2/3. Five gesture types weighted by temporal position:

- **Chord** — Piano/plucked simultaneities (25%→100% of available pitches) with arpeggiated onsets. Velocity 0→127. Bell-like sine tone probability 25%→75%.
- **Trill** — Rapid alternations between 1-4 adjacent pitches with tempo ramping (50-100ms → variable → return). Irregular acceleration/deceleration curves.
- **Blurb** — Random-walk sequences (step size 1→5) with clustered attacks. Pattern length 25%→100% of maximum. Subdivided into chord groupings.
- **Pattern** — Cyclic melodic cells (2-4 steps) repeated with time-ramping. Folded addressing for circular pitch navigation.

Processing Functions (probability 15%→66%):

- **Freeze** — Granular time-stretching with multiple detuning (0→±2 octaves), envelope shapes (linear/reverse/Hann), spatial drift
- **Granulate** — Scattered 90-200ms grains with variable read speed/position
- **Stretch** — Rubberband 1.1× to 8× (or 10000/duration, whichever lower)
- **RandEnvelope** — Random amplitude breakpoints
- **Stutter** — Time-ramped repetitions with detuning

Additional 25%→75% probability of octave-transposed sine "bell" tones (1-4 voices) accompanying each event. Gap insertion probability: 100%→0%→100%. Event durations: 1-5 seconds × (1.0→0.5→1.0).

**`03_premerge/`** — Combines stretched background (0.85 gain) with piano layer. Large reverb (room 0.97, wet 0.015), 2-second exponential fadeout.

**`04_beat/`** — 16-bar metric section (85 BPM, 4/4). Reads compressed region of premerge (from peak backward ~4.5 bars, compressed 0.25× spatially). Three rhythmic cells ([1/8 1/16 1/16], [1/24 ×3], [5/16 3/16]) scrambled internally and cycled through 16 bars. Each attack: background segment + bass sample (sforzando/pizzicato/staccato) + sine tone, with shaped envelope (slope ±1/3), occasional reversal, and legato modulation (2×→0.25×→3×). Bass velocity 0→127→0 across middle third. Dynamics compression (2:1 ratio, -30 dB threshold). One bar pre-roll offset.

**`05_cresc/`** — Full-spectrum orchestral crescendo. All 32 pitches (bass on lowest, accordion/sax on others) time-aligned so attack peaks coincide. Individual dynamic envelopes with slight slope randomization.

**`main.bell`** — Assembly: premerge up to peak → beat section (overlaps with cresc arriving early) → premerge continuation from compressed endpoint. 3-second silent gap appended.
