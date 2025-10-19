import soundfile as sf
import pyloudnorm as pyln
import os
import soundfile as sf
import numpy as np
from scipy.signal import resample_poly


def true_peak_dbtp(file_path, oversample=4):
    # Load audio
    audio, sr = sf.read(file_path)
    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)  # convert to mono for analysis

    # Oversample (zero-phase polyphase resampling)
    upsampled = resample_poly(audio, oversample, 1)

    # Compute max sample in oversampled waveform
    true_peak = np.max(np.abs(upsampled))

    # Convert to dBTP
    dbtp = 20 * np.log10(true_peak)
    return dbtp


out = ""
for f in sorted(os.listdir('./')):
    if f[0] != '0':
        continue
    file = f + '/main.wav'
    if not os.path.exists(file):
        continue

    # Load audio data from a file (e.g., a .wav file)
    data, rate = sf.read(file)

    # Create a BS.1770 loudness meter with the appropriate sample rate
    meter = pyln.Meter(rate)

    # Measure the integrated loudness in LUFS
    loudness = meter.integrated_loudness(data)
    true_peak = true_peak_dbtp(file)
    txt = f"File: {f}\n\tIntegrated Loudness: {loudness:.2f} LUFS\n\tTrue peak: {true_peak:.2f} dBTP\n"
    out = out + txt
    print(txt)

with open('./stats.txt', 'w') as f:
    f.write(out)
