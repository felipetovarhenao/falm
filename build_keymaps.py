import os
import re
import shutil
from collections import defaultdict
from argparse import ArgumentParser


def organize_wav_files(folder_path, output_file):
    # Dictionary to hold pitch groups and dynamic levels
    pitch_data = defaultdict(lambda: defaultdict(list))

    # Dynamic level mapping
    dynamic_map = {"ff": 127, "f": 127, "mf": 64,
                   "mp": 64, "p": 0, "pp": 0, "N": 64}

    # Regex to parse pitch, dynamic level, and other details
    pattern = re.compile(r"([A-G#b]+\d+)-(f{1,2}|mf|mp|p{1,2}|N)-")

    # Iterate over all files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                match = pattern.search(file)
                if match:
                    pitch, dynamic = match.groups()
                    # Adjust the pitch to an octave higher
                    pitch_letter = pitch[:-1]
                    pitch_octave = int(pitch[-1]) + 1
                    adjusted_pitch = f"{pitch_letter}{pitch_octave}"

                    # Add file to the appropriate group
                    pitch_data[adjusted_pitch][dynamic_map[dynamic]].append(
                        file_path)
    if not pitch_data:
        return
    # Write the organized data to the output file
    with open(output_file, "w") as f:
        for pitch, dynamics in sorted(pitch_data.items()):
            f.write(f"[ {pitch}\n")
            if len(dynamics) == 1:  # If only one dynamic level, skip nesting
                for files in dynamics.values():
                    for file_path in files:
                        f.write(f"\t{file_path}\n")
            else:
                for dynamic_level, files in sorted(dynamics.items(), reverse=True):
                    f.write(f"\t[ {dynamic_level} \n")
                    # Sort files to handle duplicates deterministically
                    for file_path in sorted(files):
                        f.write(f"\t\t{file_path}\n")
                    f.write("\t]\n")
            f.write("]\n")


BELL_CODE = """
KEYMAP_CACHE = null;
sol = (
    $name = 'guitar', 
    $type = 'ord', 
    $pitch = 6000, 
    $duration = 1000, 
    $velocity = 64, 
    $resample = 1, 
    $useseed = 1 -> (
        $path = $name + '/' + $type;
        $keymap = KEYMAP_CACHE.$path;
        if $keymap == null then (
            $keymap = read(
                './keymaps/' + $path + '.txt' 
            );
            if $keymap != null then KEYMAP_CACHE _= [$name $keymap] 
        );
        ezsampler(
            @pitch $pitch
            @duration $duration
            @velocity $velocity
            @keymap $keymap
            @resample $resample
            @useseed $useseed
        ) 
    ) 
)"""


def abbreviate(str: str):
    for swap in [
        [r'ordinario', 'ord'],
        [r'pizzicato', 'pizz'],
        [r'staccato', 'stacc'],
        [r'sforzato', 'sfz'],
        [r'flatterzunge', 'flz'],
        [r'violoncello', 'cello'],
        [r'crescendo', 'cresc'],
        [r'^bass$', 'tuba'],
        [r'contrabass', 'bass'],
        [r'sul_ponticello', 'pont'],
        [r'sul_tasto', 'tasto'],
        [r'trumpet', 'tpt'],
        [r'sordina', 'mute'],
        [r'tremolo', 'trem'],
        [r'mute_piombo', 'piombo'],
        [r'mute_cup', 'cup'],
        [r'mute_straight', 'straight'],
        [r'mute_harmon', 'harmon'],
        [r'stopped', 'stop'],
        [r'mute_wah', 'wah'],
        [r'aeolian', 'air'],
        [r'battuto', 'bat'],
        [r'bisbigliando', 'bisb'],
        [r'maj_seventh', 'M7'],
        [r'min_second', 'm2'],
        [r'glissando', 'gliss'],
        [r'high_register', 'high'],
        [r'multiphonics', 'multi'],
        [r'discolored', 'alt'],
        [r'major_second', 'M2'],
        [r'accordion', 'acc'],
        [r'bellowshake', 'shake'],
        [r'fifth', 'P5'],
        [r'_unison', ''],
        [r'minor_second', 'm2'],
        [r'exploding', 'exp'],
        [r'play_and_sing', 'sing'],
        [r'whistle_tones', 'whistle'],
        [r'combination_of_registers', 'reg'],
        [r'artificial_harmonic', 'harm'],
        [r'col_legno', 'legno'],
        [r'non_vibrato', 'nonvib'],
        [r'note_lasting', 'ten'],
        [r'blow_without_reed', 'noreed'],
        [r'gliss_with_throat', 'gliss'],
        [r'vibrato', 'vib'],
        [r'harmonic_fingering', 'harm'],
        [r'pizz_bartok', 'bartok'],
        [r'buzzing', 'buzz'],
        [r'pedal', 'ped'],
        [r'harmonic', 'harm'],
        [r'xylophonic', 'xylo'],
        [r'key_click', 'keyclick'],
        [r'pizz_l_vib', 'pizz'],
    ]:
        str = re.sub(swap[0], swap[1], str)

    return str


def define_function(name: str, default_type: str):
    global BELL_CODE
    BELL_CODE += f""";
{name} = (
    $pitch = 6000,
    $duration = 1000,
    $velocity = 64,
    $useseed = 1,
    $usecache = 1,
    $type = '{default_type}' -> (
        sol(
            @name '{name}'
            @pitch $pitch
            @duration $duration
            @velocity $velocity
            @useseed $useseed
            @usecache $usecache
            @type $type
        )
    )
)"""


indir = '/Users/felipetovarhenao/Documents/FullSOL2020/'
keymap_dir = './keymaps/'
instruments = []
if os.path.exists(keymap_dir):
    shutil.rmtree(keymap_dir)
for root, dirs, files in os.walk(indir):
    if not files:
        continue
    is_audio_folder = False
    for f in files:
        if os.path.splitext(f)[1] == '.wav':
            is_audio_folder = True
            break
    if not is_audio_folder:
        continue

    filename = root.split('/')[-1]
    filename = abbreviate(filename)
    instrument = root.split("/")[-2].lower()
    extra = re.findall(r'(?<=\+)[A-Za-z_]*', instrument)
    extra = '+' + abbreviate(extra[0]) if len(extra) > 0 else ''
    technique = filename
    filename += extra
    instrument = abbreviate(re.match(r'^[A-Za-z]+', instrument)[0])
    if instrument not in instruments and filename in ['ord', 'stacc', 'pizz']:
        instruments.append(instrument)
        define_function(instrument, filename)

    out_dir = os.path.join(keymap_dir, instrument)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename + '.txt')
    organize_wav_files(root, out_path)

with open("./sol.bell", 'w') as f:
    f.write(BELL_CODE)
