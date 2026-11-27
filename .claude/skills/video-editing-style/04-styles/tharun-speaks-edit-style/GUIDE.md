---
name: "tharun-speaks-edit-style"
description: "Use when editing, captioning or planning a vertical talking-head reel in the Tharun Speaks style - word-pop captions, behind-subject headlines, punch-in cuts, lime labels, flash transitions."
---

> **Scope: style reference. Measured from another creator's reels (Tharun Speaks). Borrow the grammar; never reuse the creator's footage, face or branding.**

# Tharun Speaks edit style

A reverse-engineered editing style for 9:16 talking-head reels: an educational or story-led creator speaking to camera, cut fast, with word-by-word captions and short motion-graphic scenes that illustrate every noun.

Use this skill when the editor asks to edit, caption, plan, storyboard, review or build graphics for a reel "in the Tharun Speaks style", or shares this skill's name. The job is to apply the style to the editor's own footage and script. Never reuse the reference creator's footage, face, script or sponsor branding.

## Where the rules come from

The rules were measured frame by frame from two reference reels by the same creator, both 1080x1920 at 25 fps, and checked against 25 screenshots. Reel A: 84.6 s, 36 shots, purple and lime. Reel B: 88.6 s, 31 shots, navy and neon green. Both are five-step list videos. Numbers with no reel named come from reel A. Where reel B differs, the difference is stated.

Read every rule with its label:

- **Measured**: read off the frames or the audio signal. Trust it.
- **Approx**: matched by eye or by fitting. Tune by eye.
- **Suggested**: standard practice for this genre that fits the style but was not confirmed in the reel.

Known limits. Say these to the editor when they matter:

- The audio was analysed as a signal, never heard. Loudness, bass and tempo are measured. Individual sound effects are not identified.
- Fonts are the closest free matches, not confirmed originals.
- Two reels are a small sample. Where they agree, treat the rule as the style. Where they differ, treat it as a choice to make per video.

All pixel values are for a 1080-wide frame. All frame counts are at 25 fps. At 30 fps multiply frames by 1.2.

## The style in twelve rules

1. **Voice leads everything.** Cuts, captions and graphics land on spoken words. Cuts do not follow the music beat. Measured.
2. **One caption line, mid-frame.** White, bold, sentence case, centred at 68% of frame height in reel A and 55% in reel B. No box, no outline. Measured.
3. **Captions hard-pop.** Each beat appears at final size on the frame its word is spoken and is replaced by the next. No fade, slide, bounce or typewriter. Median beat 6 frames (0.24 s). Measured.
4. **Emphasis is size first.** A key phrase becomes a stack: small lead-in at top left, big keyword, small trailer at bottom right. It holds 0.5 to 1.3 s. Reel B also tints a few key words: the word fades in orange or blue, then settles to white over about 8 frames. Measured.
5. **Big headlines sit behind the speaker.** Condensed all-caps type goes between the background and the cut-out subject, in the top third, slightly blurred and glowing. Measured.
6. **Every noun gets a picture.** A card, icon badge, label, logo or number appears on the word that names it, or up to about half a second before it. Never after. Measured.
7. **Jump cuts change size.** At a cut inside the same take, scale jumps to 127-143% (or back), anchored on the face. Long takes get a slow push-in of 1.2-3.6% per second. Measured.
8. **Short graphic scenes break up the talking.** Full-screen motion graphics last 1.1 to 3.4 s and take about a third of the runtime. Measured.
9. **Hard cuts by default, three accents.** A 2-frame negative flash, a 1-2 frame white flash and, in reel B, a 3-4 frame blur-zoom into or out of a graphic scene. No dissolves or wipes. Measured.
10. **One accent family per video.** Reel A uses lime on black or white plus purple. Reel B uses navy with a warm spotlight, neon green and yellow numerals. The type system never changes. Measured.
11. **Pace: a cut about every 2 s, a caption change about every 0.25 s.** 36 shots in 84.6 s, median 2.0 s, shortest 0.56 s, longest 8.48 s. The longest shot stays alive with five card swaps and a row of numerals in its first 4.5 s. Measured.
12. **Open hard, end on the ask.** First cut at 3.44 s. The call-to-action card is the last shot in reel A and the second-last in reel B, which adds one 1.3 s closing line to camera. No intro, no outro, no logo sting. Measured.

