import cv2, numpy as np, sys
R=sys.argv[1]
ed=lambda n: cv2.imread(R+'/ed/%04d.jpg'%n)
hx=lambda v:'#%02x%02x%02x'%(int(v[2]),int(v[1]),int(v[0]))
def kw(f,y0,y1,x0,x1,kind='orange'):
    e=ed(f)[y0:y1,x0:x1]; hsv=cv2.cvtColor(e,cv2.COLOR_BGR2HSV).astype(int)
    H,S,V=hsv[...,0],hsv[...,1],hsv[...,2]
    if kind=='orange': m=(H>=8)&(H<=32)&(S>110)&(V>160)
    elif kind=='red': m=((H<=8)|(H>=168))&(S>150)&(V>100)
    else: m=(e.min(2)>200)
    rows=np.where(m.sum(1)>2)[0]; a,b=rows.min(),rows.max(); h=b-a+1
    t=e[a:a+h//4][m[a:a+h//4]]; bt=e[b-h//4:b+1][m[b-h//4:b+1]]; mid=e[a+h//3:b-h//3][m[a+h//3:b-h//3]]
    top=np.percentile(t,70,axis=0) if len(t) else [0,0,0]
    return 'rows %d-%d top %s mid %s bottom %s brightest %s'%(y0+a,y0+b,hx(np.median(t,0)),hx(np.median(mid,0)),hx(np.median(bt,0)),hx(np.percentile(e[m],90,axis=0)))
for name,args in [('AGENTS f20',(20,411,455,60,330)),('Honestly f125',(125,425,453,110,290)),('ASKING f212',(212,418,460,90,300)),('CHATGPT f345',(345,427,452,190,350)),('AGENT f675',(675,442,473,200,340)),('FALLING f720',(720,420,455,140,325)),('POSITIONING f1000',(1000,429,449,105,325)),('MILES AHEAD f1060',(1060,434,457,105,330)),('PULLING RESULTS f448',(448,427,453,80,352))]:
    print(name, kw(*args))
for name,args in [('WORSE f765',(765,425,468,118,290,'red'))]:
    print(name, kw(*args))
# white small text brightest
for f,(y0,y1,x0,x1) in {345:(405,421,110,295),675:(418,435,90,300),965:(402,421,130,280)}.items():
    e=ed(f)[y0:y1,x0:x1]; m=e.min(2)>180; print('small white f%d p95 %s'%(f,hx(np.percentile(e[m],95,axis=0))))
def at(f,y,x,r=3): e=ed(f); return hx(e[y-r:y+r+1,x-r:x+r+1].reshape(-1,3).mean(0))
print('glow frame edge f20', [at(20,y,x,1) for (y,x) in [(115,60),(115,200),(370,200)]])
