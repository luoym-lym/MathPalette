from audit import *
from datetime import datetime, timezone
import numpy as np
from PIL import Image

binding=read(OUT/'independent_binding_audit.json')
render=read(OUT/'independent_render_audit.json')
math_audit=read(OUT/'independent_math_audit.json')
eligibility=read(OUT/'current_eligibility.json')
history=read(OUT/'historical_input_comparison.json')
inventory=read(OUT/'Plane391_invocation_inventory.json')
technical=read(OUT/'technical_summary.json')
context=read(CAND/'context.json')
canvas=context['canvas']
matrix=np.asarray(canvas['data_to_pixel'])
original=np.asarray(Image.open(BASE/'original.png').convert('RGBA'))
candidate=np.asarray(Image.open(CAND/'candidate.png').convert('RGBA'))
different=np.any(original!=candidate,axis=2)
ys,xs=np.where(different)
changed_points=np.stack([xs+.5,ys+.5],axis=1)
def pixel(point):
    return (matrix @ np.array([*point,1.0]))[:2]
def distances(points,a,b):
    a,b=pixel(a),pixel(b)
    vector=b-a
    t=np.clip(((points-a)*vector).sum(axis=1)/(vector*vector).sum(),0,1)
    return np.linalg.norm(points-a-t[:,None]*vector,axis=1)
nearest=np.full(len(changed_points),np.inf)
for item in render['paths']:
    for a,b in item['selected_controls']:
        nearest=np.minimum(nearest,distances(changed_points,a,b))
all_nearest=np.full(len(changed_points),np.inf)
for obj in read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane391.json')['objects']:
    frozen=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane391.json')
    vertices=[frozen['points'][p] for p in obj['points']]
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        all_nearest=np.minimum(all_nearest,distances(changed_points,a,b))
outside_selected=nearest>3
unselected_a=original[ys[outside_selected],xs[outside_selected],:3].astype(int)
unselected_b=candidate[ys[outside_selected],xs[outside_selected],:3].astype(int)
unselected_delta=np.abs(unselected_a-unselected_b)
def sampled_rgb(point):
    x,y=pixel(point)
    return {'data_point':point,'nearest_pixel_xy':[round(float(x)),round(float(y))],'rgba':candidate[round(float(y)),round(float(x))].tolist()}
def diagonal_change(a,b):
    a,b=pixel(a),pixel(b)
    v=b-a
    t=((changed_points-a)*v).sum(axis=1)/(v*v).sum()
    d=np.linalg.norm(changed_points-a-t[:,None]*v,axis=1)
    length=np.linalg.norm(v)
    return int(np.sum((d<2)&(t*length>6)&((1-t)*length>6)))
pixel_check={
    'changed_pixel_count':len(xs),
    'changed_pixel_bbox_xyxy':[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())],
    'max_changed_pixel_center_distance_to_selected_original_edges_px':float(nearest.max()),
    'all_pixel_changes_within_3px_of_selected_original_edges':bool(np.all(nearest<=3)),
    'max_changed_pixel_center_distance_to_any_original_edge_px':float(all_nearest.max()),
    'all_pixel_changes_within_3px_of_any_original_edge':bool(np.all(all_nearest<=3)),
    'unselected_outline_changed_pixels':int(np.sum(outside_selected)),
    'unselected_outline_original_and_candidate_achromatic':bool(np.all(unselected_a[:,0]==unselected_a[:,1]) and np.all(unselected_a[:,1]==unselected_a[:,2]) and np.all(unselected_b[:,0]==unselected_b[:,1]) and np.all(unselected_b[:,1]==unselected_b[:,2])),
    'unselected_outline_max_channel_difference':int(unselected_delta.max()) if len(unselected_delta) else 0,
    'unselected_outline_difference_histogram':{str(int(k)):int(n) for k,n in zip(*np.unique(unselected_delta[:,0],return_counts=True))},
    'unselected_outline_interpretation':'Partial path styling reconstructs also the retained black portions of affected outlines. Exact pixel equality outside the five colored intervals is therefore not asserted. The unselected differences are checked against existing geometry and grayscale character separately from source diagonal readability.',
    'source_diagonal_changes_away_from_6px_endpoint_neighborhoods':diagonal_change([0,3],[2,5]),
    'assembled_large_triangle_hypotenuse_changes_away_from_6px_endpoint_neighborhoods':diagonal_change([2,2],[4,0]),
    'actual_overlap_pixel_checks':[sampled_rgb(p) for p in ([1,5],[2.5,2],[3.5,2],[4,1])],
    'no_image_edits_performed':'Arrays read only; no crop, resize, retouch, recoloring, or derived edited image written.'
}
dump('independent_pixel_audit.json',pixel_check)

