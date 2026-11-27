---
name: app-product-animation
description: Use for SaaS / product motion-graphics videos with no talking head (app UI, cards, cursor, type-on, logo bookends) - "SaaS video", "product demo animation", "app UI motion graphics", "feature explainer", "logo + UI reveal", or a client wanting SaaS-style motion. Gives the motion grammar, typography, grade, measured easing/duration ladder, beat tables, SFX recipe, and talking-head adaptations (product review, premium news show, 3D explainer without Blender).
---

# SaaS / product motion graphics
Learned from refs 09-11 (Google Drive, ChatGPT, Spotify spec reels), 62-63 (showreel, SFX-pack promo), 69 (14.5 s "wireframe vs final" SaaS Short), 70-74 (five smooth-animation UI promos). Deepak: "high-demand videos; SFX creates the impact; learn seriously, no mistakes." Related: `motion-graphics-style`, `client-video-editing-process` (HTML/GSAP + puppeteer + mix2.py), `my-editing-rules`. `experiment/` paths are historical; finished work and code are in `edited videos by claude/<video>/code/`.

## 1. Structure
Logo enters, product name types in beside it, feature story told with the UI itself (3-6 morphing states), tagline (1-2 short lines), logo + name again. 9-16 s. **Zero hard cuts** in single-scene reels; the only "cuts" are a theme switch (light/dark), a white-out from the bottom, or fade-through-black. One element, one colour, one action at a time; only a tiny footer credit besides.

## 2. Motion grammar
1. **Morph, never cut**: pill > card > dialog > toast > pill > check; arc > input bar > send button > photo tile > full frame; text > avatar circle. A morph takes **6-12 frames (0.2-0.4 s)**, often with a few degrees of 3D tilt.
2. **Motion blur on every fast move** (anything travelling > ~10 % of frame arrives as a directional streak). Nothing pops in sharp.
3. **Spring settle once**: a dropped logo overshoots once and settles in 10 frames; UI ease-outs have no bounce; a clicked pill **tilts -8 deg** like a press and settles.
4. **Glow bloom = the impact**: brand-colour radial glow expands behind the landing element (0.3 s colour wash, click ripple rings, green success bloom). Light, not camera shake.
5. **Cursor is the actor**: white hand cursor with blurred trail, hover highlight jumps row to row (visible before the click), press tilt, ripple, drag-and-drop.
6. **Staggers**: menu rows 4-5 frames apart; list rows 3; filter pills 4; check marks 4; tagline words about 0.4 s.
7. **Move-hold-move**: hold **0.5-1.3 s** after each landing.
8. **One camera move at most** (e.g. 0.7 s push-in about 1.6x toward the button before the click); otherwise camera locked, objects move.
9. **Bookends**: outro repeats intro logo + type-on.

## 3. Typography
- The product's own UI face (Google Sans / Inter-like grotesk, medium), sentence case, tight tracking. Hero words 8-10 % of frame height, taglines about 5 %, UI text 2-3 %, footer 1.5 %.
- **Letter type-on with tracking collapse and colour flip**: each letter arrives in accent (or lighter grey) with wide tracking that collapses as it turns white/black; 15-25 chars/s; product name 2-3 frames per letter. Taglines build word by word (grey > final).
- Word swap in place (blur out / type in); headline may whip in with horizontal blur; exits fade upward or blur-wipe.
- Logo/tagline centred; feature beat can be a left-aligned hero block (H1 + 3-line paragraph + pill). UI text lives inside its element. Never overlap two elements.

## 4. Grade and colour
- Dark stage: luma 6-20, blacks 0-10, radial brand bloom (ChatGPT blue sat 30-52 %, Spotify green sat 72-97 %). Light stage (Drive): lavender-white, luma 240, sat 7 %, not pure white.
- **One brand colour + black/white**; glows, highlights, ripples, progress bars, accent letters all use it (plus green for success).
- Radial-gradient backgrounds (lit centre, dark edges). No grain, textures or particles.

## 5. SFX recipe (carries the impact)
No voice-over in the references. 83-100 % of visual events have a sound within 120 ms. Every screen change: a **300-900 ms riser/reverse swell** starting within +-100 ms of motion start and **ending on the landing frame**, a **low landing hit (43-65 Hz sub-drop) within +-80 ms** of landing, then a **settle tick 30-100 ms later, 10-20 dB quieter**. One dry "glassy UI" family (8-14 kHz shimmers/dings, sub-drops, one chime, 5-20 ms clicks); reuse samples (same pop x3, chime x6); only one sound per reel gets a reverb tail. Levels are 5 ms RMS peaks for a -14 to -16 LUFS master; lead negative = before the visual.

