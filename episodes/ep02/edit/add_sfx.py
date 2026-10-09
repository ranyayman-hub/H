"""Mix the EP02 SFX (voice/sfx/NNN.mp3) into EP02-flow-v5.mp4 at the cues from sfx_cues.py -> EP02-flow-v6.mp4."""
import json, subprocess
cues = json.load(open('build/sfx_cues.json'))
cmd = ['ffmpeg','-v','error','-y','-i','EP02-flow-v5.mp4']
fc = []
for k,(line,at) in enumerate(sorted(cues.items(), key=lambda x: x[1])):
    cmd += ['-i', f'../voice/sfx/{int(line):03d}.mp3']
    ms = int(at*1000)
    fc.append(f'[{k+1}:a]aresample=44100,aformat=channel_layouts=stereo,loudnorm=I=-25:TP=-4,aresample=44100,'
              f'adelay={ms}|{ms}[s{k}]')
n = len(cues)
fc.append('[0:a]' + ''.join(f'[s{k}]' for k in range(n)) + f'amix=inputs={n+1}:normalize=0:duration=first,alimiter=limit=0.89[a]')
cmd += ['-filter_complex', ';'.join(fc), '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','160k','-movflags','+faststart','EP02-flow-v6.mp4']
subprocess.run(cmd, check=True)