roles=[
    {
        'action_index':0,'target':'piece0','color':'#DC2626','linewidth_pt':2,
        'selected_existing_edges':[[[0,3],[0,5]],[[0,5],[2,5]]],
        'legal':True,
        'informational_role':'The two full 2cm exterior sides meet at the outer top-left corner of the 4cm2 source square. They also are exactly the legs of the actual 2cm2 large source triangle. They expose the full-square length scale to which the numeral 4 in the question refers.',
        'targeting_assessment':'Purposeful source member of the full-scale red correspondence. The possible mistake is assigning the square area associated with this 2-by-2 span to a triangle, or dropping the triangle factor 1/2. The coloring is also a correct triangle-to-triangle correspondence, so it is not evidence that a solver actually made the intended mistake.',
        'human_clarity':'Both long exterior edges remain fully visible as an open corner; the black diagonal explicitly closes a triangle. This is a recolored full-size boundary corner, not a new inset right-angle/equality symbol or new cut.'
    },
    {
        'action_index':1,'target':'piece7','color':'#DC2626','linewidth_pt':2,
        'selected_existing_edges':[[[2,2],[4,2]],[[4,2],[4,0]]],
        'actually_visible_red_centerlines':[[[2,2],[3,2]],[[4,2],[4,0]]],
        'legal':True,
        'informational_role':'Recipient at the only assembled large triangle. The selected underlying legs are both 2cm and congruent to the source exterior spans. Its long vertical red side and exposed horizontal red shoulder identify the full-scale triangular component.',
        'targeting_assessment':'This offers the precise area-confusion route 4 + 1 + 1 + 4*(1/2) = 8 if the triangle is charged the area of the full square. It is more specific than coloring an entire answer or arbitrary salient object: it connects a source area/length scale to a particular recipient. Its horizontal leg is actually red then blue, which weakens a matching-frame presentation.',
        'human_clarity':'NOT a completely visible red L: the later piece9 blue bottom side overpaints (3,2)-(4,2). The remaining red shoulder and long vertical leg are separated by that blue segment. The full triangle remains unambiguous because its complete horizontal leg and black hypotenuse remain visible. No hidden or new region is needed.'
    },
    {
        'action_index':2,'target':'piece2','color':'#2563EB','linewidth_pt':2,
        'selected_existing_edges':[[[1,3],[2,3]],[[2,3],[2,4]]],
        'legal':True,
        'informational_role':'Source member of the 1cm-by-1cm small-square family. Its two adjacent full unit edges provide a second scale, distinct from the red 2cm square-scale edges.',
        'targeting_assessment':'Useful independent size/area reference for the two actual assembled small squares. Supports the area-accounting route without falsely grouping the four small triangles or adding an area label.',
        'human_clarity':'Open bottom-right corner; the other two existing black square sides and the two flanking source small triangles stay readable. It is an existing region outline, not a new source partition.'
    },
    {
        'action_index':3,'target':'piece5','color':'#2563EB','linewidth_pt':2,
        'selected_existing_edges':[[[1,1],[2,1]],[[2,1],[2,2]]],
        'legal':True,
        'informational_role':'First assembled 1cm2 square, corresponding exactly to the source unit square. Its blue right side is also the existing shared boundary with the neighboring small triangle piece6.',
        'targeting_assessment':'Counts one true small square in the intended subtotal 1+1; it is not a redundant highlight of the large triangle.',
        'human_clarity':'Open bottom-right square corner with full black top/left sides. The blue seam retains the visible separation of piece5 and piece6; it does not create a fresh cut.'
    },
    {
        'action_index':4,'target':'piece9','color':'#2563EB','linewidth_pt':2,
        'selected_existing_edges':[[[3,2],[4,2]],[[4,2],[4,3]]],
        'legal':True,
        'informational_role':'Second assembled 1cm2 square in the same genuine blue size family. Both colored sides are real existing shared edges: its bottom with piece7 and its right with the small triangle piece10.',
        'targeting_assessment':'Supplies the other small square in the subtotal and identifies the top square explicitly. It has a role despite the red/blue overlap. Its bottom visibly wins over part of the red horizontal leg; the report must not describe both colors as simultaneously visible on that segment.',
        'human_clarity':'Open bottom-right square corner, clear full black top/left sides. The rightmost triangle remains a triangle, with a blue vertical seam and black horizontal side/hypotenuse. The shared-edge color conflict is annotation layering, not altered geometry or a new equality.'
    }
]

