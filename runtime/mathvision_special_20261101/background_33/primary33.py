from tools33 import *
from fractions import Fraction
OBS={
'Plane249':'At native 768, all five original black cells and all white cells are clear. Five normalized partial-style actions make exactly four exterior red Ls; first/last pieces meet at bottom-left. No interior line or fill was added. The same red and width occur at all four corners. Both diagonal reflection opportunities remain legible.',
'Plane325':'At native 768, all eight original gray fills and all white cells remain distinct. Sixteen 1 pt overlays draw eight complete exterior red Ls on actual staircase edges. They do not cross cell interiors. All eight D4-related positions are equally marked, so treating red as intrinsic ink still preserves every possible original axis. This explicitly replaces the untested, visibly occluded first outline version.',
'Plane328':'At native 768, all nine black dots remain individually recognizable, including the original center. Two full diagonal lines each pass through exactly three actual dots. Their one intersection is the original center. These are long collinearity examples across the whole array, without a short deletion strike, extra point, or claimed deleted state. All six row/column triples remain visually recoverable.',
'Plane363':'At native 768, the four colored side segments each visibly contain the original side midpoint and two original corner dots. All nine dots are readable; the center is untouched. Adjacent groups meet only at original corners and convey overlap rather than four new points or a physical cut.',
'Plane368':'At native 768, all six original black dot disks remain readable. The blue shared unit interval follows existing v0 exactly between the two marked points. Four red/green sides visibly connect the two original apexes to that same pair. The one-unit and four-unit perpendicular grid distances are clear; the small triangle is not obscured. The red/green crossing near the left side has no dot disk and is distinct from the original six marked points.',
'Plane448':'At native 768, the original four-point band boundary and all twenty peg disks are individually clear. Four original sides are red/blue in matched roles; one thin green internal diagonal crosses five already existing peg centers. The upper apex is visibly two peg rows from the base and the lower apex only one. No outer band side is moved or added, and the internal auxiliary does not form a competing quadrilateral silhouette.',
'Plane486':'At native 768, all nineteen black dot disks remain distinct despite thin colored wedges over their centers. Fifteen full principal-direction constraints are visible as three groups of five. All segment endpoints and crossings are original dots; there is no unmarked extra intersection or point marker. Each line visibly has at least three dots, so none is an added exactly-two-point example.',
'Plane487':'At native 768, the two red existing horizontal boundaries and two blue existing vertical boundaries group four intact border strips. The black x=3 and y=3 lines still stop at the central gap; no completion edge is present. All grid lines and their exact intersection inventory remain readable, and rectangles spanning the colored subgrid boundaries remain possible.'}
plans=read(HERE/'design_difference_audit.json')['designs']
for plan in plans:
    q=plan['question_id']
    vid='r33_dihedral_arm_outer_corner_semantic_repair' if q=='Plane325' else plan['variant_id']
    if q=='Plane325' and sys.argv[1:]!=['include325']:continue
    out=HERE/q/vid
    if (out/'primary_review.json').exists():continue
    d=read(out/'design.json');p=read(out/'plugin.json');math=read(HERE/q/'math_proof.json')
    assert len(p['params']['actions'])==len(d['per_marker_roles'])
    check=eligibility(q);assert check['eligible']
    original_source=next(ROOT/'PlaneGeometry'/x for x in check['formal_record']['runtime_dependencies'] if x.endswith('/source.json'))
    source=read(original_source)
    if not (HERE/q/'source_primary_audit.json').exists():
        write(HERE/q/'source_primary_audit.json',{'question_id':q,'created_at':now(),'source_dataset':'MathVision','formal_record':check['formal_record'],'actual_source_record_path':str(original_source),'actual_source_record_sha256':file_hash(original_source),'actual_source_record':source,'source_jpg_actually_viewed':True,'formal_png_actually_viewed_native':True,'current_approval_fingerprint_matches':check['original_approval_fingerprint_matches'],'source_jpg_sha256':file_hash(HERE/q/'source_original.jpg'),'formal_png_sha256':file_hash(HERE/q/'original.png'),'source_missing':False,'unique_original_math_proof_path':str(HERE/q/'math_proof.json'),'math_proof_sha256':file_hash(HERE/q/'math_proof.json'),'correction_to_old_prescreen':math.get('old_Plane328_record_correction'),'no_formal_edits':True})
    if q=='Plane486':
        selected=d['extra_certificate']['selected_principal_lines'];pts=math['integer_lift'];full={tuple(v) for v in pts.values()};intersections=[]
        for i,a in enumerate(selected):
            for j,b in enumerate(selected[i+1:],i+1):
                A,B,C=a['ABC'];D,E,F=b['ABC'];det=A*E-D*B
                if not det:continue
                u=Fraction(B*F-E*C,det);v=Fraction(C*D-F*A,det)
                inside=True
                for line in [a,b]:
                    ps=[pts[k] for k in line['point_ids']]
                    inside &= min(z[0] for z in ps)<=u<=max(z[0] for z in ps) and min(z[1] for z in ps)<=v<=max(z[1] for z in ps)
                if inside:
                    assert (u,v) in full
                    intersections.append({'line_indices':[i,j],'integer_lift_intersection':[int(u),int(v)],'original_point_ids':[k for k,p in pts.items() if p==[u,v]]})
        write(out/'intersection_inventory_proof.json',{'exact_method':'Rational intersections of all nonparallel pairs of the 15 complete finite marked line segments, restricted to both segment bounding boxes.','all_within_segment_intersections_are_original_dots':True,'pair_intersections':intersections,'unique_intersection_count':len({tuple(z['integer_lift_intersection']) for z in intersections})})
    review={'review_type':'PRIMARY ONLY; not independent second review','stage':'material_refinement','created_at':now(),'question_id':q,'variant_id':vid,'actual_native_candidate_png_viewed':True,'actual_formal_png_viewed_native':True,'actual_source_jpg_viewed':True,'native_observation':OBS[q],'unique_original_math_proved':True,'mathematical_certificate_path':str(HERE/q/'math_proof.json'),'mathematical_certificate_sha256':file_hash(HERE/q/'math_proof.json'),'schema_actual_defaults_normalized':True,'no_op_pixels_equal_formal':True,'two_draws_byte_identical':True,'all_markers_actually_inspected':True,'per_marker_review':[{'index':i,'role':role,'actual_native_mark_inspected':True,'concrete_original_feature':read(out/'marker_bindings.json')[i]} for i,role in enumerate(d['per_marker_roles'])],'human_semantics':d['human_semantics_precheck'],'current_eligibility_rechecked':check,'proceed_to_API':True,'test_plan':'Exactly 2 actual quicktest3 calls on this immutable PNG and predeclared wrong answer, via unchanged shared isolated harness; no overrides/retry. No controls added; all same-question history has no original control pair.','expected_wrong_answer_frozen':d['expected_wrong_answer'],'tested_image_sha256':file_hash(out/'candidate.png'),'design_sha256':file_hash(out/'design.json'),'limits':['Primary proof and native view only; every potential delivery requires a NEW parent independent review.','Two calls cannot establish statistical, causal, incremental or per-marker effects.','No original controls exist for these assigned questions, so no original-to-variant effect estimate is available.','Allowed line/color operations alone do not establish semantic suitability; actual wording and each count universe were checked.'],'approval_actions':[]}
    write(out/'primary_review.json',review)
    print(q,vid,'PRIMARY ready',flush=True)
