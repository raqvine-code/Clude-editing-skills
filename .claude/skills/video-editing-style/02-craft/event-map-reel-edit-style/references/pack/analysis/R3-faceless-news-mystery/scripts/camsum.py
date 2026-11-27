import sys, json, numpy as np
D=sys.argv[1]; rows=json.load(open(f'{D}/data/cam.json'))
segs=[("hook lab pullback",6,27),("hook coffin rise",28,43),("hook grave bw",52,89),("crowd rise",91,125),("crowd hold",126,170),("crowd tiltdown",171,194),
("datecard",202,258),("lab2 enter",262,280),("lab2 hold",281,322),("lab2->paper pullback",323,344),("paper1 hold",350,400),("paper1 exit",401,438),
("blueprint",441,512),("wood/nbc enter",515,545),("nbc hold A",546,574),("nbc hold B",576,640),("tv pullback",645,660),("tv hold",661,705),("tv exit",706,711),
("wall photos in",726,745),("wall hold",746,799),("wall exit",800,824),("wordstack",826,874),("press enter",886,900),("press hold",901,962),("press exit",963,969),
("bw closeup in",970,978),("bw closeup hold",979,1020),("redroom",1036,1062),("keyhole hold",1069,1099),("keyhole exit",1100,1109),
("cta words",1124,1166),("cta computer hold",1186,1206),("cta computer end",1215,1277)]
print(f"{'segment':24s} {'frames':>10s} {'n':>4s} {'scale%/s':>9s} {'cum_scale':>9s} {'rot°/s':>7s} {'cum_rot°':>8s} {'tx px/s@1080':>12s} {'ty px/s@1080':>12s} {'cum_ty@1080':>11s}")
for nm,a,b in segs:
    r=[x for x in rows if a<=x['f']<=b and x['s'] is not None]
    if len(r)<3: print(f"{nm:24s} {a}-{b}: insufficient matches ({len(r)})"); continue
    s=np.array([x['s'] for x in r]); rot=np.array([x['rot'] for x in r]); tx=np.array([x['tx'] for x in r]); ty=np.array([x['ty'] for x in r])
    cs=float(np.prod(s)); n=len(r); dur=n/30
    print(f"{nm:24s} {a:5d}-{b:<5d} {n:4d} {(np.median(s)-1)*100*30:9.2f} {cs:9.3f} {np.median(rot)*30:7.2f} {rot.sum():8.2f} {np.median(tx)*30*3:12.1f} {np.median(ty)*30*3:12.1f} {ty.sum()*3:11.1f}")
