#!/bin/bash
# learn_video.sh <video> <study_dir>
# Cheap, complete study of ONE reference video. All steps are local compute (no tokens).
# Afterwards read only: *_stats.txt, transcript.txt, captions_compact.txt, shots/shots_*.jpg (one frame per shot),
# then a few strips made with strip.py. See README.md.
set -e
V="$1"; OUT="$2"; K="$(cd "$(dirname "$0")" && pwd)"
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
WPY="${WHISPER_PY:-$HOME/.local/share/whisper-venv/bin/python}"
mkdir -p "$OUT"; cd "$OUT"
[ -f proxy.mp4 ] || "$FF" -v error -y -i "$V" -vf "scale='if(gt(iw,ih),1280,720)':-2" -c:v libx264 -preset veryfast -crf 20 -g 12 -c:a aac -b:a 128k proxy.mp4
[ -f st.wav ] || "$FF" -v error -y -i proxy.mp4 -vn -ac 2 -ar 22050 st.wav
[ -f a22.wav ] || "$FF" -v error -y -i proxy.mp4 -vn -ac 1 -ar 22050 a22.wav
if [ ! -f transcript.json ]; then "$WPY" "$K/transcribe_one.py" a22.wav transcript.json ${WHISPER_MODEL:-small} $WHISPER_LANG & fi
[ -f shots/shots.json ] || python3 "$K/shots.py" proxy.mp4 shots | tee shots_stats.txt
if [ ! -f ocr5.jsonl ]; then
  mkdir -p ocr5; "$FF" -v error -y -i proxy.mp4 -vf fps=5 -q:v 3 ocr5/%05d.jpg
  [ -x "$K/ocr" ] || swiftc -O "$K/ocr.swift" -o "$K/ocr"
  [ -x "$K/face" ] || swiftc -O "$K/face.swift" -o "$K/face"
  "$K/face" ocr5 faces.txt; "$K/ocr" ocr5 ocr5.jsonl; rm -rf ocr5
fi
wait
python3 "$K/face_stats.py" | tee face_stats.txt
python3 "$K/audio_side.py" | tee audio_stats.txt
python3 "$K/ocr_agg.py" | tee text_stats.txt
python3 "$K/sync_stats.py" | tee sync_stats.txt
echo "DONE: $OUT"
