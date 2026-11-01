from tools_b import *
import math
for qid in (sys.argv[1:] or ASSIGNED):
    meta=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'))
    print('\n'+qid)
    for o in meta['objects']:
        g=o['geometry'];kind=g.get('type')
        if qid=='Plane226' and (o['id'].startswith('board_') or o['id'].startswith('given_')):continue
        if qid=='Plane219' and kind=='segment':continue
        if kind=='closed_arc_path':
            cmds=g['commands'];c=next(c['center'] for c in cmds if c['op']=='arc');pts=[v['point'] for v in cmds if v['op']=='line']
            print(o['id'],kind,g.get('semantic_color'),c,pts)
        else:
            fields={k:v for k,v in g.items() if k not in ['id','commands','semantic_fill']}
            if len(fields.get('points',[]))>12:
                pts=fields.pop('points');fields['npoints']=len(pts);fields['mean']=[sum(p[d] for p in pts)/len(pts) for d in [0,1]];fields['bbox']=[[min(p[d] for p in pts),max(p[d] for p in pts)] for d in [0,1]]
            print(o['id'],json.dumps(fields,separators=(',',':')))