| Event | Sound | Level dBFS | Timing |
|---|---|---|---|
| logo / hero pops in | HF tick or reverse swell + 43 Hz sub boom + settle click | tick -7, boom -5..-7, click -12 | tick -130 ms; boom -130..-270 ms before bloom; click +20..+60 ms |
| card/panel slides or morphs | riser 300-520 ms + landing impact + 2-4 settle ticks | riser -18 to -12, impact -6, ticks -14..-20 | riser start +-100 ms of motion; impact on landing +-40 ms; ticks +50..+200 ms |
| light/dark or screen transition | bright falling whoosh 8-11 kHz (150-300 ms) + shimmer + tick | whoosh -13..-17, tick -17 | +40 ms after cut; one transition per reel gets a 1 s reverb tail |
| cursor click | 2-4 soft clicks in travel, click on press | -12..-15 (travel -27) | on frame +-15 ms |
| hover highlight | tiny tick | -30..-33 | +60..+180 ms after highlight |
| word/chip pops in | one pop (1.29 kHz, 47 ms) or chime (237 Hz) or bell (1.79 kHz); pick one, reuse | pop -13 / chime -4 | 30-60 ms before the word |
| title/headline | 12-14 kHz glass ding + short whoosh + tick | ding -16, tick -16 | +50 ms |
| type-on | **one** noise riser 600-900 ms with one HF tick per letter inside; never a click per key | riser -8..-6 | first to last letter |
| typing in a field | loud sub thud on first key, click+thud keys 2-3, then silence | -5 / -12 | on keystroke |
| progress bar | 12-16 tonal ticks 50 ms apart rising 2 to 12 kHz, then completion sound | ladder -11, completion -19 | completion +100..+250 ms after last tick |
| success/check | sub boom + 330 ms riser + falling HF whoosh with 1 s tail | boom -24, riser -16, whoosh -16 | boom -140 ms; whoosh +200 ms after tilt peak |
| outro tagline | drop SFX layer 15-20 dB, clicks -24..-35, then air only | | click on the word |

**Bed, pick one and commit:** (a) **no bed**: SFX over digital silence, each tail is the bed (Drive, 44 % silence); (b) **music-led**: one continuous track (ChatGPT 88.4 BPM), first UI action is the drop, beats on the kick grid (cuts <= +100 ms after a kick), swells end on downbeats, SFX only as filter sweeps in the music, about 8 dB sidechain pump, no UI clicks; (c) **intro swell then air**: 2 s pad swell, dry SFX over a -46 dBFS air floor, 20 dB breakdown for tagline/logo (Spotify). Density: 4.6-6.7 sound objects/s when SFX carry it, about 0.8/s when music does; busiest seconds are the quiet builds. Stereo: risers/impacts wide, clicks mono, pan one accent toward its element (+-5 dB). Master -14 to -16 LUFS, peaks -1 dBTP (ref09's +1.7 dBTP is clipped; don't copy).
**With voice-over** (product reviews): recipe (b) or a quiet (c); hits 8-13 dB over bed but under voice; ticks -25..-35 so they never mask words.

## 6. Build with our kit
Use `edited videos by claude/2. Mr Unbox iPhone 18 Pro/code/` (HTML + GSAP, puppeteer render `--sub 4` motion blur, `mix2.py`). Real DOM/SVG UI; GSAP morphs (`width/height/borderRadius` + `rotationY`); type-on = per-letter spans (tracking 0.3 em to 0, accent to white); glow bloom = radial-gradient div scaled up behind; streaks = supersampled render (or directional `filter: blur()` 3-4 frames); cursor = SVG hand with 3-frame blurred trail. A cue (`sfx()`) per event; one timeline, no cuts.

