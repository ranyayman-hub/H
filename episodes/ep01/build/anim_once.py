"""For clips whose motion should not run backwards (e.g. the lantern lighting up):
play the clip once, then continue from its last frame with a slow zoom to fill the scene."""
import json, subprocess, sys
XF, FPS = 0.8, 30
d = {int(k): v for k, v in json.load(open('build/scene_durations.json')).items()}
for s in map(int, sys.argv[1:]):
    src = f'anim/scene-{s:02d}.mp4'
    clip_len = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                              '-of', 'csv=p=0', src])) - 0.1
    length = d[s] + (XF if s < 22 else 0)
    tail = max(length - clip_len, 0.1)
    frames = int(round(tail * FPS))
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-sseof', '-0.1', '-i', src,
                    '-frames:v', '1', '-update', '1', f'build/last-{s:02d}.png'], check=True)
    fc = (f"[0:v]trim=duration={clip_len:.3f},scale=1920:1080:flags=lanczos,fps={FPS},setsar=1,setpts=PTS-STARTPTS[a];"
          f"[1:v]scale=3840:2160,zoompan=z='1+0.06*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={frames}:s=1920x1080:fps={FPS},setsar=1[b];"
          f"[a][b]concat=n=2:v=1:a=0,trim=duration={length:.3f},format=yuv420p[v]")
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', src, '-loop', '1', '-i',
                    f'build/last-{s:02d}.png', '-filter_complex', fc, '-map', '[v]', '-an', '-c:v', 'libx264',
                    '-preset', 'veryfast', '-crf', '18', f'build/clips/c{s:02d}.mp4'], check=True)
    print('anim once', s, round(length, 2))
