"""Episode 1 on the user's 52 animated clips, with the final voices.

Video: intro (7 s) dissolving into clips 01..52 joined with hard cuts (each clip
ends on the frame the next one starts with). Ghost dissolves listed in CUTS are
cut out. Every clip is split into its two halves; a half belongs to the scene of
the shot it shows and is slowed (frame-interpolated) when that scene's dialogue
needs more time than its picture, up to MAX_SLOW.

Audio: lines from voice/final, SFX, the music bed ducked under speech, the intro
sting; loudnorm to -14 LUFS.

Outputs build/v3/: master 1080p mp4, 480p preview, timeline.json (every line with
its global time and the clip part it plays over, for lip-sync), ep01-ar.srt."""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, 'voice'); sys.path.insert(0, 'build')
from lines import L
from plan_v3 import CLIPS, CUTS, SCENE, dur

FPS, SR = 30, 48000
MAX_SLOW = 1.5
LEAD, TAIL, GAP_MIN, GAP_MAX = 0.7, 0.9, 0.6, 2.0
INTRO, XF = 'build/intro-final.mp4', 1.0
OUT = 'build/v3'
os.makedirs(f'{OUT}/parts', exist_ok=True)

# ---- clip halves ----
parts = []
for k, (s, e) in CLIPS.items():
    d = dur(f'anim/{k:02d}.mp4')
    if k in CUTS:
        a, b = CUTS[k]
        halves = [(0, a, s), (b, d, e)]
    else:
        halves = [(0, d / 2, s), (d / 2, d, e)]
    for i, (t0, t1, shot) in enumerate(halves):
        parts.append(dict(clip=k, half=i, t0=round(t0, 3), t1=round(t1, 3), shot=shot, scene=SCENE(shot)))

# ---- per-scene dialogue need and slow factor ----
lines = []
for i, (sc, sp, text) in enumerate(L):
    p = f'voice/sfx/{i:03d}.mp3' if sp == 'SFX' else f'voice/final/{i:03d}.mp3'
    lines.append(dict(i=i, scene=sc, speaker=sp, text=text, path=p, dur=round(dur(p), 3)))
pic = {}
for p in parts:
    pic[p['scene']] = pic.get(p['scene'], 0) + p['t1'] - p['t0']
factor = {}
for sc in pic:
    ls = [l for l in lines if l['scene'] == sc]
    need = sum(min(l['dur'], 1.8) if l['speaker'] == 'SFX' else l['dur'] for l in ls) + GAP_MIN * max(len(ls) - 1, 0) + LEAD + TAIL
    f = need / pic[sc]
    factor[sc] = 1.0 if f < 1.05 else min(f, MAX_SLOW)

# ---- video timeline ----
t = INTRO_LEN = dur(INTRO) - XF
scene_win = {}
for p in parts:
    p['f'] = factor[p['scene']]
    p['len'] = (p['t1'] - p['t0']) * p['f']
    p['start'] = round(t, 3)
    t += p['len']
    w = scene_win.setdefault(p['scene'], [p['start'], 0])
    w[1] = round(t, 3)
video_end = t

# ---- place lines inside their scene windows ----
clock = INTRO_LEN
for sc in sorted(scene_win):
    S, E = scene_win[sc]
    ls = [l for l in lines if l['scene'] == sc]
    hold = [min(l['dur'], 1.8) if l['speaker'] == 'SFX' else l['dur'] for l in ls]
    room = E - S - LEAD - TAIL - sum(hold)
    gap = min(GAP_MAX, max(GAP_MIN, room / max(len(ls) - 1, 1))) if len(ls) > 1 else 0
    lead = LEAD + max(0, min(1.5, room - gap * (len(ls) - 1)) / 2) if room > 0 else LEAD
    cur = max(S + lead, clock)
    for l, h in zip(ls, hold):
        l['start'] = round(cur, 3)
        cur += h + gap
    clock = cur - gap + 0.5
total = max(video_end, clock + 2.5)

# ---- render parts (parallel) ----
def render(p):
    out = f"{OUT}/parts/{p['clip']:02d}-{p['half']}.mp4"
    if os.path.exists(out) and abs(dur(out) - p['len']) < 0.1:
        return out
    vf = f"trim={p['t0']}:{p['t1']},setpts=(PTS-STARTPTS)*{p['f']:.4f},scale=1280:720,setsar=1"
    vf += f",minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:vsbmc=1" if p['f'] > 1.0 else f",fps={FPS}"
    vf += ",scale=1920:1080:flags=lanczos"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f"anim/{p['clip']:02d}.mp4", '-vf', vf, '-an',
                    '-c:v', 'libx264', '-preset', 'fast', '-crf', '15', '-pix_fmt', 'yuv420p', out], check=True)
    return out

with ThreadPoolExecutor(4) as ex:
    for o in ex.map(render, parts):
        print('part', o, flush=True)
