"""7-second channel logo intro (free, no credits).

Background: the logo's own navy gradient extended to 16:9, with twinkling stars,
a warm glow behind the logo and a burst of gold sparkles when it lands.
The logo (radially masked so its square edge disappears) fades and scales in,
breathes, then fades out. Audio: build/intro_sting.mp3 if present.

Outputs build/intro.mp4 and build/intro-preview.mp4 (intro dissolving into clip 01)."""
import os, subprocess
import numpy as np

W, H, FPS, DUR = 1920, 1080, 30, 7.0
N = int(DUR * FPS)
LOGO = '../../../branding/hawadeet-world-logo.png'
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def read_rgb(path, w, h):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'scale={w}:{h}:flags=lanczos',
                                   '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'])
    return np.frombuffer(raw, np.uint8).reshape(h, w, 3).astype(np.float32)


logo = read_rgb(LOGO, 800, 800)
edge = np.median(np.concatenate([logo[:20, :20].reshape(-1, 3), logo[-20:, -20:].reshape(-1, 3),
                                 logo[:20, -20:].reshape(-1, 3), logo[-20:, :20].reshape(-1, 3)]), 0)
inner = np.median(logo[230:270, 330:370].reshape(-1, 3), 0)

# masked logo (RGBA): opaque centre, soft fade before the square's corners
L = 1000
lg = read_rgb(LOGO, L, L)
yy, xx = np.mgrid[0:L, 0:L]
r = np.hypot(xx - L / 2, yy - L / 2) / (L / 2)
alpha = np.clip((0.98 - r) / 0.16, 0, 1)
rgba = np.dstack([lg, alpha * 255]).astype(np.uint8)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{L}x{L}', '-i', '-',
                'logo_masked.png'], input=rgba.tobytes(), check=True)

# background: the logo's own radial colour profile, extended to the full frame
ly, lx = np.mgrid[0:800, 0:800]
lr = np.hypot(lx - 400, ly - 400).astype(int)
lum = logo.mean(2)
prof = np.zeros((lr.max() + 1, 3), np.float32)
for k in range(lr.max() + 1):
    px = logo[lr == k]
    if len(px):
        keep = px[lum[lr == k] <= np.percentile(lum[lr == k], 55)]
        prof[k] = np.median(keep, 0)
for k in range(1, len(prof)):
    if not prof[k].any():
        prof[k] = prof[k - 1]
prof = np.stack([np.convolve(np.pad(prof[:, c], 6, mode='edge'), np.ones(13) / 13, 'valid') for c in range(3)], 1)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
rad = np.hypot(xx - W / 2, yy - (H / 2 - 20)) / (L / 800)
bg = prof[np.clip(rad.astype(int), 0, len(prof) - 1)]
rng = np.random.default_rng(7)
stars = [(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0.8, 2.2), rng.uniform(0, 6.28), rng.uniform(0.6, 1.6))
         for _ in range(140)]
sparks = [(rng.uniform(0, 6.28), rng.uniform(150, 520), rng.uniform(1.5, 3.5), rng.uniform(0, 0.5)) for _ in range(90)]
gold = np.array([255, 214, 120], np.float32)


def blob(img, x, y, rad, color, a):
    x0, x1 = int(max(0, x - rad * 3)), int(min(W, x + rad * 3 + 1))
    y0, y1 = int(max(0, y - rad * 3)), int(min(H, y + rad * 3 + 1))
    if x0 >= x1 or y0 >= y1:
        return
    gy, gx = np.mgrid[y0:y1, x0:x1]
    k = (np.exp(-((gx - x) ** 2 + (gy - y) ** 2) / (2 * rad * rad)) * a)[..., None]
    img[y0:y1, x0:x1] = img[y0:y1, x0:x1] * (1 - k) + color * k


def ease(t):
    t = min(max(t, 0), 1)
    return 1 - (1 - t) ** 3


glow_r = np.hypot(xx - W / 2, yy - H / 2 + 20)[..., None]
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                      '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '14',
                      '-pix_fmt', 'yuv420p', 'intro_bg.mp4'], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS
    img = bg.copy()
    g = 0.55 * ease((t - 0.6) / 1.2) * (1 + 0.08 * np.sin(t * 2.4)) * (1 - ease((t - 5.6) / 1.2))
    img += np.exp(-(glow_r / 430) ** 2) * np.array([70, 50, 20], np.float32) * g
    for x, y, rad, ph, sp in stars:
        a = 0.35 + 0.65 * (0.5 + 0.5 * np.sin(t * sp * 2.2 + ph))
        blob(img, x, y, rad, np.array([255, 250, 235], np.float32), a)
    for ang, dist, rad, delay in sparks:
        k = (t - 1.1 - delay) / 2.2
        if 0 < k < 1:
            rr = 300 + dist * ease(k)
            blob(img, W / 2 + np.cos(ang) * rr, H / 2 - 20 + np.sin(ang) * rr * 0.8, rad, gold,
                 (1 - k) * (0.5 + 0.5 * np.sin(t * 9 + ang * 5)))
    fade = ease(t / 0.8)
    p.stdin.write(np.clip(img * fade, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()

# logo: fade + scale in (0.5-2.0s), gentle breathing, fade out (5.5-6.7s)
scale = "'1000*(0.84+0.16*(1-pow(1-min(max((t-0.5)/1.5,0),1),3))+0.015*sin(t*1.6))'"
fc = (f"[1:v]format=rgba,scale=w={scale}:h=-1:eval=frame,"
      f"fade=t=in:st=0.5:d=1.3:alpha=1,fade=t=out:st=5.5:d=1.2:alpha=1[lg];"
      f"[0:v][lg]overlay=x=(W-w)/2:y=(H-h)/2-20:eval=frame:shortest=1,format=yuv420p[v]")
cmd = ['ffmpeg', '-v', 'error', '-y', '-i', 'intro_bg.mp4', '-loop', '1', '-framerate', str(FPS), '-i', 'logo_masked.png']
amap = []
if os.path.exists('intro_sting.mp3'):
    cmd += ['-i', 'intro_sting.mp3']
    fc += f";[2:a]atrim=0:{DUR},afade=t=out:st={DUR-1.5}:d=1.5,apad=whole_dur={DUR}[a]"
    amap = ['-map', '[a]', '-c:a', 'aac', '-b:a', '192k']
subprocess.run(cmd + ['-filter_complex', fc, '-map', '[v]'] + amap +
               ['-t', str(DUR), '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-r', str(FPS), 'intro.mp4'],
               check=True)

# preview: intro dissolving into the first 4 s of clip 01
pre = ['ffmpeg', '-v', 'error', '-y', '-i', 'intro.mp4', '-i', '../anim/01.mp4', '-filter_complex',
       f"[1:v]scale=1920:1080:flags=lanczos,fps={FPS},setsar=1,trim=0:4,setpts=PTS-STARTPTS,settb=1/{FPS}[c];"
       f"[0:v]fps={FPS},setsar=1,settb=1/{FPS}[i];[i][c]xfade=transition=fade:duration=1:offset={DUR-1}[v]", '-map', '[v]']
if amap:
    pre += ['-map', '0:a']
subprocess.run(pre + ['-c:v', 'libx264', '-crf', '20', '-c:a', 'aac', 'intro-preview.mp4'], check=True)
print('done')
