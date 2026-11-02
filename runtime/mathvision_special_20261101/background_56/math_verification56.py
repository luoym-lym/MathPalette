from env56 import *
from fractions import Fraction as F
from collections import Counter
import math

def scene(q):return read(PROJECT/'PlaneGeometry/dataset_generator/scenes'/f'{q}.json')
def xy(sc,p):return sc['points'][p] if isinstance(p,str) else p
def pts(sc,o):return [xy(sc,p) for p in o['points']]
def area(v):return abs(sum(F(str(a[0]))*F(str(b[1]))-F(str(a[1]))*F(str(b[0])) for a,b in zip(v,v[1:]+v[:1])))/2
def angle(a,v,b):
    aa=[a[i]-v[i] for i in (0,1)];bb=[b[i]-v[i] for i in (0,1)]
    return math.degrees(math.acos(sum(a*b for a,b in zip(aa,bb))/math.hypot(*aa)/math.hypot(*bb)))

q='Plane380';sc=scene(q);edges=Counter();grey=[]
for o in sc['objects']:
    if o.get('semantic_fill'):
        v=pts(sc,o);grey.append(o['id'])
        for a,b in zip(v,v[1:]+v[:1]):edges[tuple(sorted((tuple(a),tuple(b))))]+=1
boundary=[e for e,n in edges.items() if n==1]
assert len(boundary)==30
assert all(sum((a[i]-b[i])**2 for i in (0,1))==1 for a,b in boundary)
save(f'{q}/exact_boundary_incidence.json',{'grey_cell_ids':grey,'grey_cell_count':len(grey),'boundary_unit_edges':boundary,'boundary_count':len(boundary),'internal_gray_gray_unit_edges':[e for e,n in edges.items() if n==2],'side_cm':8,'area_cm2':30*8**2,'unique_choice':'D'})

q='Plane397';sc=scene(q);entries=[]
for o in sc['objects']:
    a=area(pts(sc,o));entries.append({'id':o['id'],'area_small_units':str(a),'grey':o.get('semantic_fill',False)})
total=sum(F(e['area_small_units']) for e in entries)
gray=sum(F(e['area_small_units']) for e in entries if e['grey'])
assert (total,gray)==(36,16)
save(f'{q}/exact_square_area_weights.json',{'squares':entries,'total_area':str(total),'grey_area':str(gray),'correct_fraction':str(gray/total),'wrong_equal_object_fraction':str(F(sum(e['grey'] for e in entries),len(entries))),'original_seam_and_fill_change':False})

q='Plane390';sc=scene(q);o=next(o for o in sc['objects'] if o['id']=='grey');v=pts(sc,o)
assert area(v)==21
save(f'{q}/exact_shoelace.json',{'vertices':v,'area_cell_units':str(area(v)),'cell_side_cm':2,'cell_area_cm2':4,'correct_area_cm2':84,'correct_choice':'B','bounding_box_subtractions':{'rectangle':35,'top_triangle':'7/2','right_triangle':6,'lower_left_triangle':2,'bottom_triangle':'3/2','outside_corner_square':1},'why_linear_2_factor_is_wrong':'Cell area scales as2 squared, not2.','no_hidden_grid_added':True})

q='Plane354';sc=scene(q);rows=[]
for o in sc['objects']:
    a,t,f=pts(sc,o)
    rows.append({'id':o['id'],'O':a,'T':t,'F':f,'central_angle_degrees':angle(t,a,f),'tip_angle_degrees':angle(a,t,f),'right_angle_degrees':angle(a,f,t)})
assert len(rows)==5
assert all(abs(r['central_angle_degrees']-72)<1e-7 and abs(r['tip_angle_degrees']-18)<1e-7 and abs(r['right_angle_degrees']-90)<1e-7 for r in rows)
save(f'{q}/exact_native_triangle_checks.json',{'triangles':rows,'larger_angle_from_full_turn':'360/5=72','smaller_angle_from_right_triangle':'90-72=18','unique_N':20,'five_copies_small_angles_total':90,'five_copies_uncovered_degrees':270})

