# Track 06: **waltz**

## Musical Output

**Duration:** ~1.5 minutes

A playful, fragmented waltz in 3/4 time (60 BPM) that deconstructs traditional dance form through granular processing and stochastic transformations. Built on a 9:8 frequency ratio (major second) as its tonal center, the piece progresses through four harmonic stages: a sparse triad, a dense 11-note collection, another complex 10-note set, and finally a single unison—representing a journey from simplicity through complexity back to fundamental unity. Each phrase combines melodic gestures, chordal attacks, and arpeggios with extensive audio manipulation creating a shimmering, kaleidoscopic texture.

---

## Structure

**Harmonic Progression** — Four collections interpolated over ~20 phrases: [1 6/5 3/2] → [1 9/8 6/5 7/6 4/3 11/8 7/5 21/16 3/2 7/4 16/9] → [1 9/8 8/7 16/13 4/3 16/11 3/2 256/169 27/16 32/17] → [1]. Interpolation creates smooth transitions between adjacent collections. Each collection spawns 4 events using bar-fraction durations (1/4, 1/8, 3/8).

**Event Types** — Three gesture functions selected randomly:

- **Chirp** — Rapid scalar runs (2-6 notes) through upper register using random-walk motion. Woodwinds/accordion (staccato, ordinary, sforzando) with optional FM synthesis mixing. Time-ramped durations with single elongated tail note.

- **Chord** — Upper-register simultaneities (5-12 notes) with arpeggiated onsets (~20ms spacing). Plucked/string/accordion samples (pizzicato, staccato, harmonics, keys) plus FM synthesis. Individual decay envelopes.

- **Arpeggio** — Sequential patterns (2-10 notes) from mid-upper register. Plucked strings (harmonics, ordinary) or wind key clicks, mixed with piano. Time-ramped with variable acceleration/deceleration.

**Thump Layer** — Bass punctuation on 3/8 bar grid throughout duration. Low sine tones (velocity ~30) plus bass/cello pizzicato and occasional body percussion. Creates metric foundation.

**Processing Functions** — 80% probability of applying one transformation to each sound:

- **Granulate** — 50-200ms grains with time-varying read position, gain envelope, and speed. Mixes sample grains with sine tones at harmonic octaves.
- **Stutter** — 2-N repetitions with curved temporal distribution, independent read positions.
- **RandEnvelope** — Random breakpoint amplitude envelopes (minimum 90ms step size).
- **Freeze** — Granular time-stretching with Hann-windowed grains, bidirectional reading.
- **Stretch** — Rubberband time-stretching (1.1× to 4000/duration, max ×8).

All processed sounds normalized (-24 dB RMS), arctan saturation, gain-boosted to -18/-3 dB range.

**Coda** — Two final sustained tones: viola harmonic tremolo and harp harmonic on highest chord tone, with slow decays.

**Post-processing** — Moderate reverb (room size 0.75, wetness 0.0125), 2.5-second fadeout tail.
