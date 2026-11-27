import sys, json, numpy as np, cv2
D=sys.argv[1]
cap=cv2.VideoCapture(f'{D}/src/reel.mp4')
def bbox(m):
    ys,xs=np.where(m)
    if len(xs)<20: return None
    return (int(xs.min()),int(xs.max()),int(ys.min()),int(ys.max()),int(len(xs)))
out={}
def put(k,f,v): out.setdefault(k,[]).append((f,v))
f=0
while True:
    ok,im=cap.read()
    if not ok: break
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV); H,S_,V=hsv[...,0].astype(int),hsv[...,1].astype(int),hsv[...,2].astype(int)
    g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    if 8<=f<=49:   # white coat: bright low-sat within central columns
        m=(V>215)&(S_<45); m[:, :200]=False; m[:, 520:]=False
        m=cv2.morphologyEx(m.astype(np.uint8),cv2.MORPH_OPEN,np.ones((7,7),np.uint8))
        n,lab,st,_=cv2.connectedComponentsWithStats(m,8)
        if n>1:
            k=1+np.argmax(st[1:,4]); put('coat',f,tuple(int(v) for v in st[k]))
    if 26<=f<=46:  # coffin brown: hue 8-22, sat>80, V 60-200
        m=(H>=6)&(H<=24)&(S_>70)&(V>50)&(V<210); m[:, :150]=False; m[:, 570:]=False
        b=bbox(m); put('coffin',f,b)
    if 52<=f<=89:  # grave bw: bright coffin lid
        m=(V>150); b=bbox(m); put('gravebright',f,b)
    if 195<=f<=262: # date card: white text and red underline
        m=(V>170)&(S_<60); m[1000:,:]=False
        put('datetext',f,bbox(m))
        r=(S_>120)&(V>110)&((H<8)|(H>172)); put('dateline',f,bbox(r))
    if 268<=f<=345: # red label / red frame
        r=(S_>150)&(V>130)&((H<7)|(H>173)); put('red',f,bbox(r))
    if 345<=f<=440: # yellow highlight
        y=(H>=24)&(H<=34)&(S_>110)&(V>170); put('yellow',f,bbox(y))
    if 530<=f<=645:
        gr=(H>=45)&(H<=75)&(S_>130)&(V>150); put('green',f,bbox(gr))
        r=(S_>150)&(V>150)&((H<6)|(H>174)); r[:, 400:]=False; r[700:,:]=False; put('redcircle',f,bbox(r))
    if 440<=f<=514: # blueprint white word
        m=(V>225)&(S_<40); put('bpword',f,bbox(m))
    if 720<=f<=830:
        put('wall_luma',f,float(g.mean()))
        m=(V>150)&(S_<60); put('photos',f,bbox(m))
    if 822<=f<=890:
        m=(V>190)&(S_<50); m=m.astype(np.uint8)
        rows=np.where(m.sum(axis=1)>3)[0]
        # group rows into text lines
        lines=[]
        for y in rows:
            if lines and y-lines[-1][1]<=6: lines[-1][1]=int(y)
            else: lines.append([int(y),int(y)])
        lw=[]
        for a,b in lines:
            xs=np.where(m[a:b+1].sum(axis=0)>0)[0]
            lw.append((a,b,int(xs.min()),int(xs.max())))
        put('stack',f,lw)
    if 1018<=f<=1040:
        r=(S_>140)&(V>120)&((H<10)|(H>170)); put('irisred',f,float(r.mean()))
        put('sat',f,float(S_.mean()))
    if 1110<=f<=1170:
        gold=(H>=18)&(H<=28)&(S_>90)&(V>130); red=(S_>150)&(V>100)&((H<6)|(H>174)); blue=(H>=105)&(H<=125)&(S_>120)&(V>120)
        put('cta_gold',f,bbox(gold)); put('cta_red',f,bbox(red)); put('cta_blue',f,bbox(blue))
    if 1195<=f<=1277:
        pur=(H>=118)&(H<=135)&(S_>90)&(V>140); pur[500:,:]=False; put('aefile',f,bbox(pur))
    f+=1
json.dump(out,open(f'{D}/data/meas1.json','w'))
print('frames',f, 'keys',list(out))
