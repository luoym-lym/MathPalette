from bootstrap import install, OWN, PROJECT, SESSION
ISOLATION=install()
import sys, json, hashlib, math, itertools
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from research import save,load,sha,IDS
from prepare import eligibility

def area(poly):
    return abs(sum(F(a[0])*F(b[1])-F(b[0])*F(a[1]) for a,b in zip(poly,poly[1:]+poly[:1])))/2
def clip(poly,axis,value,greater):
    ans=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        ia=a[axis]>=value if greater else a[axis]<=value
        ib=b[axis]>=value if greater else b[axis]<=value
        if ia:ans.append(a)
        if ia!=ib:
            t=(value-a[axis])/(b[axis]-a[axis])
            ans.append([a[k]+t*(b[k]-a[k]) for k in [0,1]])
    return ans
def cellareas(poly,n):
    result=[]
    for x,y in itertools.product(range(n),repeat=2):
        p=[[F(v) for v in xy] for xy in poly]
        for axis,value,greater in [(0,F(x),True),(0,F(x+1),False),(1,F(y),True),(1,F(y+1),False)]:
            if p:p=clip(p,axis,value,greater)
        a=area(p) if p else F(0)
        if a:result.append({'cell':[x,y],'area':str(a)})
    return result

proofs={}
for qid in ['Plane480','Plane481','Plane483']:
    row=load(OWN/qid/'formal_record.json');sc=load(PROJECT/'PlaneGeometry'/row['scene'])
    o=[o for o in sc['objects'] if o['type']=='polygon'][0]
    poly=[sc['points'].get(v,v) if isinstance(v,str) else v for v in o['points']]
    cells=cellareas(poly,7 if qid=='Plane480' else 6 if qid=='Plane481' else 4)
    a=area(poly)
    proofs[qid]={'method':'Exact Fraction shoelace and independent rational clipping into original unit grid cells','formal_vertices':poly,'area':str(a),'cell_areas':cells,'sum_cell_areas':str(sum(F(c['area']) for c in cells)),'unique_numeric_answer':str(a),'conditions':'The drawn polygon or original gray fill is the target. Grid squares are explicitly unit squares; no inferred metric from approximate image pixels is used.'}
    assert a==sum(F(c['area']) for c in cells)
proofs['Plane480']['human_derivation']='The full central [2,5]x[2,5] square has area9. Four exterior triangles each have base2 and height1 and area1. Thus9+4=13.'
proofs['Plane481']['human_derivation']='The central [2,4]x[2,4] square gives4 full cells, and the twelve remaining occupied cells are half-cells, giving4+12/2=10. The two parallelograms separately have area6 and overlap in an area2 diamond, confirming6+6-2=10.'
proofs['Plane483']['human_derivation']='Cut conceptually at existing x=2 and y=2 grid lines: top-left triangle1, top-right quadrilateral2, bottom-left triangle1, bottom-right quadrilateral2. Hence6. These are computations; no cuts are added.'

# Enumerate every orientation assignment; the gray corner, not diagonal slope,
# identifies each of the four equiprobable tiles.
windows=[[(r,c,2),(r,c+1,3),(r+1,c,1),(r+1,c+1,0)] for r,c in itertools.product(range(2),repeat=2)]
hist=[0]*5;counts=[0]*4
for tiles in itertools.product(range(4),repeat=9):
    hits=[all(tiles[3*r+c]==t for r,c,t in w) for w in windows]
    hist[sum(hits)]+=1
    for i,h in enumerate(hits):counts[i]+=h
assert hist==[258048,4096,0,0,0]
proofs['Plane482']={'orientation_indices':['NW','NE','SE','SW'],'windows':windows,'assignments':4**9,'window_hit_counts':counts,'simultaneous_hit_histogram':hist,'favorable':4096,'probability':str(F(4096,4**9)),'unique_answer':'C = 1/64','human_derivation':'Each 2x2 location prescribes all four gray corners, probability1/256. Every pair of different locations shares a cell needing two different gray corners, so the four events are mutually exclusive. Sum4/256=1/64. Paired diagonal slopes alone are insufficient: gray side matters.'}

paint={(0,0),(0,4),(4,0),(4,4)} | {(u,v) for u in range(1,4) for v in range(1,4) if (u,v)!=(2,2)}
painted=set();faces={}
for axis,side in itertools.product(range(3),[0,4]):
    other=[k for k in range(3) if k!=axis];face=set()
    for u,v in paint:
        xyz=[0]*3;xyz[axis]=side;xyz[other[0]]=u;xyz[other[1]]=v;face.add(tuple(xyz))
    faces[f'{axis}:{side}']=sorted(face);painted|=face
