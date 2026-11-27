---
name: aesthetic-pro-reel-edit-style
description: Use for every short of the client who asked (2026-11-25) for "aesthetic font subtitles like the Instagram channels, and fully advanced pro edits, not a normal edit" (the Naveen bro Telugu / English shorts), and for any request for an aesthetic, premium, advanced or "Instagram editor" talking-head reel. Profile P16. Built from 11 measured Instagram reels (amro.films, viashaan, dopemotionzone, kreatize_, twenty.fourth.edit, prime_animator...). It stacks the layers: dark warm grade, M4 Haldi-Kumkum captions with a blur-to-sharp reveal (mustard-red-caption-style), a cut or punch every 2-2.5 s, a literal B-roll for every concrete noun, and a designed insert every 6-8 s: an off-white paper scene with the speaker cut out and a haldi ribbon, a mono-label face HUD, a glowing face ring, or giant number / topic words behind the head. Includes shortkit keys, budgets, an event grid, sound and QC.
---

> **Scope: mixed. Built for the Naveen bro shorts (P16): its client rules (Poppins + Playfair pairing, no Telugu-script font, no BGM and no grade on video 25) belong to that client. The layer stack, the insert menu and the event grid are general for any premium talking-head reel.**

# Aesthetic pro reel (P16) - client request, 2026-11-25

**Why it exists:** the client (Naveen bro shorts) first asked for aesthetic mustard + red subtitles (`05-clients/naveen-bro/mustard-red-caption-style`). Then the user added: the client wants the **aesthetic-font subtitle edits some Instagram channels do**, and **fully advanced pro edits, not a normal edit**. This skill defines what "advanced pro" means, measured from 11 Instagram reels (`references/instagram-references.md`, I1-I11), and how to build it with our kit.

**Read with:** `shorts-editing-pro` (build + log), `event-map-reel-edit-style` (event map, 1.3 s rule, word-to-event sync, QC), `mustard-red-caption-style` (caption layer, M4), `pro-video-editing` P11 (podcast scene inserts) and P13 (two-tier kinetic), `beginner-to-pro-edit-tips` (each move smaller, fewer effects, dull colours), `sound-and-music-design` + `ue-sound-design`.

## 1. What "advanced pro" is (measured, not guessed)
| Seen in the references | Number | Ref |
|---|---|---|
| Cut, angle change or punch-in | every **1.9-2.5 s** on talking-head / podcast clips | I3 16 in 30 s, I4 8 in 20 s, I7 13 in 30 s |
| Text change | every **~1 s**, even when the shot holds | I1, I2 |
| Type | **two fonts per line**: big display (italic serif or heavy sans) + small sans or script; one keyword colour per video | all 11 |
| Word arrival | **blur-to-sharp** (or 3D fly-in with motion blur), eased, never linear | I1, I5, I6 |
| Designed insert | one every **5-8 s**: paper cut-out scene, slam card, ribbon type, checklist card, HUD, face ring | I3, I5, I9, I11 |
| B-roll | a **literal picture for every concrete noun / number** (goal = dartboard, weight = scale, km = running) | I10 (Telugu editor), I3, I4 |
| Grade | **dark and warm** (practical lamp light) or desaturated natural; never bright and saturated | I1, I5, I6, I8 |
"Advanced" = more layers, spread out, each one quiet. No reference stacks two special moves at once.

## 2. The layer stack (build order)
| Layer | Spec | shortkit |
|---|---|---|
| 1 Grade | warm and moody: sat 0.95-1.0, warm 0.03-0.04, vignette 0.34, grain 0.04; face lift 0.12-0.16 | `grade` |
| 2 Cut rhythm | keep the client's cut; add a punch-in (1.25 -> 1.5-1.65, `expo`) or punch-out on every new sentence so the frame changes every 2-2.5 s; zoom cap 1.80 | `camera` |
| 3 Captions | M4 Haldi-Kumkum (fonts since 2026-11-26: Poppins SemiBold cream lead-in, Playfair Display ExtraBold Italic haldi keyword (user rejected Bricolage + Fraunces; one carousel pairing only), kumkum on negative words, haldi brush on up to 4 hero words, kumkum dot full stop) + **blur reveal** | `restyle_edl.py M4`, then `style.reveal: "blur"` |
| 4 Literal B-roll | one clip per concrete noun / number / product, 0.8-2.0 s, whip or blurzoom entry, caption stays on top | `broll` |
| 5 Designed inserts | one every 6-8 s, rotating through the menu in section 3 | `paper`, `brackets`, `giants`, `layers`, `dims`, `desat` |
| 6 Sound | a sound on every scene change and insert (section 5); music ducked under the voice | `sfx`, `music` |

