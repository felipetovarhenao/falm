import os
import re
import shutil
from collections import defaultdict


def file_id_to_pitch(file_id: int, num_files: int):
    center = 6000
    if num_files == 1:
        return center
    n = file_id / max(1, num_files - 1)
    n -= 0.5
    return str(int(round(n * 3800 + center)))


def organize_wav_files(folder_path, output_file):
    # Dictionary to hold pitch groups and dynamic levels
    pitch_data = defaultdict(lambda: defaultdict(list))

    # Dynamic level mapping
    dynamic_map = {"ff": 127, "f": 127, "mf": 64,
                   "mp": 64, "p": 0, "pp": 0, "N": 64}

    # Regex to parse pitch, dynamic level, and other details
    pattern = re.compile(
        r"([A-G#bq]+\d+|N)-([mfpN]+)-")

    # Iterate over all files in the folder
    for root, _, files in os.walk(folder_path):
        n_count = 0
        files = list(filter(lambda f: f.endswith('.wav'), files))
        num_files = len(files)
        for i, file in enumerate(files):
            file_path = os.path.join(root, file)
            match = pattern.search(file)
            if match:
                pitch, dynamic = match.groups()
                vel = dynamic_map[dynamic] if dynamic in dynamic_map else 64
                if pitch != 'N':
                    # Adjust the pitch to an octave higher
                    pitch_letter = pitch[:-1]
                    pitch_octave = int(pitch[-1]) + 1
                    adjusted_pitch = f"{pitch_letter}{pitch_octave}"

                    # Add file to the appropriate group
                    pitch_data[adjusted_pitch][vel].append(
                        file_path)
                else:
                    pitch_data[file_id_to_pitch(i, num_files)][vel].append(
                        file_path)
                    n_count += 1
            else:

                pitch_data[file_id_to_pitch(
                    i, num_files)][64].append(file_path)
                n_count += 1
    # return
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
keymap = (
    $name,
    $type -> (
        BP_FN_CHECK_ARGS('keymap', 'name', $name, 'type', $type);
        $path = $name + '/' + $type;
        $keymap = KEYMAP_CACHE.$path;
        if $keymap == null then (
            $keymap = read(
                '/Users/felipetovarhenao/Documents/bandcamp album/keymaps/' + $path + '.txt' 
            );
            if $keymap != null then KEYMAP_CACHE _= [$path $keymap] 
        );
        (KEYMAP_CACHE.$path) ||| BP_FN_ERROR('keymap', 'no matching keymap:' $name $type)
    )
);
range = (
    $name, $types = null -> (
        BP_FN_CHECK_ARGS('range', 'name', $name, 'types', $types);
        if $types == null then ($types = types($name));
        $keymap = for $t in $types collect keymap($name, $t);
        $pitches = $keymap.trans()::1;
        minmax($pitches):[1 3]
    )
);
instrument = (
    $name, $types -> (
        BP_FN_CHECK_ARGS('instrument', 'name', $name, 'types', $types);
        $fn = INSTRUMENT_MAP.$name;
        $alltypes = types($name);
        $types = if $types == null then $alltypes else intersection($alltypes, $types);
        $range = range($name, $types);
        [
            ['name' $name]
            ['fn' $fn]
            ['types' $types]
            ['range' pitch($range)]
        ]
    )
);
pitchfilter = (
    $instruments, $pitch, $tolerance = 300 -> (
        BP_FN_CHECK_ARGS('pitchfilter', 'instruments', $instruments, 'pitch', $pitch);
        $diffs = null; 
        $choices = for $x in $instruments collect (
            $range = $x.getkey('range') ||| BP_FN_ERROR("pitchfilter", "invalid instrument:" $x);
            $diff = pitchdiff($pitch, $range);
            $diffs _= $diff;
            if $pitch >= ($range:1 - $tolerance) && $pitch <= ($range:2 + $tolerance) then $x
        );
        $out = if $choices == null then (
            $id = abs($diffs).minmax()::2;
            $instruments:$id
        ) else $choices;
        $out ||| BP_FN_ERROR("pitchfilter", "null output")
    ) 
);
sol = (
    $name = 'guitar', 
    $type = 'ord', 
    $pitch = 6000, 
    $duration = 500, 
    $velocity = 64, 
    $resample = 1, 
    $useseed = 1 -> (
        BP_FN_CHECK_ARGS('sol', 'name', $name, 'type', $type, 'pitch', $pitch);
        $keymap = keymap($name, $type);
        ezsampler(
            @pitch $pitch
            @duration $duration
            @velocity $velocity
            @keymap $keymap
            @resample $resample
            @useseed $useseed
        ) 
    ) 
);
types = (
    $name -> (
        SOL_TECHNIQUES.$name
    )
)"""


def abbreviate(str: str, hyphen: bool = False):
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
        [r'bottleneck', 'slide'],
        [r'fifth', 'P5'],
        [r'jet_whistle', 'jet'],
        [r'_unison', ''],
        [r'minor_second', 'm2'],
        [r'exploding', 'exp'],
        [r'play_and_sing', 'sing'],
        [r'whistle_tones', 'whistle'],
        [r'tonguing', 'tongue'],
        [r'combination_of_registers', 'reg'],
        ['harmonics', 'harm'],
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
        [r'key_click', 'keys'],
        [r'pizz_l_vib', 'pizz'],
        [r'clarinet', 'clar'],
        [r'trombone', 'tromb'],
        [r'_with_', '_w_'],
        [r'near_the_', 'near_'],
        [r'difference', 'diff'],
        [r'tap_on_body', 'tap'],
        [r'chromatic_scale', 'chrom'],
        [r'glissandi', 'gliss'],
        [r'natural', 'nat'],
        [r'behind_the', 'behind'],
        [r'on_the', 'on'],
        [r'tuning_pegs', 'pegs'],
        [r'tailpiece', 'tail'],
        [r'rasguado', 'rasg'],
        [r'drum_effect', 'perc'],
        [r'fingertips', 'finger'],
        [r'fingering', 'finger'],
        [r'fingerboard', 'board'],
        [r'increasing', 'asc'],
        [r'vocalize', 'vocal'],
        [r'closed', 'close'],
        [r'percussion', 'perc'],
        [r'embouchure', 'emb'],
        [r'_into_instrument', ''],
        [r'legato', 'leg'],
        [r'pitched', 'pitch'],
        [r'backwards', 'back'],
        [r'decresc', 'dim'],
        [r'quartertones', 'micro'],
        [r'middle', 'mid'],
        [r'filtered', 'filter'],
        [r'sweeping', 'sweep'],
        [r'double_bass_bow', 'bow'],
        [r'superball', 'ball'],
        [r'scraping', 'scrape'],
        [r'damped', 'damp'],
    ]:
        str = re.sub(swap[0], swap[1], str)
    if hyphen:
        str = str.replace("_", '-')
    return str


def define_function(name: str, default_type: str):
    global BELL_CODE
    BELL_CODE += f""";
{name} = (
    $pitch = 6000,
    $duration = 500,
    $velocity = 64,
    $useseed = 1,
    $usecache = 1,
    $resample = 1,
    $type = '{default_type}' -> (
        sol(
            @name '{name}'
            @pitch $pitch
            @duration $duration
            @velocity $velocity
            @useseed $useseed
            @usecache $usecache
            @resample $resample
            @type $type
        )
    )
)"""


indir = '/Users/felipetovarhenao/Documents/FullSOL2020/'
keymap_dir = './keymaps/'
instruments = []
if os.path.exists(keymap_dir):
    shutil.rmtree(keymap_dir)
instrument_dict = {}
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
    filename = abbreviate(filename, True)
    instrument = root.split("/")[-2].lower()
    if "Percussion" in root:
        instrument = 'perc'
    extra = re.findall(r'(?<=\+)[A-Za-z_]*', instrument)
    extra = '+' + abbreviate(extra[0], True) if len(extra) > 0 else ''
    technique = filename
    filename += extra
    instrument = abbreviate(re.match(r'^[A-Za-z]+', instrument)[0])
    if instrument not in instrument_dict:
        instrument_dict[instrument] = []
    instrument_dict[instrument].append(filename)

    out_dir = os.path.join(keymap_dir, instrument)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename + '.txt')
    organize_wav_files(root, out_path)


for instrument in instrument_dict.keys():
    techniques = instrument_dict[instrument]
    found = False

    for technique in ['stacc', 'ord', 'pizz']:
        if technique in techniques:
            define_function(instrument, technique)
            found = True
            break
    if not found:
        define_function(instrument, techniques[0])

BELL_CODE += ''';
SOL_TECHNIQUES = (
'''
for instrument in instrument_dict.keys():
    BELL_CODE += f"    ['{instrument}' {" ".join([f"'{t}'"for t in instrument_dict[instrument]])}]\n"

BELL_CODE += ')'

BELL_CODE += ''';
INSTRUMENT_MAP = (
'''
for instrument in instrument_dict.keys():
    BELL_CODE += f"    ['{instrument}' {instrument}]\n"

BELL_CODE += ')'

with open("./sol.bell", 'w') as f:
    f.write(BELL_CODE)
