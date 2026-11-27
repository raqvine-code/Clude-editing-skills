---
name: pro-font-and-subtitle-guide
description: Read on EVERY edit before choosing fonts, captions, subtitles, titles, lower thirds or thumbnail text, for any form (9:16 shorts / reels, 16:9 YouTube long-form, podcast clips, documentary, vlog / travel, cinematic / wedding, tutorial / SaaS, ads / UGC, Telugu-script videos). The pro font system researched 2026-11-25 from Instagram editor reels (40K-99K likes), web guides and the Netflix / BBC subtitle specs. It covers which free font fits each video type and role (tested pairs, files in fonts-and-colours/assets/fonts, ₹ and Telugu support marked), subtitle numbers (characters per line, reading speed, durations, sizes, safe zones), contrast, Telugu rules and licensing.
---

# Pro font + subtitle guide (researched 2026-11-25)

**Why it exists:** the user asked (2026-11-25) for the best fonts for short-form, long-form and every other kind of video, aesthetic subtitle fonts and pro standards, all saved as skills and used on every edit. Evidence: 17 Instagram reels where editors show the fonts they use (Inter Black, Apple Garamond, Impact, Akira, Integral, Montserrat, Cormorant, Snell Roundhand, Mea Culpa...), the aesthetic references in `aesthetic-pro-reel-edit-style` (I1-I11) and `mustard-red-caption-style` (R1-R8, A1-A4), Submagic's count of about 2 M short videos (Montserrat in 61 %), and the Netflix / BBC subtitle specs. Sources at the end.

**Order of authority:** 1) fonts the creator or client gave (Deepak's list in `fonts-and-colours`, a client's palette such as `mustard-red-caption-style`); 2) this guide; 3) anything else only with the user's OK. Visual check: `references/font_specimen.png` (rebuild with `tools/specimen.py`).

## 1. The rule of three
Every video uses **at most 3 families**: a **caption / body** face, a **display** face (giants, titles, numbers), and optionally one **accent** (italic serif or script for the meaning word). Each role keeps its font all video. The pair must differ clearly in width, weight or style (heavy condensed + light wide, bold sans + italic serif), never two similar sans faces. Every Instagram reference with 40K+ likes follows this (big display + tiny secondary, I1 / I2; "you do not need 100 options", kienobifilms).

## 2. Pick by video type (start here)
| Video type | Caption / body | Display (giants, titles) | Accent (one word) | Notes |
|---|---|---|---|---|
| 9:16 talking-head tips / opinion (P13, Tharun) | Montserrat 800 or Inter Black or Poppins 800 | Anton / Impact / Archivo Condensed 800 | none or Playfair 800 Italic | the default short-form system; 1-4 words per group |
| 9:16 aesthetic premium (P15, P16, Naveen bro client) | Bricolage Grotesque 600 (small, lowercase) | Fraunces Soft Black Italic | Fraunces Soft Bold Italic keyword | two sizes per line; blur reveal; client palette |
| Podcast clip (P11) | Inter 600 small + Inter Black keyword | Bebas Neue | Cormorant Garamond 600 Italic | the thesanjaysingha / Figuring Out look |
| Faceless explainer / finance facts (P12) | Inter Tight 900 | Archivo Expanded 900 (1-2 words only) | EB Garamond Italic | numbers in the display face |
| Documentary / news / true story (P14, Johnny Harris) | Inter 600 or Atkinson Hyperlegible Next 700 | Oswald 700, Bebas Neue (tracked +8 %) | EB Garamond / Cormorant italic for quotes | Courier Prime / Special Elite for documents, JetBrains Mono for data labels |
| Motivation / emotional | Montserrat 800 | Anton or Bebas | Mea Culpa or Cormorant Light Italic | script only on 1 word, large, slow |
| 16:9 YouTube explainer long-form (Aasil Khan, Tharun long-form) | Inter 600-700 (lower thirds, labels), open captions Inter 700 | Archivo Expanded 800-900 or Anton for chapter cards | Playfair / Fraunces italic | Aasil Khan: Montserrat for "modern, clean"; serif for "elegant" |
| Vlog / lifestyle | Poppins 600 or Bricolage 600 | Bebas Neue tracked wide | Caveat 700 (handwritten notes) | location titles: Bebas + small Inter caps |
| Cinematic / travel film / wedding | Cormorant Garamond 300-600 (small, tracked) | Cinzel 700 (Trajan look) or Bebas Neue wide tracking | Mea Culpa for names | thin fonts only at 60 px+ and on calm footage |
| Tutorial / SaaS / product | Inter 500-700 | Archivo 800 | none | JetBrains Mono for code and keys |
| Ads / UGC | Montserrat 800 or Poppins 800 (white + black outline) | Anton | none | readable with sound off in the first 3 s |
| Meme / gaming / fan edit | Permanent Marker or Anton | Archivo Expanded 900 | Caveat | louder allowed only in this genre |
| Thumbnails (any) | n/a | Anton, Archivo Expanded 900, Montserrat 900, Bebas | Fraunces / Playfair italic for 1 word | 3-5 words max (`thumbnail-strategy`) |
| Telugu script (any) | Noto Sans Telugu, Anek Telugu, Hind Guntur 600-700, Baloo Tammudu 2 | Ramabhadra, NTR, Gidugu, Baloo Tammudu 2 800 | Suranna, Tiro Telugu, Noto Serif Telugu, Tenali Ramakrishna | see section 6 before using |

