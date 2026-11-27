"""transcribe_one.py <wav> <out.json> [model=small] [lang]  (run with the whisper venv python)"""
import sys, json
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[3] if len(sys.argv) > 3 else 'small', device='cpu', compute_type='int8', cpu_threads=4)
s, i = m.transcribe(sys.argv[1], language=sys.argv[4] if len(sys.argv) > 4 else None, word_timestamps=True, vad_filter=True)
segs = [{'s': round(x.start, 2), 'e': round(x.end, 2), 't': x.text.strip(), 'w': [[round(w.start, 2), round(w.end, 2), w.word.strip()] for w in x.words]} for x in s]
json.dump({'lang': i.language, 'segs': segs}, open(sys.argv[2], 'w'))
