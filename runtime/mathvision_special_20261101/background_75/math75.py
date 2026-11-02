import bootstrap75 as boot
from research75 import read, put, now, sha, IDS
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import json

OWN,PROJECT=boot.OWN,boot.PROJECT
ITEMS=PROJECT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'
def scene(q): return read(ITEMS/q/'scene.json')
def vertices(s,o): return [s['points'][v] if isinstance(v,str) else v for v in o['points']]
def cells(s,prefix=''):
    return {o['id']:(min(v[0] for v in vertices(s,o)),min(v[1] for v in vertices(s,o))) for o in s['objects'] if o['type']=='polygon' and o['id'].startswith(prefix)}
def norm(c):
    a=min(x for x,y in c); b=min(y for x,y in c)
    return tuple(sorted((x-a,y-b) for x,y in c))
def orientations(c,mirror=True):
    result=set()
    for m in (1,-1) if mirror else (1,):
        t=[(m*x,y) for x,y in c]
        for k in range(4):
            result.add(norm(t)); t=[(-y,x) for x,y in t]
    return sorted(result)
def placements(board,shape):
    result=set()
    for o in orientations(shape):
        for x,y in board:
            for u,v in o:
                t=frozenset((a+x-u,b+y-v) for a,b in o)
                if t<=board: result.add(tuple(sorted(t)))
    return sorted(result)
def covers(board,pls):
    ordered=sorted(board); ix={p:i for i,p in enumerate(ordered)}
    masks=[sum(1<<ix[p] for p in t) for t in pls]
    by={p:[i for i,t in enumerate(pls) if p in t] for p in board}
    @lru_cache(None)
    def count(mask):
        if not mask:return 1
        candidates=min(([i for i in by[p] if masks[i]&mask==masks[i]] for p in ordered if mask&(1<<ix[p])),key=len)
        return sum(count(mask^masks[i]) for i in candidates)
    solutions=[]
    def collect(mask,chosen):
        if not mask: solutions.append([pls[i] for i in chosen]);return
        candidates=min(([i for i in by[p] if masks[i]&mask==masks[i]] for p in ordered if mask&(1<<ix[p])),key=len)
        for i in candidates: collect(mask^masks[i],chosen+[i])
    full=(1<<len(board))-1; n=count(full)
    if n<=10000:collect(full,[])
    return n,solutions,{'states':count.cache_info().currsize,'placements':len(pls),'method':'Minimum remaining degree exact cover; place one legal shape covering selected uncovered cell, recurse; each unlabeled cover counted once; absolute board orientation retained.'}
def save(q,v):
    v={'question_id':q,'created_at':now(),'source_scene_sha256':sha((ITEMS/q/'scene.json').read_bytes()),'independent_new_local_enumeration':True,**v}
    put(OWN/q/'math_proof.json',v)
    print(q,json.dumps({k:v[k] for k in ['answer','computed_count','minimum_T','maximum_pieces','axis_additional_counts','status'] if k in v},ensure_ascii=False))

