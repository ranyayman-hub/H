"""Mix the EP03 SFX (voice/sfx/NNN.mp3) into EP03-flow-v3.mp4 -> EP03-flow-v4.mp4.
Cue times come from the segment order in build/asm/list.txt (written by assemble.py) + the 6 s logo intro."""
import os, re, subprocess
ED = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(ED)
SFX, NORM = f'{EP}/voice/sfx', f'{ED}/build/asm/norm'
dur = lambda p: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
OFFSET = 6.0
segs = [l.split("'")[1] for l in open(f'{ED}/build/asm/list.txt')]
start, t = {}, 0.0
for p in segs:
    start[re.search(r's\d+-(C\d+)', p).group(1)] = t; t += dur(p)
after = lambda clip, line, at: at + dur(f'{NORM}/{line:03d}.wav') + 0.1   # just after a spoken line ends
# (sfx file, clip, seconds into clip, max length)
CUES = [
 ('000', 'C01', 0.0, 4), ('018', 'C16', after('C16', 17, .2), 3), ('019', 'C17', 0.2, 3), ('022', 'C19', 0.0, 2),
 ('027', 'C23', 0.0, 3), ('041', 'C34', 0.0, 3), ('053', 'C44', after('C44', 52, 0), 2), ('078', 'C68', 0.0, 2),
 ('092', 'C81', after('C81', 91, .3), 3.5),
 ('097', 'C86', 0.3, 3), ('105', 'C86', 2.4, 3), ('078', 'C86', 4.3, 2.5),   # fire puff -> crystals light up
 ('105', 'C94', 0.0, 3), ('108', 'C96', 0.0, 2), ('121', 'C106', 8.6, 2.5), ('124', 'C110', 2.8, 1.2),
]
cmd = ['ffmpeg','-v','error','-y','-i',f'{ED}/EP03-flow-v3.mp4']; fc = []
for k, (f, clip, at, mx) in enumerate(CUES):
    cmd += ['-i', f'{SFX}/{f}.mp3']
    ms = int((OFFSET + start[clip] + at) * 1000)
    fc.append(f'[{k+1}:a]aresample=44100,aformat=channel_layouts=stereo,atrim=0:{mx},afade=t=out:st={max(mx-0.4,0)}:d=0.4,'
              f'loudnorm=I=-24:TP=-4,aresample=44100,adelay={ms}|{ms}[s{k}]')
    print(f, clip, round((OFFSET + start[clip] + at), 2))
n = len(CUES)
fc.append('[0:a]' + ''.join(f'[s{k}]' for k in range(n)) + f'amix=inputs={n+1}:normalize=0:duration=first,alimiter=limit=0.89[a]')
cmd += ['-filter_complex', ';'.join(fc), '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',f'{ED}/EP03-flow-v4.mp4']
subprocess.run(cmd, check=True)