## 7. Showreel and promo formats (refs 62-63)
**Showreel (15 s, 16:9, dark, 0 cuts, music at about 120 BPM):** numbered chapters, one technique each, 1.2-2.2 s (countdown, kinetic type, dot/pill grid, particle sphere assembling a word, iridescent 3D blobs over a giant word, dashboard demo, orbit-path wordmark, outro), joined by morphs; only hard cuts are a **6-word slam at 3 frames per word** on the beat, each word a different texture. **Persistent HUD**: mono-caps corner captions (project/chapter + number / 1920x1080 60 FPS / timecode) with thin rules. **4-colour kit, one per chapter** (orange, lime, violet, cream on black); display = extended heavy grotesk, countdown digits and key phrases in serif italic, "Form." in script. Letter-to-object morphs (O > disc > grid > pills > particles > type); wordmark types on with glyph scramble over a ruler rule that becomes the frame colour. **Dashboard in 2.2 s**: four cards in four colours pop staggered about 0.15 s, counter 0 to +248 %, ring to 99 %, toggle flips, line chart rises, cursor drags the cards off. Audio: every change and slam on the 0.5 s kick, 72 % energy < 150 Hz, no UI ticks, -14 LUFS.
**SFX-pack promo (15 s, 9:16, white, 0 cuts, SFX-led, no music):** word-ladder script, one word/pair at a time, accent blue then black, tracking collapsing; readable muted. Each noun gets a lookalike UI object (clock on a drawn arc, search bar typing letter by letter with hand cursor, Drive-style file list with hover walking down rows, drag-and-drop onto a phone card, pixel-bloom "processing" wash, app card). Exits: word scales to a point (dashed vertical guides) or the UI pushes to a corner; ends on a black corner wipe. One Apple-style grotesk, sentence case, one blue; only brand wordmarks multicolour; phone cards about 36 % width. Audio: 2.6 soft pops/s, nothing above 4 kHz, 9 % silence, thud on search and drop, -14 LUFS (a muffled low pop kit works as well as glassy).
Use: showreel grammar for channel/brand trailers or "what I can build" reels; promo grammar for tool/pack/course sells with one accent.

## 8. Professional SaaS Short: problem, product, result, CTA (ref 69)
14.54 s, 1080x1920, 60 fps. Format: white page, two rounded 880x482 panels stacked with big soft shadow, lowercase heavy-black labels (`wireframe`, `final`); top panel plays the same animation stripped to an After-Effects-style view (`#F7F7F7`, green grid, dotted anchors, red/blue keyframe handles, centre guide). A "how it is built" showcase: build the scene once, render a stripped wireframe pass beside it.

Beat table (6 scenes: 2.7 / 2.4 / 3.8 / 1.4 / 2.5 / 1.7 s, two hard cuts, an event every 0.5-1.4 s):
| t (s) | What | Motion / audio |
|---|---|---|
| 0.0-0.4 | "So" on near-white card | deblur+fade 0.4 s; silent |
| 0.6-1.4 | "You want / a / clean motion / ad", one word/pair at a time | each deblurs ~0.2 s, line scales down to stay centred; low onsets 0.62, 1.14, 1.51 |
| 1.8-2.6 | "For your **product**" (heavier word) holds 0.6 s | fade+shrink out 2.5-2.7 |
| **2.70** | hard cut: one pure-white frame, then globe | low onset 2.83 (+130 ms late) |
| 2.75-3.6 | "But" deblurs; small stacked "can't find / right person" beside slowly drifting globe | blur-in per line; hits 2.83, 3.0, 3.15, 3.35, 3.6 |
| 3.6-5.0 | four avatar pins pop on Europe 0.15 s apart, hold | hits 3.6, 3.82, 4.18 |
| 5.07-5.50 | two navy liquid lobes sweep in (top-right, bottom-left) and meet as a 4-point white star | 13 frames; low 5.39 (-60 ms before completion) |
| 5.5-5.8 | star holds, shrinks, spins about 90 deg | 0.25 s |
| 5.8-6.3 | "Yonomi" wordmark deblurs; star slides onto the Y and settles as logo mark | low 6.22 |
| 6.3-8.8 | logo hold 2.5 s: mark idles in 3D (x/star silhouette every 0.4 s), bright horizon arc along bottom | quietest stretch, music only |
| 8.83-9.0 | light band wipes down from top, bg to white | 0.17 s; low 8.86 |
| 9.0-9.4 | full-width saturated-blue band with spinner arc; "Sell" + "USD 209.99$" slide in, "Mastercard ....1234" row joins; band shrinks into button | morph |
| 9.6-10.25 | spinner closes to ring, green-glow check, white check; hold 0.45 s | 0.15 s |
| 10.25-10.33 | **power-down**: white card dims to near-black in 5 frames with one white streak | 0.08 s; hi/air onsets 10.42, 10.56 (-24 dBFS) |
| 10.35-10.48 | "306.53 $" types on in 8 frames at 60 fps (3, 30, 306, 306.5, 306.53, $); "Total Money" fades in above | 0.13 s |
| 10.4-12.7 | dark scene: neon comet (blue, green, white, purple, red, yellow) every 0.2-0.35 s, each **glows the digit it crosses in its colour**; white blooms at 10.9, 11.5 | arcs 0.3-0.5 s; sub onsets 10.97, 11.25 (-12.9 dBFS), 11.56 |
| 12.6-12.7 | frame smears horizontally 1-2 frames, yellow comet at right edge | low 12.71 (-90 ms) |
| **12.80** | hard cut to blue gradient; white comet loops in from left (0.3 s), becomes outline of a glass pill | sub -36 dBFS at 12.98 |
| 13.1-13.4 | pill narrows and blurs, "send me your message" at 13.2, arrow grows > to play by 13.4 | 0.2 s; hi 13.26, low 13.27 |
| 13.4-14.54 | CTA holds 1.15 s, faint sheen | music falls about 10 dB (1 s RMS -12.7 > -17.2 > -22.4) |

