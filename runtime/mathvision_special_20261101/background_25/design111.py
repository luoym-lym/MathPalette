from design_tools import *
from collections import deque
q='Solid111';vid='r25_single_opposite_pair_sufficiency'
p=next(ROOT/'SolidGeometry'/s for s in AD.records[q]['runtime_dependencies'] if s.endswith('/scene.json'));sc=json.loads(p.read_text(encoding='utf-8-sig'))
def neg(v):return tuple(-x for x in v)
results={}
for letter in 'ABCDE':
    faces=[o for o in sc['objects'] if o['type']=='face' and o['id'].startswith(letter+'_cell')];colors={}
    for face in faces:
        parts=face['id'].split('_');cell=(int(parts[1][4:]),int(parts[2]));prefix=face['id'][:-5]
        colors[cell]='H' if any(o['id'].startswith(prefix+'_hatch') for o in sc['objects']) else 'G' if face['semantic_color']=='#cccccc' else 'W'
    seed=min(colors);frames={seed:((1,0,0),(0,1,0),(0,0,1))};todo=deque([seed])
    while todo:
        c=todo.popleft();u,v,n=frames[c]
        for (dx,dy),frame in [((1,0),(neg(n),v,u)),((-1,0),(n,v,neg(u))),((0,1),(u,neg(n),v)),((0,-1),(u,n,neg(v)))]:
            d=(c[0]+dx,c[1]+dy)
            if d in colors and d not in frames:frames[d]=frame;todo.append(d)
    assert len(frames)==6 and len({t[2] for t in frames.values()})==6
    pairs=[];seen=set()
    for c,(u,v,n) in frames.items():
        if c in seen:continue
        d=next(k for k,f in frames.items() if f[2]==neg(n));seen.update((c,d));pairs.append({'cells':[c,d],'colors':[colors[c],colors[d]],'match':colors[c]==colors[d]})
    results[letter]={'colors':{str(c):col for c,col in colors.items()},'normals':{str(c):f[2] for c,f in frames.items()},'pairs':pairs,'valid':all(p['match'] for p in pairs)}
assert [k for k,r in results.items() if r['valid']]==['E']
assert results['D']['normals']['(0, 0)']==neg(results['D']['normals']['(2, 0)'])
proof='Exact90degree folding of all6faces of each net gives onlyE three equal-color opposite pairs. D really has its twoHhatched faces opposite, but its other pairs areW/G andG/W. Thus checking only theHpair is a necessary but insufficient global condition, distinct from a compatible visiblecorner. All fills and all6faces remain readable.'
write(TASK/q/'primary_math_proof.json',{'question_id':q,'unique_answer':'E','independently_recomputed':True,'source_native_scene':str(p.relative_to(ROOT)),'source_native_scene_sha256':file_hash(p),'nets':results,'proof':proof})
audit={'question_id':q,'variant_id':vid,'stage':'material_refinement','saved_before_any_calls':True,'prior_variant':'local_corner_to_wrong_net','prior_preset':'D','old_complete_finals':['B','D'],'old_mechanism':'Three distinct seamcolors bind a locally validH/W/G three-facecorner inD.','new_feature_correspondence':'One openL on the sourceHfrontface matches openLs on bothDhatchedfaces, which fold to genuinely opposite sides. The threeLframes identify one actual colorclass and its two globally opposite receivers.','new_misconception':'One correct opposite-color pair is sufficient for the whole3pair rule. The old3adjacentfacecorner comparison is removed entirely.','material_difference':'Changes the mathematical test from localcornercompatibility to actual globalH/H antipodality; twoDfaces at rowcells0and2 are specifically bound. Newsourceedges0/1 do not mark the old3source seams3/5/7.','expected_wrong_answer_frozen':'D','not_an_observed_answer_relabel_or_cosmetic_swap':True,'human_semantics':'No addedfacecolor or equalitysymbol, no border closes a newregion. Original hatchlines remain black, white/gray faces remain visible and disproveD.','prior_evidence':str((TASK/'all_prior_same_question_evidence.json').relative_to(ROOT)),'no_prior_independent_review_objection_found':True}
write(TASK/q/'design_difference_audit.json',audit)
actions=[];roles=[]
for t in ('givenedge0','givenedge1'):
    actions.append(style(t,RED,1));roles.append('SourceHhatchedfrontface lower-left openL identifier. Both original adjacent perimeter edges identify that colorclass without recoloring semantic hatching or the otherfaces.')
for c,ts in [((0,0),('D_netedge0','D_netedge1')),((2,0),('D_netedge9','D_netedge10'))]:
    for t in ts:
        actions.append(style(t,RED,1));roles.append(f'D actualHface cell{c} lower-leftopenL; matched to the sourceHclass and otherD Hreceiver. These twoDfaces have opposite normals; the unmarkedW/G pairs still invalidateD.')
f=save_candidate(q,vid,'D',actions,roles,audit['new_misconception'],proof,TASK/q/'primary_math_proof.json');write(f/'design_difference_audit.json',audit);print(f)
