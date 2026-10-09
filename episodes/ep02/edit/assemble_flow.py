"""Assemble EP02 from the finished Flow/Gemini/lip-sync clips (flow/final) + recap/ending from roughcut-v3."""
import os, subprocess, sys
EP=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,f'{EP}/voice'); import lines
L=lines.L
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
# time of line i start in roughcut-v3 (same rules as roughcut.py)
t=0; starts=[]; prev=None
for i,(s,sp,tx) in enumerate(L):
    if prev is not None: t+= 1.2 if s!=prev else 0.45
    starts.append(t)
    t+= 1.0 if sp=='SFX' else dur(f'{EP}/voice/takes/{i:03d}.mp3')
    prev=s
end=t
RC=f'{EP}/edit/EP02-roughcut-v3.mp4'
F=f'{EP}/flow/final'
ORDER=['@intro',f'{EP}/flow/02-1-veo-ourvoices.mp4','C02','L02-3','C04','C05','C06','C07',
 'L03-2','C09','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21',
 'C22','C23','C24','C25','C27','C28','C30','C31','C32','C33','C34','C35','C36','C37','C38','C39','C40','C41','C43',
 'C44','C45','C47','C49','C51','C52','C54','C56','C57','C60','C62','C64','C65','C66','C67','C69','C70','C71','@outro']
OUT=f'{EP}/edit/build/asm'; os.makedirs(OUT,exist_ok=True)
GAP=0.35
parts=[]
for n,o in enumerate(ORDER):
    dst=f'{OUT}/p{n:03d}.mp4'
    if o=='@intro': src,ss,tt=RC,0,starts[4]
    elif o=='@outro': src,ss,tt=RC,starts[98],end-starts[98]+0.5
    else:
        src=o if o.startswith('/') else f'{F}/{o}.mp4'; ss=0; tt=dur(src)
    has_a=bool(subprocess.check_output(['ffprobe','-v','error','-select_streams','a','-show_entries','stream=index','-of','csv=p=0',src]).strip())
    cmd=['ffmpeg','-v','error','-y','-ss',str(ss),'-t',f'{tt:.3f}','-i',src]
    if not has_a: cmd+=['-f','lavfi','-t',f'{tt:.3f}','-i','anullsrc=r=44100:cl=stereo']
    gap=0 if o.startswith('@') else GAP
    vf=f'scale=1280:720,fps=25,format=yuv420p,tpad=stop_mode=clone:stop_duration={gap}'
    af=f'aresample=44100,aformat=channel_layouts=stereo,apad=pad_dur={gap}'
    cmd+=['-map','0:v','-map','0:a' if has_a else '1:a','-vf',vf,'-af',af,'-t',f'{tt+gap:.3f}','-c:v','libx264','-crf','20','-preset','veryfast','-c:a','aac','-b:a','160k',dst]
    subprocess.run(cmd,check=True); parts.append(dst)
open(f'{OUT}/list.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
out=f'{EP}/edit/EP02-flow-v2.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{OUT}/list.txt','-c','copy','-movflags','+faststart',out],check=True)
print('clips',len(parts),'seconds',round(dur(out),1))
