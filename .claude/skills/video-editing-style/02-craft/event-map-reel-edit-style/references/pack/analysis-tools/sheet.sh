#!/bin/bash
# Frame-numbered contact sheet.
# usage: sheet.sh <reel_dir> <name> <start_s> <end_s> <fps> <cols> <rows> <tile_w> [crop=w:h:x:y in source px]
# output: <reel_dir>/d/<name>.jpg   (labels = source frame number at 30 fps)
D="$1"; N="$2"; A="$3"; B="$4"; FPS="$5"; C="$6"; R="$7"; W="$8"; CROP="$9"
PRE=""; [ -n "$CROP" ] && PRE="crop=$CROP,"
mkdir -p "$D/d"
ffmpeg -hide_banner -loglevel error -y -ss "$A" -to "$B" -i "$D/src/reel.mp4" -vf "${PRE}fps=$FPS,scale=$W:-1,drawtext=text='%{eif\:(t+$A)*30+0.5\:d}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.65,tile=${C}x${R}" -frames:v 1 -q:v 3 "$D/d/$N.jpg" && echo "$D/d/$N.jpg"
