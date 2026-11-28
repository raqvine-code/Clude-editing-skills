# THE WORKFLOW: PHOTO -> STYLE FRAME -> ANY SCENE
Everything runs on Higgsfield with two tools: the image generator (for the style frame) and Wan 3.0 (for the animation).

Step 1. Make the style frame. Open the image generator and pick a model that edits from a reference image (the guide's frames were made with GPT Image 2.5). Upload the original photo and paste the IMAGE PROMPT of the chosen style. Generate two or three variants and keep the one where the style reads best.

Step 2. Animate with Wan 3.0 using the style frame as a REFERENCE image. Start the prompt with "Use the reference image as the style and character reference", then describe any scene: a new place, a new action, a new camera. 5 seconds is a good first test.

Option B: start frame. If the video should begin exactly on the picture, upload the frame as the START frame instead and begin the prompt with "Animate this image in its exact style", then describe what moves.

Step 3. Go further: a whole multi-shot scene. Use the example in `multi-shot.md` and swap in your own story, line and style words.

TIPS (follow all of them):
- One style per generation. Always start from the original photo, never from another style's result.
- Simple photos work best: a clear face, visible hands, a simple pose and background.
- Keep the first paragraph of every animation prompt (the style description) and only rewrite the scene below it, so the look does not drift back to realistic.
- Describe motion that fits the style: bouncy for Rubber Hose, slow and eerie for Expressionism, stiff and stepped for Low Poly.
- Wan 3.0 generates sound with the video. Describe the sounds you want, and write "no music" if you don't want a score.
- Cost note from the guide: a 6-second 720p clip cost 10.5 credits in Wan 3.0 vs 42 in Seedance 2.5 (October 2026; prices can change).
