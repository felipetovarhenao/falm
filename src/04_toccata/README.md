# Track 04: **toccata**

## Musical Output

**Duration:** ~5 minutes

A propulsive, metric piece built on a steady 16th-note pulse (112 BPM) that gradually intensifies toward a golden-ratio positioned climax before fragmenting and reassembling. The track uses a 12-note microtonal tuning based on a 6:5 ratio (minor third) with septimal intervals, creating a shimmering, non-standard harmonic palette. The structure follows a clear arc: continuous pulse layer with gradually expanding range and density, culminating in a dramatic peak that's subsequently deconstructed through reverse playback and granular fragmentation.

---

## Structure

**`01_pulse/`** — 5-minute continuous metric stream. 16th-notes at 112 BPM (~134ms per beat) cycle through 64-note chord quantized to 12-tone microtonal collection. Time-varying parameters (all shaped toward golden ratio climax at 61.8% through duration): voice count (1→4→1), pitch range (3 notes→full 64→64), stream length (single attacks→~37 notes→9), sample vs. sine probability, legato amount (0.5→2→0.25), reversed probability, subdivision probability, stereo spread. Samples drawn from expanding orchestration (harp/guitar → strings → winds → brass → accordion). Post-climax uses reverse cycling through pitch collection.

**`02_gliss/`** — 45 glissando gestures placed at pulse events from start to climax point. Pairs of adjacent pitches from the pulse chords connected via pitch-bending (resample operator). Parameters evolve: duration (280ms→4000ms→500ms), inter-note delay (900ms→50ms), chord pair density (3→10 pairs). String and wind families with extended techniques (flutter-tongue, bisbigliando, harmonics). Occasional amplitude windows create gated effects. Reverb wetness dramatically increases.

**`03_cresc/`** — Piano arpeggio through climax chord in reverse (low to high), accelerating from 5-beat to 1/2-beat spacing. Accompanied by synthesis: triangle wave with offset modulation at fundamental, heavily processed (gain saturation → fold → lowpass → dynamic envelope). Creates low-frequency foundational rumble.

**`04_climax/`** — Explosive simultaneity: full climax chord as rapid plucked/pizzicato attacks (~20ms spacing) with octave-doubled sine tones. Sine tones include frequency-shifted vibrato effects. Light reverb and compression for clarity.

**`05_layers/`** — Sustained brass/winds/strings crescendos and staccatos filling climax-to-end duration. Non-repeating pitch selection via urn algorithm. Notes placed on 1-4 beat grid, types selected to avoid premature peaks before section end. Bass fundamental crescendo timed to peak at section conclusion.

**`06_premix/`** — Assembly: single high piano note, then pulse + gliss (start to climax), then layers + climax + cresc (all converging at climax point with cresc arriving from before).

**`main.bell`** — Takes premix and stutters the climax: full progression up to peak, then 16 fragments of decreasing duration (2-beats→5ms, exponentially) reading backwards from peak, then continuation from peak onward. 2.5-second gap appended. Dynamic compression, envelope join for smooth gap transition.
