# Animation and motion graphics

How every moving element enters, moves and leaves, with frame timings from the reference reel. Frames are at 25 fps. At 30 fps multiply by 1.2.

Labels: Measured, Approx, Suggested.

## Principles

1. **The word is the trigger.** An element appears on the word that names it, or up to half a second before. Never after. Measured.
2. **Fast in, no out.** Entrances take 0 to 12 frames. Almost nothing animates out: elements are replaced, or the shot cuts away. Measured.
3. **Pop first, ease second.** Text pops with no animation. Objects (cards, badges, coins) get a short eased entrance. Measured.
4. **Build in pieces.** Headlines, labels and lists arrive word by word or item by item, 2 to 6 frames apart, in the order they are spoken. Measured.
5. **Depth from layering, not 3D.** Cards and headlines go behind the cut-out speaker; labels, badges and captions go in front. Measured.
6. **One idea per scene.** A graphic scene shows one object and at most four display words. Measured.
7. **Real props, mirrored digitally.** The five chips on the desk and the five coins in the graphic are the same list. The viewer always knows which step they are on. Measured.

## Entrance table

| Element | Entrance | Frames | Label |
|---|---|---|---|
| Caption beat | hard pop | 0 | Measured |
| Display word in a headline | hard pop, word by word | 0 each, 3-10 apart | Measured |
| Tag text beside a headline | types on word by word | 4-5 between words | Measured |
| Name label on a photo | types on letter by letter | 1-2 per letter | Measured |
| Screenshot card behind the head | slides in from the left with motion blur | 4 | Measured |
| Article card behind the head | rises about 60 px while fading in | 8 | Measured |
| Highlighter on a phrase | swipes left to right | 4 | Measured |
| Icon badge | scales up from about 30% with a spin and a glow | 6 | Measured |
| Logo badge behind the shoulder | fades and scales in | 5 | Measured |
| Prop numerals | pop one by one, right to left | 2-4 apart | Measured |
| Step coin | flips from the row to the centre | 12 | Measured |
| Lime label word | hard swap | 0 | Measured |
| Kinetic title word | hard pop | 6 apart | Measured |
| Paper title line | fades in | 4-5 each, 3-6 apart | Measured |
| Cut-out head | pops big and settles (overshoot) | 7 | Measured |
| Photo | defocus to sharp | 3 | Measured |
| Colour sweep on a photo | band moves bottom to top | 12 | Measured |

## Scene recipes

Each recipe lists layers from back to front, then the timeline. Frame 0 is the first frame of the scene.

### 1. Hook with headline behind the subject

Layers: footage; small tag; giant headline; small trailer; cut-out copy of the speaker; thin curved arrow; captions.

| Frame | Event |
|---|---|
| 0 | Shot starts. Scale begins 100% to 116%, ease-out |
| 2, 6, 11, 15 | Tag types on, one word each |
| 22 | First giant word or number pops, left of the head |
| 36 | Second giant word pops, right of the head |
| 39 | Trailer word pops, bottom right |
| 43 | Push-in ends, hold at 116% |
| 57 | First caption beat. Headline stays |
| 40-78 | Thin curved arrow draws from the headline to the object in the speaker's hand (exact start frame not confirmed) |
| 86 | Cut |

Headline block: x 91-956, y 368-830. Blur 2-4 px plus a soft white glow. The speaker holds a physical object that the headline is about.

### 2. Counting headline

Layers: footage; numbers; small words; cut-out speaker.

| Frame | Event |
|---|---|
| 9 | First number pops, top left |
| 18 | Second number pops beside it |
| 28 | Third number pops |
| 34 | Small word under the first number |
| 39 | Small word under the last number |
| 48 | Cut |

The speaker does one physical action per count. No captions during the count.

### 3. Proof cards behind the head

Layers: footage; card; cut-out speaker; side label; curved arrow; captions.

| Property | Value |
|---|---|
| Card slot | x 76-616, y 132-900, corner radius about 16 px, soft shadow |
| Card content | a real screenshot: a page, an app screen, a game |
| Entrance | slide in from the left, 4 frames, motion blur |
| Swap rhythm | 12, 14, 14, 24 frames between cards |
| Side label | display caps, top right, counts up with each card |
| Arrow | thin white hand-drawn curve from the label to the card |
| Teaser card | the last card is blurred and its label ends in "??" |

