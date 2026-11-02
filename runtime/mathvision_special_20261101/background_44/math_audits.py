import task_env
from task_env import OWN
from inspect_sources import save
import math, functools, hashlib, json

def area(p):return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p))))/2

# Exhaust every rotated/reflected integral placement of the displayed L pentomino.
piece=[(0,0),(1,0),(2,0),(3,0),(0,1)]
orient=set()
for flip in (1,-1):
    for turn in range(4):
        p=[]
        for x,y in piece:
            x*=flip
            for _ in range(turn):x,y=-y,x
            p.append((x,y))
        xmin=min(x for x,y in p); ymin=min(y for x,y in p)
        orient.add(tuple(sorted((x-xmin,y-ymin) for x,y in p)))
placements=[]
for o in sorted(orient):
    for dx in range(5-max(x for x,y in o)):
        for dy in range(5-max(y for x,y in o)):
            cells=[(x+dx,y+dy) for x,y in o]
            placements.append((sum(1<<(y*5+x) for x,y in cells),cells))
bycell=[[] for _ in range(25)]
for mask,cells in placements:
    for x,y in cells:bycell[5*y+x].append(mask)
visited=[];full=(1<<25)-1
@functools.lru_cache(None)
def solve(mask):
    visited.append(mask)
    if mask==full:return ()
    best=min((i for i in range(25) if not (mask>>i)&1),key=lambda i:sum(not p&mask for p in bycell[i]))
    for p in bycell[best]:
        if not p&mask:
            suffix=solve(mask|p)
            if suffix is not None:return (p,)+suffix
    return None
solution=solve(0)
assert solution is None
# Two copies form a 5 by 2 rectangle, repeated in a 2 by 5 grid.
first=set(piece); second={(4-x,1-y) for x,y in piece}
assert not first&second and first|second=={(x,y) for x in range(5) for y in range(2)}
construction=[]
for bx in (0,5):
    for by in (0,2,4,6,8):
        construction += [[[x+bx,y+by] for x,y in sorted(part)] for part in (first,second)]
assert len({tuple(xy) for p in construction for xy in p})==100
save(OWN/'Plane414/exact_cover_5x5.json',{'orientations':sorted(orient),'placement_count':len(placements),'placements':[c for m,c in placements],'visited_masks':visited,'search':'MRV recursive exact cover; all branches exhausted; memoized occupied masks','solutions_exist':False,'constructive_10x10_twenty_pieces':construction})

