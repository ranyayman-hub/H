"""Build flow/FLOW-ALL.md for EP03 from art/SHOTS-EP03.md + voice/lines.py: every Flow clip with its lines and Veo prompt."""
import os, re, sys, subprocess
EP=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, f'{EP}/voice'); import lines
L=lines.L
WHO={'nour':('the little girl Nour','a cute, sweet cartoon girl voice'),
 'mama':('her mother (kind young Egyptian mother, beige headscarf)','a warm, gentle young mother voice'),
 'fanoos':('the golden lantern (its kind face glows inside the colored glass)','a warm, kind, wise male voice'),
 'lumaa':('Lumaa, the little glowing star','a tiny, high, cheerful little-girl voice'),
 'sharara':('Sharara, our own original tiny round lavender baby dragon with golden dots','a soft, shy, sweet little-boy cartoon voice')}
IPA={'/ˈɡuwwa/':'جوّه','/ˈenta nawˈwart/':'إنت نوّرت','/beˈtenzel/':'بتنزل','/leˈbesti/':'لبستي'}
TAIL='Do NOT change anything in the image: keep exactly the same characters, faces, hair, clothes, colors, places and objects, and the same 3D animation style. No new characters, people, heads, hands or objects may appear, not even at the edges of the frame. Static camera, only a very slow gentle push-in. Smooth, gentle bedtime-story motion. Absolutely no captions, no subtitles, no letters or words anywhere on screen. No background music.'
LANTERN='The lantern is the same golden Egyptian Ramadan lantern (fanoos) from the image, with red, blue and green stained-glass panes and a kind face; it is NOT an oil lamp or hurricane lamp. Its face always stays clearly visible; its glow never hides the face. There is only ONE lantern in the whole video: no second lantern appears anywhere. The lantern has NO arms and NO hands; only its face moves. '
DRAGON='Sharara is a cute, gentle, original baby dragon; he is never scary and has no sharp teeth. '
EXTRA={'05-1':[19],'05-2':[22]}   # SFX cues placed on these shots
def clean(t):
    for k,v in IPA.items(): t=t.replace(k,v)
    return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
def tags(t): return ', '.join(x for x in re.findall(r'\[([^\]]*)\]',t) if x not in ('slowly',))
def dur(i):
    if L[i][1]=='SFX': return 1.0
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{EP}/voice/takes/{i:03d}.mp3']))
def nums(spec):
    out=[]
    for part in spec.split(','):
        a,_,b=part.strip().partition('-')
        out+=list(range(int(a),int(b or a)+1))
    return out
shots=[]
for m in re.finditer(r'^Shot (\S+?)( \(TALKING, (\w+)\))?: (.*?) \[([\d,\- ]+)\]\s*$',open(f'{EP}/art/SHOTS-EP03.md').read(),re.M):
    sid,_,talker,desc,spec=m.groups()
    shots.append((sid,talker,desc,sorted(set(nums(spec)+EXTRA.get(sid,[])))))
used={}
for sid,t,d,ls in shots:
    for i in ls: used.setdefault(i,sid)
missing=[i for i in range(len(L)) if i not in used]
clips=[]
for sid,talker,desc,ls in shots:
    ls=[i for i in ls if used[i]==sid]   # a line plays on the first shot that lists it
    if not ls: continue
    group=[];t=0
    for i in ls:
        d=dur(i)
        if group and t+d+0.45>6.8:
            clips.append((sid,talker,desc,group)); group=[];t=0
        group.append(i); t+=d+(0.45 if len(group)>1 else 0)
    clips.append((sid,talker,desc,group))
out=['# EP03: كل لقطات Google Flow بالترتيب\n',
'**الإعدادات لكل لقطة:** الصورة في «بدء» و«إنهاء» فاضية، والموديل **Veo 3.1 Fast**، والمدة **8 ثواني**، والعدد **x1**.\n',
'**بعد ما الفيديو يخلص:** نزّله وسمّيه برقم اللقطة (مثلاً `C02.mp4`) وابعتهولي، وأنا أركّب أصواتنا عليه.\n',
'- 🗣️ **كلام**: Veo بيحرّك البق مع الكلام.\n- 🎙️ **صوت من برّه**: محدّش بيحرّك بقّه، وأنا هحط الصوت فوق الفيديو.\n',
'**اللوجو (مشهد 2):** جاهز.\n']
for n,(sid,talker,desc,ls) in enumerate(clips,1):
    cid=f'C{n:02d}'
    speakers=[L[i][1] for i in ls if L[i][1]!='SFX']
    mode='talk' if talker and speakers else 'vo'
    secs=sum(dur(i) for i in ls)+0.45*(len(ls)-1)
    icon={'talk':'🗣️ كلام','vo':'🎙️ صوت من برّه'}[mode]
    out.append(f'\n---\n\n## {cid}: صورة {sid} ({icon}، {secs:.1f} ث)\n')
    for i in ls:
        sp,tx=L[i][1],L[i][2]
        out.append(f"- `{i:03d}` **{sp}**: {clean(tx) if sp!='SFX' else '(مؤثر: '+tx+')'}\n")
    nn='(no necklace)' in desc
    desc=desc.replace('(no necklace) ','')
    scene=re.sub(r'^(close-up|medium close-up|wide shot|wide magical shot|closer|final teaser)[,:]\s*','',desc,flags=re.I)
    if sid.startswith('04-'):
        motion=f'The scene: {scene} Gentle living motion: soft blinking, small natural head and body movements. This is a normal cozy bedroom before the magic starts: no magic, no sparkles, no glitter, no glowing particles anywhere; the lantern on the shelf stays dark, unlit and completely still the whole time; the bedside lamp stays on the whole time and never turns off.'
    elif sid.startswith('16-') and sid!='16-6':
        motion=f'The scene: {scene} Gentle living motion: soft blinking, small natural head and body movements. Calm and quiet: no sparkles, no glitter, no glowing particles in the room; only the tiny red crystal glows softly.'
    else:
        motion=f'The scene: {scene} Gentle living motion: soft blinking, small natural head and body movements, sparkles and glows shimmer softly.'
    p=f'A cozy, safe, magical 3D cartoon bedtime story for young children; everyone is safe, calm and happy. Use the attached image as the exact first frame of the video (same camera angle, same framing). Animate this exact image. {motion}\n'
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
    if nn: p+='Nour wears NO necklace here (bare pajama collar). '
    if 'mama' in speakers: p+='Mama is calm, loving and relaxed the whole time with a soft caring smile; she is never scared and never grabs any blanket. '
    if 'lantern' in desc.lower() or 'fanoos' in speakers: p+=LANTERN
    if 'sharara' in desc.lower() or 'dragon' in desc.lower() or 'sharara' in speakers: p+=DRAGON
    p+=TAIL
    out.append(f'```\n{p}\n```\n')
os.makedirs(f'{EP}/flow',exist_ok=True)
open(f'{EP}/flow/FLOW-ALL.md','w').write(''.join(out))
print(len(shots),'shots,',len(clips),'clips; talk',sum(1 for c in clips if c[1] and any(L[i][1]!='SFX' for i in c[3])),'; lines missing:',missing)
