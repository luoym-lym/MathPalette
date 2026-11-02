from unit_tools import *
import itertools, math
def area(v):return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(v,v[1:]+v[:1])))/2
def native_scene(q):
    b='PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry'
    r=read(HERE/q/'formal_record.json')
    return read(PROJECT/b/next(p for p in r['runtime_dependencies'] if p.endswith('/items/'+q+'/scene.json')))
v=read(HERE/'Plane479/exact_paths.json')['shaded'][0]['controls']
v=[c[0] for c in v]
write(HERE/'Plane479/primary_math.json',{'polygon_area':area(v),'each_square_area':4,'total_square_area':12,'ratio':'1/3','correct_answer':'C','derivation':'Take E=(0,0),H=(2,0),I=(4,0),D=(1,0),C=(3,0),A=(1,2),B=(3,2),J=(4,-2). Shoelace of A,J,I,C,B is 4. Three squares each have area 4. Marks considered on individual square edges would only emphasize given equal areas; no targeted clean wrong correspondence was identified.'})
for q,target,answer in [('Plane480','boundary',13),('Plane481','logo',10)]:
    pts=[c[0] for c in read(HERE/q/'exact_paths.json')[target][0]['controls']]
    assert math.isclose(area(pts),answer)
    detail={'vertices_full_precision':pts,'shoelace_area':area(pts),'correct_answer':str(answer),'grid_original_and_unit_unchanged':True}
    if q=='Plane481':
        P=[[1,4],[2,5],[5,2],[4,1]];Q=[[1,2],[2,1],[5,4],[4,5]];intersection=[[2,3],[3,4],[4,3],[3,2]]
        detail.update(strip_P=P,strip_Q=Q,area_P=area(P),area_Q=area(Q),intersection=intersection,intersection_area=area(intersection),union_area=area(P)+area(Q)-area(intersection),derivation='The filled polygon is the union of the two area-6 strips; their overlap is the area-2 central diamond. 6+6-2=10. Boundary colors add no new cut or new filled area.')
    else:detail['derivation']='Nine full unit cells plus eight half-cells give 13; direct exact boundary shoelace confirms. Coloring only the caps or grid would suggest grouping but no distinct clean feature correspondence to a specific wrong total was identified.'
    write(HERE/q/'primary_math.json',detail)
windows=[[(r,c,2),(r,c+1,3),(r+1,c,1),(r+1,c+1,0)] for r in range(2) for c in range(2)]
win_counts=[0]*4;hist=[0]*5
for state in itertools.product(range(4),repeat=9):
    hits=[all(state[r*3+c]==t for r,c,t in w) for w in windows]
    for i,h in enumerate(hits):win_counts[i]+=h
    hist[sum(hits)]+=1
assert win_counts==[1024]*4 and hist[1]==4096 and sum(hist[2:])==0
write(HERE/'Plane482/primary_math.json',{'tile_orientation_indices':{'0':'NW gray','1':'NE gray','2':'SE gray','3':'SW gray'},'windows':windows,'equiprobable_tilings':4**9,'window_hit_counts':win_counts,'simultaneous_diamond_count_histogram':hist,'favorable_any_diamond':hist[1],'probability':'1/64','correct_answer':'C','proof':'Each window needs exactly four prescribed tile orientations. Different windows share a tile that would need distinct gray orientations, so events are disjoint. The full exhaustive 4^9 enumeration independently confirms 4096 favorable tilings. Colored sides coincide with the already present example diamond; source fills and all four tile orientations remain intact.'})
write(HERE/'Plane484/primary_math.json',{'status':'source_semantic_hold_no_solver_call','formal_answer':'90','finding':'Current formal wording does not require A_i to lie on the rays, nor require alternation. Even placing every A_i on the same ray permits A_i=i*u, consecutive distance 1 and strictly increasing distance from A0 for all n. The picture suggests alternation but does not explicitly impose it. No variant is advanced because a rigorous unique finite answer cannot be established from the current wording without adding a condition.','counterexample':'A0=(0,0), u=(cos(0.5deg),sin(0.5deg)); A_i=i*u for arbitrarily large i. All stated distance inequalities hold.','formal_inputs_untouched':True})
s=native_scene('Plane490');v0=s['objects'][0]['points'];v1=s['objects'][1]['points']
assert {tuple(p) for p in v0}=={tuple(-x for x in p) for p in v1}
centroid0=[sum(p[k] for p in v0)/len(v0) for k in range(2)];centroid1=[sum(p[k] for p in v1)/len(v1) for k in range(2)]
write(HERE/'Plane490/primary_math.json',{'light_vertices':v0,'dark_vertices':v1,'vertex_set_negation_equal':True,'vertex_mean_light':centroid0,'vertex_mean_dark':centroid1,'correct_answer':'180','proof':'All seven corresponding vertices are negations about C=(0,0). Their nonzero vertex-mean vectors are opposites, forcing a unique rotation angle of 180 modulo 360.','prescreen':'A proposed false same-side shaft match would discard the decisive arrowhead and merely cue translation; a quarter-turn match would compare unrelated long and short edges. No sufficiently grounded useful targeted misconception found; no forced solver call.'})
total=[];inside=[]
for x in itertools.product(range(8),repeat=4):
    if sum(x)==7:
        total.append(x)
        if min(x)>0:inside.append(x)
