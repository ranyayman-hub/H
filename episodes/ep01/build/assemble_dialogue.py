"""Build the publish-ready dialogue episode (no narrator).

Timeline: each scene opens with a short music lead, then its lines and SFX play in
order with small gaps, then a short tail. Scene length is never less than
MIN_SHOT seconds per shot. The scene's shots split that length evenly, and every
animated clip ping-pongs to fill its slot.

Audio is mixed in numpy: each line is levelled, the music bed loops with
crossfades and ducks under speech, then ffmpeg applies loudnorm for YouTube (-14 LUFS).

Outputs:
  build/timeline.json    start time of every line
  build/ep01-ar.srt      Arabic subtitles
  build/mix.wav          final audio mix
  Hawadeet-World-EP01-Nour-and-the-Magic-Lantern.mp4"""
import contextlib, io, json, os, re, subprocess, sys
import numpy as np

sys.path.insert(0, 'voice')
from lines import L
with contextlib.redirect_stdout(io.StringIO()):
    sys.path.insert(0, 'art3d')
    from shots import S

SR, FPS, XF = 48000, 30, 0.6
LEAD, TAIL = 1.4, 2.0
GAP_SAME, GAP_SWITCH = 0.5, 0.8
SFX_HOLD = 1.8          # time an SFX holds the line before the next item starts
MIN_SHOT = 7.5
EXTRA = {1: (5.0, 0), 7: (0, 5.0), 13: (0, 4.0), 15: (0, 2.0), 17: (0, 2.0), 22: (0, 9.0)}  # (lead, tail)
OUT = 'Hawadeet-World-EP01-Nour-and-the-Magic-Lantern.mp4'


def load(path):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le',
                                   '-ac', '2', '-ar', str(SR), '-'])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def level(x, rms_db):
    mono = x.mean(1)
    frames = mono[: len(mono) // 480 * 480].reshape(-1, 480)
    e = np.sqrt((frames ** 2).mean(1) + 1e-12)
    active = e[e > e.max() * 0.1]
    rms = np.sqrt((active ** 2).mean()) if len(active) else 1e-3
    return x * (10 ** (rms_db / 20) / rms)


shots_by_scene = {}
for sid, *_ in S:
    shots_by_scene.setdefault(int(sid.split('-')[0]), []).append(sid)

# ---- timeline ----
events, scene_start, scene_len = [], {}, {}
t = 0.0
for scene in range(1, 23):
    lead, tail = EXTRA.get(scene, (0, 0))
    scene_start[scene] = t
    cur = t + LEAD + lead
    prev = None
    for i, (s, sp, text) in enumerate(L):
        if s != scene:
            continue
        sfx = sp == 'SFX'
        path = f'voice/{"sfx" if sfx else "lines"}/{i:03d}.mp3'
        audio = level(load(path), -26 if sfx else -19)
        if prev is not None:
            cur += GAP_SAME if prev == sp else GAP_SWITCH
        events.append(dict(i=i, scene=scene, speaker=sp, text=text, start=round(cur, 3),
                           dur=round(len(audio) / SR, 3), audio=audio))
        cur += min(len(audio) / SR, SFX_HOLD) if sfx else len(audio) / SR
        prev = sp
    end = max(cur + TAIL + tail, t + MIN_SHOT * len(shots_by_scene[scene]))
    scene_len[scene] = end - t
    t = end
total = t
print(f'total {total:.1f}s = {total/60:.2f} min')

# ---- audio mix ----
n = int(total * SR) + SR
voice = np.zeros((n, 2), np.float32)
active = np.zeros(n, np.float32)
for e in events:
    a, s0 = e['audio'], int(e['start'] * SR)
    voice[s0:s0 + len(a)] += a[: n - s0]
    if e['speaker'] != 'SFX':
        active[max(0, s0 - int(0.25 * SR)): s0 + len(a) + int(0.35 * SR)] = 1

music = level(load('audio/music.mp3'), -20)
xf = int(4 * SR)
bed = music.copy()
ramp = np.linspace(0, 1, xf, dtype=np.float32)[:, None]
while len(bed) < n:
    head = music.copy()
    bed[-xf:] = bed[-xf:] * (1 - ramp) + head[:xf] * ramp
    bed = np.concatenate([bed, head[xf:]])
bed = bed[:n]
win = int(0.5 * SR)
env = np.convolve(active, np.ones(win, np.float32) / win, mode='same')
gain = 10 ** ((-6 + (-17 + 6) * env) / 20)        # -6 dB open, -17 dB under speech
fade_in, fade_out = int(2 * SR), int(6 * SR)
gain[:fade_in] *= np.linspace(0, 1, fade_in)
end_s = int(total * SR)
gain[end_s - fade_out:end_s] *= np.linspace(1, 0, fade_out)
gain[end_s:] = 0
mix = voice + bed * gain[:, None]
mix = mix[:end_s]
peak = np.abs(mix).max()
if peak > 0.98:
    mix *= 0.98 / peak
os.makedirs('build', exist_ok=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-',
                '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', str(SR), 'build/mix.wav'],
               input=mix.astype(np.float32).tobytes(), check=True)

