"""Cut the lip-sync inputs for the lines marked Y in build/lipsync/lines.json.

For line i: build/lipsync/in/NNN.mp4 is the master's picture (no audio) from
start-PAD to end+PAD, and NNN.mp3 is that line's voice alone, padded with PAD
silence on both sides, so audio and picture have the same length."""
import json, os, subprocess, sys
PAD = 0.25
MASTER = 'build/v3/Hawadeet-World-EP01-Nour-v3.mp4'
tl = {l['i']: l for l in json.load(open('build/v3/timeline.json'))['lines']}
rows = [r for r in json.load(open('build/lipsync/lines.json')) if r['cls'] == 'Y']
only = {int(x) for x in sys.argv[1:]}
os.makedirs('build/lipsync/in', exist_ok=True)
for r in rows:
    i = r['i']
    if only and i not in only:
        continue
    s, d = tl[i]['start'] - PAD, tl[i]['dur'] + 2 * PAD
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{s:.3f}', '-i', MASTER, '-t', f'{d:.3f}', '-an',
                    '-c:v', 'libx264', '-preset', 'fast', '-crf', '16', '-pix_fmt', 'yuv420p',
                    f'build/lipsync/in/{i:03d}.mp4'], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'voice/final/{i:03d}.mp3', '-af',
                    f'adelay={int(PAD*1000)}:all=1,apad,atrim=0:{d:.3f}', '-ar', '44100', '-ac', '1', '-b:a', '192k',
                    f'build/lipsync/in/{i:03d}.mp3'], check=True)
    print(i, round(s, 2), round(d, 2))
