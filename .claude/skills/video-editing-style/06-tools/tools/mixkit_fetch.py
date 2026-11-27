#!/usr/bin/env python3
"""Fetch Mixkit sound effects or music by id into a scratch folder (2026-11-27).
   python3 mixkit_fetch.py <restore-list.json> <out_dir> [--role whoosh,impact,foley] [--ids 2350,1492] [--music]
   Uses the public preview files (assets.mixkit.co); the category pages are behind a bot check, the ids in the list are not.
   The files are for use in a video (Mixkit licence); do NOT commit them to a public repo. Writes <out_dir>/<name>_<id>.mp3."""
import json, os, sys, time, urllib.request
lst = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
opt = lambda n: sys.argv[sys.argv.index(n) + 1].split(",") if n in sys.argv else None
roles, ids = opt("--role"), opt("--ids")
UA = {"User-Agent": "sfx-research-client/1.0"}
def grab(url, dst):
    try: open(dst, "wb").write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()); return True
    except Exception as e: print("failed", url[-40:], e); return False
n = 0
if "--music" in sys.argv:
    for k, v in lst["music"].items():
        if grab(v["url"], f"{out}/{k}.mp3"): n += 1
        time.sleep(0.3)
else:
    for k, v in lst["sfx"].items():
        if (roles and v["role"] not in roles) or (ids and v["mixkit_id"] not in ids): continue
        i = v["mixkit_id"]
        if grab(f"https://assets.mixkit.co/active_storage/sfx/{i}/{i}-preview.mp3", f"{out}/{k}_{i}.mp3"): n += 1
        time.sleep(0.3)
print("fetched", n, "files into", out)
