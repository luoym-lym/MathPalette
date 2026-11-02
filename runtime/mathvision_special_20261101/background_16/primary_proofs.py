import tools_local as t
import itertools,math
import numpy as np
OUT={}
def rotations():
    out=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([-1,1],repeat=3):
            m=np.zeros((3,3),dtype=int)
            for i,j in enumerate(perm):m[i,j]=signs[i]
            if round(np.linalg.det(m))==1:out.append(m)
    assert len(out)==24;return out
ROTS=rotations()
def norm(c):
    a=np.array(list(c));a=a-a.min(axis=0);return tuple(sorted(map(tuple,a.tolist())))
def native(q):return t.json.loads((t.ROOT/'SolidGeometry'/('dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/'+q+'/scene.json')).read_text(encoding='utf-8-sig'))
s=native('Solid157');target=norm(s['removed_cube_positions']);matches={}
for name,cubes in s['option_cube_sets'].items():
    matches[name]=[m.tolist() for m in ROTS if norm(np.array(cubes)@m.T)==target]
assert [k for k,v in matches.items() if v]==['C']
OUT['Solid157']={'method':'Independent 24 proper rigid rotations and translation-normalized cube-set equality.','removed_cube_positions':s['removed_cube_positions'],'matching_rotations':matches,'unique_answer':'C','degree_counts':{name:sorted(sum(sum(abs(x-y) for x,y in zip(a,b))==1 for b in cubes) for a in cubes) for name,cubes in s['option_cube_sets'].items()}}

def area(p):return abs(sum(np.cross(p[(i+1)%len(p)]-p[i],p[(i+2)%len(p)]-p[(i+1)%len(p)])*0 for i in [])) if False else abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p))))/2
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def clip(poly,bound):
    p=[np.array(x,dtype=float) for x in poly]
    for i,a in enumerate(bound):
        b=bound[(i+1)%len(bound)];v=b-a;prev=p[-1];new=[]
        for cur in p:
            inc=cross(v,cur-a)>=-1e-12;inp=cross(v,prev-a)>=-1e-12
            if inc!=inp:
                u=cur-prev;alpha=cross(v,a-prev)/cross(v,u);new.append(prev+alpha*u)
            if inc:new.append(cur)
            prev=cur
        p=new
        if not p:break
    return p
L=math.sqrt(3);a=np.array([L/3,0]);b=np.array([2*L/3,1]);u=(b-a)/np.linalg.norm(b-a)
left=[np.array(p) for p in [[0,0],[L/3,0],[2*L/3,1],[0,1]]]
right=[np.array(p) for p in [[L/3,0],[L,0],[L,1],[2*L/3,1]]]
ref=[a+(2*np.outer(u,u)-np.eye(2))@(p-a) for p in left]
over=clip(ref,right);union=area(ref)+area(right)-area(over);assert abs(union/L-2/3)<1e-12
OUT['Plane443']={'method':'Independent line reflection and convex polygon intersection; sum areas minus overlap.','rectangle_area':L,'stationary_half':[p.tolist() for p in right],'reflected_half':[p.tolist() for p in ref],'intersection':[p.tolist() for p in over],'intersection_area':area(over),'union_area':union,'ratio':union/L,'unique_answer':'C','exact_ratio':'2:3'}

counts={'A':(0,2),'B':(1,1),'C':(2,0),'D':(1,0),'E':(0,1)}
balances={omit:sum(counts[k][0]-counts[k][1] for k in counts if k!=omit) for omit in counts}
assert [k for k,v in balances.items() if v==0]==['B']
OUT['Plane278']={'curve_counts_convex_concave':counts,'net_convex_minus_concave_by_omission':balances,'necessity':'All curved edges must be interior seams, paired convex to concave; square outside is straight.','construction':{'lower_left':'C in original orientation','lower_right':'E rotated180degrees so concavity faces left','upper_left':'A rotated90degrees clockwise so concavities face down and right','upper_right':'D rotated90degrees counterclockwise so convexity faces left','seams':['C.top convex fits A.bottom concave','C.right convex fits E.left concave','D.left convex fits A.right concave','D.bottom straight fits E.top straight']},'unique_answer':'B','immutable_design_correction':'Design prose casually paired C two convex with A two concave as a count illustration. That is not the actual2x2 construction; the explicit three curved seams above supply the correct construction. Original design is retained unchanged.'}

