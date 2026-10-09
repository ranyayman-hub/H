"""Work out where each EP02 SFX lands in EP02-flow-v5.mp4 (v3 timeline + 6s logo intro)."""
import subprocess, re, json
ORDER = ['@intro','02-1','C02','L02-3','C04','C05','C06','C07','L03-2','C09','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21',
 'C22','C23','C24','C25','C27','C28','C30','C31','C32','C33','C34','C35','C36','C37','C38','C39','C40','C41','C43',
 'C44','C45','C47','C49','C51','C52','C54','C56','C57','C60','C62','C64','C65','C66','C67','C69','C70','C71','@outro']
# sfx line -> (clip, where): 'start' = at clip start, 'after' = when the first spoken line ends, 'end' = clip tail
CUES = {4:('02-1','start'), 12:('C05','after'), 13:('C06','start'), 16:('C09','start'), 22:('C12','start'),
        25:('C15','start'), 41:('C30','after'), 52:('C41','start'), 63:('C49','after'), 70:('C54','after'),
        77:('C60','start'), 81:('C62','start'), 93:('C69','end')}
OFFSET = 6.0
dur = lambda f: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
starts, t = [], 0.0
for i in range(len(ORDER)):
    starts.append(t); t += dur(f'build/asm/p{i:03d}.mp4')
out = {}
for line, (clip, where) in CUES.items():
    i = ORDER.index(clip); p = f'build/asm/p{i:03d}.mp4'; d = dur(p); s = dur(f'../voice/sfx/{line:03d}.mp3')
    if where == 'start': at = 0.15
    elif where == 'end': at = max(0.0, d - s - 0.4)
    else:
        log = subprocess.run(['ffmpeg','-i',p,'-af','silencedetect=n=-35dB:d=0.25','-f','null','-'], capture_output=True, text=True).stderr
        ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', log)]
        at = next((x for x in ss if x > 0.8), d - s - 0.4) + 0.05
    out[line] = round(starts[i] + OFFSET + at, 2)
    print(line, clip, where, out[line])
json.dump(out, open('build/sfx_cues.json','w'))