assert len(total)==120 and len(inside)==20
write(HERE/'Solid194/primary_math.json',{'tetrahedral_lattice':'Nonnegative integer (a,b,c,d) with a+b+c+d=7','outside':'At least one coordinate zero; includes base face','white':'All four coordinates at least one','white_reindexing':'Subtract (1,1,1,1); nonnegative coordinates sum to 3, a 4-pyramid','all_balls':len(total),'white_balls':len(inside),'white_layer_count':4,'correct_answer':'4','prescreen':'The source 3-pyramid has no interior balls. Styles on its separate layer circles cannot bind an actually shown interior feature to the 8-pyramid without inventing a shell, adding misleading stack geometry, or merely highlighting a layer count. No clean targeted design justified.'})
import numpy as np
rotations=[]
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([-1,1],repeat=3):
        m=np.zeros((3,3),dtype=int)
        for i in range(3):m[i,perm[i]]=signs[i]
        if round(np.linalg.det(m))==1:rotations.append(m)
s=native_scene('Solid201')
views=s['semantic_models'][0]['view_face_normal_word_baseline']
def rotate(view,m):return [(tuple(int(v) for v in m@np.array(n)),word,m@np.array(u),m@np.array(v)) for n,word,u,v in view]
base=rotate(views[0],np.eye(3,dtype=int));solutions=[]
for m1,m2 in itertools.product(rotations,repeat=2):
    assignment={};okay=True
    for n,word,u,v in base+rotate(views[1],m1)+rotate(views[2],m2):
        if n in assignment:
            old=assignment[n]
            if old[0]!=word or not np.allclose(old[1],u,rtol=0,atol=1e-10) or not np.allclose(old[2],v,rtol=0,atol=1e-10):okay=False;break
        else:assignment[n]=(word,u,v)
    if okay:solutions.append({'view2_to_view1':m1.tolist(),'view3_to_view1':m2.tolist(),'faces':[{'normal':list(n),'word':word,'u':u.tolist(),'v':v.tolist()} for n,(word,u,v) in assignment.items()],'YES_count':sum(v[0]=='YES' for v in assignment.values())})
assert len(rotations)==24 and len(solutions)==1 and solutions[0]['YES_count']==3
write(HERE/'Solid201/primary_math.json',{'proper_rotations':24,'tested_rotation_pairs':576,'consistent_assignments':len(solutions),'solutions':solutions,'correct_answer':'B','probability':'1/2','source_of_constraints':'Actual native semantic face normals plus printed baseline/up vectors, all current source words manually viewed. Fresh primary enumeration; historical result not used as proof.','preservation':'Five exact existing projected edges are overlaid only. Original face text vectors, 3D, projection and frozen visibility are untouched.'})
report=read(BASE/'exploration_report.json');inventory=read(BASE/'inventory.json')
assigned={p.stem:read(p)['question_ids'] for p in BASE.glob('background_*_assignment.json')}
overlap={key:sorted(set(IDS)&set(values)) for key,values in assigned.items() if key!='background_22_assignment' and set(IDS)&set(values)}
assert not overlap
write(HERE/'allocation_and_history_audit.json',{'checked_at':now(),'assigned_exactly':IDS,'assignment_count':8,'overlap_with_any_other_unit':overlap,'prior_global_attempts_for_these_ids':[a for a in report['attempts'] if a.get('question_id') in IDS],'remaining_question_statuses':[r for r in rows(BASE/'remaining_questions.jsonl') if r['question_id'] in IDS],'inventory_membership':{q:any((x==q if isinstance(x,str) else x.get('question_id')==q) for x in inventory['PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry'].get('eligible',[])) for q in IDS},'delivered_overlap':sorted(set(IDS)&set(report['new_runtime_work']['delivered_questions'])),'historical_mutable_runtime_hashes_not_treated_as_frozen_inputs':True})
print('Primary proofs saved for all eight. Solid201 fresh 576-pair proof: exactly one assignment, 3 YES.')
