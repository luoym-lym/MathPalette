from tools08 import *
for q in sys.argv[1:]:
    s=json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'));m=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'))
    print(q)
    for o in s['objects']:
        pts=o.get('points',[]);pts=[s['points'][p] if isinstance(p,str) else p for p in pts]
        bbox=[min(p[0] for p in pts),min(p[1] for p in pts),max(p[0] for p in pts),max(p[1] for p in pts)] if pts else None
        print(o['id'],o['type'],len(pts),bbox,pts if len(pts)<7 else '')
