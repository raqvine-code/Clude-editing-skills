# Prompt patterns

What the prompts behind the 242 entries look like, what each pattern tends to produce, and a fill-in template for the structured pattern. All prompts are in `data/entries-all-242.json`; the 33 picks are verbatim in `picks.md`. Entry numbers are rows of `data/entries-all-242.csv`.

## What people actually wrote [measured on the 237 entries that have a prompt]

- Median length 151 characters; 142 of 237 are 160 characters or fewer; 20 are over 1,000 characters.
- **28 entries use the same showreel prompt** ("make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."), identical apart from capitalisation and a final full stop. 41 start with it; 85 mention "showreel".
- 12 entries use the structured `<inputs>` template (26, 60, 157, 158, 182, 183, 225, 226, 227, 228, 229, 230). Entries 60 and 226 share one prompt, so these act as shared templates.
- 23 prompts are not in English (Chinese, Japanese, French and others; the site supplies translations); 4 of the picks (32, 59, 154, 173) are in Chinese.
- 5 entries are skills (an install command and no prompt): 100 and four others. None are picks.
- Of the 33 picks, 20 have prompts of 160 characters or fewer and 5 are over 1,000.

## The five patterns

### 1. Open brief: hand over the concept
Examples: "make a 20-second video about anything, your call; make it crazy." [28] · "make a 4-minute animated short that blows my mind." [68] · "Make a 45-second silent short film with no dialogue, where sound tells half the story. Invent the story." [109] · "Create me a motion video of your choice, with the sole purpose of flexing Opus 5.5 capabilities." [82] · "Make a 90-second animated short film about a bug that doesn't want to be fixed." [111].
**What I observed:** the strongest concept-driven pieces (M1, M2) came from this pattern, and the prompts are 50-105 characters. Give only length, one emotional or sensory constraint ("silent", "crazy") and, if you want, a topic. Do not over-specify.

### 2. Showreel one-liner plus one decisive twist
The base prompt is generic; the entries that stood out added a single constraint:
- a subject: "related to mathematics" [142]; "about the cycle of life... to the 9-5 cycle... elder life and death, then cutting ready to loop" [130]; "exploring the concept of “Overthinking,” inspired by the attached graphics" [77]
- a brand: "...like it's your showreel for a flowdrive" [139]; "it should be a launch saas video for https://dub.co" [202]; "...what an incredible media intelligent Drone Emprit is" [95]
- a medium or mood: "psychedelic and hypnotic" [151]; "use only code" [107]
- a method note: "dont ask just make" [124]
**Without a twist** the outputs converge (corner furniture, cream or black with primary accents, serif plus grotesk).
Two entries (by different creators, identical wording) add an explicit exclusion: "Avoid the frames and texts on the corners which are typical ai made giveaways!" [4, 199].

### 3. One sentence that states a rule
"A video explaining recursion, where every explanation about recursion has a radically different video style, make this self-referential & clever & fast moving." [63] · "create a motion design video of a poster breaking out of its own frame." [161] · "4 seasons passing outside a train window, a cozy carriage, a cup of coffee on the table, Grand Budapest Hotel style" [97] · "Cut a raw talking-head clip into a punchy, fun edit with subtitles, graphics and music" [187].
A good rule is visual, testable and self-contained (the poster must leave its frame). It gives the model something to build the whole piece around.

### 4. Name the medium
"make about my studio with Risograph style" [177] · "Make Motiongraphic about my studio with Oscilloscope style" [178]. Same subject, two looks: the cheapest way to get a distinctive piece, because the medium implies palette, texture, motion and typography. Entries 177 and 178 are worth comparing side by side.

### 5. Brief with references or assets
- A reference video attached plus a research and rules list [125]: study the brand's earlier designs, find assets, "Study the reference closely: smoothness, timing, shot durations, fonts, elements", "Take some inspiration and borrow techniques, but change the design overall", "Every morph has to be perfect", "Feel free to work 10+ hours".
- Music attached: "based on the attached music, perfectly syncing the lyrics and animation to the vocals and beat" [191].
- Real footage: a raw clip to cut [187]; hand-drawn input images to use "as much as possible" [7].
- Audio direction in words: "Use the Oppenheimer theme music as inspiration, but compose it yourself" [14].
- Tooling note: "Please do not reference any previous memories or skills" [156], which tells you that piece came from the base model with no skill.