candidate_finals=['8','8']
control_finals=['12','6.5']
for data,finals in [(binding['candidate'],candidate_finals),(binding['original_control'],control_finals)]:
    for item,final in zip(data['runs'],finals):
        item.update({'entire_raw_assistant_content_manually_read':True,'manual_final_answer_cm2':final,'unambiguous_final':True,'contradictory_final_letter_or_value':False})

harness_context=read(CAND/'harness_context.json')
harness_paths=[ROOT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py',ROOT/'runtime/mathvision_special_20261101/background_09/harness/quicktest3_isolated.py']
harness_checks={rel(p):sha(p) for p in harness_paths}
assert len(set(harness_checks.values()))==1
assert next(iter(harness_checks.values()))==harness_context['copy_sha256']==harness_context['original_sha256']
queue=read(BASE.parent/'second_review_queue.json')
checkpoint=read(BASE.parent/'checkpoint.json')
def references(value):
    if isinstance(value,dict):
        for k,v in value.items():
            if k.endswith('_sha256'):
                yield k,v
            if isinstance(v,(dict,list)):
                yield from references(v)
    elif isinstance(value,list):
        for v in value:yield from references(v)

proof=[
    'Read the actual original 355x360 MathVision JPG and the formal 768x768 redraw. The question says square papers of area 4cm2 are cut as in the first diagram, and SOME pieces form the second shape. It does not say an integer number of complete source squares is used.',
    'Let the original square side be s=sqrt(4)=2cm. Translate its lower-left corner to (0,0). Its drawn diagonal is y=x. The lower-right small square has side t and its upper-left corner is (s-t,t), on that diagonal. Hence t=s-t and t=1cm. This follows from the square and the shown diagonal/corner incidence, not from treating the renderer coordinates or colors as extra givens.',
    'The source is cut into FOUR actual pieces: the triangle above the diagonal has perpendicular legs 2 and 2, area 2cm2; the corner small square has side 1, area 1cm2; the two remaining right isosceles triangles each have legs 1 and 1, area 1/2cm2. Their areas sum to 4. They are not the three source pieces described by candidate run2.',
    'Read the assembly along the actual visible seams: far-left tip piece4 is a unit-leg triangle (1/2); left-arm piece5 is a unit square (1); next piece6 between that square and the long diagonal is a unit-leg triangle (1/2); the central downward triangle piece7 has legs 2 and 2 (2); bottom extension piece8 is a unit-leg triangle (1/2); upper extension piece9 is a unit square (1); far-right tip piece10 is a unit-leg triangle (1/2). Thus there is ONE large triangle, TWO small squares, and FOUR small triangles, seven pieces total.',
    'The six positive-length assembly adjacency relations are piece4-piece5, piece5-piece6, piece6-piece7, piece7-piece8, piece7-piece9, and piece9-piece10. Exact collinear edge intervals and every vertex are recorded in independent_math_audit.json. All 21 pairwise assembled intersection areas and all 6 source intersection areas are zero. Therefore no counting overlap can change the sum.',
    'Assembly area = 1/2+1+1/2+2+1/2+1+1/2 = 6cm2. Equivalently, one complete source set contributes 4 and the spare square plus two small triangles contribute 2. Source-area scale and the fixed seven-piece inventory force 6 uniquely. The variant changes only existing-edge styles, so this same proof applies. A coloring-based inference of equal areas between a full square and a triangle would be an invalid new assumption.',
    'Only after this independent diagram/length/area calculation was established was the stored source answer/solution treated as a cross-check; the source also gives 4+(1/2)*4=6.'
]

objections=[
    {
        'id':'visible_red_frame_description','severity':'nonblocking factual correction','finding':'The frozen primary design/review calls the assembled red mark a congruent two-leg open L frame. The selected path really is congruent, but the native final PNG does not show the full frame in red: piece9 blue bottom covers half of its horizontal side.',
        'evidence':'At data (3.5,2), nearest native pixel is blue #2563EB; at (2.5,2) and (4,1) the pixels are red #DC2626. Exact co-location, draw order, pixel checks, and byte-identical replay establish the result.',
        'impact_and_resolution':'Use the actual description: full-scale source red corner paired to a partially blue-overpainted large-triangle red leg/shoulder. This weakens the complete-frame rhetoric but does not remove the source-to-recipient size correspondence, obscure a boundary, or make any action purposeless. I assess the actual remaining correspondence sufficient for an information-targeted halving/whole-square-area trap. No existing file was corrected or retested.'
    },
    {
        'id':'mechanism_not_established_by_narratives','severity':'scope limitation','finding':'Neither candidate explanation implements the design arithmetic 4+1+1+4*(1/2). Run1 hallucinates a red diagonal, discards a source triangle, invents two assembled large triangles, and then assumes two whole source squares. Run2 hallucinates three source pieces with areas 1,1,2 and an assembly of two triangles plus three squares, explicitly treating color cues as evidence of pieces.',
        'impact_and_resolution':'Both complete numerical finals are nevertheless unambiguous 8cm2, not incidental mentions. Count the two preset hits, but do not claim that the model demonstrated the intended mechanism or that colors are formal mathematical givens.'
    },
    {
        'id':'original_controls_already_wrong','severity':'scope limitation','finding':'The two separate exact-original controls end in 12 and 6.5, both incorrect. They are post-candidate controls and neither is a valid source/assembly decomposition.',
        'impact_and_resolution':'No claim of a correct-to-incorrect flip, increased error rate, statistical gain, or causal attribution is supported. Correct controls and identical narratives were expressly not added as hard gates.'
    }
]

required_reads=[
    ROOT/'runtime/mathvision_special_20261101/Plane391_unit09_independent_review_brief.txt',
    *[ROOT/p for p in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json']],
    BASE.parent/'second_review_queue.json',BASE.parent/'checkpoint.json',
    BASE/'formal_record.json',BASE/'context.json',BASE/'input_fingerprints.json',BASE/'primary_math_audit.json',
    *[CAND/p for p in ['plugin.json','design.json','context.json','path_fingerprints.json','primary_review.json','primary_post_test_review.json','render_check.json','manual_finals_and_binding_audit.json','harness_context.json','eligibility_before_design.json','eligibility_immediately_before_calls.json','api_process.json','api_process_finished.json']],
    ROOT/'runtime/mathvision_special_20261101/background_07/source_preservation_classification_final.json',
    ROOT/'runtime/mathvision_special_20261101/Plane391_pre_review_evidence_check.json'
]
# Read every referenced primary/exact JSON document in full, recording rather than modifying it.
for p in required_reads:
    if p.suffix=='.json':read(p)
read_manifest={rel(p):sha(p) for p in required_reads}
read_manifest.update({rel(p):sha(p) for p in BASE.rglob('*') if p.is_file()})

report={
    'review_schema_version':'1.0.0',
    'question_id':'Plane391',
    'branch':'PlaneGeometry',
    'variant_id':'whole_square_frame_to_triangle',
    'decision':'recommended',
    'reviewer_role':'New independent second reviewer; worked alone with no parent task history, nested agents, delegates, threads, or worktrees.',
    'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Independent recommendation of this exact frozen runtime candidate only. This is not user approval, Special Pass/Collect, collection, publication, or modification of formal data.',
    'verdict_reasons':[
        'Independent original-diagram proof and exact rational polygon audit establish unique area 6cm2 for all seven unchanged pieces.',
        'All five actions pass the actual schema/default/target/path normalizer. Two isolated native replays reproduce the tested candidate PNG byte-for-byte. All image changes stay on existing edges; no mathematical text, piece, cut, region, equality/angle symbol, fill, coordinates, projection, or visibility is changed.',
        'Native-size source and candidate remain readable, including the source diagonal and all four assembled small triangles. Every mark has a concrete source-scale or recipient-square/triangle role.',
        'The actual annotations support a particular whole-square-area/omitted-halving mistake: transfer full-square scale 4 to the large triangular piece, while correctly matching the two unit squares. The blue-over-red shared edge weakens a complete L-frame account and is explicitly corrected here; it does not destroy the remaining targeted correspondence.',
        'The immutable preset 8 predates both complete quicktest3 calls. Both fully read raw finals are 8cm2, with identical PNG/question/request/profile bindings and no evidence of a retry or selected subset for this exact image.',
        'Current authoritative formal MathVision record, original user approval/content fingerprint, no Pass, not Collected, and no special-completion eligibility all verify.'
    ],
    'independent_mathematics':{'correct_answer':'6','unit':'cm2','unique':True,'proof':proof,'all_source_and_assembled_polygons':math_audit['inventory'],'source_total':math_audit['source_total'],'assembly_total':math_audit['assembly_total'],'all_interiors_disjoint':math_audit['all_interiors_disjoint'],'assembly_adjacency':[a for a in math_audit['edge_adjacency'] if int(a['a'][5:])>=4],'exact_audit':rel(OUT/'independent_math_audit.json')},
    'per_marker_audit':roles,
    'targeting_judgment':{
        'sufficiently_information_targeted':True,
        'not_just_arbitrary_salience_reason':'There are two measured geometric families drawn from the actual cutting: red full-size 2cm spans source-to-large-triangle; blue unit-square corners source-to-both true squares. These select the exact quantities in the intended area sum. They are not whole-answer emphasis, random marks, or an unrelated aesthetic grouping.',
        'correct_correspondence_objection':'Red also correctly matches the actual source large triangle to the assembled large triangle. That is true and must not be suppressed. The targeted error is not a false congruence premise: it is substituting the source FULL square area associated with the colored exterior span for half that area, or omitting the 1/2 in the triangle formula. The source black diagonal makes the required correction recoverable.',
        'actual_overpaint_assessment':'The target horizontal 2cm span remains geometrically clear as one red unit plus one blue unit; its entire 2cm vertical leg remains red. A clean congruent monochromatic open L is NOT visible. I regard this as a presentation/description limitation rather than failure of legality, readability, or purposeful information correspondence. Recommendation applies to this actual frozen image, without alteration.',
        'causal_mechanism_proven':False,
        'causal_or_per_marker_ablation_required_as_extra_gate':False
    },
    'human_semantics_and_native_readability':{
        'actual_image_tool_inspections':[
            {'path':'PlaneGeometry/originals/Plane391.jpg','native_dimensions':[355,360]},
            {'path':rel(BASE/'original.png'),'native_dimensions':[768,768]},
            {'path':rel(CAND/'candidate.png'),'native_dimensions':[768,768]},
            {'path':rel(OUT/'replayed_candidate.png'),'native_dimensions':[768,768]}
        ],
        'source_fidelity':'Original JPG and formal redraw have the same four-piece source cutting and same seven-piece assembled topology/orientation. The frozen native and canonical points, objects, labels, view, constraints, and ambiguities compare equal.',
        'source_diagonal':'Continuous black lower-left to upper-right line is plainly visible in both original and candidate. The blue square corner does not erase its central incidence; only tiny colored corner junctions meet it at endpoints.',
        'all_assembled_small_triangles':{
            'piece4':'Far-left triangular tip: black sloped hypotenuse, black horizontal base, existing vertical seam. Clearly separate from the left square.',
            'piece6':'Immediately right of the left square: blue vertical existing square/triangle seam, black horizontal base, black diagonal. Its full triangular region is visible.',
            'piece8':'Bottom extension on the lower half of the long diagonal: black unit bottom, black unit left, black sloping hypotenuse. The red large-triangle vertical leg does not swallow this triangle.',
            'piece10':'Far-right upper tip: blue unit vertical seam with the top square, black unit horizontal base and black sloping hypotenuse. Distinct from the top square.'
        },
        'scale_and_ink':'Uniform 131.720907354px per geometric unit. Unit-leg triangles are about 132px by 132px; the full-square side is about 263px. Selected outlines are 2pt (about 2.78px), against original 1pt (about 1.39px). Both red #DC2626 and blue #2563EB are whitelisted and separable from the remaining black seams.',
        'new_givens_assessment':'No new coordinates, statements, ticks, angle arcs/boxes, equality symbols, labels, lines, or closed partitions are introduced. The open full-edge corners are existing boundary styling. With no legend asserting equality, color is an annotation cue, not an additional equality or area condition. A reader can still solve the original question exactly.',
        'region_and_fill_preservation':'Every original polygon has semantic_fill=false; labels, constraints, distance markers, and ambiguity arrays are empty. White interiors stay white. Pixel comparison confines every changed pixel to the immediate neighborhood of original contours. Splitting/reconstructing affected outlines also produces grayscale raster differences on retained black portions; this is recorded separately and is not represented as exact pixel equality outside the colored intervals.',
        'geometry_projection_visibility':'Points, polygon connectivity, view/aspect/layout, original solid-line visibility and original scale/orientation are preserved. This is a 2D Plane question; no 3D/world/projection alteration occurs.',
        'human_study_performed':False,
        'basis':'Independent manual native-size image inspection plus exact scene/path/render/pixel checks, not a human-subject experiment.'
    },
    'exact_schema_normalization_and_replay':{
        'all_five_actions_set_object_style_only':True,'new_add_point_actions':0,'new_add_line_actions':0,
        'plugin_unchanged_by_actual_normalizer':render['normalized_equals_frozen_plugin'],
        'frozen_true_render_succeeded_twice':True,
        'path_sha256_and_exact_controls_match_saved_context':[{'target':x['target'],'path_id':x['path_id'],'path_sha256':x['current_path_sha256'],'matches_saved_and_current':x['matches_frozen_interval'] and x['matches_saved_path_controls'],'selected_segment_range':x['selected_segment_range']} for x in render['paths']],
        'interval_parameterization':'0..2/3 on the 3-edge triangle paths and 0..1/2 on the 4-edge square paths each select exactly the first two ordered segments. These are original path parameters, not fractions of screen distance. wrap=false throughout.',
        'baseline_matches_formal_and_saved_original_pixels':render['baseline_pixel_matches_formal'] and render['baseline_pixel_matches_saved_original'],
        'twice_replayed_bytes_identical':render['twice_identical_bytes'],
        'replayed_candidate_bytes_equal_tested_png':render['replay_byte_identical_to_tested_candidate'],
        'environment':history['environment_current'],
        'pixel_audit':pixel_check,
        'detailed_render_audit':rel(OUT/'independent_render_audit.json')
    },
    'frozen_identity':{
        'candidate_png_sha256':sha(CAND/'candidate.png'),'candidate_pixel_sha256':render['image_info']['candidate']['pixel_sha256'],
        'plugin_sha256':sha(CAND/'plugin.json'),'design_sha256':sha(CAND/'design.json'),
        'question_record_sha256':read(BASE/'input_fingerprints.json')['question_record_sha256'],
        'source_jpg_sha256':render['image_info']['source']['file_sha256'],'formal_original_png_sha256':render['image_info']['original']['file_sha256'],
        'formal_canonical_scene_sha256':sha(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane391.json'),
        'frozen_native_scene_sha256':sha(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane391/scene.json'),
        'original_approval_content_sha256':eligibility['recomputed_content_sha256'],
        'harness_original_and_copy_hashes':harness_checks,
        'full_evidence_file_hash_manifest':read_manifest
    },
    'complete_raw_final_and_binding_verification':{
        'candidate':binding['candidate'],'separate_original_controls':binding['original_control'],
        'candidate_final_answers_cm2':candidate_finals,'original_control_final_answers_cm2':control_finals,
        'candidate_preset_hits':2,'candidate_completed_calls':2,
        'preset_timing':'Design with preset8 created 2026-11-01T16:03:16.664557+00:00; byte-equal design snapshot bound at 16:05:53.226530; call1 started16:05:53.232490, completed16:06:08.374969; call2 started16:06:08.378182, completed16:06:33.924337. All start/completion records have the same request/image/design hashes.',
        'no_leak_request':'Exact reference payload has only model=mimo-v2.6-flash, stream=false, thinking.type=disabled, the unchanged generic system prompt, one formal question text block, and one data-image URL. The decoded PNG equals candidate.png byte-for-byte. There is no answer, preset8, design description, intent, plugin, source original, or approval supplied as extra solver context. The 4cm2 in the formal question is legitimate problem data.',
        'profile_overrides':'No temperature, seed, max_tokens, max_completion_tokens, reasoning_effort, tool, or timeout field appears in the request. Reviewed harness takes the actual quicktest3 profile and approved MiMo endpoint, uses timeout=None, one POST per run and breaks on any error with no retry. Never imported or invoked the solver harness during this audit.',
        'actual_api_evidence':'Each raw response is a complete assistant message, finish_reason=stop, not truncated, model=mimo-v2.6-flash, reasoning_tokens=0; run HTTP status200/status completed, raw hashes/content/usage agree with the reference parser and run/summary records. No alternate contradictory final letter/value occurs; this is a numeric question.',
        'narrative_limits':'Run1 and run2 have different false decompositions; neither verifies the predeclared exact route. Run1 hallucinates a red diagonal; run2 treats colored boundaries as evidence of extra pieces. These are model errors, not facts supplied by the annotations.',
        'control_limits':'Original controls were separately bound to the exact formal original PNG and same formal question/profile. They conclude12 and6.5, respectively. Their being wrong rules out any claim here of demonstrated error-rate improvement or a correct-original-to-wrong-variant flip.'
    },
    'no_retries_selection_or_fishing_audit':{
        'candidate_exact_png_invocation_count_in_available_runtime_tree':inventory['candidate_exact_image_invocation_count'],
        'exact_candidate_test_directories':1,'candidate_started_files':2,'candidate_complete_response_files':2,
        'all_candidate_calls_counted':True,'no_error_or_incomplete_candidate_artifacts':True,
        'harness_review':'Reviewed run09.py, control09.py, tools09.py and full unmodified quicktest3_isolated.py. Request/image/design are frozen once, checked before each sequential call, saved with exclusive new evidence names; no answer-conditioned branch or retry logic exists.',
        'prior_different_design_disclosed':'The same question previously had right_angle_size_alias, preset5, different plugin/image SHA22b91bd6128febbc7386ac0c9d88ca8143267393100322b8b855369cbd66df08, with finals16 and7. It remains a recorded failure and was not reclassified as this preset8 design. Thus this is exploratory selection across different predeclared hypotheses, not a claim that Plane391 had no earlier exploration.',
        'candidate_no_same_image_retries_no_subset_selection_no_posthoc_preset_rewrite':True,
        'scope_limit':'Available on-disk invocation inventory, raw records, timestamps, hashes, and reviewed harness support this conclusion. No independent provider access log or external timestamp attestation was available. No new solver call was used to manufacture confirmation.'
    },
    'current_authoritative_eligibility':eligibility,
    'concurrent_state_and_drift':{
        'candidate_frozen_inputs_unchanged_from_background09_snapshot':history['all_relevant_inputs_unchanged'],
        'all_3421_historical_input_file_entries_checked':history['checked_files'],
        'changes_since_that_snapshot':history['changes'],
        'diagnostic_progress_metadata':history['progress_metadata'],
        'unit07_context':'Read the earlier source_preservation_classification_final.json: it explicitly reports unrelated workbench changes involving Author-designed Plane492..503, question_bank.jsonl and .runtime/plane_special. That scan cannot identify an author. This review did not restore, rewrite, or attribute any of those files.',
        'workspace_wide_unchanged_claim_made':False,
        'classification':'The remaining_questions/exploration_report hash drift is mutable runtime workflow progress. The frozen candidate/design/plugin/question/geometry/request/raw evidence hashes, original approval and authoritative current Plane391 eligibility independently verify. Progress drift is not treated as frozen evidence corruption.'
    },
    'concrete_objections_and_limitations':objections,
    'additional_limitations':[
        'Only two observed candidate calls, one model/profile and one exact frozen PNG; no population success probability or robustness claim is warranted.',
        'No human experiment, statistical comparison, causal ablation, per-marker ablation, or identical-narrative criterion was imposed as an extra gate.',
        'Native readability is the independent reviewer assessment plus programmatic preservation checks. It is not a guarantee about every display, color-vision condition, or resized thumbnail.',
        'The source renderer scene has empty formal constraint arrays. The independent proof explicitly checks all lengths, right angles, area, adjacency and intersections relevant to this problem; it does not infer those results from a passed generic constraint checker.',
        'Historical protocol_review agent review flags/hashes are kept as historical provenance. Current original user approval was checked from authoritative approvals.json and current content digest; the agent review flags are not substituted for user approval.'
    ],
    'isolation_and_state_preservation':{
        'all_new_files_caches_and_temporary_outputs_inside':str(OUT),
        'isolation':'Set TEMP/TMP/TMPDIR/MPLCONFIGDIR/XDG_CACHE_HOME/PYTHONPYCACHEPREFIX and disable bytecode before project imports. Install a strict assigned-directory Python write audit hook first, then the shared runtime_isolation installer before other project imports. Network connections and subprocess launching are blocked inside all audit Python processes.',
        'no_project_files_modified':True,'no_existing_runtime_evidence_modified':True,
        'no_env_runtime_dot_runtime_git_or_formal_writes':True,
        'no_solver_calls':True,'no_helpers_edited':True,'no_approval_review_or_Pass_Collect_publication_API':True,
        'existing_evidence_and_relevant_source_start_finish_hashes_equal':technical['existing_evidence_and_relevant_sources_unchanged'],
        'new_images':'Two deterministic native replay outputs only, stored here; no edited candidate/source image.',
        'process_policy':'Only synchronous audit Python commands were started; all rendering figures were closed in finally blocks. No server, solver process, nested agent, delegate, thread, worktree, or background helper was launched. Final process query is recorded separately.'
    },
    'supporting_independent_artifacts':{p.name:rel(p) for p in OUT.glob('*.json') if p.name!='independent_review.json'}
}

# Check factual conclusions against the independently produced technical results.
assert technical['eligible'] and technical['approval_matches'] and technical['unique_area']=='6'
assert technical['replay_matches'] and technical['normalization_unchanged']
assert all(binding['candidate']['checks'].values()) and all(binding['original_control']['checks'].values())
assert all(all(r['checks'].values()) for data in binding.values() for r in data['runs'])
assert all(x['matches_frozen_interval'] and x['matches_saved_path_controls'] for x in render['paths'])
assert pixel_check['all_pixel_changes_within_3px_of_any_original_edge']
assert pixel_check['source_diagonal_changes_away_from_6px_endpoint_neighborhoods']==0
assert pixel_check['unselected_outline_original_and_candidate_achromatic']
dump('independent_review.json',report)
print(json.dumps({'decision':report['decision'],'report':rel(OUT/'independent_review.json'),'pixel_audit':pixel_check,'harness_hashes':harness_checks},ensure_ascii=False,indent=2))
