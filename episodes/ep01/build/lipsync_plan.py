"""Which lines need lip-sync, and what it costs (no credits spent).

Runs the timeline part of assemble_v3.py (no rendering), then for every spoken
line grabs three frames (start, middle, end) from the clip parts it plays over
and tiles them into contact sheets build/lipsync/sheet-NN.jpg for review."""
import os, subprocess, json
src = open('build/assemble_v3.py').read().split('# ---- render parts')[0]
src = src.replace("os.makedirs(f'{OUT}/parts', exist_ok=True)", '')
exec(src)
os.makedirs('build/lipsync/f', exist_ok=True)

def at(t):
    for p in parts:
        if p['start'] <= t < p['start'] + p['len']:
            return p['clip'], p['t0'] + (t - p['start']) / p['f']
    p = parts[-1]; return p['clip'], p['t1'] - 0.05

rows = []
D = {k: dur(f'anim/{k:02d}.mp4') for k in CLIPS}
for l in lines:
    if l['speaker'] == 'SFX':
        continue
    imgs = []
    for j, t in enumerate((l['start'] + 0.15, l['start'] + l['dur'] / 2, l['start'] + l['dur'] - 0.15)):
        c, ct = at(t)
        ct = max(0, min(ct, D[c] - 0.2))
        out = f"build/lipsync/f/{l['i']:03d}-{j}.jpg"
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{ct:.2f}', '-i', f'anim/{c:02d}.mp4', '-frames:v', '1',
                        '-vf', f"scale=480:270,drawtext=text='{l['i']:03d} {l['speaker']} c{c}':x=6:y=6:fontsize=22:fontcolor=yellow:box=1:boxcolor=black@0.6",
                        out], check=True)
        imgs.append(out)
    rows.append(dict(i=l['i'], speaker=l['speaker'], dur=l['dur'], start=l['start'], imgs=imgs))
json.dump(rows, open('build/lipsync/lines.json', 'w'), indent=1)
for s in range(0, len(rows), 8):
    chunk = rows[s:s + 8]
    files = [f for r in chunk for f in r['imgs']]
    inp = sum([['-i', f] for f in files], [])
    n = len(chunk)
    fc = ''.join(f'[{k}:v]' for k in range(len(files))) + f'xstack=inputs={len(files)}:layout=' + '|'.join(
        f'{c*480}_{r*270}' for r in range(n) for c in range(3))
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', fc, '-q:v', '4',
                    f'build/lipsync/sheet-{s//8:02d}.jpg'], check=True)
print(len(rows), 'lines', sum(r['dur'] for r in rows), 's')
