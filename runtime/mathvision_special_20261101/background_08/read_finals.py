from tools08 import *
for q in sys.argv[1:]:
    for d in sorted((HERE/q).glob('*/tests/quicktest3_*')):
        print(q,d.parent.parent.name)
        for n in (1,2):
            p=d/f'run_{n:02d}.json'
            if not p.exists():print('RUN',n,'PENDING');continue
            r=json.loads(p.read_text(encoding='utf-8'));print('RUN',n,'STATUS',r['status'],'FINISH',r.get('finish_reason'),'TRUNCATED',r.get('truncated'));print(r.get('answer',r.get('error')))
