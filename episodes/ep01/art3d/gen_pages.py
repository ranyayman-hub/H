"""Regenerate IMAGE-PROMPTS-1-53.txt and the SHOTS array inside shot-prompts.html from shots.py."""
import io, contextlib, json, re
with contextlib.redirect_stdout(io.StringIO()):
    from shots import S
HEAD = ("Generate ONE single full-frame 16:9 image. Not a collage, not a grid, no extra characters. "
        "Use the character sheet and location references from your knowledge. High-end 3D animated family movie frame, "
        "soft cinematic lighting, cozy bedtime mood, no text, no letters. Only the characters described appear.")
MOT = ("Animate this exact image. {mot} Keep the characters and 3D style exactly as in the image. "
       "Gentle, slow, calm bedtime-story motion. No text, no dialogue, no lip movement, no music.")
lines = ["أوامر توليد صور الحلقة الأولى: نور والفانوس السحري (53 لقطة)",
         "انسخ كل أمر لوحده (من سطر Generate لحد آخر سطر Shot) والصقه في الـ Gem، ونزّل الصورة باسم رقم اللقطة.", ""]
for i, (sid, ar, img, mot) in enumerate(S, 1):
    lines += ["=" * 40, f"{i}) لقطة {sid}: {ar}", "=" * 40, HEAD, "", f"Shot {sid}: {img}", ""]
open('IMAGE-PROMPTS-1-53.txt', 'w').write('\n'.join(lines))
data = [{"id": sid, "label": ar, "scene": int(sid[:2]), "img": f"{HEAD}\n\nShot {sid}: {img}", "mot": MOT.format(mot=mot)}
        for sid, ar, img, mot in S]
h = open('shot-prompts.html').read()
h = re.sub(r'const SHOTS = .*?;\n', lambda m: 'const SHOTS = ' + json.dumps(data, ensure_ascii=False) + ';\n', h, count=1, flags=re.S)
open('shot-prompts.html', 'w').write(h)
print('ok')
