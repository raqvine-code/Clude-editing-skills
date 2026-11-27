# 01-process: the order of every edit

| Folder | Use |
|---|---|
| `before-edit/` | THE GATE. Run its steps before any edit, short or long, captions-only or sound-only. |
| `mastery/` | The master plan, the PLAN.md template, and overviews of every style. |

## before-edit/ (in order)
| Step | File | Done when |
|---|---|---|
| 1 | `01-process/before-edit/1-READ-THESE-SKILLS.md` | Full mode: every row ticked in `PRE-EDIT.md`, newest lessons first. Fast mode: the Core 5 from `README.md` |
| 2 | `05-clients/<client>/` (Naveen bro: `05-clients/naveen-bro/CLIENT-BAR.md`) | its rules are copied into the plan |
| 3 | `01-process/before-edit/2-PRO-MOVE-MENU.md` | every family has at least the floor count, or a written reason |
| 4 | `01-process/before-edit/3-PRE-EDIT-SHEET.md` copied to `<project>/PRE-EDIT.md` and filled | skills, assets searched, motion-graphics plan with times |
| 5 | `01-process/mastery/05-PLAN-TEMPLATE.md` plus `analyze_raw.py` into `<project>/PLAN.md` | the event map includes the motion-graphics plan |
| 6 | `python3 01-process/before-edit/tools/pre_edit_gate.py <project>/edl.json` on the DRAFT EDL | `RESULT: READY` before the full render |
| 7 | stills, a 6-10 s full-quality sample of the hook, full render, QC, gate again | READY and scorecard PASS |

Nothing is rendered in full while the gate says NOT READY. A FAIL is fixed by adding the missing work, never by editing the gate.

## mastery/
| File | What it holds |
|---|---|
| `01-process/mastery/04-PRO-EDITOR-MASTER-PLAN.md` | the step-by-step plan for every edit, senior-editor habits |
| `01-process/mastery/05-PLAN-TEMPLATE.md` | PLAN.md: footage facts to QC targets, plus "Claude's idea" moves |
| `01-process/mastery/02-SHORT-FORM-STYLES.md` | 11 short-form styles, screenshot-only looks, platform rules |
| `01-process/mastery/03-LONG-FORM-STYLES.md` | 10 long-form styles, shared rules |
| `01-process/mastery/01-SKILLS-A-TO-Z.md` | overview of the first 23 skills (2026-11-15; now 36, see `INDEX.md`) |
| `01-process/mastery/README.md` | the original overview and the 2026-11-17 to 11-25 learning notes |
