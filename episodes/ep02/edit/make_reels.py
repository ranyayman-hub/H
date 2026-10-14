"""Full-screen 9:16 reels from EP02-flow-v6.mp4: per-shot crop window + overlay (social/ov-*.html rendered to PNG)."""
import subprocess, sys
OV = sys.argv[1] if len(sys.argv) > 1 else '.'   # folder with the rendered ov-*.png
# (start, end, crop_x) in the v6 timeline; crop is 405x720 out of 1280x720
REELS = {
    'candy': [(116.63,119.64,500),(119.64,126.0,437),(126.0,130.85,400),(130.85,136.83,650),
              (136.83,141.19,437),(141.19,146.15,620),(146.15,149.21,437)],
    'tummy': [(219.53,224.5,437),(224.5,229.06,437),(229.06,232.34,800),(232.34,237.99,437),
              (237.99,241.19,800),(250.19,258.55,400)],
    # riddle: the lantern reads it, Nour thinks, the lantern asks the kids; cut before Nour answers
    'riddle': [(329.56,337.64,648),(337.64,345.54,455)],
    'jelly': [(308.44,317.6,298)],
    # butterflies: Nour counts, the lantern asks the kids; crop_x None = full frame over a blurred fill
    'butterflies': [(200.8,207.16,None),(207.16,211.32,None)],
    # baskota: the gingerbread guide says hello, Nour is shocked, he asks who the star is
    'baskota': [(149.0,163.3,None)],
}
HOLD = {'baskota': 0.6, 'riddle': 1.2, 'jelly': 0.8, 'butterflies': 1.2}   # seconds to freeze the last frame at the end
only = sys.argv[2:]
for name, segs in REELS.items():
    if only and name not in only: continue
    cmd = ['ffmpeg','-v','error','-y']
    fc = []
    for k,(a,b,x) in enumerate(segs):
        cmd += ['-ss',f'{a}','-t',f'{b-a:.2f}','-i','EP02-flow-v6.mp4']
        if x is None:
            fc.append(f'[{k}:v]split[f{k}][b{k}];[b{k}]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.12[bb{k}];'
                      f'[f{k}]scale=1080:-2:flags=lanczos[ff{k}];[bb{k}][ff{k}]overlay=0:(H-h)/2-90,setsar=1,fps=30[v{k}];[{k}:a]aresample=44100[a{k}]')
        else:
            fc.append(f'[{k}:v]crop=405:720:{x}:0,scale=1080:1920:flags=lanczos,setsar=1,fps=30[v{k}];[{k}:a]aresample=44100[a{k}]')
    n = len(segs)
    cmd += ['-loop','1','-i',f'{OV}/ov-{name}.png']
    fc.append(''.join(f'[v{k}][a{k}]' for k in range(n)) + f'concat=n={n}:v=1:a=1[cv][ca]')
    hold=HOLD.get(name,0)
    fc.append(f'[cv]tpad=stop_mode=clone:stop_duration={hold}[cvh];[ca]apad=pad_dur={hold}[cah]')
    fc.append(f'[cvh][{n}:v]overlay=0:0:shortest=1,format=yuv420p[v];[cah]afade=t=out:st={sum(b-a for a,b,_ in segs)+hold-0.6:.2f}:d=0.6[a]')
    cmd += ['-filter_complex',';'.join(fc),'-map','[v]','-map','[a]','-c:v','libx264','-crf','20','-preset','medium',
            '-c:a','aac','-b:a','160k','-movflags','+faststart',f'../shorts/EP02-reel-{name}.mp4']
    subprocess.run(cmd, check=True)
