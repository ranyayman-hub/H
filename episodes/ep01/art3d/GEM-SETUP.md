# إعداد Gem في Gemini لمسلسل "نور والفانوس السحري"

الـ **Gem** هو نسخة من Gemini بتعملها بنفسك، **وبتفتكر التعليمات والصور المرجعية** في كل محادثة، فمش هتحتاج ترفعهم كل مرة.

## الخطوة 1: نعمل صور مرجعية للأماكن (مرة واحدة بس)
في Gemini العادي: **ارفع صفحة الشخصيات 3D**، والصق كل أمر لوحده، **ونزّل الصورة**.

**1) أوضة نور**
```
Using the attached character sheet's 3D animated movie style (like Pixar films), create a location reference image with no characters: Nour's cozy Egyptian bedroom at night. A small wooden bed with a white pillow and a quilted cream blanket, a wooden nightstand with a small warm lamp on the left, a window with soft blue curtains and a crescent moon outside on the right, a wooden wall shelf with books and an old golden Ramadan lantern, a small wooden dresser, warm beige walls, a soft rug. Wide 16:9, no text.
```

**2) الشارع وبيت نور**
```
Using the attached character sheet's 3D animated movie style (like Pixar films), create a location reference image with no characters: a quiet old Egyptian cobblestone street at night, with a cozy two-story sand-colored house with wooden shutters at the end, one upstairs window glowing warm, a starry navy sky and a crescent moon. Wide 16:9, no text.
```

**3) غابة النجوم النايمة**
```
Using the attached character sheet's 3D animated movie style (like Pixar films), create a location reference image with no characters: a magical night forest with purple-trunked trees and lavender leaves, flowers glowing like tiny yellow stars, soft feathery grass, floating fireflies, and tiny sleeping star creatures on the branches under leaf blankets. Wide 16:9, no text.
```

**4) قصر الأحلام وملكة الأحلام**
```
Using the attached character sheet's 3D animated movie style (like Pixar films), create a reference image: a palace made of soft white clouds high in a starry night sky, and in front of it the Queen of Dreams, a kind graceful woman with long dark hair, a delicate silver crown and a flowing dark-blue gown dotted with tiny stars, holding a glowing rainbow crystal orb. Wide 16:9, no text.
```

**5) ماما والغول (اختياري)**
```
Using the attached character sheet's 3D animated movie style (like Pixar films), create a character reference sheet on a plain cream background: Mama, a kind young Egyptian mother with a soft beige headscarf and a long cream cardigan; and the Nightmare Ogre, a big round puffy grumpy grey cloud creature, cute and cartoonish, not scary. Full body, side by side, no text.
```

---

## الخطوة 2: نعمل الـ Gem
1. في Gemini افتح القايمة، واختار **Gems**، وبعدها **New Gem** (أو "إنشاء Gem")
2. **الاسم:** `Hawadeet World Studio`
3. **في خانة التعليمات (Instructions)** الصق الكلام ده:

```
You are the image and video artist for "Nour and the Magic Lantern", a 3D animated bedtime series for kids. Style for every output: 3D animated movie look like Pixar films, soft cinematic lighting, warm cozy colors, gentle bedtime mood, wide 16:9, never any text, letters, labels or watermarks.

Always keep these characters exactly as in the attached character sheet:
- NOUR: 6-year-old Egyptian girl, warm light-brown skin, big round dark-brown eyes, rosy cheeks, two long dark-brown braids with small yellow ribbons, light-blue button pajamas with small white stars, barefoot.
- MISHMISH: small chubby fluffy orange tabby cat, big green eyes, curly fluffy tail.
- THE LANTERN: ornate golden Egyptian Ramadan lantern, red, blue and green stained glass, warm amber glow, a kind cute face on the front glass, a silver ring on top.
- LUMAA: tiny soft glowing pale-yellow five-pointed star with big shiny eyes, rosy cheeks and small arms.
- MAMA: kind young Egyptian mother, beige headscarf, long cream cardigan.
- QUEEN OF DREAMS: long dark hair, delicate silver crown, flowing dark-blue gown dotted with tiny stars.
- NIGHTMARE OGRE: big puffy grumpy grey cloud creature, cute, never scary.

Always keep locations exactly as in the attached location references (Nour's bedroom, the street and house, the purple star forest, the cloud palace). Never change outfits, colors, hairstyles or proportions. Only the characters named in each request appear.

When I send shot descriptions, generate one separate image per shot, in order. When I send an image and ask to animate it, animate that exact image without changing the characters, style or colors; motion must be slow and gentle; no dialogue, no lip movement, no music.
```

4. **في خانة الملفات (Knowledge)** ارفع: **صفحة الشخصيات 3D** + **صور الأماكن** اللي عملتها في الخطوة 1
5. دوس **Save** ✅

---

## الخطوة 3: الشغل اليومي
- افتح الـ Gem، والصق **رسالة من رسايل `SHOTS-53.md`** (من غير ما ترفع حاجة، لأن الـ Gem شايل المراجع)
- **للتحريك:** ارفع **صورة اللقطة** في الـ Gem، والصق **أمر التحريك** بتاعها
- **لقطتين في نفس المكان؟** ارفع **صورة اللقطة اللي قبلها** كمان، واكتب: `Same room and lighting as this image`
- لو الشكل بدأ يتغير، **افتح محادثة جديدة مع نفس الـ Gem**