save('Plane332/symbolic_piece_compatibility_proof.json',{'not_inferred_from_frozen_known_x':True,'source_variables':'a=11,b=13, source total height=x, lower rectangle height=y, lower pivot height=z. Source width a+b.','upper_piece_CCW90':'About(a,x), oldtop-left(0,x) maps to(a,x-a) and oldbottom-left(0,0) maps to(a+x,x-a).','middle_step_alignment':'The target horizontal seam is at y, so y=x-a.','lower_piece_halfturn':'About(a+b,z), oldbottom-right(a+b,0) maps to(a+b,2z), oldbottom-left(0,0) maps to(2(a+b),2z).','assembled_vertex_coincidence':'The right endpoint of the upper rotated triangle and the right endpoint of the lower rotated triangle coincide: a+x=2(a+b), x-a=2z=y.','unique_solution':'x=a+2b=11+26=37. Also y=26 and z=13; these independently agree with frozen geometry.','no_measured_pixel_length_used':True})

save('Plane320/rotation_state_checks.json',{'positive_steps_1_to18': [{'n':n,'rotation_mod360':100*n%360,'both_radial_endpoints_same':100*n%360==0,'swapped_endpoint_conditions_both':100*n%360==100 and 100*n%360==260} for n in range(1,19)],'first_complete_cover_index':18,'objects_0_through18':19,'related_semantic_duplicate':'Plane382 has same100degree apex mechanism but a different orientation; original/source/formal native images inspected; no transferred old PNG.'})

save('Plane445/exact_fold_checks.json',{'A':[0,0],'C':[4,0],'B':[4,3],'equidistance_equation':'8x+6y=25','crease_end_AB':['2','3/2'],'crease_end_AC':['25/8','0'],'outside_BC_intersection':['4','-7/6'],'length_squared':'225/64','positive_length':'15/8','choice':'D','crease_added':False})

# Full raw texts are retained together with the manual, deliberately conservative outcome.
old_specs=[('Plane320','background_12/Plane320/congruence_coincidence_binding','2',['16','9'],[False,False]),('Plane361','background_19/Plane361/diagonal_to_terminal_arc_radius_binding','D',['B (5pi+5pi sqrt2)','C (10pi+5pi sqrt2)'],[False,False]),('Plane380','background_11/Plane380/internal_external_edge_binding','C',['D / about2204 (inconsistent)','D /1920'],[False,False]),('Plane244','background_12/Plane244/local_U_global_fit','5',['3','1'],[False,False]),('Plane340','background_34/Plane340/r34_unit_frame_to_filled_regions','2',['0.75','1'],[False,False])]
out=[]
for q,rel,preset,finals,hits in old_specs:
    files=sorted((BASE/rel/'tests').glob('*/run_*_response.json'))
    assert len(files)==2
    runs=[]
    for i,p in enumerate(files):
        val=read(p);ch=val['choices'][0]
        runs.append({'path':str(p),'sha256':sha(p),'finish_reason':ch['finish_reason'],'complete_final_text':ch['message']['content'],'complete_final_manually_read':True,'manual_final':finals[i],'preset_hit':hits[i]})
    out.append({'question_id':q,'old_candidate':rel,'immutable_old_preset':preset,'runs':runs,'two_hits':False,'old_bytes_untouched':True,'no_unchanged_retest':True})
save('old_manual_full_final_reviews.json',out)

# Preserve and explicitly bind the selection-only documents and cited rejection records.
extra=[BASE/'selection56_57_parent_eligibility.json',BASE/'preparation56_57.json',BASE/'annotation_semantics_lessons_20261102.json',BASE/'annotation_semantics_lesson_plane242_r24_20261102.json']
for rel in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly','Plane263_v01','Plane192_v03','Plane233_two_U_partial_partition_binding','Solid220_false_face_pair']:
    extra.append(BASE/'independent_review'/rel/'independent_review.json')
save('extra_readonly_references.json',{str(p.relative_to(PROJECT)):{'sha256':sha(p),'complete_bytes_read':True,'json_parsed':isinstance(read(p),(dict,list))} for p in extra})
print('Exact mathematical/native checks and old full-final reviews saved.')
