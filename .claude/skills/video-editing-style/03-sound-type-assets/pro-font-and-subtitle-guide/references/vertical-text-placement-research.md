# Where text goes in a 9:16 short: research (2026-11-25)

**Why:** the user's words were "first dont create by you own just research and which is best place to put in shorts in vertical videos", then "also you have seen many short form videos also use that information with this". The earlier placement numbers in `text-animation-moves` (stack top y 1120, "2-3 above-head moments") were Claude's own guesses. Those guesses are replaced by the findings below.

**Sources, three kinds:**
- **[P]** Platform UI safe zones: the ad specs (Meta, TikTok) and the safe-zone tools that measured them.
- **[S]** Studies: eye tracking on where subtitles sit.
- **[M]** Our own measured pro reels (already in the skills).

Vendor blogs are marked as such: their numbers are rules of thumb, not tests.

## 1. What the platform UI covers on 1080 x 1920 [P]
| Platform | Top | Bottom | Right | Left | Source |
|---|---|---|---|---|---|
| Instagram Reels **ads** (Meta) | 14 % = 269 px | 35 % = 672 px (40 % = 768 px with a disclaimer) | 6 % = 65 px | 6 % = 65 px | Meta Reels ad specs as quoted by Sirency, Admanage (checked 2026-10-29), Lilach Bullock; Ads Manager has a "Safe zone guardrail" overlay |
| Instagram Reels, ordinary posts | about 220-270 px | about 310-450 px | about 120 px | about 60 px | vendor checkers (BlitzCut, Hopper, TryMyPost); not a Meta spec |
| TikTok In-Feed **ads** | 240 px | 660 px | 120 px | 120 px | measured from TikTok's own template files (Socialync, Manypixels). TikTok publishes files, not numbers |
| TikTok, ordinary posts | about 130 px | about 320-350 px | 120-164 px (button column) | about 60 px | BlitzCut (vendor) |
| YouTube Shorts | about 120-210 px | about 300-450 px (title, channel, subscribe) | about 48-192 px | about 60 px | vendors disagree (Kapwing, Eklipse, Reap, BlitzCut); Google's universal safe-zone file gives no pixels |

**What all of them agree on:** the bottom of the frame is covered by the caption, username, music and subscribe UI, and the right edge by the button column. The safest place is the middle of the frame.

## 2. Where subtitles should sit relative to the speaker [S]
- **Kurzhals et al., CHI 2017, "Close to the Action"** (eye-tracking lab study, n = 40): compared subtitles placed close to the speaker with the usual bottom-centre position.
  - Near-speaker subtitles gave more fixations on the relevant parts of the picture.
  - They also gave shorter eye jumps (saccades), which the authors tie to less eye strain.
- **Brown et al., BBC R&D, TVX 2015, "Dynamic Subtitles: the User Experience"** (eye tracking, clips from *Sherlock*):
  - People who watched subtitles placed near the action looked at the picture more like viewers with no subtitles at all.
  - The user experience improved, though not for every kind of subtitle user.
  - The rule stressed most: **never cover any part of the speaker's mouth.**
- **Brooks and Armstrong** (summarised in the BBC work): subtitles placed near the speaker helped viewers enjoy the video and recognise who was speaking.

**Meaning for a talking-head short:** put the subtitles close to the face, so the eye doesn't travel far, but never on the mouth or eyes. That is **just under the chin**, not at the very bottom of the frame.

