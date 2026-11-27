import sys,cv2,numpy as np
D=sys.argv[1]
def ang(n):
    im=cv2.imread(f'{D}/fr/{n:04d}.jpg',0)
    e=cv2.Canny(cv2.GaussianBlur(im,(3,3),0),40,120)
    L=cv2.HoughLinesP(e,1,np.pi/360,60,minLineLength=60,maxLineGap=4)
    if L is None: return None
    a=[]
    for x1,y1,x2,y2 in L.reshape(-1,4):
        t=np.degrees(np.arctan2(y2-y1,x2-x1))
        t=(t+45)%90-45   # fold to [-45,45): grid-ish
        a.append(t)
    a=np.array(a); h,b=np.histogram(a,bins=180,range=(-45,45)); k=np.argmax(h)
    return (b[k]+b[k+1])/2, len(a)
for rng in [(300,372,12),(375,460,17),(240,294,9),(770,811,8),(830,920,15),(982,1060,13),(0,40,5)]:
    print(rng, [ (n, None if ang(n) is None else round(ang(n)[0],1)) for n in range(rng[0],rng[1]+1,rng[2])])
