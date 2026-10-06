"""Episode 2 (Candy City) dialogue, one entry per spoken line: (scene, speaker, text).
Text in [brackets] is an eleven_v3 audio direction, not spoken.
Diacritics are added only where Egyptian pronunciation would otherwise drift.
SFX entries use speaker 'SFX' and an English description."""

VOICES = {
    'nour':     '09Q2MhEvwEP3ijEBee1i',  # Nour - Hawadeet World (designed)
    'fanoos':   'x6fvBLXv9YxzoVJQ0wp6',  # Momen - warm, mature, calm
    'lumaa':    'jDniWbMLsNWghA1TR3e3',  # Lumaa - Hawadeet World (designed)
    'mama':     'JHdGl5PsEzushIzzVSd1',  # Heba - soothing, Egyptian
    'baskota':  None,                    # Baskota - to be designed (playful gingerbread boy)
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
    (5, 'nour', '[amazed] دي أحلى مدينة شُفتها في حياتي!'),

    # 6 — Baskota
    (6, 'baskota', '[cheerful, loud] أهلًا أهلًا أهلًا! نوّرتوا مدينة الحلويات!'),
    (6, 'nour', '[startled] إنت... إنت بسكوتة بتتكلم؟!'),
    (6, 'baskota', '[laughs] اسمي بسكوتة! أنا الدليل بتاع المدينة. ومين النجمة الحلوة دي؟'),
    (6, 'lumaa', '[cheerful] أنا لُمعة! وده الفانوس، ودي صاحبتي نور.'),
    (6, 'fanoos', 'إحنا بندوّر على حِتّة من بلّورة الأحلام يا بسكوتة. شُفت حاجة بتلمع وقعت من السما؟'),
    (6, 'baskota', '[excited] آه! وقعت من كام يوم فوق جبل التورتة... على الكريزة اللي فوق خالص!'),

    # 7 — Nour eats and eats
    (7, 'baskota', 'بس الطريق طويل. ولو جعانين، كل حاجة هنا ممكن تتّاكل!'),
    (7, 'nour', '[delighted] بجد؟! [munching] مممم... الشبّاك ده طعمه فراولة!'),
    (7, 'nour', '[munching] وده طعمه لمون! وده... كراميل!'),
    (7, 'lumaa', '[worried] نور... كفاية كده؟'),
    (7, 'nour', '[mouth full] واحدة كمان بس! ومصّاصة كمان... وحِتّة غزل بنات...'),
    (7, 'fanoos', '[calmly] نور يا حبيبتي... إحنا لسه في أوّل الطريق.'),

    # 8 — the jelly bridge
    (8, 'SFX', 'wobbly jelly bouncing sounds, boing boing'),
    (8, 'baskota', 'لازم نعدّي جسر الجيلي ده عشان نوصل للجبل. بننُطّ نطّة نطّة!'),
    (8, 'lumaa', '[playful] بوينج! بوينج! سهلة خالص!'),
    (8, 'nour', '[groans] آه... استنّوا... بطني بتوجعني أوي...'),
    (8, 'nour', '[almost crying] مش قادرة أنُطّ... حاسّة إني تقيلة.'),

    # 9 — the story of King Sukkar
    (9, 'baskota', '[gently] تعرفي يا نور؟ زمان كان عندنا ملك اسمه الملك سُكّر. كان بياكل كل حاجة حلوة يشوفها...'),
    (9, 'baskota', '[laughs] أكل الشبابيك... والأبواب... ونُصّ نهر الشوكولاتة! لحد ما بطنه وجعته ونام مية سنة!'),
    (9, 'nour', '[weak laugh] مية سنة؟!'),
    (9, 'fanoos', '[warmly] الحلويات حلوة يا نور... بس الحِلو حِلو لما يبقى بمقدار. حِتّة صغيرة بتفرّحنا، والكتير بيتعبنا.'),
    (9, 'nour', '[quietly] ماما قالتلي نفس الكلام النهارده...'),

    # 10 — the mint spring
    (10, 'baskota', 'تعالي! هنا عندنا نبع النعناع. اشربي شويّة... هيريّح بطنك.'),
    (10, 'SFX', 'gentle trickling spring water'),
    (10, 'nour', '[drinks, relieved] آه... ساقعة وحلوة... [breathes out] أنا أحسن خالص.'),
    (10, 'nour', '[determined] خلاص... من دلوقتي هاكل حِتّة صغيرة بس، وأستمتع بيها بالراحة.'),
    (10, 'lumaa', '[happy] برافو يا نور!'),

    # 11 — crossing the bridge
    (11, 'baskota', '[cheerful] جاهزين؟ نطّة... نطّة... نطّة!'),
    (11, 'nour', '[laughs] بوينج! بوينج! أنا خفيفة زي الريشة!'),
    (11, 'lumaa', '[excited] وصلنا جبل التورتة!'),

    # 12 — the crystal shard
    (12, 'SFX', 'a big warm magical chime, sparkling shimmer'),
    (12, 'nour', '[amazed] بُصّوا! فوق الكريزة... بتلمع بلون بمبي!'),
    (12, 'fanoos', '[softly] دي هي يا نور... أوّل حِتّة من بلّورة الأحلام.'),
    (12, 'nour', '[gasps] حطّيتها في العُقد... بُصّوا! العُقد نوّر!'),
    (12, 'lumaa', '[cheering] واحدة من تمانية!'),
    (12, 'baskota', '[cheering] هييييه! الأطفال هيحلموا أحلام حلوة تاني!'),

    # 13 — Baskota's gift
    (13, 'baskota', 'يا نور، خُدي دي هدية منّي... أحلى بونبوناية في المدينة كلها.'),
    (13, 'nour', '[thoughtful] شكرًا يا بسكوتة... بس مش هاكلها دلوقتي.'),
    (13, 'nour', '[warmly] هاخدها لماما بكرة الصبح... ونقسمها سوا.'),
    (13, 'fanoos', '[proudly] هو ده يا نور. الحِلو أحلى لما نتقاسمه.'),

    # 14 — going home
    (14, 'nour', '[yawns] هااااا... مع السلامة يا بسكوتة!'),
    (14, 'baskota', '[cheerful] مع السلامة يا أصحابي! تعالوا تاني... بس كُلوا بالراحة!'),
    (14, 'SFX', 'soft calm whoosh of wind'),

    # 15 — Nour asleep
    (15, 'nour', '[whispers] تصبحي على خير يا لُمعة...'),
    (15, 'lumaa', '[distant whisper] وإنتي من أهله يا نور.'),
    (15, 'fanoos', '[whispers] ودلوقتي جه دورك إنت يا حبيبي... خُد نفس كبير زي ريحة الشوكولاتة... وطلّعه بالراحة... وغمّض عينيك.'),

    # 16 — closing
    (16, 'fanoos', '[calmly] وفي الحلقة الجاية... هنقابل تنين كبير أوي... بس خايف من الضلمة! تصبحوا على خير... وأحلام سعيدة.'),
]
