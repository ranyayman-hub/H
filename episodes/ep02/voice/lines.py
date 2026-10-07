"""Episode 2 (Candy City, extended draft 2) dialogue, one entry per spoken line: (scene, speaker, text).
Text in [brackets] is an eleven_v3 audio direction, not spoken.
Diacritics are added only where Egyptian pronunciation would otherwise drift.
SFX entries use speaker 'SFX' and an English description."""

VOICES = {
    'nour':     '09Q2MhEvwEP3ijEBee1i',  # Nour - Hawadeet World (designed)
    'fanoos':   'x6fvBLXv9YxzoVJQ0wp6',  # Momen - warm, mature, calm
    'lumaa':    'jDniWbMLsNWghA1TR3e3',  # Lumaa - Hawadeet World (designed)
    'mama':     'JHdGl5PsEzushIzzVSd1',  # Heba - soothing, Egyptian
    'baskota':  'K1k67X4shfgkvQtLXCQf',  # Baskota - Hawadeet World (designed, pick 1)
}

L = [
    # 1 — the lantern greets the children, recap
    (1, 'fanoos', '[warmly] أهلًا يا أصحابي... أهلًا بيكم تاني في عالم الحواديت.'),
    (1, 'fanoos', 'فاكرين المرّة اللي فاتت؟ غول الكوابيس كسر بلّورة الأحلام تمن حِتَت... وكل حِتّة وقعت في عالم بعيد.'),
    (1, 'fanoos', '[gently] ونور، ومعاها لُمعة النجمة الصغيرة وأنا، وعدنا ملكة الأحلام إننا نرجّعهم كلهم.'),
    (1, 'fanoos', '[softly] والليلة دي... رايحين ندوّر على أوّل حِتّة. يلا، اتغطّوا كويس... وتعالوا معايا.'),

    # 2 — Mama and the chocolate
    (2, 'SFX', 'soft clink of small plates, a cute cat meows once, quiet evening'),
    (2, 'nour', '[pleading] ماما... ممكن حِتّة شوكولاتة كمان؟ آخر حِتّة والله!'),
    (2, 'mama', '[laughs softly] دي التالتة يا نور! إنتي خدتي حِتّتين بعد العشا.'),
    (2, 'nour', '[whining] بس هي حلوة أوي يا ماما...'),
    (2, 'mama', '[tenderly] عشان هي حلوة لازم ناكلها بالراحة يا حبيبتي. الحِلو حِلو لما يبقى حِتّة صغيرة... مش لما ناكل العلبة كلها.'),
    (2, 'nour', '[sighs] حاضر يا ماما...'),
    (2, 'mama', '[softly] يلا يا قمر، النوم. تصبحي على خير.'),
    (2, 'nour', '[sleepy] وإنتي من أهله يا ماما.'),
    (2, 'SFX', 'a soft kiss sound then a gentle click of a lamp switch turning off'),

    # 3 — the lantern glows, Lumaa at the window
    (3, 'SFX', 'a gentle magical chime as a warm light glows up'),
    (3, 'nour', '[whispers] يا فانوس... إنت صاحي؟'),
    (3, 'fanoos', '[chuckles] أنا دايمًا صاحي لما تكوني محتاجاني يا نور.'),
    (3, 'SFX', 'tiny tapping on a window glass, tink tink'),
    (3, 'lumaa', '[excited] نور! نور! أنا هنا!'),
    (3, 'nour', '[happy] لُمعة! وحشتيني!'),
    (3, 'lumaa', '[excited] يلا بسرعة! العُقد بيلمع... يعني حِتّة البلّورة قريبة!'),

    # 4 — flying
    (4, 'fanoos', 'امسكي الحلقة كويس... وعِدّي معايا.'),
    (4, 'nour', '[excited] واحد... اتنين... تلاتة!'),
    (4, 'SFX', 'soft whoosh of wind, magical flying sparkle sound'),
    (4, 'lumaa', '[sniffs] شامّة الريحة دي يا نور؟ شوكولاتة... وفانيليا... وفراولة!'),
    (4, 'nour', '[laughs] بطني بتزقزق من دلوقتي!'),

    # 5 — Candy City
    (5, 'SFX', 'cheerful tiny bells and a soft sparkling magical ambience'),
    (5, 'nour', '[amazed] واااو! البيوت معمولة من البسكوت! والشبابيك من السُّكّر الملوّن!'),
    (5, 'lumaa', '[delighted] وبُصّي يا نور! نهر شوكولاتة!'),
    (5, 'fanoos', 'والشجر ده كله غزل البنات... والأعمدة اللي في الشارع مصّاصات!'),
    (5, 'fanoos', '[amused] وشايفة النافورة دي؟ بتطلّع عصير فراولة بدل المية!'),
    (5, 'nour', '[laughs] لو مشمش شافت المدينة دي... كانت هتاكل الرصيف كله!'),
    (5, 'nour', '[amazed] دي أحلى مدينة شُفتها في حياتي!'),

    # 6 — Baskota
    (6, 'baskota', '[cheerful, loud] أهلًا أهلًا أهلًا! نوّرتوا مدينة الحلويات!'),
    (6, 'nour', '[startled] إنت... إنت بسكوتة بتتكلم؟!'),
    (6, 'baskota', '[laughs] اسمي بسكوتة! أنا الدليل بتاع المدينة. ومين النجمة الحلوة دي؟'),
    (6, 'lumaa', '[cheerful] أنا لُمعة! وده الفانوس، ودي صاحبتي نور.'),
    (6, 'fanoos', 'إحنا بندوّر على حِتّة من بلّورة الأحلام يا بسكوتة. شُفت حاجة بتلمع وقعت من السما؟'),
    (6, 'baskota', '[excited] آه! وقعت من كام يوم فوق جبل التورتة... على الكريزة اللي فوق خالص!'),

    # 7 — the cotton-candy cloud ride
    (7, 'baskota', 'الطريق لجبل التورتة طويل... اركبوا معايا سحابة غزل البنات!'),
    (7, 'nour', '[excited] سحابة من غزل البنات؟! هي مش هتدوب؟'),
    (7, 'baskota', '[laughs] لا يا ستّي، دي سحابة سحرية... بس ماتاكليش منها!'),
    (7, 'SFX', 'a soft magical whoosh of a floating cloud, gentle wind chimes'),
    (7, 'lumaa', '[excited] نور! بُصّي... فراشات من الحلوى الملوّنة بتطير جنبنا!'),
    (7, 'nour', '[laughs] واحدة حمرا... واتنين خضرا... وتلاتة صفرا!'),
    (7, 'fanoos', '[warmly, to the children] يلا يا أصحابي، عِدّوا معانا! كام فراشة شُفتوا؟'),
    (7, 'nour', '[giggles] تلاتة! برافو عليكم!'),

    # 8 — Nour eats and eats
    (8, 'baskota', 'بس الطريق طويل. ولو جعانين، كل حاجة هنا ممكن تتّاكل!'),
    (8, 'nour', '[delighted] بجد؟! [munching] مممم... المصّاصة دي طعمها فراولة!'),
    (8, 'nour', '[munching] والبونبوناية دي طعمها لمون! ودي... كراميل!'),
    (8, 'lumaa', '[worried] نور... كفاية كده؟'),
    (8, 'nour', '[mouth full] واحدة كمان بس! ومصّاصة كمان... وحِتّة غزل بنات...'),
    (8, 'fanoos', '[calmly] نور يا حبيبتي... إحنا لسه في أوّل الطريق.'),

    # 9 — the jelly bridge
    (9, 'SFX', 'wobbly jelly bouncing sounds, boing boing'),
    (9, 'baskota', 'لازم نعدّي جسر الجيلي ده عشان نوصل للجبل. بننُطّ نطّة نطّة!'),
    (9, 'lumaa', '[playful] بوينج! بوينج! سهلة خالص!'),
    (9, 'nour', '[groans] آه... استنّوا... بطني بتوجعني أوي...'),
    (9, 'nour', '[almost crying] مش قادرة أنُطّ... حاسّة إني تقيلة.'),

    # 10 — the story of King Sukkar
    (10, 'baskota', '[gently] تعرفي يا نور؟ زمان كان عندنا ملك اسمه الملك سُكّر. كان بياكل كل حاجة حلوة يشوفها...'),
    (10, 'baskota', '[laughs] أكل الشبابيك... والأبواب... ونُصّ نهر الشوكولاتة! لحد ما بطنه وجعته ونام مية سنة!'),
    (10, 'nour', '[weak laugh] مية سنة؟!'),
    (10, 'fanoos', '[warmly] الحلويات حلوة يا نور... بس الحِلو حِلو لما يبقى بمقدار. حِتّة صغيرة بتفرّحنا، والكتير بيتعبنا.'),
    (10, 'nour', '[quietly] ماما قالتلي نفس الكلام النهارده...'),

    # 11 — the mint spring
    (11, 'baskota', 'تعالي! هنا عندنا نبع النعناع. اشربي شويّة... هيريّح بطنك.'),
    (11, 'SFX', 'gentle trickling spring water'),
    (11, 'nour', '[drinks, relieved] آه... ساقعة وحلوة... [breathes out] أنا أحسن خالص.'),
    (11, 'nour', '[determined] خلاص... من دلوقتي هاكل حِتّة صغيرة بس، وأستمتع بيها بالراحة.'),
    (11, 'lumaa', '[happy] برافو يا نور!'),

    # 12 — crossing the bridge
    (12, 'baskota', '[cheerful] جاهزين؟ نطّة... نطّة... نطّة!'),
    (12, 'nour', '[laughs] بوينج! بوينج! أنا خفيفة زي الريشة!'),
    (12, 'lumaa', '[excited] وصلنا جبل التورتة!'),

    # 13 — the riddle gate
    (13, 'SFX', 'a soft deep magical gong'),
    (13, 'baskota', '[worried] آه لأ... بوابة الألغاز! مابتتفتحش غير لما حد يحلّ اللغز المكتوب عليها.'),
    (13, 'lumaa', 'يا فانوس، اقرا اللغز!'),
    (13, 'fanoos', '[playful, reading] حاجة بيضا وحلوة... بتدوب في الشاي... ولو كتّرنا منها، سنانّا تزعل... أنا مين؟'),
    (13, 'nour', '[thinking] بيضا... وحلوة... وبتدوب في الشاي...'),
    (13, 'fanoos', '[to the children] فكّروا معانا يا أصحابي... عرفتوا؟'),
    (13, 'nour', '[happy] السُّكّر! هو السُّكّر!'),
    (13, 'SFX', 'a magical gate swinging open with a sparkling chime'),
    (13, 'baskota', '[cheering] البوابة اتفتحت! إنتي شاطرة أوي يا نور!'),
    (13, 'nour', '[proud, laughing] عشان دلوقتي دماغي صاحية... مش بطني بس اللي مليانة!'),
    (13, 'lumaa', '[laughs] ههههه!'),

    # 14 — the crystal shard
    (14, 'SFX', 'a big warm magical chime, sparkling shimmer'),
    (14, 'nour', '[amazed] بُصّوا! فوق الكريزة... بتلمع بلون بمبي!'),
    (14, 'fanoos', '[softly] دي هي يا نور... أوّل حِتّة من بلّورة الأحلام.'),
    (14, 'nour', '[gasps] حطّيتها في العُقد... بُصّوا! العُقد نوّر!'),
    (14, 'lumaa', '[cheering] واحدة من تمانية!'),
    (14, 'baskota', '[cheering] هييييه! الأطفال هيحلموا أحلام حلوة تاني!'),

    # 15 — Baskota's gift
    (15, 'baskota', 'يا نور، خُدي دي هدية منّي... أحلى بونبوناية في المدينة كلها.'),
    (15, 'nour', '[thoughtful] شكرًا يا بسكوتة... بس مش هاكلها دلوقتي.'),
    (15, 'nour', '[warmly] هاخدها لماما بكرة الصبح... ونقسمها سوا.'),
    (15, 'fanoos', '[proudly] هو ده يا نور. الحِلو أحلى لما نتقاسمه.'),

    # 16 — going home
    (16, 'nour', '[yawns] هااااا... مع السلامة يا بسكوتة!'),
    (16, 'baskota', '[cheerful] مع السلامة يا أصحابي! تعالوا تاني... بس كُلوا بالراحة!'),
    (16, 'SFX', 'soft calm whoosh of wind'),

    # 17 — Nour asleep
    (17, 'nour', '[whispers] هحطّ البونبوناية هنا جنب المخدة... والصبح أوّل حاجة هعملها، هقسمها مع ماما.'),
    (17, 'fanoos', '[softly] وأنا متأكد إن ماما هتفرح بيها أوي... أكتر من أي شوكولاتة في الدنيا.'),
    (17, 'nour', '[whispers] تصبحي على خير يا لُمعة...'),
    (17, 'lumaa', '[distant whisper] وإنتي من أهله يا نور.'),
    (17, 'fanoos', '[whispers] ودلوقتي جه دورك إنت يا حبيبي... خُد نفس كبير زي ريحة الشوكولاتة... وطلّعه بالراحة... وغمّض عينيك.'),

    # 18 — closing
    (18, 'fanoos', '[calmly] وفي الحلقة الجاية... هنقابل تنين كبير أوي... بس خايف من الضلمة! تصبحوا على خير... وأحلام سعيدة.'),
]