positions=list(itertools.product(range(4),repeat=3));start=(1,2,3)
shells={str(day):[p for p in positions if sum(abs(x-y) for x,y in zip(p,start))<=day] for day in range(3)}
false=(1,0,3);falsecount=sum(sum(abs(x-y) for x,y in zip(p,false))<=2 for p in positions)
assert len(shells['2'])==17 and falsecount==13
OUT['Solid178']={'method':'Independent exhaustive Manhattan-distance search over64 cubes.','start_zero_based':start,'within_distance_0_1_2':shells,'count_day2':17,'false_edge_start':false,'false_edge_count_day2':falsecount,'unique_answer':'17'}
OUT['Solid197']={'method':'Square contact geometry and physical sticker count.','proof':['A face midpoint is5cm from the facecenter. Congruent square stickers are diagonally oriented.','Let r be center-to-vertex length of the face sticker. The half edge sticker unfolds to the same square and extends r into the face. Corner contact gives2r=5, so full diagonal2r=5.','Square area=d^2/2=25/2=12.5. There are6 center stickers+12 edge stickers=18 physical squares.','Total=18*25/2=225cm^2. The marked crease is a diagonal; equating it to the marked true side is unsupported.'],'correct_answer':'225','wrong_preset':'450','causal_limits':'No human study, statistical reliability, or per-marker causal isolation. Two-call evidence establishes observed behavior only; control results, if any, must be disclosed separately.'}

patterns=native('Solid151')['face_patterns'];corner=[(0,0),(0,2),(2,0),(2,2)];edgemid=[(0,1),(1,0),(1,2),(2,1)]
def incidence(p):
    rows=p.split('/');return [sum(rows[r][c]=='B' for r,c in ix) for ix in [corner,edgemid,[(1,1)]]]
