# الحلقة 1 بستايل 3D: أوامر الصور والفيديو

## الخطة
**الجزء أ:** تعمل **22 صورة** في **Gemini**، صورة لكل مشهد، **وترفع صفحة الشخصيات 3D مع كل أمر**.
**الجزء ب:** تحرّك كل صورة في **Flow** (أو Gemini)، والمشاهد الطويلة تكمّلها بـ **Extend**، يعني **53 مقطع** في الحلقة كلها.

📌 سمّي كل صورة باسم المشهد (`scene-05.png`)، وكل مقطع برقم المشهد ورقم الجزء (`scene-05-1.mp4` و`scene-05-2.mp4`).
📌 لو مقطع ماطلعش، **عادي، كمّل**، وأنا هملا أي فراغ.

---

# الجزء أ: الصور (Gemini)

**في كل مرة:** ارفع `sheet3d-FINAL` وصورة المشهد الـ 2D بتاعه (من الـ ZIP القديم)، والصق السطر الثابت ده، وبعده وصف المشهد:

```
Use the first attached image as the character reference and the second attached image as the scene layout. Recreate this scene as a high-end 3D animated family movie frame: keep the characters exactly like the character reference, soft cinematic lighting, cozy bedtime mood, wide 16:9, no text, no letters. Only the characters described appear.
```

⚠️ لو رفعت **صورة واحدة بس** (صفحة الشخصيات)، **امسح** من الأمر الجزء ده: `and the second attached image as the scene layout`

| المشهد | الوصف (الصقه بعد السطر الثابت) |
|---|---|
| 01 | `Scene: magical deep-navy night sky with twinkling stars, lavender clouds and a crescent moon; the golden lantern with its kind face floats in the center glowing warm amber.` |
| 02 | `Scene: a cozy Egyptian house at the end of a quiet cobblestone street at night, one upstairs window glowing; through the window Nour sits on her bed with Mishmish the cat at her feet.` |
| 03 | `Scene: Nour's cozy bedroom lit by a night lamp; Mama (kind young Egyptian mother, beige headscarf, long cream cardigan) tucks Nour into bed; Nour points at an old unlit golden lantern on a wooden shelf; Mishmish sleeps at the foot of the bed.` |
| 04 | `Scene: dark bedroom in blue moonlight; Nour lies awake in bed looking at a crescent moon through the window; Mishmish sleeps at her feet; the old lantern sits unlit on a shelf.` |
| 05 | `Scene: the old lantern on the shelf starts glowing warm gold, light filling the room with floating sparkles; Nour sits up in bed amazed.` |
| 06 | `Scene: the glowing lantern floats beside the bed smiling; Nour peeks over her blanket pulled up to her nose, surprised and delighted.` |
| 07 | `Scene: Nour flies joyfully through the night sky holding the lantern's ring, above a sleeping Egyptian city with rooftops, minarets and twinkling lights; her braids flutter.` |
| 08 | `Scene: magical night forest with purple trees, flowers glowing like tiny stars, feathery grass, tiny sleeping stars on branches under leaf blankets; Nour and the lantern float down to land.` |
| 09 | `Scene: Nour tiptoes between purple trees with a hand behind her ear, listening; the lantern lights the path.` |
| 10 | `Scene: under a big purple tree, Lumaa sits crying, her glow weak and grey; Nour kneels beside her, kind and caring.` |
| 11 | `Scene: Nour sits on the grass with her hand on her cheek thinking; the lantern floats beside her smiling; dim Lumaa looks hopeful.` |
| 12 | `Scene: Nour and Lumaa laugh together among glowing flowers; Lumaa's glow grows brighter and warmer.` |
| 13 | `Scene: Lumaa shines bright and twirls up into the air leaving golden sparkles; Nour claps with delight below.` |
| 14 | `Scene: Lumaa back on the grass looks up worried at Nour; Nour leans in concerned; the lantern listens; a strange grey patch in the starry sky.` |
| 15 | `Scene: a palace of white clouds high in the night sky; the Queen of Dreams (long dark hair, silver crown, flowing dark-blue gown with tiny stars) holds a glowing rainbow crystal orb releasing colorful bubbles toward tiny sleeping houses below. Do not include Nour, the cat, the lantern or the star.` |
| 16 | `Scene: in the cloud palace, a big puffy grumpy grey cloud creature (cute, cartoonish, not scary) pushes toward the rainbow crystal; the Queen of Dreams looks startled as the orb tips. Do not include Nour, the cat, the lantern or the star.` |
| 17 | `Scene: the rainbow crystal breaks into eight glowing shards flying in different directions across the night sky toward magical worlds below: candy town, sea, fiery mountains, moon, forest, desert, island, cloud kingdom. No characters.` |
| 18 | `Scene: in the purple forest a soft blue beam of light descends; inside it the glowing Queen of Dreams smiles kindly at Nour; Nour looks up in awe with Lumaa and the lantern beside her.` |
| 19 | `Scene: close-up; the Queen of Dreams places a small silver necklace with eight empty star-shaped slots around Nour's neck; Nour holds it, shy but touched; soft blue magical light.` |
| 20 | `Scene: the team in the glowing purple forest: Nour smiling in the middle, the lantern on her right, bright Lumaa on her left; the silver necklace glimmers on Nour.` |
| 21 | `Scene: Nour asleep in her cozy bed with a gentle smile and the silver necklace; Mishmish sleeps at her feet; the lantern sits unlit on the shelf; one star outside the window shines brighter than the others.` |
| 22 | `Scene: peaceful deep-navy night sky with lavender clouds and a crescent moon; one small bright star twinkles; calm empty space in the center. No characters.` |

