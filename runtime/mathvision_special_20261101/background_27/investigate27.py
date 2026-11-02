from tools27 import *
import numpy as np
for qid in ['Plane362','Plane371','Plane444']:
    m=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'))
    print('\nQUESTION '+qid)
    for o in m['objects']:
        pts=o.get('geometry',{}).get('points',[])
        if qid=='Plane362' or qid=='Plane444':
            print(o['id'],o.get('kind'),pts)
        elif pts:
            a=np.array(pts);print(o['id'],o.get('kind'),len(pts),'bbox',a.min(axis=0).tolist(),a.max(axis=0).tolist())
q='Plane292';s=json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'));ob={o['id']:o for o in s['objects']}
v=np.array(ob['o17']['points']);f=v.copy();res=[]
for n,oid in enumerate([None,'o2','o5','o8','o11','o14']):
    if oid:
        a,b=np.array(ob[oid]['points']);u=(b-a)/np.linalg.norm(b-a);mat=2*np.outer(u,u)-np.eye(2);f=(f-a)@mat.T+a
    errors={}
    for c,tgt in zip('ABCDE',['o27','o31','o35','o39','o43']):
        t=np.array(ob[tgt]['points']);errors[c]=float(np.max(np.linalg.norm(t-t.mean(0)-f+f.mean(0),axis=1)))
    res.append({'after_reflections':n,'errors':errors})
print('Plane292 successive reflection residuals',json.dumps(res))
for p in sorted(BASE.glob('batch_*/manifest.json')):
    d=json.loads(p.read_text(encoding='utf-8-sig'))
    print('DELIVERED_REFERENCE',p.parent.name,str(d)[:2800])
