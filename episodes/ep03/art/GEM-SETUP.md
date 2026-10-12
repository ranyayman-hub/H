# الحلقة 3: إعداد Gemini (التنين اللي خايف من الضلمة)

**نفس طريقة حلقة 2:** نعمل الصور المرجعية الأول، وبعدين نعرّف Gemini بيها، وبعد كده نبعتله أوامر اللقطات.

## الملفات اللي هترفعها
- `ref-characters.jpg`: صفحة الشخصيات (نور، ومشمش، والفانوس، ولُمعة)
- `ref-bedroom.jpg`: أوضة نور (من حلقة 2)
- `ref-sharara.png` و`ref-crystal-mountains.png` و`ref-cave.png` ✅ (اتعملوا على ChatGPT)

---

## الخطوة 1: صور مرجعية جديدة (مرة واحدة بس)
في Gemini العادي: ارفع `ref-characters.jpg`، والصق كل أمر لوحده، ونزّل الصورة بالاسم اللي جنبه.

**1) شرارة** → `ref-sharara.png`
```
Using the attached character sheet's high-end 3D animated family movie style, create an original character reference sheet on a plain cream background: SHARARA, a tiny, soft, round, cuddly baby dragon about knee-high to a 6-year-old girl. Pastel lavender-purple body covered with small golden dots, a smooth cream-colored round belly, very big round shiny dark eyes with sparkles, rosy cheeks, two small rounded nub horns on top of the head (cream colored), small stubby legs, a short chubby tail with a little golden tip, and two tiny soft wings that look too small to fly. Gentle, shy and adorable, not scary at all, no sharp teeth or claws. Show him front view, side view, back view, and three expressions: shy and scared (covering his eyes with his little hands), laughing, and proudly breathing a tiny puff of warm orange fire. Full body, no text.
```

**2) جبال الكريستال** → `ref-crystal-mountains.png`
```
Using the attached character sheet's high-end 3D animated family movie style, create a location reference image with no characters: the CRYSTAL MOUNTAINS at night. Tall mountains made of giant glowing purple and blue crystals, shimmering waterfalls that sparkle like diamonds falling into a calm lake, a small rainbow above the water, soft mist, a starry navy sky with a crescent moon. On one mountain side, a big dark round cave entrance surrounded by crystals. Magical, calm and safe bedtime mood. Wide 16:9, no text.
```

**3) جوه الكهف** → `ref-cave.png`
```
Using the attached character sheet's high-end 3D animated family movie style, create a location reference image with no characters: INSIDE the crystal cave. A wide, cozy cave with smooth rock walls and many unlit crystals of all colors (red, blue, green, purple) growing from the walls and floor, a narrow glassy crystal bridge crossing a small dark gap, and at the far end one big crystal with a small glowing purple gem resting on top. The cave is dim and blue but still safe and cute, not scary; tiny glowing fireflies float here and there. Wide 16:9, no text.
```

**ابعتلي الـ 3 صور** وأنا أراجعهم قبل ما نكمل. لو شرارة طلع شبه تنين معروف أو شكله مخيف، نعدّل الأمر.

---

## الخطوة 2: الـ Gem (أو مشروع في ChatGPT)
**لو هتشتغل على ChatGPT:** اعمل **Project** جديد اسمه `Hawadeet World EP03`، وحط نص `KICKOFF.txt` في **Instructions**، وارفع الـ 5 مراجع في **Files**. وبعدين كل رسالة من `SHOTS-EP03.md` في محادثة جوه المشروع.

**لو على Gemini:**
1. Gemini ← **Gems** ← **New Gem**
2. **الاسم:** `Hawadeet World Studio EP03`
3. **Instructions:** الصق نص `KICKOFF.txt` كله
4. **Knowledge:** ارفع الـ 5 مراجع: `ref-characters.jpg` و`ref-bedroom.jpg` و`ref-sharara.png` و`ref-crystal-mountains.png` و`ref-cave.png`
5. **Save** ✅

---

## الخطوة 3: الشغل
- افتح الـ Gem، والصق رسالة رسالة من `SHOTS-EP03.md`
- سمّي كل صورة باسم اللقطة: `04-1.png`، `06-2.png`...
- لو الشكل بدأ يتغير، افتح محادثة جديدة مع نفس الـ Gem
- ابعتلي كل 3 صور، وأنا أراجعهم قبل ما نكمل
