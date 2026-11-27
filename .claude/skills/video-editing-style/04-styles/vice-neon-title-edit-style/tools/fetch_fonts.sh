#!/usr/bin/env bash
# Fetch the fonts this style uses into tools/fonts/ (not stored in the repo).
# Pricedown Black: free for commercial use under the Typodermic Desktop License (one user; rendered video is covered;
# the font file itself may not be redistributed, so it is downloaded here, never committed).
# The rest are SIL Open Font License fonts from the Google Fonts repository.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd); F="$HERE/fonts"; mkdir -p "$F"; cd "$F"
B=https://raw.githubusercontent.com/google/fonts/main/ofl
curl -sSfL -m 60 -o NotoSerifDisplay.ttf "$B/notoserifdisplay/NotoSerifDisplay%5Bwdth,wght%5D.ttf"
curl -sSfL -m 60 -o InterTight.ttf "$B/intertight/InterTight%5Bwght%5D.ttf"
curl -sSfL -m 60 -o Inter.ttf "$B/inter/Inter%5Bopsz,wght%5D.ttf"
curl -sSfL -m 60 -o PatrickHand.ttf "$B/patrickhand/PatrickHand-Regular.ttf"
T=$(mktemp -d); curl -sSfL -m 60 -A "Mozilla/5.0" -e "https://www.1001fonts.com/pricedown-font.html" -o "$T/p.zip" "https://www.1001fonts.com/download/pricedown.zip"
unzip -o -q "$T/p.zip" -d "$T"; cp "$T/Pricedown Bl.otf" PricedownBl.otf; cp "$T"/Typodermic*EULA*.pdf . 2>/dev/null || true; rm -rf "$T"
ls -la "$F"
