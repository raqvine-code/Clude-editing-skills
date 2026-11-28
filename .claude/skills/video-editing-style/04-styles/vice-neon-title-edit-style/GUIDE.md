---
name: vice-neon-title-edit-style
description: Use when a video needs the "Vice City" neon-sunset title look (profile P21) - a number or word drawn as a two-tone neon outline, filled with an indigo-to-orange sunset gradient, a game-style wordmark wiped across it, wide-tracked opener lines that flash and settle, an editorial high-contrast serif card on deep red, and a stacked game-title card with a handwritten aside. Learned from one logo-reveal video and two type posters the owner sent for his own GTA 6 facts video. Holds the measured timing of every move, the palette in hex, three matched free fonts with their licences, the sound pattern (build, then sparse notes that the moves land on) and a working HTML title page with a frame renderer.
---

> **Scope: general, first built for the owner's own channel (a GTA 6 facts video, 2026-11-27).** Client rules always win over a profile. Numbers are labelled **[measured]** (computed from the file), **[seen]** (read off frames) or **[choice]** (my decision when rebuilding).

# Vice-neon title style (P21), learned 2026-11-27

**Why it exists.** The owner sent one video and two posters and said: "Learn these fonts and pictures and video also, because after learn this I will send you one video ... I am telling about GTA 6 facts, means why GTA 13 years takes time ... So use your entire creativity."

**What was studied**
- **R9**, a 26.65 s logo reveal (720x748, 30 fps, one continuous shot on black, no cuts): a studio badge with a light pulse, a "presents" line, then a large numeral drawn in neon, filled with a sunset gradient, and a wordmark wiped across it. Full frame table: `references/r9-logo-reveal-measured.md`.
- **Poster A**, an editorial font poster: high-contrast condensed serif title on a deep-red car interior.
- **Poster B**, a game-title font poster: a stacked white title with a dark outline on a blue-to-pink sky, a handwritten aside with a lime arrow.

Reference work belongs to its makers: study only. **Never redraw a studio's or a game's logo.** Build the moves on our own numbers, words and shapes (the test uses "13" and a striped sun).

## 1. The six moves, with their numbers

| # | Move | What happens | Timing |
|---|---|---|---|
| 1 | **Top-down soft reveal** | a small mark is uncovered from its top edge to its bottom, outline first, letters dim and then brighten | reveal 0.5 s, brighten to 1.3 s [measured] |
| 2 | **Light-sweep pulse** | a glow starts orange at the top edge, travels down and turns magenta at the bottom; one detail (a star) keeps the magenta for a moment | rise 0.33 s (2.67 to 3.00 s), decay 0.8 s, gone by 4.5 s [measured] |
| 3 | **Flash and settle line** | a wide-tracked caps line appears in ONE frame, bright and soft, then sharpens and dims to its resting level | brightness 1.7x to 1x and blur to zero in about 0.35 s; holds 4.7 s; fades out in 0.37 s [measured] |
| 4 | **Neon edge draw** | the outline of the hero numeral is revealed top to bottom at a steady speed, as a thin bright line with a soft glow; left-facing edges are pink, right-facing edges are orange (two lights) | 1.9 s for the full height, linear [measured] |
| 5 | **Fill, bloom, settle** | the inside fills from the bottom up, dark purple first; then the fill brightens into the full gradient while the outer glow fades and the whole mark shrinks slightly | fill 0.7 s; bloom 1.8 s; scale 1.16 to 1.00 over the bloom [measured]; the tool uses 1.13 [choice] |
| 6 | **Diagonal wordmark wipe, in and out** | a three-line wordmark is wiped on from the top-left to the bottom-right, one line after another; the exit is the same diagonal wipe, fast | in 1.0 s for three lines (about 0.33 s a line); hold 3.1 s; out 0.3 s [measured] |

Order in R9 [measured]: badge 0.1-8.0 s, black 0.4 s, line 8.47-13.6 s, black 0.6 s, numeral 14.2-18.5 s, wordmark 18.5-19.6 s, hold to 22.8 s, out by 23.1 s, 3.5 s of black. **Every element leaves before the next arrives; nothing overlaps.**

## 2. Sound pattern [measured; instrument names are a listening model's guess]

- Loudness -14.2 LUFS. No sound effects; the music does the work.
- **Build, then drop to sparse.** 0-14.7 s: an orchestral bed that rises from -19 to -12 LUFS under the badge and the line. At 14.7 s, as the numeral starts, the bed stops and single guitar notes take over with real silence between them (17.5-18.0 s and 19.5 s are near silent).
- **Moves land on notes.** Wordmark starts 18.5 s, note at 18.53 s. Wordmark complete 19.6 s, note at 19.58 s. Exit starts 22.8 s, note at 22.81 s.
- Use: put the reveal on a note or hit, keep 0.3-0.5 s of air before it, and let the last state hold through at least two notes. With a no-music client, a real riser into the numeral and one real hit on the wordmark do the same job.

