"""Assemble EP03 from the approved Flow clips (flow/clips) + our ElevenLabs takes (voice/takes).

Every shot is rebuilt here with the timings approved in the review previews; each take is
levelled to -17 LUFS first.
Output: edit/EP03-flow-v1.mp4 (no logo/music/SFX yet).
"""
import os, re, subprocess
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CL, TK = f'{EP}/flow/clips', f'{EP}/voice/takes'
OUT = f'{EP}/edit/build/asm'; os.makedirs(OUT, exist_ok=True)
FPS = 24

def run(cmd): subprocess.run(cmd, check=True)
NORM = f'{OUT}/norm'; os.makedirs(NORM, exist_ok=True)
def lufs(p):
    log = subprocess.run(['ffmpeg','-i',p,'-af','ebur128=framelog=quiet','-f','null','-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', log)[-1])
def T(n):
    """Take n, gain-normalised to -17 LUFS (raw ElevenLabs takes vary by ~12 dB)."""
    src, dst = f'{TK}/{n:03d}.mp3', f'{NORM}/{n:03d}.wav'
    if not os.path.exists(dst):
        g = -17 - lufs(src)
        run(['ffmpeg','-v','error','-y','-i',src,'-af',f'volume={g:.2f}dB,alimiter=limit=0.95:level=false','-ar','44100',dst])
    return dst

# helper audio: two takes joined (second quieter echo-like reply) as in review
def joined(a, b, out, vol_b=1.0):
    if not os.path.exists(out):
        run(['ffmpeg','-v','error','-y','-i',T(a),'-i',T(b),'-filter_complex',
             f'[0:a]aresample=44100,apad=pad_dur=0.6[a];[1:a]aresample=44100,volume={vol_b}[b];[a][b]concat=n=2:v=0:a=1[o]',
             '-map','[o]','-ac','2',out])
    return out
C35A = joined(42, 43, f'{OUT}/c35a.wav', 0.6)
C46A = joined(55, 56, f'{OUT}/c46a.wav')
def fx(out, fc, ins):
    if not os.path.exists(out):
        cmd=['ffmpeg','-v','error','-y']
        for i in ins: cmd+=['-i',i]
        run(cmd+['-filter_complex',fc,'-map','[o]','-ac','2',out])
    return out
C15A = fx(f'{OUT}/c15a.wav', '[0:a]aresample=44100,apad=pad_dur=0.4[x];[1:a]aresample=44100[y];[x][y]concat=n=2:v=0:a=1[o]', [T(15), T(16)])
C29A = fx(f'{OUT}/c29a.wav', '[0:a]aresample=44100,aecho=0.8:0.6:400|800:0.5|0.3,apad=pad_dur=1.3[x];[1:a]aresample=44100[y];[x][y]concat=n=2:v=0:a=1[o]', [T(33), T(35)])
C31E = fx(f'{OUT}/c31e.wav', '[0:a]aresample=44100,aecho=0.8:0.6:400|800:0.6|0.4,volume=0.6[o]', [T(33)])

