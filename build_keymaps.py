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


indir = '/Users/felipetovarhenao/Documents/FullSOL2020/'
keymap_dir = './keymaps/'
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

    instrument = root.split("/")[-2].lower()
    extra = re.findall(r'(?<=\+)[A-Za-z_]*', instrument)
    extra = '_' + \
        extra[0].replace("sordina", "mute").replace(
            '_', '-') if len(extra) > 0 else ''
    instrument = re.match(r'^[A-Za-z]+', instrument)[0]
    out_dir = os.path.join(keymap_dir, instrument + extra)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    filename = root.split('/')[-1]
    out_path = os.path.join(out_dir, filename + '.txt')
    organize_wav_files(root, out_path)
