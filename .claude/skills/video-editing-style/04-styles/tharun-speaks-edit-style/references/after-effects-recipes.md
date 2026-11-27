# After Effects recipes

Settings and paste-ready expressions for building the style in After Effects. Values are for a 1080x1920 composition at 25 fps. At 30 fps multiply frame counts by 1.2; flashes stay 2 frames.

Menu names follow recent After Effects versions. If an item has moved, search for it by name in the Effects & Presets panel.

To add an expression: hold Alt (Windows) or Option (Mac) and click the stopwatch next to the property, then paste.

The shadow, blur and glow amounts below are starting values matched by eye. Tune them against your footage.

## 1. Project set-up

1. Main composition: 1080x1920, your footage frame rate.
2. One composition per full-screen scene (coin, demo card, kinetic title, paper, CTA). Drop them into the main composition as layers.
3. Layer order in the main composition, top to bottom: black flash solids, captions, white flash solids, flash adjustment layers, labels and badges, cut-out speaker copies, behind-subject text and cards, footage.

## 2. Caption style

Character panel:

| Setting | Value |
|---|---|
| Font | Inter Tight Bold |
| Size | 116 px |
| Tracking | -25 |
| Fill | white, no stroke |
| Paragraph | Center text |

Position: `540, 1304`.

Anchor Point expression, so the text block stays centred on that point whatever it says:

```
r = sourceRectAtTime(time, false);
[r.left + r.width / 2, r.top + r.height / 2]
```

Shadow, two layers:

1. Layer > Layer Styles > Drop Shadow: black, Opacity 80%, Angle 120, Distance 5, Spread 0, Size 12.
2. Effect > Perspective > Drop Shadow: black, Opacity 50%, Direction 180, Distance 10, Softness 34.

Save this layer as your caption master and duplicate it.

## 3. Caption beats from a list

One text layer can play the whole single-line caption track. Paste this on Source Text and replace the list. Each entry is `[in frame, "text"]`. Use `""` to clear the caption.

```
beats = [
  [57, "This"],
  [59, "will"],
  [63, "change"],
  [69, "your week."],
  [86, ""]
];
f = timeToFrames(time);
txt = "";
for (i = 0; i < beats.length; i++) {
  if (f >= beats[i][0]) txt = beats[i][1];
}
txt
```

The text changes on the exact frame with no animation, which is what the style needs. Frames count from the start of the composition.

By hand instead: put the playhead on a beat, change the text, and After Effects adds a Source Text keyframe. Source Text keyframes always hold.

## 4. Emphasis stack

Use three text layers named `LEAD`, `KEY` and `TRAIL`. Trim each so it starts on its own word. End all three on the same frame.

| Layer | Size | Paragraph |
|---|---|---|
| LEAD | 84 px | Left align |
| KEY | 203 px up to 5 letters, 168 px for 6-8, 151 px for 9 or more | Center |
| TRAIL | 84 px | Right align |

Give `KEY` the caption Anchor Point expression from section 2 and position it at `540, 1290`.

`LEAD` Anchor Point:

```
r = sourceRectAtTime(time, false);
[r.left, r.top + r.height]
```

`LEAD` Position, which pins it to the keyword's top-left corner:

```
k = thisComp.layer("KEY");
r = k.sourceRectAtTime(time, false);
p = k.toComp([r.left, r.top]);
[p[0], p[1] + 4]
```

`TRAIL` Anchor Point:

```
r = sourceRectAtTime(time, false);
[r.left + r.width, r.top]
```

`TRAIL` Position, pinned to the keyword's bottom-right corner:

```
k = thisComp.layer("KEY");
r = k.sourceRectAtTime(time, false);
p = k.toComp([r.left + r.width, r.top + r.height]);
[p[0], p[1] - 4]
```

The lead-in is on screen before the keyword. Because its position reads the keyword layer even before that layer starts, it is already in its final place. Change the 4 in each Position expression to tighten or loosen the lines.

## 5. Punch-in at a jump cut

1. Put the playhead on the cut point and choose Edit > Split Layer.
2. On the second piece, drag the anchor point onto the face with the Pan Behind tool.
3. Set Scale between 127% and 143%.
4. Split again at the next cut and set that piece back to 100%.

No keyframes. The size changes on the cut.

## 6. Slow push-in

Scale expression for a take longer than 2.5 s:

```
rate = 2.5;   // percent per second, use 1.2 to 3.6
base = 100;   // use 139 on a punched-in piece
s = base + rate * (time - inPoint);
[s, s]
```

## 7. Hook push-in

1. Scale keyframe 100% on frame 0.
2. Scale keyframe 116% on frame 43.
3. Select the second keyframe: Animation > Keyframe Assistant > Easy Ease In.
4. Anchor point on the face.

## 8. Negative flash

1. Layer > New > Adjustment Layer. Trim it to 1 frame.
2. Place it on the last frame of the outgoing shot, above the footage and its overlays, below the captions.
3. Add Effect > Channel > Invert.
4. Add Effect > Color Correction > Hue/Saturation and set Master Saturation to -100.
5. Layer > New > Solid, black, 1 frame long, on the next frame, above everything including captions.
6. The new shot starts on the frame after the black one.

