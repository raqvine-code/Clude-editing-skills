# Applying the style to new footage

A practical workflow, from raw clips to export. Use it to guide the editor step by step, or to produce the plan yourself when they give you a script or transcript.

Frames are at 25 fps. Sizes are for 1080x1920.

## Before you start: what to ask for

Ask only for what is missing.

| Need | Why | If it is missing |
|---|---|---|
| Script or transcript | everything is timed to words | ask for it; nothing else can start |
| Word timestamps | caption in-points | plan in words; the editor sets frames, or auto-captions provide them |
| Frame rate and length | frame maths | assume 25 or 30 fps and say which |
| Editing tool | the build steps differ | give tool-neutral steps |
| The list items | each needs a step scene | ask what the N things are |
| Proof assets | cards behind the head | plan placeholders and list what to capture |
| Brand colours | the accent family | use lime #D6FD00 on black and white |
| The call to action | the end card | ask; the video must end on it |

## Shooting notes, if the footage is not shot yet

These come from the reference footage. Suggested for new shoots.

- Vertical, 4K if possible, so punch-ins to 143% stay sharp.
- Wide lens, camera close and slightly above the desk, speaker centred, eyes about a third of the way down.
- Warm key light on the face. Room darker than the face, with one coloured practical light behind.
- A desk surface with a pattern, and one small prop per list item, laid out in a row.
- One physical object for the hook: a photo, a printout, the product.
- Leave the chest area clear of busy patterns. Captions sit there.
- Deliver each thought as its own take, with a clean pause before and after. The edit cuts on those pauses.

## The workflow

### Step 1. Clean the voice

1. Lay all takes in script order.
2. Cut every false start, breath and gap between phrases.
3. Leave a pause only where the script wants silence. The reel has almost none.
4. Lock the voice edit. Every later step depends on these timings.

### Step 2. Mark the sections

Label the timeline with the nine sections from `timing-sequencing.md`: hook, proof, reveal, stakes, promise, list, mistake and payoff, tool mention, end CTA.

Compare each section's length with its share. If the hook runs past about 4% of the runtime, tighten it first.

### Step 3. Set the framing

1. At each cut inside one take, alternate the framing: normal, then punched in to 127-143%, then back.
2. Put the punched-in piece on the payoff phrase.
3. Anchor every scale change on the face.
4. On takes longer than 2.5 s, add a slow push-in of about 2.5% per second.
5. On the hook, push in from 100% to 116% over the first 1.7 s, ease-out, then hold.

### Step 4. Choose keywords

Go through the script and mark at most one key phrase per sentence. Good keywords:

- a number or amount;
- a name: person, product, place;
- the outcome ("acquired", "missing out");
- the last content word before a cut.

Aim for about one every 5 seconds. Too many and none stands out.

### Step 5. Build the caption track

1. One beat per word, in-point on the frame the word starts.
2. Join a quick glue word to the next short word.
3. Turn each key phrase into a stack: lead-in, keyword, trailer.
4. Set font, size, position and shadow from the tokens. Check the position on the tightest and widest framings.
5. Remove captions under giant headlines and inside kinetic scenes.
6. No entrance animation. No coloured words.

With word timestamps and the script file available:

```
python3 scripts/caption_beats.py --words words.json --emphasis "acquired,seriously" --out beats.json --srt captions.srt
```

Mark keywords in a plain transcript with asterisks: `it was finally *acquired*`. Review the result by hand. The script chooses lead-ins and trailers mechanically.

### Step 6. Plan a picture for every noun

Make a list: the word, the asset, the scene type, the in-point.

| The word is | Use |
|---|---|
| a person | photo insert with name label, or a cut-out in a paper scene |
| a number | number build in captions, or a giant headline behind the head |
| an article, post or page | proof card behind the head with a highlighter swipe |
| an app or website | screenshot card behind the head, or a demo card on the white grid |
| a list item | step coin scene |
| a brand or tool | logo badge behind the shoulder plus a "like / NAME" stack |
| an abstract idea | icon badge beside the head |
| a list of three verbs or nouns | lime label swapping word by word, or a kinetic title |
| the call to action | white CTA card |

In-point: on the word, or up to 12 frames before it.

### Step 7. Place the full-screen scenes

1. Put each scene on a sentence boundary and let the voice run under it.
2. Keep each between 1.1 and 3.4 s.
3. Give every list item the same step scene, changing only the number and name.
4. Put the richest scenes in the first third.
5. Check that no A-roll run is longer than about 9 s.

### Step 8. Add transitions

1. Leave every cut as a hard cut.
2. Add a negative flash at two to four section changes.
3. Add a white flash going into or out of one or two bright scenes.
4. Remove any dissolve or preset transition.

### Step 9. Colour and look

