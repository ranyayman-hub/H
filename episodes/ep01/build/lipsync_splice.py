"""Put the lip-synced segments build/lipsync/out/NNN.mp4 back into the master at
exactly the time they were cut from (line start - PAD), keeping the master's
mixed audio. Writes the publish file Hawadeet-World-EP01-Nour-final.mp4."""
import glob, json, os, subprocess
PAD, FPS = 0.25, 30
MASTER = 'build/v3/Hawadeet-World-EP01-Nour-v3.mp4'
OUT = 'build/v3/Hawadeet-World-EP01-Nour-final.mp4'
tl = {l['i']: l for l in json.load(open('build/v3/timeline.json'))['lines']}
segs = sorted(glob.glob('build/lipsync/out/*.mp4'))
inp, fc, prev = ['-i', MASTER], [], '[0:v]'
for k, p in enumerate(segs, 1):
    i = int(os.path.basename(p)[:3])
    s = tl[i]['start'] - PAD
    e = s + tl[i]['dur'] + 2 * PAD
    inp += ['-i', p]
    fc.append(f'[{k}:v]scale=1920:1080:flags=lanczos,fps={FPS},setsar=1,trim=0:{e - s:.3f},'
              f'setpts=PTS-STARTPTS+{s:.3f}/TB[s{k}]')
    fc.append(f"{prev}[s{k}]overlay=eof_action=pass:enable='between(t,{s:.3f},{e - 1 / FPS:.3f})'[v{k}]")
    prev = f'[v{k}]'
fc.append(f'{prev}format=yuv420p[v]')
subprocess.run(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '0:a',
                '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-tune', 'animation', '-r', str(FPS),
                '-c:a', 'copy', '-movflags', '+faststart', OUT], check=True)
print('spliced', len(segs), '->', OUT)
