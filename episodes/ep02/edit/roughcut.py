"""Build EP02 rough cut: voices + lip-sync clips + Ken Burns stills. usage: python3 roughcut.py"""
import subprocess, sys, os
EP=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, f'{EP}/voice'); import lines
L=lines.L
GAP, SCGAP, SFX = 0.45, 1.2, 1.0
W,H,FPS = 1280,720,25
# line -> shot: EP02 image id, 'e1:<id>' = EP01 animated clip, list = split the line between shots
SHOT={0:'e1:01-1',1:['e1:16-1','e1:17-1','e1:17-2'],2:['e1:19-1','e1:20-2'],3:'e1:22-1',
 4:'02-1',6:'02-3',7:'02-2',9:'02-2',10:'02-3',11:'02-4',12:'02-4',
 13:'03-0',14:'03-1',16:'03-3',19:'03-3',20:'03-2',21:'03-4',
 22:'04-1',24:'04-1',
 25:'05-1',27:'05-3',28:'05-1',29:'05-4',30:'05-4',31:'05-2',
 34:'06-1',35:'06-3',36:'06-3',37:'06-3',
 38:'07-1',39:'07-1',40:'07-1',41:'07-1',42:'07-2',43:'07-2',45:'07-1',
 46:'08-1',48:'08-1',50:'08-2',51:'08-1',
 52:'09-1',53:'09-1',54:'09-1',56:'09-2',
 58:'10-2',59:'10-1',61:'10-1',
 62:'11-1',63:'11-1',64:'11-1',66:'11-2',
 67:'12-1',68:'12-1',69:'12-1',
 70:'13-1',71:'13-1',72:'13-1',74:'13-3',75:'13-2',77:'13-4',78:'13-4',79:'13-4',80:'13-4',
 81:'14-1',82:'14-1',83:'14-1',85:'14-3',86:'14-3',
 89:'15-2',90:'15-2',
 91:'16-1',92:'16-1',93:'16-1',
 94:'17-1',95:'17-1',96:'17-2',97:'17-2',98:'e1:22-1',99:'e1:22-3'}
LS={5:'02-2-nour',8:'02-3-mama',15:'03-2-lantern',17:'03-3-lumaa',18:'03-4-nour',23:'04-2-lumaa',26:'05-2-nour',32:'06-1-baskota',
 33:'06-2-nour',44:'07-3-lantern',47:'08-2-nour',49:'08-3-lumaa',55:'09-2-nour',57:'10-1-baskota',60:'10-3-lantern',65:'11-2-nour',
 73:'13-2-lantern',76:'13-3-nour',84:'14-2-nour',87:'15-1-baskota',88:'15-2-nour'}
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
E1=os.path.join(os.path.dirname(EP),'ep01','shots3d','clips')
def img(s):
    if s.startswith('e1:'): return f'{E1}/{s[3:]}.mp4'
    for ext in ('jpg','png'):
        p=f'{EP}/images/{s}.{ext}'
        if os.path.exists(p): return p
OUT=f'{EP}/edit/build'; os.makedirs(OUT,exist_ok=True)
# 1) timeline of segments: (kind, src, seconds) and audio pieces
segs=[]; aud=[]; prev=None
for i,(s,sp,tx) in enumerate(L):
    if prev is not None:
        g = SCGAP if s!=prev else GAP
        aud.append(('sil',g)); segs[-1][2]+=g
    if sp=='SFX': d=SFX; aud.append(('sil',d))
    else:
        p=f'{EP}/voice/takes/{i:03d}.mp3'; d=dur(p); aud.append(('file',p))
    if i in LS: segs.append(['ls',f'{EP}/lipsync/{LS[i]}.mp4',d]); prev=s; continue
    shots=SHOT[i] if isinstance(SHOT[i],list) else [SHOT[i]]
    for sh in shots:
        src=img(sh); k='vid' if src.endswith('.mp4') else 'img'; dd=d/len(shots)
        if segs and segs[-1][1]==src: segs[-1][2]+=dd
        else: segs.append([k,src,dd])
    prev=s
# 2) audio master
parts=[]
for n,(k,v) in enumerate(aud):
    o=f'{OUT}/a{n:04d}.wav'
    if k=='sil': subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=44100:cl=mono','-t',f'{v:.3f}',o],check=True)
    else: subprocess.run(['ffmpeg','-v','error','-y','-i',v,'-ar','44100','-ac','1',o],check=True)
    parts.append(o)
open(f'{OUT}/a.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{OUT}/a.txt','-c:a','pcm_s16le',f'{OUT}/voice.wav'],check=True)
# 3) video segments
vparts=[]
for n,(k,src,d) in enumerate(segs):
    o=f'{OUT}/v{n:03d}.mp4'
    if k=='img':
        vf=f"scale={int(W*1.12)}:-2,crop={W}:{H}:'(iw-{W})*t/{d:.3f}':'(ih-{H})/2',fps={FPS},format=yuv420p"
        cmd=['ffmpeg','-v','error','-y','-loop','1','-i',src,'-t',f'{d:.3f}','-vf',vf]
    elif k=='vid':
        vf=f"scale={W}:{H},fps={FPS},format=yuv420p"
        cmd=['ffmpeg','-v','error','-y','-stream_loop','-1','-i',src,'-an','-t',f'{d:.3f}','-vf',vf]
    else:
        vf=f"scale={W}:{H},fps={FPS},tpad=stop_mode=clone:stop_duration=30,format=yuv420p"
        cmd=['ffmpeg','-v','error','-y','-i',src,'-an','-t',f'{d:.3f}','-vf',vf]
    subprocess.run(cmd+['-c:v','libx264','-preset','veryfast','-crf','23',o],check=True); vparts.append(o)
open(f'{OUT}/v.txt','w').write(''.join(f"file '{p}'\n" for p in vparts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{OUT}/v.txt','-i',f'{OUT}/voice.wav','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',f'{EP}/edit/EP02-roughcut-v3.mp4'],check=True)
print('segments',len(segs),'lipsync',sum(1 for s in segs if s[0]=='ls'),'missing',[i for i in range(len(L)) if i not in LS and i not in SHOT],'seconds',round(sum(s[2] for s in segs),1))
