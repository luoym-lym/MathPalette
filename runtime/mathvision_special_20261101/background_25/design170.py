from design_tools import *
from collections import deque
q='Solid170';vid='r25_bent_opening_to_planar_window'
p=next(ROOT/'SolidGeometry'/s for s in AD.records[q]['runtime_dependencies'] if s.endswith('/scene.json'))
src=json.loads(p.read_text(encoding='utf-8-sig'))
def neg(v):return tuple(-t for t in v)
def add(*vs):return tuple(sum(ts) for ts in zip(*vs))
def mul(v,s):return tuple(t*s for t in v)
def key(v):return tuple(round(float(t),9) for t in v)
cells={(0,0),(1,0),(2,0),(3,0),(1,1),(1,-1)}
basis={(1,0):((1,0,0),(0,1,0),(0,0,1))};todo=deque([(1,0)])
while todo:
    c=todo.popleft();u,v,n=basis[c]
    for delta,frame in [((1,0),(neg(n),v,u)),((-1,0),(n,v,neg(u))),((0,1),(u,neg(n),v)),((0,-1),(u,n,neg(v)))]:
        d=add(c,delta)
        if d in cells and d not in basis:basis[d]=frame;todo.append(d)
assert len({b[2] for b in basis.values()})==6
results={}
for i,letter in enumerate('ABCDE'):
    off=7*i
    fills=[o for o in src['objects'] if o['type']=='face' and o['id'].startswith(letter+'material')]
    rects=[(min(p[0] for p in o['points'])-off,max(p[0] for p in o['points'])-off,min(p[2] for p in o['points']),max(p[2] for p in o['points'])) for o in fills]
    features=[]
    for cell in sorted(cells):
        x,y=cell;xs=sorted({x,x+1,*[round(t,10) for r in rects for t in r[:2] if x<t<x+1]});ys=sorted({y,y+1,*[round(t,10) for r in rects for t in r[2:] if y<t<y+1]})
        void={(ix,iy) for ix in range(len(xs)-1) for iy in range(len(ys)-1) if not any(a-1e-9<(xs[ix]+xs[ix+1])/2<b+1e-9 and c-1e-9<(ys[iy]+ys[iy+1])/2<d+1e-9 for a,b,c,d in rects)}
        while void:
            stack=[void.pop()];comp=[]
            while stack:
                t=stack.pop();comp.append(t)
                for delta in ((1,0),(-1,0),(0,1),(0,-1)):
                    d=add(t,delta)
                    if d in void:void.remove(d);stack.append(d)
            bounds=[min(xs[a] for a,b in comp),max(xs[a+1] for a,b in comp),min(ys[b] for a,b in comp),max(ys[b+1] for a,b in comp)]
            lo,hi,bot,top=bounds;touch=[]
            if abs(lo-x)<1e-8:touch.append(('left',(0,0),(0,1)))
            if abs(hi-x-1)<1e-8:touch.append(('right',(1,0),(1,1)))
            if abs(bot-y)<1e-8:touch.append(('bottom',(0,0),(1,0)))
            if abs(top-y-1)<1e-8:touch.append(('top',(0,1),(1,1)))
            u,v,n=basis[cell]
            def project(pt):return key(add(mul(n,.5),mul(u,pt[0]-.5),mul(v,pt[1]-.5)))
            edge=sorted(project(t) for t in touch[0][1:]) if len(touch)==1 else None
            features.append({'cell':cell,'void_bounds':bounds,'touches':[t[0] for t in touch],'folded_edge':edge})
    groups={}
    for f in features:groups.setdefault(str(f['folded_edge']),[]).append(f)
    paired=[g for k,g in groups.items() if k!='None' and len(g)==2]
    opposite=False
    if len(features)==4 and len(paired)==2:
        a,b=[g[0]['folded_edge'] for g in paired]
        opposite=key(mul(add(*a),.5))==key(neg(mul(add(*b),.5)))
    results[letter]={'features':features,'paired_edge_holes':len(paired),'interior_face_holes':sum(f['folded_edge'] is None for f in features),'two_opposite_edge_holes':opposite}
assert [k for k,v in results.items() if v['two_opposite_edge_holes']]==['C']
proof='The target shell holes straddle the centrally opposite parallel edges x=15,z=9 and x=18,z=6. Exact90degree folding of all six face frames and every source material rectangle gives A,D two adjacent edgeholes, B one paired edgehole plus two unpaired capnotches, C two opposite edgeholes, E two interior facewindows. Only C matches; target has four affected faces and E onlytwo. Sizes are schematic, no dimension or tunnel assumed.'
write(TASK/q/'primary_math_proof.json',{'question_id':q,'unique_answer':'C','independently_recomputed':True,'source_native_scene':str(p.relative_to(ROOT)),'source_native_scene_sha256':file_hash(p),'folded_face_frames':{str(k):v for k,v in basis.items()},'nets':results,'proof':proof})
audit={'question_id':q,'variant_id':vid,'stage':'material_refinement','saved_before_any_calls':True,'prior_variant':'opposite_to_adjacent_hole_pairs','old_preset':'A','old_complete_finals':['D','A'],'old_mechanism':'Correct local straddling holes mapped to an adjacent rather than opposite pair.','new_feature_correspondence':'Whole bent two-face source-opening contours map to full coplanar four-edge windows of E; red and blue each identify one source opening and one E window.','new_geometric_misconception':'Flatten a two-face bent opening into a face-interior rectangle, substituting apparent2D window shape for fold incidence. This loses the crease-straddling property, rather than the old adjacent/opposite placement property.','expected_wrong_answer_frozen':'E','new_target_independent_of_old_observed_answers':True,'substantive_change':'E differs topologically: only2affectedfaces versus target4. No earlier same-question design tested faceinterior binding. Whole window contour is used specifically as a2D shape receiver, not option salience.','human_semantics':'All actual notch/hinge boundaries and hidden dash styles retained; no geometric equality, closed sourcecut or newfill. A human can track both target halves and reject E.','prior_evidence':str((TASK/'all_prior_same_question_evidence.json').relative_to(ROOT)),'no_prior_independent_hold_or_reject_report_for_this_variant':True}
write(TASK/q/'design_difference_audit.json',audit)
actions=[];roles=[]
for idx,color,source_halves,targets in [(0,RED,(0,1),[22,23,25,33]),(1,BLUE,(2,3),[58,59,61,65])]:
    for h in source_halves:
        for side in range(3):
            t=f'hole{h}_{side}';actions.append(style(t,color,1));roles.append(f'Source opening{idx+1}, half{h}, existing contour side{side}; together the six edges identify the bent two-face perimeter, with its original visible/hidden style preserved. The two long base edges correspond to the planar window long edges; four returns preserve the actual seam distinction.')
    for side in targets:
        t=f'Eboundary{side}';actions.append(style(t,color,1));roles.append(f'E planar window{idx+1} actual side {t}; these four original edges make the selective2D rectangular receiver for the source bent contour. Central face crease and uncolored material remain visible, exposing the false incidence match.')
folder=save_candidate(q,vid,'E',actions,roles,audit['new_geometric_misconception'],proof,TASK/q/'primary_math_proof.json')
write(folder/'design_difference_audit.json',audit)
print(folder)
