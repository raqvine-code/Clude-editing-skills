#!/bin/bash
# Lists media files that exist in the asset folders but are NOT yet in the catalogs.
# Usage: bash skill-saver/scripts/find_uncatalogued.sh   (override with ASSETS=/path/to/claude)
SKILLS="$(cd "$(dirname "$0")/../.." && pwd)"
ASSETS="${ASSETS:-/Users/raghusai/Downloads/claude}"
check () { # $1 = asset folder, $2 = catalog file
  echo "== $1 (not in $(basename "$(dirname "$2")")/$(basename "$2"))"
  ls "$ASSETS/$1" | while IFS= read -r f; do
    grep -qF "\`$f\`" "$2" || echo "  NEW: $f"
  done
}
check "brolls for claude" "$SKILLS/broll-library/catalog.md"
check "png for claude"   "$SKILLS/png-library/catalog.md"