## 2b. Pairing recipes (two fonts that look designer-made; learned 2026-11-25 from a client's carousel brief and a reel)
The aesthetic look is two fonts that contrast on **two axes at once** (sans vs serif / script, upright vs italic, caps vs lowercase). One word is the picture, the other the whisper (size ratio 1:2.5 to 1:4). Heavy caps and big italics take tight tracking, and the lines touch or overlap. Measured references and the client adaptation: `mustard-red-caption-style/references/client-font-brief.md` and section 2c there.
| Recipe | Small word | Big word | Free files | Good for |
|---|---|---|---|---|
| Italic serif + heavy caps | serif italic, lowercase | geometric caps | Playfair 800 Italic + Poppins ExtraBold | a fact, a proof word |
| Script over condensed caps | brush script overlapping the caps' top | condensed caps | Yellowtail + Anton | a negative or loud word |
| Grotesk + heavy serif italic | bold grotesk, lowercase | heavy serif italic | Inter Tight 800 + DM Serif Display Italic | the question line |
| Condensed serif caps + formal script | condensed serif caps + a dot | thin formal script | Instrument Serif + Italianno | the topic or brand word, titles |
| Sans + wide caps behind the subject | bold sans, lowercase | wide black caps, feet behind the head or object | Bricolage ExtraBold + Archivo Expanded Black | the one big idea |
| Word stack (the reel) | bold sans words, lowercase | one script keyword | Poppins ExtraBold + Pinyon Script | an emotional line; word by word, 0.17-0.2 s fade or blur reveal |

**Rules:**
- One or two recipes per video, inside the rule of three (section 1).
- Thin scripts only on plain backgrounds (sky, wall, paper) at 200 px or more.
- Type goes in the empty part of the frame, never over the face.
- The accent colour comes from the palette (or from the picture when no palette is fixed).

