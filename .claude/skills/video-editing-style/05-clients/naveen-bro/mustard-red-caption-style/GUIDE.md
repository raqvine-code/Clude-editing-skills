---
name: mustard-red-caption-style
description: Use for the subtitles / captions of every short for the client who asked (2026-11-25) for "aesthetic subtitles in mustard yellow and red" (the Naveen bro Telugu and English shorts), and whenever a request says mustard captions, yellow and red subtitles, aesthetic subtitles, podcast serif captions, golden caps, vintage / film yellow subtitles. Only the caption layer changes; cuts, B-roll, giants, grade and sound stay as the other skills say. Default look M4 "Haldi-Kumkum" (Claude's own signature design for this client - turmeric + vermilion, Fraunces Soft Italic keyword, Bricolage Grotesque ghost lead-ins, haldi brush under hero words, kumkum dot full stop; tools/restyle_edl.py converts any EDL). Three more looks learned from 11 measured Instagram / YouTube references - M1 podcast serif (cream caps lead-in + mustard bold-italic serif keyword, Figuring Out style), M2 golden caps (one line of condensed caps, keyword mustard, Kobe / Hormozi style), M3 film subtitle (small sentence-case soft-mustard subtitle, Instagram vintage trend) - one fixed palette (mustard #E2AA2C, brick red #D2483C for negative words only, cream #F4EFE3, ink #1A1410), shortkit settings, QC. Also holds the client's font-pairing brief (round 4, 2026-11-25): six two-font pairing moments set above the head (section 2c).
---

> **Scope: client (Naveen bro shorts). Use only for this client, or when a request says mustard / yellow-and-red / golden-caps / podcast-serif captions.**

# Mustard-red caption style (client request, 2026-11-25)

**Why it exists:** the client was disappointed with the current edits. Their words: subtitles must be **aesthetic** and use **mustard yellow and red**, "rest all good". So this skill changes the caption layer only. Everything else follows `shorts-editing-pro` and the event-map method as before.

**Sources:** 8 reference shorts measured frame by frame on 2026-11-25 (table, colours, sizes, links: `references/reference-reels.md`), plus web search. Style frames on the client's own footage: `references/frames/` (made by `tools/style_frames.py`; the Pink Tax engine test is `engine_test_pinktax_M1_M2.jpg`).
Labels: **M** = measured in a reference, **O** = observed by eye, **C** = Claude's synthesis (not in any reference).

**Waiting on the client:** which look (M4 / M1 / M2 / M3), and any reference reels of their own (`edits/mustard-red-captions/inbox/README.md`). Until they choose, **M4 Haldi-Kumkum is the default** (section 2b; pitch board `references/frames/HALDI_KUMKUM_style_board.png`, 11.6 s sample `edits/mustard-red-captions/previews/signature/Pink_Tax_HaldiKumkum_sample.mp4`). M1 is the safe fallback (the look of the biggest Indian podcast pages, R1). **Round 4 (2026-11-25):** the client sent font pairings and a reel; they are adapted as pairing moments above the head (section 2c), and M4 stays the running caption.

## 1. Palette (fixed for this client, every video)
| Role | Hex | Source |
|---|---|---|
| Keyword (the word that carries the line) | mustard `#E2AA2C` | **C**, between R4 gold `#F6C703` / R5 amber `#FFC213` and the dull film mustard of R6, pulled down per `beginner-to-pro-edit-tips` rule 3 |
| Film-subtitle body text (M3) | soft mustard `#E0BE60` | R6 (**M** `#B8A244` with edges, core about `#D9C050`) |
| Negative / warning word (not, no, kaadu, ledu, waste, scam, the price that hurts) | brick red `#D2483C` | **C** from R3 (`#F85355` glow / `#AE312A` body), dulled: no `#FF0000` |
| Lead-in words | cream `#F4EFE3` | rule 3: no pure white for large text |
| Outline + shadow | ink `#1A1410` | warm near-black, no `#000000` |

Rules:
1. **Mustard on the keyword only**, one per caption group. Never a whole video of mustard lines (R5 is loud, not aesthetic).
2. **Red is rare:** only on a negative or warning word, at most 1 caption group in 4. Never mustard and red on the same word. Mustard + red share a group only as "keyword + its negation" (LUXURY / KAADU).
3. **Never pure yellow** `#FFFF00`-`#FFFF4A`: it is the cheap clip-page look (R2).
4. **Red always gets a 4-6 px ink outline + soft shadow.** The client's speaker often wears a red-and-white checked shirt right under the caption zone (videos 22-24); without the outline red disappears into it. Never put red text on red B-roll; swap to cream there.
5. Check every keyword colour against the picture under it (Pink Tax lesson: contrast beats colour-role). Mustard on a yellow or wooden B-roll → cream keyword with a mustard underline (`"bar"`) instead.

## 2. The three looks
### M1 podcast serif (fallback) - from R1 Figuring Out
- **M** Small caps lead-in in a geometric sans + ONE big bold-italic high-contrast serif keyword under it. The stack builds word by word on the voice and clears together.
- Fonts: lead-in Montserrat Bold (caps), keyword Playfair Display ExtraBold Italic. Alternates from the list: Poppins SemiBold caps; EB Garamond Bold Italic.
- Sizes (1080x1920): lead-in 56-64 px caps, keyword 140-160 px, keyword never wider than 860-900 px (**M** R1: serif about 5.5 % of height, caps about 2.1 %).
- Keyword lowercase (it reads "aesthetic"); lead-in caps. Red negative word: the keyword of its own group in red serif, or a red caps lead-in.
- Soft same-colour glow 0.3-0.35 on the serif keyword only (the one attention element, rule 2).

### M2 golden caps - from R4 Kobe edit + R5 Hormozi
- **M** One line of heavy caps, 2-3 words (never more: a 4-word line shrinks to fit and reads small, seen in the engine test). Cream words, the spoken keyword in mustard, a negative word in red.
- Fonts: Montserrat Black or Oswald Bold (condensed, closest to R4); Anton or Impact as the heavier stand-in.
- Size 96-115 px, line at most 900 px. Hard pop on each word (shortkit pop), no other effect.
- Best for punchy motivational / rant lines; with a B&W stretch (`"desat"`) the mustard word looks like R4. Use B&W only where the plan already wants it (client said the rest is good).

### M3 film subtitle - from R6 (Instagram "vintage yellow subtitles" trend)
- **M** Small sentence-case subtitle, centred low, soft mustard, thin dark edge; **C** one word in red.
- Font Inter Tight 500 (Helvetica-like) or Montserrat Medium; 50-56 px; y 1480-1520 (above the platform UI); 1-2 lines.
- Calm story or emotional lines only.
- **Clash:** a sentence subtitle breaks `mistakes-to-avoid` E11 (keyword captions only, max 1-4 words). Use M3 only if the client picks it, and say so first (CLAUDE.md Rule 3).

## 2b. M4 Haldi-Kumkum (Claude's own look, default) - 2026-11-25
> **Font override (user, 2026-11-26): no Bricolage Grotesque + Fraunces Soft Italic for this client.** The user's words: "dont use all fonts types use only best font combination" and "Bricolage Grotesque with Fraunces Soft Italic dont use these use i gaved image ... take best fonts combinations". So M4 keeps its palette and mechanics (ghost lead-ins, blur reveal, haldi brush, kumkum dot) but takes ONE pairing from the client's carousel (section 2c). Default: **Poppins SemiBold** lowercase lead-ins (58 px) + **Playfair Display ExtraBold Italic** keyword (148 px), with Poppins ExtraBold caps for any big word (pairing A). Two families per video, nothing else: no Impact, no mono HUD label, no script on the chest. First used on video 25 (Uncertainty Truth English).

**Idea (C):** read the client's "mustard + red" as **haldi + kumkum**, turmeric and vermilion, the pair every Telugu home knows (puja, weddings, the doorstep). The palette stops being "two random colours" and becomes a cultural signature, worn softly like an editorial magazine. Built on what the aesthetic references share (A1, A2, R1: moody picture, mixed-weight type, ONE warm italic word, few effects).
| Element | Spec |
|---|---|
| Lead-in words | Bricolage Grotesque SemiBold, lowercase, cream `#F4EFE3`, 60 px, 3 px ink outline. **Ghost line** (`"ghost": 0.30`): the whole lead-in waits at 30 % and each word goes solid on its spoken time (A2). Needs one token per word with its own time; phrase tokens show all at once. |
| Keyword | Fraunces Soft Bold Italic (opsz 144, SOFT 100, WONK 1: soft, retro 70s italic, "modern retro serif" trend), lowercase, haldi `#E2AA2C`, 150 px, glow 0.25 |
| Hero keyword (up to 4 per video, the longest-held keyword in each 12 s, never a negative word) | cream keyword on a **haldi brush stroke** (`"brush": "#E2AA2C"`): textured, dry-brush edges, soft ends, behind the lower half of the word, wipes left to right in 0.22 s (documentary highlighter, A4; mistakes-to-avoid 9: a highlighter, never a slab) |
| Negative / warning word | Fraunces in kumkum `#C8372D`, no glow, ink outline |
| **Kumkum dot** (`"dot": "#C8372D"`) | a small vermilion dot sits on the baseline after the keyword that ends a statement (next caption 0.35 s+ later), 0.12 s after the word, pops from 1.5x; at most 1 per 8 s; never after ? ! . , - the look's signature full stop |
| Effects budget | brush and dot are the only special moves; nothing shakes, glitches or flashes in the caption layer (beginner-to-pro rule 2) |
Convert any finished EDL: `python3 -I 05-clients/naveen-bro/mustard-red-caption-style/tools/restyle_edl.py <edl.json> <out.json> M4 [--project <dir>]` (also `M1`, `M2`). Per-word overrides in the EDL: `{"role": "neg" | "key" | "hero" | "dot" | "nodot"}`. Pitch board for a client: `tools/style_board.py`.
**Optional finish (only if the client wants more than captions):** one grade across the whole video, slightly lower saturation (A1 25 %, A2 36 %), warm highlights, fine grain 0.035 (documentary realism / phone-first cinematic lane, OpusClip 2026). Not applied to the sample: the client said the rest is good.
**Giants:** existing giant words keep their own colour (Pink Tax's rose "PINK TAX" is the topic colour). For a new video, giants in cream with a haldi swap keep the palette whole.

## 2c. Client font pairings: round 4 (client brief, 2026-11-25)
**Built since (2026-11-25, late):** the reel's "stack that builds word by word" is now shortkit `stacks` (skill `text-animation-moves`): fixed layout, big + small words, a letter-by-letter type-on hero word, blur / rise / grain arrivals and a sound per move. A pairing moment can be a stack whose hero word uses `"font": "script"` or `"serif"`. Stacks run on the chest with the ink outline (2 lines at most); above the head only as one of the 1-3 accents.

**Brief:** the client sent a font-pairing carousel and a reel of how words should appear, "as reference, not like that". Measured in `references/client-font-brief.md`; adapted on the client's footage in `references/frames/PAIRINGS_board.jpg` (tool `tools/pairing_board.py`, tiles in `edits/mustard-red-captions/previews/pairings/`).

**What it changes:**
- Running captions stay M4 in the chest zone.
- On top of them come **pairing moments**: the hook title, a number, a short label: 1-3 accent texts above the head per short in total, counting giants and stacks too. The running subtitles stay on the chest under the chin, with the block centre at 58-65 % of the height (user feedback 2026-11-25: "full subtitles in upper head looks heavy"; researched in `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`). Each is set as a two-font title in the plain wall above the head (y 300-640; the hair top is about y 660), like the carousel's type over empty sky.
- Each moment uses ONE pairing from the menu.
- Each video keeps **one or two pairings**, never all six (the rule of three families in `pro-font-and-subtitle-guide`).

| # | Pairing (free fonts) | Client ref | Use on | shortkit |
|---|---|---|---|---|
| A | Playfair Display 800 Italic small + Poppins ExtraBold caps big | Playfair + Poppins | a fact / proof word ("same INGREDIENTS") | `giants` Poppins caps (haldi) + group `"y"` with a Playfair keyword `"font": "PlayfairDisplay-ExtraBoldItalic.ttf"` above (static 800 instance in the library) |
| B | Yellowtail script over Anton caps | Billion Dreams + Anton | the negative word ("ekkuva WASTE", caps in kumkum with the ink outline) | `giants` Anton + a script keyword group at the same y |
| C | Inter Tight 800 small + DM Serif Display Italic big | Acumin Pro + Times | the question line ("kaani enduku ee difference?") | group `"y": 560`, lead-in + keyword `"font": "DMSerifDisplay-Italic.ttf"` |
| D | Instrument Serif caps small + Italianno big + kumkum dot | Spire + Italianno | the topic / brand word ("ANNI• Companies") | group `"y"`, keyword `"font": "Italianno-Regular.ttf", "size": 1.8` (the dot after the caps is drawn as a layer) |
| E | Bricolage ExtraBold small + Archivo Expanded Black caps behind the head | Satoshi + wide caps | the one big idea ("prathi woman ki SHARE") | `giants` `behind: true`, Archivo Expanded; the hair covers only the feet of the letters |
| F | Poppins ExtraBold lowercase words + one Pinyon Script keyword, stair-step stack, blur reveal | the reel | an emotional / hero line ("vaallaki kooda teliyaali") | group `"y"`, `style.reveal: "blur"`, keyword `"font": "script"` with `style.script_font` Pinyon |

**Rules:**
1. **Two fonts per moment**, contrasting on two axes (sans vs serif or script, upright vs italic, caps vs lowercase). The big word is 2.5-4x the small one. Tracking is tight on heavy caps and big italics, and lines may touch.
2. **Thin scripts (Italianno, Pinyon) only on the plain wall or a paper scene, at 200-300 px.** Never in the chest zone over the checked shirt: the test still `references/frames/client-font-brief/test_italianno_on_shirt.jpg` is unreadable. In the chest zone the keyword stays Fraunces Soft Italic.
3. **How words appear** (from the reel):
   - one word at a time;
   - a fade of about 0.17 s, or a blur reveal (dim and soft to sharp in about 0.2 s, `reveal: "blur"`);
   - hero lines build as a stack, word by word;
   - a soft shadow, no boxes.
4. **Colours stay the client's palette:** cream small words, a haldi big word, kumkum only on negative words. The carousel's white and lime are not copied. An accent may be picked from the scene only if it is haldi or kumkum.
5. **No Telugu-script font** (user, 2026-11-25: "dont use telugu font"): lines stay Tenglish in these Latin fonts. Telugu script only if the user asks for it by name; then see `pro-font-and-subtitle-guide` section 6.
6. `giants` take the full font path; keyword `"font"` takes a library file name.
7. **Fonts named by the client that are not free** are swapped for free fonts (table in the reference file, section C). Tell the user if the client asks for the exact font.

## 3. Placement and timing (all looks)
- Chest height, centre x, y 1150-1330 for M1 / M2 (house rule from `shorts-editing-pro`); never over the mouth. R1 places the stack beside the face: **not copied**, our framing centres the speaker and the side is often a hand or a gesture.
- Word in-point = the word's first frame (envelope onset), up to 1 frame late, never early (house rule). Group clears in 1 frame at the next phrase or cut.
- Captions hide while a giant word or full-screen scene is up (unchanged).
- Telugu speech stays Tenglish (romanised), as spoken.

## 4. shortkit settings (`02-craft/shorts-editing-pro/tools/shortkit.py`)
Added on 2026-11-25 for this style (defaults keep older EDLs unchanged): `style.cap_color` and a per-word `{"c": "#hex"}` on lead-in words; `style.ghost` (alpha of not-yet-spoken lead-in words); keyword options `"brush": "#hex"` (haldi stroke) and `"dot": "#hex"` (kumkum dot). Fonts for M4: `03-sound-type-assets/fonts-and-colours/assets/fonts/BricolageGrotesque-SemiBold.ttf`, `Fraunces-SoftBoldItalic.ttf`.
```json
M1: "style": {"accent": "#E2AA2C", "cap_color": "#F4EFE3", "stroke": 4,
              "cap_font": ".../Montserrat-Bold.ttf", "key_font": ".../PlayfairDisplay-ExtraBoldItalic.ttf",
              "cap_size": 62, "key_size": 150, "key_max_w": 880, "cap_y": 1290}
    words: [[t, "IDI", "n"], [t, "luxury", "k", {"c": "#E2AA2C", "glow": 0.3}]]   then  [[t, "kaadu", "k", {"c": "#D2483C"}]]
M2: "style": {"accent": "#E2AA2C", "cap_color": "#F4EFE3", "stroke": 5, "cap_font": ".../Montserrat-Black.ttf", "cap_size": 100}
    words: [[t, "IDI", "n"], [t, "LUXURY", "n", {"c": "#E2AA2C"}], [t, "KAADU", "n", {"c": "#D2483C"}]]
M3: group "y": 1500, all words "n" in sentence case, cap_font Inter Tight 500, cap_size 50, cap_color "#E0BE60", red word {"c": "#D2483C"}
```
Font files on this Mac: Montserrat Bold / Black `edits/telugu3/assets/fonts/`, Playfair ExtraBold Italic `edits/telugu4/assets/fonts/`, Inter Tight `edits/telugu2/assets/fonts/`, Oswald `03-sound-type-assets/fonts-and-colours/assets/fonts/`. Copy the ones used into the project's `assets/fonts/`.
Working converter from an old EDL (uppercase lead-ins, keyword colours): `edits/mustard-red-captions/code/test_edl_M1.json` / `_M2.json` show the result for Pink Tax.

## 5. Claude's ideas (C, not in any reference; use when they fit the plan)
1. **Price in mustard, the extra in red:** when the speaker names two prices, the fair one is mustard and the extra amount is red (Pink Tax-type videos). One per video.
2. **Mustard underline wipe** (`"bar": "#E2AA2C"`) under a cream keyword where mustard text would sit on a warm or busy picture.
3. **Loop word:** the last caption of the video uses the same mustard serif word as the first one (frame 0 = the loop frame), so the short repeats cleanly.

## 6. QC (add to the export check)
- [ ] One mustard keyword per group; red on at most 1 group in 4, only on negative / warning words.
- [ ] No `#FFFF00`, `#FF0000`, `#FFFFFF`, `#000000` in caption text (sample one still per look).
- [ ] Every red word has the ink outline and reads over the checked shirt and over each B-roll (check a still per B-roll slot).
- [ ] M2 lines 2-3 words, nothing shrunk below 90 px; M1 keyword at most 900 px wide.
- [ ] Captions land on the word (5 random words checked on a strip), never cross a cut into another picture.
- [ ] Pairing moments (2c): at most one every 6-8 s, at most two pairings per video, scripts only on the plain wall or paper, nothing under the hair line except a `behind` giant's feet.

## 7. Clashes with other skills (say these before editing; CLAUDE.md Rule 3)
- `fonts-and-colours`: one accent per video, a new one every video. **This client fixes two colours (mustard + red) for all their videos.** Client request wins for their videos; other videos keep the rotation.
- `fonts-and-colours`: change fonts every video. Keep the client's look recognisable: rotate only inside the look's alternates (Montserrat ↔ Poppins, Playfair ↔ EB Garamond, Fraunces Soft Bold ↔ Black Italic, Bricolage ↔ Inter Tight), never jump to a different look without the client choosing it.
- `fonts-and-colours` "font list is complete": the user approved (2026-11-25) researching and adding free OFL fonts for this client: Fraunces, Bricolage Grotesque, Bebas Neue, DM Serif Display. More fonts still need the user's OK. Later the same day the user asked for the best fonts for every video type (library now 76 files), and for the client's pairing brief Italianno, Pinyon Script, Yellowtail and Instrument Serif were added (all OFL / Apache).
- Section 2c vs `pro-font-and-subtitle-guide` "rule of three families": six pairings exist, but one video uses one or two of them plus the M4 caption fonts. Never use all six in one short.
- `mistakes-to-avoid` E11 (keyword captions only): M3 sentence subtitles break it; M1 / M2 follow it.
- `beginner-to-pro-edit-tips` rule 3 (no bright red): the palette uses dulled red and mustard. If the client wants brighter "pure" colours, ask before switching.