## 3. The insert menu (rotate; never two at once)
> **Floor since 2026-11-26 (client not impressed by video 25):** the insert budget below is a minimum, not a menu to sample. Designed MG every 8 s, 3+ kinds, >= 25 % of runtime, no stretch over 9 s without one, HL + MC. Add the kinds in `01-process/before-edit/2-PRO-MOVE-MENU.md` (list device, contrast object, UI card with `dims`, split, full scene, object behind the head). Gate: `01-process/before-edit/tools/pre_edit_gate.py`.

| Insert | When to use it | Budget per 45 s | shortkit |
|---|---|---|---|
| **Haldi paper scene** (I5, Claude's idea C1): room becomes textured off-white paper `#EFE7D6`, speaker cut out with a soft shadow, a haldi `#E2AA2C` ribbon draws on behind them in 0.45 s; captions turn ink `#1A1410`, keyword deep haldi `#B9831A`. **But when the caption block sits on the speaker's shirt (it does at y 1110-1250), keep it cream + haldi with the outline: `"text": "#F4EFE3", "key": "#E2AA2C", "stroke": 3`** (2026-11-26: ink on the brown shirt vanished; only the room turns to paper) | the topic word or the key question; 1.2-2.0 s, starts on a hard cut | 2 | `"paper": [{"t0","t1","color":"#EFE7D6","ribbon":"#E2AA2C","path":"swoosh|arc"}]` |
| **Topic giant behind the head on paper**: lowercase italic serif (Playfair Display ExtraBold Italic since 2026-11-26; Fraunces before) in the topic colour (`#C8476E` rose for the pink tax) | inside a paper scene, on the topic word | 1-2 | `giants` with `font` Fraunces-SoftBlackItalic, `glow` 0, `behind` true |
| **Face HUD** (I5): haldi corner brackets + Courier Prime Bold mono label + live X/Y | a "check this" / question line; label = the script's own words in caps (Claude's idea C2: never a made-up number) | 2 | `"brackets": [{..., "label": "SCAN: SAME INGREDIENTS"}]` |
| **Face ring** (I11): thin glowing haldi circle, scales in | a pointed line about "you" / the viewer / the target | 1-2 | `"brackets": [{..., "shape": "ring", "label": "TARGET CUSTOMER"}]` |
| **Number beat** (I10, Claude's idea C3): the number as a Fraunces haldi giant behind the head, the rest as small caption | the ONE biggest number (it takes the middle above-head slot, rule 7); every other number is a haldi keyword in the lower caption | 1 | `giants` |
| **Designed scene** (I3, I9): price board, receipt, checklist card, tag layers (`edits/ammailu/tools/scenes.py` style) | the proof / comparison beat | 1-3 | `layers` (RGBA frames) + `dims` |
| **B&W stretch** | the "waste" / loss beat | 1 | `desat` or B-roll `bw` |
| **Pairing moment** (client font brief, round 4): two-font title in the plain wall above the head, from the menu in `mustard-red-caption-style` section 2c (Playfair + Poppins, Yellowtail + Anton, Inter Tight + DM Serif Italic, Instrument Serif + Italianno, wide caps behind the head, Pinyon word stack) | hook or loop line (above-head budget, rule 7) | 1-2 (one or two pairings per video) | `giants` + a caption group with `"y"` and a keyword `"font"` |
| **Word stack** (2026-11-25, `text-animation-moves`): one sentence builds word by word into 2 tight lines on the chest under the chin (block centre 58-65 % of the height, ink outline on the shirt; research: `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`); big meaning words, small link words, ONE hero word typed on letter by letter; clears hard at the sentence end. Above the head only as one of the budget moments (rule 7) | hook line, the turn, a list of reasons, the loop line | 2-4 | `stacks` (fx `type` / `rise` / `blur`) |
| **Artwork plate** (2026-11-26, video 25): a portrait painting / scripture page shown WHOLE on the client's paper `#EFE7D6` in the upper half (740 px wide, y 120-1050, soft shadow), rising 36 px in 0.2 s then a slow 1.06 -> 1.00 pull-back; the caption sits below it in ink lead-ins + deep-haldi keyword with the ink outline. Use when a full-bleed 9:16 crop would put busy or gold detail behind the caption | a named scripture / book / artwork | 1 | a scene clip as a B-roll slot, `shade: false` (`edits/roughcut3/tools/scenes.py`) |
Not used: lime or green accents (I11, I3) because the palette is haldi / kumkum / cream / ink. No 3D-tracked text (no camera solve in the kit), no fake UI with invented numbers, no font salad.

## 4. Event grid for a 45 s Telugu short (fit to the real words)
| Time | Event |
|---|---|
| 0-1.5 s | hook: giant topic word behind the head (or a paper scene); first caption blur-reveals on the first spoken word |
| every 2-2.5 s | cut / punch / B-roll entry (layer 2 or 4) |
| every 6-8 s | one insert from section 3, rotating (paper -> HUD -> number beat -> scene -> ring -> paper); text above the head only as 1-3 accents per short (rule 8); all other text on the chest |
| turn (about 2/3) | the strongest insert (paper scene or designed scene) |
| last 2 s | loop line: same giant / paper look as the hook |
Check with `event-map-reel-edit-style`: something new every 1.3 s, every event on its word.

## 5. Sound for the inserts (levels from `ue-sound-design`)
Paper scene: a soft paper slide or whoosh on the cut + a light "swipe" as the ribbon draws (-16 to -18 dB). HUD: one soft UI tick when the label appears (-18 dB). Ring: a low soft bloom (-17 dB). Number beat: a short riser into a tick. B-roll whip: a whoosh panned with the direction. Never more than 2 sounds on one frame.
Word stack and other text moves: one sound per move kind, link words silent, at most 2 sounds per stack; files, slices and levels in `text-animation-moves` section 5 (type-on = keyboard burst sliced to the word, -16; rise = soft whoosh peak-aligned, -18; pop -14).

## 6. Rules
1. Keep the client's cut (`my-editing-rules`); every layer goes on top.
2. One special move at a time: paper, HUD and ring never overlap, and no insert while a giant is up (except the topic giant inside a paper scene).
3. Each move is small and quiet (`beginner-to-pro-edit-tips`): HUD label 26 px, ring 4 px, ribbon 5 % of the width, no shake, no glitch.
4. Captions stay on the chest, with the block centre at 58-65 % of the height (rule 8); on B-roll and paper scenes they keep the same place.
5. HUD labels say true words from the script. Coordinates are decoration only.
6. A paper scene needs a clean person matte: check the hair and hands on a still before the full render.
7. Every keyword colour is checked against the picture under it (red on the red checked shirt needs the ink outline; on paper the keyword turns deep haldi).
8. **Where text goes (researched 2026-11-25, `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`; user feedback "full subtitles in upper head looks heavy").** Running subtitles and stacks sit on the chest under the chin: block centre 58-65 % of the height (y about 1110-1250), bottom above y 1470, lines within x 120-960, never on the mouth or eyes. Above the head (below y 270) go only accent texts: the hook title, a number headline, a short label, 1-3 per short in total (giants, pairings and number giants counted together; `shorts-editing-pro` rule 8).
9. **No Telugu-script font** (user, 2026-11-25): the client's subtitles are Tenglish in the Latin fonts. Telugu script only if the user asks for it by name.

## 7. Clashes (said to the user before an edit)
- `beginner-to-pro-edit-tips` "fewer effects" vs the client's "fully advanced": solved by spreading the layers (one insert every 6-8 s) while each one stays small. The references do the same. No stop needed unless the user wants more per moment.
- P15 (`ultimate-editors-shortform-style`) also uses off-white scenes: P15 is cool and calm with a blue keyword; P16 is warm haldi with the speaker cut out. Do not mix the two in one video.
- `fonts-and-colours` "one accent per video / change fonts every video": overridden for this client (fixed haldi / kumkum palette and the M4 fonts; user's choice 2026-11-25; fonts are Poppins + Playfair Display Italic since 2026-11-26).
- Layer 1 (dark warm grade) vs a user request for **no colour grading** (video 25, 2026-11-26): the request wins. Neutral grade dict with `vignette: 0` and `grain: 0` set explicitly (shortkit's vignette default is 0.3), B-roll `sat` 1.0 / `gain` 1.0; the caption shade band is allowed (it is readability, not a look).

## 8. QC (add to the `event-map-reel-edit-style` QC list)
- [ ] Something new every 1.3 s; cut or punch every 2-2.5 s
- [ ] One insert every 6-8 s, none overlapping
- [ ] Every caption blur-reveals ON its word (never early)
- [ ] Paper scene: no halo round the hair, captions readable in ink
- [ ] HUD labels true; ring centred on the face through the punch
- [ ] Every number and product has its B-roll or number beat
- [ ] Loudness -14 LUFS, -1.5 dBTP; watched once on a phone

## 9. Status (2026-11-25)
- shortkit gained `style.reveal`, `paper`, `brackets.label` and `brackets.shape: "ring"` today (all optional; old EDLs unchanged).
- Sample: `edits/mustard-red-captions/previews/signature/Pink_Tax_PRO_sample.mp4` (Pink Tax 18.3-29.9 s, the same range as the captions-only M4 sample, so the client can compare). EDL `edits/mustard-red-captions/code/pinktax_PRO_edl.json`.
- Not verified: the client has not seen it; nobody has watched it on a phone.
