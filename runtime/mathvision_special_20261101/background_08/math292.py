from tools08 import *
import numpy as np
q='Plane292';s=json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'));obj={o['id']:o for o in s['objects']}
v=np.array(obj['o17']['points']);f=v.copy();steps=[]
for oid in ['o2','o5','o8','o11','o14']:
    a,b=np.array(obj[oid]['points']);u=(b-a)/np.linalg.norm(b-a);matrix=2*np.outer(u,u)-np.eye(2);f=(f-a)@matrix.T+a
    steps.append({'mirror_object':oid,'endpoints':[a.tolist(),b.tolist()],'matrix':matrix.tolist()})
res={}
for c,oid in zip('ABCDE',['o27','o31','o35','o39','o43']):
    t=np.array(obj[oid]['points']);res[c]=float(np.max(np.linalg.norm((t-t.mean(axis=0))-(f-f.mean(axis=0)),axis=1)))
report={'reflection_steps':steps,'answer_residual_after_translation':res,'unique_match':min(res,key=res.get),'tolerance':1e-10,'description':'Compare all 369 ordered frozen contour vertices after five exact reflections, allowing only source/option panel translation. Vertex order carries silhouette anatomy; source controls already depict first two reflections.'}
write(HERE/q/'five_reflection_math_audit.json',report);print(json.dumps(report))
assert res['E']<1e-10 and all(res[c]>.01 for c in 'ABCD')
if len(sys.argv)>1 and sys.argv[1]=='render':
    m=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'));targets={t['id']:t for t in m['canvas']['targets']}
    n=len(v);index=int(v[:,0].argmin());lo=(index-12)/n;hi=(index+12)/n;assert 0<lo<hi<1
    actions=[]
    for oid in ['o17','o31']:
        p=targets[oid]['partial_paths'][0];actions.append({'type':'set_object_style','target':oid,'color':'#DC2626','linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':lo,'end':hi,'wrap':False}})
    actions += [{'type':'set_object_style','target':oid,'color':'#2563EB','linewidth_pt':2} for oid in ['o19','o33']]
    render(q,'tail_ear_mirror_binding',actions,'B','Bind initial kangaroo tail and ear strokes to their same anatomical features in B, inviting a simple one-axis mirror shortcut instead of five alternating reflections.',
    'Reflect every ordered source silhouette vertex successively in the five frozen dashed lines o2,o5,o8,o11,o14. After translating each option to the same centroid, E is the sole contour equal to the result (max residual <1e-10); A-D all differ. The existing two intermediate kangaroos and all five reflection lines remain unchanged. Color-only original tail intervals and ear strokes do not add puzzle objects, fill or mirror axes. See five_reflection_math_audit.json for numeric comparison and exact matrices.',
    [{'actions':[0,1],'role':'Same indexed short tail-bend interval in original kangaroo and B; anatomically meaningful feature correspondence tempts a single mirror.'},{'actions':[2,3],'role':'Original ear stroke and B ear stroke provide independent head orientation and prevent the design being whole-answer coloring. Both tail and ear are already part of each kangaroo; no points or characters are added.'}])
