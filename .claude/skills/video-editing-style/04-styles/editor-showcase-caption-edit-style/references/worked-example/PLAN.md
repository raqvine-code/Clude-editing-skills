# PLAN: "The story you tell yourself" (redo)

## A. Footage analysis
- Four clips, 1080x1920, 60 fps, 12.42 + 10.36 + 12.40 + 12.45 s = 47.6 s, one speaker, green slatted wall, seated at a microphone, one continuous take (joins checked frame by frame in the first session: each clip's last frame matches the next clip's first).
- Joined once at 30 fps with 6 ms fades at the three joins (no clicks): `src30.mp4`, 1428 frames.
- Words: 170, word onsets from three Whisper models + energy map (first session). Speech about 215 wpm with pauses at 8.84-9.32, 12.21-12.69, 34.66-35.20, 38.32-38.90, 43.09-43.56, 45.08-45.57.
- Face track: centre x 344-535 px (he sways), top 552, chin 936. Eye line used for framing: y 715 -> screen y 600; chin lands at 44-47 % of the height, so the caption block centre (chin + 17 %) is 61-64 %.

## B. Goal and audience
- A premium 47 s short for an English-speaking audience (self-narrative, psychology / growth); retention to the CTA "share it with someone who needs to hear this". Not four edits: one story with one visual language.

## C. Story structure
Hook (0-3.1 s: the claim, "story ... self-creating") -> luck frame (3.3-9.5: good things, luck as a frame) -> reframe (9.5-18.5: the research, FACTS vs FRAMES) -> three questions (18.5-24.6) -> patterns (24.7-31: PATTERNS match cut, repeating) -> seeing (31-35: eye) -> the turn (35.16: "if they want to change it") -> the thesis quote (36.45-41.6: self-conversation) -> the callback (41.9-45.4: aware, mirror: talking to yourself) -> CTA / loop (45.45-47.6: the hook card with SHARE).

## D. Style decision
P19 (under-chin kinetic captions, one focal zone) as the base, with P17 object cards (speaker in a card, colour inversion) as the designed inserts. Reasons: one talking speaker, no real cuts, so the frame has to change through plates and framing; the client bar asks for Instagram-editor level and for captions on the chest; no BGM, no grade means designed motion carries the energy. Client colours: ink `#1A1410`, paper `#EFE7D6`, haldi `#E2AA2C` (deep `#B9831A` on paper), kumkum `#C8372D` on NOT only, cream `#F4EFE3`.

## E. Shot-by-shot plan
See `PRE-EDIT.md` section 3 (speech -> visual map) and 4 (motion-graphics table). Camera: 26 shots, hard jump every 1-2.5 s, wide 1.14-1.22 / tight 1.40-1.48, slow 4-6 % drift inside a shot, face-follow on x.

## F. Graphics and assets
Built in code (`build.py` + `caption_moves.py`): 9 layers (5 speaker/B-roll cards, tile list, match cut, HL quote card, CTA card). Footage: 6 Mixkit clips (sunset, book, couple, coworkers, dominoes, eye). Fonts: Poppins SemiBold / ExtraBold, Playfair Display ExtraBold Italic. SFX: 71 cues from the Mixkit set and the synthesised set of the first session. No music.

## G. Creative ideas (Claude's own)
1. **The frame is the motif.** The picture frame around his face closes in on "luck frame" (8.1), returns inverted and in colour on "frames of your life" (16.82), and the opening and closing cards are the same rounded frame: the speaker lives inside the story's frame, and the video loops.
2. **FACTS -> FRAMES as one object.** Facts are black-and-white and struck out on ink; frames arrive in colour on paper, with the speaker inside a haldi frame: the contrast is shown by the picture changing state, not by words.
3. **The match cut is made, not bought.** PATTERNS is pinned while seven patterns (stripes, dots, chevrons, rings, bricks, diagonals, checks) flash in the client's colours every four frames; the dominoes then "repeat" it.
4. **He talks to himself, literally** (mirror split on "talking to yourself").

## H. Sound plan
Voice (high-passed at 75 Hz) + 71 effects, no music (client). Whooshes on every card in / out and B-roll entry, panned by motion where it matters; textures on every change (pops on hero words, scratch on NOT and the strike, paper swipes under the brush, 7 ticks on the match cut); risers into the MC, the turn and the mirror; hits on the claim, the contrast and the loop. Master -14 LUFS, true peak -1.5 dBTP.

## I. Risks and the three weakest moments
1. 9.5-12.4 "and what if really have been thinking about a lot": filler words; fix: wide-to-tight jump, ring on "thinking", hero THINKING.
2. 36.45-41.6 the speaker is dimmed behind a card for 5 s: fix: blur, not black; face stays readable; brush + paper swipes + a card pulse on the second sentence start.
3. 19.8-22.7 one tile alone for 3 s: fix: INTERPRETING hero and a camera jump at 19.8; the tile sits under the caption, not on it.

## J. QC targets and delivery
- Gate READY before the render and again after. Neutral colour: mean RGB of rendered speaker frames within 2 levels of the source frames (no grade). Caption block centre 58-65 % of the height. No text above the head. Phone-size contact sheet. Loudness -14 +/- 1 LUFS, true peak <= -1.0 dBTP, 1428 frames, no black or freeze frames.
- Delivery: `story_you_tell_yourself.mp4` (1080x1920, 30 fps, H.264 + AAC) to the user in the session.