## 3. What the short-form reels we already studied do [M]
These are all the reels measured in earlier sessions (positions taken from the skills' own notes; % = caption centre as a share of the frame height from the top).

**Talking head, speaker centred (the client's framing):**
| Reel (where it is written up) | Running caption | Text above the head |
|---|---|---|
| Tharun Speaks reel A (`tharun-speaks-edit-style`) | 68 % (y 1304), on the chest under the chin; never in the bottom 15 % | hook headline behind the head (y 368-830), number / counting headlines (y 190-514), small side label |
| Tharun Speaks reel B | 55 % (y 1062): tighter framing, so the caption moves up and stays under the chin | same |
| Tharun look across the 82-reel library (`motion-graphics-style`) | 62-70 %, over the chest, never the mouth | hook / number headlines only |
| P1-P14 profile summary (`shorts-editing-pro/references/style-profiles.md`) | one line at 55-68 % | rare |
| R4 talking-head showcase (`event-map-reel-edit-style`) | two-tier card: keyword 63 % (±2.5 % over 13 cards), small line 59 %, below the chin | none |
| P6 violet condensed tips, P8 real-estate explainer (`pro-video-editing/profiles`) | two tiers (small line + big word) on the chest band | none |
| Ultimate Editors reel 3 (`ultimate-editors-shortform-style`) | hook block 49-56 %, section titles 62-76 %, never on the face | none |
| Kobe motivation (mustard R4) | 62-66 %, chest, one warm word per line | none |
| Raj Shamani quote page (mustard R3) | centred on the chest | two-tone header in the top band |
| Hormozi short (mustard R5) | about 50 %: a walking selfie, so the face is small and high | none |
| P10 amber UI educator | 45-50 %: the speaker is small in the frame, so the chest is higher | none |
| Our own house rule (`reel-editing-method`) | top of the caption at y 1250 (65 %), y 1210 when a card sits below | behind-head words (its "top 60-90 px" lies inside the top UI band, so use y 270 or lower) |
| R7 "golden rule" lesson reel (`editor-showcase-caption-edit-style`, measured 2026-11-27 on 947 frames) | **53.8 %** median (47-62 %); the caption centre sits **17.4 % of the height below the chin** (12.6-21.3 %); 96 % of caption frames inside x 30-70 %, y 45-70 % | none; one deliberate scatter to the top corners on the line "make people's eyes move" |
| R8 script + sans reel (same skill) | **58.5 %** median (56.6-64.4 %) over 12 caption groups, block about 50 % of the width | none |
| R6 brand-colour caps reel (same skill) | 56-64 % (about 58 %) in all seven beats | none |
| R5 type-card reel (same skill) | on footage: on the chest; on its type cards the hero word sits mid-frame | none |

**When the text goes beside or above the face instead:**
| Reel | Where | Why it works there |
|---|---|---|
| Raj Shamani podcast (mustard R1) | stack beside the face at 33-50 % | wide podcast frame with empty space beside the head |
| shami.mp4 "$80 edit" (`text-animation-moves` A) | stacks in the empty side, alternating sides | a 16:9 picture inside the 9:16 post, speaker off-centre |
| tobydeboer Grind szn (client brief B) | beside the person in the sky / wall, moving every shot | music montage, no talking head |
| Instagram aesthetic references (`aesthetic-pro-reel-edit-style`, I2) | hook pairs at the top of the frame | the hook only, then the captions go back to the chest |
| Telugu podcast pages (mustard R7) | yellow title in a top black band | a fixed title, not subtitles |

**Pattern from about 15 measured reels:**
- When the speaker is centred, the running subtitles sit at **55-68 % of the height** (median about 63 %), just under the chin.
- They move higher (45-56 %) only when the face is small or high in the frame, or for a hook block.
- Text beside the face appears only when there is real empty space: a wide podcast shot, an off-centre speaker, 16:9 inside 9:16, or a montage.
- Text above the head is an accent: the hook headline, numbers, labels, hook pairs. **No measured reel runs its subtitles above the head.**

**Added 2026-11-27, a way to place the block in any framing:** find the chin in a still, then put the caption block centre at **chin + 17 % of the frame height** (13-21 %). A tight shot (chin at 45 %) gives 62 %; a wide shot (chin at 38 %) gives 55 %. R7's own script gives the reason: "if you make people's eyes move, you lose their attention". It also keeps the eye line at one height (26-33 %) through every cut, so the caption never has to chase the face.

## 4. The rule (all three sources together)
1. **Running subtitles and word stacks:**
   - centred at x 540, with the block centre at **58-65 % of the height (y about 1110-1250)**: the middle of the 55-68 % band the studied reels use, and above the bottom UI;
   - the block's top at least about 60 px below the chin, and its bottom above y 1470 (the bottom UI on Reels and TikTok);
   - lines no wider than x 120-960, which clears the button column on the right.
   - Tight framing (chin low in the frame): move up towards 55 % only if the block still clears the mouth. Wide framing: down to 68 % at most.
   - Measure the chin on a still for every video.
2. **If the short may run as an ad** (Meta Reels: bottom 35 %; TikTok: bottom 660 px), keep the whole block above y 1250, with its centre at about y 1150-1180.
3. **Never** on the mouth or eyes ([S] BBC). Avoid the hands where possible; when a gesture crosses the caption, the caption stays (R1 measured) or the line moves for that phrase only.
4. **Above the head** (the band between y about 270, below the top UI, and the hair top): only accent text.
   - The hook title, a number or counting headline, a short label.
   - At most **1-3 per short** (`shorts-editing-pro` rule 8; Tharun measured).
   - Never the running subtitles, and never a whole sentence-stack.
5. **Word stacks in the chest band:** 2 lines at most (the R4 two-tier card: a small line plus a keyword). A 3-5 line stack only on a plain side wall in an off-centre or 16:9 frame (the shami.mp4 reference).
6. **Check every edit on a phone-size sheet with a safe-zone overlay:** bottom 450 px, right 164 px, top 270 px shaded.

## Sources
- Meta Reels ad safe zone (14 / 35 / 6 %), as quoted by: https://www.sirency.com/blog/instagram-reels-safe-zone · https://admanage.ai/instagram-reels-safe-zone · https://www.lilachbullock.com/instagram-reels-safe-zone/
- TikTok In-Feed ad files, measured: https://ads.tiktok.com/help/article/video-ads-specifications?lang=en · https://www.socialync.io/tools/safe-zones/tiktok · https://www.manypixels.co/blog/social-media-design/tiktok-ad-specs
- Ordinary-post safe zones (vendors): https://blitzcutai.com/blog/best-caption-placement-short-form-video · https://www.hopperhq.com/blog/instagram-reel-size/ · https://www.trymypost.com/blog/instagram-reels-safe-zones-text-placement-2026 · https://www.kapwing.com/video-editor/youtube-shorts/safe-zone · https://reap.video/blog/short-form-video-safe-zones · https://services.google.com/fh/files/misc/universalsafezones-youtube.pdf
- Caption placement for talking heads (vendors): https://openclip.app/guides/caption-placement-guide · https://www.capcut.com/create/vertical-video-subtitles-placement-tips · https://www.opus.pro/blog/youtube-shorts-caption-subtitle-best-practices
- Kurzhals et al. 2017, CHI, DOI 10.1145/3025453.3025772: https://herohuyongtao.github.io/research/publications/eye-tracking-evaluation
- Brown et al. 2015, BBC R&D, TVX: https://research.manchester.ac.uk/en/publications/dynamic-subtitles-the-user-experience/ · https://salford-repository.worktribe.com/OutputFile/2155279
