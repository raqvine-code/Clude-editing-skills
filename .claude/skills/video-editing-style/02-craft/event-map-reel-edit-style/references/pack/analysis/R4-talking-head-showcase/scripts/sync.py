import cv2, numpy as np, sys
R=sys.argv[1]
ed=lambda n: cv2.imread(R+'/ed/%04d.jpg'%n)
raw=lambda n: cv2.imread(R+'/raw/%04d.jpg'%n)
s,tx,ty=1.302,-7,-5
M=np.float32([[s,0,tx],[0,s,ty]])
def warp(img): return cv2.warpAffine(img,M,(392,696),flags=cv2.INTER_CUBIC,borderValue=(0,0,0))
valid=warp(np.full((550,232,3),255,np.uint8))[:,:,0]>250
valid[:,280:]=False
capmask=np.ones((696,392),bool); capmask[180:560,:]=True
print('sync check: mean abs err (gray, valid region, rows 0-380 to avoid captions) by offset')
for f in [130,160,340,520-0,660,700,760,800,960,1000,1040]:
    if f>=1066: continue
    e=cv2.cvtColor(ed(f),cv2.COLOR_BGR2GRAY).astype(float)
    res=[]
    for o in range(-3,4):
        if not(0<=f+o<1068): res.append(None); continue
        w=cv2.cvtColor(warp(raw(f+o)),cv2.COLOR_BGR2GRAY).astype(float)
        m=valid.copy(); m[380:,:]=False
        # normalise means to remove grade offset
        a=e[m]; b=w[m]; b=(b-b.mean())/b.std()*a.std()+a.mean()
        res.append(round(np.abs(a-b).mean(),2))
    print(f,res)