## The structured production prompt

Twelve entries use the same skeleton, and its picks (183, 225, 226, 227, 229, 230, 182, 228) are among the most polished work in the collection. Sections, in order:

| Section | What it does |
|---|---|
| `<inputs>` | "Ask me for: ..." the things only the user can supply (brand name, photos, a track around 120 BPM, one accent colour), plus defaults if they skip any. Makes the prompt reusable. |
| `<direction>` | The look in 5-8 sentences: length, aspect and fps, canvas and accent colours, fonts, the one governing idea (one continuous take, one shape that morphs), camera rule, cursor rule, loop rule. Ends with a **Banned:** list. |
| `<structure>` | The film beat by beat. Often tied to a tempo ("120 BPM, 54 beats, something happens on every beat"). Each beat says what physically transforms into what. |
| `<build>` | A numbered engineering recipe: `seek(t)` architecture, closed-form springs, camera, audio analysis, Playwright render with subframes, a frame-per-beat check. See `techniques.md` section 1. |
| `<gotchas>` | Failure modes the author already hit. This is where hard-won knowledge lives. |
| `<start>` | "Ask me for the inputs, then show me the beat map and four stills before building the full video." A review gate before the expensive render. |

### Fill-in template (my synthesis of 183, 226 and 230; text in brackets is mine)

```text
<inputs>
Ask me for: [3-6 things the film needs: the copy, one accent colour, brand mark, photos or clips, a royalty-free track around 120 BPM]. If I skip anything, use [defaults].
</inputs>

<direction>
A [N]-second [2D | 3D] [film type] in [16:9 | 1:1 | 9:16] at [60]fps. [The one governing idea, e.g. "one shape that never cuts" / "one dot links every scene"]. [Canvas colour, one accent, type faces]. [Camera rule]. [How a cursor or hero object behaves]. The last frame is the first frame, so it loops.
Banned: [effects you do not want, e.g. crossfades, glows, particle bursts, bouncy easing, stock footage, holds longer than 1s, anything that looks like a template].
</direction>

<structure>
[BPM, bars or beats], something happens on every beat.
[Scene 1]: [what it is, and what it physically becomes].
[Scene 2]: [...]
Return: match the final frame to the first (cursor, hero object, type) so the loop does not stutter.
</structure>

<build>
1. One HTML file, [WxH] at 60fps. Compute every visual from time inside seek(t): no CSS transitions, timers or state carried between frames.
2. Closed-form springs for every pop and settle; a value with many targets is the sum of one spring per change.
3. One camera transform keyed by [time, zoom, x, y], zoom in log space, one eased move per scene.
4. Analyse the track with numpy for tempo, beat grid and the drop; place every cut and UI hit on the grid. Place each sound effect by its measured peak; loudnorm to -14 LUFS; licensed audio only.
5. Render with Playwright at 60fps, [8] subframes per frame blended with ffmpeg tmix. Render one frame per beat first and fix what is off-grid, cramped or hard to read; then scan for single-frame pops.
</build>

<gotchas>
[Anything you already know will go wrong: shapes that fill the screen must overscale past the corners; incoming and outgoing text need separate timing; first and last frames must match.]
</gotchas>

<start>
Ask me for the inputs, then show me the beat map and four stills before building the full video.
</start>
```

## Writing tips drawn from the evidence

1. **Decide the profile first** (`style-profiles.md`). A concept film wants fewer words than a UI loop.
2. **One governing idea per piece**: one shape, one dot, one ball, one frame, one medium. Every strong structured prompt has exactly one.
3. **Say what changes into what**, not what appears. The structured prompts describe transformations ("the circle becomes a square, shrinks, the grid unfolds from behind it"), which is what produces continuity.
4. **Ban the clichés explicitly** and, if you want them, name them as decisions.
5. **Ask for a review gate** (beat map plus stills) before a long render.
6. **Supply real assets** for premium results (photos, clips, licensed track). The ban "never placeholder cards" [227] is the difference between a demo and a film.
7. **Add one constraint to a generic prompt.** Of the 28 identical showreel prompts, the ones that stand out are the ones whose result carries one idea through to the end.
8. **Think in tempo.** The best structured prompts fix a BPM and count beats, so cuts, hits and the drop are planned rather than hoped for.
