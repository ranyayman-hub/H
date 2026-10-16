"""Generate EP03 sound effects with the ElevenLabs sound-generation API -> voice/sfx/NNN.mp3.
The 'hello hello' echoes (034/038/039) are already made from Nour's own voice with aecho, so they are skipped;
041 reuses 000 (same cave drips). Skips files that already exist, so re-running never re-spends credits."""
import json, os, shutil, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lines
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx'); os.makedirs(OUT, exist_ok=True)
DUR = {0: 4, 18: 4, 19: 2.5, 22: 2, 27: 3, 53: 1.5, 78: 2.5, 92: 3, 97: 6, 105: 3, 108: 1.5, 121: 3, 124: 1}
KEY = os.environ['ELEVENLABS_API_KEY']
for n, d in DUR.items():
    dst = f'{OUT}/{n:03d}.mp3'
    if os.path.exists(dst): continue
    text = lines.L[n][2] + ', gentle and soft, for a calm bedtime cartoon for young children'
    req = urllib.request.Request('https://api.elevenlabs.io/v1/sound-generation',
        data=json.dumps({'text': text, 'duration_seconds': d, 'prompt_influence': 0.5}).encode(),
        headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=120) as r: open(dst, 'wb').write(r.read())
    print('ok', n, os.path.getsize(dst))
if not os.path.exists(f'{OUT}/041.mp3'): shutil.copy(f'{OUT}/000.mp3', f'{OUT}/041.mp3')
