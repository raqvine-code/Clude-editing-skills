# r3: "A Russian scientist died mysteriously…" (42.6 s, 720x1280, 30 fps, 1278 f)

Conventions: frame numbers are source frames at 30 fps (f300 = 10.00 s). Pixel sizes are at 720x1280 unless marked "@360" (frame dumps) or "@1080". Values marked ≈ were estimated by eye from frame-numbered sheets rather than measured. All font names are visual guesses.
Evidence: R/d/*.jpg (26 sheets by the previous analyst, all reviewed), R/st/type_crops.jpg (full-res text crops), R/st/spec_small.jpg, R/data/cam.json (per-frame ORB similarity transform), R/data/meas1.json (per-frame colour-mask bboxes), R/data/framediff.npy (new: per-frame mean abs diff @360).

---

## 0 Identity

This is a faceless "news-mystery" short. It is built entirely from AI-generated stills that are animated as 2.5D layers (a cut-out subject, a blurred plate and a foreground layer). The camera never stops moving: only 1.2 % of frames are static and the median frame-to-frame difference is 5.8. The voice-over is slow, at 130 wpm with roughly 1 s pauses. The edit avoids true cuts. Most of the 18 scene changes are motion-continuous: zoom-out reveals, card push-ups, rotation-matched cuts, shape irises (coffin, grave circle, coffin-shaped photo frame, mouth iris, keyhole) and macro-texture bridges. On-screen text is rationed. It appears only for the date, a name, diegetic newspaper headlines, two abstract VO phrases, and the call to action. Red is the thread colour from the first underline to the final "red room". The story is a demo reel for selling After Effects project files. It ends on an open question at 34.1 s, then turns that open loop into a rewatch CTA: "Some editors rewatch this. Others open the project file…".

---

## 1 Beat sheet

| # | t (s) | frames | VO | Visual | On-screen text | Transition in | Audio event (side-channel / sub) |
|---|---|---|---|---|---|---|---|
| 1 | 0.00–3.00 | 0–89 | "A Russian scientist died mysteriously," | Defocused empty lab. Scientist flies back from the lens (f6–18). Coffin rises behind her (f28–35). Circular grave iris (f43–48). B&W switch (f50). Lid slides shut (f52–71). | none | start | booms 0.19 / 0.37 / 0.67 / 0.99 / 1.16 s; sub drone −15 dB 0–3.7 s |
| 2 | 3.00–6.50 | 90–194 | "and fears of a deadly plague suddenly resurfaced." | Quarantine crowd (hazmat coats, plague-doctor whites) before a brick sanatorium at sunset. Fly-back entrance, then slow drift, then an accelerating lift-out (f171–194). | none | hard cut on "and" (+2 f) | click 3.01 s (7.5 kHz, **clips**); hit 4.45 |
| 3 | 6.50–8.65 | 195–259 | (pause) "In October 2026," (pause) | Near-black dusty card. Text drifts upward. | "OCTOBER, 2026" typed, with cursor and red underline | hard cut in the VO pause | swish-hit 6.47 s (2.6→7.9 kHz, **clips**) |
| 4 | 8.67–10.70 | 260–321 | "a 28-year-old laboratory worker in Siberia" | Lab 2. The scientist flies back inside a card that slides up. | red name pill "Darya Shipilova" (name is never spoken) | **card push-up #1** (f260–268) | boom 8.56 s (+25.9 dB, 0.79 s), sub −13 dB |
| 5 | 10.73–11.47 | 322–344 | "…Siberia died" | Pull-back reveals the shot is a photo in a red-outlined coffin-hexagon frame in a newspaper. Desaturates mid-move. | the label goes grey with the photo | zoom-out reveal (frame-within-frame) | boom 11.44 s |
| 6 | 11.50–14.65 | 345–439 | "died after developing severe pneumonia." | Hands hold the newspaper over dark wood. Yellow highlighter runs line by line. Paper drops out with a +21° roll. | diegetic headline + highlight | continuous zoom-out with blur (×0.78 over 6 f) | sub swell 11.6–13.7 s |
| 7 | 14.67–17.15 | 440–514 | "Rumors of a possible plague infection spread," | Blueprint grid starts rolled ≈15–20° (measured +15.2° cumulative from f441) and un-rotates. | one word at a time, italic serif | rotation-matched cut | click 14.66 s (**clips**) |
| 8 | 17.17–19.15 | 515–574 | (pause) "putting nearly 200 contacts" | Macro red wood. Camera pulls back and counter-rolls. The NBC-style paper slides in. Green highlight, then a red circle around "200". | diegetic headline + annotations | texture bridge (hard cut) | whoosh-boom 17.18 s (2.4 k→409 Hz, **clips**) |
| 9 | 19.17–21.40 | 575–642 | "under medical observation." | ×1.35 punch-in on the headline. Slow push-out. Exits with a blur zoom-out. | — | **punch-in cut** (1 f) | none on the cut (sub transient f577) |
| 10 | 21.43–23.68 | 643–710 | "The news quickly raised fears" | Retro TV room seen from behind two viewers. The screen shows "DAILY REPORT", then an anchor. Plays at 15 fps. | TV graphics (diegetic) | hard cut on "The" (±0 f) | whoosh-boom 21.49 s (**clips**) |
| 11 | 23.70–27.47 | 711–824 | "of a disease once responsible for devastating outbreaks throughout history." | Grungy wall. Four B&W archive photos slide in from the left and right edges. 2-frame camera flash (f737–738). Photos converge into a 2×2 grid. Light rays sweep. Grid rolls out. | none | push-in into the TV, then cut to the wall texture | whoosh 23.75 s (**clips**); flash hit 24.56 s |
| 12 | 27.50–29.37 | 825–881 | "But there was a twist." | Dark teal void. Vertical word stack builds upward on a tilted 3D column. | But / there / was / a / twist. | rotation-matched cut (−9°/f) | boom 27.39 + click 27.52 (**clips**) |
| 13 | 29.40–32.30 | 882–969 | "Russian officials reported negative plague tests," | Desaturated press conference. The Russian flag and the mics stay in colour. Speaker flies back; foreground mics rise into frame. | none | **card push-up #2** (f875–882) | — |
| 14 | 32.33–34.00 | 970–1020 | "and no outbreak was confirmed." | Same plate at ×1.41 with −16.4° Dutch tilt, crushed B&W. | none | punch + roll + grade switch on "no" | boom 32.26 s; sub drone −17 dB 32.3–34.5 s |
| 15 | 34.03–35.43 | 1021–1063 | "So what actually killed…" | A circular iris opens out of the speaker's mouth with a red light-ray burst. Red room: the scientist sits at a desk, smiling. | none | mouth-iris (12 f) | (sub drone continues) |
| 16 | 35.47–36.97 | 1064–1109 | "…the scientist?" (silence 36.3–37.2) | Whip-zoom, then the same plate seen through a keyhole matte. Hold 1 s, then accelerate through the keyhole. | none | whip-zoom into keyhole matte on "killed" | big boom 35.44 s (+22 dB, 0.77 s) |
| 17 | 37.00–38.90 | 1110–1167 | "Some editors rewatch this." | Defocused grid paper under window-blind shadow, rack focus to sharp. 3D extruded words reveal letter by letter. | SOME / EDITORS / REWATCH THIS | hard cut out of the keyhole push | click 37.01 s (**clips**) |
| 18 | 38.93–42.60 | 1168–1277 | "Others open the project file on earnedits.com." | Retro computer in a poster-covered room; the site scrolls on screen. An AE file tag drops on a rope and swings. A glass URL pill types the address. | "EarnEdits.com" typed | **card push-up #3** (f1168–1182) | boom 40.12 s (+27.8 dB) when the file lands; 4 rising ticks at 41.61–42.36 s |

Shape: 18 visual scenes in 42.6 s (mean 2.37 s each). 11 cut points: f90, 195, 440, 515, 575, 643, 711, 825, 970, 1110, plus a 1-frame flash at f737. The other 7 changes are in-camera. Cut density is highest from 17.2 to 27.5 s: 6 cut events in 10.3 s, one every 1.7 s. The edit holds from 0 to 17 s (hook plus long continuous moves) and again from 29.4 to 37 s (slow push, keyhole).

---

## 2 Hook dissection (0–3.0 s, frame by frame)

| frames | t (s) | What happens | Measured |
|---|---|---|---|
| f0–5 | 0.00–0.17 | Empty lab, heavily defocused: window, plants and microscope bokeh. Slight tilt down. No subject and no text. VO "A … Russian". | content moves up 10–15 px/f @360 (≈20–30 px/f @720) |
| f6–9 | 0.20–0.30 | The scientist's head enters from bottom centre, extremely close (≈3× final scale), with vertical/radial motion blur. | boom at 0.19 s (f6); sub transient f2 |
| f10–17 | 0.33–0.57 | Fly-back: she resolves holding a pipette and a flask. "scientist" at 0.44 s (f13). | per-frame scale 0.832, 0.881, 0.911, 0.931, 0.946, 0.956, 0.962, 0.972. Expo-out: log-velocity decays ≈×0.75 per frame |
| f18–27 | 0.60–0.90 | Full body, centred, settled. Lab sharpens; background is still soft (DOF). | drift continues at −1.1 %/frame (≈ −30 %/s); cumulative ×0.445 over f6–27 |
| f28–35 | 0.93–1.17 | An open hexagonal wooden coffin rises from the bottom edge **behind** the cut-out and **in front of** the plate. By f35 she stands inside it. | rise ≈8 f; VO "died" at 1.16 s = f35; booms at 0.99 s and 1.16 s |
| f36–42 | 1.20–1.40 | Coffin and subject drift together (zoom-out −1.1 to −1.6 %/f). | — |
| f43–48 | 1.43–1.60 | A dark circular soil patch with grass edges scales up behind the coffin from centre and fills the frame. The lab is gone. | 5–6 f iris; "mysteriously" at 1.56 s (f47) |
| f50–53 | 1.67–1.77 | Hard **grade switch to B&W** plus bloom and heavy blur. The coffin glows white. | 1-frame switch; zoom ×1.041 kick at f50 |
| f52–71 | 1.73–2.37 | A white lid slides in from the right with slight rotation and closes the coffin. Shovel sits bottom-right. | 20 f |
| f72–89 | 2.40–2.97 | Closed coffin in the grave; vignette darkens. VO pause (≈2.4–2.94 s). | zoom-out continues; cumulative ×0.378 over f52–89 (−62 %/s) |
| f90 | 3.00 | Hard cut to the crowd on "and". | click 3.01 s, peak 0 dBFS |

Why it works:
- 5 distinct visual events land in 3 s (subject in, coffin, grave, B&W, lid), one every ≈0.6 s.
- Each event is literally the VO word being spoken or about to be spoken: scientist→person, died→coffin, mysteriously→grave + B&W + darkness.
- The camera never settles, so there is no "safe" frame to swipe on.
- Sub drone at −15 dB under the whole hook gives physical weight.

Weak point: frame 0 is an empty blurred lab, which is poor for the feed thumbnail and the first impression.

---

## 3 Typography and on-screen text

**Rule:** Text is withheld from about 85 % of the VO (no captions). It appears only when the VO carries something that cannot be pictured or that needs proof:
1. Time: the date card.
2. Identity: the name. The VO never says it, so it adds information.
3. Evidence: diegetic headlines, annotated.
4. Abstract phrases: "Rumors … spread" and "But there was a twist."
5. The CTA.

Picturable lines (death, crowd, news, archive, officials, red room) get no text.

**Font per register (visual guesses):**

| Use | Look | Guess | Why this register |
|---|---|---|---|
| Date card | white condensed all-caps sans, #F7F8FB | Bebas Neue / Oswald | documentary "case file" factuality |
| Name pill | white bold geometric sans #FEF5EB on red #E61C1F pill | Poppins / Montserrat Bold | broadcast ID strap |
| Abstract words, word stack | white high-contrast italic serif with looped italic w, soft dark drop shadow | Playfair Display Italic | literary, "narrator's voice"; signals story over fact |
| CTA | heavy rounded display sans, 3D extruded, grain/halftone texture; gold / red / blue lines | ≈ Bowlby One / Rubik Black | deliberately breaks register: toy-like and branded, so it reads as "the ad part" |
| URL | thin sans inside a frosted glass pill, 1–2 px white stroke | Inter / SF-style | UI realism |

**Date card ("OCTOBER, 2026"), f195–259:**
- Background #17181B with dust and scratch overlay.
- Typewriter reveal with a vertical-bar cursor "I". "O" appears at f201 (6.70 s), 0.32 s **before** the VO says "October" (7.02 s). "OCTOBER" is complete at f211, which is exactly the VO onset. "2026" is complete at f226; VO "2026" starts at 7.38 s (f221).
- Rate: 13 characters in 25 frames = 1.9 f/char (≈15.6 char/s).
- After typing, the cursor blinks on a ≈12-frame cycle (≈).
- **Red underline** #921419, 5–6 px thick (0.45 % H). It trim-paths left to right behind the type, starting at f210 (22 px wide). It lags the text by ≈8–9 frames and reaches full width (341 px = 47 % W) at f234.
- Text block: 327 px = 45 % W; glyph rows ≈ 47 px including the comma (≈3.7 % H).
- The text rises during the card, continuing the upward motion of the outgoing crowd lift. Underline y moves 886 → 736 (f210–222, 12.5 px/f), then 4 px/f, then 3.3 px/f, then accelerates (6.7 px/f) into the exit. Total rise ≈300 px (from 70 % H to 46 % H): ease-out in, ease-in out.

**Name pill ("Darya Shipilova"), f276–331:**
- A small red block appears near her hand at f276. It expands horizontally from f282 to f290 (8 f, motion-blurred, text revealed by the expansion). Total ≈14 f. Complete at 9.67 s, while the VO says "-year-old laboratory".
- Final size 334 × 68 px = **46 % W × 5.3 % H**, corner radius ≈10 px. Placed **on the subject's chest** at y 582–649 (45–51 % H), not at the bottom of the screen.
- During the pull-back (f325–331) it desaturates with the photo. It ends up printed in the newspaper photo ("Darya Shipi…" is visible at f345–440). The graphic turns into evidence.

**Highlighter, then circle (two newspapers):**
- Yellow (≈#CFBE23 as composited on paper), f354–400. Line 1 "Dozens quarantined after researcher" runs f354–372 (18 f). Line 2 "at Russian plague laboratory Dies" runs f372–≈392. Line 3 "of 'unknown' infection" runs ≈392–400. Each line wipes left to right, ease-out, about 0.6 s per line, starting 7 f after "died" (f347).
- Green (#60ED28, lime, multiply look), f540–566. Line 1 "Russian lab worker dies" runs f540–≈552; line 2 "of suspected plague as" runs ≈552–566. The "R" first goes green at f540 (18.0 s; "putting" is at 17.66 s and "200" at 18.20 s).
- Red circle (#DB351F, ≈4 px hand-drawn ellipse with overlapping ends) around "200", drawn **f556–563 (≈8 f)**. It starts 10 f after VO "200" (f546) and lands on "contacts" (18.66 s).
- The order is always highlighter first, then circle, then a **×1.35 punch-in 9–12 f after the circle completes (f575)**, on the pause before "under medical observation".

**Blueprint single words, f445–513:**
- One word at a time, centred (y 610–662 = 48–52 % H), x-height plus ascenders ≈52 px.
- Widths: "Rumors" 258 px (36 % W) settled; "possible" 170 (24 %); "plague" 141 (20 %); "infection" 178 (25 %); "spread" 145 (20 %).
- Entrance: only "Rumors" animates. It pops in at 1.42× (366 px) and settles to 1.0 in 6 f, rotated with the grid. "possible" shrinks ≈12 % over 12 f. The rest hard-cut on and off.
- The words ride the grid's un-rotation and a −10 %/s drift.

**Vertical word stack, f825–881:**
- New words appear **above** the previous ones. The camera rises along a 3D-tilted column, so lower words get larger and defocused.
- At f850 line heights are 44 / 41 / 57 / 56 px; at f860 they are 75 / 47 / 49 / 82 px (bottom word "there" is blurred and big).
- "But" enters with a roll whip (−9°/f decaying, scale 0.79/f).
- Exit: pushed up by the press-conference card (f875–882).

**CTA 3D words, f1110–1167:**
- Paper #BBB6B5 starts defocused under a window-blind shadow and racks into focus over ≈15 f.
- Letters fade and scale in with blur, one at a time:
  - "SOME", gold #CCA758: f1114–1124, ≈2.5 f/letter, 453 × 108 px = **63 % W × 8.4 % H**.
  - "EDITORS", red (extruded median #8C282A): f1125–1135, ≈1.6 f/letter, 467 × 73 px.
  - "REWATCH THIS", blue #3769C9: f1137–1156, ≈1.8 f/letter, 456 × 51 px.
- Block spans y 472–719 (37–56 % H). Hold ≈11 f, then card push-up #3.

**URL pill:** glass pill ≈56 % W, drops in blurred at f1216–1222. "EarnEdits.com" types f1236–1254: 13 characters in 18 f = **1.4 f/char**.

**Per-word timing vs Whisper onsets** (positive = text after speech; frames):

| word | VO onset (s / f) | text on (f) | Δ f |
|---|---|---|---|
| October (typed, complete) | 7.02 / 210.6 | 211 | 0 (first letter −10) |
| 2026 (complete) | 7.38 / 221 | 226 | +5 |
| Rumors | 14.84 / 445 | 445 | 0 |
| of | 15.18 / 455 | 452 | −3 |
| a | 15.38 / 461 | 457 | −4 |
| possible | 15.52 / 466 | 462 | −4 |
| plague | 15.82 / 475 | 475 | 0 |
| infection | 16.24 / 487 | 490 | +3 |
| spread | 16.82 / 505 | 500 | −5 |
| But | 26.98 / 809 (VO-band energy f806–810 confirms) | 825 | **+16** |
| there | 27.74 / 832 | 835 | +3 |
| was | 28.10 / 843 | 845 | +2 |
| a | 28.26 / 848 | 850 | +2 |
| twist. | 28.34 / 850 | 855 | +5 |
| Some | 37.22 / 1117 | 1114 | −3 |
| editors | 37.40 / 1122 | 1125 | +3 |
| rewatch | 37.78 / 1133 | 1137 | +4 |
| this | 38.38 / 1151 | ≈1146–1156 | ≈0 |
| earnedits (typing start) | 41.06 / 1232 | 1236 | +4 |
| .com (complete) | 41.70 / 1251 | 1254 | +3 |

Takeaway:
- Blueprint words lead speech by about 2 f on average (range −5 to +3). That is good practice: the eye reads slightly ahead of the ear.
- Stack and CTA words trail by 2–5 f.
- "But" trails by 0.53 s because it waits for the transition. This is the biggest sync miss.

---

## 4 Motion and camera

**Measured camera** (from cam.json via camsum; % values are relative scale change, px @1080):

| segment | frames | scale %/s | cumulative | rotation °/s | notes |
|---|---|---|---|---|---|
| hook lab pull-back | 6–27 | −73.6 | ×0.445 | −0.95 | fly-back entrance |
| coffin rise | 28–43 | −35.6 | ×0.813 | 0.3 | constant drift |
| grave B&W | 52–89 | −61.7 | ×0.378 | 0.3 | never stops |
| crowd rise | 91–125 | −66.6 | ×0.311 | −1.7 | fly-back; ty −366 px/s |
| crowd hold | 126–170 | −5.9 | ×0.878 | 0 | the only gentle hold |
| crowd lift-out | 171–194 | +8.6 | — | 2.8 | ty accelerates to −685 px/s (ease-in exit) |
| date card | 202–258 | −5.8 | ×0.855 | — | text rises ≈300 px |
| lab2 enter | 262–280 | −123 | ×0.461 | 1.5 | in-out ease (per-frame 0.969 → 0.938 at f270 → 0.985) |
| lab2→paper | 323–344 | −38 | ×0.682 | — | then ×0.78 over f344–350 |
| paper exit | 401–438 | −25 | — | **+13.5** (cum +20.9°) | ty +758 px/s |
| blueprint | 441–512 | −9.9 | — | +3.6 (cum +15.2°, expo decay 1.9 → 0.4°/f) | rotation continuity |
| wood→NBC | 515–545 | −49 | ×0.661 | **−41** (cum −36.9°) | counter-roll pull-back |
| NBC punch | 575 | ×1.35 in 1 f | — | −0.5 | — |
| TV pull-back | 645–660 | −96 | ×0.407 | 0 | 15 fps (alternate frames duplicated) |
| TV exit | 700–711 | +107 | ×1.48 | 0 | ease-in push (1.03 → 1.24 per 2 f) |
| wall hold | 746–799 | ≈0 | — | 0 | photos converge; light rays move |
| wall exit | 800–824 | −16 | — | −8.8 (cum −11.7°) | roll leads into "But" roll |
| word stack | 826–874 | +18 | — | −29° cumulative (mostly f826–834) | camera rises, ty +511 px/s |
| press enter | 886–900 | −99 | ×0.601 | — | fly-back |
| press hold | 901–962 | +5.8 | ×1.12 | — | slow push |
| press→B&W | 963–979 | +66 then a jump to ×1.41 | — | −16.4° | Dutch tilt |
| red room | 1027–1062 | −38 | ×0.658 | — | per-frame 0.915 → 0.985 (expo-out) |
| keyhole exit | 1100–1109 | +65 | ×1.31 | 0 | ease-in 1.008 → 1.064 per frame |
| CTA push-up | 1172–1190 | ≈0 | — | — | ty −65 → −3 px/f @360, ×≈0.8 per frame (expo-out) |
| AE-file impact | 1210–1214 | camera bump 1.018 / 1.020 / 0.986 | — | — | defocus on impact |

**Signature moves:**
- **Fly-back entrance** (used 5×: f6, f91, f262, f884, f1027). Start ≈3× scale with motion blur. Per-frame scale goes 0.82 → 0.97 over ≈12 f, then keeps drifting at −1 to −1.2 %/f.
- **Continuous zoom-out drift as the default state.** Most holds are still shrinking 0.5–1.2 %/frame, so the frame always "breathes" away from the subject.
- **Ease-in exits.** Pushes accelerate into the cut (TV, keyhole, crowd lift), so the cut is "thrown" by momentum.
- **2.5D layering:** a cut-out subject or prop (scientist, coffin, newspaper, AE tag) sits over a defocused plate, with a third **foreground layer that rises from the bottom edge**: crowd front row, TV viewers f647–653, press mics f893–905, blurred foreground posters in the computer room. The parallax speed difference sells depth. DOF is faked with plate blur (backgrounds are soft in every shot).
- **Mixed cadence:** 30 fps everywhere except the TV room (30 of 67 frames duplicated) and the wall-photos section (40 of 113), which are effectively 15 fps. This plausibly reads as "archival / historical". ≈ deliberate posterize-time.

---

## 5 Transitions catalogue

| # | frames | duration | Recipe | Why there |
|---|---|---|---|---|
| T1 Fly-back entrance | f6–18 (and 91, 262, 884, 1027) | 12 f | Subject layer starts ≈3×, expo-out scale (0.83 → 0.97 per f), vertical blur, boom on frame 1. | Pattern interrupt; a person "arrives" at the viewer. Each use introduces a new character or location. |
| T2 Coffin insert + grave iris | f28–35, f43–48 | 8 f + 5 f | Insert the coffin layer between the cut-out and the plate, rising from the bottom edge (ease-out). Then scale a circular soil texture from centre behind the coffin until it covers the plate. | Shape-anchored scene change: the coffin persists, so the eye never loses the object while the world changes. Lands on "died". |
| T3 Grade switch | f50 | 1 f + 4 f bloom/blur | Hard switch to B&W with a glow flash, keeping the zoom. | Marks death; "mysteriously" goes cold. |
| T4 Lift-out to date card | f171–195 | 24 f + cut | Crowd layer accelerates upward (ease-in, faster than the grass, so parallax), then a hard cut to the dark card, where the type also rises. Swish 6.47 s (2.6 → 7.9 kHz). | Direction continuity (up → up) across a full change of material. Sits in the 0.9 s VO pause. |
| T5 Card push-up (×3) | f260–268, f875–882, f1168–1182 | 9 / 8 / 14 f | Next scene as a full-width card with ≈20 px rounded top corners slides up over the held previous frame. Expo-out (first frame ≈10 % H). Inner content runs a fly-back simultaneously. Boom ≈3 f before (8.56 s). | Reads like a new "page" or "story card". Used for chapter breaks: case details, officials' response, CTA. |
| T6 Frame-within-frame pull-back | f321–350 | 23 f + 6 f blur | Zoom out ×0.45 to reveal the shot was the photo inside a red coffin-hexagon frame on a newspaper. Desaturate the photo over f325–331. Blur zoom ×0.78 reveals hands. | "The person becomes the headline" (alive → printed, colour → B&W) on "Siberia died". The coffin shape quietly repeats T2. |
| T7 Roll-out, rotation-matched cut | f401–440 | ≈38 f exit + 0 | Paper drops bottom-left with +21° roll. Wood smears. Cut to the blueprint grid pre-rolled ≈+20°, which un-rolls with expo decay (1.9°/f → 0.4°/f over 20 f). Click at 14.66 s. | Motion vector continues through the cut, so it feels like one camera move. Placed in the 0.8 s VO pause. |
| T8 Macro-texture bridge | f514–534 | 1 f blur + 8 f hold + 12 f slide | Blur out the word, hard cut to an extreme close-up of the next set's surface (red wood, diagonal grain). Pull back with counter-roll (−41°/s). The hero prop (paper) slides in from bottom-right. Whoosh 17.18 s. | A texture full-frame is "neutral" enough to accept any cut, then becomes the new location. Fills a 0.66 s VO pause. |
| T9 Punch-in | f575 | 1 f | ×1.35 scale jump, no SFX. Framing moves to the third headline line ("enter medical observation"). | Emphasis cut that lands just before the VO reads the line. |
| T10 Zoom-out blur, then cut to screen | f641–645 | 4 f | Paper zooms out bright and blurry. Cut to a blurred close-up of the TV screen, then ×0.68 in one frame and keep pulling back; viewers rise in the foreground. | "Paper news → TV news". Hard cut on "The news" (±0 f). |
| T11 Push into the TV, wall texture | f700–712 | 12 f | Accelerating push-in toward the TV, cut to a grungy grey wall texture (12 f empty), then photos slide in from both edges (10 f). Whoosh 23.75 s. | Texture reset before the archive montage. |
| T12 Photo flash | f737–738 | 2 f | White flash (luma 75 → 194 → 83) as the photos land. Hit at 24.56 s. | Camera-flash = "archive evidence"; doubles as a beat on "for". |
| T13 Roll-matched cut into the void | f800–834 | 25 f + 9 f | Photo grid rolls −11.7° and shrinks. Cut to "But" entering with −9°/f roll and 0.79/f scale, decaying. Boom plus click 27.4–27.5 s. | Twist line gets a hard visual reset (images → pure type on black). |
| T14 Punch + Dutch + B&W | f963–979 | 7 f accel + 9 f settle | Accelerate the push (1.5 → 3.5 %/f), jump to the same plate ×1.41, −16.4°, crushed B&W, blur settling over 9 f. Boom at 32.26 s. | Lands on "no" (+2 f). Distrust of the official line. |
| T15 Mouth iris | f1021–1033 | 12 f | A red glow appears on the speaker's mouth (f1021). A circle grows from there with a light-ray burst. Saturation goes 24 → 154 in 7 f. The inner red-room plate zooms out (0.915 → 0.985 per f). | The question comes "out of the official's mouth". Starts 3 f before "So". |
| T16 Whip into keyhole | f1063–1069 | 6 f | Blur whip, then the same plate ×0.90 behind a keyhole matte with a warm rim light. Big boom at 35.44 s. | On "killed" (+1.5 f): voyeur/secret framing for the unresolved question. |
| T17 Push through keyhole | f1100–1110 | 10 f | Ease-in zoom (1.008 → 1.064 per f) until the matte leaves frame, then cut to defocused paper with a click at 37.01 s. | Exits the story "through the door"; the CTA begins in the 0.96 s silence. |
| T18 AE file drop | f1199–1225 | ≈26 f | File tag on a rope drops from the top with an overshooting ease. Lands f1210 with a camera bump and defocus, then swings like a pendulum (≈±80 px, half-period ≈28 f). | Lands on "file" (40.40 s). The rope and noose read as a "hanging" file, echoing death. ≈ intended. |

---

## 6 Motion-graphic devices and metaphors

1. **Coffin as recurring shape.** Open coffin (f28), closed coffin (f71), the coffin-shaped hexagon photo frame in red outline (f322–440). Built as a cut-out layer, then a red-stroked elongated hexagon mask. It works because the death metaphor carries forward without being restated, and the shape gives the eye an anchor through transitions.
2. **Grave iris.** Circular soil texture scaled from 0 behind the coffin, with an irregular edge (≈5 f). Changes the world while the object stays put; "buried" reads instantly.
3. **Live-to-print pull-back.** The video shot of the person becomes the newspaper photo, desaturating as it shrinks. The name pill is baked in, so the motion-graphic becomes a printed artefact. It sells "this is documented".
4. **Highlighter → circle → punch-in.** Line-by-line left-to-right wipes (18–20 f per line), then a hand-drawn red ellipse (≈8 f), then a ×1.35 punch-in. This mimics a researcher annotating evidence and guides the eye to the number before the VO finishes the clause.
5. **Typed date card with trailing red underline.** Typewriter (1.9 f/char) plus a cursor, with the underline trim lagging ≈8 f. Reads as a "case file timestamp"; the red underline seeds the red motif.
6. **Name pill on the body.** The red pill expands from a block on the subject's torso. Attaching the label to the person (not a screen-bottom strap) reads like an ID badge, so she is "this specific worker".
7. **Single-word serif on blueprint.** Abstract phrase ("rumors spread") rendered as type on a plan-like grid: a rumour has no picture, so the words are the picture. The blueprint suggests "plan/plot".
8. **Vertical word stack in a void.** Words build upward on a tilted 3D plane with DOF. It slows the read to word-by-word for the pivot line and makes "twist." the top and largest word.
9. **Selective colour.** Press conference desaturated (sat 42) while the flag (red/white/blue) and the red, blue and green mics keep full colour. Directs attention to "Russian officials" and the media.
10. **Dutch B&W punch.** Same plate re-used ×1.41, −16°, crushed blacks (highlights only reach #8C8D90). Turns the official into a suspicious figure on "no outbreak was confirmed".
11. **Mouth iris into the red room.** The circle is born at the speaker's mouth and the red light floods out. "Officials say X" opens into "what actually happened?". The scientist sitting calmly in red light suggests conspiracy or a secret lab.
12. **Keyhole.** The matte frames the same red-room plate (×0.90) with a rim-lit edge. Peeking through a keyhole = forbidden knowledge; it holds the open loop visually for 1 s of near-silence.
13. **Hanging AE file.** The CTA prop is an "AEP" tag on a rope, swinging. It keeps physical motion in the CTA and echoes the death theme. ≈ intended.
14. **Retro computer room.** The website appears on a CRT inside a busy poster room (2.5D, blurred foreground). The product is shown "in the world", not as a flat screen recording.

---

## 7 Colour and finishing

**Colour script** (frame medians unless noted):

| t (s) | Scene | Median | Highlight | Sat (0–255) | Luma |
|---|---|---|---|---|---|
| 0–1.6 | lab (cool blue-white) | #6D87AB | #EBF1F7 | 88 | 136 |
| 1.7–3.0 | grave **B&W** | #1B1C1F | #C8D1D7 | 36 | 40 |
| 3.0–6.5 | crowd, warm sunset | #4E3C2C | #F0E6DA | 111 | 90 |
| 6.5–8.6 | date card | #17181B (text #F7F8FB, underline #921419) | — | 35 | 27 |
| 8.7–10.7 | lab 2 (name pill #E61C1F) | #637A9F | #F2F3F4 | 99 | 123 |
| 10.8–14.6 | B&W photo in newspaper on charcoal wood (yellow highlight ≈#CFBE23) | #413C3B | — | 40 | 91 |
| 14.7–17.1 | blueprint | #223D70 (shadow #0F244E, grid #6077A7) | — | **170** | 64 |
| 17.2–21.4 | red wood / NBC (green #60ED28, circle #DB351F) | #592E20 → #5E4436 | — | 162 → 96 | 58 → 102 |
| 21.4–23.7 | TV room, teal with warm lamps (teal-orange) | #232B28 | #EBF0EE | 84 | 60 |
| 23.7–27.5 | wall, B&W photos | #333E40 | #D9D8D2 | 56 | 78 |
| 27.5–29.4 | word void | #161F22 | — | 85 | 34 |
| 29.4–32.3 | press, desaturated plus selective colour | #35343A | #B2AAAD | 42 | 69 |
| 32.3–34.0 | crushed B&W close-up | #1E1F22 | #8C8D90 | 26 | 46 |
| 34.0–35.4 | **red room** | #61211F (red mask #772320) | #B6A3A0 | **143** | 68 |
| 35.5–37.0 | keyhole | #1F1615 | #B38C82 | 99 | 38 |
| 37.0–38.9 | CTA grid paper | #BBB6B5; gold #CCA758, red #8C282A, blue #3769C9 | — | 26 | 135 |
| 38.9–42.6 | retro room (green/orange; AE tag #726EE5) | #29352C | #A5856A | 95 | 58 |

**Logic:**
- B&W marks death, the past and doubt: grave, printed photo, archive, the denial close-up.
- Saturation spikes mark "information" scenes (blueprint 170, red wood 162) and the reveal (red room 143).
- Luma flips at 1.7 s (light → dark), 9 s (dark → light), 12 s, 37 s (dark → bright CTA) and 39 s. The CTA is the brightest neutral frame since the opening (luma 135), so the context switch is visible.
- **Red thread:** underline #921419, then name pill #E61C1F, hexagon outline, circle #DB351F, flag, red room #61211F, and "EDITORS" red. The red room cashes in the motif.

**Finishing:**
- Dust and scratch overlays on the date card and wall.
- Bloom on the B&W switch (f50–53) and on the red iris (light rays).
- Vignettes in the grave, word void and keyhole.
- Halftone/grain on the CTA letters.
- Soft drop shadows on all serif words (dark, ≈6 px down, ≈8 px blur, ≈60 %).
- Motion blur on every fast move (directional, matched to the move).
- Fake DOF throughout.

---

## 8 Sound

**Bed:**
- No melodic or rhythmic music is detectable. Tempo autocorrelation r ≤ 0.16 and there are no stable harmonic lines outside the VO.
- The "score" is **sub-bass drones and boom tails** in the 20–80 Hz band, between −12 and −17 dB:
  - 0–3.7 s (whole hook)
  - 8.7–9.1 s (card push-up #1)
  - 11.6–13.7 s (newspaper)
  - 17.2 s and 21.5 s (cuts)
  - 32.3–34.5 s (denial close-up into the mouth iris)
  - 35.4–36 s ("killed")
  - 40.1 s (AE drop)
- In the CTA the sub drops to −46…−72 dB and the gap spectrum moves to 123–370 Hz, a lighter bed (≈).

**VO:**
- Mid RMS −14.5 dBFS against side RMS −22.6 dBFS. VO is centred; SFX are wide (side/mid −9 to −22 dB per 2 s).
- Median level during VO −17.1 dB, in gaps −20.4 dB. The gaps are barely quieter because booms fill them.

**SFX-to-picture map** (side-channel events; offsets in frames, + means the event comes after the picture):

| SFX (s) | type | Picture event | Δ |
|---|---|---|---|
| 0.19 / 0.37 | layered boom (sub 87 %) | head enters f6 | 0 |
| 0.67 | boom | subject settles f20 | ≈ |
| 0.99, 1.16 | booms | coffin rise f30 / "died" f35 | 0 / 0 |
| 3.01 | click 7.5 kHz (**0 dBFS**) | cut f90 | +0.3 |
| 4.45 | hit | crowd hold (≈) | — |
| 6.47 | swish-hit 2.6 → 7.9 kHz (**0 dBFS**) | cut to date card f195 | −1 |
| 8.56 | boom +25.9 dB, 0.79 s | card push-up starts f260 | −3 (pre-lap) |
| 11.44 | boom 583 → 1240 Hz | pull-back into newspaper f343–345 | ≈0 |
| 14.66 | click (**0 dBFS**) | blueprint cut f440 | 0 |
| 17.18 | whoosh-boom 2.4 k → 409 Hz (**0 dBFS**) | wood cut f515 | 0 |
| 21.49 | whoosh-boom 1.4 k → 278 Hz (**0 dBFS**) | TV cut f643 | +2 |
| 23.44 / 23.75 | boom + down-whoosh (**0 dBFS**) | TV push-in / wall cut f711 | 0 |
| 24.46 / 24.56 | hits | photos land plus flash f737 | 0 |
| 27.39 / 27.52 | boom + click (**0 dBFS**) | wall roll-out → "But" cut f825 | −3 / +1 |
| 32.26 | boom | B&W Dutch punch f970 on "no" | −2 |
| 35.44 | boom +22 dB, 0.77 s | whip on "killed" f1063 | 0 |
| 37.01 | click 8.3 kHz (**0 dBFS**) | CTA cut f1110 | 0 |
| 40.12 | boom +27.8 dB | AE file lands f1204–1210 | −2 to 0 |
| 41.61 / 41.86 / 42.11 / 42.36 | 4 ticks, 0.25 s apart, rising +8 → +20 dB | URL complete f1254 → end | ≈ outro sting |

Rules inferred:
- Every visual cut or transition gets an SFX within ±3 frames (8 of 9 hard cuts, plus all scene-internal "impacts"). Scorecard cut-to-air offsets are 0.02–0.05 s.
- **High clicks/swishes** mark material changes (cut to card, blueprint, CTA). **Descending whoosh-booms** mark location changes (wood, TV, wall). **Pure sub booms** mark meaning (died, killed, the file).
- Booms pre-lap pushes by about 3 f.
- The punch-in at f575 is the only silent cut.

**Loudness:**
- −15.2 LUFS integrated, LRA 4.4 LU (heavily compressed).
- **True peak +3.4 dBTP. All 19 samples ≥0.99 sit on 8 transition SFX** (3.02, 6.56, 14.69, 17.19, 21.49, 23.72, 27.52, 37.02 s). The transition hits were placed at 0 dBFS without a limiter, so they distort after AAC/Opus transcoding.

**VO pauses and how they are filled:**

| Pause (≈s) | Filled visually by | Filled sonically by |
|---|---|---|
| 2.4–2.94 | lid closing, zoom-out | sub drone |
| 6.04–6.94 | crowd lift-out, cut, typing starts at 6.70 | swish 6.47 |
| 7.9–8.9 | cursor blink, text drift, card push-up at 8.67 | boom 8.56 |
| 14.04–14.84 | paper roll-out, blueprint cut, un-roll | click 14.66 |
| 17.0–17.66 | wood bridge, paper slide | whoosh 17.18 |
| 20.74–21.44 | zoom-out blur exit | — (cut lands on "The") |
| 33.56–34.14 | B&W hold, red glow on mouth from f1021 | sub drone |
| 36.26–37.22 | keyhole hold, push-through | click 37.01 |

No pause is left empty. Each one carries a transition or a moving device plus an SFX.

---

## 9 Storytelling and retention devices

- **0.0–2.4 s, literal triple:** scientist → died (coffin) → mysteriously (grave + B&W). Every noun or verb gets an image, with one visual event every 0.6 s.
- **3.0 s, stakes widen:** a single death becomes a deadly plague (crowd). The scale jump from one person to many is the second hook.
- **6.5–11 s, specificity stack:** date (typed), age plus job (VO), name (on screen, never spoken), place (VO). Each new fact is a new visual layer, which builds credibility.
- **10.8–11.5 s:** the person turns into a headline (pull-back plus desaturation): proof device.
- **11.8–13.3 s and 18.0–19.2 s, annotated evidence:** highlighter, circle on "200", punch-in. Teaches the eye where to look and pays off with a number.
- **14.7–17 s, abstract to type:** rumours have no picture, so the words become the picture. It also changes texture at the 15 s mark, where a mid-video drop-off often happens.
- **17.2–27.5 s, acceleration:** 6 cut events in 10.3 s across the "spread → news → history" escalation. The 15 fps archival cadence at 21.4–27.5 s adds texture change.
- **27.5 s, the twist reset:** all imagery is removed (black void, words only), then the officials arrive by card push-up. A strong pattern break at about 65 % of runtime.
- **32.3 s, visual editorial:** the Dutch B&W punch on "no" tells the viewer to distrust the denial without saying it.
- **34.1 s, open loop:** "So what actually killed the scientist?" The mouth iris and the alive-looking scientist in a red room imply a hidden truth. The keyhole holds the question through 1 s of silence.
- **37.0 s, CTA converts the open loop:** "Some editors rewatch this" assigns the viewer an identity (editor) and an action (rewatch, which drives loop/rewatch metrics). "Others open the project file…" is a binary choice that reframes the whole story as a sample of the product.
- No resolution is given, which drives comments ("what killed her?") and rewatches.

---

## 10 Weaknesses and mistakes

1. **Clipping:** true peak +3.4 dBTP; 8 transition SFX hit 0 dBFS (19 samples). Use a −1 dBTP limiter and keep transition hits at −6 to −3 dBFS.
2. **Dead first frames:** f0–5 are an empty, blurred lab with no subject or text. The thumbnail and first impression are weak, and the strongest image (coffin + subject) only appears at f35.
3. **Text sync is inconsistent:** "But" appears 16 f after it is spoken, and CTA words trail 3–4 f, while blueprint words lead by up to 5 f. Choose one rule (lead 2–3 f) and keep it.
4. **Date card is too small and low-contrast:** about 3.7 % H text and a #921419 underline on #17181B (low luminance contrast) are hard to read on a phone.
5. **The fly-back entrance repeats 5 times.** Predictable by the third use (f262), and the 3rd–5th uses have no SFX variation.
6. **Mixed frame cadence:** 15 fps segments (TV, wall) next to 30 fps zooms look like stutter unless signposted (no film grain or gate weave was added to justify it).
7. **Fabricated evidence risk:** a real outlet's branding (NBC-style masthead) on generated headlines, a generated "named victim", and AI photos presented as archive photos, all without disclosure. This is a credibility and policy risk. Use fictional mastheads or clear "illustration" framing.
8. **AI artefacts:** headline casing errors ("Dies" mid-line), garbled body text, hands on the newspaper. Visible on pause, which undermines the "evidence" device.
9. **Story payoff missing:** the question is asked, but no hint or theory follows. The red room and keyhole imply a conspiracy that is never addressed. Viewers who want the answer get an ad.
10. **CTA is 13 % of runtime (5.6 s)** with no story value, and the end frame does not loop back to frame 0 (lab). A loop-friendly last frame would compound rewatches.
11. **The name pill covers the subject's torso** and appears only once. The style is never re-used, so it reads as a one-off.
12. **Low-information opening VO:** 130 wpm and only 5 words in the first 2.4 s. The visuals carry the hook alone.
13. **The punch-in at f575 has no SFX** while every other cut has one. Inconsistent, although it does not hurt much.

---

## 11 Steal list (recipes with numbers)

1. **Fly-back entrance:** subject cut-out starts at 3× scale. Per-frame scale 0.83 → 0.88 → 0.91 → 0.93 → 0.95 → 0.96 → 0.97 (expo-out, ≈12 f), directional blur on frames 1–4, sub boom on frame 1. Then keep drifting at −1 %/f. Use at most twice per reel.
2. **Shape insert on the verb:** put a prop layer (coffin) between subject and plate. Rise from the bottom in 8 f so it lands exactly on the verb ("died"). Then iris a new background texture from centre behind it in 5 f, and hard-switch to B&W plus bloom on the next word.
3. **Card push-up for chapter breaks:** the next scene is a full-width rounded-corner card (≈20 px radius @720) sliding up. Expo-out over 9–14 f, first frame about 10 % H. Pre-lap a sub boom by 3 f. The inner content runs its own entrance at the same time.
4. **Typed date card:** condensed caps, white on #17181B, about 45 % W. 1.9 f/char with a bar cursor that blinks on a ≈12 f cycle. A red trim-path underline (5–6 px) trails the text by 8 f. The block drifts up about 300 px (ease-out). Start typing 10 f before the VO says the date.
5. **Body-attached name pill:** red #E61C1F pill, 46 % W × 5 % H, white bold sans, placed on the subject's chest. It expands from a small block in 8 f with motion blur, then gets "printed" in the next shot.
6. **Live-to-print pull-back:** zoom out ×0.45 over 23 f to reveal the shot is a photo in a newspaper frame. Desaturate in 7 f mid-move, then blur-zoom ×0.78 over 6 f to reveal hands holding it.
7. **Highlight → circle → punch:** line-by-line left-to-right highlighter at 18–20 f per line (lime #60ED28 or yellow). Then a hand-drawn red ellipse (#DB351F, 4 px, 8 f) around the number about 10 f after the VO says it. Then a ×1.35 punch-in 9–12 f later on the next clause.
8. **Rotation-matched cut:** roll the exit +20° with ease-in, cut to the next plate pre-rolled the same way, and un-roll with expo decay (1.9°/f → 0.4°/f over 20 f). Click SFX on the cut.
9. **Macro-texture bridge:** cut to an extreme close-up of the next set's surface for about 8 f, then pull back with a −40°/s counter-roll while the hero prop slides in over 12 f. Use a descending whoosh-boom (2.4 kHz → 400 Hz).
10. **One-word serif for abstract lines:** Playfair-style italic, white with a soft drop shadow, centred, 20–36 % W. The first word pops 1.42 → 1.0 in 6 f; the rest hard-cut. Lead the VO by 2 f.
11. **Twist word stack:** pure dark void (#161F22). Words added upward on a 3D column tilted so lower words grow and blur. Camera rises about 500 px/s @1080. Exit with a card push-up.
12. **Denial punch:** re-use the same plate at ×1.41 with a −16° roll and crushed B&W (whites capped ≈#8C8D90). Blur settles in 9 f; boom on the negation word ±2 f.
13. **Mouth iris:** a red glow starts at the speaker's mouth 3 f before the question. A circle grows over 12 f with light rays; saturation goes 24 → 154 in 7 f. The inner plate zooms out 0.915 → 0.985 per f.
14. **Keyhole hold for the open question:** whip-zoom on the key verb (6 f, boom). Same plate ×0.90 behind a rim-lit keyhole matte. Hold 1 s through silence, then ease-in push (1.008 → 1.064 per f) through it into the CTA with a click.
15. **SFX grammar:** high click for a material change, descending whoosh-boom for a location change, sub boom for a meaning word. SFX within ±3 f of the picture event; fill every VO pause ≥0.5 s with a move plus SFX. **Unlike r3, limit transition hits to ≤ −3 dBFS and master to −14 LUFS / −1 dBTP.**
