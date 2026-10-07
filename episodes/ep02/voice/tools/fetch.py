"""Download ElevenLabs generations by id, reading signed URLs from this session's transcript.
usage: python3 fetch.py OUTDIR name=generation_id [name=generation_id ...]"""
import sys, re, glob, os, subprocess
out=sys.argv[1]; os.makedirs(out, exist_ok=True)
pairs=[a.split('=',1) for a in sys.argv[2:]]
txt=''
for f in glob.glob('/root/.claude/projects/-home-user-H/*.jsonl')+glob.glob('/root/.claude/projects/-home-user-H/*/tool-results/*.txt'):
    txt+=open(f,encoding='utf-8',errors='ignore').read()
for name,gid in pairs:
    urls=re.findall(r'https://storage\.googleapis\.com/xi-backend/[^"\\\s]*?/'+re.escape(gid)+r'/content\.(?:mp3|mp4|png|jpg|webp)\?[^"\\\s]+', txt)
    if not urls: print(name,'NO URL'); continue
    url=urls[-1]; ext=url.split('/content.')[1].split('?')[0]
    p=os.path.join(out,f'{name}.{ext}')
    r=subprocess.run(['curl','-sS','-f','-o',p,url]); print(name, 'ok' if r.returncode==0 else 'FAIL')
