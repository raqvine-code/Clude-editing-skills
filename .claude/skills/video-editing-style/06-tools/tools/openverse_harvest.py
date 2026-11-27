#!/usr/bin/env python3
"""Collect real sound-effect candidates from Openverse by role (2026-11-27).
   Needs OPENVERSE_TOKEN (a 12 h bearer token from a free registered client: sfx-sources-and-ears.md section 1b). Keeps cc0 / pdm / by only; writes ov/<role>/<id>.<ext> and ov/catalog.json."""
import json, os, sys, time, urllib.parse, urllib.request
D = os.getcwd(); OUT = D + "/ov"; os.makedirs(OUT, exist_ok=True)      # run it in a scratch folder; results go to ./ov
tok = os.environ["OPENVERSE_TOKEN"]; UA = {"User-Agent": "sfx-research-client/1.0"}      # bearer token: see sfx-sources-and-ears.md
OK_LIC = {"cc0", "pdm", "by"}
ROLES = {   # role: (queries, max seconds, files to keep per role)
 "whoosh":   (["whoosh", "swoosh", "fast swipe whoosh", "air swish", "transition whoosh"], 3.0, 14),
 "slide":    (["slide", "card slide", "swipe"], 2.0, 8),
 "paper":    (["paper slide", "paper swipe", "paper rustle", "page flip", "paper flick"], 3.0, 10),
 "click":    (["soft click", "mouse click", "switch click", "button click", "tick"], 1.0, 12),
 "key":      (["keyboard key", "typewriter key", "typing"], 2.0, 6),
 "pop":      (["pop", "bubble pop", "cork pop", "soft pop"], 1.0, 10),
 "impact":   (["soft impact", "low thud", "deep boom", "cinematic hit", "sub drop"], 4.0, 12),
 "riser":    (["riser", "reverse swell", "tension riser", "reverse cymbal"], 6.0, 8),
 "shutter":  (["camera shutter", "photo click", "dslr shutter"], 2.0, 6),
 "chime":    (["glass tap", "soft chime", "bell ding", "marimba note"], 3.0, 8),
 "knock":    (["wood knock", "tap", "table tap"], 1.5, 6),
 "scratch":  (["record scratch", "tape stop"], 2.5, 4),
 "marker":   (["marker squeak", "pen stroke", "chalk"], 2.5, 5),
 "heartbeat":(["heartbeat"], 4.0, 3),
 "cloth":    (["cloth movement", "fabric swish", "clothes rustle"], 3.0, 6),
 "roomtone": (["room tone", "quiet room ambience", "air conditioner hum"], 40.0, 6),
}
def get(url, headers):
    for a in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=40)
        except urllib.error.HTTPError as e:
            if e.code == 429: print("429, stop", e.read()[:100]); sys.exit(2)
            if a == 2: raise
            time.sleep(1.5)
cat = json.load(open(OUT + "/catalog.json")) if os.path.exists(OUT + "/catalog.json") else {}
for role, (qs, maxs, keep) in ROLES.items():
    os.makedirs(f"{OUT}/{role}", exist_ok=True); seen = {k for k, v in cat.items() if v["role"] == role}; got = len(seen)
    for q in qs:
        if got >= keep: break
        url = "https://api.openverse.org/v1/audio/?" + urllib.parse.urlencode({"q": q, "page_size": 30, "source": "freesound"})
        try: d = json.load(get(url, {"Authorization": "Bearer " + tok, **UA}))
        except Exception as e: print(role, q, "search failed", e); continue
        time.sleep(0.3)
        for x in d.get("results", []):
            if got >= keep: break
            if x["id"] in cat or x.get("license") not in OK_LIC: continue
            dur = (x.get("duration") or 0) / 1000
            if not (0.05 <= dur <= maxs) or (x.get("filesize") or 0) > 2_500_000 or x.get("filetype") not in ("mp3", "wav", "ogg", "flac"): continue
            f = f"{OUT}/{role}/{x['id'][:8]}.{x['filetype']}"
            try: open(f, "wb").write(get(x["url"], UA).read())
            except Exception as e: print("download failed", x["url"][-40:], e); continue
            cat[x["id"]] = dict(role=role, query=q, file=f.replace(D + "/", ""), title=x["title"], creator=x.get("creator"), license=x["license"], license_version=x.get("license_version"),
                                duration_s=round(dur, 2), source=x.get("source"), landing=x.get("foreign_landing_url"), download_url=x["url"])
            got += 1; time.sleep(0.15)
    print(f"{role:10s} {got} files"); json.dump(cat, open(OUT + "/catalog.json", "w"), indent=1)
print("total", len(cat))