1. Grade the A-roll warm on skin, dark and slightly green or olive in the room.
2. Add a strong vignette.
3. Use one accent family for every label, coin and title.
4. Blur and glow any text that sits behind the subject. Check the cut-out edge on hair and hands.

### Step 10. Sound

Follow `sound-design.md`. The short version: voice on top, music in for the proof and the last third, out for the serious claim, one short sound per graphic event, none on captions.

### Step 11. Check and export

Run the QC list in `GUIDE.md`. Watch once muted. Export 1080x1920 at the project frame rate.

## What to hand the editor

### Edit plan table

| # | In | Len | Scene | On screen | Transition in |
|---|---|---|---|---|---|
| 1 | 0.00 | 3.2 | A-roll hook | Speaker holds the product box. Tag "the story of a", giant "21 YO" behind the head, trailer "founder". Push-in to 116% | none |
| 2 | 3.20 | 2.4 | Photo insert | Founder photo, black and white, colour sweep, name label | hard cut |
| 3 | 5.60 | 2.0 | A-roll | Article card behind the head, highlighter on the revenue line | hard cut |
| 4 | 7.60 | 1.0 | A-roll, punched in 139% | Stack: "it was / finally / launched" | hard cut |
| 5 | 8.60 | 2.8 | Paper reveal | Cut-out, three red title lines | hard cut |
| 6 | 11.40 | 1.4 | A-roll | Captions | white flash |

### Caption track

| In | Out | Type | Text |
|---|---|---|---|
| 57 | 59 | pop | This |
| 59 | 63 | pop | will |
| 63 | 69 | pop | change |
| 69 | 86 | pop | your week. |
| 118 | 151 | stack | lead "you're" at 118, key "seriously" at 121 (1.30x), trail "missing out." at 130 |

### Graphics list

| Asset | Lands on | In | Animation | Length |
|---|---|---|---|---|
| Giant "21 YO" | "twenty-one" | frame 22 | pop behind subject | to cut |
| Article card | "article" | 6.2 s | rise 8 frames, highlighter at +12 | 1.7 s |
| Step coin 1 | "first" | 33.4 s | flip 12 frames | 2.0 s |
| Lime label | "plan, build and ship" | 36.1 s | word swap | 1.9 s |
| CTA card | "link" | 82.2 s | caption build | 2.2 s |

## Tool notes

Give steps in the editor's tool. Keep them numbered and plain. Do not assume menu names you are not sure of; describe the action and let the editor find the control.

### After Effects

See `after-effects-recipes.md` for settings and expressions. In short:

- one composition per full-screen scene, nested into the main edit;
- captions as text layers trimmed to their beats, or one text layer with hold keyframes on Source Text;
- flashes as one-frame adjustment layers under the caption layers;
- behind-subject text between the footage and a rotoscoped copy of it.

### Timeline editors (Premiere Pro, DaVinci Resolve, CapCut, Final Cut)

- Cut and punch-in on the timeline with the clip's scale and position.
- Auto-captions can produce the one-word beats. Set them to one word per caption, no animation, then restyle.
- Build stacks by hand as separate text clips. Auto-captions cannot make them.
- For behind-subject text, duplicate the clip, remove the background on the top copy, and put the text between the two.
- For a negative flash, put a one-frame adjustment clip with invert and zero saturation on the last frame, then a one-frame black clip.

### Code-based tools (HyperFrames, Remotion)

- Start from the values in `assets/style-tokens.json` and the structure of `assets/style-template.html`.
- Follow that tool's own skill and documentation for how compositions are written and rendered. This skill supplies the look, not the framework rules.
- These tools suit the full-screen scenes and the caption track best. Cutting the speaker's footage is usually easier in a timeline editor.
- When the editor works through a coding agent and prefers not to handle code, give them a ready-to-paste request for that agent that names the scene, its length, and every value from the tokens.

## Adapting the style

| Situation | What to do |
|---|---|
| No props on the desk | Keep the step scene; it carries the count on its own |
| No way to cut out the speaker | Put giant headlines in the space above the head instead of behind it. Never put them over the face |
| A different brand colour | Replace lime with the brand's brightest colour, text black or white for contrast. Keep everything else |
| Not a list video | Keep hook, proof, reveal, stakes and CTA. Replace the list with three beats of story, each opened by one full-screen scene |
| 30 fps project | Multiply frame counts by 1.2. Flashes stay 2 frames |
| A language with long words | Lower the keyword scale so no line passes 765 px. Keep one word per beat |
| A script without numbers or names | Use outcomes and verbs as keywords, and icon badges for ideas |
| Very short video, under 20 s | Hook, one proof card, one full-screen scene, CTA. One negative flash at most |

## What not to carry over

The style is how the reel is cut. The content belongs to its creator. Do not reuse the reference reel's footage, the people in it, its script, its on-screen screenshots or its sponsor's branding. Use the editor's own footage, proof and call to action.
