"""How much a lip-sync output differs from its input: mean pixel change and where."""
import numpy as np, subprocess, sys
def fr(p):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', p, '-vf', 'scale=192:108,fps=30', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'])
    return np.frombuffer(raw, np.uint8).reshape(-1, 108, 192).astype(float)
for n in sys.argv[1:]:
    a, b = fr(f'build/lipsync/in/{n}.mp4'), fr(f'build/lipsync/out/{n}.mp4'); m = min(len(a), len(b))
    d = np.abs(a[:m] - b[:m]); sp = d.mean(0); top = np.sort(sp.ravel())[-40:].mean()
    ys, xs = np.unravel_index(np.argsort(sp.ravel())[-40:], sp.shape)
    print(n, 'mean', d.mean().round(2), 'hot', top.round(1), 'y', ys.min(), ys.max(), 'x', xs.min(), xs.max())
