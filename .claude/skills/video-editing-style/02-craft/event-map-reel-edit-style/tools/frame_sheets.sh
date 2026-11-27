#!/bin/bash
# frame_sheets.sh - frame-numbered contact sheets for frame-by-frame review of a reel
# (a reference you are studying, or your own render you are checking).
#
# usage: frame_sheets.sh VIDEO OUT.jpg START_S END_S FPS COLS ROWS TILE_W [CROP=W:H:X:Y]
#   whole reel overview : frame_sheets.sh reel.mp4 overview.jpg 0 45 1 9 5 200
#   one transition      : frame_sheets.sh reel.mp4 cut1.jpg 10.8 11.6 30 8 3 240
#   caption animation   : frame_sheets.sh reel.mp4 cap.jpg 0 1.6 15 8 3 300
# Each tile is labelled with its source frame number (at 30 fps numbering = time * 30).
# Use 30 fps across transitions, 10-15 fps across text/graphic animation, 1-3 fps for overviews.
set -e
[ $# -lt 8 ] && { sed -n 2,10p "$0"; exit 1; }
V="$1"; OUT="$2"; A="$3"; B="$4"; FPS="$5"; C="$6"; R="$7"; W="$8"; CROP="$9"
PRE=""; [ -n "$CROP" ] && PRE="crop=$CROP,"
# local change 2026-11-22: fall back to the imageio ffmpeg binary when ffmpeg is not on PATH
FF="$(command -v ffmpeg || python3 -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')"
"$FF" -hide_banner -loglevel error -y -ss "$A" -to "$B" -i "$V" \
  -vf "${PRE}fps=$FPS,scale=$W:-1,drawtext=text='%{eif\:(t+$A)*30+0.5\:d}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.65,tile=${C}x${R}" \
  -frames:v 1 -q:v 3 "$OUT" && echo "$OUT"
