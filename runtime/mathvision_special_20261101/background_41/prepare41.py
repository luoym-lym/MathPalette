from env41 import *
import numpy as np
from fractions import Fraction
from math import sqrt
from dataset_tools.mathvision_workbench import png_bytes
from partial_style import object_paths

cfg,ad=adapter()
q=sys.argv[1];assert q in ASSIGNED
e=eligibility(q);assert e['eligible'];meta=ad.inspect_question(q)
assert meta==read(HERE/q/'context.json')
scene=ad.scene(q)
actions=[];roles=[];bindings=[]
def style(oid,a,b,color,role,width=2):
    a=np.array(a,float);b=np.array(b,float);paths=object_paths(scene,oid)
    found=[]
    for path in paths:
        count=len(path['segments'])
        for i,seg in enumerate(path['segments']):
            c=seg['control'];
            if len(c)!=2:continue
            v=c[1]-c[0];den=v@v
            if den<1e-20:continue
            t0=float((a-c[0])@v/den);t1=float((b-c[0])@v/den)
            if min(t0,t1)>=-1e-9 and max(t0,t1)<=1+1e-9 and np.linalg.norm(c[0]+t0*v-a)<1e-8 and np.linalg.norm(c[0]+t1*v-b)<1e-8:
                t0=max(0,min(1,t0));t1=max(0,min(1,t1))
                found.append((path,i,sorted([(i+t0)/count,(i+t1)/count]),c.tolist()))
    assert len(found)==1,(oid,a,b,len(found))
    path,i,(u,v),controls=found[0]
    action={'type':'set_object_style','target':oid,'color':color,'linewidth_pt':width,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':u,'end':v,'wrap':False}}
    bindings.append({'action_index':len(actions),'target':oid,'path_id':path['id'],'path_sha256':path['sha256'],'native_segment_index':i,'all_path_controls':[s['control'].tolist() for s in path['segments']],'selected_source_segment_controls':controls,'actual_selected_endpoints':[a.tolist(),b.tolist()]})
    roles.append({'action_index':len(actions),'role':role,'endpoints':[a.tolist(),b.tolist()]});actions.append(action)
def pt(name,xy,color,role):
    actions.append({'type':'add_point','id':name,'xy':list(xy),'color':color});roles.append({'action_index':len(actions)-1,'role':role,'xy':list(xy)})
def line(name,a,b,color,role):
    actions.append({'type':'add_line','id':name,'endpoints':[list(a),list(b)],'color':color,'linestyle':'dashed'});roles.append({'action_index':len(actions)-1,'role':role,'endpoints':[list(a),list(b)]})
R='#DC2626';B='#2563EB';G='#16A34A';O='#EA580C'
s=read(HERE/q/'source_scene_snapshot.json');p=s['points']
if q=='Plane427':
    variant='r41_isosceles_base_angle_frame';wrong='B'
    mechanism='Bind the two actual equal rotation-radius sides ST and TV as a blue pair and the existing dotted SV as the base. The hypothesized error is returning the isosceles base angle TSV=25 instead of subtracting it from RST=60 to obtain requested RSV=35.'
    style('o0',p['S'],p['T'],B,'First actual equal leg ST of isosceles STV; true rotation-radius information.')
    style('o1',p['V'],p['T'],B,'Second actual equal leg TV, paired to ST without equality ticks.')
    style('o2',p['S'],p['V'],R,'Existing dotted base links the equal legs and shares the target ray SV; original dotted style retained.',1.5)
    proof=['RST and TUV are equilateral and congruent, so TS=TV. In the shown ray order ST,RT,VT at T, angle STV=60+70=130 degrees.','Isosceles STV has angle TSV=(180-130)/2=25. Ray SV lies within RST at S, so RSV=60-25=35, uniquely D.','The marked base-angle frame is a real intermediate triangle. It is not the requested angle and no mark is a new relation symbol. The original 70-degree arc and target arc remain black.']
    difference='Old unit20 saved no PNG or calls, rejecting unsupported new equalities. This design uses only true equal rotation radii and targets the intermediate-versus-requested angle frame, with no new equality/angle relation.'
elif q=='Plane430':
    variant='r41_local_diagonal_L_cost_binding';wrong='E'
    mechanism='Pair each of two permitted single-cell diagonal steps with its two original orthogonal edge components, using red at Start and blue at Finish. Hypothesis: transfer the two-unit L cost to each diagonal, obtaining Manhattan distance 6 instead of 2+2sqrt2. No complete longer route is selected.'
    style('gh2',[0,2],[1,2],R,'Start-cell horizontal unit leg of the L replacement.')
    style('gv1',[1,2],[1,1],R,'Start-cell vertical unit leg of the same L replacement.')
    line('start_cell_diagonal',[0,2],[1,1],R,'Actual permitted diagonal of one unit square, source/receiver counterpart of the red two-edge L.')
    style('gh1',[3,1],[4,1],B,'Finish-cell horizontal unit leg of the second local L.')
    style('gv4',[4,1],[4,0],B,'Finish-cell vertical unit leg of the second local L.')
    line('finish_cell_diagonal',[3,1],[4,0],B,'Actual permitted diagonal of a single unit square, paired with its blue two-edge L.')
    proof=['Let a step have dx,dy in {-1,0,1}. Its Euclidean length is at least dx+(sqrt(2)-1)*(-dy) for a net journey right/down; this linear lower bound holds for every horizontal, vertical and diagonal directed step.','Summing from (0,2) to (4,0) gives 4+2(sqrt2-1)=2+2sqrt2. Two down-right cell diagonals and two horizontal unit edges attain it. Thus the minimum value is uniquely C.','Both dashed additions are expressly permitted cell diagonals. Their red/blue L alternatives cost2, while a diagonal costs sqrt2. Color grouping compares displacement, never declares equal travel lengths. Grid sizes, Start and Finish remain unchanged.']
    difference='Unit20 rejected a highlighted full longer route and illegal multicell chords. New diagram compares two LOCAL legal one-cell diagonal/L substitutions, without marking the connecting route or any option.'
elif q=='Plane436':
    variant='r41_boundary_ordinal_unit_binding';wrong='B'
    mechanism='Compare the three successive original boundary spans on PQ with four successive spans on QR by ordered red/blue/green correspondence; orange identifies the fourth receiver span. A short and long edge are eventually conflated as one unit by ordinal position, yielding3:4 instead of8:9.'
    style('top0',[0,4],[0,3],R,'First PQ span, short; source of first ordinal pair.')
    style('left1',[0,3],[0,1.5],B,'Second PQ span, long; source of second ordinal pair.')
    style('left0',[0,1.5],[0,0],G,'Third PQ span, long; source of false equal-unit third correspondence.')
    style('left0',[0,0],[1,0],R,'First QR span, short; true first local length match.')
    style('mid0',[1,0],[2.5,0],B,'Second QR span, long; true second local length match.')
    style('right00',[2.5,0],[3.5,0],G,'Third QR span, short; receives same ordinal role as a LONG PQ span, the intended mistaken unit.')
    style('right10',[3.5,0],[4.5,0],O,'Fourth QR span has no PQ counterpart; makes the count-based denominator4 explicit without an extra line or label.')
    proof=['Write each small rectangle sides l>s. In the lower block, two vertical long sides span the same height as three stacked short sides:2l=3s.','PQ=s+2l=4s. QR=3l=9s/2 (also three short widths plus one long width). Therefore PQ:QR=8:9, uniquely E.','Counting3 left boundary spans and4 bottom boundary spans as equal units is invalid. Their lengths are (s,l,l) and(s,l,s,s). All12 original tile boundaries remain and no equality ticks are added.']
    difference='Unit20 saved no design and considered only correct length correspondences or arbitrary answer highlighting. This is a new ordered boundary-span map, retaining two true matches followed by one specific short/long role error and an unmatched extra span.'
elif q=='Plane437':
    variant='r41_join_nodes_to_length_intervals';wrong='90'
    mechanism='Pair the actual long side of the left upright tile with the long top edge of the central horizontal tile (blue); mark the four existing join nodes along the upright side (red). Hypothesis: count the four node locations as four short-side intervals, infer lambda1/4 and return90.'
    style('left',[1,0],[1,3],B,'Upright long edge, receiving the three short tile widths; its endpoints and joins are the four red nodes.')
    style('middle2',[1,3],[4,3],B,'Actual same-length horizontal long edge of a congruent tile, source/receiver comparison across orientations.')
    for i,y in enumerate((0,1,2,3)):pt('join_node_'+str(i),[1,y],R,'Existing visible long-edge join at y='+str(y)+'. Four node locations bound only THREE short-side intervals; not a new tile or boundary.')
    proof=['Let small sides be s<l. Three central horizontal tiles stack over the height of either upright tile. Hence l=3s and lambda=s/l=1/3.','360lambda=120 uniquely. Four boundary nodes at y0,1,2,3 bound three gaps, not four. The five congruent rectangles and lambda<1 remain the original conditions.']
    difference='Unit21 rejected an outer3:5 frame distraction with no correspondence. New design uses an inner congruent long-edge pair and existing four-versus-three join incidence, with no outer-frame cue or new subdivision.'
elif q=='Plane438':
    variant='r41_corner_leg_hypotenuse_role_binding';wrong='17753'
    mechanism='Red pairs the given AB with the true equal adjacent octagon side BC. Blue pairs the two perpendicular but unequal legs of the actual NE corner triangle. Hypothesis: promote the leg grouping into a false isosceles assumption, use corner hypotenuse a=43/99, remove total area a^2, and return7952+9801=17753.'
    style('o0',p['A'],p['B'],R,'Given octagon side AB, the numerical source a=43/99.')
    style('o1',p['B'],p['C'],R,'True equal octagon side BC, also hypotenuse of the actual removed NE corner triangle; transfers a to a specific local feature.')
    style('o0',p['B'],[.5,.5],B,'Horizontal NE corner leg of length p; compared with the perpendicular leg, not declared equal.')
    style('o0',[.5,.5],p['C'],B,'Vertical NE corner leg of length q. In the frozen exact geometry p and q are visibly and numerically unequal; same hue is an appearance grouping only.')
    a=Fraction(43,99);pq=((1-a)**2-a*a)/2;area=1-2*pq
    assert pq==Fraction(13,198) and area==Fraction(86,99) and area.numerator+area.denominator==185
    proof=['For two congruent concentric squares, reflection about their orientation bisector swaps the squares and maps AB to the adjacent BC. Quarterturn symmetry gives four congruent removed corner triangles. These are symmetries of the whole arrangement, not new drawn relation symbols.','Let the NE corner triangle legs be p,q and its hypotenuse BC=a=43/99. The complete horizontal unit side consists of q,AB,p, so p+q=1-a=56/99; p^2+q^2=a^2 by Pythagoras.','2pq=(p+q)^2-(p^2+q^2)=(56^2-43^2)/99^2=13/99. Four removed triangle areas total2pq=13/99. Intersection area=86/99 in lowest terms and m+n=185 uniquely.','The wrong isosceles assumption would give one triangle area a^2/4 and all four a^2, hence1-a^2=7952/9801 (coprime) and17753. Actual p≈0.1630983,q≈0.4025583, so p!=q. No label or fill is changed.']
    difference='Unit21 saved no design and rejected whole-square recoloring and a redundant octagon contour. New marks transfer the numerical AB to actual corner hypotenuse BC, and isolate unequal perpendicular leg roles. Only four short existing portions change, not an entire square or new region.'
elif q=='Plane440':
    variant='r41_rotated_side_vertical_span_transfer';wrong='C'
    mechanism='Pair a unit vertical side of the original middle square with its actual clockwise45-degree image, the lower-right oblique side of the diamond. Two red contact corners anchor the actual stopping condition. Hypothesis: transfer the source unit VERTICAL span to the rotated square entire vertical span, combining it with lower-vertex clearance1/2 and returning3/2.'
    style('o2',[2,0],[2,1],B,'Visible original middle/right shared unit vertical edge. It is also the original middle square right edge before clockwise45 rotation.')
    diamond=next(o for o in s['objects'] if o['id']=='o7')['points']
    style('o7',diamond[0],diamond[1],B,'True rotated image of the original unit right edge, now lower-right oblique side. Unit side length survives, its vertical span does not.')
    pt('left_actual_contact',[6,1],R,'Actual upper-right stationary corner contacting the lower-left diamond side, not its leftmost vertex.')
    pt('right_actual_contact',[7,1],R,'Actual upper-left stationary corner contacting the lower-right diamond side; symmetric counterpart of the first contact.')
    proof=['In coordinates relative to gap center, stationary contact corners are(-1/2,1) and(1/2,1). A unit square at45 degrees has halfdiagonal r=sqrt2/2.','Let its bottom vertex height be b. Its lower-left edge is y=b-x, so actual contact(-1/2,1) implies b=1/2. Its top vertex is a full diagonal sqrt2 above bottom:height(B)=1/2+sqrt2, uniquely D.','For b>1/2 there is a gap and for b<1/2 the corner penetrates the diamond, so first contact uniquely fixes b. The unit side has vertical projection sqrt2/2, and is not the entire vertical diagonal.','The physical square can carry the two blue side styles under the actual rotation: the original right side maps exactly to the selected lower-right side. Red points identify stationary contacts only. Thus unlike the Plane242 counter-reading, no competing ink-preservation picture choice is created.']
    difference='Oldv01 marked the entire vertical diagonal with two endpoints and sought B=sqrt2 by omitting bottom clearance. New design adds NO diagonal, compares an actual pre/postrotation side, marks actual contact corners, and predeclares C=3/2 via side-versus-total-span error. Old D with inconsistent value remains a miss for presetB.'
elif q=='Plane442':
    variant='r41_half_side_to_band_projection_binding';wrong='B'
    t=1+sqrt(2)
    mechanism='Red matches one full central-square side to an actual equal octagon sloping side. Blue compares a half central-square side (s/2) with an adjacent band depth(s/sqrt2). Hypothesis: retain corner-triangle areas from their true outer hypotenuse s but transfer s/2 into rectangular band depth, incorrectly computing total4 center areas and probability1/4.'
    style('interior3',[-1,-1],[1,-1],R,'Full central-square side s, source of the true side-length match.')
    style('octagon',[-t,1],[-1,t],R,'Actual octagon sloping side of length s, true match to center side and source for corner-triangle hypotenuse area s^2/4.')
    style('interior2',[-1,1],[0,1],B,'Exactly half of existing central-square top side, length s/2. The endpoint0 is only a style interval endpoint, with no new dot or cut.')
    style('interior0',[-1,1],[-1,t],B,'Adjacent top band depth s/sqrt2 on an actual original edge; compared to the half-side source, not declared equal.')
    proof=['Put octagon side s=2 without loss of scale. Its vertices are(±1,±(1+sqrt2)) and(±(1+sqrt2),±1). The center square has side2 and area4.','Each of four adjacent rectangles has dimensions2 bysqrt2, area2sqrt2. Each of four corner right isosceles triangles has legs sqrt2 and area1. Total area=4+8sqrt2+4=8(1+sqrt2).','Uniform landing probability is area ratio4/[8(1+sqrt2)]=(sqrt2-1)/2, uniquely A. No fill, boundary or probability measure changes.','Erroneously making band depth s/2 instead of s/sqrt2 while retaining true quarter-square corner triangle areas gives total s^2+4(s^2/2)+s^2=4s^2 and B1/4. This is an inconsistent projection transfer, not an alternative legitimate solution.']
    difference='Unit21 rejected a new bounding-square denominator and unsupported contour emphasis. New design has no bounding square or new geometry: one true full-side match feeds corner-area reasoning while a distinct local half-side/depth correspondence targets one specific projection error.'
else:raise ValueError(q)
out=HERE/q/variant
write(out/'design_difference_audit.json',{'question_id':q,'variant_id':variant,'stage':'material_refinement','created_at_utc':now(),'old_history_path':str(HERE/q/'prior_history_inventory.json'),'substantive_difference':difference,'new_mechanism':mechanism,'predeclared_wrong_answer':wrong,'cosmetic_redesign':False,'no_old_observation_relabel':True,'old_evidence_read_only':True})
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Research appearance comparison; no new numerical/geometric givens.','params':{'actions':actions}}
renderer=PluginRenderer(cfg,ad,{q:meta});norm=renderer.normalize(plugin)
write(out/'plugin.json',norm);write(out/'path_fingerprints.json',bindings)
noop=png_bytes(scene);scene.close();assert pixel_hash(noop)==pixel_hash(ad.original_paths[q]);(out/'noop.png').write_bytes(noop)
normalized,png,digest=renderer.render(norm,frozen=True);normalized2,png2,digest2=renderer.render(norm,frozen=True)
assert norm==normalized==normalized2 and png==png2 and digest==digest2
(out/'candidate.png').write_bytes(png)
write(out/'eligibility_before_design.json',e)
design={'question_id':q,'variant_id':variant,'created_at_utc':now(),'expected_wrong_answer':wrong,'correct_answer':ad.records[q]['answer'],'mechanism':mechanism,'substantive_difference':difference,'primary_unique_math_proof':proof,'marker_roles':roles,'human_semantics':'Numerical geometry/measurement question. Colors are comparison groups, not tick marks, angle symbols, new units, fills or constraints. Every original text and count target remains. Specific false relationships are hypotheses of model error; they are not asserted as added givens. Native visual review required before calls.','plugin_path':str(out/'plugin.json'),'image_path':str(out/'candidate.png'),'png_sha256':hashlib.sha256(png).hexdigest(),'pixel_sha256':digest,'plugin_sha256':file_hash(out/'plugin.json'),'context_sha256':file_hash(HERE/q/'context.json'),'path_fingerprints_sha256':file_hash(out/'path_fingerprints.json'),'approval_status':'UNREVIEWED_RESEARCH_ONLY; no Pass/Collect/approval/publication','independent_second_review_performed':False}
write(out/'design.json',design)
write(out/'render_check.json',{'fresh_context_exact':True,'no_op_formal_pixel_equal':True,'plugin_schema_and_actual_normalization_valid':True,'normalized_default_parameters_frozen':True,'normalized_twice_identical':True,'consecutive_complete_redraw_bytes_equal':True,'candidate_sha256':hashlib.sha256(png).hexdigest(),'pixel_sha256':digest,'all_original_frozen_inputs':e['frozen_content'],'exact_path_binding':bindings,'environment':environment_versions(),'source_canvas_dimensions':meta['canvas']['width'],'source_context_sha256':file_hash(HERE/q/'context.json'),'no_geometry_or_fill_or_text_or_visibility_operation':True,'native_view_pending':True})
print(json.dumps({'question_id':q,'variant_id':variant,'expected_wrong_answer':wrong,'actions':len(actions),'render_checks_passed':True,'candidate':str(out/'candidate.png')},ensure_ascii=False),flush=True)