## 3. The library (all in `03-sound-type-assets/fonts-and-colours/assets/fonts/`, free for commercial use)
| Role | Files | ₹ | Telugu |
|---|---|---|---|
| Caption sans | `Montserrat-Variable.ttf` (also statics in edits/), `Inter-Black.ttf`, `Inter-Bold.ttf`, `Inter-SemiBold.ttf`, `Inter-Variable.ttf`, `Inter-ExtraBoldItalic.ttf`, `InterTight-800/900.ttf`, `Poppins-SemiBold/ExtraBold/Black.ttf`, `AtkinsonHyperlegibleNext-Bold.ttf` (low-vision legibility) | yes | no |
| Modern grotesk | `BricolageGrotesque-*.ttf` (Light, SemiBold, ExtraBold, CondensedExtraBold, Variable) | yes | no |
| Display | `Anton-Regular.ttf`, `BebasNeue-Regular.ttf`, `Oswald-Variable.ttf`, `Archivo-ExpandedBlack.ttf` / `-ExpandedExtraBold` (Akira / Integral stand-in), `Archivo-CondensedExtraBold.ttf`, `Archivo-Variable.ttf` (wdth 62-125) | yes | no |
| Editorial serif | `Fraunces-*` (Soft Bold / Black Italic), `PlayfairDisplay-*Variable` + `PlayfairDisplay-ExtraBoldItalic.ttf` (static 800), `CormorantGaramond-*` (Apple Garamond stand-in), `EBGaramond-*`, `DMSerifDisplay-*` (Times bold italic stand-in), `Cinzel-Bold.ttf`, `InstrumentSerif-Regular/Italic.ttf` (condensed high-contrast, Spire stand-in) | **DM Serif, Cinzel, Instrument Serif: no** | no |
| Script / hand | `MeaCulpa-Regular.ttf`, `Caveat-Bold.ttf`, `PermanentMarker-Regular.ttf`, `Italianno-Regular.ttf` and `PinyonScript-Regular.ttf` (thin formal scripts, plain backgrounds only), `Yellowtail-Regular.ttf` (bold brush script, Billion Dreams stand-in, Apache 2.0) | **Permanent Marker, Italianno, Pinyon, Yellowtail: no** | no |
| Mono / typewriter | `JetBrainsMono-Bold.ttf`, `CourierPrime-*`, `SpecialElite-Regular.ttf` | **no** | no |
| Telugu | `NotoSansTelugu-Variable`, `AnekTelugu-Variable`, `HindGuntur-SemiBold/Bold`, `BalooTammudu2-Variable` / `-ExtraBold`, `Mandali-Regular`, `Ramabhadra-Regular`, `NTR-Regular`, `Gidugu-Regular`, `Suranna-Regular` (no ₹), `NotoSerifTelugu-Variable` / `-Bold`, `TiroTelugu-Regular`, `TenaliRamakrishna-Regular` | mostly | yes |
| The creator's own | Tactic Sans (42 weights, `fonts for claude/`), Impact (system) | Tactic: no ₹ (use Montserrat Black ₹ at 0.8x) | no |
**₹ rule:** never set a price in a font marked "no": the specimen shows an empty box. Use the caption font's ₹ or Montserrat Black at 0.8x.
**Variable fonts in shortkit:** shortkit loads a file at its default weight (Inter default = 400). Use the static files above or cut one with `fontTools.varLib.instancer` (whisper venv).

## 4. Subtitle and caption numbers
| Spec | Value | Source |
|---|---|---|
| Characters per line (sentence subtitles) | **42** (English and Telugu) | Netflix |
| Lines | **2 max**, usually 1; a bottom-heavy pyramid when 2 | Netflix |
| Reading speed | English up to **20 cps** adult / 17 kids; **Telugu up to 22 cps** / 18 kids; BBC 160-180 wpm | Netflix, BBC |
| Duration | min **0.83 s** (5/6 s), max **7 s**; **2-frame** gap; out-time 2 frames before a shot change; hold 0.5 s past the last audio when nothing follows | Netflix |
| Line breaks | after punctuation, before conjunctions / prepositions; never split article + noun, first + last name, verb + negation | Netflix |
| Line width (16:9) | **68 %** of frame width max | BBC |
| Text size (16:9 online) | line height about **8 %** of frame height (= 86 px at 1080p) | BBC research |
| Short-form caption groups | 1-4 words; lead-in 3-3.5 % of height (60-68 px), keyword 6.5-8 % (125-150 px); never Light / Thin weights | references + vendor guides |
| Social contrast | white or cream + dark outline 3-7 px or soft shadow; a dark band only for sentence subtitles | all guides |
| Italics | English: narration, thoughts, lyrics, foreign words only. **Telugu: never italics** (use quotes) | Netflix |
| Numbers | 1-10 in words, above 10 in digits (English and Telugu); currency in words in Telugu subtitles (10 డాలర్లు); on social captions, big numerals are fine (they are design, not subtitles) | Netflix |
| Songs | subtitle only plot-relevant lyrics, ♪ around them | Netflix |
Short-form captions (word groups on the chest) follow the house rules in `shorts-editing-pro` and `my-editing-rules`. The Netflix numbers apply to **sentence subtitles**: long-form open captions, documentary, translated subtitles and any .srt we deliver.

