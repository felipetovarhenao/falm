# _Fully Automated Luxury Music_

## About

**Fully Automated Luxury Music** (**F.A.L.M**) is an open-source, generative music album. The music is entirely generated through stochastic algorithms—probabilistic, rule-based processes designed to produce finely structured yet potentially infinite variants of a musical output, in the form of audio files. All generative scripts in this repository are written in the [_bell_](https://felipe-tovar-henao.com/bell-tutorials) programming language and meant to be run in [_bellplay~_](https://bellplay.net), an offline algorithmic audio software and framework I started developing in 2024. The codebase is end-to-end (E2E), meaning it generates and assembles the entire album from scratch by running the scripts in the proper order, without need or expectation of any manual editing—in other words, it's a fully reproducible and parameterized work.

This album serves primarily as a proof of concept for _open-source music_—a rather recent and unexplored compositional practice (see, for instance, Pierre Cusa AKA _Pure Code_'s [_Ambient Garden Album_](https://github.com/pac-dev/AmbientGardenAlbum))—and as a reflection on recent developments in AI automation, what they mean for the future of artistic practice, and how human expression can remain central to algorithmic design. The title is a wink and nod to Aaron Bastani's book [_Fully Automated Luxury Communism: A Manifesto_](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism), which similarly offers an optimistic, though increasingly unlikely, vision of automation's impacts on society.

### Track listing

| #   | Title                            | Source Code                          |
| --- | -------------------------------- | ------------------------------------ |
| 1.  | Élegie (_in memoriam Malugo_)    | [`01_preludio/`](/01_preludio)       |
| 2.  | Sérénade                         | [`02_serenata/`](/02_serenata)       |
| 3.  | Caprice                          | [`03_caprice/`](/03_caprice)         |
| 4.  | Promenade                        | [`04_andante/`](/04_andante)         |
| 5.  | Chaconne                         | [`08_fantasia/`](/08_fantasia)       |
| 6.  | Valse                            | [`06_intermezzo/`](/06_intermezzo)   |
| 7.  | Rêverie                          | [`07_chorale/`](/07_chorale)         |
| 8.  | Nocturne                         | [`05_nocturno/`](/05_nocturno)       |
| 9.  | Rondò                            | [`09_passacaglia/`](/09_passacaglia) |
| 10. | Épilogue (_a Victoria E. Henao_) | [`10_epilogo/`](/10_epilogo)         |

## Requirements

In addition to some basic familiary with [_bell_ programming](https://felipe-tovar-henao.com/bell-tutorials) and [shell commands](https://www.tutorialspoint.com/unix/index.htm), the following resources are required:

### Software

- _Python~_ v3.12.4 [[download](https://www.python.org/downloads/release/python-3124/)]: Used for setting up the working environment.
- _bellplay~_ v0.2.8-beta [[download](https://bellplay.net/)]: Used for generating and modifying the actual music/audio output.
- _Visual Studio Code_ [[download](https://code.visualstudio.com/)]: Used for editing the code.
  - _bellplay~ extension_ [[download](https://marketplace.visualstudio.com/items?itemName=tovarhenao.bellplay-plugin)]: Improves the user experience for working on _bellplay~_ scripts.
- _Ableton Live 12 (Standard or Suite)_ [[download](https://www.ableton.com/en/live/)]: Used by _bellplay~_ to generate piano samples.

### Data

2. Download [_FullSOL_](https://forum.ircam.fr/projects/detail/fullsol/) dataset (~20 GB of instrumental audio samples) from IRCAM forum.

   > **NOTE**: Requires _Premium_ subscription.

## Environment setup

### FullSOL integration with _bellplay~_

The _bellplay~_ source code for _Fully Automated Luxury Music_ relies almost entirely on the IRCAM's _FullSOL_ dataset as the main audio source. As such, a [Python script](/keymap_generator.py) is included which automatically generates the files necessary for the scripts to run properly. This includes keymaps (`.txt` files used in _bellplay~_ for designing custom samplers) as well as `.bell` files with global _bell_ function definitions that are extensively used across different scripts for sampling from _FullSOL_.

From the top directory of the repo, run the following command:

```zsh
python3 ./keymap_generator.py <path to FullSOL dataset>
```

This should generate a new folder called `/keymaps` with multiple subfolders, one for each instrument in _FullSOL_, each subfolder containing `.txt` files with the keymap specification for the different instrumental techniques available for that instrument. To learn more about keymaps in _bellplay~_, read [this](https://bellplay.net/docs/learning/tutorials/sampling).

### Additional keymaps

In addition to the _FullSOL_-based keymaps, two additional keymaps need to be generated.

#### Ableton Live's _Grand Piano_

The first keymap is for Ableton Live's [_Grand Piano_](https://www.ableton.com/en/packs/grand-piano/), which is available in _Standard_ and _Suite_ licenses. To generate it, run the [`piano.bell`](/__lib__/piano.bell) script.

> NOTE: You may need to may need to manually change the first line in [`piano.bell`](/__lib__/piano.bell) to match path to the Ableton's _Grand Piano_ directory in your computer. For instance, in MacOS it would look something like this:

    ```bell
    $files = readfolder('/Applications/Ableton Live 12 Suite.app/Contents/App-Resources/Core Library/Samples/Multisamples/Grand Piano');
    ```

#### Maracas keymap

The second keymap is for maracas samples, which can be easily generated by running [`maracas.bell`](/__lib__/maracas.bell).

### _bellplay~_ Library Configuration

Finally, the following two files should be added to the _Default imports_ list in _bellplay~_'s `Settings/Library`:

- [`sol.bell`](/__lib__/sol.bell) (generated by Python script)
- [`utils.bell`](/__lib__/utils.bell)

This step is important, as it ensures that _bellplay~_ automatically runs these scripts at launch, thus making the functions defined within available to any scripts subsequently run during the session.

All scripts within `/__lib__` should be left unedited as they serve the backbone (mostly global functions and variables) of how the scripts in this repo work.

## How to generate _Fully Automated Luxury Music_

## License

All content in this repository—including code, scripts, and generated audio—is licensed under [**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**](https://creativecommons.org/licenses/by-nc-sa/4.0/).

This means you are free to share and adapt this work, provided you:

- Give appropriate credit
- Do not use it for commercial purposes
- Distribute any derivative works under the same license

See the [LICENSE](LICENSE) file for full details.
