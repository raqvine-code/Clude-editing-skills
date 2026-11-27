import sys, numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel
sr, x = wavfile.read(sys.argv[1]); x = x.astype(np.float32)/32768.0
m = WhisperModel("base.en", device="cpu", compute_type="int8")
segs, info = m.transcribe(x, word_timestamps=True, vad_filter=False)
for s in segs:
    print(f"[{s.start:.2f}-{s.end:.2f}] {s.text}")
    print("   " + " | ".join(f"{w.start:.2f} {w.word.strip()}" for w in s.words))