## 9. White flash

1. Adjustment layer, 1 frame, on the last frame of the outgoing shot, below the captions. Add Effect > Color Correction > Exposure and raise Exposure to about 2.5.
2. White solid, 1 frame, on the next frame, below the captions.
3. The new shot starts on the frame after.

## 10. Headline behind the subject

1. Duplicate the footage layer.
2. On the top copy, isolate the speaker with the Roto Brush tool or any background remover. Check hair and fingers on every frame the text touches.
3. Put the headline text layers between the two copies.
4. On the headline: Effect > Blur & Sharpen > Gaussian Blur at 3, then Effect > Stylize > Glow with Threshold 60%, Radius 40, Intensity 0.6.
5. Trim each word's layer to start on its spoken frame.

Display type settings: Bebas Neue, All Caps, Horizontal Scale 80%, Tracking -20. For giant numerals use Anton at Horizontal Scale 83%.

## 11. Lime label that sizes itself

1. Text layer named `LABEL`: Bebas Neue, 170 px, Horizontal Scale 80%, black, Center text. Place it so the box will sit between y 1406 and y 1574.
2. Shape layer named `BOX` under it: one rectangle, fill `#D6FD00`, no stroke.
3. Parent `BOX` to `LABEL`. Then set the `BOX` layer's Position to `0, 0` and Anchor Point to `0, 0`, and the rectangle group's Transform Position to `0, 0`.
4. Rectangle Path > Size:

```
t = thisComp.layer("LABEL");
r = t.sourceRectAtTime(time, false);
[r.width + 48, r.height + 22]
```

5. Rectangle Path > Position:

```
t = thisComp.layer("LABEL");
r = t.sourceRectAtTime(time, false);
[r.left + r.width / 2, r.top + r.height / 2]
```

6. Swap the label's word with Source Text keyframes on the spoken frames. The box follows.

## 12. Kinetic title on black

1. Black solid as the background.
2. One text layer per word or line, lime `#D6FD00`, display type at about 238 px.
3. Start each layer 6 frames after the one before. No keyframes.
4. The small joining word is in the caption font, about 70 px, lime.

## 13. Type-on label, letter by letter

1. On the text layer: Animate > Opacity, and set the animator's Opacity to 0.
2. Open Range Selector > Advanced and set Smoothness to 0%.
3. Keyframe Range Selector > Start from 0% to 100% over 1.5 frames per letter.

## 14. Cards

Screenshot card behind the head:

1. Rounded rectangle about 540x768 with the screenshot inside, corner radius 16, soft drop shadow.
2. Position keyframes: 90 px left of the final place, then the final place 4 frames later. Easy Ease In on the last keyframe.
3. Opacity 0 to 100 over the same 4 frames.
4. Turn on Motion Blur for the layer and the composition.
5. Place the card layer under the cut-out speaker copy.

Article card: rise 60 px over 8 frames with Opacity 0 to 100.

Highlighter: a `#F8E202` solid over the phrase with blending mode Multiply. Reveal it left to right over 4 frames with Effect > Transition > Linear Wipe, Transition Completion 100% to 0%.

## 15. Icon badge pop

1. White circle, 183 px, with a dark icon. Layer Styles > Outer Glow, white, Size 46.
2. Scale 30% to 100% over 6 frames, Easy Ease In on the last keyframe.
3. Rotation -90 to 0 over the same 6 frames.
4. Opacity 0 to 100 over the first 3 frames.

## 16. Step coin flip

1. Build the coin in its own composition with two layers: the number side, and the name side.
2. Make both 3D layers. Rotate the name side 180 degrees on Y. Parent both to a null.
3. On the null, over 12 frames: Position from the coin's place in the row to the centre, Scale 40% to 100%, Y Rotation 0 to 540 degrees. Easy Ease In on the last keyframes.
4. Hold for 16 to 38 frames.

## 17. Backgrounds

Paper:

1. Solid `#E8E2D7`.
2. A dark solid on top with a large feathered elliptical mask set to Subtract, Opacity 45-60%, for the vignette.
3. Effect > Noise & Grain > Noise at 6-8% on an adjustment layer for grain.

White grid:

1. Solid `#FDFDFD`.
2. A second solid with Effect > Generate > Grid: Size From set to Width & Height Sliders, Width 113, Height 91, Border 1, colour `#E0E0E0`.
3. A large feathered elliptical mask on the grid layer so the lines fade toward the edges.

Coin scene:

1. Solid `#040309`.
2. Two large, heavily feathered ellipses: `#641C97` at the left edge, `#0A2666` at the upper right.

## 18. Final checks in After Effects

- Step through each flash frame by frame: exactly one effect frame and one solid frame.
- Step through the first frame of five captions: each is at full size and full opacity.
- Turn the cut-out copy off and on: the headline should be whole behind it and readable with it.
- Solo the caption layers: no beat with more than three words outside a stack.
