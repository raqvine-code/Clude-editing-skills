# 3. PRE-EDIT sheet (copy to `<project>/PRE-EDIT.md` and fill in BEFORE PLAN.md)

```bash
cp "01-process/before-edit/3-PRE-EDIT-SHEET.md" "<ROOT>/edits/<project>/PRE-EDIT.md"
```

## 0. The job
- Video file / client / form (9:16 short, 16:9 long, captions-only...):
- The user's words for THIS video (verbatim):
- Overrides for this video (no BGM, no grade, fonts...):
- The ONE style (`video-styles-atlas`, profile P__) and why:

## 1. Skills read (from `1-READ-THESE-SKILLS.md`; one row per skill)
| Skill | Read | The one thing taken for this video (or "n/a: reason") |
|---|---|---|
| CHANGELOG top 3 + LEARNING-LOG feedback | [ ] | |
| my-editing-rules (11: HL + MC) | [ ] | |
| mistakes-to-avoid (H 16-21) | [ ] | |
| fonts-and-colours / pro-font-and-subtitle-guide | [ ] | |
| video-styles-atlas | [ ] | |
| edit-kit-playbook (4: speech -> visual) | [ ] | |
| beginner-to-pro-edit-tips | [ ] | |
| shorts-editing-pro + LEARNING-LOG | [ ] | |
| event-map-reel-edit-style (8) | [ ] | |
| faceless-explainer-reel-edit-style (12B) | [ ] | |
| ultimate-editors-shortform-style (3-5) | [ ] | |
| aesthetic-pro-reel-edit-style (3 insert menu) | [ ] | |
| mustard-red-caption-style (2b, 2c) | [ ] | |
| text-animation-moves | [ ] | |
| editor-showcase-caption-edit-style (P17-P20: profile, chest placement, plates, focus pull) | [ ] | |
| tharun-speaks-edit-style / reel-editing-method / pro-video-editing | [ ] | |
| motion-graphics-style | [ ] | |
| text-highlight-match-cut | [ ] | |
| video-intro-design | [ ] | |
| app-product-animation | [ ] | |
| client-video-editing-process | [ ] | |
| motivational-video-editing / top-editor-styles | [ ] | |
| broll-library / png-library / where-to-find-assets | [ ] | |
| sound-and-music-design / ue-sound-design | [ ] | |

## 2. What is in the words (from the full transcript)
- Lists (3+ items):
- Contrasts (X vs Y, not X but Y):
- Numbers / percentages:
- Quotes, sources, books, scripture, named people:
- Key word repeated 2+ times (MC candidate):
- Named things / objects:
- The turn ("but..."), the payoff, the CTA, the loop line:
- Pauses of 0.5 s or more (from `analysis/facts.json`):

## 3. Speech -> visual map (every line gets a visual that matches its exact words)
| t | Words | Visual: MG kind / B-roll / face | Text move | Sound |
|---|---|---|---|---|

## 4. Motion-graphics plan (floor from `2-PRO-MOVE-MENU.md`)
| # | t0-t1 | Kind (list device, contrast object, HL card, MC, UI card, split, full scene, object behind head, paper, plate, HUD / ring, B&W, mirror) | Words it shows | Build (scenes.py key `mg_...` / `layers` / kit key) | Sound |
|---|---|---|---|---|---|

Check before going on:
- [ ] count >= runtime / 8
- [ ] 3+ kinds
- [ ] >= 25 % of runtime
- [ ] no stretch over 9 s without one
- [ ] one in the first 3 s
- [ ] every element 25 % smaller, one effect, dull colours

## 5. HL + MC
- HL (page / quote / verse, brush wipe under the spoken words):
- MC (pinned word + 5-7 flash-cut sources):
- Skip reason, only if the script truly has no quote or repeated word (goes into `edl["meta"]["skip_hl"]` / `["skip_mc"]`):

## 6. Asset search log (local first)
| Noun / idea | broll-library / png-library hit | Download (site, id) | Frames watched, matches the words |
|---|---|---|---|

## 7. Research (`mistakes-to-avoid` 21a, CLAUDE.md Rule 4.3)
- 5+ references per new scene type (Dribbble, Behance, Pinterest, Instagram via `browser_reference_capture.js`), with what each one gives:

## 8. Sound passes
- [ ] whooshes on every movement
- [ ] textures on every change
- [ ] risers + hits on turn / reveal / payoff / loop
- [ ] a flick on every cut
- Music per the brief:

## 9. Clashes (CLAUDE.md Rule 3)
- Any request that goes against a skill, or two skills that disagree: what, and whether the user has been told:

## 10. Gate (paste the output)
- `pre_edit_gate.py` on the DRAFT EDL: must say `RESULT: READY` before the full render.
- Hook sample (6-10 s, full quality) watched: [ ]
- Gate again on the final EDL + scorecard: [ ]