# (name, source, duration, video opts, [(audio, delay_s)])
# opts: speed=slowdown factor, pre=freeze first frame seconds
S = [
 ('C01', 'C01', 4.0, {}, [(T(1), 1.0)]),
 ('C02', 'C02', 4.0, {}, [(T(2), .3)]),
 ('C03', 'C03', 5.0, {}, [(T(3), .1)]),
 ('C04', 'C04', 6.0, {}, [(T(4), .1)]),
 ('C05', 'C05', 4.2, {}, [(T(5), .4)]),
 ('C06', 'C06', 3.2, {}, [(T(6), .1)]),
 ('C07', 'C07', 4.1, {}, [(T(7), .1)]),
 ('C08', 'C08', 4.2, {}, [(T(8), .1)]),
 ('C09', 'C09', 3.3, {}, [(T(9), .1)]),
 ('C10', 'C10', 6.0, {}, [(T(10), .1)]),
 ('C11', 'C11', 8.8, {'speed': 1.1}, [(T(11), .1)]),
 ('C12', 'C12', 6.1, {}, [(T(12), .1)]),
 ('C13', 'C13', 4.0, {}, [(T(13), .1)]),
 ('C14', 'C14', 8.0, {}, [(T(14), .1)]),
 ('C15', 'C15', 7.4, {}, [(C15A, .1)]),
 ('C16', 'C16', 4.5, {}, [(T(17), .2)]),
 ('C17', 'C17', 5.375, {'speed': 1.25}, [(T(20), .2)]),
 ('C18', 'C18', 3.6, {}, [(T(21), .3)]),
 ('C19', 'C19', 6.0, {}, [(T(23), .2), (T(24), 3.7)]),   # C20 rides on C19's tail
 ('C21', 'C21', 6.3, {}, [(T(25), .2)]),
 ('C22', 'C22', 3.4, {}, [(T(26), .15)]),
 ('C23', 'C23', 3.0, {'own': 0.6}, []),                   # keeps Veo's own ambience
 ('C24', 'C24', 4.8, {}, [(T(28), .15)]),
 ('C25', 'C25', 6.1, {}, [(T(29), .15)]),
 ('C26', 'C26', 3.7, {}, [(T(30), .15)]),
 ('C27', 'C27', 3.9, {}, [(T(31), .15)]),
 ('C28', 'C28', 6.9, {}, [(T(32), .15)]),
 ('C29', 'C29', 6.0, {}, [(C29A, .1)]),
 ('C30', 'C30', 3.2, {}, [(T(36), .15)]),
 ('C31', 'C31', 8.0, {}, [(T(37), 0), (C31E, 6.6)]),      # C32 echo on C31's tail
 ('C33', 'C33', 5.3, {}, [(T(40), .15)]),
 ('C34', 'C34-still', 1.5, {}, []),
 ('C35', 'C35', 5.3, {}, [(C35A, .1)]),
 ('C36', 'C36', 3.4, {}, [(T(44), .1)]),
 ('C37', 'C37', 4.5, {}, [(T(45), .15)]),
 ('C38', 'C38', 4.4, {}, [(T(46), .15)]),
 ('C39', 'C39', 3.2, {}, [(T(47), .15)]),
 ('C40', 'C40', 2.7, {}, [(T(48), .2)]),
 ('C41', 'C41', 6.2, {}, [(T(49), .15)]),
 ('C42', 'C42', 3.2, {}, [(T(50), .15)]),
 ('C43', 'C43', 3.6, {}, [(T(51), .15)]),
 ('C44', 'C44', 8.0, {'pre': 2.5}, [(T(52), 0), (T(54), 4.8)]),   # C45 rides on C44's tail
 ('C46', 'C46', 8.0, {}, [(C46A, .15)]),                           # C46+C47
 ('C48', 'C48', 4.1, {}, [(T(57), .15)]),
 ('C49', 'C49', 3.2, {}, [(T(58), .15)]),
 ('C50', 'C50', 5.1, {}, [(T(59), .15)]),
 ('C51', 'C51', 5.3, {}, [(T(60), .2)]),
 ('C52', 'C52', 2.6, {}, [(T(61), .15)]),
 ('C53', 'C53', 6.2, {}, [(T(62), .3)]),
 ('C54', 'C54', 4.0, {}, [(T(63), .3)]),
 ('C55', 'C55', 7.4, {}, [(T(64), .3)]),
 ('C56', 'C56', 5.9, {}, [(T(65), .3), (T(66), 4.2)]),
 ('C57', 'C57', 5.6, {}, [(T(67), .3)]),
 ('C58', 'C58', 5.8, {}, [(T(68), .3)]),
 ('C59', 'C59', 10.4, {'speed': 1.3}, [(T(69), .3), (T(70), 5.0)]),  # C59+C60
 ('C61', 'C61', 5.6, {}, [(T(71), .3)]),
 ('C62', 'C62', 6.1, {}, [(T(72), .3)]),
 ('C63', 'C63', 5.6, {}, [(T(73), .3)]),
 ('C64', 'C64', 4.8, {}, [(T(74), .3)]),
 ('C65', 'C65', 4.0, {}, [(T(75), .3)]),
 ('C66', 'C66', 2.9, {}, [(T(76), .3)]),
 ('C67', 'C67', 4.7, {}, [(T(77), .3)]),
 ('C68', 'C68-still', 2.0, {}, []),
 ('C69', 'C69', 4.3, {}, [(T(79), .3)]),
 ('C70', 'C70', 4.8, {}, [(T(80), .3)]),
 ('C71', 'C71', 6.8, {}, [(T(81), .3)]),
 ('C72', 'C72', 4.8, {}, [(T(82), .3)]),
 ('C73', 'C73', 4.4, {}, [(T(83), .3)]),
 ('C74', 'C74', 4.0, {}, [(T(84), .3)]),
 ('C75', 'C75', 4.7, {}, [(T(85), .3)]),
 ('C76', 'C76', 4.0, {}, [(T(86), .3)]),
 ('C77', 'C77', 3.6, {}, [(T(87), .3)]),
 ('C78', 'C78', 9.8, {'speed': 1.25}, [(T(88), .3), (T(89), 3.6)]),  # C78+C79
 ('C80', 'C80', 3.4, {}, [(T(90), .3)]),
 ('C81', 'C81', 5.4, {}, [(T(91), .3)]),
 ('C82', 'C82-still', 3.0, {}, [(T(93), .3)]),
 ('C83', 'C83', 2.5, {}, [(T(94), .3)]),
 ('C84', 'C84', 3.9, {}, [(T(95), .3)]),
 ('C85', 'C85', 6.3, {}, [(T(96), .3)]),
 ('C86', 'C86', 7.0, {}, []),
 ('C87', 'C87', 4.6, {}, [(T(98), .3)]),
 ('C88', 'C88', 6.3, {}, [(T(99), .3)]),
 ('C89', 'C89', 4.1, {}, [(T(100), .3)]),
 ('C90', 'C90', 6.6, {}, [(T(101), .3)]),
 ('C91', 'C91', 3.7, {}, [(T(102), .3)]),
 ('C92', 'C92', 5.1, {}, [(T(103), .3)]),
 ('C93', 'C93', 3.2, {}, [(T(104), .3)]),
 ('C94', 'C94', 4.2, {}, [(T(106), 1.2)]),
 ('C95', 'C95', 3.6, {}, [(T(107), .3)]),
 ('C96', 'C96-still', 2.0, {}, []),
 ('C97', 'C97', 3.6, {}, [(T(109), .3)]),
 ('C98', 'C98', 2.4, {}, [(T(111), .3)]),
 ('C99', 'C99', 5.6, {}, [(T(110), .3)]),
 ('C100', 'C100', 8.0, {}, [(T(112), .3)]),
 ('C101', 'C101', 7.3, {}, [(T(114), .3)]),
 ('C102', 'C102', 10.2, {'speed': 1.3}, [(T(113), .3), (T(115), 2.85), (T(116), 5.9)]),  # C102+C103
 ('C104', 'C104', 8.0, {}, [(T(118), .3), (T(119), 4.5)]),  # C104+C105
 ('C106', 'C106', 9.2, {'speed': 1.25}, [(T(117), .3), (T(120), 5.8)]),  # C106+C107
 ('C108', 'C108', 3.4, {}, [(T(122), .3)]),
 ('C109', 'C109', 5.0, {}, [(T(123), .3)]),
 ('C110', 'C110', 7.5, {}, [(T(125), 3.2)]),
 ('C111', 'C111', 5.6, {}, [(T(126), .3)]),
 ('C112', 'C112-long', 24.8, {}, [(T(127), .5), (T(128), 8.6), (T(129), 11.3), (T(130), 14.6)]),  # C112-C114
 ('C115', 'C115', 8.96, {'speed': 1.12}, [(T(131), .5)]),
]

