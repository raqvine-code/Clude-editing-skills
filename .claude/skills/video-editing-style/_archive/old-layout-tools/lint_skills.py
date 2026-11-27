"""Check that the skills folder is well structured (added 2026-11-25).
Usage: python3 "VIDEO EDITING MASTERY/tools/lint_skills.py"   (from the CLAUDE 2.0 folder)
Checks every skill folder for: SKILL.md present, frontmatter name == folder name, a description,
a row in skills/README.md, a mention in the skill-saver map, and that every `skill-name` a SKILL.md
or the README points to exists. Folders starting with "_" are shared kits: they need a README.md instead.
Prints problems and exits 1 if there are any.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SK = ROOT / "skills"
problems = []


def front(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip().strip("'\"")
    return out


folders = sorted(p for p in SK.iterdir() if p.is_dir() and not p.name.startswith("."))
names = {p.name for p in folders}
kit = {p.name for p in (SK / "_edit-kit" / "skills").iterdir() if p.is_dir()}  # Edit-Kit skills, named in edit-kit-playbook
KNOWN_ABSENT = {"gadget-review-editing"}  # noted in motion-graphics-style as never in the original set
readme = (SK / "README.md").read_text()
saver = (SK / "skill-saver" / "SKILL.md").read_text()

for p in folders:
    if p.name.startswith("_"):
        if not (p / "README.md").exists():
            problems.append(f"{p.name}: shared folder without README.md")
        if f"`{p.name}" not in readme:
            problems.append(f"{p.name}: not listed in skills/README.md")
        continue
    f = p / "SKILL.md"
    if not f.exists():
        problems.append(f"{p.name}: no SKILL.md")
        continue
    t = f.read_text()
    fm = front(t)
    if fm.get("name") != p.name:
        problems.append(f"{p.name}: frontmatter name is {fm.get('name')!r}")
    if len(fm.get("description", "")) < 40:
        problems.append(f"{p.name}: description missing or too short")
    if f"`{p.name}`" not in readme:
        problems.append(f"{p.name}: no row in skills/README.md")
    if p.name not in saver:
        problems.append(f"{p.name}: not in the skill-saver map")

# dangling skill references: `word-word` that looks like a skill name but has no folder
pat = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
suffixes = ("-style", "-editing", "-guide", "-atlas", "-tips", "-library", "-playbook", "-design", "-process", "-rules", "-avoid", "-colours", "-method", "-animation", "-cut", "-assets", "-strategy", "-saver", "-builder", "-pro")
for src in [SK / "README.md"] + [p / "SKILL.md" for p in folders if (p / "SKILL.md").exists()]:
    for ref in set(pat.findall(src.read_text())):
        if ref.endswith(suffixes) and ref not in names | kit | KNOWN_ABSENT and not ref.startswith(("style-", "slug-")):
            problems.append(f"{src.relative_to(SK)}: points to `{ref}`, which has no folder")

skills = [p for p in folders if not p.name.startswith("_")]
print(f"{len(skills)} skills + {len(folders) - len(skills)} shared folders checked")
for x in problems:
    print("  -", x)
print("OK" if not problems else f"{len(problems)} problem(s)")
sys.exit(1 if problems else 0)
