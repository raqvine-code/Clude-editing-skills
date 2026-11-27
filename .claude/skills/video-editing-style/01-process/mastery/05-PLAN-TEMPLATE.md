# PLAN TEMPLATE - copy to `<project_dir>/PLAN.md` and fill every section before editing

`analyze_raw.py` pre-fills section A and creates `<project_dir>/PLAN.md` from this template. Sections B-J are written by Claude after watching the sheets and reading the whole transcript.

## A. Footage analysis (facts - auto + checked)
- File / duration / resolution / fps / orientation:
- Loudness (LUFS, LRA, peak) and noise/room notes:
- Speech: words, words per second, longest pauses, silence total (pauses > 0.3 s are cut candidates):
- Language (English / Telugu / Tenglish / Hindi):
- Already cut? (jump cuts found / polished?) -> keep the user's cut unless told otherwise:
- Visual check from sheets: framing, lighting, colour cast, headroom, background, hands/gestures, dead moments:
- Best moments (time + line): 
- Problems to fix (exposure, WB, audio, black bands, mistakes, repeats):

## B. Goal and audience
- Platform + aspect + target length:
- Goal (teach / sell / grow / hire / entertain) and the ONE takeaway:
- Viewer and what they care about:
- CTA (exact words):

## C. Story structure
| Part | Time in raw | Line(s) | Job |
|---|---|---|---|
| Hook (0-3 s) | | | promise + visual interrupt |
| Context / stakes | | | |
| Body (points / steps) | | | |
| Payoff | | | |
| CTA / loop | | | |
Cut list: lines removed and why.

## D. Style decision
- Style (ONE): ___ from skill ___ ; reason in one line:
- Skills used (Stage 0): my-editing-rules, mistakes-to-avoid, fonts-and-colours, ___
- Fonts per role (caption / display / label), accent colour (one family), grade:
- Safe zones: top ___ px, bottom ___ px, right ___ px.

## E. Shot-by-shot edit plan
| # | Out time | Len | Spoken words | Framing / camera | On-screen text (tier, word that triggers it) | Graphic / B-roll / PNG | Transition in | SFX | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.00 | | | | | | | | |

Rules: each graphic lands on its word or 0.1-0.35 s before; one keyword per sentence; visual change every ~2-3 s (short) / ~5 s (long); no hold over 2.5 s (short) without a scale/overlay change.

## F. Graphics and assets list
Copy the motion-graphics plan from `PRE-EDIT.md` (`01-process/before-edit/3-PRE-EDIT-SHEET.md` section 4): designed MG every 8 s, 3+ kinds, >= 25 % of runtime, HL + MC. Text on footage is not motion graphics.
| Asset | Source (local library / site / build) | Lands on (word, time) | Enter -> hold -> exit (frames) |
|---|---|---|---|

## G. Creative ideas (Claude's own, 2-3)
1. Claude's idea:  - why it fits this video:  - risk / rule check (mistakes-to-avoid):
2. Claude's idea:
3. Claude's idea:

## H. Sound plan
- Voice clean-up chain and target (-16 LUFS voice, -14 LUFS master, -1 dBTP):
- Music (mood, BPM, source Mixkit/Freesound/Pixabay), where it changes, where it cuts:
- SFX list (moment -> sound), phone-speaker rule (mid knock + HF click):

## I. Risks and the three weakest moments
| Moment | Why weak | Fix |
|---|---|---|

## J. QC targets and delivery
- Sample: 10-15 s of ___ to render first.
- Checks: hook moves by frame 3; text readable >= 0.5 s; no text over eyes/mouth; one palette; sync within -0.35..+0.1 s; loudness; freeze/black detection; mobile view.
- Export: ___ x ___, ___ fps, H.264, AAC 48 kHz. File name:
- Approval needed before full render? yes / no (new style or client = yes)
