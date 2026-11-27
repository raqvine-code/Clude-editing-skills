# Quality bar: how the picks were chosen, and a checklist for new work

## How the 33 were chosen

All 242 entries were fetched and viewed as frame sheets (8 frames each), then 89 were shortlisted, 72 examined closely (18 of the shortlist were not examined beyond triage; they are listed in `visual-reference/INDEX.md`), and 33 picked. The brief was: unique, premium, modern, professionally executed; quality over quantity; skip repetitive or basic pieces. Grades (A, A-, B+) are my judgement from stills and measurements and are in `data/entries-all-242.json` (`review_grade`, `review_note`). They are not an objective ranking, and I could not hear any audio.

What separated an A from a B+ in practice:

1. **A single idea carried to the end.** 28, 82, 161, 183, 230 each have one thing (a photon, a point, a poster, a ball, a dot) that every beat serves.
2. **One visual system held throughout.** Two colours (69), one material (197), one medium (177), one chapter palette each (41). Pieces that mixed several unrelated looks without an anchor scored lower unless variety was the concept (63, 130, 187).
3. **Continuity at the seams.** Morphs, flood-and-contract, match cuts, shared elements, loops with matching first and last frames. Hard cuts only where they land on a beat.
4. **Control of pace.** Variety between fast and still moments. The busiest picks (M4, M5) still had designed rests; the quiet ones (M1) used light and camera, not stillness.
5. **Typographic decisions.** Large, specific, set against a counter-weight (serif italic against grotesk; one outlined word behind a simulation).
6. **Polish where AI work often breaks**: text that stays legible during camera moves, shapes that really cover the corners, no teleporting objects, a real end card.
7. **A soundtrack that exists and is placed.** All 33 picks have audio; the structured prompts place effects by measured peak and normalise to -14 LUFS. [I could not listen, so this is about presence and level, not taste.]

## Weaknesses seen in individual entries (for calibration)

- Low resolution on a good idea: 22 (720x900).
- Silence or near silence: 47 and 233 have no audio track; 195 is near silent.
- Blank or black tails: 99.
- Looks like generated footage rather than code-built motion graphics, so outside this study: 54.
- Overlong for the idea: some 4-5 minute pieces (68, 173, 186) rely on captions and pacing to hold attention; I did not judge them to be equally strong across their full length.
- Facts on screen that I did not check: 28, 156, 116, 36.
- Generic showreel look (corner labels, same palette): many of the 28 entries sharing the one-line showreel prompt, which is why only four type-and-shape showreels (69, 161, 197, 131) were picked.

## Checklist before delivering a piece

**Concept**
- [ ] I can state the idea in one sentence and every scene serves it.
- [ ] There is a payoff in the last beat (a line, a reveal, a loop closing).
- [ ] Text is as short as it can be; the picture carries the meaning.

**Look**
- [ ] One accent colour or one medium; neutrals were chosen, not defaulted.
- [ ] No corner furniture (labels, tick marks, timecodes) unless it is part of the idea.
- [ ] Type pairs are deliberate and legible at the smallest size shown.
- [ ] Nothing on the banned list in `techniques.md` section 10 is present by accident.

**Motion**
- [ ] Every scene change is a morph, a match, a shared element, or a hard cut on a beat.
- [ ] Springs overshoot a little at most; nothing floats without a reason.
- [ ] No hold longer than about one second unless it is a deliberate rest.
- [ ] Full-screen shapes cover all four corners and take about 0.3 s.
- [ ] Hero objects never teleport; every handoff is visible.

**Technical** (run `scripts/qc_render.py video.mp4 --strips out/`)
- [ ] Resolution, frame rate and duration are what the brief asked for.
- [ ] Each single-frame pop candidate is either a deliberate cut or fixed.
- [ ] If it should loop, the first-versus-last-frame difference is near zero.
- [ ] Look at a contact sheet (`scripts/contact_sheet.py`) and at a 6-frame burst of the fastest move (`--burst T`): no ghost copies (use more subframes), no blurry text during camera moves.
- [ ] Loudness near -14 LUFS, true peak below -1 dB, effects under the music.
- [ ] Licences checked for music, sound effects, fonts and photos.

**Delivery**
- [ ] The first frame (thumbnail) is strong and readable.
- [ ] The end card has a mark, a URL or a call to action as appropriate.
