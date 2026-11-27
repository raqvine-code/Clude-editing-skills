#!/bin/bash
# Full-res still(s) side by side. usage: still.sh <reel_dir> <name> <frame> [frame ...]  -> <reel_dir>/st/<name>.jpg
D="$1"; N="$2"; shift 2; mkdir -p "$D/st"; IN=""; FC=""; i=0
for f in "$@"; do ffmpeg -hide_banner -loglevel error -y -i "$D/src/reel.mp4" -vf "select=eq(n\,$f)" -frames:v 1 -q:v 2 "$D/st/_f$f.jpg"; IN="$IN -i $D/st/_f$f.jpg"; FC="$FC[$i]"; i=$((i+1)); done
if [ $i -gt 1 ]; then ffmpeg -hide_banner -loglevel error -y $IN -filter_complex "${FC}hstack=$i" -q:v 2 "$D/st/$N.jpg"; else cp "$D/st/_f$1.jpg" "$D/st/$N.jpg"; fi; echo "$D/st/$N.jpg"
