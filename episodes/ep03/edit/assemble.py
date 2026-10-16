"""Assemble EP03 from the approved Flow clips (flow/clips) + our ElevenLabs takes (voice/takes).

Part 1 (C01-C33) reuses flow/preview/C01-C33-voice.mp4, which was built clip by clip during review.
Part 2 (C34-C115) is rebuilt here with the same timings used in the review previews.
Output: edit/EP03-flow-v1.mp4 (no logo/music/SFX yet).
"""
import os, subprocess
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CL, TK = f'{EP}/flow/clips', f'{EP}/voice/takes'
OUT = f'{EP}/edit/build/asm'; os.makedirs(OUT, exist_ok=True)
FPS = 24

def run(cmd): subprocess.run(cmd, check=True)
def T(n): return f'{TK}/{n:03d}.mp3'

# helper audio: two takes joined (second quieter echo-like reply) as in review
def joined(a, b, out, vol_b=1.0):
    if not os.path.exists(out):
        run(['ffmpeg','-v','error','-y','-i',T(a),'-i',T(b),'-filter_complex',
             f'[0:a]aresample=44100,apad=pad_dur=0.6[a];[1:a]aresample=44100,volume={vol_b}[b];[a][b]concat=n=2:v=0:a=1[o]',
             '-map','[o]','-ac','2',out])
    return out
C35A = joined(42, 43, f'{OUT}/c35a.wav', 0.6)
C46A = joined(55, 56, f'{OUT}/c46a.wav')

# (name, source, duration, video opts, [(audio, delay_s)])
# opts: speed=slowdown factor, pre=freeze first frame seconds
S = [
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
    if aud:
        for k, (_, t) in enumerate(aud):
            ms = int(t*1000); fc.append(f'[{k+1}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{k}]')
        fc.append(''.join(f'[a{k}]' for k in range(len(aud))) + f'amix=inputs={len(aud)}:normalize=0,apad,atrim=0:{d}[a]')
    else:
        fc.append(f'anullsrc=r=44100:cl=stereo,atrim=0:{d}[a]')
    cmd += ['-filter_complex', ';'.join(fc), '-map','[v]','-map','[a]','-c:v','libx264','-crf','18','-preset','veryfast',
            '-c:a','aac','-b:a','192k','-ar','44100', dst]
    run(cmd); return dst

parts = []
p1 = f'{OUT}/s000-C01-C33.mp4'
if not os.path.exists(p1):
    run(['ffmpeg','-v','error','-y','-i',f'{EP}/flow/preview/C01-C33-voice.mp4','-vf',VN,'-af','aresample=44100,aformat=channel_layouts=stereo',
         '-c:v','libx264','-crf','18','-preset','veryfast','-c:a','aac','-b:a','192k','-ar','44100',p1])
parts.append(p1)
for i, s in enumerate(S, 1): parts.append(seg(i, *s))
open(f'{OUT}/list.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
out = f'{EP}/edit/EP03-flow-v1.mp4'
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{OUT}/list.txt','-c','copy','-movflags','+faststart',out])
print('segments', len(parts), 'seconds', subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out]).decode().strip())
