from design_tools import *
from collections import deque
import re
q='Solid228';vid='r25_same_face_overlap_transfer'
p=next(ROOT/'SolidGeometry'/s for s in AD.records[q]['runtime_dependencies'] if s.endswith('/scene.json'));sc=json.loads(p.read_text(encoding='utf-8-sig'))
def neg(v):return tuple(-t for t in v)
def ekey(a,b):return tuple(sorted([tuple(a),tuple(b)]))
results={};cells_by_letter={}
for letter in 'ABCDE':
    edges=set()
    for o in sc['objects']:
        if not o.get('points') or not isinstance(o['points'][0],str) or not o['points'][0].startswith(letter+'v'):continue
        ends=[tuple(map(int,re.fullmatch(letter+r'v(\d+)_(\d+)',s).groups())) for s in o['points']];edges.add(ekey(*ends))
    cells={(x,y) for x in range(5) for y in range(4) if all(ekey(a,b) in edges for a,b in [((x,y),(x+1,y)),((x+1,y),(x+1,y+1)),((x+1,y+1),(x,y+1)),((x,y+1),(x,y))])}
    assert len(cells)==6,(letter,cells);cells_by_letter[letter]=cells
    seed=min(cells);frames={seed:((1,0,0),(0,1,0),(0,0,1))};todo=deque([seed]);consistency=[]
    while todo:
        c=todo.popleft();u,v,n=frames[c]
        for (dx,dy),f in [((1,0),(neg(n),v,u)),((-1,0),(n,v,neg(u))),((0,1),(u,neg(n),v)),((0,-1),(u,n,neg(v)))]:
            d=(c[0]+dx,c[1]+dy)
            if d not in cells:continue
            if d not in frames:frames[d]=f;todo.append(d)
            elif frames[d]!=f:consistency.append([c,d])
    groups={}
    for c,f in frames.items():groups.setdefault(str(f[2]),[]).append(c)
    results[letter]={'cells':sorted(cells),'frames':{str(c):f for c,f in frames.items()},'normal_groups':groups,'six_unique_faces':len(groups)==6,'inconsistent_hinges':consistency,'valid':len(groups)==6 and len(frames)==6 and not consistency}
assert [k for k,v in results.items() if not v['valid']]==['D']
assert results['D']['frames']['(1, 2)'][2]==results['D']['frames']['(3, 0)'][2]
assert results['B']['frames']['(0, 2)'][2]==neg(results['B']['frames']['(0, 0)'][2])
proof='Recover all6unitcells of eachpattern directly from its four frozenedge bindings; propagate orthonormal faceframes across every hinge. A,B,C,E give6unique face normals and consistent hinges;D repeats one face (cell1,2 and3,0) and is invalid. InB the upper and lower wingcells0,2and0,0 fold to opposite normals, so they do not overlap. D alone cannotfold.'
write(TASK/q/'primary_math_proof.json',{'question_id':q,'unique_answer':'D','independently_recomputed':True,'source_native_scene':str(p.relative_to(ROOT)),'source_native_scene_sha256':file_hash(p),'nets':results,'proof':proof})
audit={'question_id':q,'variant_id':vid,'stage':'material_refinement','saved_before_any_calls':True,'prior_variants':['false_net_edge_pair','stair_end_pair'],'old_presets':['A','A'],'old_complete_finals':[['A','D'],['E','B']],'old_mechanisms':'Both markedonlyA staircase endboundaries to imply a falseclosure or repeatedface. No source/receiver crosspattern relation.','new_feature_correspondence':'Transfer two actual collidingDfaces (upperterminal1,2; rightterminal3,0) to the two noncollidingBwingfaces (upper0,2; lower0,0), via redandblue openL frames. Eachcolor links correspondingterminal face role across two fullnets.','new_geometric_misconception':'Treat opposite-side wingsB as same-side overlapping faces by importing D actualrepeated-face relation and failing to preserve hinge path handedness.','substantive_change':'Eight existingedgestyles on fourfaces inB/D replace allA marks. Concrete erroneous globalface-normal relation is independently proved beforetesting. Although B appeared as an oldfailed final, that output supplies no newpreset justification; the newcrosspattern hinge-normal comparison does.','expected_wrong_answer_frozen':'B','human_semantics':'Onlyopen facecornerLs; no new foldline, arrow, duplicateface, equalitysymbol or boundaryclosure. Allsix cells and allhingepaths remain visible for correction.','prior_evidence':str((TASK/'all_prior_same_question_evidence.json').relative_to(ROOT)),'no_prior_independent_review_objection_found':True}
write(TASK/q/'design_difference_audit.json',audit)
actions=[];roles=[]
for letter,cell,color,role in [('D',(1,2),RED,'Truecolliding Dupperface, geometricreference'),('D',(3,0),BLUE,'Truecolliding Dterminaltailface, geometricreference'),('B',(0,2),RED,'Bupperwingreceiver, falselygrouped ascolliding'),('B',(0,0),BLUE,'Blowerwingreceiver, actuallyopposite notcolliding')]:
    x,y=cell
    for ends in [((x,y),(x+1,y)),((x,y),(x,y+1))]:
        names=[f'{letter}v{a}_{b}' for a,b in ends]
        target=next(o['id'] for o in sc['objects'] if o.get('points') in [names,names[::-1]])
        actions.append(style(target,color,1.5));roles.append(role+': one of2 existing adjacent faceedges forming an openL. The two arms identifya2D squareface atfullnative scale; allotherfoldlines retainoriginalblackstyles. Red/blue distinguish thetwo roles acrossbothpatterns.')
f=save_candidate(q,vid,'B',actions,roles,audit['new_geometric_misconception'],proof,TASK/q/'primary_math_proof.json');write(f/'design_difference_audit.json',audit);print(f)
