"""Build flow/FLOW-ALL.md (every clip of EP02 with Veo prompt + dialogue) and a zip of the start images in clip order."""
import os, re, sys, subprocess, zipfile
EP=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, f'{EP}/voice'); import lines
L=lines.L
WHO={'nour':('the little girl Nour','a cute, sweet 6-year-old girl voice'),
 'mama':('her mother (kind young Egyptian mother, beige headscarf)','a warm, gentle young mother voice'),
 'fanoos':('the golden lantern (its kind face glows inside the colored glass)','a warm, kind, wise male voice'),
 'lumaa':('Lumaa, the little glowing star','a tiny, high, cheerful little-girl voice'),
 'baskota':('Baskota, the gingerbread boy with the white chef hat','a playful, cheerful little-boy voice')}
TAIL='Do NOT change anything in the image: keep exactly the same characters, faces, hair, clothes, colors, room, furniture and objects in the same places, and the same 3D animation style. No new characters or objects. Static camera, only a very slow gentle push-in. Smooth, gentle bedtime-story motion. No subtitles, no text on screen, no background music.'
# (clip, image, lines, motion, mode)  mode: talk = lip-sync in Flow, vo = voice-over (mouths closed), ready = already done
C=[
('C01','02-1',[4,5,6],'','ready'),
('C02','02-1',[7],'Nour pouts, tilts her head and swings her shoulders. After she speaks she looks up hopefully; her mother smiles tenderly and slowly closes the chocolate box. The cat yawns.','talk'),
('C03','02-3',[8],'','ready'),
('C04','02-1',[9,10],'Nour lowers her hands with a little sigh. Then her mother puts the chocolate box down and gently strokes Nour\'s hair.','talk'),
('C05','02-4',[11,12],'Nour, lying under her blanket with closed eyes, smiles sleepily. While Nour speaks, her mother keeps her lips pressed on Nour\'s forehead in a long silent kiss and does not talk at all. After Nour finishes, the mother slowly lifts her head, smiles silently and switches off the bedside lamp; the room softly dims to blue moonlight; the cat stays asleep. The mother never speaks in this video.','talk'),
('C06','03-0',[13],'Nour sleeps peacefully; the lantern beside the bed slowly lights up with a warm colorful glow and sparkles; outside the window Lumaa twinkles and bobs.','vo'),
('C07','03-1',[14],'Nour sits up in bed, eyes widening with wonder, and leans toward the glowing lantern. The lantern floats and turns gently with swirling sparkles.','talk'),
('C08','03-2',[15],'','ready'),
('C09','03-3',[16,17],'Lumaa taps the window glass twice with her little arm, glowing brighter and bouncing with excitement.','talk'),
('C10','03-4',[18,19],'Nour leans out of the open window delighted; Lumaa glows and bounces beside her shoulder; Nour\'s silver necklace starts to shine.','talk'),
('C11','03-1',[20,21],'The lantern floats down next to Nour and offers its silver ring; Nour grabs the ring with both hands, excited.','talk'),
('C12','04-1',[22],'Nour flies forward joyfully holding the lantern\'s ring, braids fluttering in the wind; Lumaa swoops beside her leaving sparkles; the city lights twinkle below; slow camera follow.','vo'),
('C13','04-2',[23],'Lumaa flies close to camera, closes her eyes and sniffs the sweet air happily; pink and golden sparkles drift by.','talk'),
('C14','04-1',[24],'Nour laughs while flying and holds her tummy with one hand, the other holding the lantern\'s ring.','talk'),
('C15','05-1',[25],'Slow camera push-in toward Candy City; Nour, Lumaa and the lantern glide gently down from the sky toward the street; lollipop lamps twinkle; cotton-candy trees sway.','vo'),
('C16','05-2',[26],'Nour looks around amazed, turning her head from the biscuit houses to the glowing sugar windows, pointing.','talk'),
('C17','05-3',[27],'Lumaa twirls happily above the chocolate river, pointing down at it; the river flows slowly; the lantern bobs nearby.','talk'),
('C18','05-3',[28],'The lantern floats closer to camera and turns toward the cotton-candy trees and the lollipop street lamps; the trees sway softly.','talk'),
('C19','05-4',[29],'The strawberry-juice fountain splashes gently; the lantern turns toward it with a glow.','talk'),
('C20','05-4',[30],'Nour laughs and holds her tummy next to the fountain; Lumaa bounces happily.','talk'),
('C21','05-2',[31],'Nour clasps her hands near her chest, looking around with sparkling eyes.','talk'),
('C22','06-1',[32],'Baskota pops out from behind the biscuit house with arms wide open, bouncing cheerfully.','talk'),
('C23','06-2',[33],'Nour steps back a little, startled and amused, looking down at the small gingerbread boy just out of frame.','talk'),
('C24','06-1',[34],'Baskota puts a hand on his chest proudly, then points up curiously at the little star.','talk'),
('C25','05-4',[35],'Lumaa floats forward and waves; she points to the lantern and then to Nour.','talk'),
('C26','05-4',[36],'The lantern floats forward, glowing softly, turning to look down at someone small just out of frame.','talk'),
('C27','06-3',[37],'Baskota jumps and points far away at the Cake Mountain; Nour, Lumaa and the lantern turn to look; the giant cherry on top glows softly with pink light.','talk'),
('C28','07-1',[38],'The fluffy cotton-candy cloud drifts slowly; Baskota waves everyone to come aboard, happily.','talk'),
('C29','07-1',[39],'Nour pats the cotton-candy cloud curiously, surprised.','talk'),
('C30','07-1',[40,41],'Baskota laughs and wags his finger playfully at Nour. Then the cloud floats higher through the night sky; Lumaa and the lantern fly alongside.','talk'),
('C31','07-2',[42],'Colorful candy butterflies (one red, two green, three yellow) flutter gently around the cotton-candy cloud, wings shimmering, leaving tiny sparkles.','vo'),
('C32','07-1',[43],'Nour points at butterflies one by one as she counts, laughing; candy butterflies flutter around the cloud.','talk'),
('C33','07-3',[44],'The lantern floats beside the cloud, looking straight at the camera as if talking to the children watching.','talk'),
('C34','07-1',[45],'Nour claps happily toward the camera, giggling.','talk'),
('C35','08-1',[46],'Baskota spreads his arms toward the candy stand, inviting; sparkles float.','talk'),
('C36','08-2',[47],'Nour licks the big swirly lollipop and chews happily with puffed cheeks.','talk'),
('C37','08-1',[48],'Nour grabs more candies from the stand and tastes them happily; Baskota laughs and claps.','talk'),
('C38','08-3',[49],'Lumaa looks worried, her glow slightly dimmer, little arms raised.','talk'),
('C39','08-2',[50],'Nour, cheeks full of candy, reaches for more, holding the lollipop and cotton candy.','talk'),
('C40','08-2',[51],'Nour stops chewing, cheeks still full, and looks up a little guiltily.','vo'),
('C41','09-1',[52,53],'Baskota bounces on the wobbly rainbow jelly bridge, which jiggles with each step, waving everyone to follow.','talk'),
('C42','09-1',[54],'Lumaa bounces across the jelly bridge, twirling happily; the bridge jiggles.','talk'),
('C43','09-2',[55,56],'Nour holds her tummy with both hands, bends a little in pain, eyes watery.','talk'),
('C44','10-1',[57],'Baskota, sitting on the big cookie stone, tells a story with one hand raised; Nour sits beside him listening quietly with her mouth closed.','talk'),
('C45','10-2',[58],'The chubby sugar king snores on his big cushion, his tummy rising and falling; candy wrappers flutter softly; dreamy storybook haze.','vo'),
('C46','10-1',[59],'Nour gives a small weak laugh; Baskota smiles and listens.','talk'),
('C47','10-3',[60],'The lantern glows softly and speaks kindly and wisely, looking at Nour beside it.','talk'),
('C48','10-1',[61],'Nour looks down thoughtfully and speaks quietly; Baskota listens.','talk'),
('C49','11-1',[62,63],'Baskota points happily at the mint spring. Then Nour kneels and drinks clear sparkling water from her cupped hands; bubbles rise; mint leaves sway.','talk'),
('C50','11-1',[64],'Nour lifts her head from the water, relieved, and breathes out with a smile.','talk'),
('C51','11-2',[65,66],'Nour stands straight with a calm, determined small smile; mint leaves sway around her.','talk'),
('C52','12-1',[67],'Baskota on the far side of the jelly bridge cheers and claps, calling Nour to jump.','talk'),
('C53','12-1',[68],'Nour bounces high and light across the jelly bridge, arms out like wings, laughing; the bridge jiggles.','talk'),
('C54','13-1',[69,70],'Slow camera tilt up the tall white sugar riddle gate with candy-cane pillars; the team stands small in front of it looking up; soft glow.','vo'),
('C55','13-1',[71,72],'The team stands in front of the closed riddle gate; Baskota holds his head worried; Lumaa turns to the lantern.','vo'),
('C56','13-2',[73],'The lantern floats in front of the riddle gate, reading playfully, looking at the camera.','talk'),
('C57','13-3',[74],'Nour thinks with one finger on her chin, eyes looking up.','talk'),
('C58','13-2',[75],'The lantern looks straight at the camera, inviting the children watching to guess.','talk'),
('C59','13-3',[76],'Nour\'s face lights up with a happy idea and she jumps a little.','talk'),
('C60','13-4',[77,78],'The riddle gate swings open with a burst of sparkles; Baskota jumps happily and cheers; Lumaa twirls.','vo'),
('C61','13-4',[79,80],'Nour cheers with both arms up, proud and laughing; Lumaa giggles and twirls around her.','vo'),
('C62','14-1',[81,82],'At the top of the cake mountain, the small pink crystal shard on the giant cherry pulses with soft pink light; the team leans in, amazed.','vo'),
('C63','14-1',[83],'The pink crystal shard glows brighter; the lantern floats closer to it, glowing warmly.','vo'),
('C64','14-2',[84],'Nour holds the glowing pink crystal shard gently, gasps happily; pink light on her face.','talk'),
('C65','14-3',[85,86],'Close-up: the pink crystal shard settles into one star slot of Nour\'s silver necklace and lights up with a gentle pink glow and sparkles.','vo'),
('C66','15-1',[87],'Baskota holds up the shiny wrapped bonbon as a gift with a proud smile.','talk'),
('C67','15-2',[88,89],'Nour holds the wrapped bonbon gently with a thoughtful, warm smile.','talk'),
('C68','15-2',[90],'Nour hugs the bonbon to her chest and smiles proudly.','vo'),
('C69','16-1',[91,92,93],'Nour, holding the lantern\'s ring, and Lumaa fly up and away from Candy City; Baskota waves goodbye from below; slow camera pull-back.','vo'),
('C70','17-1',[94],'Nour, sleepy, places the wrapped bonbon gently on the pillow beside her and smiles; the cat stays asleep; the necklace glows softly pink.','talk'),
('C71','17-1',[95,96],'Nour lies down slowly, smiling sleepily, and looks toward the window.','vo'),
('C72','17-2',[97],'Nour sleeps peacefully with a gentle smile; the lantern on the shelf dims slowly; one star outside the window twinkles brighter than the others.','vo'),
]
def clean(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
def tags(t): return ', '.join(re.findall(r'\[([^\]]*)\]',t))
def dur(i):
    if L[i][1]=='SFX': return 1.0
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{EP}/voice/takes/{i:03d}.mp3']))
out=['# EP02: كل لقطات Google Flow بالترتيب\n',
'**الإعدادات لكل لقطة:** الصورة في «بدء» و«إنهاء» فاضية، والموديل **Veo 3.1 Fast**، والمدة **8 ثواني**، والعدد **x1**.\n',
'**بعد ما الفيديو يخلص:** نزّله وسمّيه برقم اللقطة (مثلاً `C02.mp4`) وابعتهولي، وأنا أركّب أصواتنا عليه.\n',
'- 🗣️ **كلام**: Veo بيحرّك البق مع الكلام.\n- 🎙️ **صوت من برّه**: محدّش بيحرّك بقّه، وأنا هحط الصوت فوق الفيديو.\n- ✅ **جاهزة**: مش محتاجة Flow.\n',
'**مشهد 1 (المقدمة) ومشهد 18 (الختام):** جاهزين من لقطات حلقة 1.\n']
zf=zipfile.ZipFile(f'{EP}/flow/EP02-flow-images.zip','w')
for cid,img,ls,motion,mode in C:
    secs=sum(dur(i) for i in ls)+0.45*(len(ls)-1)
    who=' + '.join(f"{i:03d} {L[i][1]}" for i in ls)
    icon={'talk':'🗣️ كلام','vo':'🎙️ صوت من برّه','ready':'✅ جاهزة'}[mode]
    out.append(f'\n---\n\n## {cid}: صورة {img} ({icon}، {secs:.1f} ث)\n')
    for i in ls:
        sp,tx=L[i][1],L[i][2]
        out.append(f"- `{i:03d}` **{sp}**: {clean(tx) if sp!='SFX' else '(مؤثر: '+tx+')'}\n")
    if mode=='ready': continue
    p=f'Use the attached image as the exact first frame of the video (same camera angle, same framing). Animate this exact image. {motion}\n'
    if mode=='talk':
        first=True
        for i in ls:
            sp,tx=L[i][1],L[i][2]
            if sp=='SFX': continue
            name,voice=WHO[sp]; t=tags(tx)
            p+=f'{"Right at the start, " if first else "Then "}{name} says{" ("+t+")" if t else ""} in Egyptian Arabic with {voice}:\n"{clean(tx)}"\n'
            first=False
        p+='Only the character who is speaking moves the mouth; everyone else stays completely silent with lips pressed together. Clear lip-sync. All talking ends before the 7th second.\n'
    else:
        p+='Nobody talks; all mouths stay closed.\n'
    if 'lantern' in motion.lower() or any(L[i][1]=='fanoos' for i in ls): p+='The lantern\'s kind face always stays clearly visible on its glass; its glow never hides the face. '
    p+=TAIL
    out.append(f'```\n{p}\n```\n')
    ip=next(f'{EP}/images/{img}.{e}' for e in ('png','jpg') if os.path.exists(f'{EP}/images/{img}.{e}'))
    zf.write(ip, f'{cid}-{img}{os.path.splitext(ip)[1]}')
zf.close()
open(f'{EP}/flow/FLOW-ALL.md','w').write(''.join(out))
print(len(C),'clips;',sum(1 for c in C if c[4]!='ready'),'to make')
