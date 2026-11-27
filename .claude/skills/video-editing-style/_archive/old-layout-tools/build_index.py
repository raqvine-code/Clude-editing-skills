"""Build QUICK-INDEX.md: every skill in CLAUDE 2.0/skills with its description, files, and every ## / ### heading
with its line number, so Claude can Read(file, offset=line) straight to the needed part.
usage: python3 build_index.py   (re-run after any skill is added or edited)"""
import os, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # .../CLAUDE 2.0
SK = os.path.join(ROOT, "skills")
OUT = os.path.join(ROOT, "VIDEO EDITING MASTERY", "QUICK-INDEX.md")
SKIP_DIRS = {"cache", "__pycache__", "fonts", "boards"}

lines = ["# QUICK INDEX - all video-editing skills",
         f"Generated {datetime.date.today()} by `VIDEO EDITING MASTERY/tools/build_index.py`. Paths are relative to `{SK}`.",
         "Use: find the topic, then Read the file at the listed line (offset) instead of loading whole skills.", ""]
toc = []
body = []
for name in sorted(os.listdir(SK)):
    d = os.path.join(SK, name)
    if not os.path.isdir(d):
        continue
    sk = os.path.join(d, "SKILL.md")
    desc = ""
    if os.path.exists(sk):
        txt = open(sk, encoding="utf-8").read()
        m = re.search(r"^description:\s*(.+)$", txt, re.M)
        desc = (m.group(1).strip() if m else "")[:260]
    toc.append(f"- [{name}](#{name.lower().replace('_', '').replace(' ', '-')}) - {desc[:120]}")
    body.append(f"## {name}")
    if desc:
        body.append(f"_{desc}_")
    if name == "_edit-kit":  # vendored kit: index one line per sub-skill, not its ~2200 files
        for sub in sorted(os.listdir(os.path.join(d, "skills"))):
            sp = os.path.join(d, "skills", sub, "SKILL.md")
            if os.path.exists(sp):
                t = open(sp, encoding="utf-8").read()
                m = re.search(r"^description:\s*>?\s*(.+)$", t, re.M)
                n = t.count("\n") + 1
                body.append(f"- `_edit-kit/skills/{sub}/SKILL.md` ({n} lines) - {(m.group(1).strip() if m else '')[:140]}")
        body.append("")
        continue
    for dp, dns, fns in os.walk(d):
        dns[:] = sorted(x for x in dns if x not in SKIP_DIRS)
        for fn in sorted(fns):
            if not fn.endswith((".md", ".py", ".json", ".html")) or fn == "manifest.json":
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, SK)
            n = sum(1 for _ in open(p, encoding="utf-8", errors="ignore"))
            body.append(f"- `{rel}` ({n} lines)")
            if fn.endswith(".md"):
                for i, ln in enumerate(open(p, encoding="utf-8", errors="ignore"), 1):
                    if re.match(r"^#{2,3} ", ln):
                        body.append(f"  - L{i}: {ln.strip().lstrip('#').strip()[:110]}")
            elif fn.endswith(".py"):
                first = open(p, encoding="utf-8", errors="ignore").read(400).split("\n")
                doc = next((x.strip('"\' ') for x in first if x.strip().strip('"\'')), "")
                body.append(f"  - {doc[:140]}")
    body.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(lines + ["## Contents"] + toc + [""] + body))
print("wrote", OUT, len(body), "lines")
