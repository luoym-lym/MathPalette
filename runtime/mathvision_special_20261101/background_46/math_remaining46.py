from tools46 import *
from collections import Counter,defaultdict
import numpy as np,math
assert not (OWN/'external_failure_stop.json').exists()
q='Solid104';sc=read(OWN/q/'native_scene_46.json');poly=sc['polyhedra'][0];faces=poly['faces'];verts=poly['vertices'];edges=defaultdict(list);vfaces=defaultdict(list)
for i,f in enumerate(faces):
    for v in f:vfaces[v].append(i)
    for a,b in zip(f,f[1:]+f[:1]):edges[tuple(sorted([a,b],key=int))].append(i)
assert all(len(x)==2 for x in edges.values())
counts=Counter(map(len,faces));assert counts=={3:20,4:30,5:12}
vertex_types=Counter(tuple(sorted(len(faces[i]) for i in fs)) for fs in vfaces.values());assert vertex_types=={(3,4,4,5):60}
neighbours={i:[next(k for k in edges[tuple(sorted([a,b],key=int))] if k!=i) for a,b in zip(f,f[1:]+f[:1])] for i,f in enumerate(faces)}
square_records=[{'face_index':i,'vertices':f,'adjacent_face_sizes':[len(faces[j]) for j in neighbours[i]],'neighbour_indices':neighbours[i]} for i,f in enumerate(faces) if len(f)==4]
assert all(sorted(x['adjacent_face_sizes'])==[3,3,5,5] for x in square_records)
ctx=read(OWN/q/'context_46.json');om={o['id']:o for o in ctx['objects']}
P=np.array(sc['projection']['matrix']);centers={i:np.array([verts[v] for v in f]).mean(axis=0)@P.T for i,f in enumerate(faces)}
# The central square lies closest to the body projection origin.
central=min([i for i,f in enumerate(faces) if len(f)==4 and poly['face_visibility'][str(i)]],key=lambda i:float(np.linalg.norm(centers[i])))
marked=[]
for a,b in zip(faces[central],faces[central][1:]+faces[central][:1]):
    pair=[verts[a],verts[b]];targets=[o for o in ctx['objects'] if o.get('styleable') and o['geometry'].get('type')=='segment' and (np.allclose(o['geometry']['points'],pair,atol=1e-12,rtol=0) or np.allclose(o['geometry']['points'],pair[::-1],atol=1e-12,rtol=0))]
    assert len(targets)==1
    other=next(i for i in edges[tuple(sorted([a,b],key=int))] if i!=central)
    marked.append({'target':targets[0]['id'],'points':pair,'receiver_square_face':central,'adjacent_face_index':other,'adjacent_face_sides':len(faces[other]),'color':'#DC2626' if len(faces[other])==5 else '#2563EB'})
audit={'question_id':q,'independent_exact_face_census':dict(counts),'vertices':len(verts),'edges':len(edges),'vertex_configurations':{str(k):v for k,v in vertex_types.items()},'Euler_check':len(verts)-len(edges)+len(faces),'all_square_adjacencies':square_records,'central_square_face_index':central,'central_square_projected_center':centers[central].tolist(),'chosen_true_shared_edges':marked,'correct_derivation':'12*5=60 pentagon-square incidences, each square counted2 times -> S30. Each square has2 triangle incidences ->3T=60 ->T20. Sum12*5+20-30=50.','wrong_predeclared_derivation':'Substitute the60 pentagon-square side-contact records for60 distinct square faces; retain two triangle contacts per inferred square ->T=120/3=40; sum60+40-60=40. This double-counts each square.','unique_human_answer':'50; actual depicted graph, source pentagon/square/triangle shapes, original fills and legend provide the reciprocal two-sided check.','primary_status':'candidate mathematically and topologically justified; native rendered review pending'}
save(OWN/q/'substantive_math_audit_46.json',audit);print(q,'central',central,json.dumps(marked),flush=True)
q='Solid141';sc=read(OWN/q/'native_scene_46.json');stairs=sc['staircase'];rows=stairs['steps'];hidden=[x['row'] for x in rows if not x['visible']];visible=[x['row'] for x in rows if x['visible']]
assert hidden==list(range(2,8))+list(range(14,20));assert len(visible)==9
# Check every visible source fill facet belongs to its row's true angular30-degree tread and0.1high band.
facet_counts=Counter();maxerr=0
for o in sc['objects']:
    if o.get('semantic_material')!='step':continue
    r=int(o['id'].split('_')[0][4:]);facet_counts[r]+=1;p=np.array(o['points']);z=set(np.round(p[:,2],12));assert z=={round(r*.1,12),round((r+1)*.1,12)}
    angles=(np.degrees(np.arctan2(p[:,1],p[:,0]))+360)%360;lo,hi=rows[r]['angle_deg'];angles=np.where((angles<lo-1e-7)&(hi==360),angles+360,angles)
    assert np.min(angles)>=lo-1e-7 and np.max(angles)<=hi+1e-7
