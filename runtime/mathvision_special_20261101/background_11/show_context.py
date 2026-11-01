from tools_local import *
for qid in sys.argv[1:]:
    data=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'))
    print('\nQUESTION',qid)
    for o in data['objects']:
        g=o['geometry'];pts=g.get('points',[])
        print(json.dumps({'id':o['id'],'kind':o['kind'],'styleable':o['styleable'],'geometry':g if len(pts)<30 else {'point_count':len(pts),'first':pts[:3]}},ensure_ascii=False))