# ---- timeline + subtitles ----
json.dump(dict(total=round(total, 3), scenes={k: [round(scene_start[k], 3), round(scene_len[k], 3)] for k in scene_len},
               lines=[{k: v for k, v in e.items() if k != 'audio'} for e in events]),
          open('build/timeline.json', 'w'), ensure_ascii=False, indent=1)
NAMES = dict(nour='نور', fanoos='الفانوس', lumaa='لُمعة', mama='ماما', queen='الملكة', ogre='الغول')


def ts(x):
    ms = int(round(x * 1000))
    return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'


with open('build/ep01-ar.srt', 'w') as f:
    k = 0
    for e in events:
        if e['speaker'] == 'SFX':
            continue
        k += 1
        text = re.sub(r'\[[^\]]*\]\s*', '', e['text']).strip()
        f.write(f"{k}\n{ts(e['start'])} --> {ts(e['start'] + e['dur'])}\n{NAMES[e['speaker']]}: {text}\n\n")

# ---- video ----
order, durs = [], []
for scene in range(1, 23):
    ids = shots_by_scene[scene]
    for sid in ids:
        order.append(sid)
        durs.append(scene_len[scene] / len(ids))
os.makedirs('build/shots', exist_ok=True)
for i, (sid, d) in enumerate(zip(order, durs)):
    length = d + (XF if i < len(order) - 1 else 0)
    fc = (f"[0:v]scale=1920:1080:flags=lanczos,fps={FPS},setsar=1,split[a][b];[b]reverse[r];"
          f"[a][r]concat=n=2:v=1:a=0,loop=loop=-1:size=32767,trim=duration={length:.3f},"
          f"setpts=PTS-STARTPTS,format=yuv420p[v]")
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', f'shots3d/clips/{sid}.mp4',
                    '-filter_complex', fc, '-map', '[v]', '-an', '-c:v', 'libx264', '-preset', 'veryfast',
                    '-crf', '16', f'build/shots/{sid}.mp4'], check=True)
    print(sid, round(length, 2), flush=True)

inputs, f, prev, acc = [], [], '[0:v]', 0.0
for sid in order:
    inputs += ['-i', f'build/shots/{sid}.mp4']
m = len(order)
for i in range(1, m):
    acc += durs[i - 1]
    f.append(f'{prev}[{i}:v]xfade=transition=fade:duration={XF}:offset={acc:.3f}[v{i}]')
    prev = f'[v{i}]'
inputs += ['-i', 'build/mix.wav', '-loop', '1', '-i', 'build/logo-round.png']
outro = total - 9
f.append(f"[{m+1}:v]format=rgba,split[la][lb];"
         f"[la]trim=duration=8,fade=t=in:st=0.8:d=1.2:alpha=1,fade=t=out:st=6.5:d=1.2:alpha=1,setpts=PTS-STARTPTS[lgi];"
         f"[lb]trim=duration={total:.3f},fade=t=in:st={outro:.2f}:d=1.5:alpha=1,setpts=PTS-STARTPTS[lgo]")
f.append(f"{prev}fade=t=in:st=0:d=1.5,fade=t=out:st={total-2:.3f}:d=2[vf]")
f.append(f"[vf][lgi]overlay=W-w-60:60:eof_action=pass[vi]")
f.append(f"[vi][lgo]overlay=(W-w)/2:(H-h)/2-40:enable='gte(t,{outro:.2f})'[vout]")
subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y'] + inputs + [
    '-filter_complex', ';'.join(f), '-map', '[vout]', '-map', f'{m}:a',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-tune', 'animation', '-pix_fmt', 'yuv420p',
    '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-t', f'{total:.3f}', OUT], check=True)
print('done', OUT)
