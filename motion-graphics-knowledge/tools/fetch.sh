#!/usr/bin/env bash
# Re-run the study: download every entry from prompt-motion.com, extract title/creator/tags/prompt/video link,
# download the videos, measure them (fps, duration, motion energy, cut rate) and cross-check the prompts.
# usage: tools/fetch.sh OUT_DIR [LIMIT]     (LIMIT = only the first N entries, for a quick test)
# needs: curl, python3 with Pillow + numpy, ffmpeg/ffprobe. Videos total ~2.7 GB for all 242 entries.
# Prompt Motion's videos and prompts belong to their creators: keep downloads for your own study.
set -euo pipefail
OUT=${1:?usage: fetch.sh OUT_DIR [LIMIT]}; LIMIT=${2:-100000}
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$OUT/pages" "$OUT/videos"
curl -sS -L -m 60 -o "$OUT/index.html" https://prompt-motion.com/
# entry pages are /<creator>-<6 or 7 hex chars>; the home page links all of them
python3 -I - "$OUT" "$LIMIT" <<'PY'
import re,sys
s=open(sys.argv[1]+'/index.html',encoding='utf-8').read()
slugs=sorted(set(re.findall(r'href="/([a-z0-9-]+-[0-9a-f]{6,7})"',s)))[:int(sys.argv[2])]
open(sys.argv[1]+'/slugs.txt','w').write('\n'.join(slugs)+'\n'); print(len(slugs),'entries')
PY
xargs -P 8 -I{} sh -c 'curl -sS -L -m 60 --retry 3 -o "$0/pages/{}.html" "https://prompt-motion.com/{}" || echo FAIL {}' "$OUT" < "$OUT/slugs.txt"
# each page has a schema.org VideoObject (title, creator, contentUrl) and the prompt in <div id="entry-prompt">
python3 -I "$HERE/parse.py" "$OUT/pages" "$OUT/data.json"
python3 -I - "$OUT" <<'PY'
import json,sys
d=json.load(open(sys.argv[1]+'/data.json'))
open(sys.argv[1]+'/dl.txt','w').write(''.join(f"{r['slug']} {r['video']}\n" for r in d))
PY
xargs -P 8 -L 1 sh -c 'curl -sS -L -m 300 --retry 3 -o "'"$OUT"'/videos/$0.mp4" "$1" || echo FAIL $0' < "$OUT/dl.txt"
python3 -I "$HERE/probe.py" "$OUT"      # duration, fps, size, audio track
python3 -I "$HERE/metrics.py" "$OUT"    # motion energy, static share, spike (cut) rate per 10 s at 12 fps
python3 -I "$HERE/rsc.py" "$OUT"        # cross-check prompts against the page data, extract translations
echo "done: $OUT/data.json"
