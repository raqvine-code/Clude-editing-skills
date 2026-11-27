# Before edit: the gate every edit passes first

**Why this folder exists (user, 2026-11-26):** "this edit not impressed by client. I told you use all skills what you learned still now, especially yesterday's learned things. From next time onwards use perfect skills: B-rolls, motion graphics and other things, like a pro editor."

Video 25 had good captions and B-roll, but it was mostly **text on footage**. Designed motion graphics covered only 11 % of the runtime, nothing was designed for the first 17.8 s, and it had no highlight or match cut (`08-learning-log/VIDEO-25-POSTMORTEM.md`). This folder makes sure that never ships again.

## The order (before ANY edit: short, long, captions-only, sound-only)
| Step | File | Done when |
|---|---|---|
| 1 | `1-READ-THESE-SKILLS.md` | every row is ticked in the project's `PRE-EDIT.md`, newest lessons first |
| 2 | `05-clients/naveen-bro/CLIENT-BAR.md` (for that client) | its rules are copied into the plan |
| 3 | `2-PRO-MOVE-MENU.md` | every family has at least the floor count, or a written reason |
| 4 | `3-PRE-EDIT-SHEET.md` -> copy to `<project>/PRE-EDIT.md` and fill it in | the sheet is complete: skills, assets searched, MG plan with times |
| 5 | `CLAUDE.md` Rule 2: `analyze_raw.py` + `PLAN.md` | the event map includes the MG plan from the sheet |
| 6 | `tools/pre_edit_gate.py <project>/edl.json` on the DRAFT EDL | `RESULT: READY` (no FAIL) **before** the full render |
| 7 | Stills + a 6-10 s full-quality sample of the hook, then the full render, QC, and the gate again | READY + scorecard PASS |

Nothing gets rendered in full while the gate says NOT READY. A FAIL is fixed by adding the missing work, never by editing the gate.

```bash
python3 "01-process/before-edit/tools/pre_edit_gate.py" "<ROOT>/edits/<project>/edl.json"
```

## Files
- `1-READ-THESE-SKILLS.md`: every skill to open, by job, with the newest learning marked.
- `2-PRO-MOVE-MENU.md`: the full menu of B-roll, motion graphics, text, transitions, camera and sound, with the kit key / tool and the floor count for a 45-60 s short.
- `3-PRE-EDIT-SHEET.md`: the template copied into every project as `PRE-EDIT.md`.
- `05-clients/naveen-bro/CLIENT-BAR.md`: everything this client and the user have asked for, in one place.
- `08-learning-log/VIDEO-25-POSTMORTEM.md`: what fell short and what to do instead.
- `tools/pre_edit_gate.py`: the automatic check (reads the EDL, plus `analysis/facts.json` for pauses).
