import json, subprocess
XF = 0.8
d = {int(k): v for k, v in json.load(open('build/scene_durations.json')).items()}
total = sum(d.values())

# round logo with transparent corners
subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', '../../branding/hawadeet-world-logo.png',
                '-vf', "format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(lte(hypot(X-400,Y-400),396),255,0)',scale=420:420",
                'build/logo-round.png'], check=True)

inputs = []
for s in range(1, 23):
    inputs += ['-i', f'build/clips/c{s:02d}.mp4']
inputs += ['-i', 'episode01-narration-full.mp3', '-loop', '1', '-i', 'build/logo-round.png']

f, prev, acc = [], '[0:v]', 0.0
for s in range(1, 22):
    acc += d[s]
    out = f'[v{s}]'
    f.append(f'{prev}[{s}:v]xfade=transition=fade:duration={XF}:offset={acc:.3f}{out}')
    prev = out
outro_start = total - 11
f.append(f"[23:v]format=rgba,trim=duration={total:.3f},"
         f"fade=t=in:st=0.6:d=1.2:alpha=1,fade=t=out:st=6:d=1.2:alpha=1,"
         f"fade=t=in:st={outro_start:.2f}:d=1.5:alpha=1[lg0]")
# second fade-in needs a separate stream: build intro and outro logos independently
f[-1] = (f"[23:v]format=rgba,split[la][lb];"
         f"[la]trim=duration=7.5,fade=t=in:st=0.6:d=1.2:alpha=1,fade=t=out:st=6:d=1.2:alpha=1,setpts=PTS-STARTPTS[lgi];"
         f"[lb]trim=duration={total:.3f},fade=t=in:st={outro_start:.2f}:d=1.5:alpha=1,setpts=PTS-STARTPTS[lgo]")
f.append(f"{prev}[lgi]overlay=(W-w)/2:(H-h)/2:eof_action=pass[vi]")
f.append(f"[vi][lgo]overlay=(W-w)/2:(H-h)/2-40:enable='gte(t,{outro_start:.2f})'[vout]")
f.append(f"[22:a]adelay=1000|1000,apad,atrim=duration={total:.3f},afade=t=out:st={total-2.5:.3f}:d=2.5[aout]")

cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y'] + inputs + [
    '-filter_complex', ';'.join(f), '-map', '[vout]', '-map', '[aout]',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', '30',
    '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-t', f'{total:.3f}',
    'Hawadeet-World-EP01-Nour-and-the-Magic-Lantern.mp4']
subprocess.run(cmd, check=True)
print('done', total)
