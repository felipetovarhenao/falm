import os
import re
import time
import threading
from collections import OrderedDict
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer
from argparse import ArgumentParser
import sys
import random


parser = ArgumentParser(prog='FALM',
                        usage=f"{sys.executable} 01_render.py [tracks]...",
                        description="Automated rendered for Fully Automated Luxury Music in bellplay~")

parser.add_argument('tracks',
                    action='store',
                    nargs='*',
                    default='all')
parser.add_argument('--seed', action='store', default=-1, type=int)
args = parser.parse_args()

SEED = (args.seed)
if SEED == 0:
    SEED = random.randint(1, 2 ** 16)
elif SEED < 0:
    SEED = 0

SRC_ROOT = os.path.join(os.path.dirname(__file__), 'src')
DIR_TREE = OrderedDict()
SCRIPT_SEQUENCE = []
ALL_TRACKS = ['prelude',
              'serenade',
              'caprice',
              'toccata',
              'chaconne',
              'waltz',
              'reverie',
              'nocturne',
              'rondo',
              'postlude']

SELECTED_TRACKS = args.tracks
CODE_CACHE = {}


if SELECTED_TRACKS == 'all':
    SCRIPT_SEQUENCE.append(os.path.join(SRC_ROOT, 'main.bell'))
    SELECTED_TRACKS = ALL_TRACKS

if not set(ALL_TRACKS).intersection(set(SELECTED_TRACKS)):
    raise ValueError(f"Invalid tracks: {','.join(SELECTED_TRACKS)}")


def format_time(time):
    time = int(time)
    secs = time % 60
    mins = time // 60
    hours = mins // 60
    mins %= 60
    return f"{hours:2d}:{mins:2d}:{secs:2d}"


def set_seed(path: str):
    global CODE_CACHE
    global SEED
    with open(path, 'r') as f:
        txt = f.read()
    pat = r'(?<=\bsetseed\()([^;]+)(?=\);)'
    CODE_CACHE[path] = txt
    sub_txt = re.sub(pat, rf'(\g<1>) + {SEED}', txt, flags=re.DOTALL)
    with open(path, 'w') as f:
        f.write(sub_txt)


def run_files(paths,
              send_ip="127.0.0.1",
              send_port=12345,
              listen_ip="127.0.0.1",
              listen_port=12346):
    client = SimpleUDPClient(send_ip, send_port)
    done = threading.Event()

    def on_console(_, *args):
        if any("***done***" in str(a).strip() for a in args):
            done.set()

    dispatcher = Dispatcher()
    dispatcher.map("/console", on_console)

    server = ThreadingOSCUDPServer((listen_ip, listen_port), dispatcher)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    start = time.time()
    client.send_message(address='/load_file',
                        value=os.path.join(SRC_ROOT, '__imports__/utils.bell'))
    try:
        for i, path in enumerate(paths):
            set_seed(path)
            prog = int(round((i + 1) / len(paths) * 100))
            print(f"Running: {path}")
            done.clear()
            client.send_message("/load_file", str(path))
            done.wait()
            elapsed = format_time(time.time() - start)
            print(f"         [{elapsed}] DONE ({prog:3d}%)")
    finally:
        server.shutdown()
        server.server_close()
        global CODE_CACHE
        for (path, text) in zip(CODE_CACHE):
            with open(path, 'w') as f:
                f.write(text)


def path_to_title(path):
    global SRC_ROOT
    return path[(len(SRC_ROOT) + 4):].split('/')[0]


for root, folders, files in os.walk(SRC_ROOT):
    dir_name = os.path.basename(root)
    if not re.match(r'\d\d_\w+', dir_name):
        continue
    title = path_to_title(root)
    if title not in SELECTED_TRACKS:
        continue
    for file in sorted(files):
        file_name, file_ext = os.path.splitext(file)
        if file_ext != '.bell':
            continue
        file_path = os.path.join(root, file)
        SCRIPT_SEQUENCE.append(file_path)

run_files(sorted(SCRIPT_SEQUENCE))
