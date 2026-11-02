from tools_local import *
for q in ['Solid112','Solid117','Solid114']:
    s=AD.scenes[q]
    by={}
    for o in s['objects']:
        pre=o['id'].split('e')[0]
        if pre not in by:by[pre]=o
    print(q,json.dumps(by,ensure_ascii=False))
    print('native visibility keys',list(s['visibility']))
    print('native extra keys',list(json.loads((AD.branch/next(p for p in AD.records[q]['runtime_dependencies'] if p.endswith('/scene.json'))).read_text(encoding='utf-8-sig'))))