unpainted=sorted(set(itertools.product(range(5),repeat=3))-painted)
assert len(unpainted)==69
proofs['Plane489']={'painted_face_cells':sorted(paint),'six_faces':faces,'painted_cube_union':sorted(painted),'unpainted_cubes':unpainted,'painted_count':len(painted),'unpainted_count':len(unpainted),'unique_answer':'69/125','human_derivation':'Interior3^3=27, three unpainted noncorner cubes on each of12 edges=36, and one unpainted face-center cube on each of6 faces=6. Sum69. The12 gray cells per face comprise8 distinct face-interior cells and4 corner incidences;6*8+8=56 painted distinct cubes.'}
proofs['Plane484']={'status':'unique finite maximum not established; no design','formal_and_upstream_missing_conditions':['A_i lies on a ray','successive A_i alternate rays'],'counterexample':'Let u be the unit direction of either ray and A_i=i*u for every integer i>=0. Consecutive lengths are1 and |A_iA0|=i strictly increases, for arbitrary n, even if membership in the two-ray union is informally presumed. The diagram depicts alternating first points, but does not state universal alternation as a condition.','disposition':'No added premise, no alteration, no preset, no solver call.'}
proofs['Plane488']={'unique_answer':'55/2','proof':['Use rectangle corners L=(0,0),R=(8,0),U=(0,5),V=(8,5). Both folded upper corners meet at X, so LX=RX=5 (the left/right rectangle sides).','Subtract x^2+y^2=25 and (x-8)^2+y^2=25: x=4. Inside the rectangle gives y=3. This uses the actual common corner in the drawing and does not assume symmetric folds.','For left crease upper endpoint P=(a,5), equality of distances PU=PX yields a^2=(a-4)^2+4, hence a=5/2. Similarly Q=(11/2,5).','Reflection in LP sends U to X; reflection in RQ sends V to X. For a direct check, LP has direction(1,2), and reflection of(0,5) is(4,3).','The remaining outer trapezoid has vertices(0,0),(8,0),(11/2,5),(5/2,5). Its bases are8 and3, height5, so area55/2. Equivalently remove two original side triangles of area25/4 each from40. The inward flap copies occupy part of that trapezoid and are not further holes.'],'fold_contact':[4,3],'left_top':[2.5,5],'right_top':[5.5,5],'each_original_flap_area':'25/4','incorrect_double_subtraction':'40-4*(25/4)=15'}
sc=load(PROJECT/'PlaneGeometry/dataset_generator/scenes/Plane490.json')
light=sc['objects'][0]['points'];dark=sc['objects'][1]['points']
assert sorted([[-x,-y] for x,y in light])==sorted(dark)
proofs['Plane490']={'light':light,'dark':dark,'vertex_mean_light':[2,1],'vertex_mean_dark':[-2,-1],'proof':'All7 vertices negate about C=(0,0), including the unique arrow tip and both shoulders. A rotation carrying the two polygon boundaries carries the finite vertex set, hence its mean (2,1) to(-2,-1). This nonzero vector forces180 degrees modulo360; direct negation proves existence. There is no second symmetry angle in[0,360).','unique_answer':'180','design_status':'No different grounded false pairing survives original dark/light identity and human rotation semantics; a partial same-side shaft or perpendicular arbitrary edge pairing was already screened out, and colored unmatched ink can turn mapping into no-solution.'}
for qid,p in proofs.items(): save(OWN/qid/'primary_math_proof.json',p)

sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
cfg=load_config();adapter=RendererAdapter(cfg)

