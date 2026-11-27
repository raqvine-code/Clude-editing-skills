# Typography pairings for talking-head captions (client font board)

Source: a client font-pairing board: one talking-head frame (dark green slatted wall, red/white check shirt, Telugu-English
speech) set in six type treatments, each labelled with free fonts and the client reference it substitutes. Palette tag
"M4 haldi / kumkum / cream". Visual reference: `frames/type-pairing-crops.jpg` (text-only crops, open it before building).

Evidence limits: this is a **static board**. Sizes, positions and colours below are **measured** on it (panel 374×666 px,
percentages of frame width W / height H). Nothing about motion timing was measured: the reel itself was not available
(the Instagram link resolved to a designer's "font pairings you must try" carousel, only its cover was public). Rules marked
*recommendation* are mine, not read off the board. Frame values for animation come from the main skill's measured recipes.

## 1. The favourite: pairing 1 ("same INGREDIENTS")

Fonts (board label): **Playfair Display 800 Italic** (small word) + **Poppins ExtraBold, caps** (big word). Both free on
Google Fonts (check the licence before commercial delivery). Client reference it matches: "Playfair + Poppins".

| Part | Measured on the board |
|---|---|
| Small word "same" | lowercase italic serif, cream `#F3EFE3` (core `#F1F0E4`), x-height 3.0 % H, width 24 % W |
| Big word "INGREDIENTS" | heavy geometric sans caps, haldi `#E1A92C` (core), width 79 % W (10 %–89 % W), cap height ≈ 5 % H |
| Stack | big word on the lower line; small word sits above-left, 1.4 % W inside the big word's left edge; line gap ≈ 1.8 % H |
| Block position | top of block 21.8 % H, bottom 31.5 % H; head top is at 34.8 % H, so ≈ 3 % H of clear wall between type and hair |
| Contrast on the wall (`#2D3329`) | haldi 6.1:1, cream 11.4:1: no stroke or backing needed on a dark wall |
| Size ratio | small italic ≈ 80 % of the sans font size (≈, from x-height vs cap height) |

Why it works: one quiet word and one loud word. The italic lowercase serif reads like a spoken aside ("same"), the sans caps
read like the claim ("INGREDIENTS"); they differ on four axes at once (serif vs sans, italic vs upright, lowercase vs caps,
cream vs haldi), so the hierarchy is read in one glance and no box or stroke is needed. The gold word is the only coloured
thing on the frame, so the eye lands on it first. It is the two-tier caption of R1 and R4 with a more premium voice.

Recipe (1080×1920):
1. Pick the keyword (the noun or claim). Set it in Poppins ExtraBold caps, tight tracking (≈ −10 to −20), colour `#E1A92C`.
   Size it so the word is **75–85 % of W** wide (≈ 810–920 px) then check cap height ≈ 4.5–5 % H (≈ 86–96 px) for a long word.
2. Set the small word above it in Playfair Display 800 Italic, lowercase, `#F3EFE3`, ≈ 80 % of the sans size, left edge ≈ 1.4 % W
   inside the big word's left edge, ≈ 35 px above the caps.
3. Place the block with its top at ≈ 22 % H and ≥ 3 % H clear above the speaker's hair. Reframe the speaker (scale/position) so
   head top ≈ 35 % H if you need this headroom.
4. Animate with the skill's text recipes: small word in on its onset (blur 14→0, y +10→0, 6–8 f), big word on its onset
   (keyword fill 7–10 f or tracking-in 6–8 f, optional sub boom on the keyword). Hold until the phrase ends, clear in 1 frame.
5. CSS sketch: `.big{font:800 var(--big)/1 Poppins;letter-spacing:-.01em;text-transform:uppercase;color:#E1A92C}`
   `.small{font:italic 800 calc(var(--big)*.8)/1 'Playfair Display';color:#F3EFE3}`: tune `--big` until the big word measures
   79 % of the frame width.

## 2. The six pairings (measured)

| # | Fonts (board) | Roles | Big word width / cap height | Colours | Block y (% H) | Use for |
|---|---|---|---|---|---|---|
| 1 | Playfair Display 800 Italic + Poppins ExtraBold caps | small serif italic / big sans caps | 79 % W / 5 % H | cream + haldi | 21.8–31.5 | default: statements, nouns, values |
| 2 | Yellowtail script + Anton | small script over big condensed caps, overlapping | 75 % W / 15 % H | cream script, kumkum `#D2483D` caps, ink outline | 14.9–32.9 | loss, waste, anger, a warning: ≤ 2 words per reel |
| 3 | Inter Tight 800 + DM Serif Display Italic | small sans / big serif italic | 85 % W / 9.5 % H | cream + haldi | 21.0–33.3 | questions and reflections ("difference?") |
| 4 | Instrument Serif caps + Italianno + kumkum dot | small serif caps / big script | 76 % W / 12.8 % H | cream + haldi, red dot `#C34D3F` | 15.2–36.8 | premium or inclusive beats ("all companies"); script is slow to read, keep it to one word |
| 5 | Bricolage ExtraBold + Archivo Expanded Black | small sans / big wide caps | 83 % W / 7.1 % H | haldi small, cream big | 21.6–40.8 | authority, money, share, numbers; big word runs behind the head |
| 6 | Poppins ExtraBold + Pinyon Script, blur reveal | staggered small sans words + script keyword fading in | n/a (torso band) | cream words, haldi script | 59–66 | connective words on the torso, fast stretches |

What all six share:
- **Two voices per card**, never three, in different classes (serif/script vs sans) or widths (condensed vs expanded).
- **The big word is 75–85 % of W wide**, whatever its length: size to the word, not to a fixed point size (WASTE in Anton ends
  up 15 % H tall, INGREDIENTS 5 % H).
- **The small word is 22–52 % of W**, left or centre aligned, never right.
- **Everything sits in the top 40 % of the frame** (block top 15–22 % H, bottom ≤ 41 % H), above the face on the empty wall. Pairing 6
  moves down to the torso band instead.
- Text is flat colour (no gradient, no bevel); the only effect on the board is the ink outline in pairing 2.

Code-mixed (Telugu in Latin script + English) logic visible in the examples: the **small words are the connective/function
words** (ekkuva ≈ "more", kaani enduku ee ≈ "but why this", ANNI ≈ "all", prathi woman ki ≈ "for every woman", kooda vaallaki ≈
"also to them"; glosses are my reading, confirm with the client) and the **big word is the English concept word** (WASTE,
INGREDIENTS, difference, Companies, SHARE). Rule: glue small, concept big. Pick one romanisation scheme and have the client
approve spellings once (Whisper will not give clean Latin-script Telugu).

## 3. Colour roles (palette M4)

| Colour | Measured | Role |
|---|---|---|
| Haldi (turmeric) | `#E1A92C` core, `#DCAA35` median | the emphasis colour for the keyword; default big-word colour |
| Kumkum (vermilion red) | `#D2483D` | loss, waste, danger; also a one-dot accent (`ANNI •`) |
| Cream | `#F3EFE3` | the small word and any neutral big word (SHARE); never pure white except the torso words (`#FEFAF0`) |
| Ink | `#351C0F` (median of the dark ring around the red letters) | outline for kumkum, shadow colour |
| Wall (grade) | `#2D3329` top-left, dark green slats | keeps the type zone dark and quiet |

Matches the red-for-threat / gold-for-opportunity logic measured on R4. **Warning from the board itself:** kumkum on the dark
wall is only **2.9:1**, below the skill's 4.5:1 floor. Pairing 2 solves it with a dark ink outline plus huge size; if you use
kumkum on small text, lift it toward `#E85A4A` or outline it.

## 4. Layering and overlap

- **Overlap (pairing 2):** the cream script sits over the top-left of the red caps, covering ≈ 25 % of the cap height; it works
  because the script is a different colour class and the caps are very tall.
- **Behind the head (pairing 5):** confirmed on a zoom: the hair covers the top of the "A" of SHARE, so the word is masked
  behind the speaker (roto or a person-matte). It adds depth and ties type to the speaker; keep the loss to the top of one
  letter (the word stays readable because the caps are wide). Do not do it on a word that is a hair too small to survive a mask error.
- Pairing 1 sits fully above the head: the safe default when no matte is available.

## 5. Selection rules (recommendation)

1. One **primary** pairing per reel (pairing 1 for this client) for most cards; **at most two special pairings** (e.g. 2 for the loss
   word, 3 for the question). Six pairings are options, not a menu to use in one video.
2. Keep colour roles fixed all reel: haldi = emphasis, kumkum = loss/threat, cream = glue.
3. Alternate the card layout (overlap, behind-head) only on the beat the story turns; the rest stays clean.
4. Leave the Reels header clear: block top ≥ 14 % H (the board's highest top is 14.9 % H).
5. Spell-check every card against the spoken line, including the transliteration.

## 6. Open items

- Upload the client reel (mp4) to measure timing: per-word entrance frames, sync to onsets, how long cards hold, whether the
  keyword uses the blur reveal that pairing 6's label mentions. Until then use the skill's measured defaults.
- The Instagram cover shows the same principle at the extreme (tiny sans label + giant italic serif word): scale contrast as the
  main hierarchy tool.
