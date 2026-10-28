# _Fully Automated Luxury Music_

![artwork](https://d2cq0goacowtde.cloudfront.net/falm/artwork.jpg)

[Listen/Purchase](https://deadlandrecords.bandcamp.com/album/fully-automated-luxury-music) | [Web Player](https://fullyautomatedluxurymusic.com)

## About

**Fully Automated Luxury Music** (**F.A.L.M**) is an open-source, [generative music](https://en.wikipedia.org/wiki/Generative_music) album. The music is entirely generated through [stochastic](https://en.wikipedia.org/wiki/Stochastic) algorithms—probabilistic, rule-based processes designed to produce finely structured yet potentially infinite variants of a musical output, in the form of audio files. All generative scripts in this repository are written in the [_bell_](https://felipe-tovar-henao.com/bell-tutorials) programming language and meant to be run in [_bellplay~_](https://bellplay.net), an offline algorithmic audio software and framework I started developing in 2024. The codebase is end-to-end (E2E), meaning it generates and assembles the entire album from scratch by running the scripts in the proper order, without need or expectation of any human editing—in other words, it's a fully reproducible and parameterized work.

This album serves primarily as a proof of concept for _open-source music_—a still recent and underexplored compositional practice (see, for instance, Pierre Cusa AKA _Pure Code_'s [_Ambient Garden Album_](https://github.com/pac-dev/AmbientGardenAlbum))—and as a reflection on recent developments in AI and automation, what they mean for the future of creative labor, and whether human expression can be embeddeded in, and formalized through computer algorithms. The title is a wink and nod to Aaron Bastani's popular book [_Fully Automated Luxury Communism: A Manifesto_](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism), which offers a cautiously optimistic, though increasingly unlikely, utopian vision of technology's impacts on society.

**Fully Automated Luxury Music** was written and developed between May and October of 2025, in Chicago, Cincinnati, and Gainesville, USA.

### Listen

You can listen to a mastered version of _Fully Automated Luxury Music_ [here](https://deadlandrecords.bandcamp.com/album/fully-automated-luxury-music).

Alternatively, you can listen to different versions of the album at [fullyautomatedluxurymusic.com](https://fullyautomatedluxurymusic.com)

### Track listing

| #   | Title                              | Source code directory                |
| --- | ---------------------------------- | ------------------------------------ |
| 1.  | **prelude** (_in memoriam malugo_) | [`src/01_prelude`](src/01_prelude)   |
| 2.  | **serenade**                       | [`src/02_serenade`](src/02_serenade) |
| 3.  | **caprice**                        | [`src/03_caprice`](src/03_capprice)  |
| 4.  | **toccata**                        | [`src/04_toccata`](src/04_toccata)   |
| 5.  | **chaconne**                       | [`src/05_chaconne`](src/05_chaconne) |
| 6.  | **waltz**                          | [`src/06_waltz`](src/06_waltz)       |
| 7.  | **reverie**                        | [`src/07_reverie`](src/07_reverie)   |
| 8.  | **nocturne**                       | [`src/08_nocturne`](src/08_nocturne) |
| 9.  | **rondo**                          | [`src/09_rondo`](src/09_rondo)       |
| 10. | **postlude** (_to my mother_)      | [`src/10_postlude`](src/10_postlude) |

## Requirements

In addition to some basic familiary with [_bell_ programming](https://felipe-tovar-henao.com/bell-tutorials) and [shell commands](https://www.tutorialspoint.com/unix/index.htm), the following resources are required:

### Software

- _Python~_ v3.12 or higher [[download](https://www.python.org/downloads/release/python-31216/)]: Used for setting up the working environment.
- _bellplay~_ v0.3.0-beta [[download](https://github.com/felipetovarhenao/bellplay/releases/tag/v0.3.0-beta)]: Used for generating and assembling the audio output.
- _Visual Studio Code_ [[download](https://code.visualstudio.com/)]: Used for editing the code.
  - _bellplay~ plugin extension_ [[download](https://marketplace.visualstudio.com/items?itemName=tovarhenao.bellplay-plugin)]: Improves the user experience for working on _bellplay~_ scripts.
- _Ableton Live 12 Standard or Suite (Free trial works)_ [[download](https://www.ableton.com/en/live/)]: Used specifically to create a _bellplay~_-friendly version of the _Grand Piano_ sampler.

### Data

1. Download [_FullSOL_](https://forum.ircam.fr/projects/detail/fullsol/) dataset (~20 GB of instrumental audio samples) from IRCAM forum.

   > **NOTE**: Requires _Premium_ subscription to IRCAM forum.

2. Download [_Orchidea tam tam_](https://www.orch-idea.org/data/db/Orchidea_tam_tam_0.6.zip) dataset from Orchidea's website (free).

## Setup

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Auto-generate _bellplay~_ dependencies:

   ```zsh
   python3 00_setup.py <path-to-FullSOL-dataset> <path-to-Orchidea-tam-tam-dataset>
   ```

   The _bellplay~_ source code for _Fully Automated Luxury Music_ relies almost entirely on the [IRCAM](https://www.ircam.fr/en)'s _FullSOL_ dataset as the main audio source. As such, a [Python script](00_setup.py) is included which automatically generates dependencies for the code to run properly. This includes keymaps (`.txt` files used in _bellplay~_ for designing custom samplers) as well as `.bell` files with global _bell_ function definitions that are extensively used across different scripts for sampling from _FullSOL_.

   This should generate a new folder called `src/__data__/` with multiple subfolders, one for each instrument in _FullSOL_ and _Orchidea tam tam_, each subfolder containing `.txt` files with the keymap specification for the different instrumental techniques available for that instrument. To learn more about keymaps in _bellplay~_, read [this](https://bellplay.net/docs/learning/tutorials/sampling).

3. In addition to the _FullSOL_-based keymaps, two additional keymaps need to be generated. The first keymap is for Ableton Live's [_Grand Piano_](https://www.ableton.com/en/packs/grand-piano/), which is available in _Standard_ and _Suite_ licenses. To generate it, run the [`piano.bell`](src/__imports__/piano.bell) script in _bellplay~_.

   > NOTE: You may need to may need to manually change the first line in [`piano.bell`](src/__imports__/piano.bell) to match path to the Ableton's _Grand Piano_ directory in your computer.

   ```py
   $pianopath = '/Applications/Ableton Live 12 Suite.app/Contents/App-Resources/Core Library/Samples/Multisamples/Grand Piano';
   ```

4. The second keymap is for maracas samples, which can be easily generated by running [`maracas.bell`](src/__imports__/maracas.bell) in _bellplay~_.

5. Finally, the following two files should be added to the _Default imports_ list in _bellplay~_'s `Settings/Library`:
   - [`sol.bell`](src/__imports__/sol.bell) (auto-generated by [Python script](keymap_generator.bell))
   - [`utils.bell`](src/__imports__/utils.bell)

   This step is important, as it ensures that _bellplay~_ automatically runs these scripts at launch, thus making the functions defined within available to any scripts subsequently run during the session.

   All scripts within [`src/__imports__/`](src/__imports__/) should be left unedited as they serve as the backbone of how the scripts in this repo work (mostly global functions and variables).

## Rendering

### Option 1: Python

The simplest way to render _F.A.L.M_ into audio is via the [`01_render.py`](01_render.py) Python script.

> Before running this script, make sure to first open _bellplay~_

To generate the full album, run:

```py
python 01_render.py
```

To generate specific tracks, you can provide one or more track titles. For instance, to only generate `waltz` and `caprice`, you can run:

```py
python 01_render.py waltz caprice
```

To generate variations of the album, you can provide a random seed. If seed is `0`, the seed will be chosen at random; if the seed is `-1` (_default_) no seed will be applied.

```py
python 01_render.py rondo --seed 2
```

### Option 2: bellplay~

For more fine-grained modification, you can of course directly modify and run the _bellplay_ scripts, which can be found in [`src/`](src).

The tree-like, hierarchical structure of the `src/` directory loosely mirrors that of the album, whereby each folder corresponds to a different track, and these in turn are further organized into subfolders containing scripts to generate its constituent parts. All nested folders' names have a prefix (e.g., `00_`, `01_`, ...) specifying the order in which they are meant to be executed. Running them in the incorrect order may result in errors, since some scripts generate dependency files that influence the behavior of subsequent scripts. As such, the album would need to be generated in a bottom-up, step-by-step process, and not in a single shot, like the `01_render.py` script does. This allows for iterative tinkering and refining of smaller audio files or data that are gradually assembled into the full album.

Once all audio tracks have been generated, they can be combined into a single one with the top-level [`main.bell`](src/main.bell) script.

## Credits & Acknowledgements

**F.A.L.M** was realized using different audio data—primarily [IRCAM](https://www.ircam.fr/)'s [FullSOL dataset](https://forum.ircam.fr/projects/detail/fullsol/), and to a lesser extent the the [_Grand Piano_](https://www.ableton.com/en/packs/grand-piano/) samples in [_Ableton Live_](https://www.ableton.com/en/), as well as a maracas samples available via [_Epidemic Sound_](https://www.epidemicsound.com/).

Thanks to [Deadland Records](https://deadlandrecords.bandcamp.com/) for distributing and the official album release.

## License

The code for **Fully Automated Luxury Music** is distributed under the terms of the GNU General Public License version 3 ([GPL-v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)).
