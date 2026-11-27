> Analyst notes for R1 (talking-head tips reel), measured frame by frame (30 fps, 720×1280 source). Frame numbers fNNN are 0-based (t = f/30).
> Evidence sheets and data files named below were working files and are not bundled; the numbers are what matters.
> Sections: 0 Identity · 1 Beat sheet table · 2 Hook dissection · 3 Typography and captions · 4 Motion and camera · 5 Transitions catalogue · 6 Motion-graphic devices and metaphors · 7 Colour and finishing · 8 Sound · 9 Storytelling and retention devices · 10 Weaknesses and mistakes · 11 Steal list

# r1: "Remember your script" (3 tips): frame-by-frame notes

Source: `src/reel.mp4`, 34.03 s, 720x1280, 30 fps, 1021 frames. Frame numbers (fNNN) are source frames at 30 fps; t = f/30.
Evidence sheets are in `d/` (frame numbers are printed on each tile): `hook_full_15fps`, `hook_cap_a/b_30fps`, `th3_cap_15fps`, `list_15fps`, `title1_30fps`, `title2_title3_30fps`, `white1_in/out_30fps`, `white1_10fps`, `white2_15fps`, `outro_cap_30fps`, `occlusion_check_fullres`, `occl2`, `occl3`, `topel_15fps`, `spec_cuts.png`. Full-res stills: `st/grade_type_f266_f1000.jpg`. The numbers behind this file are in `data/r1_measures.json`. The scripts are in `work/` (`direct.py` = masked direct scale fit, `capdet.py` = caption onset detector, `topel.py` = bokeh tracker).
Conventions: values marked ≈ were estimated by eye and not measured. Font names are visual guesses. Whisper word onsets are accurate to about ±50–100 ms, so sync offsets within ±3 f should be read as "on the word".

---

## 0 Identity

This is a dark, low-key talking-head explainer (frame median luma 5–17/255, near-black magenta-tinted background) with a warm orange hair rim and a steel-blue fill. A woman with a handheld mic delivers a fast list format (224 wpm overall, 261 wpm in the hook): a question hook, a contrarian reframe, three numbered tips, and a CTA that calls back to the hook. The edit is built on 4 systems:
1. Centred two-tier kinetic captions on the torso. Small function words sit next to 2.3× bigger content words, built word by word, and each group clears hard.
2. Two high-contrast white editorial motion-graphic interludes, with a live video card, visual metaphors and a 3D mascot. Each is entered by a hard dark→white luma flip.
3. One reusable dark "chapter card" template for First / Second / Third.
4. Constant digital camera life: eased push-ins on the hook and the list, and slow pull-outs on the tight tip shots.

Time split: talking head 24.5 s (72%), white MG 6.1 s (18%), chapter cards 3.4 s (10%). 11 shots, ASL 3.09 s. The music is a steady 133-bpm hi-hat bed with one drop on the first cut. Apart from that drop, the edit follows the voice and ignores the music grid.

## 1 Beat sheet table