## Design tokens

| Thing | Value | Label |
|---|---|---|
| Canvas | 1080x1920, 25 fps | Measured |
| Caption font | Inter Tight Bold, 116 px, tracking -2.5%, line height 0.86 | Approx (width fit within 1-2%) |
| Caption fill | #FFFFFF on footage, #000000 on white cards | Measured |
| Caption shadow | soft black, about 5 px down, 12 px blur at 80% plus 34 px blur at 50% | Approx |
| Caption position | centre x 540, centre y 1304 (67.9%) | Measured |
| Lead-in and trailer size | 0.72x of regular (range 0.70-0.80) | Measured |
| Keyword size | 1.75x up to 5 letters, 1.45x for 6-8, 1.30x for 9 or more; never wider than 765 px | Measured |
| Caption on white card | black, 62 px, no shadow, second line bigger | Measured |
| Caption over a full-screen demo | white, about 48 px | Approx |
| Display font | Bebas Neue, ALL CAPS, width 80%, tracking -2% (Anton at 83% for giant numerals) | Approx |
| Lime | #D6FD00 with black text | Measured |
| White card | #FDFDFD, grid lines #E0E0E0, cells 113x91 px, fading at the edges | Measured |
| Paper scene | centre #E8E2D7, edge #CEC8BD, corners #67625D, red type #D92029, charcoal type #323230 | Measured |
| Step coin | purple #7709BA (light #940CE4, dark #64079F) on #040309 with purple-left and blue-right glows | Measured |
| Highlighter | #F8E202 | Measured |

If the caption sits on the speaker's mouth or hands, move it within the chest zone, 50% to 68% of height, then keep that value for the whole video. Reel B sits at 55% (centre y 1062) with a smaller caption, about 85 px, because the speaker is framed tighter.

## Captions

- **Beat size:** one word. Join a quick glue word to the next word when the pair is short: "he built", "in the", "a link". Keep acronyms, names and numbers on their own beat.
- **Text:** sentence case, exactly as spoken, punctuation kept ("late,", "your mind.").
- **Stack layout:** reserve the whole stack's space from its first word. The lead-in appears small in its final place, then the keyword pops under it, then the trailer. Nothing moves.
- **Stack variants:** two lines (lead-in over keyword); three lines; a number build where a small unit sits to the right of a big number and a small line goes under it.
- **Where stacks go:** the last phrase of a sentence, usually right before a cut or right after a punch-in. About one stack every 4 to 6 s.
- **When captions leave:** during full-screen kinetic scenes and while a giant headline is on screen. They stay through flash frames, except the single black frame.
- **Timing:** in-point is the frame the word starts. Typical beat 4-10 frames, fastest 2. Stack hold 12-33 frames.

If `scripts/caption_beats.py` is present, run it on word timestamps to produce the beats, then review the keywords by hand.

## Scene types

| Scene | What it is | Length |
|---|---|---|
| A-roll | Speaker to camera, wide lens, warm key light, olive background, dark vignette, desk in the lower third with props | 0.6-8.5 s |
| Behind-subject headline | Small tag, giant caps or numerals, small trailer, built word by word behind the head | 1.2-2.5 s inside A-roll |
| Proof card | Screenshot or article card behind the head, slides in over 4 frames; label plus thin curved arrow in front | 0.5-2 s each |
| Icon badges | White circles, 183 px, with glow; spin-pop over 6 frames around the head, one per keyword | stay to shot end |
| Photo insert | Photo defocuses in over 3 frames, turns black and white, colour sweeps back onto the person, name label types on | 2.5 s |
| Step coin | Row of numbered coins; the current step flips to the centre in 12 frames and shows its name | 1.1-2.1 s |
| Demo card | Screen recording in a rounded card with shadow on the white grid; lime label below swaps word by word | 1.9-3.4 s |
| Kinetic title | Lime caps on black, one word every 6 frames, small "and" between lines | 1.2 s |
| Paper reveal | Paper texture with heavy vignette; cut-out pops with overshoot; red caps fade in behind it line by line | 2.8-3.2 s |
| CTA card | White card, QR or handle, black caption building phrase by phrase | 2.2-2.7 s |

