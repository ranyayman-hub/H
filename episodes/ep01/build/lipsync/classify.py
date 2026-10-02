"""Manual review of build/lipsync/sheet-*.jpg: does the speaker's face show while the line plays?
Y = face clearly visible (needs lip-sync), M = small/far or only part of the line, N = speaker not on screen."""
import json
Y = [0, 1, 6, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 28, 30, 35, 37, 49, 50, 51, 52, 53, 54, 55, 56,
     57, 58, 59, 61, 68, 77, 78, 88, 89, 90, 91, 92, 96, 99, 100, 101, 103, 104]
M = [5, 7, 8, 9, 26, 29, 32, 34, 36, 38, 39, 40, 41, 46, 47, 62, 64, 67, 69, 79, 86, 97, 98, 105, 107, 108]
cost = lambda d: 382 * (d + 0.5) + 140
rows = json.load(open('build/lipsync/lines.json'))
out = {}
for r in rows:
    r['cls'] = 'Y' if r['i'] in Y else 'M' if r['i'] in M else 'N'
    r['cost'] = round(cost(r['dur']))
for c in 'YMN':
    rs = [r for r in rows if r['cls'] == c]
    by = {}
    for r in rs:
        b = by.setdefault(r['speaker'], [0, 0, 0]); b[0] += 1; b[1] += r['dur']; b[2] += r['cost']
    print(c, len(rs), 'lines', round(sum(r['dur'] for r in rs)), 's', sum(r['cost'] for r in rs), 'credits')
    for s, (n, d, k) in sorted(by.items(), key=lambda x: -x[1][2]):
        print(f'   {s:7s} {n:3d} lines {d:6.1f}s {k:7d}')
json.dump(rows, open('build/lipsync/lines.json', 'w'), indent=1, ensure_ascii=False)
