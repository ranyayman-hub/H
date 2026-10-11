"""Episode 3 (The dragon who is afraid of the dark) dialogue, one entry per line: (scene, speaker, text).
Text in [brackets] is an eleven_v3 audio direction, not spoken.
Diacritics are added only where Egyptian pronunciation would otherwise drift.
SFX entries use speaker 'SFX' and an English description.
'sharara' has no voice yet: design one (small, sweet, shy young dragon) before generating."""

VOICES = {
    'nour':    '09Q2MhEvwEP3ijEBee1i',  # Nour - Hawadeet World (designed)
    'fanoos':  'x6fvBLXv9YxzoVJQ0wp6',  # Momen - warm, mature, calm
    'lumaa':   'jDniWbMLsNWghA1TR3e3',  # Lumaa - Hawadeet World (designed)
    'mama':    'JHdGl5PsEzushIzzVSd1',  # Heba - soothing, Egyptian
    'sharara': None,                    # TODO: design
}

L = [
    # 1 — cold open: a dark cave, two big glowing eyes
    (1, 'SFX', 'soft echoing drips of water in a big dark cave, a low gentle rumble'),
    (1, 'sharara', '[deep, trying to sound scary] غررررر!'),
    (1, 'sharara', '[small voice, shaky, almost crying] حد هنا؟... أنا... أنا خايف.'),

    # 2 — logo (no dialogue)

    # 3 — the lantern in the sky, short recap
    (3, 'fanoos', '[warmly] أهلًا يا أصحابي! فاكرين؟ نور جابت حتّتين من بلّورة الأحلام...'),
    (3, 'fanoos', '[mysteriously] والليلة... هنروح نجيب الحِتّة التالتة. بس الأول... تعالوا نشوف نور بتعمل إيه.'),

    # 4 — bedtime with Mama
    (4, 'mama', '[softly] يلا يا نور، غسلتي سنانك؟ ولبستي البيجامة؟'),
    (4, 'nour', '[proudly] أيوة يا ماما! وكمان رتّبت لعبي.'),
    (4, 'mama', '[warmly] شاطرة يا حبيبتي. يلا، هطفّي النور بقى.'),
    (4, 'nour', '[a little scared] لأ يا ماما! استني... ممكن تسيبي النور شوية؟'),
    (4, 'mama', '[gently] ليه يا قمر؟ إنتي خايفة؟'),
    (4, 'nour', '[shyly] شوية صغيرين... الأوضة بتبقى ضلمة أوي... وببقى حاسّة إن فيه حاجة في الركن.'),
    (4, 'mama', '[tenderly] تعالي هنا. الأوضة في الضلمة هي هي نفس الأوضة بالنهار... نفس السرير، ونفس الدولاب، ونفس الدبدوب.'),
    (4, 'mama', '[warmly] بس عشان خاطرك، هسيبلك اللمبة الصغيرة دي منوّرة. اتفقنا؟'),
    (4, 'nour', '[curious] ماما... إنتي كنتي بتخافي من الضلمة وإنتي صغيرة؟'),
    (4, 'mama', '[smiles] أيوة طبعًا! وتيتة كانت بتقولّي: الضلمة دي بطانية كبيرة الدنيا بتتغطّى بيها عشان تنام.'),
    (4, 'nour', '[giggles] بطانية كبيرة! حلوة دي.'),
    (4, 'nour', '[relieved] اتفقنا! تصبحي على خير يا ماما.'),
    (4, 'mama', '[softly] وإنتي من أهله يا روحي.'),
    (4, 'SFX', 'a soft kiss, footsteps leaving, a door closing gently'),

    # 5 — the lantern wakes, Lumaa at the window
    (5, 'SFX', 'a gentle magical chime as a warm light glows up'),
    (5, 'fanoos', '[softly] نور... نور... صاحية؟'),
    (5, 'nour', '[happy whisper] الفانوس! إنت نوّرت!'),
    (5, 'SFX', 'tiny tapping on a window glass, tink tink'),
    (5, 'lumaa', '[excited] نور! نور! افتحي الشباك!'),
    (5, 'nour', '[happy] لُمعة! وحشتيني!'),
    (5, 'lumaa', '[excited] لقيت الحِتّة التالتة! بتلمع بنفسجي... في جبال الكريستال!'),
    (5, 'fanoos', '[calmly] يبقى يلا بينا. امسكي إيدي يا نور... وما تخافيش.'),

    # 6 — flying over the crystal mountains, echo game
    (6, 'SFX', 'soft whoosh of wind, magical flying sparkle sound'),
    (6, 'nour', '[amazed] واااو! الجبال كلها بتلمع... بنفسجي وأزرق!'),
    (6, 'fanoos', '[warmly] وبصّي تحت يا نور... الشلالات بتنزل مية بتلمع زي الألماظ.'),
    (6, 'nour', '[delighted] وفيه قوس قزح صغيّر فوق المية!'),
    (6, 'lumaa', '[giggles] ده بيطلع بس للأطفال اللي قلبهم طيب!'),
    (6, 'lumaa', '[playful] دي جبال الكريستال! ولو قلتي حاجة بصوت عالي... الجبل بيرد عليكي!'),
    (6, 'nour', '[calling out, playful] هالووو!'),
    (6, 'SFX', 'a soft echo repeating hello hello hello, fading'),
    (6, 'nour', '[laughs] ههههه! الجبل قال هالو!'),
    (6, 'fanoos', '[warmly, to the children] يلا يا أصحابي، قولوا معانا: هالووو!'),
    (6, 'nour', '[laughs] والجبل رد عليكم كلكم! يلا تاني... بصوت أعلى: هالووو!'),
    (6, 'SFX', 'a soft echo repeating hello hello hello, fading'),
    (6, 'SFX', 'a soft echo repeating hello hello hello, fading'),
    (6, 'lumaa', '[pointing] بصّوا! الحِتّة هناك... جوه الكهف الكبير ده!'),

    # 7 — the cave entrance
    (7, 'SFX', 'soft echoing drips of water in a big dark cave, a low gentle rumble'),
    (7, 'nour', '[nervous] الكهف... ضلمة أوي.'),
    (7, 'sharara', '[distant, small, sniffling] هئ... هئ...'),
    (7, 'nour', '[scared whisper] سامعين؟ فيه حد بيعيّط جوه!'),
    (7, 'lumaa', '[gently] ما تخافيش يا نور... أنا جنبك. امسكي إيدي.'),
    (7, 'fanoos', '[calmly] اللي بيعيّط ده... محتاج مساعدة. يلا ندخل بالراحة.'),

    # 8 — meeting Sharara
    (8, 'nour', '[softly] مين هنا؟... إحنا أصحاب.'),
    (8, 'sharara', '[hiding, muffled] إ... إنتو مش وحوش؟'),
    (8, 'lumaa', '[giggles] وحوش؟ أنا نجمة صغيرة! ودي نور... ودا الفانوس.'),
    (8, 'sharara', '[peeking, shy] أنا شرارة... أنا تنين.'),
    (8, 'nour', '[surprised, happy] تنين؟! بس إنت صغيّر وحلو أوي!'),
    (8, 'sharara', '[sniffs, then a tiny sneeze] هاا... هاا... هاتشي!'),
    (8, 'SFX', 'a tiny cute sneeze with a few crackling sparkles'),
    (8, 'lumaa', '[laughing] ههههه! عطس شرارات صغيّرة!'),
    (8, 'sharara', '[giggles shyly] آسف... بيحصل لما بتكسف.'),
    (8, 'sharara', '[embarrassed] أنا عملت غررر عشان أخوّفكم... عشان أنا اللي كنت خايف.'),
    (8, 'nour', '[laughs softly] ما تقلقش... إحنا كمان اتخضّينا شوية.'),
    (8, 'fanoos', '[kindly] أهلًا يا شرارة. ليه بتعيّط يا صغيّر؟'),

    # 9 — the problem
    (9, 'sharara', '[sad] كنت بلعب برّه... ولقيت حاجة بنفسجي بتلمع وقعت من السما.'),
    (9, 'sharara', '[sad] دحرجت... ودحرجت... ودخلت جوّه الكهف خالص.'),
    (9, 'lumaa', '[excited] دي حِتّة البلّورة اللي بندوّر عليها!'),
    (9, 'sharara', '[ashamed, quiet] بس... أنا مش قادر أدخل وراها. الكهف من جوّه ضلمة... ضلمة خالص.'),
    (9, 'nour', '[surprised] بس إنت تنين! والتنين بيطلّع نار!'),
    (9, 'sharara', '[very small voice] أيوة... بس أنا بخاف من الضلمة. والتنين اللي بيخاف من الضلمة... أكيد تنين مش شاطر.'),

    # 10 — Nour admits it, breathing exercise
    (10, 'nour', '[gently] تعرف يا شرارة؟... أنا كمان بخاف من الضلمة.'),
    (10, 'sharara', '[surprised] بجد؟!'),
    (10, 'nour', '[honest] بجد. النهارده طلبت من ماما تسيب النور منوّر. الخوف مش عيب.'),
    (10, 'fanoos', '[warmly] كلنا بنخاف ساعات يا شرارة. وفيه سر صغير بيخلّي الخوف يهدى.'),
    (10, 'nour', '[playful] أنا عارفاه! اسمه: شُمّ الوردة... وطفّي الشمعة!'),
    (10, 'nour', '[slowly] تاخد نفس من مناخيرك بالراحة... زي ما بتشمّ وردة حلوة...'),
    (10, 'nour', '[slowly] وتطلّعه من بُقّك بالراحة... زي ما بتطفّي شمعة.'),
    (10, 'fanoos', '[to the children, softly] يلا يا أصحابي، جرّبوا معانا... شُمّوا الوردة... وطفّوا الشمعة.'),
    (10, 'sharara', '[breathing, calmer] شُمّ الوردة... وطفّي الشمعة... [happy] أنا حاسس إني أحسن!'),

    # 11 — inside the cave, counting steps, fireflies
    (11, 'lumaa', '[softly] أنا هنوّر قدّامكم... امسكوا إيدين بعض.'),
    (11, 'nour', '[brave] يلا يا شرارة. هنمشي سوا... ونعدّ خطواتنا!'),
    (11, 'nour', '[counting] واحد... اتنين... تلاتة...'),
    (11, 'fanoos', '[to the children, softly] عِدّوا معانا يا أصحابي... أربعة... خمسة...'),
    (11, 'SFX', 'tiny soft magical twinkles, gentle sparkles appearing'),
    (11, 'sharara', '[amazed whisper] إيه دا؟! نجوم صغيرة جوّه الكهف!'),
    (11, 'lumaa', '[happy] دول يراعات! بينوّروا عشان يقولوا لنا: أهلًا!'),
    (11, 'nour', '[playful] يلا نعدّهم! واحدة صفرا... واتنين خضرا... وتلاتة زرقا!'),
    (11, 'fanoos', '[to the children] كام يراعة شُفتوا يا أصحابي؟ عدّوا معانا على صوابعكم!'),
    (11, 'sharara', '[giggles] ستة! ستة يراعات! أنا عدّيت لوحدي!'),
    (11, 'nour', '[soft wonder] شفت يا شرارة؟ الضلمة فيها حاجات حلوة كمان.'),

    # 12 — the crystal bridge
    (12, 'sharara', '[trembling] لأ لأ... كوبري؟! وتحته... ضلمة خالص!'),
    (12, 'nour', '[calm and kind] بُصّ لي أنا بس يا شرارة. ما تبُصّش تحت.'),
    (12, 'fanoos', '[gently] ونفس الوردة... ونفس الشمعة.'),
    (12, 'sharara', '[breathing] شُمّ الوردة... وطفّي الشمعة...'),
    (12, 'nour', '[encouraging] خطوة... وخطوة... وخطوة كمان... برافو عليك!'),
    (12, 'sharara', '[surprised, proud] أنا عدّيت! أنا عدّيت الكوبري!'),

    # 13 — the big moment: Lumaa fades, Sharara breathes fire, crystals light up
    (13, 'lumaa', '[weak, tired] نور... أنا... نوري بيخلص... أنا تعبت شوية...'),
    (13, 'SFX', 'a soft magical light fading out, quiet hum'),
    (13, 'nour', '[worried] لُمعة! الدنيا ضلمت!'),
    (13, 'sharara', '[scared] الضلمة رجعت!'),
    (13, 'fanoos', '[calm, steady] شرارة... إنت تقدر. افتكر السر.'),
    (13, 'sharara', '[deep breath] شُمّ الوردة... [determined] وطفّي... [shouting bravely] لأ! ونوّر الشمعة!'),
    (13, 'SFX', 'a small cute dragon puff of warm fire, then a huge magical sparkling shimmer as many crystals light up'),
    (13, 'nour', '[amazed] وااااو! شرارة! الكهف كله نوّر!'),
    (13, 'lumaa', '[recovering, happy] الكريستال كله بيلمع بالألوان! أحمر... وأزرق... وأخضر!'),
    (13, 'sharara', '[amazed, laughing] أنا عملت كده؟! أنا نوّرت الضلمة!'),
    (13, 'fanoos', '[to the children, playful] يا أصحابي... إيه أكتر لون بتحبّوه في الكريستال؟ قولوه بصوت عالي!'),
    (13, 'nour', '[happy] أنا بحب البنفسجي... لون شرارة!'),
    (13, 'sharara', '[proud, giggling] وأنا بحب كل الألوان... عشان أنا اللي نوّرتها!'),

    # 14 — the shard
    (14, 'nour', '[excited] بصّوا! هناك... فوق الكريستالة الكبيرة!'),
    (14, 'SFX', 'a big warm magical chime, sparkling shimmer'),
    (14, 'lumaa', '[happy] الحِتّة البنفسجي!'),
    (14, 'fanoos', '[warmly] يلا يا نور... حطّيها في العقد.'),
    (14, 'SFX', 'a soft magical click and a sparkling chime'),
    (14, 'nour', '[happy] تلات حتت! فاضل خمسة بس!'),
    (14, 'fanoos', '[to the children] والأطفال في كل حتّة في الدنيا... هيحلموا أحلام أحلى الليلة.'),

    # 15 — goodbye, the lesson, a gift
    (15, 'sharara', '[proud] أنا مش خايف تاني!'),
    (15, 'fanoos', '[wisely, warmly] تعرف يا شرارة؟ الشجاعة مش إنك ماتخافش أبدًا... الشجاعة إنك تعمل الحاجة الصح... حتى وإنت خايف.'),
    (15, 'nour', '[softly] زي ما إنت عملت النهارده.'),
    (15, 'sharara', '[shy, sweet] يا نور... خُدي دي. كريستالة صغيرة... بتنوّر لوحدها. عشان لو خفتي في الضلمة... تفتكريني.'),
    (15, 'nour', '[touched] شكرًا يا شرارة! هحطها جنب سريري.'),
    (15, 'nour', '[warmly] وإنت يا شرارة... لو خفت تاني، افتكر السر.'),
    (15, 'sharara', '[proud] شُمّ الوردة... وطفّي الشمعة! ولو الدنيا ضلمت... أنوّرها أنا!'),
    (15, 'lumaa', '[happy] وأنا لما نوري يرجع كامل... هاجي ألعب معاك.'),
    (15, 'lumaa', '[yawning] هااااا... يلا يا نور... نرجع البيت.'),
    (15, 'sharara', '[waving] مع السلامة يا أصحابي! تعالوا تاني!'),
    (15, 'SFX', 'soft calm whoosh of wind'),

    # 16 — home, Nour turns off the light herself
    (16, 'nour', '[whispers] هحط الكريستالة هنا... جنب المخدة.'),
    (16, 'nour', '[softly, brave] وتعرف يا فانوس؟... أنا هطفّي اللمبة الصغيرة لوحدي.'),
    (16, 'SFX', 'a gentle click of a lamp switch turning off'),
    (16, 'nour', '[calm whisper] شُمّ الوردة... وطفّي الشمعة... أنا مش خايفة.'),
    (16, 'fanoos', '[softly, proud] برافو يا نور. الأوضة في الضلمة... هي هي نفس الأوضة.'),
    (16, 'nour', '[sleepy, smiling] والضلمة... بطانية كبيرة... الدنيا بتتغطّى بيها عشان تنام... زي ما قالت ماما.'),
    (16, 'lumaa', '[distant whisper] تصبحي على خير يا نور...'),
    (16, 'nour', '[sleepy whisper] وإنتي من أهله يا لُمعة.'),
    (16, 'fanoos', '[whispers] ودلوقتي جه دورك إنت يا حبيبي... شُمّ الوردة بالراحة... وطفّي الشمعة بالراحة... وغمّض عينيك.'),
    (16, 'fanoos', '[calmly] وفي الحلقة الجاية... هننزل تحت البحر... لقصر الحوريات! تصبحوا على خير... وأحلام سعيدة.'),
]
