"""Rough animatic: each Flow clip from flow/FLOW-ALL.md shown as its still image (slow push-in) with our voice lines; missing images get a dark placeholder."""
import os, re, subprocess, sys
EP=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B=f'{EP}/edit/build/animatic'; os.makedirs(B,exist_ok=True)
sys.path.insert(0,f'{EP}/voice'); import lines; L=lines.L
txt=open(f'{EP}/flow/FLOW-ALL.md').read()
clips=[]
for blk in re.split(r'\n## ',txt)[1:]:
    m=re.match(r'(C\d+): صورة (\S+)',blk)
    clips.append((m.group(1),m.group(2),[int(x) for x in re.findall(r'- `(\d{3})`',blk)]))
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
parts=[]
for cid,img,ls in clips:
    out=f'{B}/{cid}.mp4'; parts.append(out)
    if os.path.exists(out): continue
    aud=[]; 
    for i in ls:
        f=f'{EP}/voice/takes/{i:03d}.mp3'
        aud.append(f if L[i][1]!='SFX' and os.path.exists(f) else None)
    inp=[];flt='';n=0
    for a in aud:
        if a: inp+=['-i',a]
        else: inp+=['-f','lavfi','-t','1','-i','anullsrc=r=44100:cl=mono']
        flt+=f'[{n}:a]aresample=44100,aformat=channel_layouts=mono,apad=pad_dur=0.35[a{n}];'; n+=1
    flt+=''.join(f'[a{k}]' for k in range(n))+f'concat=n={n}:v=0:a=1[aout]'
    wav=f'{B}/{cid}.wav'
    subprocess.run(['ffmpeg','-y','-v','error',*inp,'-filter_complex',flt,'-map','[aout]',wav],check=True)
    d=dur(wav)+0.4
    ip=next((f'{EP}/images/{img}.{e}' for e in ('jpg','png') if os.path.exists(f'{EP}/images/{img}.{e}')),None)
    vin=['-loop','1','-i',ip] if ip else ['-f','lavfi','-i','color=c=0x101020:s=1280x720']
    fr=int(d*25)
    vf=(f"scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,zoompan=z='1+0.04*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1280x720:fps=25" if ip else 'null')
    if not ip: vf=f"drawtext=text='{cid} {img}':fontcolor=white:fontsize=48:x=(w-tw)/2:y=(h-th)/2"
    subprocess.run(['ffmpeg','-y','-v','error',*vin,'-i',wav,'-t',f'{d:.2f}','-vf',vf,'-r','25','-c:v','libx264','-preset','veryfast','-crf','26','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-shortest',out],check=True)
open(f'{B}/list.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',f'{B}/list.txt','-c','copy',f'{EP}/edit/EP03-animatic.mp4'],check=True)
print(len(clips),'clips', round(dur(f'{EP}/edit/EP03-animatic.mp4'),1),'s')
