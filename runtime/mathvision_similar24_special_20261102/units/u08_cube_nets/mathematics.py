from worker import *
from collections import deque, Counter
from fractions import Fraction as F
import re

def neg(v):return tuple(-x for x in v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(v,s):return tuple(s*x for x in v)
def frame(cells):
    cells=set(map(tuple,cells));root=min(cells)
    found={root:((1,0,0),(0,1,0),(0,0,1))};queue=deque([root]);conflicts=[]
    while queue:
        a=queue.popleft();u,v,n=found[a]
        for delta,f in [((1,0),(neg(n),v,u)),((-1,0),(n,v,neg(u))),((0,1),(u,neg(n),v)),((0,-1),(u,n,neg(v)))]:
            b=add(a,delta)
            if b not in cells:continue
            if b in found:
                if found[b]!=f:conflicts.append([a,b])
            else:found[b]=f;queue.append(b)
    assert len(found)==len(cells)
    return found,conflicts

def mapped(fr,cell,p):
    u,v,n=fr[cell]
    return add(scale(n,F(1,2)),add(scale(u,p[0]-cell[0]-F(1,2)),scale(v,p[1]-cell[1]-F(1,2))))
def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x
def scene(q):return read(OWN/q/'source_scene_snapshot.json')

def proof228():
    results={}
    for panel in scene('Solid228')['net_panels']:
        cells=[c['cell'] for c in panel['cells']];fr,con=frame(cells)
        normals=[f[2] for f in fr.values()]
        results[panel['id']]={'frames':serial(fr),'centers':{str(c):serial(scale(f[2],F(1,2))) for c,f in fr.items()},'six_distinct_faces':len(set(normals))==6,'repeated_faces':{str(n):[c for c,f in fr.items() if f[2]==n] for n,count in Counter(normals).items() if count>1},'cycle_conflicts':con}
    assert [k for k,v in results.items() if not v['six_distinct_faces']]==['D']
    save(OWN/'Solid228/primary_math_proof.json',{'question_id':'Solid228','independently_recomputed':True,'root_frame':'u=(1,0,0),v=(0,1,0),n=(0,0,1) at lexicographically first cell','propagation':'east:(-n,v,u), west:(n,v,-u), north:(u,-n,v), south:(u,n,-v); centers=n/2; vertices=n/2 +/-u/2 +/-v/2','why_sufficient':'Connected tree hinges uniquely fix oriented faces of any convex unit cube, up to a global rigid motion and reflection. Six distinct signed-axis normals with centers n/2 construct exactly the six faces, edge incidences agree, face interiors disjoint. D repeats a face so overlaps and leaves another face empty. It is necessary for every folding sign consistent with a convex cube; folding the entire cube inside-out changes all normals and preserves repetition.','panels':results,'unique_correct':'D','source_preserved':True})
    print('Solid228',[(k,v['six_distinct_faces'],v['repeated_faces']) for k,v in results.items()])

def proof193():
    sc=scene('Solid193');obs={o['id']:o for o in sc['objects']};results={}
    axes={(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}
    for i,panel in enumerate(sc['net_panels']):
        cells=[tuple(c['xy']) for c in panel['unit_cells']];fr,con=frame(cells)
        missing=axes-{f[2] for f in fr.values()};assert len(missing)==1 and not con
        missing=next(iter(missing));off=panel['page_offset'];tri=[]
        for j in range(4):
            s0=obs[f'net{i}triangle{j}side0']['points'];s1=obs[f'net{i}triangle{j}side1']['points']
            a=(F(str(s0[0][0]))-off[0],F(str(s0[0][2]))-off[1]);b=(F(str(s1[0][0]))-off[0],F(str(s1[0][2]))-off[1]);peak=(F(str(s0[1][0]))-off[0],F(str(s0[1][2]))-off[1])
            candidates=[]
            for cell in cells:
                x,y=cell
                for side,ends,d in [('W',[(x,y),(x,y+1)],(-1,0)),('E',[(x+1,y),(x+1,y+1)],(1,0)),('S',[(x,y),(x+1,y)],(0,-1)),('N',[(x,y+1),(x+1,y+1)],(0,1))]:
                    if set(ends)=={a,b} and add(cell,d) not in cells:candidates.append((cell,side,d))
            assert len(candidates)==1
            cell,side,d=candidates[0];u,v,n=fr[cell];normal=scale(u,d[0]) if d[0] else scale(v,d[1]);newpeak=scale(normal,F(1,2))
            tri.append({'index':j,'base':[a,b],'original_peak':peak,'hinge_cell':cell,'hinge_side':side,'destination_normal':normal,'folded_peak':newpeak,'folded_vertices':[mapped(fr,cell,a),mapped(fr,cell,b),newpeak],'fills_missing_face':normal==missing})
        valid=all(t['fills_missing_face'] for t in tri) and len({tuple(sorted((t['folded_vertices'][0],t['folded_vertices'][1]))) for t in tri})==4
        results[str(i+1)]={'frames':fr,'missing_face_normal':missing,'triangles':tri,'valid':valid}
    assert [k for k,v in results.items() if not v['valid']]==['3','5']
    save(OWN/'Solid193/primary_math_proof.json',serial({'question_id':'Solid193','independently_recomputed':True,'method':'Five unit squares fold by the exact signed-axis recurrence. Each flap is one right-isosceles quarter of the cut face. Its base remains fixed and its tip folds onto the center of the face outward from that hinge. The normal identifies this destination. A valid cut cube requires all four tips at the single missing-face center and four distinct base edges.','necessity_sufficiency':'Triangles have fixed base length1 and altitude1/2. Destination normal differs from missing normal => overlaps an occupied full square or covers a wrong face. If all four destination normals equal missing and bases are the four distinct sides, their right-isosceles interiors are disjoint and exactly tile it. These local rigid hinge mappings give an explicit assembly.','panels':results,'unique_correct':{'letter':'E','value':'3 and 5'},'duplicate_wrong_choices_C_D':'Both retain 2 and 4 and are false; no relabeling allowed.'}))
    print('Solid193',[(k,v['valid'],[t['destination_normal'] for t in v['triangles']]) for k,v in results.items()])

def proof187():
    sc=scene('Solid187');results={}
    for panel in sc['net_panels']:
        cells=panel['unit_cells'];fr,con=frame(cells);assert not con
        features=[];groups={};interior=0
        for cell in map(tuple,cells):
            x,y=cell
            for r in panel['cutout_rectangles']:
                x0,y0,x1,y1=map(lambda a:F(str(a)),r)
                xa,xb=max(x,F(x0)),min(x+1,F(x1));ya,yb=max(y,y0),min(y+1,y1)
                if xa>=xb or ya>=yb:continue
                sides=[]
                for side,test,a,b in [('W',xa==x,(x,y),(x,y+1)),('E',xb==x+1,(x+1,y),(x+1,y+1)),('S',ya==y,(x,y),(x+1,y)),('N',yb==y+1,(x,y+1),(x+1,y+1))]:
                    if test:sides.append((side,tuple(sorted((mapped(fr,cell,a),mapped(fr,cell,b))))))
                assert len(sides)<=1
                entry={'cell':cell,'rectangle_clipped':[xa,ya,xb,yb],'side':sides[0][0] if sides else None,'folded_cube_edge':sides[0][1] if sides else None}
                features.append(entry)
                if sides:groups.setdefault(sides[0][1],[]).append(entry)
                else:interior+=1
        paired=[e for e,halves in groups.items() if len(halves)==2]
        midpoints=[scale(add(*e),F(1,2)) for e in paired]
        opposite=len(midpoints)==2 and add(*midpoints)==(0,0,0)
        results[panel['id']]={'frames':fr,'features':features,'paired_edge_count':len(paired),'unpaired_notch_count':sum(len(h) for e,h in groups.items() if len(h)!=2),'interior_face_window_count':interior,'paired_edge_midpoints':midpoints,'opposite_parallel_edges':opposite}
    assert [k for k,v in results.items() if v['opposite_parallel_edges']]==['C']
    save(OWN/'Solid187/primary_math_proof.json',serial({'question_id':'Solid187','independently_recomputed':True,'world_geometry':'Target zero-thickness cube shell has openings straddling x=0,z=1 and x=1,z=0, both parallel to y, with centrally opposite edge midpoints (0,1/2,1) and (1,1/2,0). No tunnel walls or wall thickness inferred.','folding':'Every net has identical six-square tree. Exact face frames determine each clipped rectangle and whether two half-notches share a cube edge. Coordinate origin and orientation arbitrary global rigid frame; no screenshot length used.','panels':results,'proof':'A and D each have two edge holes with adjacent parallel edge midpoints, not central opposites. B has one complete edge hole and two unpaired flap notches on different edges; it cannot give the same removed shell. E has two fully interior windows, affecting only two opposite faces rather than the four faces at two opposite edges. Only C has two paired holes on centrally opposite parallel edges; rotate its cube frame onto target. This exhaustive invariant distinction also proves uniqueness under all cube rotations/reflections. Schematic notch depths are not dimensions.','unique_correct':'C','projection':'Target cabinet matrix and frozen displayed/hidden notch segments are unchanged, inspected against JPG and PNG. Net views are x,z in y=0, so oblique projection does not distort their local adjacency.'}))
    print('Solid187',[(k,v['paired_edge_count'],v['unpaired_notch_count'],v['interior_face_window_count'],v['opposite_parallel_edges']) for k,v in results.items()])

if __name__=='__main__':
    proof187();proof193();proof228()
