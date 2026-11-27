import sys,cv2,numpy as np
D=sys.argv[1]
acc=np.zeros((640,360));n=0
for i in range(0,1226,2):
    acc+=cv2.imread(f'{D}/fr/{i:04d}.jpg',0); n+=1
m=acc/n
c=m[280:360,140:220].mean(); corners=np.mean([m[:60,:40].mean(),m[:60,-40:].mean(),m[-60:,:40].mean(),m[-60:,-40:].mean()])
edges_lr=np.mean([m[280:360,:20].mean(),m[280:360,-20:].mean()])
print(f"mean-of-all-frames luma: centre {c:.1f} corners {corners:.1f} ratio {corners/c:.2f} | L/R edge {edges_lr:.1f} ratio {edges_lr/c:.2f}")
# per-scene corner/centre ratio
for f in [30,85,200,280,306,420,540,660,745,800,890,1040,1105,1215]:
    g=cv2.imread(f'{D}/fr/{f:04d}.jpg',0).astype(float)
    print(f, round(np.mean([g[:50,:30].mean(),g[:50,-30:].mean(),g[-50:,:30].mean(),g[-50:,-30:].mean()])/g[260:380,120:240].mean(),2))
