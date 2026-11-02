from tools18 import *
qids=sys.argv[1:]
for q in qids:
    if q not in ASSIGNED:continue
    c=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'));r=json.loads((HERE/q/'formal_record.json').read_text(encoding='utf-8'));br='PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry'
    scene=json.loads((ROOT/br/r['scene']).read_text(encoding='utf-8-sig'))
    print('\nQUESTION',q,'scene',scene.keys())
    print('labels',json.dumps(scene.get('labels'),ensure_ascii=False))
    print('notes',json.dumps(scene.get('ambiguities'),ensure_ascii=False))
    pts=scene.get('points',{})
    for o in c['objects']:
        if not o.get('styleable',True):continue
        g=o.get('geometry',{});pp=g.get('points',[])
        xy=[pts.get(p) if isinstance(p,str) else p for p in pp] if isinstance(pts,dict) else []
        if len(xy)>10:xy={'count':len(xy),'first':xy[:2],'last':xy[-2:]}
        print(json.dumps({'id':o['id'],'type':o.get('type'),'geometry':g if len(str(g))<600 else {'type':g.get('type'),'npoints':len(pp)},'xy':xy,'keys':list(o) if not g else None},ensure_ascii=False))