given=np.array([incidence(p) for p in patterns['given']]).sum(axis=0);options={}
for name,p in zip('ABCDE',patterns['options']):
    total=given+np.array(incidence(p));valid=total[0]%3==0 and total[1]%2==0
    exterior=int(total[0]//3+total[1]//2+total[2]) if valid else None
    options[name]={'raw_black_face_incidences':total.tolist(),'corner_edge_multiplicity_valid':bool(valid),'forced_exterior_black':exterior,'compatible_with_15':bool(valid and exterior<=15 and exterior+1>=15)}
assert [k for k,v in options.items() if v['compatible_with_15']]==['A']
OUT['Solid151']={'method':'Independent corner/edge/facecenter incidence counts, without relying on source answer.','five_given_corner_edge_center_incidences':given.tolist(),'options':options,'unique_answer':'A','existence_note':'The source five-face cube is given to exist; A is the only candidate compatible with any15-black cube. Its15 exterior black cells leave the invisible center white.'}

light=[]
for x,y in itertools.product(range(-3,4),repeat=2):
    d=abs(x)+abs(y)
    if d<=3 and d%2==0:
        light +=[(x,y,z) for z in range(4-d)]
assert len(light)==20
OUT['Solid189']={'method':'Independent layer/column enumeration from sideheight and plan parity.','center_height':4,'distance2_columns':8,'distance2_height_each':2,'light_cubes':light,'correct_answer':20,'false_center_height2_total':18}

paint={}
front=[(0,0),(0,2),(1,1),(2,0),(2,2)];right=[(0,1),(1,0),(1,2),(2,1)]
for y in [0,2]:paint['front' if y==0 else 'back']={(x,y,z) for x,z in front}
for x in [0,2]:paint['left' if x==0 else 'right']={(x,y,z) for y,z in right}
for z in [0,2]:paint['bottom' if z==0 else 'top']={(1,1,z)}
painted=set().union(*paint.values());assert len(painted)==20
OUT['Solid222']={'method':'Independent union of six painted-face cube sets.','painted_cubes_by_face':{k:sorted(v) for k,v in paint.items()},'distinct_painted':sorted(painted),'sum_face_painted_counts':sum(map(len,paint.values())),'overlapping_painted_incidence_count':sum(map(len,paint.values()))-len(painted),'unique_answer':20}

painted5=set();faces5={}
for axis in range(3):
    others=[i for i in range(3) if i!=axis]
    for boundary in [0,4]:
        arr=set()
        for a,b in itertools.product(range(5),repeat=2):
            gray=(a in (0,4) and b in (0,4)) or (a in (1,2,3) and b in (1,2,3) and (a,b)!=(2,2))
            if gray:
                p=[None]*3;p[axis]=boundary;p[others[0]]=a;p[others[1]]=b;arr.add(tuple(p))
        painted5|=arr;faces5[str((axis,boundary))]=sorted(arr)
assert len(painted5)==56
OUT['Plane489']={'method':'Independent six-face union over5x5x5 unit cubes.','face_painted_counts':{k:len(v) for k,v in faces5.items()},'painted56':sorted(painted5),'unpainted':125-len(painted5),'unique_answer':'69/125','wrong_face_multiplicity_result':'53/125'}

def viewsets(q):
    s=native(q)
    if q=='Solid163':
        a=s['two_view_verification'];vis=set(map(tuple,a['visible_cells_each']));black=[set(map(tuple,a[k])) for k in ['first_visible_black','second_visible_black']]
        return [(vis,v) for v in black]
    patterns=s['semantic_models'][0]['source_patterns'];out=[]
    for p in patterns:
        known={}
        for face in ['left','right','top']:
            for r in range(3):
                for c in range(3):
                    xyz=(0,c,r) if face=='left' else (c,0,r) if face=='right' else (r,c,2)
                    if xyz in known:assert known[xyz]==p[face][r][c]
                    known[xyz]=p[face][r][c]
        out.append((set(known),{p for p,v in known.items() if v}))
    return out
for q in ['Solid163','Solid200']:
    (v0,b0),(v1,b1)=viewsets(q);w0=v0-b0;w1=v1-b1;cases=[]
    for m in ROTS:
        rot=lambda ss:{tuple(((np.array(p)-1)@m.T+1).tolist()) for p in ss}
        wb,bb=rot(w1),rot(b1);conflict=(w0&bb)|(b0&wb)
        cases.append({'rotation':m.tolist(),'conflict_cells':sorted(conflict),'white_union':len(w0|wb),'maximum_gray_or_black_if_white_only':27-len(w0|wb),'consistent':not bool(conflict)})
    good=[c for c in cases if c['consistent']];assert len(good)==1 and good[0]['maximum_gray_or_black_if_white_only']==9
    OUT[q]={'method':'Independent24 proper cube rotations, visible black/white compatibility and remaining white-union complement.','cases':cases,'consistent_cases':good,'unique_maximum':9}

# Extract the actual unit cells from the segment graph, then cover by2 Ls.
scene=t.json.loads((t.ROOT/'PlaneGeometry/dataset_generator/scenes/Plane206.json').read_text(encoding='utf-8-sig'))
obs=t.json.loads((t.HERE/'Plane206/context.json').read_text())['objects']
def cells(prefix):
    es={frozenset(map(tuple,o['geometry']['points'])) for o in obs if o['id'].startswith(prefix)}
    pts=set().union(*es);xmin=min(p[0] for p in pts);xmax=max(p[0] for p in pts);ymin=min(p[1] for p in pts);ymax=max(p[1] for p in pts);out=set()
    for x in range(int(xmin),int(xmax)):
        for y in range(int(ymin),int(ymax)):
            square=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
            if all(frozenset([square[i],square[(i+1)%4]]) in es for i in range(4)):out.add((x,y))
    return out
source=cells('source_');assert len(source)==4
def norm2(c):
    a=np.array(list(c));a-=a.min(axis=0);return frozenset(map(tuple,a.tolist()))
orients=[]
for r in range(4):
    a=np.array(list(source));m=np.array([[0,-1],[1,0]])
    for _ in range(r):a=a@m.T
    orients.append(norm2(a))
results=[]
for i in range(4):
    target=cells('option'+str(i)+'_');assert len(target)==8;placements=[]
    for shape in orients:
        for a in target:
            for b in shape:
                p={(x+a[0]-b[0],y+a[1]-b[1]) for x,y in shape}
                if p<=target:placements.append(p)
    witness=next(((sorted(a),sorted(target-a)) for a in placements if norm2(target-a) in orients),None)
    assert witness is not None;results.append({'target':sorted(target),'two_L_cover_witness':witness})
OUT['Plane206']={'method':'Independent extraction of unitcells from current exact segment context and all4 rotated L placements.','source_cells':sorted(source),'target_covers':results,'unique_count':4}

t.write(t.HERE/'primary_math_proofs.json',OUT)
print(t.json.dumps({'saved':'primary_math_proofs.json','verified':list(OUT),'correct_answers':{q:v.get('unique_answer',v.get('unique_count',v.get('unique_maximum',v.get('correct_answer')))) for q,v in OUT.items()}}))