assert facet_counts=={r:30 for r in visible}
audit={'question_id':q,'full_native_row_angle_table':rows,'actual_visible_rows':visible,'actual_hidden_rows':hidden,'visible_tread_facets_verified':dict(facet_counts),'uniform_rise':0.1,'hidden_groups':[{'rows':list(range(2,8)),'angle_domain':[0,180],'count':6},{'rows':list(range(14,20)),'angle_domain':[0,180],'count':6}],'correct_unique_answer':'12','specific_new_mechanisms_evaluated':[{'proposal':'Bind visible row1 to visible row8 and row13 to row20 as equal7-rise intervals; mistake each row-index difference for hidden count, predicting14.','exact_math':'8-1=20-13=7, but the actual hidden indices are endpoints-excluded:8-1-1=20-13-1=6.','concise_mark_objection':'These endpoints occur at opposite cylinder generators, not on one actual vertical path. Drawing a connector creates a non-stair diagonal; coloring a full side vertical interval highlights intervening visible front-surface grid cells, not the hidden helical treads. Without a new legend, the cue fails to specify an interval-versus-endpoint transfer clearly.'},{'proposal':'Pair top and bottom visible fragments sharing angle180..210 or300..330 to infer totalturn/endpoint count.','exact_math':'Repeated same-angle source intervals are12rows apart and correctly imply one360degree turn. They support12steps per turn but do not select a unique false hidden count.','concise_mark_objection':'A generic pair of matching arc fragments is valid but gives no specific new erroneous information transfer; selecting a wrong preset would be arbitrary.'}],'disposition':'skip_after_substantive_exact_geometry_assessment_no_clean_concise_information_targeted_new_candidate','no_calls':True,'no_claim_all_legal_variants_impossible':True}
save(OWN/q/'substantive_math_audit_46.json',audit);print(q,'hidden12; endpoint7versus6 mechanism assessed; skip rather than freeze unsupported preset',flush=True)
q='Solid189';sc=read(OWN/q/'native_scene_46.json');model=sc['tower_model'];light=[tuple(x) for x in model['light_blocks']];dark=[tuple(x) for x in model['dark_blocks']];columns=defaultdict(list)
for b in light+dark:columns[b[:2]].append(b[2])
assert len(columns)==25
cols=[]
for (x,y),zs in sorted(columns.items()):
    h=4-abs(x)-abs(y);assert sorted(zs)==list(range(h));c='light' if (x,y,0) in light else 'dark';assert all(((x,y,z) in light)==(c=='light') for z in zs)
    cols.append({'xy':[x,y],'height':h,'color':c})
assert len(light)==20 and len(dark)==24
save(OWN/q/'substantive_math_audit_46.json',{'question_id':q,'all25_exact_column_records':cols,'light_height_census':dict(Counter(c['height'] for c in cols if c['color']=='light')),'correct_unique_answer':'20 = center4 +8outerlight*2','original_JPG_and_native_PNG_viewed':True,'new_local_direction':'Transfer center side-view peak height4 to the distinct outerlight plan column(2,0), whose actual height is2, predicting22. Both source and receiver differ from old centerplan<-outer2highside direction; old target18/finals9,32 not reused.'})
ctx=read(OWN/q/'context_46.json');M=np.array(sc['projection']['matrix']);origin=np.array(sc['projection']['origin']);offset=np.array(sc['projection']['offset'])
for o in ctx['objects']:
    if o['id'].startswith('planedge'):
        xy=(np.array(o['geometry']['points'])-origin)@M.T+offset
        print(o['id'],np.round(xy,5).tolist())
print('189 exact light20/dark24; plan projected edges above',flush=True)