| t (s) | frames | VO line | visual | caption | transition in | audio event |
|---|---|---|---|---|---|---|
| 0.00–3.30 | f0–99 | "How will you even master your personal branding if you can't remember your script?" | TH. Opens on the widest framing of the reel (≈0.77 of the f900 framing), then an eased digital push-in ≈×1.6 (f5–55, peak 3.2 %/frame at f13–14), held from f55 | 3 groups: "How will you even / **Master**" (f1–32) · "your / **Personal** / **Branding**" (f34–57) · "if you can't / **remember** / your / **script?**" (f59–99). The last keyword of each group gets a cyan swoosh | Video starts on VO frame 0 (first word at 0.00 s, caption f1) | Sub boom 0.1–0.8 s (sub peak −16 dB @0.4 s). The beat is removed 1.0–3.3 s (sub −35…−45 dB). Stereo transient at 3.22 s (≈ riser into the cut) |
| 3.33–4.80 | f100–144 | "So here's the thing," | White canvas #FFFFFF. The speaker keeps playing inside a rounded dark card (0.52 W, r≈24 px, soft shadow) that settles from 0.61 W→0.52 W in 3 f. A dark crescent ribbon grows bottom-left→top-right (f101–108). Tiny filler paragraphs drift | "so here's the" (small, black, above the card) f114; "**thing**" (big, below) f127 | Hard cut dark→white (luma 12→255) | **Beat drop**: kick + hats enter at 3.36 s, 27 ms after the cut |
| 4.83–6.30 | f145–189 | "you don't actually need to learn your scripts" | The canvas pushes left (≈720 px in ≈7 f, ease-out). A blue 3D brain in a silver birdcage on grid paper slides in from the right | Whole sentence at once: "you don't actually / need to learn / **your scipt**" (typo) | Push / slide-left | Stereo transient 5.05 s (≈ whoosh on the push) |
| 6.33–7.30 | f190–219 | "word by word," | Square of grid paper (#F1F1F1 lines), empty for 3 f | "word" f193 → "by" f199 → "word" f204, stacked. Each word goes grey→black | Hard cut | — |
| 7.33–10.43 | f220–313 | "but the trick is to break them into ideas and not into the sentences." | TH medium (≈1.12 of ref). Slow push-in +5–9% over 3.1 s (≈+2.4 %/s) | "but the / **trick** is to / **break** / them into / **ideas**" (9 words, f220–273) then "& not into the / **sentences**" (f274–313) | Hard cut white→dark | — |
| 10.47–12.20 | f314–366 | "First, understand the flow." | Chapter card template: blue-black #020308, slowly drifting dark 3D ribbons with silver/cyan edge light, dust specks | "First" (small) f319 → "**Understand**" f333 → thin cyan arc draws on f342–346 → "**the Flow**" f348 | Hard cut, 47 ms after the end of the VO phrase | Stereo transient 11.49 s (on the arc draw) |
| 12.23–15.03 | f367–451 | "Hook, main point, example, and then ending." | TH wide (≈0.85 of ref) with 4 stepped eased punch-ins: f367–373 +13%, f385–392 +15%, f405–411 +7%, f442–450 +12% → ≈×1.6 total | Single centred labels replace each other: "Hook," f367 / "Main Point," f389 / "Example" f409 / "and then" f429 / "Ending" f443 | Hard cut, 67 ms before "Hook" | Stereo transients 12.28 s (cut) and 12.91 s (zoom step 2) |
| 15.07–15.73 | f452–472 | "Second," | Same chapter template, clip restarted at its frame 0 (corr 0.99 with f314) | "Second" f453 | Hard cut | — |
| 15.77–19.43 | f473–583 | "practice saying it in your own words instead of forcing exact lines." | TH tight (≈1.35 of ref). Slow pull-out −11% over 3.7 s (−3.1 %/s). The top bulbs enter frame at f545 as the pull-out reveals them | "**practice** / it in your **saying** / **own** / **words**" (f474–526); "instead of / **forcing** / **exact** / **lines.**" (f528–583) | Hard cut, 113 ms before "practice" | — |
| 19.47–20.40 | f584–612 | "And third," | Chapter template restarted | "& Third" f585 | Hard cut, 307 ms after the phrase end | Stereo transient 19.50 s (+33 ms) |
| 20.43–25.67 | f613–770 | "repeat it out loud a couple of times until it feels natural like you're just telling a story to a friend." | TH tight (≈1.31 of ref). Pull-out −12% over 5.2 s (−2.5 %/s) | "repeat / it out **loud** a / **couple** / **times** of" · "**feels** until it / **natural,**" · "like you're / just **telling** a / **story**" · "to a / **friend**" | Hard cut on "repeat" (−7 ms) | — |
| 25.70–27.73 | f771–832 | "And that way you will never sound robotic" | White canvas. "and that way," alone at centre for 0.77 s, then 2 empty frames. A 3D robot mascot flies in from bottom-left with rotation (f804→≈f816) and bobs | "and that way," f772 · "you" f798, "will" f804, "never" f806, "**sound**" f812, "**robotic,**" f820. The black text block re-centres as words are added, then shifts right for the robot | Hard cut dark→white | Stereo transient 26.82 s = robot entrance (+20 ms) |
| 27.77–34.03 | f833–1020 | "and won't forget what to say. Try this in your next video and you will see how much easier it gets to speak on camera and remember the script." | TH medium (≈1.09 of ref). Pull-out −18% over 6.2 s (−3.2 %/s), flat from f1001 | "and won't / **forget** / **what** to / **say**" · "try this in your / **next** / **video**" · "& you'll **how** / see **much** / **easier**" · "it gets to / **speak** / on **camera**" · "and / **remember** / the **scripts**" | Hard cut white→dark | The music runs to the last frame. The file ends 0.17 s after the last word |

## 2 Hook dissection (f0–99, 3.30 s; sheets `hook_full_15fps`, `hook_cap_a/b_30fps`)

- **f0**: VO is already on the first syllable ("How" at 0.00 s). The frame is the widest of the reel: subject small and centred, face at ≈0.30 H, near-black surround, warm bulb cluster top-left of centre. No caption on f0.
- **f1**: "How" appears at full white. Small words follow at f5 ("will"), f10 ("you") and f14 ("even"). They are spread across 0.69 W at one baseline (y≈0.57 H), wide spacing, so each word lands like a separate beat.
- **f5–f55, push-in**: the masked direct fit gives ×1.65; the chain fit gives ×1.57. The scale steps are 0.1 %/f at f1–4, then 0.9 → 3.2 %/f (f7→f14 peak), 1.5 %/f at f20, 0.5 %/f at f30, and <0.1 %/f after f55. So 1.0→1.35 happens in f5–20 (0.5 s) and the remaining 1.35→1.6 eases out over 35 f. This is an aggressive ease-out (fast attack, long settle), and the frame is fully stable for the second half of the hook.
- **f20**: "Master" (big, 2.3×) pops at 31% opacity, ramps linearly to 100% by f30 (10 f), and a cyan swoosh (#2EC0D7) draws left→right under it in f23–28.
- **f33**: the whole group clears in 1 frame (opacity 0.98→0.09). **f34** "your" → **f39** "Personal" (big, 7 f ramp) → **f48** "Branding" (big). Its swoosh draws f50–53. Clears at **f58**.
- **f59** "if", **f61** "you", **f64** "can't" → **f73** "remember" (36%→100% by f82) → **f85** "your" → **f90** "script?". Its swoosh draws f93–97 and the shot holds to f99.
- **Audio**: a sub-bass boom 0.1–0.8 s (sub band peak −16 dB at 0.4 s) gives the open weight. Then the kick is removed 1.0–3.3 s (sub −35 to −45 dB vs −18 dB in the body) so the question sits on a thin bed. The full beat drops at 3.36 s, 1 frame after the cut to white.
- **Why it works**:
  - The question is voiced with no lead-in.
  - The first caption arrives in 33 ms.
  - Motion is concentrated in the first 0.5 s, when the scroll decision is made.
  - The three swooshes give three micro-rewards in 3.3 s (0.77 s, 1.67 s, 3.10 s).
  - The question ends exactly where the music drops and the luma flips (12→255), so the answer is promised with a sensory jolt.

## 3 Typography and captions

- **Typeface** (visual guess): a heavy geometric sans of the Gilroy ExtraBold / Montserrat ExtraBold class, with double-storey a and tight negative tracking. One weight for both tiers. Size and opacity create the hierarchy, not weight.
- **Sizes** (measured glyph heights at 720 w): small supporting words ≈22 px ascender (≈30 px font ≈ 2.3% of frame height); big keywords ≈45–58 px (median ≈50 px, ≈68–70 px font ≈ 5.4% H); ratio ≈2.3×. List labels ("Hook," etc.) ≈46 px, standing alone.
- **Which words are big**: content words (nouns, verbs, adjectives: trick, break, ideas, forcing, exact, lines, loud, couple, natural, story, friend, forget, what, say, speak, camera). Function words stay small (the, to, is, of, it, a, you, your, and, &). About 40–45% of words are big.
- **Position**: every group is centred at x = 0.49–0.51 W. The block spans y 0.56–0.74 H (chest to lap, under the mic hand, never over the face) and is 0.39–0.69 W wide (median ≈0.48 W).
- **Line stacking**: a zig-zag stack with negative leading. Lines overlap by ≈5 px; for example "trick" ends at y 805 and "break" starts at 800. Small words are tucked into the cap-height gaps beside a big word ("**trick** is to", "them into" right-aligned above "**ideas**", "**feels** until it"). Lines alternate left/right offset by ≈0.1–0.15 W.
- **Words on screen at once** (speaker shots): 3–9, median 6, mean ≈5.6. A group lasts 19–56 f (mean ≈40 f = 1.33 s). Groups clear in 1 frame, and the next group's first word appears on the same or the next frame. The list section switches to 1–2 words per card.
- **Per-word animation in**:
  - Small words go to full in 1–2 frames ("will": dim at f5, full at f6).
  - Big keywords pop at 31–39% opacity on frame 1, then ramp roughly linearly to 100% over 7–10 frames (Master 10 f, remember 9 f, Understand 7 f, forget 7 f). The first 3 frames read as grey text.
  - No visible position or scale animation (≤ ≈5%, not resolvable through hand motion).
  - The same grey→solid build is used in black on white (sound: 26%→100% over 12 f).
- **Animation out**: none per word. The whole group cuts out in 1 frame at the start of the next phrase.
- **Colour / effects**: pure white #FFFFFF on the speaker, #100D11 black in white scenes. No stroke and no measurable shadow on the speaker captions: mean luma in a 4–12 px ring around glyphs is 87–88 vs 82–83 at 24–32 px, so there is no dark halo. Black text in the white scenes has a soft grey shadow (≈). The cyan #2EC0D7 accent swoosh is used only in the hook and under "Understand".
- **Occlusion / depth**: none. Captions always sit in front of hands and forearms (verified f254–258 "trick/break", f555–564 "forcing" over the crossed hand, f939–948 "much" over the open hand). No roto.
- **Sync** (first-visible frame minus Whisper onset, n = 53 words across 0–30 s): median **+0.8 f**, IQR −2.0…+2.6 f; 70% within ±3 f and 92% within ±5 f. Examples: How +1, will −2, Master −1, Personal +2, remember −1, script? −2, trick +4, break +4, ideas +2, sentences −2, Hook −2, Example +1, Ending +3, practice −2, repeat +1, sound +2, robotic +4, forget +2, what +1, say −1, next +4. So captions land *on* the word, not ahead of it. Exceptions:
  - Chapter-card words lead the VO by 2–8 f ("First" −2, "& Third" −5, "Second" −8).
  - The cage sentence appears whole ≈1 s before "scripts" is spoken.
  - "word" on grid paper is +9 f late because the scene change waited for the cage line.
- **Copy edits**: "&" replaces "and" at group starts (inconsistently: "& not into", "& you'll", "& Third", but "and won't", "and remember"). There are typos and VO mismatches ("your scipt", "the scripts" vs the spoken "the script").

## 4 Motion and camera

All moves are digital (scale about frame centre, no rotation measured). The scale factors below come from a direct SIFT similarity fit to each shot's first frame with the caption band masked (`work/direct.py`). The chained fit is in `data/scale_chain.json` and the absolute values vs f900 are in `data/scale_vs_f900.json`. The previous analyst's files hold per-frame [scale, rot°, tx, ty, inliers, matches]. The chain version under-reads by ≈5% where static captions dominate the matches.

| shot | frames | start framing (vs f900) | move | rate |
|---|---|---|---|---|
| Hook | f0–99 | ≈0.77 (widest) | eased push-in ×1.57–1.65, f5–55, peak 3.2 %/f at f13–14, 70% done by f20 | ≈+60% in 1.7 s, then hold 1.5 s |
| Tip intro | f220–313 | ≈1.12 | linear push-in ×1.05–1.09 | ≈+2.4 %/s |
| List | f367–451 | ≈0.85 | 4 stepped punch-ins, each 6–8 f eased (ease-in-out, 1.3–2.5 %/f peak): +13.4% (f367–373), +15.1% (f385–392), +6.5% (f405–411), +12.4% (f442–450). Holds are dead-still (<0.1 %/f) | total ×1.56 (chain) – 1.62 (direct) in 2.8 s |
| Tip 2 | f473–583 | ≈1.35 | linear pull-out ×0.887 | −3.1 %/s |
| Tip 3 | f613–770 | ≈1.31 | linear pull-out ×0.876 | −2.5 %/s |
| Outro | f833–1020 | ≈1.09 | pull-out ×0.818, easing to a stop around f1001 | −3.2 %/s |

- **Pattern**: shots that *explain structure* (hook, list) push in, starting wide. Shots that *deliver a tip* start tight and slowly pull out. Every chapter card hides a framing jump: 1.2→0.85, 1.36→1.35 with the direction reversed, 1.16→1.31, 1.17→1.09.
- **List zoom-bumps**: each step starts 1–4 f before the label appears (zoom f367 / label f367; f385/f389; f405/f409; f442/f443). "and then" (f429) gets no bump, so the 4 bumps fall on the 4 list nouns.
- **No handheld shake** was added: global frame-to-frame dx sd is 0.5–3 px and comes from subject motion.
- **The "small animated element near the top" is not a graphic.** It is a practical light in the set: a cluster of 5 warm out-of-focus bulbs (core #FDEE96, brightness sd 1.0 over 188 f, so no flicker). It moves exactly with the digital zooms. In the outro it travels from (226,55) to (251,159) as the pull-out moves it toward frame centre, at the predicted ≈0.6 px/f. It slides out of the top during the hook push-in (gone by ≈f40–44) and re-enters at f545 during the tip-2 pull-out. It reads as "animated" because the zooms carry it in and out. It works as a warm accent in the top third that echoes the orange rim. It is absent from all white and title scenes.
- **White-scene motion**: the card settles from 0.61→0.52 W in 3 f (f100–103, ease-out). The whole canvas drifts slowly (paragraph blocks move ≈1 px/f). The push-left at f144–151 runs at ≈35→25 px/f on the card edge (decelerating). The robot rises from below frame with rotation over ≈12 f and then bobs (≈).
- **Title-card motion**: the background ribbons rotate and drift slowly (mean abs frame diff 0.19/255, almost static). The text has no motion other than the grey→white ramp.

## 5 Transitions catalogue

| # | where (frames) | recipe | why there |
|---|---|---|---|
| T1 Luma-flip hard cut | f99→100, f770→771 (also back: f219→220, f832→833) | 0-frame cut, dark TH (median luma ≈12) to pure white #FFFFFF (luma 255). The first instance coincides with the beat drop (+27 ms) and a stereo transient 113 ms before the cut (≈ riser) | The biggest possible pattern interrupt, placed exactly at the end of the hook question (3.33 s) and before the payoff line ("never sound robotic"). The brightness change alone resets attention without a whoosh-flash |
| T2 Card scale-settle | f100–103 | The live speaker is placed in a rounded card (r≈24 px, soft drop shadow) at 0.61 W on frame 1, which settles to 0.52 W in 3 f (ease-out) | Changes mode (explainer) without losing the face or the lip-sync. The card says "this is a video about videos" |
| T3 Canvas push-left | f144–151 | The whole white canvas translates left ≈720 px in ≈7 f, decelerating. The next composition enters from the right | Moves between two metaphors in the same white world, so it reads as one continuous scene. Stereo transient at 5.05 s (≈ whoosh) |
| T4 Breath cut to empty stage | f189→190 | Hard cut to empty grid paper, 3 empty frames (f190–192), then the type builds | The empty grid makes the "word / by / word" build feel like writing on a page |
| T5 Chapter-card cut | f313→314, f451→452, f583→584 | Hard cut 47–307 ms after the VO phrase ends. The card is a reusable clip restarted at frame 0 each time. Text pops 1–5 f in (grey→white over 3–4 f). Lengths 53 f / 21 f / 29 f | Fills the breath between tips with a progress marker. The structure is visible ("First… Second… & Third") and gives the eyes a 0.7–1.8 s rest from the face |
| T6 Return-on-the-word | f366→367, f472→473, f612→613 | Hard cut back to TH 7–113 ms before the first word of the next phrase, at a new framing scale | The face returns exactly as the next idea starts. The scale change makes the cut read as a new angle |
| T7 Zoom-bump | f367–373, f385–392, f405–411, f442–450 | 6–8 f eased digital punch of +7…+15%, starting 1–4 f before the list label | Gives each list item a physical "hit" without cutting away. Stereo transient on bump 2 (12.91 s) |
| T8 Caption group wipe | every group change (≈25 times) | Opacity 0.98→0.09 in 1 f. The next word appears on the same or next frame | Keeps the caption zone always occupied and rhythmically refreshed (≈1.33 s per group) |

No dissolves, flashes, light leaks, glitches, masks or whip-pans were used. Every transition is a hard cut or a layout move.

## 6 Motion-graphic devices and metaphors

1. **Live video card in an editorial white canvas** (f100–144). The speaker footage keeps playing in a rounded dark card (0.52 W × ≈0.29 H, r≈24 px, soft grey shadow). Around it: a dark grey crescent ribbon (leading line from bottom-left to top-right, grows in f101–108) and 2 blocks of ≈8 px body copy ("Scripting is the process of writing short programs called 'scripts'…") as editorial texture. It works because it keeps the face, changes the brightness world, and makes the content look like a "post" (meta for creators). The body copy is unreadable noise that implies "lots of text to memorise".
2. **Brain in a birdcage on grid paper** (f145–189). A blue glossy 3D brain inside a silver wire cage, on a square of graph paper with a soft vignette. The copy surrounds it: small "you don't actually" above, small "need to learn" plus big "your scipt" below. Metaphor: rote memorising = a trapped mind. It works because one object carries the "don't" and lands within 0.5 s.
3. **Typographic mimicry, "word by word"** (f190–219). The words build one at a time, each grey→black, on the grid square. Form = meaning: the phrase is literally built word by word.
4. **Chapter-card template** (f314–366, f452–472, f584–612). Blue-black #020308 field, slowly drifting dark ribbons with silver-to-cyan edge highlights (#5D5E62→#BAB7BB), sparse dust specks. Centred text at ≈0.43–0.50 H: small label + big word, with a cyan arc under the big word on card 1. The same clip restarts each time (template reuse = cheap consistency).
5. **3D mascot pun** (f804–832). A cute black-and-mint robot (cyan eyes) flies up from bottom-left on "will never" and settles beside "**sound / robotic,**". It literalises the word and adds a laugh beat at the emotional payoff. The text block re-centres as each word is added, then makes room for the robot.
6. **Cyan swoosh underline** (hook only, f23–28, f50–53, f93–97, plus the arc f342–346). A brush-stroke under the final keyword of each hook group, ≈0.15 W long, drawn in 5–6 f, starting ≈3 f after the keyword pops. It gives a micro-reward at the end of every caption phrase in the hook.
7. **Practical bulbs as a "free" animated accent** (see §4). The zooms carry the bulbs in and out of frame, so motion appears without any graphics work.

## 7 Colour and finishing

| element | value |
|---|---|
| Background (side strips, 5–50% H) | median #040004 (luma 1.4), p95 luma 21–23. Crushed blacks with a faint magenta/purple bias (R≈B>G) |
| Frame luma | p1 / p50 / p99 = 0 / 5–17 / 202–251 (very low key; whites near clip only on captions and shirt highlights) |
| Hair rim (frame-right of her head) | peak #DC8438 (hot orange), median #953C26 |
| Cool fill/rim (frame-left arm, shoulder, glasses) | #465C70 (steel blue). A two-tone orange/blue split |
| Skin (face) | median #9C7668 (≈#A27D73 in the wide outro); neutral-warm, not pushed orange |
| Shirt | #B4A6A6 (mauve-pink white). This is the caption backplate |
| Practical bulbs | #FDEE96 core with orange falloff |
| Accent | cyan #2EC0D7 (bright core #3CD0EB) |
| White MG scenes | #FFFFFF field (78–96% of pixels pure white), grid lines #F1F1F1, structure #ECE9ED, type #100D11, card shadow ≈#352B2D |
| Chapter cards | field #020308, ribbon edges #5D5E62→#BAB7BB, text #F1EFF3 |

- **Contrast math**: white caption on the shirt gives a WCAG ratio ≈2.35:1 (shirt relative luminance 0.397). The captions read through weight and size, not contrast (see §10).
- **Grade intent**: the face is the brightest skin-tone object, and the rim separates hair from a black background that has no detail. The white MG scenes are pure white with no grade, which maximises the flip.
- **Finishing**: no grain, vignette, flash or LUT-look overlay measured. The sub-bass and the white flips carry the "energy". The export is 720×1280, so a ≈1.6× digital zoom on the hook and list is only clean if the source was ≥1080×1920 (≈ not verified).

## 8 Sound

- **Music**:
  - Hi-hats sit on a strict 0.2254 s grid (134/161 air-band onsets within ±25 ms). That is 8th notes at **133.1 bpm** (equivalently triplets at 88.7 bpm, which is why the earlier tempo read said 88/133).
  - The kick/808 sub band p90 sits at −18 dB in every second from 3.36 s to the end. The mid-band spectral flatness is 0.02–0.08 (tonal bed).
  - The mix is nearly mono (side/mid RMS 0.106).
- **Arrangement**:
  - 0.1–0.8 s: sub boom.
  - 1.0–3.3 s: kick removed (sub −35…−45 dB) under the question.
  - **3.36 s: full beat drop, 27 ms after the first cut** (f100).
  - From there it loops unchanged to 34.03 s with no outro tail. The final 0.17 s after the last word is music only.
- **Cuts vs beat grid**:
  - Cut offsets to the hat grid are −34, −91, +112, +75, −22, +2, +96, −65, +18 and +56 ms. That is 3/10 within ±34 ms, against 30% expected by chance.
  - Keyword pops score 7/23 (30% vs 30% chance). All caption words score 25% vs 30%.
  - **Hit rate is at chance.** Apart from the hook drop, cuts and captions are timed to the voice, not the music.
  - The earlier `scorecard.json` "sfx_on_cut 80%" is an artifact: with hats every 225 ms, every cut is within ±113 ms of an air onset.
- **Cut vs VO**: every mode change sits in a VO gap, +47…+307 ms after the phrase ends and 180–313 ms before the next phrase. Returns to the speaker land −113…+187 ms around the next phrase's first word.
- **SFX**: there are 20 stereo (side-channel 1–16 kHz) transients that are not hats. 7 of 20 visual events have one within ±120 ms (35% vs 14% chance):
  - riser into cut 1 (3.22 s)
  - cage push (5.05 s, ≈)
  - chapter-1 arc (11.49 s)
  - cut to list (12.28 s)
  - zoom-bump 2 (12.91 s)
  - "& Third" cut (19.50 s)
  - robot entrance (26.82 s)

  So the SFX are sparse, used on graphic moves rather than on every cut, and are ≈ whooshes or pops (not isolated from stems).
- **Loudness and balance**:
  - Integrated −14.1 LUFS, true peak −0.8 dBTP, LRA 1.0 LU (heavily limited, constant).
  - Music-only gaps run at −18.7 dBFS RMS vs −15.5 dBFS with VO, so the bed is hot, only ≈3 dB under the full mix.
  - There is no measurable ducking of the kick (sub p90 is constant at −18 dB through speech).
- **VO**: 127 words in 34 s (224 wpm), 261 wpm in the hook. The longest pause is 0.52 s (19.16→19.68, covered by "& Third"). The VO is never silent for more than 0.52 s.

## 9 Storytelling and retention devices

| t | device |
|---|---|
| 0.00 | Question hook voiced from frame 0. It targets an identity goal ("personal branding") and a pain ("can't remember your script") |
| 0.03 | First caption on f1. Word-by-word build from then on (a new word every ≈0.27 s, never more than ≈1.3 s without new text) |
| 0.17–0.67 | 70% of a ×1.6 push-in happens in the first half-second |
| 0.77 / 1.67 / 3.10 | Cyan swoosh micro-rewards, one per caption group |
| 1.0–3.3 | Beat removed: tension under the question |
| 3.33 | Triple interrupt: luma flip 12→255, beat drop (+27 ms) and mode change to motion graphics |
| 3.58–7.06 | Contrarian reframe ("you don't actually need to learn your script word by word"), with 3 visuals in 4 s (≈1.3 s each) |
| 7.33 | "but the trick is…": the turn, back on the face at a new scale |
| 10.47 / 15.07 / 19.47 | Numbered chapter cards (First / Second / & Third). Visible progress means viewers know how much is left. Card length shrinks 1.77→0.70→0.97 s as the pattern becomes familiar |
| 12.23–15.03 | A 4-item list with a zoom-bump on each noun: a concrete takeaway (Hook, Main Point, Example, Ending) that invites a screenshot |
| 23.42–25.54 | Relatable simile ("like you're just telling a story to a friend") |
| 25.70 | Second luma flip plus a 3D mascot pun on the emotional payoff ("never sound robotic") |
| 29.04 | CTA as a challenge ("Try this in your next video and you will see…") |
| 33.14–33.86 | Callback to the hook ("remember the script" ↔ "remember your script?"). The file ends 0.17 s after the last word, so the loop restarts straight into the question that this ending answers |

## 10 Weaknesses and mistakes (so we can surpass it)

1. **Typo on screen**: "your scipt" for 1.3 s (f151–189), in the biggest type of that scene. The end caption "the scripts" also doesn't match the VO "the script".
2. **Wrong filler copy**: the decorative paragraph is a definition of *computer* scripts ("…short programs called 'scripts'… automate tasks… add functionality to applications"). Anyone who pauses on it sees a semantic mismatch.
3. **Broken reading order in the stacks**: layout beats syntax, which costs comprehension at 224 wpm. Examples: "practice / it in your **saying** / own / words", "repeat / it out **loud** a / **couple** / **times** of", "& you'll **how** / see **much** / easier", "**feels** until it / natural".
4. **Legibility on the shirt**: white text on #B4A6A6 is ≈2.35:1 with no stroke or shadow. Keywords enter at 31–39% opacity, so for 3–4 frames they are grey on pinkish-white and nearly invisible on the chest (f20–22, f73–75, f849–851).
5. **The music is ignored**: cut and caption timing hit the beat grid at chance rate (30% vs 30%). The only musical edit is the 3.36 s drop. The bed is hot (≈3 dB under the mix) with no ducking, which competes with fast VO.
6. **True peak −0.8 dBTP** is above the usual −1.0 dBTP delivery ceiling, so it may clip after platform transcode.
7. **The ending is visually flat**: the last shot is 6.27 s (18% of runtime), with only a −3 %/s pull-out and captions during the CTA. There is no end card, no graphic and no SFX button. Retention risk is highest exactly where the CTA lives.
8. **Chapter cards cost 3.4 s (10%) with no new information**: the VO already says "First/Second/Third". The template is identical each time (same clip, restarted), and "Second" at 0.70 s is a flash. "& Third" uses "&" as if continuing a sentence.
9. **Uneven sync in the graphics scenes**: the cage sentence pre-reveals ≈1 s early, "word" is +9 f late, and "and that way," sits alone on a 93%-white frame for 0.77 s followed by 2 empty frames. That is the lowest information density in the reel.
10. **Inconsistent micro-style**: "&" vs "and". Cyan accents appear only in the hook and on card 1 and are then dropped. The second white scene has no card or ribbon language from the first.
11. **No occlusion or depth play**: captions sit flat on top of hands even when a hand crosses them (f555–564, f939–948). A cheap roto-behind on 1–2 keywords would add depth.
12. **Heavy digital punch**: ×1.6 on a 720-wide export risks softness on the hook face if the source is 1080p (≈, not verified).

## 11 Steal list (recipes with numbers)

1. **Hook push-in**: open on your widest framing. Start an eased digital push at f5, peak at 3%/frame around f13, reach ×1.35 by f20 and ×1.6 by f55, then hold dead still. All the motion lands in the first 0.5 s.
2. **Two-tier caption stack**: heavy geometric sans, function words ≈2.3% H, content words ≈5.4% H (2.3×). Centre at 0.50 W, block in 0.56–0.74 H (below the chin, on the torso), 3–9 words per group (median 6), ≈1.3 s per group, negative leading (lines overlap ≈5 px). Fix it: keep reading order left→right, top→bottom, and add a 2–3 px dark stroke or 30% shadow when the backplate is light.
3. **Keyword fill-in**: content words pop at 35% opacity and ramp linearly to 100% over 7–10 f; function words are full in 1–2 f. Clear the whole group in 1 frame on the next phrase.
4. **Word-onset sync**: first-visible frame = VO onset +1 f (target IQR ±2 f). Only chapter titles may lead, by 2–8 f.
5. **Accent swoosh**: a cyan (#2EC0D7) brush underline, ≈0.15 W long, under the last keyword of each hook group. It draws left→right in 5–6 f, starting 3 f after the keyword pops. That gives 3 micro-rewards in the first 3.3 s.
6. **Beat drop on hook exit**: sub boom on 0–0.8 s, cut the kick from 1.0 s to the end of the question, then drop the full beat within 1 frame of the first cut. Our upgrade: also snap later cuts to the 8th-note grid (225 ms at 133 bpm).
7. **Luma-flip cut**: go from a low-key TH (median luma ≈10) straight to a pure #FFFFFF canvas on the last syllable of the hook. No flash is needed; the 12→255 jump is the flash.
8. **Live video card**: put the speaker in a rounded card (0.52 W, r≈24 px, soft shadow) that settles from 0.61 W in 3 f (ease-out), plus a dark crescent ribbon that grows in 6 f behind it as a leading line. Use real, on-topic micro-copy as texture.
9. **Canvas push**: switch between metaphors with a ≈720 px push-left in ≈7 f, decelerating (≈35→25 px/f), plus a stereo whoosh.
10. **Chapter-card template**: a blue-black #020308 field with slow 3D ribbons (silver/cyan edges), restarted from frame 0 each time. Small label + big word centred at ≈0.45–0.50 H, text in 1–5 f. Cut in 50–300 ms after the phrase ends; cut back on the next phrase's first word at a new framing scale (≥15% different). Keep each card 0.7–1.8 s.
11. **List zoom-bumps**: each list noun gets a 6–8 f eased punch of +7…+15%, starting 1–4 f before the label pops. Hold dead still between bumps. Put a pop SFX on at least one bump.
12. **Breathing pull-outs**: on tight delivery shots, add a linear −2.5…−3.2 %/s digital pull-out for 3.7–6.2 s and ease it to a stop over the last ≈0.6 s. Let practicals at the frame edge slide in and out as free motion.
13. **Mascot pun on the payoff**: on the key adjective, fly a 3D character in from below frame with rotation over ≈12 f, with a stereo pop at its entrance (±20 ms). Re-centre the black text block as words are added.
14. **Grade**: crush the background to ≈#040004 (luma 1–2), with a hot orange hair rim (#DC8438 peak) on one side and a steel-blue fill (#465C70) on the other. Keep skin ≈#9C7668, and put warm bulb practicals (#FDEE96) in the top third, out of focus.
15. **Breath-cut and loop rules**: put every mode change in a VO gap (+50…+300 ms after the phrase end). End the VO on the hook's own object ("remember the script") and end the file ≤0.2 s after the last word. Our upgrade: −1 dBTP ceiling, duck the bed 3–4 dB under the VO, and add a 1–1.5 s visual button on the CTA.
