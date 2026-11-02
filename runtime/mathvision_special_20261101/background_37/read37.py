from tools37 import *
for q in sys.argv[1:]:
    print('\nQUESTION',q)
    ctx=read(TASK/q/'context.json')
    scene=read(TASK/q/'source_scene_snapshot.json')
    for o in ctx['objects']:
        if o.get('styleable'):
            g=o.get('geometry',{});points=g.get('points',[])
            points=[scene.get('points',{}).get(p,p) if isinstance(p,str) else p for p in points]
            print(json.dumps({'id':o['id'],'world':points,'visibility':g.get('visibility'),'paths':o.get('partial_paths',[])},ensure_ascii=False))
    print('PROJECTION',scene['projection'])
    print('SOURCE', [str(ROOT/'SolidGeometry'/p) for p in AD.records[q]['runtime_dependencies'] if p.endswith('source_redraw.py')])
