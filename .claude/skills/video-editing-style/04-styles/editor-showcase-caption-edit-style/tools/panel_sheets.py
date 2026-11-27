#!/usr/bin/env python3
"""Panel sheet: psheet.py REEL_DIR W:H:X:Y F0 F1 STEP COLS TILE_W OUT.jpg [subx0,suby0,subx1,suby1 fractions of the panel]
Tiles are labelled with the source frame index and time (s)."""
import sys, cv2, numpy as np
r,crop,f0,f1,step,cols,tw,out=sys.argv[1:9]; f0,f1,step,cols,tw=int(f0),int(f1),int(step),int(cols),int(tw)
w,h,x,y=[int(v) for v in crop.split(':')]
sub=[float(v) for v in sys.argv[9].split(',')] if len(sys.argv)>9 else [0,0,1,1]
cap=cv2.VideoCapture(f'{r}/src/reel.mp4'); fps=cap.get(cv2.CAP_PROP_FPS); n=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
want=set(range(f0,min(f1,n),step)); tiles=[]; i=0
cap.set(cv2.CAP_PROP_POS_FRAMES,f0); i=f0
while i<min(f1,n):
    ok,f=cap.read()
    if not ok: break
    if i in want:
        p=f[y:y+h,x:x+w]; ph,pw=p.shape[:2]
        p=p[int(sub[1]*ph):int(sub[3]*ph),int(sub[0]*pw):int(sub[2]*pw)]
        th=int(round(p.shape[0]*tw/p.shape[1])); t=cv2.resize(p,(tw,th),interpolation=cv2.INTER_AREA if tw<p.shape[1] else cv2.INTER_CUBIC)
        lab=f'{i} {i/fps:.2f}'; cv2.rectangle(t,(0,0),(8*len(lab)+4,15),(0,0,0),-1); cv2.putText(t,lab,(2,12),cv2.FONT_HERSHEY_SIMPLEX,0.42,(0,255,255),1,cv2.LINE_AA)
        tiles.append(t)
    i+=1
rows=[]
for k in range(0,len(tiles),cols):
    row=tiles[k:k+cols]; row+= [np.zeros_like(tiles[0])]*(cols-len(row)); rows.append(np.hstack(row))
img=np.vstack(rows); cv2.imwrite(out,img,[cv2.IMWRITE_JPEG_QUALITY,88]); print(out,img.shape[1],'x',img.shape[0],len(tiles),'tiles')
