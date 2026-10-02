"""Find cross-dissolves inside each animated clip.
A frame inside a dissolve looks like a blend of a frame before and a frame after it,
while those two frames differ a lot. Prints the detected [start, end] per clip."""
import subprocess, sys, json
import numpy as np
FPS = 24

def frames(path):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'fps={FPS},scale=128:72',
                                   '-f', 'rawvideo', '-pix_fmt', 'gray', '-'])
    return np.frombuffer(raw, np.uint8).reshape(-1, 72, 128).astype(np.float32)

out = {}
for k in range(1, 53):
    f = frames(f'anim/{k:02d}.mp4')
    n, d = len(f), 5
    score = np.zeros(n)
    for t in range(d, n - d):
        A, B, C = f[t - d], f[t + d], f[t]
        ab = np.abs(A - B).mean()
        if ab < 18:
            continue
        D = A - B
        a = np.clip(((C - B) * D).sum() / ((D * D).sum() + 1e-6), 0, 1)
        r = np.abs(C - (a * A + (1 - a) * B)).mean()
        mid = min(a, 1 - a)
        score[t] = (ab / (r + 1)) * (mid > 0.2)
    hot = np.where(score > 6)[0]
    if len(hot):
        segs, s, p = [], hot[0], hot[0]
        for t in hot[1:]:
            if t - p > 3:
                segs.append((s, p)); s = t
            p = t
        segs.append((s, p))
        segs = [(round((a - d) / FPS, 2), round((b + d) / FPS, 2), round(float(score[a:b + 1].max()), 1)) for a, b in segs if b - a >= 2]
        if segs:
            out[k] = segs
    print(k, out.get(k, ''), flush=True)
json.dump(out, open('build/dissolves.json', 'w'))
