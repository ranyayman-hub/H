"""Episode 4 (Nour in the Mermaid Palace) dialogue, one entry per line: (scene, speaker, text).
Text in [brackets] is an eleven_v3 audio direction, not spoken.
Spelling follows Egyptian pronunciation (أ for ق) so eleven_v3 does not drift to MSA.
SFX entries use speaker 'SFX' and an English description.
"""
VOICES = {
    'nour':     '09Q2MhEvwEP3ijEBee1i',  # Nour - Hawadeet World (designed)
    'fanoos':   'x6fvBLXv9YxzoVJQ0wp6',  # Momen - warm, mature, calm
    'lumaa':    'jDniWbMLsNWghA1TR3e3',  # Lumaa - Hawadeet World (designed)
    'mama':     'JHdGl5PsEzushIzzVSd1',  # Heba - soothing, Egyptian
    'morgana':  'Ant0ZQGVlIbuhAhJFdMk',  # Morgana - Hawadeet World (designed, pick 1)
    'baqbouqa': 'ur9inWR4qZl3iUnUpXe0',  # Baqbouqa - Hawadeet World (designed, pick 3)
}

L = [

    # 1
    (1, 'SFX', 'deep calm underwater ambience, a big wobbly bubble rising upward'),  # 000
    (1, 'baqbouqa', '[muffled inside a bubble, funny panic] بُلُب! بُلُب! حَدّ يطلّعني من هنا!'),  # 001
    (1, 'SFX', 'a loud funny bubble pop, then a tiny bubbly tumble'),  # 002
    (1, 'baqbouqa', '[dizzy, then giggling] أنا كويسة... أنا كويسة! هِهِهِهِ... بُلُب!'),  # 003

    # 3
    (3, 'fanoos', '[warmly] أهلًا يا أصحابي! اللّيلة رايحين مكان... عُمْرِنا ما رُحْناه! بَسّ الأوّل... نشوف نور.'),  # 004
    (3, 'SFX', 'playful bathtub splashing and soft bubbles'),  # 005
    (3, 'nour', '[giggling] ماما! بُصّي! عملت فُأّاعة أَدّ راسي!'),  # 006
    (3, 'mama', '[laughing] ههه! يلا يا سمكة صُغَيَّرة... كفاية مَيّة. وَأْت النوم.'),  # 007
    (3, 'nour', '[curious, in bed] ماما... هو فيه حوريّات بجد؟ تحت البحر؟'),  # 008
    (3, 'mama', '[smiles] مين عارف يا حبيبتي... يمكن في الأحلام. يلا غمّضي... تصبحي على خير.'),  # 009
    (3, 'nour', '[sleepy] وإنتي من أهله يا ماما.'),  # 010
    (3, 'SFX', 'a soft kiss, a door closing gently'),  # 011

    # 4
    (4, 'SFX', 'a gentle magical chime as a warm light glows up'),  # 012
    (4, 'fanoos', '[softly, playful] نور... صاحية؟ جَهّزي نفسك... اللّيلة هَنِتْبِلّ شُوَيّة!'),  # 013
    (4, 'SFX', 'tiny tapping on a window glass, tink tink'),  # 014
    (4, 'lumaa', '[excited] نور! البلّورة التالتة! وِئْعِت في البحر... جنب أَصْر الحوريّات!'),  # 015
    (4, 'nour', '[gasps, excited] أَصْر الحوريّات؟! ماما آلِت يمكن في الأحلام!'),  # 016
    (4, 'lumaa', '[giggles] وإحنا فين دِلْوَأْتي؟ في الأحلام! يلا بينا!'),  # 017

    # 5
    (5, 'SFX', 'soft whoosh of wind, magical flying sparkle, distant gentle sea waves'),  # 018
    (5, 'nour', '[amazed] البحر كلّه بيلمع تحت الأمر!'),  # 019
    (5, 'nour', '[worried] بس استنّى... أنا مش بعرف أتنفّس تحت المَيّة!'),  # 020
    (5, 'fanoos', '[playful] ولا يِهِمِّك! واحد... اتنين... تلاتة... فُأّاعة سحرية!'),  # 021
    (5, 'SFX', 'a magical bubbly shimmer and a soft pop'),  # 022
    (5, 'lumaa', '[giggles] ههههه! راسك جوّه فُأّاعة يا نور! شكلك رائد فضاء!'),  # 023
    (5, 'fanoos', '[to the children, playful] يلا يا أصحابي... امسكوا مناخيركم... واحد... اتنين... تلاتة!'),  # 024
    (5, 'SFX', 'a big happy splash into the sea, then deep calm underwater bubbles'),  # 025

    # 6
    (6, 'nour', '[amazed, whispering] وااااو... إحنا تحت البحر!'),  # 026
    (6, 'lumaa', '[happy] بُصّوا! المرجان بينَوَّر... أحمر وبَنَفْسِجي وأصفر!'),  # 027
    (6, 'fanoos', '[warmly, amused] والأناديل دي... شَبَهي! فوانيس صُغَيَّرة بتعوم!'),  # 028
    (6, 'nour', '[playful] وفيه سمك أحمر! يلا نعدّهم يا أصحابي!'),  # 029
    (6, 'nour', '[counting slowly] واحد... اتنين... تلاتة!'),  # 030
    (6, 'fanoos', '[to the children] كام سمكة حمرا شُفْتوا؟ أولوها بصوت عالي!'),  # 031
    (6, 'nour', '[happy] تلاتة! برافو عليكم!'),  # 032

    # 7
    (7, 'SFX', 'soft swaying seaweed, tiny nervous bubbles'),  # 033
    (7, 'lumaa', '[whispering] فيه حدّ مستخبّي ورا العُشْب دا!'),  # 034
    (7, 'nour', '[gently] ما تخافيش... إحنا أصحاب.'),  # 035
    (7, 'baqbouqa', '[shy, tiny voice] إ... إنتو مين؟ بُلُب!'),  # 036
    (7, 'SFX', 'a tiny cute bubble pop'),  # 037
    (7, 'baqbouqa', '[embarrassed, fast] بُلُب! بُلُب! بُلُب!'),  # 038
    (7, 'SFX', 'several tiny bubbles popping in a fast funny row'),  # 039
    (7, 'lumaa', '[laughing] ههههه! كل ما تتكلّم... تطلّع فُأّاعات!'),  # 040
    (7, 'baqbouqa', '[shy] آسفة... أنا بأبوءة. ولمّا بتكسف... بطلّع فُأّاعات. بُلُب!'),  # 041
    (7, 'nour', '[laughs softly] اسمك حلو أوي! أنا نور. وإحنا بندوّر على بلّورة فَيْروزي بتلمع.'),  # 042
    (7, 'baqbouqa', '[excited] البلّورة اللّامعة؟ شُفْتها! الأميرة مرجانة لِئْيِتْها... تعالوا ورايا على الأَصْر!'),  # 043

    # 8
    (8, 'SFX', 'soft magical underwater shimmer, gentle bubbles rising'),  # 044
    (8, 'nour', '[amazed] أَصْر من الصَّدَف واللّولي!'),  # 045
    (8, 'SFX', 'a big bubbly whoosh as palace doors open'),  # 046
    (8, 'morgana', '[excited] بأبوءة! مين دول؟... بنت من فوء؟! أوّل مرّة أشوف بنت من فوء!'),  # 047
    (8, 'nour', '[friendly] أهلًا! أنا نور. ودي لُمعة... ودا الفانوس.'),  # 048
    (8, 'morgana', '[cheerful] وأنا مرجانة! تعالوا... هَوَرّيكم أحلى أوضة في الأَصْر... أوضة كنوزي!'),  # 049

    # 9
    (9, 'SFX', 'a sparkling treasure shimmer'),  # 050
    (9, 'morgana', '[proud] بُصّوا! صَدَفة بتلمع... ومِشْط من اللّولي... وجرس صُغَيَّر بيرِنّ!'),  # 051
    (9, 'SFX', 'a tiny bell ring'),  # 052
    (9, 'lumaa', '[whispers, excited] نور! هناك... البلّورة الفَيْروزي!'),  # 053
    (9, 'nour', '[politely] مرجانة... ممكن من فضلك تِدّينا البلّورة دي؟ إحنا محتاجينها أوي.'),  # 054
    (9, 'morgana', '[hides it behind her back, firmly] لأ! دي بتاعتي! أنا اللي لِئيتها!'),  # 055
    (9, 'baqbouqa', '[nervous] بُلُب! بُلُب!'),  # 056
    (9, 'morgana', '[pouting] دي أحلى حاجة عندي... مش هَدّيها لحدّ!'),  # 057

    # 10
    (10, 'fanoos', '[softly] بالرّاحة يا نور... الزّعل مش هَيْحِلّها.'),  # 058
    (10, 'nour', '[gently, sitting next to her] أنا فاهماكي يا مرجانة. لو أنا لِئيت حاجة حلوة كده... كنت هحبّها أوي برضه.'),  # 059
    (10, 'morgana', '[surprised] بجد؟'),  # 060
    (10, 'nour', '[softly] بس البلّورة دي... من بلّورات الأحلام. ومن غيرها... أطفال كتير مش بيعرفوا يحلموا أحلام حلوة.'),  # 061
    (10, 'morgana', '[quietly] أطفال... مش بيحلموا؟'),  # 062
    (10, 'morgana', '[sad, unsure] بس... لو ادّيتها... هيبأى معايا أأَلّ.'),  # 063
    (10, 'fanoos', '[to the children] إيه رأيكم يا أصحابي؟ لمّا بنشارك حاجة حلوة... بتِأِلّ؟ ولا بتكبر؟'),  # 064

    # 11
    (11, 'nour', '[warmly] تعالي... أنا هشاركك حاجة من عندي الأوّل. سرّ بيهدّي الألب... اسمه: تمرين الفُأّاعة!'),  # 065
    (11, 'nour', '[slowly] خُدي نَفَس كبير من مناخيرك... بالرّاحة...'),  # 066
    (11, 'nour', '[slowly] وانفخي... بالرّاحة خالص... كإنّك بتعملي فُأّاعة كبيرة.'),  # 067
    (11, 'SFX', 'a soft big bubble slowly growing, then a gentle pop'),  # 068
    (11, 'fanoos', '[warmly] يلا يا أصحابي، جرّبوا معانا... خُدوا نَفَس... وانفخوا فُأّاعة كبيرة.'),  # 069
    (11, 'morgana', '[giggles, calmer] عملت فُأّاعة أَدّ الأَصْر! أنا حاسّة إنّي مبسوطة.'),  # 070
    (11, 'nour', '[softly] وكمان... هغنّيلِك الأغنية اللي ماما بتغنّيهالي.'),  # 071
    (11, 'nour', '[singing softly, slow lullaby] نامي نامي يا حلوة... والأمر جاي يِسْهَر... والنجوم بتلمع... والأحلام تِكْبَر.'),  # 072
    (11, 'morgana', '[touched] حلوة أوي! إنتي شاركتيني حاجتين... وأنا حاسّة إنّ ألبي كِبِر.'),  # 073

    # 12
    (12, 'morgana', '[deep breath, deciding] خُدي يا نور... البلّورة. عشان كل الأطفال يحلموا.'),  # 074
    (12, 'SFX', 'a big warm magical chime, then a turquoise sparkling wave of light spreading'),  # 075
    (12, 'nour', '[amazed] وااااو! الأَصْر كلّه نَوَّر!'),  # 076
    (12, 'lumaa', '[happy] بالفَيْروزي! والسمك بيرأص!'),  # 077
    (12, 'baqbouqa', '[happy] بُلُب! بُلُب! بُلُب!'),  # 078
    (12, 'SFX', 'many playful bubbles popping like a little bubbly song'),  # 079
    (12, 'lumaa', '[laughing] بأبوءة بتعمل فُأّاعات على شكل ألوب!'),  # 080
    (12, 'fanoos', '[to the children, playful] يلا يا أصحابي... ارأصوا مع السمك! لِفّوا... ولِفّة كمان!'),  # 081

    # 13
    (13, 'SFX', 'a soft magical click and a sparkling chime'),  # 082
    (13, 'nour', '[happy] تلات بلّورات! فاضل خمسة بس!'),  # 083
    (13, 'morgana', '[glowing, happy] تعرفي يا نور؟ أنا فرحانة أكتر من الأوّل!'),  # 084
    (13, 'morgana', '[discovering] الفرحة دي... لمّا أسمناها... كِبْرِت!'),  # 085
    (13, 'fanoos', '[to the children] والأطفال في كل حتّة... هيحلموا اللّيلة أحلى أحلام.'),  # 086

    # 14
    (14, 'morgana', '[sweet] نور... خُدي دي. صَدَفة صُغَيَّرة... لو حطّيتيها على وِدْنِك... هتسمعي البحر بيغنّي.'),  # 087
    (14, 'nour', '[touched] شكرًا يا مرجانة! هسمعها كل ليلة.'),  # 088
    (14, 'fanoos', '[wisely, warmly] الفرحة زي النّور يا أصحابي... لمّا بنِأْسِمْها... مش بتِأِلّ... بتكبر.'),  # 089
    (14, 'baqbouqa', '[shy, happy] وأنا... مش هتكسف تاني... بُلُب! [giggles] أوه... ساعات بس!'),  # 090
    (14, 'lumaa', '[yawning] هاااا... يلا يا نور... نرجع البيت.'),  # 091
    (14, 'morgana', '[waving] مع السلامة يا أصحابي! تعالوا تاني!'),  # 092
    (14, 'SFX', 'a soft rising whoosh of water and bubbles'),  # 093

    # 15
    (15, 'SFX', 'very soft calm sea waves'),  # 094
    (15, 'nour', '[whispering] هحطّ الصَّدَفة على وِدْني...'),  # 095
    (15, 'SFX', 'soft gentle sea waves heard inside a seashell'),  # 096
    (15, 'nour', '[dreamy whisper] البحر بيغنّي... زي ما آلِت مرجانة.'),  # 097
    (15, 'nour', '[sleepy, smiling] ماما كان عندها حأّ... الحوريّات موجودين... في الأحلام.'),  # 098
    (15, 'fanoos', '[whispers] ودِلْوَأْتي جه دورك إنت يا حبيبي... خُد نَفَس بالرّاحة... وانفخ فُأّاعة كبيرة بالرّاحة... وغمّض عينيك.'),  # 099
    (15, 'lumaa', '[distant whisper] تصبحي على خير يا نور...'),  # 100
    (15, 'nour', '[sleepy whisper] وإنتي من أهله يا لُمعة.'),  # 101
    (15, 'fanoos', '[calmly] وفي الحَلْأة الجاية... هنطلع فوء السّحاب... لِمدينة أوس أُزَح! تصبحوا على خير... وأحلام سعيدة.'),  # 102
]
