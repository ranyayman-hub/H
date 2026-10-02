"""Plan for the dialogue edit on the user's 52 clips.
Clip k goes from shot START[k] to shot END[k] (the end frame of clip k is the
start frame of clip k+1, so clips butt-join with hard cuts). The first half of a
clip belongs to its start shot's scene, the second half to its end shot's scene."""
import json, subprocess, sys
sys.path.insert(0, 'voice')
from lines import L

A = ['01-2', '01-1', '02-1', '02-2', '03-1', '03-2', '03-3', '04-1', '04-2', '05-1', '05-2', '06-1', '06-2',
     '06-3', '06-4', '07-1', '07-2', '07-3']
B = ['07-3b', '08-1', '08-2', '08-3', '09-1', '10-1', '10-2', '11-1', '12-1', '12-2', '13-1', '13-2', '14-1', '14-2',
     '15-1', '15-2', '15-3', '16-1', '17-1', '17-2', '18-1', '18-2', '19-1', '19-2', '19-3', '20-1', '20-2', '20-3',
     '20-4', '21-1', '21-2', '21-3', '21-4', '22-1', '22-2', '22-3']
CLIPS = {k: (A[k - 1], A[k]) for k in range(1, 18)}
CLIPS.update({k: (B[k - 18], B[k - 17]) for k in range(18, 53)})
CUTS = {5: (4.70, 5.15), 7: (6.60, 7.15), 19: (5.45, 6.00), 28: (4.05, 5.10), 38: (5.05, 5.60), 43: (6.05, 6.60)}
SCENE = lambda shot: int(shot[:2])


def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                          '-of', 'csv=p=0', p]))


if __name__ == '__main__':
    halves = {}
    for k, (s, e) in CLIPS.items():
        d = dur(f'anim/{k:02d}.mp4')
        cut = CUTS.get(k, (0, 0))
        mid = d / 2
        first = mid - max(0, min(cut[1], mid) - cut[0]) if cut[0] < mid else mid
        second = (d - mid) - max(0, cut[1] - max(cut[0], mid))
        halves.setdefault(SCENE(s), 0)
        halves.setdefault(SCENE(e), 0)
        halves[SCENE(s)] += first
        halves[SCENE(e)] += second
    need = {}
    for i, (sc, sp, t) in enumerate(L):
        f = f'voice/final/{i:03d}.mp3' if sp != 'SFX' else f'voice/sfx/{i:03d}.mp3'
        d = dur(f)
        need.setdefault(sc, [0, 0])
        need[sc][0] += min(d, 1.8) if sp == 'SFX' else d
        need[sc][1] += 1
    tot_a = tot_n = 0
    for sc in sorted(halves):
        sp, n = need.get(sc, [0, 0])
        req = sp + 0.65 * max(n - 1, 0) + 1.4
        tot_a += halves[sc]; tot_n += req
        print(f'scene {sc:2d}: picture {halves[sc]:5.1f}s  dialogue needs {req:5.1f}s  ' +
              ('SLOW x%.2f' % (req / halves[sc]) if req > halves[sc] else f'spare {halves[sc]-req:4.1f}s'))
    print(f'total picture {tot_a:.0f}s, dialogue needs {tot_n:.0f}s')
