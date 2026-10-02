"""Build the 3D episode from the 53-shot list.
Each scene's duration (from the narration timing) is split evenly across its shots.
For every shot it uses, in order of preference:
  shots3d/clips/<id>.mp4   animated clip (looped forward/backward to fill the shot)
  shots3d/images/<id>.png|jpg  still image with a slow zoom
  the scene's first available shot image, as a fallback."""
import json, os, glob, subprocess, sys
sys.path.insert(0, 'art3d')
from shots import S

XF, FPS = 0.6, 30
scene_dur = {int(k): v for k, v in json.load(open('build/scene_durations.json')).items()}
shots_by_scene = {}
for sid, *_ in S:
    shots_by_scene.setdefault(int(sid.split('-')[0]), []).append(sid)

def find(kind, sid):
    exts = ['mp4'] if kind == 'clips' else ['png', 'jpg', 'jpeg', 'webp']
    for e in exts:
        p = f'shots3d/{kind}/{sid}.{e}'
        if os.path.exists(p):
            return p

os.makedirs('build/shots', exist_ok=True)
order, durs = [], []
for scene in range(1, 23):
    ids = shots_by_scene[scene]
    for sid in ids:
        order.append(sid)
        durs.append(scene_dur[scene] / len(ids))

missing = []
for i, (sid, d) in enumerate(zip(order, durs)):
    length = d + (XF if i < len(order) - 1 else 0)
    out = f'build/shots/{sid}.mp4'
    clip = find('clips', sid)
    if clip:
        fc = (f"[0:v]scale=1920:1080:flags=lanczos,fps={FPS},setsar=1,split[a][b];[b]reverse[r];"
              f"[a][r]concat=n=2:v=1:a=0,loop=loop=-1:size=32767,trim=duration={length:.3f},"
              f"setpts=PTS-STARTPTS,format=yuv420p[v]")
        cmd = ['ffmpeg', '-y', '-i', clip, '-filter_complex', fc, '-map', '[v]']
    else:
        img = find('images', sid) or next((find('images', o) for o in shots_by_scene[int(sid[:2])] if find('images', o)), None)
        if not img:
            missing.append(sid)
            continue
        frames = int(round(length * FPS))
        z = f"'1+0.07*on/{frames}'" if i % 2 == 0 else f"'1.07-0.07*on/{frames}'"
        vf = (f"scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,scale=3840:2160,"
              f"zoompan=z={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1920x1080:fps={FPS},format=yuv420p")
        cmd = ['ffmpeg', '-y', '-loop', '1', '-i', img, '-vf', vf, '-frames:v', str(frames)]
    subprocess.run(['ffmpeg'] + ['-hide_banner', '-loglevel', 'error'] + cmd[1:] +
                   ['-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', out], check=True)
    print(sid, 'clip' if clip else 'image', round(length, 2), flush=True)

if missing:
    sys.exit(f'missing images for scenes of shots: {missing}')

total = sum(durs)
inputs, f, prev, acc = [], [], '[0:v]', 0.0
for sid in order:
    inputs += ['-i', f'build/shots/{sid}.mp4']
n = len(order)
for i in range(1, n):
    acc += durs[i - 1]
    f.append(f'{prev}[{i}:v]xfade=transition=fade:duration={XF}:offset={acc:.3f}[v{i}]')
    prev = f'[v{i}]'
inputs += ['-i', 'episode01-narration-full.mp3', '-loop', '1', '-i', 'build/logo-round.png']
outro = total - 11
f.append(f"[{n+1}:v]format=rgba,split[la][lb];"
         f"[la]trim=duration=7.5,fade=t=in:st=0.6:d=1.2:alpha=1,fade=t=out:st=6:d=1.2:alpha=1,setpts=PTS-STARTPTS[lgi];"
         f"[lb]trim=duration={total:.3f},fade=t=in:st={outro:.2f}:d=1.5:alpha=1,setpts=PTS-STARTPTS[lgo]")
f.append(f"{prev}[lgi]overlay=W-w-60:60:eof_action=pass[vi]")
f.append(f"[vi][lgo]overlay=(W-w)/2:(H-h)/2-40:enable='gte(t,{outro:.2f})'[vout]")
f.append(f"[{n}:a]adelay=1000|1000,apad,atrim=duration={total:.3f},afade=t=out:st={total-2.5:.3f}:d=2.5[aout]")
subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y'] + inputs + [
    '-filter_complex', ';'.join(f), '-map', '[vout]', '-map', '[aout]',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '24', '-tune', 'animation', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', f'{total:.3f}',
    'Hawadeet-World-EP01-3D.mp4'], check=True)
print('done', round(total, 2))
