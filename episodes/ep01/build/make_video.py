import json, re, subprocess, os

GAP = 1.2      # silence between audio parts (same as narration build)
LEAD = 1.0     # silence before narration starts
TAIL = 4.0     # extra time on the last scene
XF = 0.8       # crossfade length
FPS = 30

parts = json.load(open('parts.json'))
# scene numbers per audio part, in paragraph order
scene_map = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13],
             [14, 15, 16, 17], [18, 19, 20], [21, 22]]

def dur(p):
    return float(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))

def silences(p):
    out = subprocess.run(['ffmpeg', '-hide_banner', '-i', p, '-af', 'silencedetect=n=-35dB:d=0.35',
                          '-f', 'null', '-'], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]
    en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
    return [(a + b) / 2 for a, b in zip(st, en)]

scene_dur = {}
for i, (text, scenes) in enumerate(zip(parts, scene_map)):
    paras = [p for p in text.split('\n\n') if p.strip()]
    if i == 4:  # paragraph 3 holds scenes 16 and 17; split where the orb breaks
        a, b = paras[2].split('واتكسرت!', 1)
        paras = paras[:2] + [a, 'واتكسرت!' + b] + paras[3:]
    assert len(paras) == len(scenes), (i, len(paras))
    d = dur(f'audio/part{i+1}.mp3')
    sil = silences(f'audio/part{i+1}.mp3')
    total = sum(len(p) for p in paras)
    bounds, acc = [], 0
    for p in paras[:-1]:
        acc += len(p)
        guess = d * acc / total
        near = [s for s in sil if abs(s - guess) < 3.0]
        bounds.append(min(near, key=lambda s: abs(s - guess)) if near else guess)
    edges = [0] + bounds + [d]
    for k, s in enumerate(scenes):
        scene_dur[s] = edges[k + 1] - edges[k]
    scene_dur[scenes[-1]] += GAP if i < 6 else 0
scene_dur[1] += LEAD
scene_dur[22] += TAIL
json.dump(scene_dur, open('build/scene_durations.json', 'w'), indent=1)
print({k: round(v, 2) for k, v in scene_dur.items()}, round(sum(scene_dur.values()), 2))

# render each scene as a slow Ken Burns clip
os.makedirs('build/clips', exist_ok=True)
for s in range(1, 23):
    length = scene_dur[s] + (XF if s < 22 else 0)
    frames = int(round(length * FPS))
    zoom_in = s % 2 == 1
    z = f"'1+0.08*on/{frames}'" if zoom_in else f"'1.08-0.08*on/{frames}'"
    vf = (f"crop=1365:768,scale=3840:2160,"
          f"zoompan=z={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1920x1080:fps={FPS},"
          f"format=yuv420p")
    out = f'build/clips/c{s:02d}.mp4'
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-loop', '1', '-i',
                    f'art/scenes/scene-{s:02d}.png', '-vf', vf, '-frames:v', str(frames),
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', out], check=True)
    print('clip', s, round(length, 2), flush=True)
