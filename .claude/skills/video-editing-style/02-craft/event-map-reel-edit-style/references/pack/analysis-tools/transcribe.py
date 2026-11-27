# usage: python3 -I transcribe.py <reel_dir> [model]
import sys, numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel
D=sys.argv[1]; model=sys.argv[2] if len(sys.argv)>2 else "small"
sr,x=wavfile.read(f'{D}/data/a16.wav'); x=x.astype(np.float32)/32768.0
m=WhisperModel(model,device="cpu",compute_type="int8")
segs,info=m.transcribe(x,word_timestamps=True,vad_filter=False)
o=[f"language {info.language} p={info.language_probability:.2f} duration {len(x)/sr:.2f}s"]; nw=0
for s in segs:
    o.append(f"[{s.start:.2f}-{s.end:.2f}] {s.text.strip()}")
    o.append("   "+" | ".join(f"{w.start:.2f} {w.word.strip()}" for w in s.words)); nw+=len(s.words)
o.append(f"words {nw} | wpm over full duration {nw/(len(x)/sr)*60:.0f}")
open(f'{D}/data/transcript.txt','w').write("\n".join(o)); print("\n".join(o))
