# Track 09: **rondo**

## Musical Output

**Duration:** ~3.5 minutes

A spirited, accelerating perpetual motion piece built on a seven-tone modal rotation system. The track employs a rondo-like structure where a recurring rhythmic "riff" returns with increasing textural complexity across eight iterations, each lasting progressively shorter durations as the underlying harmonic collection rotates through modal transpositions. Built on a 7:10 frequency ratio (tritone) as its tonal center, the piece grows from sparse plucked arpeggios through layered polyrhythmic ostinatos, staccato brass punctuations, granular clouds, and cascading scalar runs before dissolving into granular fragments. The work demonstrates additive orchestration: each return of the riff accumulates new instrumental layers until reaching maximum density, then deconstructs through metric fragmentation.

---

## Structure

**Harmonic Framework** (`00_sequence/`)\*\* — Eight sections with progressively smaller chord sizes (60→2→3→4→5→6→16→45 pitches, controlled by seed values). Seven-ratio collection [1 9/8 5/4 7/5 3/2 5/3 13/7 2] rotates by increments of (chordsize-1)×4 steps for each section, creating modal shifts. Within each section: chords paired as dyadic glissandi, organized as overlapping voice-leading progressions. Each note specifies pitch, duration, velocity, instrument/technique, and pitch-bending envelope (glissando slope ±1/3 to ±6/7). Base duration unit: 175ms.

**`01_riff/`** — Primary cyclical layer, eight iterations with additive instrumentation:

- **Strings** — Core glissando texture. Four repetitions of each section's chord progression, with pitch-bending resampling and high-pass filtering (1/3 fundamental frequency). Stutter probability increases (0%→20%), creating fragmented repetitions with variable subdivisions (3→12) and octave detuning (0→±1 octave). Processed with RMS normalization (-14 dB).

- **Perc** (sections 2-8) — Body percussion/behind-frog attacks on off-beats. Subdivisions increase with section number (max 1→4 divisions per beat). Multiple repetitions per unit with detuning. Light reverb.

- **Downbeat** (sections 2-8) — Bass pizzicato + sub-octave sine fundamental on first beat of each chord change. Attack synchronized to chord onsets.

- **Bass** (sections 4-8) — Low pizzicato/pizz-secco attacks on loudest chords in progression (filtered by mean note velocity). Number of attacks increases 0%→100% across range.

- **Sines** (sections 3-8) — Octave-transposed sine tones (1-6× fundamental) with amplitude tremolo modulation. Ring time increases (1×→3×), mix increases (50%→90%), density increases (25%→100%). Spatial panning based on pitch. Reverb with dry reduction (room 0.75, wet 0.015, dry 0.33).

- **Brass** (sections 5-8) — Staccato saxophone/trumpet/trombone offbeat attacks plus maracas. Subdivisions (1→2 per beat), chord density (2→5 notes). Synchronized to metric grid defined by unit subdivisions.

**`02_gap/`** (section 8 transition) — 1.5-second reversed percussion cascade. High plucked/string body hits with occasional reversed crushed-to-ordinary crescendos. Minimal reverb (room 0.9, wet 0.001).

**`03_bell/`** (sections 5-8) — Detuned guitar "bell" tones (behind-frog technique). Number of attacks inversely proportional to section ID (4→1 tones). Cents-based detuning mapped to harmonic collection. Beat duration: 1.5× unit. Increasing reverb wetness (0.0025→0.0125).

**`04_strum/`** (sections 2-8) — Arpeggiated chords with glissandi plus granular freezing. Wind layer probability increases (0%→100%): reversed flutter-tongue/bisbigliando sustains. Bass drum synthesis: cycle wave fundamental + body percussion knocks, with increasing subdivision (2× to 1/2× unit). Piano/plucked samples with spatial pan modulation and pitch glissandi. Duration contracts with section number.

**`05_blast/`** (sections 7-8) — Sustained brass/string sforzandos and crushed-to-ordinary attacks spanning full duration. Frequency-shifted (±2-12 Hz with vibrato envelopes), 50% reversed. Aggressive reverb processing (room 0.9, wet 0.0125).

**`06_arpeggi/`** (sections 4-8) — Polyrhythmic plucked/pizzicato arpeggios. Voice count increases (2→5), sine tone probability (10%→100%). Random-walk sequences (2-5 notes, step ±1/2) cycling through subdivisions (3÷3 to 7÷3 of unit). Brass staccato chords introduce each section. Moderate reverb (room 0.5, wet 0.0125).

**`07_run/`** (sections 3-8) — Reversed scalar cascades. Notes grouped (1→4 overlapping), then reversed temporally. Glissando resampling between adjacent pitches. Pitch-bending slopes and maximum note count decrease (12→8). Double-reverb: initial reverse pass, then forward pass with fadeout. Extreme normalization (-9 dB).

**`08_doppel/`** (sections 6-8) — Sparse metric layer with bass pizzicato alternating with body percussion, plus high key clicks/slaps with octave-transposed sine fundamentals and pitch-bending. Four notes per chord, varied metric subdivisions. Minimal reverb (room 0.98, wet 0.0015).

**`09_dissolve/`** — Final granular deconstruction of section 8 riff. Eight repetitions with increasing fragmentation: samples segmented at unit boundaries, temporal scrambling every 1/4 period, contracting time (speed 100%→33%→100%), shortening legato (100%→5%), fluctuating gain. Slope shifts from forward decay (0.99) to reverse crescendo (-0.5). 2-second gap appended.

**`main.bell`** — Layers assembled in reverse folder order (doppel → run → arpeggi → blast → strum → bell → gap → riff) for each of 8 sections, creating cumulative additive texture. Strum layer offset by pre-roll amount. Final dissolve layer appended. 2.5-second silent gap.
