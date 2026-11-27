# Central font folder (added 2026-11-22)

Downloaded from the Google Fonts repository (`github.com/google/fonts`, raw files). Licences: SIL Open Font License 1.1, except Special Elite (Apache 2.0). Free for commercial video use. Load with `@font-face` from this folder (HyperFrames) or by file path (Pillow / ffmpeg `drawtext fontfile=`). Not installed into macOS.

| File | Role |
|---|---|
| `Montserrat-Variable.ttf`, `Montserrat-Italic-Variable.ttf` (100-900) | House default caption font (`my-editing-rules`: Montserrat Bold 700); ExtraBold 800 for the P13 heavy keyword |
| `PlayfairDisplay-Variable.ttf`, `PlayfairDisplay-Italic-Variable.ttf` (400-900) | Bold italic serif: P14 one-word moral and abstract lines, P12 serif line |
| `SpecialElite-Regular.ttf` | Typewriter, worn: P14 data voice (chart labels, typed lines) |
| `CourierPrime-Regular.ttf`, `CourierPrime-Bold.ttf` | Typewriter, clean: dates, numbers, search-bar typing |
| `Oswald-Variable.ttf` (200-700) | Condensed caps: date cards, labels |
| `AnekTelugu-Variable.ttf` (width + weight 100-800) | Telugu display: heavy keyword words in Telugu script |
| `NotoSansTelugu-Variable.ttf` (width + weight 100-900) | Telugu text: small lines and labels in Telugu script |
| `Ramabhadra-Regular.ttf` | Telugu heavy headline face |

Not tested in a render yet. Check Telugu conjuncts on a still before using a Telugu face in an edit.

## Added 2026-11-25 (user approved researching + adding free fonts for the mustard-red client)
All SIL Open Font License 1.1 (free, commercial and client use OK); licences in `licences/`. Downloaded from the google/fonts GitHub repo.
| File | Role |
|---|---|
| `Fraunces-SoftBoldItalic.ttf`, `Fraunces-SoftBlackItalic.ttf` (static: opsz 144, SOFT 100, WONK 1, wght 700 / 900) | soft retro italic serif: the keyword of the Haldi-Kumkum look (M4) |
| `Fraunces-SoftSemiBold.ttf` (roman) + `Fraunces-Variable.ttf`, `Fraunces-Italic-Variable.ttf` | titles, other weights |
| `BricolageGrotesque-Light / SemiBold / ExtraBold / CondensedExtraBold.ttf` (static) + `BricolageGrotesque-Variable.ttf` | lead-in words, labels, ghost lines; condensed caps |
| `BebasNeue-Regular.ttf` | condensed caps (M2 golden caps; closest to the Kobe reference) |
| `DMSerifDisplay-Regular.ttf`, `DMSerifDisplay-Italic.ttf` | alternate display serif (no rupee sign) |
Static files were cut from the variable fonts with fontTools (whisper venv) so shortkit / PIL / CapCut / After Effects all read them.

## Added 2026-11-25 (the user asked for the best fonts for every video type; roles in `03-sound-type-assets/pro-font-and-subtitle-guide`)
All from the google/fonts GitHub repo, SIL OFL 1.1 (Permanent Marker: Apache 2.0); licences in `licences/`. Statics cut with fontTools.
| File | Role |
|---|---|
| `Inter-Variable.ttf`, `Inter-Italic-Variable.ttf`; statics `Inter-Black`, `Inter-Bold`, `Inter-SemiBold`, `Inter-ExtraBoldItalic` (opsz 32) | captions, UI, lower thirds (Inter Black = the "cinematic fonts" reels' caption face) |
| `Archivo-Variable.ttf` (wdth 62-125); statics `Archivo-ExpandedBlack`, `Archivo-ExpandedExtraBold`, `Archivo-CondensedExtraBold` | Akira / Integral stand-in (expanded), tight condensed headings |
| `CormorantGaramond-Variable` / `-Italic-Variable`; statics `-Bold`, `-SemiBoldItalic`, `-LightItalic` | Apple Garamond stand-in: elegant serif, cinematic titles |
| `EBGaramond-Variable.ttf`, static `EBGaramond-SemiBold.ttf` | roman Garamond for quotes and documentary text |
| `Cinzel-Variable.ttf`, static `Cinzel-Bold.ttf` | Trajan-style film-poster caps (no ₹) |
| `AtkinsonHyperlegibleNext-Variable.ttf`, static `-Bold` | maximum-legibility captions and subtitles |
| `Caveat-Variable.ttf`, static `Caveat-Bold.ttf`; `MeaCulpa-Regular.ttf`; `PermanentMarker-Regular.ttf` (no ₹) | handwritten notes, elegant script accent, marker labels |
| `JetBrainsMono-Variable.ttf`, static `JetBrainsMono-Bold.ttf` | code, keys, data labels (no ₹) |
| `Anton-Regular.ttf`, `Poppins-SemiBold / ExtraBold / Black.ttf`, `InterTight-800 / 900.ttf` | copied from earlier edits into the central folder |
| Telugu: `Mandali-Regular`, `NTR-Regular`, `Gidugu-Regular`, `Suranna-Regular` (no ₹), `NotoSerifTelugu-Variable` / `-Bold`, `HindGuntur-SemiBold` / `-Bold`, `BalooTammudu2-Variable` / `-ExtraBold`, `TiroTelugu-Regular`, `TenaliRamakrishna-Regular` | Telugu captions, display, traditional lines. **PIL on this Mac cannot shape Telugu (raqm off)**: do not render Telugu script with shortkit until that is fixed |

## Added 2026-11-25 (client font-pairing brief, round 4)
| File | Licence | Role |
|---|---|---|
| `Italianno-Regular.ttf` | OFL (`licences/Italianno-OFL.txt`) | thin formal script, the client's named font |
| `PinyonScript-Regular.ttf` | OFL (`licences/PinyonScript-OFL.txt`) | formal script for the word stack (reel look) |
| `Yellowtail-Regular.ttf` | Apache 2.0 (`licences/Yellowtail-LICENSE.txt`) | bold brush script, Billion Dreams stand-in |
| `InstrumentSerif-Regular.ttf` / `-Italic.ttf` | OFL (`licences/InstrumentSerif-OFL.txt`) | condensed high-contrast serif, Spire stand-in |
| `PlayfairDisplay-ExtraBoldItalic.ttf` | OFL (static 800 cut from the variable file) | italic serif small word of recipe A |
None of these has a ₹ glyph. Library total: 76 font files (79 after the Telugu statics below).

## Added 2026-11-25 (Telugu script now renders: raqm on)
| File | Licence | Role |
|---|---|---|
| `AnekTelugu-SemiBold.ttf` / `AnekTelugu-Bold.ttf` | OFL (static cuts of the variable file, wdth 100) | Telugu lead-in / caption |
| `NotoSansTelugu-Bold.ttf` | OFL (static wght 700, wdth 100) | Telugu caption |
Gidugu and Suranna have no ₹. Shaping check: `03-sound-type-assets/pro-font-and-subtitle-guide/tools/telugu_check.py`.

