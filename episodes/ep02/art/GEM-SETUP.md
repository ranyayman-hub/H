# الحلقة 2: إعداد Gemini (مدينة الحلويات)

**الفكرة:** نعرّف Gemini بالمسلسل مرة واحدة: الستايل، والشخصيات، والأماكن، والمراجع. بعد كده نبعتله أمر لكل صورة.

## الملفات اللي هترفعها
- `ref-characters.jpg`: صفحة الشخصيات 3D من الحلقة 1
- `ref-02-1-living-room.png`: أوضة المعيشة، وماما ونور (اتعملت واتعتمدت)
- بعد الخطوة 1 هتزود: `ref-baskota.png` و`ref-candy-city.png` و`ref-cake-mountain.png`

---

## الخطوة 1: صور مرجعية جديدة (مرة واحدة بس)
في Gemini العادي: ارفع `ref-characters.jpg`، والصق كل أمر لوحده، ونزّل الصورة بالاسم اللي جنبه.

**1) بسكوتة** → `ref-baskota.png`
```
Using the attached character sheet's high-end 3D animated family movie style, create a character reference sheet on a plain cream background: BASKOTA, a small cheerful gingerbread boy about knee-high to a 6-year-old girl. Golden-brown cookie body with soft rounded edges, a white icing smile with a clearly visible mouth, round friendly candy-button eyes, three colorful candy buttons on his chest, white icing trims on wrists and ankles, a tiny white chef hat. Show him front view, side view, back view, and two expressions (laughing, worried). Full body, no text.
```

**2) مدينة الحلويات** → `ref-candy-city.png`
```
Using the attached character sheet's high-end 3D animated family movie style, create a location reference image with no characters: CANDY CITY at night. Houses built from biscuits with colorful sugar-glass windows glowing warm, a slow river of melted chocolate with a little wafer bridge, pink and blue cotton-candy trees, giant swirly lollipop street lamps glowing softly, sprinkles on the cobblestone road, a fountain spraying strawberry juice, and far in the distance a tall cake mountain topped with a giant red cherry. Starry navy sky with a crescent moon. Wide 16:9, no text.
```

**3) جبل التورتة وجسر الجيلي وبوابة الألغاز** → `ref-cake-mountain.png`
```
Using the attached character sheet's high-end 3D animated family movie style, create a location reference image with no characters: the foot of the CAKE MOUNTAIN at night. A wobbly translucent rainbow JELLY BRIDGE crossing a chocolate stream, a small MINT SPRING bubbling clear water among mint leaves, a tall round RIDDLE GATE made of white sugar and candy canes with swirly carvings and no letters, and behind it a giant layered cream cake mountain with a huge glossy red cherry on top glowing with a pink light. Wide 16:9, no text.
```

---

## الخطوة 2: الـ Gem
1. Gemini ← **Gems** ← **New Gem**
2. **الاسم:** `Hawadeet World Studio EP02`
3. **Instructions:** الصق ده:

```
You are the image artist for "Nour and the Magic Lantern", a 3D animated bedtime series for kids. Episode 2: "Candy City". Style for every output: high-end 3D animated family movie look (Pixar-like), soft cinematic lighting, warm cozy candy colors under a magical night sky, gentle bedtime mood, wide 16:9, never any text, letters, labels or watermarks.

Always keep these characters exactly as in the attached references:
- NOUR: 6-year-old Egyptian girl, warm light-brown skin, big round dark-brown eyes, rosy cheeks, TWO long dark-brown braids (one on each side) with small yellow ribbons, light-blue button pajamas with small white stars, barefoot, a small silver necklace with eight empty star-shaped slots.
- MAMA: slim young Egyptian mother in her late twenties, plain solid beige headscarf (no pattern), long cream knit cardigan, dark grey trousers.
- MISHMISH: small chubby fluffy orange tabby cat, big green eyes, curly fluffy tail.
- THE LANTERN: ornate golden Egyptian Ramadan lantern, red, blue and green stained glass, warm amber glow, a kind cute face on the front glass, a silver ring on top. It floats. Not an oil lamp.
- LUMAA: tiny soft glowing pale-yellow five-pointed star with big shiny eyes, rosy cheeks, a small mouth and small arms. She flies.
- BASKOTA: small cheerful gingerbread boy, knee-high to Nour, golden-brown cookie body, white icing smile, candy-button eyes and chest buttons, tiny white chef hat.

Always keep locations exactly as in the attached location references (the living room, Candy City, the Cake Mountain with the jelly bridge, mint spring and riddle gate). Never change outfits, colors, hairstyles or proportions. Only the characters named in each shot appear.

Talking shots: when a shot says TALKING, the speaking character faces the camera straight on, face fully visible and centered, mouth closed and relaxed, no hands or objects covering the face.

When I send shot descriptions, generate one separate image per shot, in order, and keep the same place and lighting between shots of the same scene.
```

4. **Knowledge:** ارفع الـ 5 مراجع: `ref-characters.jpg` و`ref-02-1-living-room.png` و`ref-baskota.png` و`ref-candy-city.png` و`ref-cake-mountain.png`
5. **Save** ✅

---

## الخطوة 3: الشغل
- افتح الـ Gem، والصق رسالة رسالة من `SHOTS-EP02.md`
- سمّي كل صورة باسم اللقطة: `02-2.png`، `05-1.png`...
- لو الشكل بدأ يتغير، افتح محادثة جديدة مع نفس الـ Gem
- ابعتلي كل 3 صور، وأنا أراجعهم قبل ما نكمل
