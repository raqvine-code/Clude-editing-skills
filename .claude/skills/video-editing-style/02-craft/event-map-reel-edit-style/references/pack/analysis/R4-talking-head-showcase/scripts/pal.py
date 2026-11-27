import cv2, numpy as np, sys
R=sys.argv[1]
ed=lambda n: cv2.imread(R+'/ed/%04d.jpg'%n)
hx=lambda v:'#%02x%02x%02x'%(int(v[2]),int(v[1]),int(v[0]))
def km(f,k=5,box=None):
    e=ed(f)
    if box: y0,y1,x0,x1=box; e=e[y0:y1,x0:x1]
    Z=e.reshape(-1,3).astype(np.float32)
    _,lab,c=cv2.kmeans(Z,k,None,(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,1.0),3,cv2.KMEANS_PP_CENTERS)
    n=np.bincount(lab.ravel(),minlength=k)/len(lab); o=np.argsort(-n)
    return ' '.join('%s:%d%%'%(hx(c[i]),round(100*n[i])) for i in o)
for f,lab,box in [(80,'phone UI',None),(240,'brain grey stage',None),(290,'brain red stage',None),(290,'brain bg top-right',(100,200,330,390)),(400,'search bar',(235,265,40,380)),(600,'pedestals',None),(890,'chess',None),(774,'light leak',None),(778,'flash',None),(108,'leak f108',None),(110,'leak f110',None),(2,'invert f2',None),(928,'exp flash f928',None),(190,'REALTOR title',(0,70,0,392))]:
    print(f,lab,km(f,5,box))
# glow frame: brightest saturated orange in f20 top region
e=ed(20); hsv=cv2.cvtColor(e,cv2.COLOR_BGR2HSV)
m=(hsv[...,1]>150)&(hsv[...,2]>200)&(hsv[...,0]<25); m[400:]=False
ys,xs=np.where(m); print('glow frame px bbox x',xs.min(),xs.max(),'y',ys.min(),ys.max(),'colour p50',hx(np.median(e[m],0)),'p90',hx(np.percentile(e[m],90,0)))
