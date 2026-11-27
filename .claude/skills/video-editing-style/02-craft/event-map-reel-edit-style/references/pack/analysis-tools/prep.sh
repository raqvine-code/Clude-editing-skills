#!/bin/bash
# usage: prep.sh <reel_dir>   (expects <reel_dir>/src/reel.mp4)
set -e
D="$1"; V="$D/src/reel.mp4"
mkdir -p "$D/sheets" "$D/fr" "$D/d" "$D/st" "$D/data"
# scene scores per frame
ffmpeg -hide_banner -loglevel error -i "$V" -vf "select='gte(scene,0)',metadata=print:file=$D/data/scene_raw.txt" -an -f null -
# contact sheets 3 fps, 6x3 tiles, timestamped
ffmpeg -hide_banner -loglevel error -y -i "$V" -vf "fps=3,scale=240:-1,drawtext=text='%{pts\:hms}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x3" "$D/sheets/s_%02d.jpg"
# small frames for numeric work
ffmpeg -hide_banner -loglevel error -y -i "$V" -vf "scale=360:640" -q:v 3 -start_number 0 "$D/fr/%04d.jpg"
# audio
ffmpeg -hide_banner -loglevel error -y -i "$V" -vn -ac 1 -ar 16000 "$D/data/a16.wav"
ffmpeg -hide_banner -loglevel error -y -i "$V" -vn -ac 2 -ar 44100 "$D/data/a44.wav"
ffmpeg -hide_banner -i "$V" -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Input (Integrated|True Peak|LRA|Threshold)" > "$D/data/loudness.txt"
ffmpeg -hide_banner -loglevel error -y -i "$D/data/a44.wav" -lavfi "showspectrumpic=s=1800x600:legend=1:scale=log:fscale=log" "$D/data/spec.png"
echo "prep done $D: $(ls $D/fr | wc -l) frames, $(ls $D/sheets | wc -l) sheets"