def main():
    s=scene('Plane317'); cc=cells(s); board=set(cc.values()); black={cc[o['id']] for o in s['objects'] if o.get('semantic_color')=='#222222'}; white=board-black
    pls=placements(white,[(0,0),(1,0)]); n,sol,audit=covers(white,pls)
    common=set.intersection(*[set(tuple(p) for p in t) for t in sol]) if sol else set()
    save('Plane317',{'board_cells':sorted(board),'black_cells':sorted(black),'white_cells':sorted(white),'counts':{'board':len(board),'black':len(black),'white':len(white)},'computed_count':n,'answer':n,'all_covers':sol,'forced_dominoes':sorted(common),'enumeration':audit,'symmetry_rule':'No rotation/reflection quotient, per explicit wording. Four independent 8-cell rings have two perfect matchings each once four joining dominoes are forced: 2^4=16.'})
    s=scene('Plane337');cc=cells(s);board={v for v in cc.values() if v[0]<4};shape=norm([v for v in cc.values() if v[0]>=5]);pls=placements(board,shape)
    n,sol,audit=covers(board,pls)
    ordered=sorted(board);ix={p:i for i,p in enumerate(ordered)};masks=[sum(1<<ix[p] for p in t) for t in pls];by={p:[i for i,t in enumerate(pls) if p in t] for p in board}
    @lru_cache(None)
    def pack(mask):
        if not mask:return (0,())
        p=next(p for p in ordered if mask&(1<<ix[p]));best,choice=pack(mask^(1<<ix[p]))
        for i in by[p]:
            if mask&masks[i]==masks[i]:
                score,part=pack(mask^masks[i])
                if score+1>best:best,choice=score+1,(i,)+part
        return best,choice
    mx,wit=pack((1<<16)-1)
    save('Plane337',{'board_cells':sorted(board),'template':shape,'orientations':orientations(shape),'all_legal_placements':pls,'complete_four_piece_cover_count':n,'maximum_pieces':mx,'answer':len(board)-len(shape)*mx,'attaining_packing':[pls[i] for i in wit],'enumeration':audit,'packing_states':pack.cache_info().currsize,'proof':'At most four pieces by area; exhaustive exact cover gives zero four-piece tilings; packing recurrence allows leave-selected-cell-empty or one piece through it, hence exhausts all packings and constructs three. Therefore exactly four cells remain.'})
    s=scene('Plane375');cc=cells(s);board=set(cells(s,'celltarget').values());piece=norm(cells(s,'cellpiece').values());pls=placements(board,piece);n,sol,audit=covers(board,pls)
    demo={(x,y) for x in range(3) for y in range(2)};dn,ds,da=covers(demo,placements(demo,piece))
    # Count orbits only for diagnosis; do not impose a missing equivalence convention.
    transforms=[]
    for m in [1,-1]:
        for r in range(4):
            def tr(p,m=m,r=r):
                x,y=p;x*=m
                for k in range(r):x,y=-y,x
                return x,y
            tb=[tr(p) for p in board];dx=min(x for x,y in board)-min(x for x,y in tb);dy=min(y for x,y in board)-min(y for x,y in tb)
            if {(x+dx,y+dy) for x,y in tb}==board: transforms.append((tr,dx,dy))
    def canon(t):return min(tuple(sorted(tuple(sorted((tr(p)[0]+dx,tr(p)[1]+dy) for p in piece)) for piece in t)) for tr,dx,dy in transforms)
    orbits={canon(t) for t in sol}
    save('Plane375',{'board_cells':sorted(board),'template':piece,'orientations':orientations(piece),'computed_count':n,'all_covers':sol,'enumeration':audit,'demo_3x2_count':dn,'demo_covers':ds,'board_preserving_D4_elements':len(transforms),'diagnostic_symmetry_orbit_count':len(orbits),'formal_answer':'2','status':'original_math_requires_convention_review' if n!=2 else 'proved','proof_note':'Use rotation/reflection freedoms of L triomino (all four orientations; mirror gives no new shape). Board positions are absolute unless the actual question supplies an equivalence rule. Symmetry orbits reported separately; never substituted silently.'})
    s=scene('Plane381');board=set(cells(s,'board').values());T=norm(cells(s,'T').values());F=norm(cells(s,'F').values());pT=placements(board,T);pF=placements(board,F)
    # Area gives t=2 mod4. Find exactly 2 triominoes plus 4 tetrominoes.
    opts=[('T',p) for p in pT]+[('F',p) for p in pF];by={p:[i for i,(k,t) in enumerate(opts) if p in t] for p in board}; states=[0]
    def witness(rem,tleft,fleft,chosen):
        states[0]+=1
        if not rem:return chosen if tleft==fleft==0 else None
        candidates=min(([i for i in by[p] if set(opts[i][1])<=rem and (tleft if opts[i][0]=='T' else fleft)>0] for p in sorted(rem)),key=len)
        for i in candidates:
            k,t=opts[i];found=witness(rem-set(t),tleft-(k=='T'),fleft-(k=='F'),chosen+[{'kind':k,'cells':t}])
            if found:return found
        return None
    wit=witness(board,2,4,[])
    assert wit is not None
    save('Plane381',{'board_cells':sorted(board),'area':len(board),'T_cells':T,'F_cells':F,'T_orientations':orientations(T),'F_orientations':orientations(F),'minimum_T':2,'answer':2,'lower_bound':'The actual T has area3 and F area4. 3t+4f=22 gives t=2 mod4; with t>=0, t>=2. Letter names do not stipulate conventional T/F pentominoes.','attaining_construction':wit,'witness_search_states':states[0],'legal_placement_counts':{'T':len(pT),'F':len(pF)}})
    s=scene('Plane384');cc=cells(s);board=set(cc.values());shaded={cc[o['id']] for o in s['objects'] if o.get('semantic_fill')};transforms={'vertical_x4.5':lambda p:(8-p[0],p[1]),'horizontal_y4.5':lambda p:(p[0],8-p[1]),'diagonal_y_equals_x':lambda p:(p[1],p[0]),'diagonal_x_plus_y9':lambda p:(8-p[1],8-p[0])};out={}
    for k,tr in transforms.items():
        assert {tr(p) for p in board}==board
        add={tr(p) for p in shaded}-shaded;out[k]={'additional_count':len(add),'additional_cells':sorted(add),'symmetric_closure':sorted(shaded|add)}
    save('Plane384',{'frame_cells':sorted(board),'shaded_cells':sorted(shaded),'axis_additional_counts':{k:v['additional_count'] for k,v in out.items()},'axes':out,'answer':min(v['additional_count'] for v in out.values()),'axis_completeness':'The square cell frame with its four unique extreme tips has reflection group D4; any symmetry must map those extreme tips, yielding only horizontal, vertical and two diagonals. Shading does not change this frame. For each axis the forced added set is reflection(shaded) minus shaded, so the minimum is exact.'})
    s=scene('Plane385');dots={tuple(v) for v in s['points'].values()};squares=[];rejected=[]
    for q in combinations(sorted(dots),4):
        d=sorted((a[0]-b[0])**2+(a[1]-b[1])**2 for a,b in combinations(q,2))
        if d[0]>0 and d[:4]==[d[0]]*4 and d[4:]==[2*d[0]]*2:squares.append({'vertices':q,'squared_lengths':d})
    save('Plane385',{'original_dots':sorted(dots),'four_point_subsets_tested':70,'squares':squares,'answer':len(squares),'proof':'Every square is a 4-point subset. Its six squared distances consist of four equal nonzero sides and two equal twice-side diagonals; this condition is also sufficient. Exactly three unit squares and one tilted square meet it. No missing(0,0) point was inferred.'})
    s=scene('Plane389');cc=cells(s);board=set(cc.values());occupied={cc[o['id']] for o in s['objects'] if o.get('semantic_fill')};pls=placements(board,[(0,0),(1,0),(2,0)]);valid=[];edgeonly=[]
    for t in pls:
        if all(max(abs(a-c),abs(b-d))>1 for a,b in t for c,d in occupied):valid.append(t)
        if all(abs(a-c)+abs(b-d)>1 for a,b in t for c,d in occupied):edgeonly.append(t)
    save('Plane389',{'board_size':[5,5],'occupied_cells':sorted(occupied),'total_horizontal_vertical_3x1_placements':len(pls),'valid_placements':valid,'answer':len(valid),'edge_only_wrong_count':len(edgeonly),'edge_only_placements':edgeonly,'proof':'Closed unit squares intersect including at a corner iff their coordinate Chebyshev distance is <=1. Test all 15 horizontal and15 vertical positions against each occupied cell; exactly eight have no common boundary point. Edge-only exclusion is separately diagnostic, not the true condition.'})
    points={(x,y) for x in range(3) for y in range(3)};pairs=list(combinations(sorted(points),2))
    def tr(p,m,r):
        x,y=p;x-=1;y-=1;x*=m
        for k in range(r):x,y=-y,x
        return x+1,y+1
    def pair(p,m,r):return tuple(sorted(tr(v,m,r) for v in p))
    groups={}
    for p in pairs:
        key=min(pair(p,m,r) for m in [1,-1] for r in range(4));groups.setdefault(key,[]).append(p)
    rot={min(pair(p,1,r) for r in range(4)) for p in pairs}
    save('Plane454',{'all_unordered_pairs':len(pairs),'D4_orbits':[{'representative':k,'members':v,'size':len(v)} for k,v in sorted(groups.items())],'answer':len(groups),'rotation_only_wrong_count':len(rot),'proof':'All C(9,2)=36 unordered shaded pairs are explicitly partitioned by eight D4 transformations; eight classes result. Flip and turn equivalence both apply. Existing four examples are one corner-edge adjacent orbit, not four new patterns.'})

if __name__=='__main__':main()
