"""Turn an animated clip (from Flow/Kling/Sora) into a scene clip of the exact length,
looping it forward-then-backward (boomerang) so the motion never jumps."""
import json, subprocess, sys
XF, FPS = 0.8, 30
d = {int(k): v for k, v in json.load(open('build/scene_durations.json')).items()}
for s in map(int, sys.argv[1:]):
    length = d[s] + (XF if s < 22 else 0)
    vf = (f"[0:v]scale=1920:1080:flags=lanczos,fps={FPS},setsar=1,split[a][b];[b]reverse[r];"
          f"[a][r]concat=n=2:v=1:a=0,loop=loop=-1:size=32767,trim=duration={length:.3f},"
          f"setpts=PTS-STARTPTS,format=yuv420p[v]")
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', f'anim/scene-{s:02d}.mp4',
                    '-filter_complex', vf, '-map', '[v]', '-an', '-c:v', 'libx264', '-preset', 'veryfast',
                    '-crf', '18', f'build/clips/c{s:02d}.mp4'], check=True)
    print('anim clip', s, round(length, 2))