## 3. Palette

| Role | Hex | From |
|---|---|---|
| Sunset gradient, top to bottom | `#3447B5` indigo, `#7C3CC4` violet, `#C936B6` magenta, `#F0489C` pink, `#F7706A` coral, `#FDA53A` orange | R9 fill [measured, muted by compression: #544998 to #C36D49] lifted toward Poster B's `#FEB423` [choice] |
| Neon edge | `#FF62D6` pink (left), `#FFB45E` orange (right) | R9 [seen] |
| Outline and deep shadow | `#1E0624` plum, `#31072C` | R9 wordmark outline, Poster B title outline [measured] |
| Wordmark face | `#F1EDF6` (R9 shows `#BDBAC3`, a grey-lilac) | [measured], lifted [choice] |
| Opener line | `#E9DDF0` lilac white | [seen] |
| Sky | `#2B3FA6` to `#8B6DE6` to `#FBCDEB` | Poster B [measured] |
| Accents | lime `#9EFE3C` (arrow), hot pink `#FA3BB1`, gold `#FEB423` | Poster B [measured] |
| Editorial card | black `#060101`, deep red `#420303`, red `#942315`, white type | Poster A [measured] |

Rule: one card uses ONE family (sunset on black, or sky, or red editorial). Lime appears once per card at most.

## 4. Type: three voices and a utility face

| Voice | Font | Settings | Licence |
|---|---|---|---|
| Game title | **Pricedown Black** | white face; plum outline 11-15 % of the font size (`paint-order: stroke`); a 3 px hot-pink hairline around the outline; stacked 2-3 lines, line height 0.78-0.86; title 60-75 % of the frame width | free for commercial use, rendered video included (Typodermic Desktop License). **Do not commit the font file**; `tools/fetch_fonts.sh` downloads it |
| Editorial serif | **Noto Serif Display**, width 78 %, weight 400 | tracking -0.065 em so letters touch, word spacing +0.16 em, line height 0.9, two centred lines, 60-68 % of the width | SIL OFL. Chosen from 11 candidates rendered beside Poster A; the poster's own font (Romens Dawn) was not found under a free commercial licence |
| Handwritten aside | **Patrick Hand** | `scaleX(.92)`, 3.5 px stroke to thicken, rotate -3 degrees, a lime up-right arrow before the second line | SIL OFL. Closest of 6 candidates to Poster B's label; a visual match, not the same font |
| Utility | **Inter Tight** (300 for pills, 600 for the opener line), **Inter** 300 for body copy | opener line: caps, tracking 0.34 em, second line smaller at 0.42 em; pill: 62 px, dark glass, 1.5 px light inner edge | SIL OFL |
| Hero numeral | **Inter Tight 900** | 760 px on a 1080 frame, tracking -30 px, clean corners so the neon edge reads | SIL OFL |

## 5. Poster layout rules [seen]

- **Editorial card (Poster A):** full-bleed dark photo or deep-red field; a small glass pill label sits on the title's top-left corner; serif title in the lower-middle; three lines of light body copy near 90 % of the height at about 2 % of the frame height; two or three tiny white squares ("selection handles") as points of light; fine film grain over everything.
- **Game-title card (Poster B):** sky gradient; one large gradient shape behind the title (use our own shape: a striped sun, a numeral); the stacked title overlaps the shape; handwritten aside low-left of the title; a thin barcode strip on the right edge; a subject fills the lower half.
- Both keep the name tag and the "save" tag small in opposite corners. In a video, leave those corners empty unless the owner wants a handle there.

## 6. Using it in a talking-head facts video

1. **Hook:** the key number of the video (for the GTA 6 video: 13) as the hero numeral: moves 4, 5 and 6 over a dark plate, 4-5 s, then cut to the speaker. The wordmark carries the claim in 2-4 words.
2. **Chapters:** one editorial serif card per chapter ("Fact 01" pill plus a two-line title), 1.5-2.5 s, lines rising out of a mask with blur.
3. **Facts on the speaker:** Pricedown for one hero word per beat, outline on, placed with the caption rules of P19 (under the chin, one focal zone); handwritten asides for jokes and side notes only.
4. **Colour:** the sunset gradient is the accent family; keep the speaker's footage natural unless the owner asks for a grade.
5. **Variety:** moves 4-6 are a signature; use the full neon draw once (hook) and at most once more (payoff). Other numbers use a shorter move (wipe or flash and settle).
6. **Footage of the game, its trailers or its artwork** is only used when the owner supplies it and says he has the right to use it. Never invent screenshots, release dates or quotes; facts on screen come from the owner's script.

Floors from `01-process/before-edit/2-PRO-MOVE-MENU.md` still apply (a designed motion graphic every 8 s, a sound on every insert), and so does Rule 0 step 3: plan plus storyboard frames before a full render.

## 6b. Lessons from the first P21 edit (GTA 6 video, 2026-11-27): see `references/worked-example-gta6/`
- **Layout B (the owner's choice):** the talking head sits in its 4:5 window (y 276-1644) between two neon lines, with a small wide-tracked label in the top band. Designed scenes break out to full screen.
- **Captions:**
  - one Tenglish line (Inter Tight 700, plum outline), centred at y 1500, with the spoken word in orange;
  - keep y 1440-1560 clear in every design;
  - keep key items off the right edge (x > 940, y 1000-1700, under the like and share buttons) and below y 1600.
- **B-roll source order:**
  1. the game's official media page (download-and-share zips);
  2. official images on the publisher's site;
  3. evidence pages captured as cards.
  YouTube refuses downloads from a cloud server: ask the owner for the files instead.
- **Facts on screen:** only checked facts. The narrator's opinion stays in his voice. Illustrative charts carry an ILLUSTRATION tag and no invented numbers.
- **Sound without music:** put a short real attack (click, knock, glitch hit, shutter) on every cut, placed by its loudest point, at about −10 dB under the voice. Quieter hits vanish under continuous speech.

## 6c. Owner's notes on the first P21 edit (2026-11-28): apply to his videos
His words: "Remove starting frame and keep my face · Remove tanglish captions entire video · Remove (why) word in that frame · Remove top sentences entire video · Remove time symbol, I dont like that may be add good one · At 34 sec remove frame · At 41 sec remove that frame · At 46 sec that letter (13 years of development) keep small and add that lines on the words properly its not straight · At 50 sec remove that frame".
- **Open on his face,** not on official game art. A punch-in on the first key word replaces the logo hook.
- **No running captions** and **no small sentence pinned at the top** (series labels, kickers). Neon frame lines alone are fine.
- **No handwritten asides** on the hero numeral.
- **No clock or dial icon for "timing".** What he accepted instead: a flip calendar whose real dates peel away and land on the release day, circled in lime.
- **Strike-through lines** must be perfectly straight, measured from each line's own text box (`getBoundingClientRect`), through the middle of the letters. Never hand-placed or tilted.
- **Text over his face stays small** (hero about 118 px, second line about 72 px on 1080 wide).
- **He removed** the GTA V sales-line chart with its counter and headline card, the delay-headline card and the 13-year timeline, wanting his face there instead. **Data-heavy full-screen cards are not his taste:** keep designed scenes for the few beats he keeps (cards, money and timing, the profit bars, the covers).
- With the captions gone, **gentle 5 % punch-ins on one stressed word per sentence** keep the face scenes alive without any graphics.

## 7. Tool

```
bash 04-styles/vice-neon-title-edit-style/tools/fetch_fonts.sh          # once per machine; fonts are not in the repo
cd 04-styles/vice-neon-title-edit-style/tools
node render.js stills OUT_DIR 0.3,4.3,6.2,7.4,9.8,12.6                  # stills at those seconds
node render.js video OUT_DIR 13.5                                       # 30 fps JPEG frames for 13.5 s, then encode with ffmpeg
```
`vice_neon_titles.html` holds four scenes driven by `renderAt(t)`: A opener line (move 3), B neon numeral with wordmark (moves 4-6), C editorial serif card, D game-title card. Change the words in the HTML; the timings are constants at the top of each scene block. It needs the pre-installed Chromium and Playwright (cloud session) or any Playwright install. A sheet of the test is in `references/style-test-sheet.jpg`. About 0.1 s per frame.

## 8. QC for this style

- The neon edge is thin and bright with a soft glow; if it looks like a fat stroke, lower the stroke width before adding blur.
- The gradient reaches orange at the feet of the glyphs (map it to the glyph height, not the text box).
- The fill is visibly dark before it blooms; the bloom takes at least 1.2 s.
- Serif title: letters touch, words do not (check the word spacing).
- Pricedown outline is closed on every letter and no counter is filled in.
- Nothing overlaps between cards: the old element is gone before the new one starts.
- One hero numeral on screen at a time; lime at most once per card.
- No studio or game logo has been redrawn.

## 9. Limits

- One reference video, a compressed 720 px capture: its colours are muted and its sound was identified by a model, not heard. The palette sits between the video and Poster B on purpose.
- The two posters are stills; the motion on cards C and D is my own choice.
- No edit built with P21 has been seen by the owner yet. Treat the numbers as a starting point and show stills first.