---

# الجزء ب: الفيديو (Flow أو Gemini)

**أول مقطع لكل مشهد:** ارفع صورة المشهد كـ **First frame**، والصق **"المقطع 1"**.
**المقاطع اللي بعده:** دوس **Extend** على المقطع اللي قبله، والصق **"تمديد"**.

**السطر ده ثابت في آخر كل أمر:**
`Keep the characters and 3D style exactly as in the image. Gentle, slow, calm bedtime-story motion. No text, no dialogue, no lip movement, no music.`

| مقطع | الأمر |
|---|---|
| **01-1** | `The lantern floats softly among the stars, bobbing gently while its glow pulses; stars twinkle; clouds drift; slow camera push-in.` |
| 01-2 (تمديد) | `The lantern slowly turns and smiles, sparkles drift around it; the camera keeps drifting closer.` |
| **02-1** | `Night street; window light flickers softly; stars twinkle; slow camera push-in toward the glowing window.` |
| 02-2 (تمديد) | `The camera arrives at the window: Nour sits on her bed smiling while Mishmish slowly flicks her tail.` |
| **03-1** | `Mama gently tucks the blanket around Nour and smiles; the night lamp glows; Mishmish breathes slowly.` |
| 03-2 (تمديد) | `Nour points curiously at the old lantern on the shelf; Mama looks at it and smiles warmly.` |
| 03-3 (تمديد) | `Mama kisses Nour's forehead and turns off the lamp; the room becomes dim and cozy.` |
| **04-1** | `Nour lies awake, turning left and right under her blanket; moonlight shimmers; Mishmish sleeps.` |
| 04-2 (تمديد) | `Nour looks at the moon through the window and whispers a wish with a hopeful face.` |
| **05-1** | `The old lantern on the shelf slowly begins to glow; tiny sparkles appear in the air.` |
| 05-2 (تمديد) | `The golden glow grows and fills the whole room like sunrise; Nour sits up in bed amazed.` |
| **06-1** | `The glowing lantern floats beside the bed and smiles; Nour peeks over her blanket pulled up to her nose.` |
| 06-2 (تمديد) | `The lantern bobs gently as if speaking kindly; Nour slowly lowers the blanket, curious.` |
| 06-3 (تمديد) | `Nour's surprise turns into a big happy smile; she sits up excited.` |
| 06-4 (تمديد) | `Nour bounces happily on the bed nodding yes; golden sparkles swirl around them.` |
| **07-1** | `The lantern's light wraps around Nour and she floats up out of the window holding its ring.` |
| 07-2 (تمديد) | `Nour flies happily over the sleeping city, braids fluttering; lights twinkle below.` |
| 07-3 (تمديد) | `Nour laughs with joy as they glide higher toward the stars; slow camera follow.` |
| **08-1** | `Nour and the lantern float down gently and land in the purple forest; glowing flowers pulse.` |
| 08-2 (تمديد) | `Nour looks around in wonder at the purple trees and the glowing flowers.` |
| 08-3 (تمديد) | `Camera slowly pans up to the tiny sleeping stars on the branches breathing under leaf blankets.` |
| **09-1** | `Nour tiptoes slowly between the trees with a hand behind her ear, listening; the lantern lights the path.` |
| **10-1** | `Lumaa sits under the tree sniffling, a small tear rolls down; Nour kneels beside her.` |
| 10-2 (تمديد) | `Nour gently reaches out to comfort her; Lumaa looks up with teary eyes.` |
| **11-1** | `Nour taps her cheek thinking; the lantern bobs beside her with a wise smile; Lumaa looks hopeful.` |
| **12-1** | `Nour tells a story with animated hands; Lumaa begins to smile.` |
| 12-2 (تمديد) | `Lumaa giggles and her glow grows brighter and warmer with each laugh.` |
| **13-1** | `Lumaa shines bright and lifts off the ground, spinning; Nour gasps happily.` |
| 13-2 (تمديد) | `Lumaa twirls in loops leaving golden sparkle trails, then floats back down slowly; Nour claps.` |
| **14-1** | `Lumaa lands on the grass looking worried; Nour leans closer, concerned.` |
| 14-2 (تمديد) | `The lantern floats closer to listen; the grey patch in the sky drifts slowly.` |
| **15-1** | `The Queen holds the glowing rainbow crystal; colorful bubbles float out one by one.` |
| 15-2 (تمديد) | `The bubbles drift slowly down toward the tiny sleeping houses far below.` |
| 15-3 (تمديد) | `Camera follows one bubble gently entering a window of a sleeping child's house.` |
| **16-1** | `The puffy grumpy cloud creature pushes toward the crystal; the Queen looks startled; the orb wobbles. Cute, not scary.` |
| **17-1** | `The crystal breaks into eight glowing shards that fly slowly outward, trailing ribbons of light.` |
| 17-2 (تمديد) | `The shards fall gently toward the faraway magical worlds below; stars twinkle.` |
| **18-1** | `A soft blue beam of light shimmers down into the forest; Nour looks up in awe.` |
| 18-2 (تمديد) | `The glowing Queen appears inside the beam and smiles kindly at Nour; sparkles float.` |
| **19-1** | `The Queen gently fastens the silver necklace around Nour's neck.` |
| 19-2 (تمديد) | `Nour holds the necklace with both hands and looks down at it shyly.` |
| 19-3 (تمديد) | `Nour slowly looks up with a small brave smile; blue sparkles drift.` |
| **20-1** | `Lumaa flies to Nour's side smiling; the lantern glows brighter beside her.` |
| 20-2 (تمديد) | `Nour smiles her biggest smile between her two friends; the necklace glimmers.` |
| 20-3 (تمديد) | `The necklace sparkles briefly and Lumaa sniffs the air curiously, surprised.` |
| 20-4 (تمديد) | `Nour yawns sleepily; the lantern's golden light gently wraps around them.` |
| **21-1** | `Nour sleeps peacefully, breathing slowly; Mishmish breathes at her feet.` |
| 21-2 (تمديد) | `The lantern on the shelf seems to smile softly; very slow camera push-in.` |
| 21-3 (تمديد) | `The star outside the window twinkles softly like a wink.` |
| 21-4 (تمديد) | `Nour touches the necklace in her sleep and smiles; the room stays calm and dim.` |
| **22-1** | `Peaceful night sky; the small bright star twinkles gently; clouds drift very slowly.` |
| 22-2 (تمديد) | `The moon glows softly; the camera drifts slowly upward; very calm and sleepy.` |
| 22-3 (تمديد) | `The scene slowly fades darker and calmer; the little star twinkles one last time.` |

**المجموع: 53 مقطع** 🎬
