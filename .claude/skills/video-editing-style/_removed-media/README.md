# Media removed to save storage (owner's request, 2026-11-28)

The owner wants only the trained skills (rules, style profiles, numbers, scripts) in GitHub, not videos or frames.
- **Removed:** 199 images (frames, storyboards, contact sheets, font and style boards) and the 37 MB zip `video-editing-style-data.zip` (161 frames of the five reference reels; every text and JSON file in it was already in the skill). Their paths are in `removed-image-paths.txt`.
- **Kept (2 key frames):**
  - `04-styles/vice-neon-title-edit-style/references/worked-example-gta6/final_key_moments.jpg`: the GTA 6 style;
  - `05-clients/move-with-raghu/worked-example-back-to-facts/frames/final_contact_sheet.jpg`: the back-to-facts style.
- **Still in the repo:** every rule, profile, measurement, script, font and the real sound-effect files. Markdown links to a removed image now point at nothing: read the words around the link, the numbers are in the text.
- **Rule from now on:** save a style as text and numbers (profile, measured values, working code). Never commit videos, frames or zips of frames. At most 1-2 key frames in the whole repo, only if the owner asks. A new style needs a frame for review: send it in the chat, do not commit it.
- **Getting an old image back:** it is still in the git history of this repository until the history is rewritten: `git show <commit-before-removal>:<path from the list>`.
