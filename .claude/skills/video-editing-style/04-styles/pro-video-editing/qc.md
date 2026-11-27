# Quality Control System

Run after the sample render and again on the final.

## Automatic checks (tools)
1. `python3 tools/refscan.py <folder-with-render>` or run `tools/vstrip.py` on the render around every transition: confirm frame counts match the plan (+/-1 f).
2. Contact sheet at 0.5 s (refscan output) - look for: empty frames, text over faces, colour drift, unreadable text.
3. Loudness: `ffmpeg -i out.mp4 -af ebur128=peak=true -f null -` -> -14 LUFS +/-1, true peak <= -1 dBTP (unless user said otherwise).
4. Sync: compare transcript word times with keyword-graphic first full frame: must be within -0.35..+0.1 s.

## Visual checklist
- [ ] Hook moves on frame 0-3.
- [ ] Max 1 accent colour (+ white/black/greys).
- [ ] Every on-screen word readable for >= 0.5 s (3-tier keyword >= 1 s).
- [ ] No text crosses eyes/mouth; safe zones for platform UI (9:16: keep 14 % bottom, 8 % top, 12 % right clear).
- [ ] Entries 2-8 f, morphs ~15 f; no animation slower than 1.5 s except camera pans.
- [ ] Motion blur on anything moving > 1/3 frame width per frame-group.
- [ ] Transitions from the library only; no dissolves/spins unless the user asks.
- [ ] Matte edges clean on behind-subject text (no halo, no flicker > 1 px).
- [ ] Style matches the chosen profile; do not mix profiles in one video.

## Side-by-side test against references
Render the same beat with the recreated technique and build a strip next to the reference strip (`vstrip.py` both) at equal frame counts; record differences in `knowledge/CHANGELOG.md`.
