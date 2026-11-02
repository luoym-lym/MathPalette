from tools27 import *
import numpy as np
for q in ['Plane159','Plane203','Plane292','Plane371']:
    ob={o['id']:o for o in json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'))['objects']}
    print('\n'+q)
    ids=([f'source{i}' for i in range(9)]+[f'E{i}' for i in range(9)] if q=='Plane159' else
         ['o'+str(i) for i in range(19)] if q=='Plane203' else
         ['o'+str(i) for i in range(17,27)] if q=='Plane292' else ['o1','o4','o5','o8','o11','o13','o69','o58','o60','o66','o65'])
    for oid in ids:
        if oid not in ob:continue
        o=ob[oid];pts=o['points'];print(oid,len(pts),pts if len(pts)<45 else pts[:5],o.get('semantic_fill'),o.get('fill_color'))
    if q=='Plane371':
        def ce(a):return a-(a.max(0)+a.min(0))/2
        def haus(a,b):
            d=np.linalg.norm(a[:,None,:]-b[None,:,:],axis=2);return float(max(d.min(0).max(),d.min(1).max()))
        for src,tgt in [('o1','o69'),('o4','o66'),('o5','o65'),('o13','o58')]:
            a=ce(np.array(ob[src]['points']));b=ce(np.array(ob[tgt]['points']))
            print(src,tgt,{str((sx,sy)):haus(a*[sx,sy],b) for sx,sy in [(1,1),(-1,1),(1,-1),(-1,-1)]})
