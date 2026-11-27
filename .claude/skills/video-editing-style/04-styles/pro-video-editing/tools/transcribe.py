"""Add word-level transcripts to every cached video that lacks one.
usage: ~/.local/share/whisper-venv/bin/python transcribe.py   (needs faster-whisper; model 'base', auto language)
Writes knowledge/cache/<hash>/transcript.json = {lang, segs:[{s,e,t,w:[[s,e,word]...]}]}"""
import os, json
from faster_whisper import WhisperModel
KB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "knowledge", "cache")
m = WhisperModel("base", device="cpu", compute_type="int8")
for h in sorted(os.listdir(KB)):
    d = os.path.join(KB, h)
    wav, out = os.path.join(d, "a16.wav"), os.path.join(d, "transcript.json")
    if not os.path.exists(wav) or os.path.exists(out):
        continue
    s, i = m.transcribe(wav, word_timestamps=True, vad_filter=True)
    segs = [{"s": round(x.start, 2), "e": round(x.end, 2), "t": x.text.strip(),
             "w": [[round(w.start, 2), round(w.end, 2), w.word] for w in (x.words or [])]} for x in s]
    json.dump({"lang": i.language, "segs": segs}, open(out, "w"), ensure_ascii=False)
    print(h, i.language, len(segs), "segments")
