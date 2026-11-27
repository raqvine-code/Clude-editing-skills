# Client font brief: round 4 (2026-11-25)

**What arrived:** the user passed on instructions from the client (Naveen bro shorts).
- Six screenshots of a font-pairing carousel.
- One reel link showing "how fonts should appear in the video".

**The user's words:** "just take that as reference, not like that", so the brief is a direction to adapt, not a layout to copy.

**Study only** (CLAUDE.md Rule 1.6): nothing from these posts goes into a delivered edit.

**Files:**
- Screenshots: `frames/client-font-brief/carousel_shot_1-6.jpg`.
- Our adaptation on the client's footage: `frames/PAIRINGS_board.jpg` (tool `../tools/pairing_board.py`).
- Full-size tiles: `edits/mustard-red-captions/previews/pairings/`.

## A. The carousel: raktimcreates "font pairings you must try" (1,661 likes, 572 comments, 84 shares, 7 slides)
Each slide: one photo with the subject in the lower half, the type in the empty upper half, and a label naming each font (the labels are the carousel's own device, not for video).
| Slide | Small word (role, font) | Big word (role, font) | Placement / trick | Colour |
|---|---|---|---|---|
| 1 cover | "font" bold grotesk, "YOU MUST TRY!" tracked caps | "pairings" heavy high-contrast serif italic, huge | the serif word is about 3x the sans; two round dots as accents | white on sky blue |
| 2 | "think" / "trends" bold serif italic (**Playfair Display**) | "BEYOND" heavy geometric caps (**Poppins**) | italic words tucked top-left and bottom-right of the caps, lines touching | white |
| 3 | "Beyond" brush script (**Billion Dreams**) | "ORDINARY" condensed heavy caps (**Anton**) | the script overlaps the top of the caps | caps in a dark teal taken from the water, script white |
| 4 | "simply" bold grotesk (**Acumin Pro**) | "stunning" heavy serif italic (**Times New Roman** bold italic) | very tight tracking; a round dot as the tittle above | white |
| 5 | "create your" bold geometric lowercase (**Satoshi**) | "LEGACY" wide heavy caps | the hat covers the lower middle of the giant word (text behind the object) | small line lime, giant white |
| 6 | "FIRST" condensed high-contrast serif caps (**Spire**) | "Design" formal script (**Italianno**) | script about 4x the caps, a dot after the caps word | white |

**Rules taken from it** (O = observed):
1. **Two fonts only.** They contrast on two axes at once: sans vs serif / script, upright vs italic, caps vs lowercase.
2. **One word is the picture, the other is the whisper.** The size ratio is about 1:2.5 to 1:4.
3. **Tight is premium.** Negative tracking on heavy caps and big italics. The lines touch or overlap (the script crosses the caps).
4. **Type lives in the empty part of the picture** (sky, wall), and the subject sits under or in front of it. On slide 5 the object covers the word.
5. **One small accent:** a dot or a colour pulled from the photo. Never a second loud colour.

## B. The reel: tobydeboer "Grind szn" (2,818 likes, 10 comments, 8.1 s, 16:9 1916x1078)
**What it is:** a cinematic music montage (city at dusk, desk, trading screens, bed). Measured with `06-tools/_video-analysis-tools/browser_reference_capture.js` (picture only; sound not measured).
| Thing | Measured |
|---|---|
| Cuts | 22 in 8.05 s, average shot **0.35 s** (8 fps diff, threshold 30) |
| Words | **one new word per shot**: "Yeah · What if i lost it all and i started at zero, what would i do to become my best? working everyday of the week for the past few days i ain't even slept" |
| Two fonts | most words: a bold geometric sans in **lowercase**, small (cap height about 4-5 % of the frame); emphasis words ("What", "what", "become", "Slept", "Yeah"): a formal high-contrast **script**, about 2-2.5x bigger |
| Colour | all white, a soft dark shadow, no outline, no box |
| Arrival | the sans word fades in about **0.17 s** (5 f at 30 fps, grey to white); the last word of a stack arrives **blurred and dim, sharp by 0.23 s** (= our `reveal: "blur"`) |
| Stacks | a phrase can build word by word while the shots keep cutting ("to" / "become" / "my" / "best"). Lines are staggered left and right, with tight leading: the script touches the sans |
| Placement | beside the person in the empty part of the frame (sky, window, wall), never over the face; it moves shot to shot |
| Loop | the last shot equals the first shot (foggy window, "Yeah"), so it loops cleanly |

## C. What it means for the client's shorts (talking head, 9:16, Telugu in English letters)
- **Their footage has the same empty space as the references:** the plain green / grey wall above the head (y about 200-640 of 1920; the hair top is near y 660). Put the pairing moments there, but only as 1-3 accents per short (hook title, number, label; `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`). The top 270 px is covered by the app's own interface, so at camera 1.25 the usable wall is only about y 270-450. User feedback 2026-11-25: full subtitles above the head look heavy, so the running subtitles stay in the chest zone (y 1150-1330), which sits on a red-white checked shirt and needs the ink outline.
- **Thin scripts (Italianno, Pinyon Script) are unreadable on the checked shirt.**
  - Test still: `frames/client-font-brief/test_italianno_on_shirt.jpg`.
  - Scripts go on the wall above the head (or on a paper scene), at 200-300 px.
  - In the chest zone the keyword stays M4 Fraunces Soft Italic, with the ink outline where needed.
- **Keep the client's cut:** we don't copy the montage's one-word-per-cut pace. The reel's rhythm is adapted instead:
  - one word at a time (M4 ghost lead-in + keyword);
  - a 0.17-0.2 s fade or blur reveal;
  - a stack that builds word by word on the hero lines.
- **Colours stay the client's palette** (haldi / kumkum / cream / ink). The carousel's white-and-lime looks are not copied.
- **Fonts the client named that we can't use as-is:**
  | Named font | Licence | Free substitute | Notes |
  |---|---|---|---|
  | Acumin Pro | Adobe Fonts, subscription | Inter Tight 800 | |
  | Times New Roman | macOS system font | DM Serif Display Italic, or the system Times New Roman Bold Italic | render it into the video only, never ship the file |
  | Billion Dreams | personal-use licence | Yellowtail | Apache 2.0 |
  | Spire | commercial licence | Instrument Serif | OFL, condensed |
  | Satoshi | Fontshare free licence | Bricolage Grotesque ExtraBold | add Satoshi only if the client insists |
  | Playfair Display, Poppins, Anton, Italianno | free (OFL) | none needed | already in the library |
