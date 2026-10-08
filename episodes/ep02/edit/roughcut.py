"""Build EP02 rough cut: voices + lip-sync clips + Ken Burns stills. usage: python3 roughcut.py"""
import subprocess, sys, os
EP=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, f'{EP}/voice'); import lines
L=lines.L
GAP, SCGAP, SFX = 0.45, 1.2, 1.0
W,H,FPS = 1280,720,25
# scene -> still shots used when no lip-sync line is on screen
STILLS={1:['03-0','03-2'],2:['02-1','02-4'],3:['03-1'],4:['04-1'],5:['05-1','05-3','05-4'],6:['06-3'],7:['07-1','07-2'],
 8:['08-1'],9:['09-1'],10:['10-2','10-1'],11:['11-1'],12:['12-1'],13:['13-1','13-4'],14:['14-1','14-3'],15:['15-1','15-2'],
 16:['16-1'],17:['17-1','17-2'],18:['17-2']}
LS={5:'02-2-nour',8:'02-3-mama',15:'03-2-lantern',17:'03-3-lumaa',18:'03-4-nour',23:'04-2-lumaa',26:'05-2-nour',32:'06-1-baskota',
 33:'06-2-nour',44:'07-3-lantern',47:'08-2-nour',49:'08-3-lumaa',55:'09-2-nour',57:'10-1-baskota',60:'10-3-lantern',65:'11-2-nour',
 73:'13-2-lantern',76:'13-3-nour',84:'14-2-nour',87:'15-1-baskota',88:'15-2-nour'}
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
def img(s):
    for ext in ('jpg','png'):
        p=f'{EP}/images/{s}.{ext}'
        if os.path.exists(p): return p
OUT=f'{EP}/edit/build'; os.makedirs(OUT,exist_ok=True)
# 1) timeline of segments: (kind, src, seconds) and audio pieces
segs=[]; aud=[]; prev=None; rot={}
for i,(s,sp,tx) in enumerate(L):
    if prev is not None:
        g = SCGAP if s!=prev else GAP
        aud.append(('sil',g)); segs[-1][2]+=g
    if sp=='SFX': d=SFX; aud.append(('sil',d))
    else:
        p=f'{EP}/voice/takes/{i:03d}.mp3'; d=dur(p); aud.append(('file',p))
    if i in LS: segs.append(['ls',f'{EP}/lipsync/{LS[i]}.mp4',d])
    else:
        st=STILLS[s]; k=rot.get(s,0); rot[s]=k+1
        src=img(st[k%len(st)])
        if segs and segs[-1][0]=='img' and segs[-1][1]==src and s==prev: segs[-1][2]+=d
        else: segs.append(['img',src,d])
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
    else:
        vf=f"scale={W}:{H},fps={FPS},tpad=stop_mode=clone:stop_duration=30,format=yuv420p"
        cmd=['ffmpeg','-v','error','-y','-i',src,'-an','-t',f'{d:.3f}','-vf',vf]
    subprocess.run(cmd+['-c:v','libx264','-preset','veryfast','-crf','23',o],check=True); vparts.append(o)
open(f'{OUT}/v.txt','w').write(''.join(f"file '{p}'\n" for p in vparts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{OUT}/v.txt','-i',f'{OUT}/voice.wav','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',f'{EP}/edit/EP02-roughcut-v1.mp4'],check=True)
print('segments',len(segs),'lipsync',sum(1 for s in segs if s[0]=='ls'),'seconds',round(sum(s[2] for s in segs),1))
