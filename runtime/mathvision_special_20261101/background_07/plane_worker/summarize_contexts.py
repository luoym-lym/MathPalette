from tools_local import *
import math
for q in ASSIGNED:
    m=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'))
    summary=[]
    for o in m['objects']:
        g=o['geometry'];pts=g.get('points',[])
        e={'id':o['id'],'kind':o['kind'],'fill':g.get('fill_color'),'geometry':g if len(pts)<16 else {'point_count':len(pts),'bbox':[min(p[0] for p in pts),min(p[1] for p in pts),max(p[0] for p in pts),max(p[1] for p in pts)]}}
        if q=='Plane245' and o['id'] not in ['o0','o1','o52','o104','o105','o106','o111','o112','o113','o114','o115','o116','o117','o118','o119','o120','o121','o122','o123','o124','o125','o126','o127','o128']:continue
        summary.append(e)
    write(HERE/q/'eligibility_with_approval.json',eligibility(q))
    write(HERE/q/'compact_geometry.json',summary)
    print(q,json.dumps(summary,ensure_ascii=False))
