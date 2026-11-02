from common23 import *
import itertools,math
def norm(s):
    mx=min(x for x,y in s);my=min(y for x,y in s)
    return frozenset((x-mx,y-my) for x,y in s)
def forms(s):
    out=set()
    for flip in [-1,1]:
        t={(flip*x,y) for x,y in s}
        for i in range(4):
            out.add(norm(t));t={(-y,x) for x,y in t}
    return out
def placements(s,board):
    out=set();mx=max(x for x,y in board);my=max(y for x,y in board)
    for f in forms(s):
        for x in range(mx+1):
            for y in range(my+1):
                p=frozenset((a+x,b+y) for a,b in f)
                if p<=board:out.add(p)
    return sorted(out,key=lambda p:sorted(p))
def cells(meta,prefix):
    es={frozenset(tuple(p) for p in o['geometry']['points']) for o in meta['objects'] if o['id'].startswith(prefix)}
    coords=[p for e in es for p in e];out=set()
    for x in range(min(p[0] for p in coords),max(p[0] for p in coords)):
        for y in range(min(p[1] for p in coords),max(p[1] for p in coords)):
            vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
            if all(frozenset([vs[i],vs[(i+1)%4]]) in es for i in range(4)):out.add((x,y))
    return norm(out)
m=read(OUT/'Plane233/fresh_context.json');board=cells(m,'given_');result={}
for letter in 'ABCDE':
    shape=cells(m,letter+'_');ps=placements(shape,board)
    tilings=[t for t in itertools.combinations(ps,3) if len(set().union(*t))==15]
    result[letter]={'cells':sorted(shape),'orientations':len(forms(shape)),'placements':len(ps),'solutions':len(tilings),'witnesses':[[sorted(p) for p in t] for t in tilings]}
assert [result[x]['solutions'] for x in 'ABCDE']==[2,0,0,0,0]
write(OUT/'Plane233/math_primary_proof.json',{'method':'Fresh independent primary enumeration from CURRENT frozen edges, all translations and all D4 forms; every unordered triple enumerated. No prior enumeration imported.','board':sorted(board),'results':result,'unique_answer':'A','notch_correspondence_transform':{'formula':'(x,y)->(22-x,9-y)','maps':[[[14,8],[8,1]],[[14,7],[8,2]],[[15,8],[7,1]]]},'no_internal_source_edges_styled':True,'no_cut_or_region_added':True})
m=read(OUT/'Plane192/fresh_context.json');data={}
for i,l in enumerate('ABCD'):
    segs=[o['geometry']['points'] for o in m['objects'] if o['id'].startswith('route'+str(i)+'_')]
    ds=[(b[0]-a[0],b[1]-a[1]) for a,b in segs]
    assert all(dx>0 and abs(dy)==dx for dx,dy in ds)
    assert sum(dx for dx,dy in ds)==8
    data[l]={'segments':segs,'horizontal_units':[dx for dx,dy in ds],'length_exact':'8*sqrt(2)','marked_first_run_unit_count':ds[0][0]}
write(OUT/'Plane192/math_primary_proof.json',{'method':'Fresh exact integer-coordinate length proof. Each segment has |dy|=dx, so length=sqrt2*dx. Each route total dx=8. All routes equal; E is the unchanged explicit image option.','routes':data,'unique_answer':'E','source_distinction':'Every route is piecewise continuous on the same square grid. Same color identifies a run category; it is not an equality or new unit definition.'})
s={(0,0),(1,0),(2,0),(3,0),(0,1)};board5=frozenset(itertools.product(range(5),repeat=2));ps=placements(s,board5)
nodes=0
def cover(rem,used):
    global nodes
    nodes+=1
    if not rem:return used
    opts=[(p,[q for q in ps if p in q and q<=rem]) for p in rem]
    point,options=min(opts,key=lambda p:(len(p[1]),p[0]))
    for q in options:
        r=cover(rem-q,used+[q])
        if r:return r
    return None