New patterns: (1) **text before product**: first 2.7 s is only the pain sentence, product at 5.5 s; arc pain, "can't find the right X", brand reveal, one feature, result as a number, CTA. (2) word-append sentence with auto-fit and weight contrast on the key word. (3) **shape = transition = logo** (lobes meet as star, shrinks, spins, becomes logo mark). (4) idle on holds (3D mark spin + horizon arc glow). (5) band > button > spinner > green-glow check (green is the only second hue in UI). (6) 5-frame power-down cut while the number types on. (7) result number types in 0.13 s, label after; comets glow digits. (8) 2-frame blur-out then hard cut; next scene's first move is a comet drawing the CTA pill outline. (9) **glass CTA pill**: about 25 % white fill, thin white rim, lowercase label, growing arrow, held 1.15 s. (10) theme rhythm (luma 231 > 178 > 203 > 143-151 > 182; sat 0.01 > 0.30 > 0.17 > 0.38 > 0.28): white card, sky-blue globe, navy hero gradient (logo), white UI, near-black result, **same navy gradient for the CTA** (bookend). (11) hard cuts allowed when hidden by a white frame or 1-2 frame blur-out at a theme change, never mid-scene.

Palette: story card `#F7F7F7` with indigo-slate text about `#6574B7`; globe scene `#A9D6F6 > #E8F8FE`, globe `#5492DC`; **hero gradient** diagonal `#0B1794` top-left, mid `#2A4DB0 / #4B7BCE`, `#8DC5EE` bottom-right (highlights `#B8D9F7`); **action blue** `#0001E9` with white text on `#F7F7F7`; result scene `#010118` with `#020241` glow low-right, white `#F5F6FA` type; six comet colours each with white core; success green only on the check. Blue is the brand family; the dark scene is the only one with six hues.
Type (inferred): story text/wordmark in a light humanist sans (Segoe UI/Open Sans-like), centred; UI text/numbers in bold neo-grotesk (Inter/SF Pro-like); CTA lowercase medium. In the 880 px panel: story/UI text 4-6 % of panel height, hero number about 9 %; >= 40 px at 1920x1080, above Deepak's 24 px floor.
Audio (measured; music-led recipe b): -11.4 LUFS (louder than ours), LRA 1.8, TP +0.7 (clipped, don't copy); 81 % energy < 500 Hz, 0.6 % > 6 kHz: no glassy ticks, clicks or risers; one continuous pitched gliding lead over sub bed (looks like a trending music track). Visuals sit on low-band onsets within +-100 ms; track ducks about 10 dB for the CTA; no per-event SFX needed.
For Deepak: client SaaS/AI-tool Short or "how I animate this" showcase. Keep scene lengths 1.4-3.8 s, brand hold about 2.5 s, result number about 2.5 s, CTA about 1.2 s; **one** hero gradient for opening logo and CTA, one neon moment on the result scene, a new accent hue per video (`fonts-and-colours`). Over his footage, one-element-at-a-time (`mistakes-to-avoid` B2) wins.

## 9. Smooth-animation study (refs 70-74)
Five UI/UX promos, 60 fps: 70 AE tutorial "Spotify Glass Folder" (9:16, 88 s); 71 "Yonomi" editor promo (16:9, 16.8 s, 4 cuts at 4.02 / 9.25 / 13.78 / 15.02, each on a theme change); 72 app promo with one continuous 3D camera (15.1 s, 0 cuts); 73 Apple-Wallet concept (1:1, 10.35 s, 5 s sequence plays twice); 74 "Teamsonic.org" website promo (17.2 s, 1 cut at 16.37 to logo). (Klickpin file names are irrelevant.)

**Measured easing (t50 / t90 = share of time at which 50 / 90 % of distance is done; linear .50/.90):**
| Move | Duration | Curve | Numbers |
|---|---|---|---|
| dock rises from bottom edge (y 0.92 to 0.50) | 0.50 s | very strong ease-out (about out-quart) | t50 .17, t90 .83 |
| green circle wipe (0 to 91 % area) | 0.22 s | ease-out (about out-quad), 2.6 % overshoot | t50 .31, t90 .77 |
| card slides in from right (edge 0.99 to 0.78) | 0.57 s | ease-out, long soft tail | t50 .32, t90 .82 |
| pill to card morph (height 0.21 to 0.66) | rises 0.15 s to 0.75, settles by about 0.3 s | under-damped spring | **21 % overshoot, once** |
| full-frame white to black fade | 0.55 s | ease-in-out, late-weighted | t10 .18, t50 .61, t90 .88 |
| halo ring grows behind phone | 0.20 s | nearly linear, ends off-frame | 0.10-0.17 per frame |
Rules: (1) **no move is linear**; entrances are ease-out whose last 10 % takes 17-23 % of the time; only full-frame fades are ease-in-out. (2) **Overshoot only on a small-to-big morph** (about 20 %, once, back in 0.3 s); slides/wipes < 3 %. (3) **Duration ladder**: 0.15-0.22 s snaps (morph, wipe, halo), 0.5-0.6 s travel (rise, slide, fade through black), 1-1.2 s hold before the next beat. (4) Quick moves carry blur and bloom; long moves stay clean.

**Patterns:**
1. **Object chain**: one object carries the story (71: dot > ring+arrow > pill "Video Editor" > tall white card (overshoots) > star grows inside > cursor presses "Hire" > card tilts in 3D, 0-4 s no cut; 73: Wallet icon > Face ID brackets > card stack > map card; 74: Chrome icon > circle wipe > loader ring > "Team" pill > domain pill > laptop). Plan the chain before scenes.
2. **Conveyor, never an empty frame** (71, 9.8-13.4 s): each card enters from the right in the same move that pushes the previous out left; hold about 1 s, contents build while held.
3. **Type is motion**: letters blur in one by one, the line scales down and collapses to a dot that becomes the button (0.5-0.7 s); next phrase pushes the previous off-frame with a horizontal smear; a pill reveals its label left to right.
4. **Depth cues over effects**: 3D tilt, defocused far edge of a tilted card, rim-light glow on phone edge, soft shadow growing when an object lifts, three offset-colour stacked cards.
5. **Circle wipe from the thing you clicked** (0.22 s), concentric rings behind the logo, logo zooms past frame into the next colour; halo ring behind a new object = glow bloom.
6. **One continuous camera can replace cuts** (72: tumble, pull back to a turntable ring of phones, white bloom hides the change at 12 s). Hard cuts only at theme change (luma jumps 90 to 222, 175 to 103); the new scene moves in its first 0.2 s.
7. **Loop by design** (73 repeats with different data; 70 ends on the opening frame).
8. Guide lines as accent: green/yellow segments draw along the laptop frame, a green zigzag crosses the yellow wipe.
9. Cursor reaction within 3 frames of press (tilt, pop, ripple).
10. One accent per scene; scenes separated by theme so cuts are free.

Tutorial 70: the glass folder = Front + Back layers with **CC Light Sweep** (centre 256,128; direction -30 deg; shape Smooth; width 284; sweep intensity 10; edge intensity 47; edge thickness 3.9; light colour green; light reception Cutout), moved by null layers (Front null, Back null, "all control") with 3D rotation; album cards parented inside so they fan out. CapCut has no equivalent; transferable idea: glass body, moving light edge, controller object, emerging cards. Untested.

Audio of the five: 71 -13.7 LUFS, LRA 1.5, music-led flat, drops to -33 dBFS the second before the white cut and the beat returns on the cut; 72 -24.0 LUFS, quiet low thumps/swells, 23 % silent frames, gear-logo hold about 2 s near silence; 73 -28.8 LUFS single flat low bed, no hits; 74 essentially silent; 70 -20.6 LUFS, low hits every 0.17-0.2 s in the finished piece. No SFX kit to copy; section 5 stays the recipe. Confirmed: heavy low end, clean top; duck the bed about 1 s into a hard cut and re-enter on it; end on about 2 s near-silence under the logo.
For Deepak: define object chain and easing set up front; one accent per scene; hide hard cuts on theme changes; fonts from his list only. **On talking-head footage** the footage rules win: one graphic at a time (B2), no tilted cards (D10), no phone mock-up with his footage (D8); 3D tilts, turntables and full-colour scenes belong to full-screen promo scenes only.

## 10. Checklist
No linear moves (ease-out long tail; ease-in-out only on fades; overshoot <= 3 % except one 20 % small-to-big morph) / 0 hard cuts (ref 69 allows 2, hidden at a theme change) / blur on every move / one overshoot max / bloom on every landing / hover before click / holds 0.5-1.3 s / type-on with tracking collapse / one brand colour / logo bookends / riser, landing hit, settle tick on every screen change / one pop/chime sample reused, ticks -25..-35, hits -5..-7 / one bed strategy / master -14..-16 LUFS, -1 dBTP.

## 11. Talking-head product review adaptation (IKKO MindOne)
Every UI object explains one spoken fact and sits on/beside the real product: **tracked selection boxes** (Figma-style: 2.5-3 px accent stroke, white corner handles, mono tag; phone box vs dashed palm box); dimension line corner to corner for display size; spec pills on number words; AF viewfinder brackets for "this camera"; segmented toggle for two-state features (Back/Front) that morphs into the benefit pill; heads-up notification from the top edge growing extra rows; comment box to follow chip with cursor for CTA. Use the product's own screen colour as the one accent; keep his face clean on opinion lines. Levels with voice: bed 16-25 dB under speech RMS by section, UI cue gains -20 to -10 dBFS, one success sound with a tail. Notes: `client-video-editing-process` section 10.

## 12. Premium SaaS news show on a talking head (AI Tech News ep 02)
- **World**: midnight navy gradient `#071233 > #040918` with electric-blue top bloom and floor glow; faint 80 px grid only on chapter cards; glass cards (navy fill, 1 px light rim, inner top highlight, big soft shadow); white "ice" cards for documents/evidence; one accent `#2F6BFF / #5A8BFF`; red and green only inside data; yellow only as article marker.
- **Type**: Outfit 600-700 for titles/numbers, Inter 500-600 for UI/chips; letter type-on with tracking collapse for names; word-by-word blur-in for lines; accent word in light blue.
- **Devices**: search pill typing "Artificial Intelligence" with "Artificial" replaced by "Super" (hook); document card with hand-drawn signature + "Signed" chip; 12 agency tiles flipping AI to SI in a diagonal wave; glass profile grid ticking checks in a wave; pill-to-card morph (the one about 25 % overshoot); countdown ring; node trace (sources > model > MATCH > Fired); toggle switching live internet off; code window with bug row red then patched row green; bar boards (vendor chart, then independent index with rank badges); race lanes; poll card with cursor; satellite globe (pins only); keyed subscribe card; chapter key row (active key lights blue with bloom).
- **Rule**: a full-screen scene needs a visible change at least every **about 5 s** while he talks (counter, chip, highlight). Slow drifts and small colour changes don't read, and `freezedetect` flags them.

## 13. 3D product explainer without Blender (video 15 Mini LED Backlight)
Brief: copy a 3D explainer shot for shot, no text (macro LED dolly, dot field pulling back into a backlight panel, LCD slides out in front, airplane backlight with blue edge glow, LCD slides in, orbit, slice glitch, push-in on angled LED wall). Kit `edited videos by claude/15. Mini LED Backlight/code/render.py` (numpy + PIL + scipy only): pinhole `Cam`; `homog`/`warp` (PIL PERSPECTIVE, texture pre-shrunk to on-screen size so LED grids don't alias); `draw_panel` (front face, side/top edge for thickness, fading mirrored floor reflection, optional blurred edge glow); `draw_leds` (dome sprites resized per LED, squashed by view angle); bloom, soft highlight knee, vignette, grain. About 1-2.5 s per 1080x1920 frame over 12 workers. Shapes: Zapf Dingbats plane glyph (rotated 28 deg) and Apple dolphin emoji alpha; `distance_transform_edt` on the mask gives a lit 1-2-LED outline. Moves: one continuous camera grazing dot field to frontal to reveal; all LEDs on then dim to the outline (local dimming); LCD sliding along the panel normal; exploded 3/4 view; LED-wall camera about 35 deg off normal. **Gotcha**: imageio's ffmpeg is an Intel build under Rosetta (libx264 pipe about 1 fps); encode with `h264_videotoolbox -b:v 45M`.


Full original notes (every detail, uncut): `_archive/original-full/app-product-animation.md` in this folder.
