# Summarise dominant-plane camera motion per segment (360x640 frames; px reported at 720 wide)
import sys, cv2, numpy as np, math
D=sys.argv[1]
segs=[("hook pullback-rotate",0,39),("hook drift",39,50),("hook zoom-through window",50,94),
("sky card+ticker",112,150),("sky ticker pan",150,220),("study settle",240,294),("study exit blur",294,299),
("1840s grid",300,372),("graph follow",375,460),("corridor walk",486,598),("corridor exit",600,614),
("sink",618,688),("deathrate",704,750),("clipboard",770,811),("clip->news whip",811,827),("newspaper",830,920),
("microscope",946,972),("spotlight",982,1060),("cta text",1075,1118),("cta collapse",1118,1140),("laptop",1140,1225)]
def g(n): return cv2.cvtColor(cv2.imread(f'{D}/fr/{n:04d}.jpg'),cv2.COLOR_BGR2GRAY)
print("segment                     frames     cum_scale  %/s     rot_deg  dx_px  dy_px (720w)  px/s   peak_step_scale")
for name,a,b in segs:
    prev=g(a); cs=1; cr=0; cx=0; cy=0; peak=1; n_ok=0
    for n in range(a+1,b+1):
        cur=g(n)
        p=cv2.goodFeaturesToTrack(prev,400,0.01,6)
        if p is None or len(p)<12: prev=cur; continue
        q,st,err=cv2.calcOpticalFlowPyrLK(prev,cur,p,None,winSize=(21,21),maxLevel=3)
        ok=st.ravel()==1
        if ok.sum()<12: prev=cur; continue
        M,inl=cv2.estimateAffinePartial2D(p[ok],q[ok],method=cv2.RANSAC,ransacReprojThreshold=2.0)
        if M is None: prev=cur; continue
        s=math.hypot(M[0,0],M[1,0]); r=math.degrees(math.atan2(M[1,0],M[0,0]))
        c=np.array([180,320,1.0]); t=M@c-c[:2]
        cs*=s; cr+=r; cx+=t[0]; cy+=t[1]; n_ok+=1
        if abs(math.log(s))>abs(math.log(peak)): peak=s
        prev=cur
    dur=(b-a)/30
    rate=(cs**(1/dur)-1)*100 if dur>0 else 0
    print(f"{name:27s} {a:4d}-{b:4d}  {cs:8.3f}  {rate:+6.1f}  {cr:+7.1f}  {2*cx:+6.0f} {2*cy:+6.0f}   {2*math.hypot(cx,cy)/dur:6.0f}   {peak:.4f}  ok={n_ok}")
