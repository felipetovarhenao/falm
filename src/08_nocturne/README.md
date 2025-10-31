# Track 08: **nocturne**

## Musical Output

**Duration:** ~4 minutes

A nocturnal meditation unfolding in seven distinct sections that transition from sparse, breathy textures through rhythmic fragmentation to dense granular clouds before dissolving into silence. Built on a 5:6 frequency ratio (minor sixth) as its tonal center, the piece cycles through a modal progression that modulates root pitch classes while exploring complex septimal and undecimal harmonies. The work balances written-out gestural objects (key clicks, tremolos, swirls, arpeggios, rhythmic beats) with generative processes (granulation, spectral crackling), creating a narrative arc from whispered beginnings to shimmering climax to quiet dissolution.

---

## Structure

**Harmonic Framework** — Seven root pitch classes cycle through the progression, each spawning two chords with varying rational intervals. Collections emphasize septimal (7/4, 7/6, 8/7) and undecimal (11/8) harmonies alongside traditional just-intonation ratios. Final cadence: two chords, first using altered septimal collection [1 16/15 11/8 9/7 5/4 3/2 7/4 16/9], second returning to opening material. 64-note base spectrum quantized to each collection.

**`01_keyclicks/`** — Primary developmental layer spanning four subsections:

- **Pickup** (2 seconds) — Three high air tones (flute/sax/clarinet) reversed and crescendoed, with bass sine fundamental building underneath.

- **Intro** (~30 seconds) — Five gesture types cycle through harmonic progression with increasing intensity (control parameter 0→1):

  - _KeyClicks_ — Arpeggiated wind key clicks layered with pizzicato, flutter-tongue air tones, and octave-transposed sine clusters. Sustained low pizzicato foundation. Pattern stored in `init` variable for consistency.
  - _Tremolo_ — Sustained wind chords (ordinary/air) with optional amplitude modulation via oscillator multiplication (probability 50%→100%). Increasing chord density (4→8 notes).
  - _Swirl_ — Random-walk sequences with dual layers: sustained clarinet air tones + rapid harp/pizzicato attacks at varying tempos (50-300ms).
  - _Arpeggio_ — Ascending/descending/scrambled wind lines with high sine tone probability (50%→100%). Includes occasional string crushed-to-ordinary "scratch" gestures.
  - _Beats_ — Percussive brass slap-tongues and key clicks in time-ramped subdivisions (4→max subdivisions based on duration).

  Duration per event: 2.5 seconds → 1.67 seconds. Gesture sequence cycles through five types with rotation offset per chord.

- **Break** (~10 seconds) — Five-note plucked chord (harp/guitar harmonics or wind key clicks), followed by 8-second tremolo layer with increasing reverb wetness (0.015→0.25).

- **Cresc** — Eight-stage accelerating buildup. Each stage: variable subdivisions (10 seconds/12 notes → 800ms/8 notes) executing all three functions (Swirl, Tremolo, KeyClicks) simultaneously at increasing intensities.

- **Transient** — Reversed soft brush percussion crescendo + bass pizzicato attack at peak.

All keyclicks material processed with RMS normalization (-26 dB), arctan saturation, final normalization (-3 dB).

**`02_climax/`** — 70-second sustained air tone texture. Full 32-note cadential chord gradually introduced with expanding temporal spacing (50ms → 7 seconds). Air tones and non-vibrato sustains, with increasing flutter-tongue probability. 80% of attacks accompanied by octave-transposed sine tones (1-3 voices with detuning, reversed/normal). Light reverb.

**`03_sparkles/`** — 20-second decay cascade. Opens with full chord as rapid key clicks (~20ms spacing) plus two bass attacks (Bartók/pizzicato). Then: descending density of sine tone clusters (1-5 voices, octaves 1-8× fundamental) mixed with sparse key clicks. Temporal spacing 20ms → 1 second, gain 100% → 12.5%, velocity 127 → 0. Heavy reverb increases (wetness 0.025→0.05) with 5-second tail.

**`04_rall/`** — 7.9-second ritardando through seven time-stretched events using timeramp with positive slope (0.18). Each event: bass pizzicato attack (reversed crescendo + forward decay) plus upper-register scrambled attacks (keys, slaps, air tones, body hits) with negative roll offset creating anticipatory clustering. Sine tone probability 1%→100%, gain increases. Chord interpolates from first cadence collection toward second (mix 0→100%). Reversed brushed percussion crescendos at peak. Entire texture processed through double-reverb: initial reverse pass, then forward pass with increasing wetness.

**`05_granular/`** — Extended glissando texture. 16 iterations, each generating random-walk sequence (12-23 notes) through cadential chord with step motion. Dyadic pitch-bending via resample operator, optional sine tone mixing (70% probability). Segments either transcribed directly (25%) or granularly scattered (75%): 4-22 fragments with exponential decay envelope, detuning ±1 octave. Time-varying dry/wet mix envelope controls reverb balance. 4-second fadeout tail.

**`06_crackles/`** — 60-second spectral noise layer. Samples accordion, wind, and string body percussion/key clicks, segmented to 15-100ms, pitch-shifted 0-4 semitones, scattered with increasing density (5ms → 200ms spacing). Gain envelope decreases 100% → 0%. Dynamic compression (2:1 ratio, -20 dB threshold) into normalization (-9 dB).

**`main.bell`** — Assembly: keyclicks → rall → [climax (offset 2s, fading gain) + sparkles + crackles overlaid] → granular continuation. RMS normalization (-24 dB), arctan saturation, final normalization (-3 dB).
