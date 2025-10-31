# Track 10: **postlude** (_to Victoria E. Henao_)

## Musical Output

**Duration:** ~5.5 minutes

A tender, contemplative conclusion built on a 10-note just-intonation collection emphasizing septimal and undecimal intervals. The piece unfolds in three overlapping layers: a delicate introductory texture that gradually accumulates pitch material with increasing density and wetness, a lyrical melodic solo exploring glissando connections between adjacent scale degrees, and a final climactic convergence where cascading arpeggios, sustained orchestral swells, and climactic percussion unite before fading. The work serves as both emotional catharsis and structural resolution to the album's journey.

---

## Structure

**Harmonic System** — Single 10-ratio collection: `1 9/8 8/7 5/4 9/7 11/8 7/5 3/2 5/3 15/8`, rooted on D2. 64-note base spectrum quantized to these pitch classes provides complete tonal palette.

**`01_intro/`** — 48-section textural accumulation spanning ~2 minutes. Random pitch selections from quantized 64-note chord with time-varying parameters controlling emergence:

- Chord size exposed: 5 → full 64 notes (25% curve)
- Note density per section: 5 → 64 (25% curve)
- Instrumental diversity: 2 → all available (strings, winds, brass, plucked, accordion; 12.5% curve)
- Articulation variety: 2 → 13 techniques including air tones, harmonics, tremolo, bisbigliando (12.5% curve)
- Velocity: 0 → 90 (50% curve)
- Temporal gaps: 3 seconds → 750ms → 2 seconds (12.5% curves with peak at 75%)
- Onset jitter: 500ms → 100ms (12.5% curves)
- Reverb wetness: 0.025 → 0.1 (25% curve)

Each note accompanied by octave-transposed sine tone cluster (gain 0.4). Samples processed with RMS normalization to -70/-18 dB range, long sustains (minimum 2.5 seconds), exponential decay envelopes. Creates gradual emergence from silence through accumulating harmonic clarity to maximal density.

**`02_solo/`** — Lyrical wind solo (horn, sax, clarinet, trombone, flute) beginning at intro's marker 2 + 2 seconds. Spans intro's remaining duration minus global delay. Multi-voice texture (1 → 4 voices, 66% curve) with individual melodic strands:

- Random-walk sequences through pitch-class filtered chord (retaining only notes within 1 cent of target collection)
- Dyadic glissandi between adjacent pitches via resampling (slopes 50%-95% of interval)
- Phrase durations: 3 seconds → 1.5 seconds (-12.5% curve)
- Inter-phrase gaps: 5 seconds → 250ms (-12.5% curve)
- Note counts per phrase: 0% → 100% of phrase duration ÷ 100ms (5% curve)
- Velocity: 0 → 127 (25% curve)
- Technique variety: 2 → 17 articulations including stopped horn, flutter-tongue, bisbigliando, mutes (5% curve)
- Gain: 50% → 100% (12.5% curve)

Envelopes shaped as Hann windows or linear ramps with variable slopes. Occasional phase inversion for timbral variation. Voice balance via exponential scaling (1.1^(1-numvoices)). Heavy reverb (room 0.95, wet 0.05) with 5-second tail and 66% fadeout curve.

**`03_arpeggi/`** — 24-voice polyrhythmic cascade using stratified pitch regions. Chord divided into 8-note segments across its range; each voice assigned random-walk pattern (2-16 notes, step motion ±1/±2) within its segment. Optional retrograde extension for longer patterns. Hann-windowed dynamic shaping per voice. Parameters:

- Note duration unit: 70-140ms
- Time-stretching: 1× → 6× (50% curve)
- Velocity scaling: 100% → 0% (50% curve)
- Sine tone probability: 33% → 0% (50% curve)
- Total duration per voice: ~120 seconds ± 33% variation

Instrumental assignments from guitar, harp, accordion, strings, winds with technique-specific extensions (harmonics for strings/harp, tremolo for strings, microtonal inflections for winds). Samples gain-boosted with -33% compression slope. Pan positions drift across stereo field. Moderate reverb (room 0.96, wet 0.03).

**`04_sustain/`** — 16-voice sustained layer using bass register + scrambled selection from upper chord. Continuous overlapping sustains (ordinary, non-vibrato, crescendo, diminuendo, staccato when loud). Velocity 120 → 0 (50% curve), gain 100% → 10% (50% curve). Each voice cycles through samples with ~200ms overlap until reaching total duration. Gain-boosted with -12.5% slope to -40 dB minimum. DC filtering. Moderate reverb (room 0.96, wet 0.05, dry 100%).

**`05_climax/`** — 30-second orchestral climax with 4-second pre-delay. Full wind and string sections with dramatic articulations (crescendo, diminuendo, sforzando, brassy/crushed transitions, natural harmonic glissandi, tremolo). Attack spacing accelerates from 1 second to 20ms (-12.5% curve), velocity builds 0 → 127 (12.5% curve), gain 1.25% → 100% (12.5% curve). Attacks time-aligned so peak envelope occurs at climax point. Two percussion hits (mid + drawn techniques) conclude. Reverb wetness 5%.

**`main.bell`** — Assembly: intro unfolds alone until solo entry point, then arpeggi + sustain + climax layers converge at intro's final marker, with climax pre-delayed to arrive at precise culmination. Final normalization (-3 dB).
