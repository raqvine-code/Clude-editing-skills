import sys,cv2,numpy as np
D=sys.argv[1]
cap=cv2.VideoCapture(f'{D}/src/reel.mp4')
def fr(n):
    cap.set(cv2.CAP_PROP_POS_FRAMES,n); ok,im=cap.read(); return im
def hx(c): return '#%02X%02X%02X'%(int(c[2]),int(c[1]),int(c[0]))
def samp(n,roi,pred,lab):
    im=fr(n); x0,y0,x1,y1=roi; s=im[y0:y1,x0:x1].reshape(-1,3).astype(int); b,g,r=s[:,0],s[:,1],s[:,2]
    m=pred(r,g,b); p=s[m]
    print(f"f{n} {lab:34s} {hx(np.median(p,0)) if len(p) else 'n/a'}  (n={m.sum()})")
samp(4,(0,500,300,800),lambda r,g,b:(r>200)&(g<80),"red cross glow (hook)")
samp(30,(0,200,720,1000),lambda r,g,b:(r>150)&(g<90)&(b<120),"hospital window red")
samp(30,(0,0,720,200),lambda r,g,b:np.ones_like(r,bool),"storm sky")
samp(85,(0,200,720,1100),lambda r,g,b:(g>r+10)&(g>60),"surgeon scrubs teal")
samp(200,(0,0,720,500),lambda r,g,b:b>r+60,"sky blue")
samp(200,(0,950,720,1280),lambda r,g,b:g>r+30,"grass green")
samp(130,(150,250,550,600),lambda r,g,b:(r>180)&(g<70),"portrait card red")
samp(306,(150,250,620,450),lambda r,g,b:(r<90)&(g<90)&(b<90),"1840s ink")
samp(306,(0,600,720,1280),lambda r,g,b:np.ones_like(r,bool),"grid paper")
samp(440,(0,200,720,1100),lambda r,g,b:(r>110)&(g<60)&(b<70),"graph line red")
samp(440,(0,200,720,1100),lambda r,g,b:(r<45)&(g<45)&(b<45),"slate black")
samp(540,(0,0,720,500),lambda r,g,b:np.ones_like(r,bool),"corridor wall")
samp(540,(0,1000,720,1280),lambda r,g,b:np.ones_like(r,bool),"corridor floor")
samp(745,(0,700,720,1280),lambda r,g,b:g>r+25,"death-rate green fill")
samp(745,(0,350,720,700),lambda r,g,b:(abs(r-g)<12)&(r<120),"slate grey")
samp(800,(0,0,720,300),lambda r,g,b:r>g+20,"wood desk")
samp(890,(0,1000,720,1280),lambda r,g,b:r>g+40,"red cutting mat")
samp(960,(0,300,720,1000),lambda r,g,b:r>g+50,"bacteria red")
samp(1040,(200,200,520,500),lambda r,g,b:np.ones_like(r,bool),"spotlight paper (lit)")
samp(1040,(0,500,120,900),lambda r,g,b:np.ones_like(r,bool),"spotlight shadow")
samp(1105,(60,560,680,700),lambda r,g,b:(r<120)&(g<120)&(b<120),"CTA grey words")
samp(1105,(0,800,720,1200),lambda r,g,b:np.ones_like(r,bool),"CTA paper")
samp(1215,(0,1000,720,1280),lambda r,g,b:np.ones_like(r,bool),"plinth wood")
samp(1215,(60,350,640,750),lambda r,g,b:g>r+60,"laptop UI green")