with open(f'{OUT}/parts.txt', 'w') as fh:
    for p in parts:
        fh.write(f"file 'parts/{p['clip']:02d}-{p['half']}.mp4'\n")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{OUT}/parts.txt',
                '-c', 'copy', f'{OUT}/body.mp4'], check=True)

# ---- audio mix ----
def load(path):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()

def level(x, db):
    m = x.mean(1); fr = m[: len(m) // 480 * 480].reshape(-1, 480)
    e = np.sqrt((fr ** 2).mean(1) + 1e-12); act = e[e > e.max() * 0.1]
    return x * (10 ** (db / 20) / (np.sqrt((act ** 2).mean()) if len(act) else 1e-3))

n = int(total * SR) + SR
voice = np.zeros((n, 2), np.float32); active = np.zeros(n, np.float32)
for l in lines:
    a = level(load(l['path']), -26 if l['speaker'] == 'SFX' else -19)
    s0 = int(l['start'] * SR)
    voice[s0:s0 + len(a)] += a[: n - s0]
    if l['speaker'] != 'SFX':
        active[max(0, s0 - int(0.25 * SR)): s0 + len(a) + int(0.35 * SR)] = 1
music = level(load('audio/music.mp3'), -20)
xf = int(4 * SR); ramp = np.linspace(0, 1, xf, dtype=np.float32)[:, None]
bed = music.copy()
while len(bed) < n:
    bed[-xf:] = bed[-xf:] * (1 - ramp) + music[:xf] * ramp
    bed = np.concatenate([bed, music[xf:]])
m0 = int(INTRO_LEN * SR)
bed = np.concatenate([np.zeros((m0, 2), np.float32), bed])[:n]
win = int(0.5 * SR)
env = np.convolve(active, np.ones(win, np.float32) / win, mode='same')
gain = 10 ** ((-6 - 11 * env) / 20)
gain[m0:m0 + 2 * SR] *= np.linspace(0, 1, 2 * SR)
end = int(total * SR)
gain[end - 6 * SR:end] *= np.linspace(1, 0, 6 * SR); gain[end:] = 0
sting = level(load(INTRO), -20)[: int(dur(INTRO) * SR)]
mix = voice + bed * gain[:, None]
mix[:len(sting)] += sting
mix = mix[:end]
mix *= min(1, 0.98 / max(np.abs(mix).max(), 1e-6))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-',
                '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', str(SR), f'{OUT}/mix.wav'],
               input=mix.astype(np.float32).tobytes(), check=True)

# ---- final video: intro dissolving into the body, hold last frame, fade out ----
hold = max(0, total - video_end)
fc = (f"[0:v]fps={FPS},setsar=1,settb=1/{FPS}[i];"
      f"[1:v]tpad=stop_mode=clone:stop_duration={hold + 0.1:.2f},settb=1/{FPS}[b];"
      f"[i][b]xfade=transition=fade:duration={XF}:offset={INTRO_LEN:.3f},fade=t=out:st={total - 2:.3f}:d=2[v]")
MASTER = f'{OUT}/Hawadeet-World-EP01-Nour-v3.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', INTRO, '-i', f'{OUT}/body.mp4', '-i', f'{OUT}/mix.wav',
                '-filter_complex', fc, '-map', '[v]', '-map', '2:a', '-t', f'{total:.3f}',
                '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-tune', 'animation', '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', MASTER], check=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', MASTER, '-vf', 'scale=854:480', '-c:v', 'libx264', '-crf', '30',
                '-preset', 'medium', '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart',
                f'{OUT}/preview-480p.mp4'], check=True)

# ---- timeline + subtitles ----
def where(t):
    for p in parts:
        if p['start'] <= t < p['start'] + p['len']:
            return dict(clip=p['clip'], half=p['half'], shot=p['shot'],
                        clip_time=round(p['t0'] + (t - p['start']) / p['f'], 2), slow=round(p['f'], 2))
    return None

for l in lines:
    l['on'] = where(l['start'])
json.dump(dict(total=round(total, 2), intro=INTRO_LEN, factor=factor, scene_window=scene_win,
               parts=parts, lines=[{k: v for k, v in l.items() if k != 'path'} for l in lines]),
          open(f'{OUT}/timeline.json', 'w'), ensure_ascii=False, indent=1)
NAMES = dict(nour='نور', fanoos='الفانوس', lumaa='لُمعة', mama='ماما', queen='الملكة', ogre='الغول')
ts = lambda x: f'{int(x//3600):02d}:{int(x//60%60):02d}:{int(x%60):02d},{int(round(x*1000))%1000:03d}'
with open(f'{OUT}/ep01-ar.srt', 'w') as fh:
    k = 0
    for l in lines:
        if l['speaker'] == 'SFX':
            continue
        k += 1
        text = re.sub(r'\[[^\]]*\]\s*', '', l['text']).strip()
        fh.write(f"{k}\n{ts(l['start'])} --> {ts(l['start'] + l['dur'])}\n{NAMES[l['speaker']]}: {text}\n\n")
print(f'done total={total:.1f}s ({total/60:.2f} min)')
