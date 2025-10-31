# Track 05: **chaconne**

## Musical Output

**Duration:** ~6 minutes

A continuously evolving passacaglia built on a cyclical harmonic progression that modulates through six chords. The piece begins sparsely with plucked textures, gradually accumulating layers of woodwind tremolos, melodic fragments, granular clouds, and frozen piano resonances before reaching a sustained climax at 70% through its duration. The second half fragments and stutters the accumulated material, creating a glitchy dissolution that's eventually reassembled through a gradual fade-in process overlaid with descending arpeggios.

---

## Structure

**Harmonic Framework** — Six just-intonation chords cycle with modulating roots: [1 6/5 3/2 9/8], [1 5/4 3/2 7/4], [1 6/5 3/2 4/3], [1 5/4 3/2 7/4], [1 5/4 3/2 15/8], [1 5/4 3/2 7/4]. Root shifts by ratios: 32/21, 2/3, 8/9, 21/16, 3/4, 10/9. Harmony updates either every 6 events or after 2.25 seconds. Full 23-note chord quantized to current collection.

**`01_foreground/`** — Main generative layer using four gesture types weighted differently across structure: (1) **Arpeggi** — subdivided patterns (1/16, 1/20, 1/12 bar) with woodwinds/accordion, occasional granulation; (2) **TremChord** — amplitude-modulated woodwinds with high-octave oscillators creating tremolo effects, evolving envelope shapes; (3) **Melody** — stepwise melodic lines with pitch-bending glissandi (flute/sax), low bass punctuation, frequent granulation and stuttering; (4) **Pluck** — harp/guitar harmonics in randomized dyadic patterns, occasional granulation/stuttering. Event durations drawn from fractional bar subdivisions (1/8 to full bar). Chord density increases from 7 to 23 notes. Occasional percussive gaps insert slap-tongue, key clicks, pizzicato. Dynamic range tightens toward climax (-24→-3 dB). Piano roll accompaniment with frozen grain clouds throughout.

**`02_percussion/`** — Metric layer synchronized to foreground's harmonic onsets up to climax. 12-step velocity pattern (scaled 1-127) and pitch selection pattern cycle through foreground chords. Maracas plus sampled percussion (body hits, slap-tongue, key clicks, Bartók pizzicato). Frequency-shifting probability increases. Synthesis: descending glissando cycles on high-velocity attacks. Final bass Bartók pizzicato.

**`03_leadup/`** — 20-bar accelerating buildup to climax. Body percussion and key clicks from plucked/string families, crescendoing from velocity 20→127. Overlaid reversed string/plucked sustains reading backward through duration. Heavy bass synthesis: rectangle wave modulation with amplitude envelope, spatial panning motion.

**`04_glide/`** — 13-event coda sequence using final-cycle chord. Decelerating tempos (150→90 BPM), diminishing velocities (127→1), expanding durations (3-7 seconds). Each event: percussive attacks with random-walk pitch sequences, continuous arpeggios with slight acceleration, piano roll + sine tones, granular freezing.

**`05_bridge/`** — 7-bar transition featuring multi-voice random-walk patterns ("swirls") with woodwinds, accelerating/decelerating based on amplitude envelope direction. Bass synthesis with frequency sweep. Climactic chord cascade with pizzicato/piano/sine tones. Four time-stretched fragments of preceding material read backward with increasing grain size.

**`06_transient/`** — Brief exhale: air tones, scrapes, harmonics, crushed-to-ordinary attacks from winds/strings, reverse probability, sine wave mixing. Single bass pizzicato at peak moment.

**`07_stutter/`** — Pizzicato chord segmented (50-200ms) and scrambled in two groups: first 1-5 segments shuffled, remainder shuffled separately. Optional sine wave blending at octave transpositions.

**`08_premerge/`** — Assembly: foreground (with evolving reverb wetness) up to climax, then leadup overlaps at -0.33 gain, transient centers on climax, bridge follows. Second half of foreground mixed with percussion, then granularly stuttered: segments masked/copied based on time-varying probability (0→100→25%), with 1-4 repetitions per segment and speed modulation (1×→2×).

**`09_tile/`** — Extracts non-masked segments from premerge and overlays glide coda reading at 0.125× speed. Bass sine tone reinforces. Reverb wetness increases dramatically (0.0001→0.015).

**`main.bell`** — Concatenates premerge + tile.
