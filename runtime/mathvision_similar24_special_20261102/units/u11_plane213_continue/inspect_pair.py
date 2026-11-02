from bootstrap import *
d=OWN/'Plane213'/sys.argv[1]
for f in sorted(d.rglob('run_*_response.json')):
    print(str(f));print(f.read_text(encoding='utf-8-sig'))
for f in d.rglob('summary.json'):
    s=read(f)
    print(json.dumps({'summary':str(f),'two_completed':s['two_completed'],'results_metadata':[{k:v for k,v in r.items() if k not in ('answer','thinking')} for r in s['results']]},ensure_ascii=False,indent=2))
for name in ('pair.stderr.txt','pair_reaped.json'):
    f=d/name
    if f.exists():print(name);print(f.read_text(encoding='utf-8-sig'))
