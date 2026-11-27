---
name: text-animation-moves
description: Use whenever on-screen words must arrive with a designed move in a short or long video - a word stack that builds word by word on the chest under the chin, a letter-by-letter type-on keyword, blur / rise / grain / pop / cut arrivals, big meaning words with small link words, faceless one-word kinetic typography - and for the sound of each move. Measured 2026-11-25 from three Instagram reels (a "$5 vs $80 edit" pro version, a faceless kinetic-type reel, the client's Grind szn reference). Built into shortkit as the "stacks" key, SFX "ss" slices and tools/sfx_measure.py.
---

# Text animation moves (learned 2026-11-25)

**Why it exists:** the user asked for client-level edits, then said "dont do edits now just learn skills". The gaps between our shorts and the client's references were:
- shortkit could not build a multi-line word stack;
- words arrived only with a pop or a blur, with no letter-by-letter type-on;
- text moves had no sound recipe.

This skill closes those gaps. No video was edited while learning it; the tests are stills only.

**Read with:**
- `shorts-editing-pro`: the build.
- `aesthetic-pro-reel-edit-style`: the P16 insert menu. A stack counts as an insert.
- `mustard-red-caption-style`: M4 captions and the 2c pairings.
- `event-map-reel-edit-style`: every word arrival is an event for the 1.3 s rule.
- `beginner-to-pro-edit-tips`: smaller, fewer effects, dull colours.
- `ue-sound-design` and `sound-and-music-design`: sound levels.

## 1. Measured references (study only, CLAUDE.md Rule 1.6)
Measured with `06-tools/_video-analysis-tools/browser_reference_capture.js` (picture only; the sound of these reels is unknown). The frames are in `references/frames/ref_*.jpg`.

### A. shami.mp4 `DKC2AJ0z6s0` (50K likes): a "$5 vs $80 edit" of a Mark Tilbury talking head, 16.1 s
The $80 version is the pro one: a 16:9 talking head inside the 9:16 post. Frames: `ref_shami_pro_stacks_*.jpg`, `ref_shami_type_letters_30fps.jpg`.

| Thing | Measured |
|---|---|
| Stacks | Sentences build word by word into a stack in the empty side of the frame. The side changes each sentence: "if you / don't wanna / be like / everyone / else" (left), "then you / have to / make the / sacrifices" (right), "others / aren't / willing to" (left) |
| Type | One heavy geometric sans, lowercase, white, soft shadow, no box |
| Sizes | Big meaning words are about 2.3x the link words (ratio about 0.42). A big and a small word can share a baseline ("**have** to") |
| Leading | Lines almost touch. The descender of "everyone" tucks over "else" |
| Hero word | "everyone" types on letter by letter, synced to the spoken word: 8 letters in 0.37 s (1.37 to 1.73 s). Each new letter is faint for 1-2 frames, then solid |
| Link words | appear whole in 1-2 frames |
| Exit | The stack clears on a hard cut at the sentence end (gone between 2.33 and 2.37 s), and the next stack starts on the other side in the same frame. No exit animation |
| Quiet line | "that's what my mentor told me." goes back to a one-line lower caption with the keyword in bold, after a punch-out. Quiet beats get small captions |
| Into a story insert | punch-in, then the frame dims in 4 frames (7.02 to 7.15 s) to a navy scene with a picture card and a "Young Mark" title |
| Cuts | none found in 16 s (6 fps frame diff). The pro version moves with punches and text, not with cuts |

### B. yp.motionstudio `DYnW0cCIlry` (28K likes): "Your brand deserves more than basic edits", 9.4 s, faceless kinetic type
Frames: `ref_ypmotion_*.jpg`.

| Thing | Measured |
|---|---|
| Rhythm | One word per shot: 22 cuts in 9.3 s, average shot 0.40 s. It speeds up towards the end: 0.6 s, then 0.4, 0.3, and 0.2 s at "repe." / "repeat." |
| Background | Every cut flips between black and white |
| Arrivals | **grain**: a speckled dissolve, sharp in 3 frames ("we", 0.00 to 0.07 s). **slam**: the word is at full size on the cut frame with no move ("edit"). A liquid ink matte transition at 3.05 s. A type-on for the last word |
| Scale contrast | a small word next to a word that fills the width ("just" / **edit**) |

### C. tobydeboer "Grind szn" (the client's reference)
Measured earlier; see `mustard-red-caption-style/references/client-font-brief.md` B.
- The sans fades in over 0.17 s.
- The last word goes from blurred to sharp in 0.23 s.
- Stacks are staggered left and right.
- The script emphasis word is 2-2.5x the size of the sans.

## 2. The move menu (shortkit `stacks` token `fx`)
| fx | What happens | Timing | Use it for | Sound (section 5) |
|---|---|---|---|---|
| `cut` | the word is there on its frame, no move | 0 | a word that lands on a camera cut or a beat; faceless slams | click or pop on the frame |
| `fade` | alpha in, out-cubic | 0.10 s for link words, 0.17 s for big words | the default; always for link words | none |
| `blur` | blurred to sharp, 35 % to 100 % alpha, scale 1.05 to 1 | 0.18 s | calm big words; the last word of a stack | low shimmer, or none |
| `rise` | slides up 0.35 em while fading in | 0.20 s | a big word that opens a line | soft whoosh, peak aligned |
| `grain` | speckled dither dissolve | 0.10 s | tech / digital / "data" words; faceless reels | digital blip |
| `pop` | scale 1.12 to 1 in 5 frames | 0.08 s | a punchy word or a number | pop |
| `type` | letters appear one by one across the spoken word, each fading in over 0.07 s | 0.045 s per letter (0.15 to 0.6 s), or `"dur"` = the word's spoken length | the ONE hero word of a stack | typing burst sliced to `dur` |

**More moves, added 2026-11-27** (measured on four editor-showcase reels; full recipes in `04-styles/editor-showcase-caption-edit-style/GUIDE.md` section 4). They render as front `layers` with that skill's `tools/caption_moves.py`, not as `stacks` tokens:
| Move | What happens | Timing | Use it for |
|---|---|---|---|
| `writeon` | a script (or italic serif) phrase is uncovered left to right through a soft blur; small sans words fade in beside it | 0.4-0.53 s for three words; clears in 1 frame | the calm premium caption (P20) |
| `pill` | dark full-radius pill with a glow blob wipes in left to right; two can stack | 0.2 s each | a pair of nouns ("the insecurities, the flaws") |
| `converge` | two hero words slide in from the left and right edges with motion blur | 0.3 s | a hook line with two halves ("nine / ten times") |
| `typecard` | full-frame accent plate + hero word (ghost to solid) + tiny lines; hard colour inversions; optional window that closes in round the live speaker | hold 0.3-2.5 s; inversion 0.3-0.5 s | a one-word claim; the speaker-in-card insert |
| `tiles` | 1-2-3 diamond tiles pop (ghost, then lit); the named one rolls to its word | pops 0.2-0.33 s apart; fly 0.55 s | a spoken list ("one of these three things") |
Clash to know: those references start a keyword 6-8 frames early so it is sharp ON the spoken word; rule 3 below (never early) stays the default until the owner says otherwise.

**Rules:**
1. **At most two fx kinds in one stack** (beginner-to-pro: fewer effects). Link words always use `fade`.
2. **At most one `type` per stack, on the meaning word.** Set `dur` to the word's spoken length from the transcript, so the last letter lands when the word ends.
3. **Every word starts on its spoken time, never early** (house rule).
4. **Ghost (future words shown faint) is optional:** 0.2-0.3, only on a plain wall. The reference reels don't use it.

## 3. Word-stack layout (9:16 talking head)
**User feedback, 2026-11-25:**
- First: "full subtitles in upper head looks heavy, adjust, not all text in upper head". The first test had every stack above the head (`references/frames/STACKS_v1_all_above_head_REJECTED.jpg`).
- Then: "first dont create by you own just research". So the placement below comes from research, not from Claude's own guesses. It combines platform safe zones, two eye-tracking studies and about 15 short-form reels studied earlier. It is all in `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`.

The fixed demo is `references/frames/STACKS_test_sheet.jpg`, with full-size crops in `STACKS_lower_zone_fullsize.jpg`.

1. **Where:**
   - **Default: on the chest, just under the chin** (where the studied reels put their running captions; the eye-tracking studies say near the face but never on the mouth).
     - Centred at x 540, with the block centre at **58-65 % of the height (y about 1110-1250)**.
     - The block's bottom stays above y 1470 (the bottom UI on Reels and TikTok), and its lines stay within x 120-960.
     - On a busy shirt give the stack the ink outline: `"stroke": 3`. A red word on the client's red-checked shirt needs `"stroke": 5`.
     - No thin scripts here.
   - **Above the head: accent text only.**
     - Below the top UI band (y 270), down to the hair top; at camera 1.25 on the client's footage that is about y 270-450. Check a still for every video.
     - It holds the hook title, a number headline, or a short label: **1-3 per short in total** (`shorts-editing-pro` rule 8; Tharun Speaks measured).
     - Never the running subtitles, and never a whole sentence-stack. No studied reel runs its subtitles above the head.
   - **Beside the face:** only when there is real empty space (a wide podcast shot, an off-centre speaker, 16:9 inside 9:16), changing sides each sentence (A).
2. **Content:** one sentence in 2 lines at most on the chest: a small line plus the keyword line, the two-tier card measured in R4, P6 and P8. Use 3-5 lines only in real side space. Big tokens (`"b"`) are the meaning words; small tokens (`"s"`) are the link words ("if you", "be like", "to", "the").
3. **Sizes:**
   - on the chest: big words 100-110 px, `ratio` 0.5 (link words about 52 px);
   - above the head: big words 110-150 px, `ratio` 0.42;
   - a link word is never under 44 px (phone check).
4. **Leading and alignment:**
   - `lead` 0.06: the lines nearly touch.
   - `center` above the head, `left` / `right` beside a speaker, `stagger` for the cinematic look.
5. **Colour and font:**
   - One colour for the stack plus one accent word. For the client that is cream plus haldi, with red only on negative words (mustard style).
   - One font family in two weights.
   - A serif or script swap only for the single pairing word, and a script only on the plain wall (mustard 2c).
6. **Behind the head:** `"behind": true` puts the stack behind the head, so the hair covers the bottom of the word. Use it for one big word only, size 180-220.
7. **Exit:**
   - `t1` = the sentence end: the stack clears hard, and the next stack or caption starts on the same frame.
   - Use `"out": "fade"` only for the last stack before a calm beat.
8. **Budget:**
   - A stack on the chest is a subtitle with a designed build. Use it on hero sentences (about one every 6-10 s); the other lines stay M4 captions.
   - Quiet or reflective lines go back to the small lower caption (A).
   - Above the head, only as one of the 1-3 accents (rule 1).
9. **Captions:** normal captions are hidden while a stack is up; shortkit does this.
10. **No Telugu-script font** (user, 2026-11-25: "dont use telugu font"): the client's lines stay Tenglish in Latin fonts. Use Telugu script only if the user asks for it by name.

## 4. In shortkit (`02-craft/shorts-editing-pro/tools/shortkit.py`, 2026-11-25)
```json
"stacks": [{"t0": 0.5, "t1": 2.0, "y": 110, "x": 540, "size": 112, "align": "center",
            "lines": [[[0.5, "if you", "s"]],
                      [[0.65, "don't wanna", "b", {"fx": "rise"}]],
                      [[0.9, "be like", "s"]],
                      [[1.05, "everyone", "b", {"fx": "type", "c": "#E2AA2C", "dur": 0.36}]],
                      [[1.45, "else.", "s"]]]}]
```
- **Stack keys:**
  - `y`: the top of the stack, in 1080x1920 px.
  - `x`: the stack's centre.
  - `align`, `max_w` (the whole stack scales down to fit), `size`, `ratio`, `lead`, `stagger`.
  - `fx` (stack default), `ghost`, `behind`, `out`.
  - `c` (big-word colour), `cs` (small-word colour), `font` (big words: `"serif"`, `"script"` or a library file).
- **Token:** `[t, text, "s"|"b", {opts}]`. Opts: `fx`, `c`, `font`, `size` (multiplier), `d` (seconds), `dur` (type), `glow`, `stroke`. Tokens in one line share a baseline.
- **Style keys:** `stack_font` (default `cap_font`), `stack_small_font`, `stack_size`, `stack_ratio`, `stack_lead`, `stack_fx`, `stack_color`, `stack_stroke` (ink outline in px, also used on type-on letters).
- **SFX slice:** `"ss"` (start in the file) with `"dur"` cuts a typing burst to the word.
- **Demo:**
  - `tools/stack_demo_edl.json` holds four stacks on the client's raw, with their sounds; the project is `edits/text-animation-moves-demo`.
  - Three stacks sit on the chest (top y 1120, block centre about 63 %, size 104, ratio 0.5, `style.stack_stroke` 3; "aren't" in kumkum with stroke 5).
  - One accent sits above the head as a single line: Yellowtail "willing to" + "WORK". Its top is at y 285, below the top UI band, and it ends above the hair. Safe-zone overlay check: `references/frames/STACKS_safe_zone_check.jpg` (red = UI, cyan = the 58-65 % subtitle band).
  - Stills: `$PY shortkit.py stills tools/stack_demo_edl.json 0.72,1.22,1.9,2.24,2.73,3.3,4.5,5.9 --scale 0.5`.
  - The result is `references/frames/STACKS_test_sheet.jpg`, all on the chest except the last: rise mid-way, type on "ever", the full stack, blur on "have", grain on "sacrifices", the full second stack, "others **aren't**", then the one above-head accent, "willing to WORK".

## 5. Sound for each move (files on this Mac; chosen by numbers, because Claude cannot listen)
**How the files were chosen:** measured with `tools/sfx_measure.py`, which gives length, peak time, active time, brightness and transient count.

**Level:** shortkit `db` = the cue's loudest 100 ms against the speech average.

**Files:** the Mixkit files are copied into `assets/sfx/` (Mixkit free licence there). The `ui sfx` files stay in `~/Downloads/ui sfx/`, because their source and licence are not recorded.

| Move | File | Slice / align | db | Why (measured) |
|---|---|---|---|---|
| `type` | `~/Downloads/ui sfx/KEYBOARD 1 (1).wav` | `"ss": 0.12`, `"dur"` = type duration, align start | -16 | 29 transients in 0.92 s (about 30 a second, the type-on speed); 92 % of its energy above 4 kHz, so crisp ticks |
| `type`, long word | `~/Downloads/ui sfx/ES_Communications, Typewriter, ... Typing Burst ... Clicking 08 - Epidemic Sound.mp3` | `"ss": 0.04` | -18 | 107 transients in 11 s |
| `pop` | `assets/sfx/mixkit_3005_48k.wav` | start | -14 | 0.18 s long, peak at 0.02 s, dark |
| `cut` / slam | `assets/sfx/mixkit_2358_48k.wav`, or `~/Downloads/ui sfx/Button  (21).wav` | align peak | -12 to -14 | a single transient, peak at 0.02 s / 0.10 s |
| `rise` | `assets/sfx/mixkit_2632_48k.wav` (soft whoosh) | align peak, `"lead": 0.03` (the fastest frame) | -18 | 1.16 s long, peak at 0.42 s |
| `blur` (big word) | `assets/sfx/mixkit_3108_48k.wav` (shimmer) | align peak, `"lead": 0.06` | -20 | 74 % bright, heard for 0.8 s |
| `grain` | `~/Downloads/ui sfx/DATA 2 (8).wav` | start | -16 | a 0.51 s digital blip, heard for 0.10 s |
| pairing / script word | `assets/sfx/mixkit_3062_48k.wav` (sparkle) | align peak | -20 | 98 % bright |
| the stack clearing | nothing (if it is also a camera cut, the cut's own sound) | | | |

**Rules:**
1. Link words are silent.
2. At most 2 sounds per stack (the hero word plus one), and never 2 sounds within 0.25 s.
3. Run `shortkit.py audio` and read the collision table (SFX against voice, 300 Hz-4 kHz). On the demo every cue sat 18-30 dB under the voice: -24.8, -26.5, -27.3, -30.2, -19.6, -18.2, -18.6, with no "masks voice?" flag.
4. **Not a Rule 3 clash:** `ue-sound-design` sets textures at -6 / -7 dB of clip gain. The user's answer of 2026-11-22 ("use when it required") keeps the older rule for the user's own and client edits: textures 15-20 dB under the voice. The levels above follow that.

## 6. Faceless kinetic type (P12 reels only)
From B:
- one word per shot;
- the background flips black / white on each cut;
- the cut rhythm speeds up towards the end (0.6 s down to 0.2 s);
- small word + width-filling word pairs;
- grain arrivals and slams on the cut;
- an ink transition into the turn.

shortkit can come close with a `paper` scene plus one-word stacks (`fx` `cut` / `grain`). A full faceless reel still belongs in the `faceless-explainer-reel-edit-style` pipeline.

## 7. QC (add to the edit's QC list)
- [ ] Phone-size sheet: link words readable (44 px or more); no stack over the eyes or mouth; a script only on the plain wall.
- [ ] The subtitles run on the chest, with the block centre at 58-65 % of the height and its bottom above y 1470. Above-head accents (giants, pairings, number giants): 1-3 per short, below y 270.
- [ ] Every coloured word is readable on the shirt behind it (outline 3; red on the red check needs 5).
- [ ] No Telugu-script font, unless the user asked for one.
- [ ] Every word arrives on or after its spoken frame. Check the still at word start + 1 frame.
- [ ] No word moves while the stack builds (shortkit fixes the layout from all tokens first).
- [ ] At most 2 fx kinds, 1 type-on and 2 sounds per stack.
- [ ] The stack clears on the sentence-end frame; the next element starts on the same frame.
- [ ] The collision table has no "masks voice?" flag.

## 8. Gaps (build when a video needs them; research first, CLAUDE.md Rule 4.3)
- A liquid / ink matte word transition (B, 3.05 s).
- Invert-background one-word scenes as an EDL key.
- A mask-wipe reveal (a moving edge uncovers the word).
- The sound of the reference reels (the browser tool measures picture only).