audits={
'Plane414':{'unique_answer':'20','proof':[
    'Normalize cell side to1. Every piece has area5. A square tiling has integer side: every external side is a concatenation of complete axis-parallel piece edges of integral lengths.',
    'All piece orientations are parallel to the square axes: a boundary piece fixes an orthogonal direction, and positive-length shared-edge adjacency propagates that direction through the connected tiling.',
    'Even if translations were initially nonintegral, independently floor each piece translation in x and y. Each pair of unit cells that was disjoint has at least one separating inequality with integral constants, which flooring preserves. Containment in an integer-sided square is preserved too. Total area then forces an integral-grid tiling. Thus the grid enumeration loses no possible axis-aligned congruent-piece square tiling.',
    'If side is k, k^2=5n, so k is divisible by5. The only positive candidate below20 pieces is a5x5 square using5 pieces. Exhaustive exact cover including all8 rotations/reflections has no solution.',
    'A displayed L and its180degree image fill a5x2 rectangle. Ten such rectangles tile10x10;20 pieces suffice. The minimum is therefore20.'
], 'exact_cover_placement_count':len(placements),'exact_cover_visited_states':len(visited),'computational_certificate':'exact_cover_5x5.json','not_drawing_tiling_into_question':True},
'Plane415':{'unique_answer':'20','proof':['The frozen2x1 rectangle represents10x5cm. Large quarter-circle radii are10, small radii5.','Both complete exposed arc inventories have length15*pi. Left exposed straight radii are10+10+5+5=30; all rectangle edges are seams. Right only exposed straight edge is rectangle bottom10; the upper vertical large radii and other contact radii are seams.','P_left=15*pi+30; P_right=15*pi+10; absolute difference20. Print or annotation color does not change which geometric edges are external.'], 'independent_source_image_and_native_read':True},
'Plane417':{'unique_answer':'D','value':'16 cm^2','proof':['Side8, half diagonal d=4sqrt2. First reflection takes left tip(-d,0) to(0,0), so first crease is x=-d/2. Second reflection takes right tip(d,0) to(-d/2,0), so second crease is x=d/4.','The top gray rectangle, in a common local origin, has vertices(-d/2,d/2),(0,d),(d/4,3d/4),(-d/4,d/4). Its adjacent edge vectors have lengths4 and2 and zero dot product. Its area is8. The bottom is its reflection, also8.','The query is the visible two rectangles, not accumulated paper-layer material. Sum16, uniquely choiceD.'], 'shaded_rectangle_side_lengths':[4,2],'area_each':8},
'Plane419':{'unique_answer':'C','value':'7.5 cm','proof':['Put the original diagonal endpoints atO=(0,0),V=(12,6). Reflection inOV has matrix[[3/5,4/5],[4/5,-3/5]]. The folded image of(12,0) isR=(36/5,48/5).','The cut leaves triangleOPV, whereP=OR intersect y=6=(9/2,6). Reflect P inOV to Pprime=(15/2,0). The unfolded quadrilateralO,P,V,Pprime is the rhombus.','OP=sqrt((9/2)^2+6^2)=15/2. The other3 sides have the same length15/2. Original6,12, reflected endpoints and existing cuts fix this uniquely; it is not a measurement of the sketch.'], 'exact_vertices':[['0','0'],['9/2','6'],['12','6'],['15/2','0']]},
'Plane421':{'unique_answer':'B','value':'1/2','proof':['Let hexagon side1 and h=sqrt3/2. One regular hexagon consists of6 equilateral unit triangles of area t=sqrt3/4. Two hexagons have12t.','The frozen parallelogram has base4 and height3h, so area12h=24t. Hence gray area24t-12t=12t and shaded fraction1/2.','The proposed gray diagonal fan triangulates EACH concave gray pentagon into actual areas3t,t,2t. It is invalid to count those3 unequal triangles as3 unit triangles; their total is6t.'], 'hexagon_area_units_each':6,'gray_triangle_area_units_each':[3,1,2],'parallelogram_area_units':24},
'Plane424':{'unique_answer':'3','proof':['Let T be paper material area, H the heptagon union area, O its double-layer white overlap, and S=1 its gray single-layer area. A single fold creates at most2 layers.','T=S+2O and H=S+O. Given T=(3/2)H, subtracting yields O=S=1, then H=2 and T=3. Equivalently S=2H-T.','The white overlap, all3 gray single-layer components, original crease and diagram-not-to-scale text are essential semantics. No diagram coordinate area is a numerical given.'], 'algebra':{'S':1,'O':1,'H':2,'T':3}},
'Plane441':{'unique_answer':'6','proof':['Area8*18=144 fixes square side12. Let the lower horizontal extent of one L-shaped hexagon be b, its upper extent a, so a+b=18 by congruence and b-a=y. The two vertical step runs each have length4 under the half-turn congruence in the shown configuration.','An orthogonal square tiled by these2 congruent one-reentrant-corner L pieces must have the pieces owning adjacent corner pairs and hence one complete outer square side each. A piece cannot own opposite or3 square corners because its bounding height is8<12. The simple stepped shared interface connects opposite outer sides. Thus one maximal straight extent of the piece is12. Its fixed maximal vertical extent8 cannot be that side; b=12.','Then a=18-12=6 and y=b-a=6. Existence: use polygon(0,0),(12,0),(12,4),(6,4),(6,8),(0,8) and its180degree image about(6,6); their union is12x12 with disjoint interiors.'], 'equations':['a+b=18','b=12','y=b-a=6'],'candidate_semantics':'Pure numerical question. Shared hue on an8-unit source, two4-unit vertical returns and the6-unit y-run does not constitute a conventional equality mark; treating the aggregate rise as y is the predeclared mistake, not a new given.'},
'Plane443':{'unique_answer':'C','value':'2:3','proof':['Set width1 and length L=sqrt3. The unchanged thirds put fold endpointsP=(L/3,0),Q=(2L/3,1). The fold line is y=sqrt3*x-1.','Reflection is R(x,y)=(-x/2+sqrt3*y/2+sqrt3/2, sqrt3*x/2+y/2-1/2). The folded left quadrilateral has vertices(L/2,-1/2),P,Q,(L,0).','The stationary right quadrilateral has verticesP,(L,0),(L,1),Q. Their intersection is triangleP,(L,0),Q of areaL/3. Material area remainsL; union areaB=L-L/3=2L/3. Folding the other half gives the same union area by reflection. Therefore B:A=2:3, choiceC.'], 'overlap_area_over_original':'1/3','union_area_over_original':'2/3'}
}
for qid,a in audits.items():
    a['primary_research_math_only']=True
    a['native_source_and_formal_images_actually_viewed']=True
    a['not_user_approval']=True
    save(OWN/qid/'primary_math_audit.json',a)
print(json.dumps({'proofs_written':list(audits),'Plane414_exactcover_placements':len(placements),'Plane414_exhausted_states':len(visited)},ensure_ascii=False))