## Reel B additions

All measured on reel B. Use them when they suit the video.

- **Counting numbers:** a number runs up to its final value over 20-30 frames, fast first and slow at the end, then holds. Seen as a currency amount over a prop, a percentage behind the head and a "500+" on the chest.
- **Gradient numerals:** giant condensed numerals behind the head, white fading to yellow #FDE944.
- **Glowing props:** two objects on the desk relit green and red, each with a floating value label in its colour (#D4FD2D for green). The hook cuts to a macro of each.
- **Spotlight step scene:** navy room (#11315C), warm spotlight, a paper flies up from a pile and shows "STEP n" and its title. Earlier steps stay as small papers. 1.8-2.5 s. It does the job of the step coin.
- **Glass cards:** one translucent UI card per idea on near-black navy, captions above it at 28% of height.
- **Flow diagram:** grey background, white line icons, thin connectors. The camera travels stage to stage without a cut. 7.0 s, the longest graphic scene in either reel.
- **Recap card:** a light card on navy whose lines type on one by one as they are spoken. 5.2 s.
- **Icon strip:** a band of round icons slides across under the caption to preview the steps.
- **List captions:** a spoken list stacks at the left edge (x 60-400), one line per item, with a thin blue streak beside it.
- **Pacing:** 31 shots, median 2.44 s. A-roll 48%, graphics 52%. The list starts at 12% of the runtime, with no separate proof or reveal section.

## Transitions and camera

- **Hard cut:** 30 of the 35 cuts in reel A.
- **Blur-zoom (reel B):** 3-4 frames of heavy zoom or directional blur across a cut, into or out of a graphic scene or a tight punch-in. At least 4 uses.
- **Negative flash:** last outgoing frame inverted and desaturated, then one black frame, then the new shot. Captions are not inverted. Used 3 times: twice at section changes, once mid-sentence for a jolt.
- **White flash:** one blown-out frame, then one white frame. Used twice in reel A and about 6 times in reel B, mostly on the way out of a graphic scene.
- **Punch-in at a jump cut:** 127%, 139% and 143% measured; return cuts go back out. Anchor at about x 50%, y 36%.
- **Hook push-in:** 100% to 116% over 43 frames, ease-out, then hold.
- **Slow push-in:** 1.2-3.6% per second, linear, on takes longer than about 2.5 s.

## Timing and structure

Reference reel map. Scale the proportions to the new length:

| Time | Share | Section |
|---|---|---|
| 0.0-3.4 s | 4% | Hook: promise plus a curiosity object, giant headline behind the head |
| 3.4-11.6 s | 10% | Proof: who, what, the big number, how fast |
| 11.6-14.4 s | 3% | Reveal scene |
| 14.4-24.9 s | 12% | Stakes: why the viewer should care, ending on a kinetic scene |
| 24.9-33.4 s | 10% | The promise: "here are the N things, in order", with previews |
| 33.4-64.7 s | 37% | The list: each step is a coin scene, then A-roll or demo cards |
| 50.0-52.7 s | | Mid-roll CTA card, after step 3 of 5 |
| 64.7-76.2 s | 14% | Common mistake, then the payoff |
| 76.2-82.2 s | 7% | Tool mention and closing claim |
| 82.2-84.4 s | 3% | End CTA card |

A-roll is 64% of the runtime. Graphics and inserts are 36%.

## Sound

- Measured: very loud, voice-forward master (-9.4 LUFS integrated, 2.4 LU range, peaks over 0 dBFS). A bass-heavy bed runs under the story section. No bass bed through the middle. A kick-driven track at about 129 BPM runs from the fourth step to the end.
- Measured: low hits land on a label reveal, a card rise and the mid-roll CTA cut.
- Suggested: aim for -10 to -12 LUFS with peaks under -1 dBFS; whoosh on card slides, soft pop on badges, impact on slams, shutter click on flashes. Tell the editor these are suggestions.

## How to apply the style to new footage

Work in this order. Give the editor numbered, plain-language steps for their own tool.

1. **Get the words.** Ask for the script or a transcript with word timestamps. Without timestamps, plan in words and let the editor set frames.
2. **Mark the structure.** Label hook, proof, reveal, stakes, promise, list steps, mistake, payoff, CTA. Flag missing parts.
3. **Cut the A-roll to the voice.** Remove breaths and gaps. At each cut inside a take, alternate normal and punched-in framing. Add slow push-ins to long takes.
4. **Pick keywords.** One stack per sentence at most. Prefer numbers, names, outcomes and the last word before a cut.
5. **Build the caption track.** One beat per word, hard pops, stacks for keywords.
6. **List every noun.** For each, choose a card, badge, label, logo or number and note the word it lands on.
7. **Place graphic scenes.** One full-screen scene every 4 to 8 s of talking, never more than about 9 s apart, 1.1-3.4 s each. Give every list item its step scene.
8. **Add the two flash transitions.** Negative flash at 2 to 4 section changes. White flash in or out of 1 or 2 graphic scenes. Everything else is a hard cut.
9. **Choose one accent family** and use it for every label, coin and kinetic title.
10. **Finish:** grade warm with a vignette, add sound, end on the CTA card.

### What to hand back

When asked to plan an edit, return:

- an **edit plan table**: number, in time, length, scene type, what is on screen, transition in;
- a **caption track**: beats with in and out frames, stacks marked with lead, key, trail;
- a **graphics list**: asset, the word it lands on, in frame, animation, duration;
- **build steps** for the editor's tool.

When asked to review an edit, check it against the twelve rules and the QC list, and report the misses with timestamps.

## QC list

- Any caption beat with more than 3 words, or two lines that are not a stack?
- Any caption sliding, bouncing or typing in? A colour-to-white fade on a key word is the only allowed animation.
- Any stretch over 2.5 s with no cut, overlay or scale change?
- Any dissolve or wipe?
- Headline text in front of the face instead of behind the subject?
- More than one accent family?
- Captions covering the mouth, or inside the bottom 15% of the frame?
- Is the CTA card the last or second-last shot?

## Extra files

Everything needed is in this file. If the skill folder also holds these, read them when the task calls for it:

- `references/style-analysis.md`: the evidence, the full 36-shot log, how each number was measured.
- `references/second-reel-analysis.md`: reel B in full: shot map, new devices, differences from reel A.
- `references/captions-typography.md`: caption and display type in full detail.
- `references/motion-graphics.md`: build recipe and frame timings for every scene type.
- `references/transitions-effects.md`: cuts, flashes, punch-ins, grade and looks.
- `references/timing-sequencing.md`: pacing numbers and the section template.
- `references/sound-design.md`: measured audio and the suggested effects map.
- `references/workflow-new-footage.md`: the step-by-step process with worked examples.
- `references/after-effects-recipes.md`: settings and paste-ready expressions.
- `assets/style-tokens.json`: every value as data.
- `assets/style-template.html`: a working 18 s demo of every building block with placeholder content. Open it in a browser. For HyperFrames or Remotion builds, port its values under that tool's own rules.
- `assets/boards/`: reference boards rendered from the template.
- `assets/fonts/`: Inter Tight, Bebas Neue and Anton with their open licences.
- `scripts/caption_beats.py`: turns word timestamps into caption beats.