no5=cover(board5,[]);assert no5 is None
pair=[s,{(4-x,1-y) for x,y in s}]
assert len(pair[0]&pair[1])==0 and set.union(*pair)==set(itertools.product(range(5),range(2)))
witness=[sorted((x+dx,y+dy) for x,y in p) for dx in [0,5] for dy in range(0,10,2) for p in pair]
assert len(witness)==20 and len(set().union(*map(set,map(lambda p:map(tuple,p),witness))))==100
write(OUT/'Plane263/math_primary_proof.json',{'method':'Fresh independent exact-cover search including reflections excludes 5x5; fresh constructive 10x10 witness uses ten 2x5 rectangles, each formed by two L tiles.','cells':sorted(s),'forms':len(forms(s)),'placements_5x5':len(ps),'search_nodes':nodes,'tilings_5x5':0,'tiling_10x10':witness,'minimality':'For copies of the shown unit lattice polygon, square side is an integer and area=5*n. A square divisible by5 has side divisible by5. First sides are5,10: exclude5 and construct10, so n=20.','unique_answer':20,'annotated_hook_transform':'Geometric boundary half-turn (x,y)->(5-x,2-y): notch upright x=1,y=1..2 maps to outer terminal x=4,y=0..1; shoulder y=1,x=1..4 maps to itself. These are actual mating interfaces for a second tile, but two tiles yield a 2x5 RECTANGLE, not a square.','two_copy_rectangle':[sorted(p) for p in pair]})
neg=lambda a:tuple(-v for v in a)
pos={'U':(0,2),'V':(1,2),'W':(2,2),'Y':(2,3),'X':(1,1),'Z':(1,0)}
frames={'V':((1,0,0),(0,1,0),(0,0,1))};queue=['V']
while queue:
    q=queue.pop(0);r,u,n=frames[q];x,y=pos[q]
    for name,(nx,ny) in pos.items():
        dx,dy=nx-x,ny-y
        f={ (1,0):(neg(n),u,r),(-1,0):(n,u,neg(r)),(0,1):(r,neg(n),u),(0,-1):(r,n,neg(u))}.get((dx,dy))
        if f is not None:
            if name in frames:assert frames[name]==f
            else:frames[name]=f;queue.append(name)
assert frames['Y'][2]==neg(frames['X'][2]);assert frames['Z'][2]!=neg(frames['X'][2])
write(OUT/'Solid220/math_primary_proof.json',{'method':'Fresh primary exact 90-degree orthonormal-frame propagation along shared square edges from V; no prior fold result imported. Normal is the third vector of each frame.','net_cells':pos,'frames':frames,'opposite_pairs':[['U','W'],['V','Z'],['X','Y']],'unique_answer':'E','misconception':'U/W have interveningV and opposite normals. X/Z have no intervening square; normals dot0, not -1. Matching ordered endpoint colors does not assert opposition or change the six-square folding problem.','frozen_world_projection_visibility_preserved':True})
write(OUT/'Plane373/assessment.json',{'stage':'material_refinement','question_id':'Plane373','status':'SKIPPED_NO_CLEAN_MEANINGFUL_REPAIR','old_finals':{'initial_spoke_orientation_binding':['E','E'],'halfturn_reflected_sector_binding':['C','C']},'old_status':'Initial B preset missed; C/C remains primary HELD, not promoted.','math':'r=1, distance11pi -> clockwise angle11pi -> half-turn. Source white top/grey lower-left/black lower-right becomes white bottom/grey upper-right/black upper-left: uniquelyE.','assessed_new_hypotheses':['Source/options point or partial-spoke matching still risks treating new colors as physical rolling marks; then no option preserves full colored pattern.','Uniform rotation-invariant boundary marks would repair physical semantics but convey no wrong correspondence.','Marking only K-L/rotation arrow/radius would be formula or attention emphasis without a new meaningful feature-to-option mapping.'],'reason':'No simple useful targeted wrong correspondence found that preserves physical-pattern semantics, tiny source-sector legibility and unique human answer. No new PNG or solver calls; old held C/C not queued.','native_source_and_both_prior_candidates_viewed':True,'independent_review_required_for_any_future_design':True})
print(json.dumps({'Plane233':{k:v['solutions'] for k,v in result.items()},'Plane192':'E','Plane263':{'answer':20,'nodes':nodes,'placements':len(ps)},'Solid220':{k:v[2] for k,v in frames.items()},'Plane373':'skip'}))