The big article card variant fills x 94-971, y 97-974, rises over 8 frames, and gets a yellow highlighter swipe (#F8E202, 4 frames) on its key phrase about 12 frames after it lands.

### 4. Icon badges

Layers: footage; badges; captions.

| Property | Value |
|---|---|
| Badge | white circle, 183 px, dark simple icon, soft white glow ring |
| Slots | left of head (x 83-266, y 479-652), above head (x 397-580, y 126-299), right of head (x 819-1002, y 400-575) |
| Entrance | scale from about 30% with a quarter-turn spin, 6 frames |
| Timing | one badge per keyword, 0.7 to 1.3 s apart |
| Exit | all stay until the shot ends |

The orbit variant, used in the paper scene: four black badges ride a thin ring around a cut-out head and rotate about a quarter turn in one second.

### 5. Photo insert

Layers: photo; black-and-white grade; colour sweep matte; name label; pointer line; icon badge; captions.

| Frame | Event |
|---|---|
| 0-2 | Photo goes from blurred to sharp |
| 13 | Whole photo turns black and white and darkens slightly |
| 14-26 | A purple band sweeps bottom to top over the main person, leaving them in colour |
| 16-21 | Name label types on above the person; a thin pointer line draws to them |
| 32 | Snap zoom to a closer crop, one frame of motion blur |
| 47 | Icon badge pops beside the caption, tied to it by a thin line |
| 63 | Cut |

Use this for any third-party photo: it makes a flat image feel edited, and it points at the one person who matters.

### 6. Step coin

Layers: near-black background with a purple glow at the left and a blue glow at the right; two outlined neon hands; a row of numbered coins; the hero coin.

| Property | Value |
|---|---|
| Background | #040309, glows #641C97 (left) and #0A2666 (right) |
| Coins | purple #7709BA with a lighter top-left and darker rim, white bold number |
| Row | five coins, evenly spaced, in the lower half |
| Hero coin | about 313 px across, centre at about 41% of height |
| Flip | the current coin leaves the row, flips two or three times as it rises, lands face-on with its name; 12 frames |
| Done coins | sit small and labelled at the left of the row |
| Hold | 16 to 38 frames after landing |
| Extra | one white flash frame right after the scene starts, first time only |

Timeline, first use: frame 0 row visible; frame 2 white flash; frames 3-15 flip; frames 15-50 hold. Later uses are shorter: 28 to 53 frames in total.

Reuse the same scene for every list item. Only the number and the name change. Swap coins for any object that fits the topic, and keep the count visible.

### 7. Demo card on white grid with lime label

Layers: white background; faint grid; screen recording in a rounded card with shadow; lime label; optional small captions.

| Property | Value |
|---|---|
| Background | #FDFDFD |
| Grid | 1 px lines, #E0E0E0, cells 113x91 px, fading out toward the edges |
| Card | 904 px wide (x 88-992), corners about 14 px, shadow about 22 px down and soft |
| Label | black display caps on #D6FD00, box about 168 px tall, centred at y 1490 |
| Label rhythm | one word at a time, swapped on the spoken word: 10, 12, 6, 20 frames |
| Card content | changes with each label word |

The label keeps the comma of a spoken list ("WORD,") and gives the joining word its own beat ("AND").

Without a label, the card can carry small white captions over its bottom edge, or black captions under it.

### 8. Kinetic title

Layers: black; lime words.

| Frame | Event |
|---|---|
| 0 | Word 1 pops, line 1, left |
| 6 | Word 2 pops, completing line 1 |
| 12 | Small "and" in the caption font, lime, between the lines |
| 18 | Line 2 pops |
| 30 | Cut |

Cap height 166 px. Block x 154-944, y 667-1088. Nothing moves once it has appeared.

### 9. Paper reveal

Layers: warm paper with grain and a heavy dark vignette; red title lines; cut-out head; captions.

| Frame | Event |
|---|---|
| 0-7 | Cut-out head pops in oversized and settles |
| 8 | Title line 1 fades in behind the head, 4 frames |
| 11 | Title line 2 fades in |
| 17 | Title line 3 fades in |
| 41 | Title clears. Orbit ring with four badges appears and turns |
| 68-69 | White flash out |

Paper: centre #E8E2D7, edges #CEC8BD, corners #67625D. Title red #D92029. The title lines are different widths; they are not justified.

### 10. Paper kinetic ("the threat")

Layers: paper; dots; ball; two-line charcoal headline; debris.

| Frame | Event |
|---|---|
| 0-20 | Six dark dots drift in from the edges, growing |
| 20-24 | Dots rush to the centre and merge into one ball with a short label |
| 26-34 | A grey ring pulses out from the ball |
| 37-44 | Ball rises to the upper third |
| 40 | Two-line headline pops under it |
| 49-58 | A second ring pulse |
| 58-60 | Ball drops through the headline |
| 59-80 | The right half of the letters breaks into small shards that scatter and fall |

Ball about 190 px, #434343. Headline #323230, block x 342-737, y 760-1158. This is the most complex scene in the reel and the only one with particles. Treat it as the single "hero" graphic of a video.

### 11. CTA card

Layers: white; QR code or handle; black captions.

| Property | Value |
|---|---|
| Background | #FDFDFD, nothing else |
| QR | 517 px square, x 281-798, y 600-1117 |
| Caption | black, 62 px, y 1250-1366, builds phrase by phrase |
| Final state | two lines: small first line, bigger second line |
| Uses | once mid-roll at about 60% of the runtime, once as the last shot |

The mid-roll card builds its line across 2.7 s: three short phrases, then the instruction. The end card builds two stacks in 2.2 s.

## Camera moves on A-roll

| Move | Value | Label |
|---|---|---|
| Hook push-in | 100% to 116% in 43 frames, ease-out, then hold | Measured |
| Slow push-in | 1.2 to 3.6% per second, linear, for the whole take | Measured |
| Static | several takes under 1.5 s do not move | Measured |
| Punch-in at a jump cut | 127%, 139%, 143% | Measured |
| Punch-out at a jump cut | back to 77-79% of the punched size | Measured |
| Anchor for all scaling | the face, about x 50%, y 36% | Measured |

Never animate a zoom between two framings. The change of size happens on the cut.

## Building these in a code-based tool

`assets/style-template.html` implements recipes 1, 3, 4, 6, 7, 8, 9 and 11 in simplified form, with a frame-accurate timeline and placeholder content. Every element carries `data-in` and `data-out` frame numbers.

For HyperFrames or Remotion, do not copy the template's small timeline engine. Use that tool's own composition rules and its own skill or documentation, and carry over only the values: sizes, positions, colours, frame offsets and layer order.