VN = f'scale=1280:720,fps={FPS},format=yuv420p,setsar=1'
def seg(i, name, src, d, o, aud):
    dst = f'{OUT}/s{i:03d}-{name}.mp4'
    if os.path.exists(dst): return dst
    sp = o.get('speed', 1.0); pre = o.get('pre', 0)
    v = f'[0:v]setpts={sp}*(PTS-STARTPTS),{VN}'
    if pre: v += f',tpad=start_duration={pre}:start_mode=clone'
    v += f',tpad=stop_mode=clone:stop_duration=2,trim=0:{d},setpts=PTS-STARTPTS[v]'
    cmd = ['ffmpeg','-v','error','-y','-i',f'{CL}/{src}.mp4']
    for a, _ in aud: cmd += ['-i', a]
    fc = [v]
    if 'own' in o:
        fc.append(f"[0:a]aresample=44100,aformat=channel_layouts=stereo,volume={o['own']},apad,atrim=0:{d}[a]")
    elif aud:
        for k, (_, t) in enumerate(aud):
            ms = int(t*1000); fc.append(f'[{k+1}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{k}]')
        fc.append(''.join(f'[a{k}]' for k in range(len(aud))) + f'amix=inputs={len(aud)}:normalize=0,apad,atrim=0:{d}[a]')
    else:
        fc.append(f'anullsrc=r=44100:cl=stereo,atrim=0:{d}[a]')
    cmd += ['-filter_complex', ';'.join(fc), '-map','[v]','-map','[a]','-c:v','libx264','-crf','18','-preset','veryfast',
            '-c:a','aac','-b:a','192k','-ar','44100', dst]
    run(cmd); return dst

parts = []
for i, s in enumerate(S, 1): parts.append(seg(i, *s))
open(f'{OUT}/list.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
out = f'{EP}/edit/EP03-flow-v1.mp4'
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{OUT}/list.txt','-c','copy','-movflags','+faststart',out])
print('segments', len(parts), 'seconds', subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out]).decode().strip())