## 5. Placement: safe zones (1080x1920)
**Researched 2026-11-25** (the user asked for research, not Claude's own numbers). The sources are platform safe zones, eye-tracking studies and about 15 short-form reels studied earlier. Details and links are in `references/vertical-text-placement-research.md`.
- **Platform UI:**
  - Ordinary posts cover about the top 120-270 px, the bottom 300-450 px and a right button column of 120-164 px.
  - Ads cover more: Meta Reels keeps the bottom 35 % (672 px) clear, TikTok In-Feed the bottom 660 px.
  - Keep everything inside x 120-960, y 270-1470.
- **Running subtitles (talking head, speaker centred):**
  - centred at x 540, with the block centre at **58-65 % of the height (y about 1110-1250)**, just under the chin, never on the mouth or eyes;
  - the studied reels sit at 55-68 % (median about 63 %);
  - the eye-tracking studies (Kurzhals CHI 2017, BBC R&D 2015) found subtitles near the speaker cost less eye travel, and the most important rule is not to cover the mouth.
  - If the short may run as an ad, keep the block above y 1250.
- **Above the head:** accent text only (hook title, number headline, label), 1-3 per short, below y 270. Never the running subtitles.
- **Beside the face:** only with real empty space (wide podcast shot, off-centre speaker, 16:9 inside 9:16).
- 16:9: subtitles at the bottom, centred, inside the 90 % title-safe area; lower thirds on the left third, with the name in the display or semibold face and the role in a lighter weight.

## 6. Telugu
- **Roman-letter Telugu** ("kaani enduku ee") uses the Latin fonts above: it is how the client's shorts are captioned and needs nothing extra.
- **Telugu script works since 2026-11-25.**
  - **Why:** Pillow's wheel already bundles raqm and harfbuzz; it only needed Homebrew `fribidi` (`brew install fribidi`, not `libraqm`). The full `libraqm` formula builds 36 packages from source on this Intel Mac; `fribidi` needs only 3.
  - **Check:** `~/.local/share/whisper-venv/bin/python -I 03-sound-type-assets/pro-font-and-subtitle-guide/tools/telugu_check.py <out.png>`. It prints `raqm: True` and draws every Telugu font twice: basic layout (broken) and raqm (correct). The sheet is `references/telugu_shaping_check.png`.
  - **If raqm turns False again** (a Pillow reinstall, or fribidi removed), run `brew install fribidi` again.
  - **shortkit draws Telugu-script captions as-is.** Proof frame: `references/telugu_caption_test.jpg`, the Pink Tax line "కానీ ఎందుకు ఈ / తేడా?" with an Anek Telugu SemiBold lead-in and a Baloo Tammudu 2 ExtraBold haldi keyword.
  - **Settings:**
    - Set `style.cap_font` to a Telugu face (variable files load thin, so use the statics `AnekTelugu-SemiBold/Bold.ttf` or `NotoSansTelugu-Bold.ttf`).
    - Give the keyword `"font": "BalooTammudu2-ExtraBold.ttf"` (or Ramabhadra).
    - Telugu needs about 10-15 % more line height than Latin, because vowel signs sit above and below.
  - **Do not use Telugu-script fonts for the client's shorts** (user, 2026-11-25: "dont use telugu font"). Captions stay Tenglish in Latin fonts. Use Telugu script only when the user asks for it by name.
  - **₹:** Gidugu (draws a blank) and Suranna (draws an empty box) have no ₹; the other Telugu faces have it.
  - **Latin side effect:** raqm also applies GPOS kerning, so Latin captions render up to 1.6 % narrower than before. For a partial re-render of a project first rendered before 2026-11-25, set `SHORTKIT_LAYOUT=basic` so new frames match the old ones.
- Roles: captions in Noto Sans Telugu / Anek Telugu / Hind Guntur 600-700 (clean, open counters); display in Ramabhadra / NTR / Gidugu / Baloo Tammudu 2 800 (heavy, poster); traditional or emotional lines in Suranna / Tiro Telugu / Noto Serif Telugu / Tenali Ramakrishna (calligraphic). Mandali is a calm book sans for long text.
- Telugu designer pages on Instagram (designer.rajesh, edit_by_srivastav, inksudha) mostly show the paid **Anu** font pack: not licensed here, so do not use it unless the client owns it.
- Netflix Telugu rules: 42 cpl, 22 cps, no italics, the ellipsis character (…), no space before punctuation, abbreviations spelled out, names transliterated, modern standard Telugu.

## 7. Licensing
- Everything in the library is SIL OFL (Permanent Marker: Apache 2.0); licences are in `assets/fonts/licences/`. OFL allows commercial video, client and monetised use.
- "Free" on dafont / Instagram packs usually means personal use only (kalylsfilms' dafont fonts, "comment FONTS" packs, Akira, Integral, Snell Roundhand, Apple Garamond, Neue Plak and the rest of akhilfilms' list): use the stand-ins named here.
- Never download a font pack offered in a DM / "comment for link" post.

## 8. QC (fonts and subtitles)
- [ ] At most 3 families; each role keeps its font; the pair contrasts
- [ ] No Light / Thin weight in captions; display faces only for 1-4 words
- [ ] Every price shows ₹ (no empty box or blank); Telugu script: `telugu_check.py` prints raqm True before rendering, and a still shows every vowel sign joined
- [ ] Sentence subtitles: 42 cpl, 2 lines, reading speed, 0.83-7 s, 2-frame gaps
- [ ] Text inside x 120-960, y 270-1470; subtitle block centre at 58-65 % of the height, under the chin; above-head accents 1-3 per short (section 5)
- [ ] Outline or shadow on every caption over moving footage

## 9. Sources (2026-11-25; vendor blogs are direction, not proof)
Netflix: [Telugu Timed Text Style Guide](https://partnerhelp.netflixstudios.com/hc/en-us/articles/4482320288787-Telugu-Timed-Text-Style-Guide), [English (USA)](https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide), [General Requirements](https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617), [Subtitle Timing Guidelines](https://partnerhelp.netflixstudios.com/hc/en-us/articles/360051554394-Timed-Text-Style-Guide-Subtitle-Timing-Guidelines). BBC: [subtitle guidelines summary](https://clevercast.com/bbc-subtitling-guidelines), [How big should subtitles be](https://bbc.github.io/csun/how_big_should_subtitles_be/index.html). Caption fonts: [Submagic](https://www.submagic.co/blog/best-font-for-subtitle), [BlitzCut Reels](https://blitzcutai.com/blog/best-caption-fonts-reels-2026), [BlitzCut Shorts](https://blitzcutai.com/blog/best-caption-fonts-youtube-shorts-2026), [BlitzCut video fonts](https://blitzcutai.com/blog/best-fonts-for-video-editing-2026), [Made Good Designs captions](https://madegooddesigns.com/best-fonts-for-captions/), [Made Good Designs YouTube](https://madegooddesigns.com/best-fonts-for-youtube-channel/), [SpotlightFX Google Fonts](https://spotlightfx.com/blog/best-google-fonts-for-video-editors), [Miracamp documentaries](https://www.miracamp.com/learn/video-editing/best-fonts-for-documentaries), [OpusClip Shorts captions](https://www.opus.pro/blog/youtube-shorts-caption-subtitle-best-practices). Safe zones: [Reap](https://reap.video/blog/short-form-video-safe-zones), [TryMyPost Reels](https://www.trymypost.com/blog/instagram-reels-safe-zones-text-placement-2026), [Kapwing](https://www.kapwing.com/video-editor/instagram-reels/safe-zone). Telugu: [Adobe Fonts Noto Sans Telugu](https://fonts.adobe.com/fonts/noto-sans-telugu), [Tiro Telugu](https://fonts.adobe.com/fonts/tiro-telugu). Instagram (study only): harrisonniap `DIb36sczbeW` / `DGaL56SoKhe`, thesanjaysingha `DTnc3oekwSC`, kalylsfilms `DcBwAjvoEqI`, bytheway.deshna `DNS7D8-sdne`, aasil_khan_ `DVK93xnk8Ai`, kienobifilms `DcgwecURmrE` / `Df9zWEShGeG`, amro.films `DU3Y__EDHil`, motionby_lance `Dd1J3c_CT6g`, akhilfilms.exe `DVkDFeCj863`, kuldeep.mp4 `DfVIm8go5vf`.
