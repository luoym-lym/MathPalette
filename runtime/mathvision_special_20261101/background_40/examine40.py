from tools40 import *
def brief(x):
    if isinstance(x,dict):return {k:brief(v) for k,v in x.items()}
    if isinstance(x,list):
        if len(x)>12:return {'array_length':len(x),'first':brief(x[0]),'last':brief(x[-1]),'sha256':canonical_hash(x)}
        return [brief(v) for v in x]
    return x
for q in sys.argv[1:]:
    print(q,flush=True)
    rec=AD.records[q];folder=AD.branch/next(p for p in rec['runtime_dependencies'] if p.endswith('/scene.json')).rsplit('/',1)[0]
    scene=read(folder/'scene.json')
    print(json.dumps({k:brief(v) for k,v in scene.items() if k!='objects'},ensure_ascii=False))
    for o in scene.get('objects',[]):print(json.dumps(brief(o),ensure_ascii=False))
    for n in ['renderer_semantic.py','source_redraw.py']:
        p=folder/n
        if p.exists():print(n,p.read_text(encoding='utf-8'))
