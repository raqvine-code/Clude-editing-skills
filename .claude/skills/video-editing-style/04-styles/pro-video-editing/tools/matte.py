"""Person matte for behind-subject text (T8). Run with the venv that has mediapipe:
  ~/.local/share/whisper-venv/bin/python matte.py in.mp4 out_dir [t0] [t1]
Writes a grayscale PNG mask sequence out_dir/mask_00000.png (white = person) at the source size/fps, temporally smoothed (EMA 0.6) and
edge-feathered, ready to use as a track matte (text layer between plate and masked person)."""
import sys, os, cv2, numpy as np, mediapipe as mp
src, out = sys.argv[1], sys.argv[2]
t0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0
t1 = float(sys.argv[4]) if len(sys.argv) > 4 else 1e9
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS) or 30
w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000)
os.makedirs(out, exist_ok=True)
seg = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=0)
prev, n = None, 0
while True:
    ok, fr = cap.read()
    if not ok or cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 > t1:
        break
    m = seg.process(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)).segmentation_mask
    prev = m if prev is None else 0.6 * m + 0.4 * prev
    k = cv2.GaussianBlur(prev, (0, 0), 1.5)
    mask = np.clip((k - 0.35) / 0.3, 0, 1)
    cv2.imwrite(os.path.join(out, f"mask_{n:05d}.png"), (mask * 255).astype(np.uint8)); n += 1
print(out, n, "frames @", fps, "fps; use as luma track matte")