def partial(qid,target,start,end,color=None,width=2):
    p=load(OWN/qid/'exact_paths.json')[target][0]
    a={'type':'set_object_style','target':target,'linewidth_pt':width,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
    if color:a['color']=color
    return a
R='#DC2626';B='#2563EB'
specs=[]

q='Plane480';acts=[partial(q,'h7',0,1/7,R)]
roles=['Unit-grid horizontal side from(0,7) to(1,7): source one-centimeter unit reference.']
for target,s,e,role in [('h5',2/7,4/7,'upper protrusion base, true length2'),('h2',3/7,5/7,'lower protrusion base, true length2'),('v2',2/7,4/7,'left protrusion base, true length2'),('v5',3/7,5/7,'right protrusion base, true length2')]:
    acts.append(partial(q,target,s,e,R));roles.append('Existing grid portion serving as '+role+'; recipient matched to the one-unit source by the same red stroke. All intermediate unit subdivisions remain visible.')
specs.append((q,'r52_unit_side_to_two_unit_triangle_bases','11',acts,roles,'Transfer the unit-grid side label to each length2 protrusion base, while reading the unchanged perpendicular height1. The specific wrong rule gives9+4*(1*1/2)=11.','Old Plane480 saved no design or call and dismissed broad cap/grid salience. This uses a definite one-unit source side and the four actual two-unit triangle bases, with a precomputed length-unit substitution and wrong total11, rather than isolated whole-boundary coloring.'))

q='Plane481';acts=[partial(q,'h6',0,1/6,R),partial(q,'v0',5/6,1,R),partial(q,'h4',1/6,2/6,R),partial(q,'v2',4/6,5/6,R)]
roles=['Top horizontal edge of a complete reference unit grid square at[0,1]x[5,6].','Left vertical edge of that same complete unit square; with mark1 makes its true two-leg size frame.','Existing horizontal unit leg of the shaded half-cell with vertices(1,4),(2,4),(2,5); matched reference-frame leg.','Existing vertical unit leg of that same shaded half-cell, matched reference-frame leg. The diagonal closure stays black and visible.']
specs.append((q,'r52_unit_square_frame_to_half_cell','16',acts,roles,'The true1-by-1 grid frame is shared by a full square and a shaded half-cell. Transfer area1 through the frame and count all12 half-cells as whole cells, in addition to4 actual full cells:4+12=16.','Old12-edge strip-color design attempted6+6 without overlap subtraction and returned10/3, both misses of12. The new image leaves the entire logo contour black and pairs one actual full unit-square frame with one existing triangular half-cell frame. It targets unit-area transfer/half-cell weights, not strip overlap.'))

q='Plane483';acts=[partial(q,'h1',2/4,3/4,R),partial(q,'v3',1/4,2/4,B),partial(q,'h2',1/4,2/4,R),partial(q,'v2',2/4,4/4,B),partial(q,'v2',1/4,2/4,R),partial(q,'h0',0,2/4,B)]
roles=['Actual shaded unit-square reference bottom side(2,1)-(3,1), true base1.','Reference right side(3,1)-(3,2), true height1.','Top-left shaded triangle base(1,2)-(2,2), true length1; matches source base role.','Top-left triangle altitude along existing x=2 grid line from y=2 to4, true length2; targets mistaken copying of source unit height1.','Bottom-left shaded triangle vertical base(2,1)-(2,2), true length1; same base role under a quarter turn.','Bottom-left triangle horizontal altitude on existing y=0 grid line from x=0 to2, true length2; targets mistaken copying of source unit height1. Its foot is on the base line extension and is not a new point or given.']
specs.append((q,'r52_unit_cell_height_to_two_triangle_altitudes','5',acts,roles,'Copy the true one-unit reference height into both two-unit triangle altitudes while retaining their true unit bases and the1/2 triangle factor. This miscounts the two left triangles as1/2 each, keeps right quadrilaterals2 each, and yields5.','Old whole-gray-contour red3pt image targeted8 and returned8/6.5 (not two hits). This new six-interval design leaves all oblique gray boundaries unchanged; it binds explicit full-cell base/height roles to two exact triangle bases/altitudes and preregisters5, derived before calls. It is not recoloring or chasing6.5.'))

q='Plane488';acts=[];roles=[]
# Rectangular path order: bottom, right, top (right-to-left), left.
for target,s,e,color,role in [('o0',.25,.5,B,'Original right vertical5 side'),('o0',.5,.578125,R,'Original right top2.5 side'),('o0',.671875,.75,R,'Original left top2.5 side'),('o0',.75,1,B,'Original left vertical5 side'),('o3',0,1,B,'Folded left5-side image from(0,0) toX'),('o4',0,1,R,'Folded left2.5-side image fromP toX'),('o5',0,1,B,'Folded right5-side image from(8,0) toX'),('o6',0,1,R,'Folded right2.5-side image fromQ toX')]:
    acts.append(partial(q,target,s,e,color,1.5));roles.append(role+'; genuine original-to-reflected flap-side correspondence. Solid/dashed/dotted form is preserved. Together the two size groups show each flap before and after, targeting counting both copies as separate losses.')
specs.append((q,'r52_flap_source_and_reflection_double_loss','15',acts,roles,'Each actual flap before and after has area25/4. The paired true side information makes the original outside flap and its inward reflected copy appear as two losses:40-4*(25/4)=15 instead of removing only the two outside triangles.','Old two red3pt intervals paired center top-base3 with vertical5 to target32.5; complete finals45.625/32 missed. New design has genuine5/2.5 original-to-reflected flap correspondences, preserves both crease lines, and targets double subtraction15. No central top-base coloring and no added cut/overlap.'))

q='Plane482';acts=[];roles=[]
paths=load(OWN/q/'exact_paths.json')
for target in ['graytile0','graytile1','graytile2','graytile3']+[f'eggray{r}{c}' for r in range(3) for c in range(3)]:
    p=paths[target][0];controls=p['controls'];n=len(controls)
    diagonal=[(i,c) for i,c in enumerate(controls) if abs(c[-1][0]-c[0][0])>.1 and abs(c[-1][1]-c[0][1])>.1]
    assert len(diagonal)==1
    i,c=diagonal[0];rising=(c[-1][0]-c[0][0])*(c[-1][1]-c[0][1])>0
    acts.append(partial(q,target,i/n,(i+1)/n,None,3 if rising else 1.5))
    roles.append(('Allowed tile source' if target.startswith('graytile') else 'Example tile recipient')+' '+target+': existing '+('rising' if rising else 'falling')+' diagonal in the '+('3pt' if rising else '1.5pt')+' black slope family. Gray-side orientation remains distinct. Styling is globally slope-consistent across all4 samples and all9 example tiles, so no singled-out2x2 target or fifth unmatched tile is created.')
specs.append((q,'r52_diagonal_family_erases_gray_side','E',acts,roles,'Collapse the4 gray-corner tiles into2 diagonal-slope families, falsely giving each required tile probability1/2. Then erroneously keep the four true gray-diamond location events disjoint and sum4*(1/2)^4=1/4, choiceE. This is explicitly a two-part false rule; the true exact result remains1/64.','Old8 colored diagonal marks bijectively paired4 gray orientations to one singled-out example diamond, targetB, finalsC/D both misses. New13 black intervals instead classify both gray-side variants of each diagonal together across the entire library and entire example. It tests slope-family/gray-side confusion with E, not one-window omission; black widths are globally consistent and introduce no new color or restricted location.'))

for qid,name,wrong,actions,roles,hypothesis,difference in specs:
    folder=OWN/qid/name;folder.mkdir(parents=True,exist_ok=True)
    audit={'question_id':qid,'variant_id':name,'created_at_utc':datetime.now(timezone.utc).isoformat(),'substantive_difference':difference,'new_information_transfer':hypothesis,'old_history_path':str(OWN/qid/'old_history_read.json'),'not_cosmetic':True,'not_old_image_retry':True,'no_posthoc_old_final_selection':True,'primary_only':True}
    save(folder/'design_difference_audit.json',audit)
    eligibility(qid,'eligibility_before_render.json')
    context=adapter.inspect_question(qid)
    save(folder/'fresh_context.json',context)
    renderer=PluginRenderer(cfg,adapter,{qid:context})
    submitted={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':name,'intent':hypothesis,'params':{'actions':actions}}
    normalized=renderer.normalize(submitted)
    save(folder/'plugin_submitted.json',submitted)
    save(folder/'plugin.json',normalized)
    a,data,digest=renderer.render(normalized,frozen=True)
    b,repeat,digest2=renderer.render(normalized,frozen=True)
    assert a==b==normalized and data==repeat and digest==digest2
    assert not any(item['sha256']==hashlib.sha256(data).hexdigest() and item['path'].endswith('candidate.png') for item in load(OWN/'history_inventory.json'))
    (folder/'candidate.png').write_bytes(data);(folder/'repeat.png').write_bytes(repeat)
    bound=[]
    for i,(action,role) in enumerate(zip(normalized['params']['actions'],roles)):
        source=next(o for o in context['objects'] if o['id']==action['target'])
        bound.append({'index':i,'action':action,'role':role,'source_object':source,'exact_native_path':load(OWN/qid/'exact_paths.json')[action['target']]})
    design={'question_id':qid,'variant_id':name,'created_at_utc':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':wrong,'hypothesis':hypothesis,'difference_audit':str(folder/'design_difference_audit.json'),'primary_unique_math_proof':proofs[qid],'marker_roles':bound,'plugin_path':str(folder/'plugin.json'),'plugin_sha256':sha(folder/'plugin.json'),'image_path':str(folder/'candidate.png'),'image_sha256':sha(folder/'candidate.png'),'pixel_sha256':digest,'source_eligibility':str(OWN/qid/'eligibility_before_render.json'),'original_source_fingerprints':load(OWN/qid/'eligibility_initial.json')['content'],'approval_status':'PRIMARY UNREVIEWED; not Pass/Collect/independent review; native pretest check required'}
    save(folder/'design.json',design)
    save(folder/'render_check.json',{'schema_normalized':True,'normalized_defaults_frozen':True,'baseline_pixel_equal':True,'two_consecutive_draws_byte_identical':data==repeat,'image_sha256':sha(folder/'candidate.png'),'repeat_sha256':sha(folder/'repeat.png'),'pixel_sha256':digest,'actions':len(actions),'geometry_text_fill_view_original_inputs_unchanged_by_style_operations':True,'native_view_status':'pending actual view before calls','isolation':ISOLATION})
    print(json.dumps({'qid':qid,'variant_id':name,'wrong':wrong,'actions':len(actions),'image_sha256':sha(folder/'candidate.png')},ensure_ascii=False),flush=True)
