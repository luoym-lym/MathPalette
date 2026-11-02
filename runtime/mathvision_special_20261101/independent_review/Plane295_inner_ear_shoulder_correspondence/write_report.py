"""Assemble the second review from independently checked evidence."""
from audit import *

verify()
eligibility = read(OWN / 'current_eligibility.json')
evidence = read(OWN / 'evidence_bindings.json')
render = read(OWN / 'render_audit.json')
pixels = read(OWN / 'pixel_audit.json')
manifest = read(OWN / 'reviewed_evidence_manifest.json')
scene = read(ROOT / 'PlaneGeometry' / FORMAL['scene'])
objects = {o['id']:o for o in scene['objects']}

def local(obj, center):
    result = {k:v for k,v in obj.items() if k not in ('id','points','center')}
    if 'points' in obj:
        result['points'] = (np.array(obj['points']) - center).round(12).tolist()
    if 'center' in obj:
        result['center'] = (np.array(obj['center']) - center).round(12).tolist()
    return result

original_center = np.array(objects['givenhead']['center'])
features = {}
for choice in 'ABCDE':
    center = np.array(objects[choice+'head']['center'])
    suffixes = ('ear-1','ear1','inner-1','inner1','head','nose')
    details = {suffix:{'given':local(objects['given'+suffix],original_center), 'choice':local(objects[choice+suffix],center), 'same_preexisting_feature':local(objects['given'+suffix],original_center)==local(objects[choice+suffix],center)} for suffix in suffixes}
    features[choice] = {'all_preexisting_features_preserved':all(item['same_preexisting_feature'] for item in details.values()), 'features':details, 'added_eye_objects':[local(objects[choice+'eye'+side],center) for side in ('-1','1')], 'common_mouth_arcs':[local(objects[choice+'mouth'+side],center) for side in ('0','1')]}
assert [c for c in features if features[c]['all_preexisting_features_preserved']] == ['B']
assert len({json.dumps(features[c]['common_mouth_arcs'],sort_keys=True) for c in features}) == 1

roles = [
    ('Original left inner-ear shoulder', 'A source-feature anchor; pairs the sloping upper edge with the red flatter C edge.', 'Given white triangle remains visible, but the thick red upper boundary looks like colored cat-ear ink at native size.'),
    ('Choice C left inner-ear shoulder', 'Targets the actual changed upper edge, not the choice label, head as a whole, or unrelated decorative ink.', 'The flatter shoulder and reduced white wedge remain recoverable on careful inspection; color matching dominates the immediate comparison with the given.'),
    ('Original right inner-ear shoulder', 'Blue source-feature anchor; separates right-side correspondence from the left red pair.', 'Original white wedge remains visible. Blue is on the ear boundary itself and has the same drawing-content ambiguity as the left red stroke.'),
    ('Choice C right inner-ear shoulder', 'Blue counterpart on C\'s lowered, flatter shoulder; a purposeful second handed comparison.', 'Flatter edge is still present. The thick blue stroke reduces the small white region and looks like preserved ear color.')
]
markers=[]
for item,(name,role,clarity) in zip(render['markers'],roles):
    markers.append({**item, 'target_feature':name, 'information_role':role, 'schema_legality':'legal', 'legal_operation':'set_object_style only; whitelist red/blue and 2 pt; solid native line type retained; no new point/line/text; p0 is the actual three-edge closed triangle; [1/3,2/3] selects its second edge without wrap.', 'path_binding_exact':item['path_sha256_actual']==item['action']['interval']['path_sha256'], 'endpoint_preservation':'Selected endpoints are the actual frozen triangle vertices, not new/freehand points. All other path controls retain their original geometry.', 'native_size_clarity':clarity, 'semantic_disposition':'Purposeful feature targeting passes. The shared image-level annotation/content ambiguity prevents an unqualified human-semantics pass.', 'new_relation_or_cut_or_region':False})

control_dir = BASE/'background_16/Solid197/control_original/tests/quicktest3_20261101T163310_8019543c7d1e'
control_binding=read(control_dir/'binding.json')
controls=[]
for i in (1,2):
    raw_path=control_dir/f'run_{i:02}_response.json'
    raw=read(raw_path)
    controls.append({'run':i,'raw_response_path':str(raw_path),'raw_sha256':sha(raw_path),'finish_reason':raw['choices'][0]['finish_reason'],'final_manually_read':'450 cm^2','complete_raw_final_manually_read':raw['choices'][0]['message']['content']})

timestamp_paths = {'source_JPG':ROOT/'PlaneGeometry/originals/Plane295.jpg','formal_PNG':ROOT/'PlaneGeometry/image/Plane295.png','formal_dataset':ROOT/'PlaneGeometry/dataset.jsonl','frozen_candidate':CAND/'candidate.png','preset_design':CAND/'design.json'}
file_dates={name:{'path':str(p),'sha256':sha(p),'filesystem_mtime_utc':datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat()} for name,p in timestamp_paths.items()}

report={
    'question_id':'Plane295',
    'variant_id':'inner_ear_shoulder_correspondence',
    'decision':'reject',
    'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
    'role':'New independent second reviewer; worked alone, no nested agent/delegate/thread/worktree and no solver calls.',
    'reason':'The frozen candidate is legally rendered and achieves two explicit predeclared C finals, but fails the requested unambiguous human picture-completion requirement. Its colored ear boundaries can reasonably be read as original drawing content, while B is the only geometry-preserving completion. The image/question gives no way to distinguish those readings.',
    'requirement_disposition':{
        'formal_original_answer_independently_checked':'B under the intended preserve-existing-features completion interpretation; source-wide mouth caveat explicitly recorded below.',
        'source_feature_targeting':'pass',
        'normalized_operation_and_frozen_path_legality':'pass',
        'original_geometry_fill_text_view_preservation':'pass at vector/input level; outline stroke widening visibly occupies some white-boundary pixels as expected.',
        'two_complete_frozen_preset_hits':'pass: C and C on identical tested PNG/request, no contradictory terminal letter/value.',
        'native_readability':'Small but the ear-shape difference remains recoverable; does not justify claiming total geometry loss. The thickness and tiny head size weaken immediate comparison.',
        'human_unique_interpretation':'fail: actual picture-completion semantics conflict with selectively colored outlines.',
        'current_authoritative_eligibility':'pass; no approval/Pass/Collect performed by this review.'
    },
    'independent_unique_answer_proof':{
        'formal_question':FORMAL['question'],
        'source_wording':'Carina has started to draw a cat. <image1> She then adds some eyes. Which picture could show her finished drawing?\n<image2>',
        'method':'Visually compared actual source JPG, formal PNG and native candidate at their actual resolutions. Independently translated the given and each option by their own head centers, then compared all six preexisting anatomical objects, rather than relying on stored answer or primary proof.',
        'invariants':'The oval head is 2.2 by 2; outer ear triangles and white inner ear boundaries, nose type/location/size and handedness must be preserved when eyes are added. All five choices have the same two eye polygons, so eye shapes do not discriminate.',
        'original_local_features':{suffix:local(objects['given'+suffix],original_center) for suffix in ('head','ear-1','ear1','inner-1','inner1','nose')},
        'elimination':{
            'A':'Outer/inner ears and head match, but the downward nose begins 0.2 units above the original nose base and is taller: vertices (-0.2,0.2),(0.2,0.2),(0,-0.4), versus original (-0.2,0),(0.2,0),(0,-0.34). Actual source and native images show the elongated nose; adding eyes cannot cause this.',
            'B':'All six existing objects match after translation, including the two white triangles, the downward small triangular nose and their relative placement. Hence B is the unique option preserving existing anatomical features.',
            'C':'Head, outer ears and nose match, but each white-ear upper corner is lower and slightly inward. Left original (-0.82,1.18) becomes (-0.8,0.99); right original (0.82,1.18) becomes (0.8,0.99), with fixed lower/inner vertices. The source JPG shows a sloping original/B shoulder and a much flatter, lower C shoulder; native pixels confirm it. Eye addition cannot alter those preexisting white regions.',
            'D':'Ear/head features match, but the nose triangle points upward and is shifted: base y=-0.3, apex y=0.04. It does not preserve the original downward nose.',
            'E':'Ear/head features match, but the original triangle has been replaced by a radius-0.2 disk centered at (0,-0.12).'
        },
        'mouth_and_exact_completion_wording':{
            'given_has_mouth':False,
            'all_five_options_have_same_extra_mouth':True,
            'geometry':'Two quarter-circle arcs of radius 0.55, centered locally at (-0.55,-0.34) and (0.55,-0.34), meeting at the nose tip. They are present in the actual source choices and formal choices, absent from the given; no candidate action adds or edits them.',
            'disposition':'This is a preexisting source-wording looseness, not an effect of this variant. If only eyes literally may be added and absolutely nothing else, none of the options is an exact eyes-only extension, since every option also contains mouth arcs. Under the natural finished-drawing reading allowing those common mouth details while preserving existing anatomy, B uniquely survives. I do not silently claim exact eyes-only pixel equivalence or use a mouth difference to eliminate a choice.'
        },
        'all_choice_feature_comparison':features,
        'answer_of_annotated_image_without_annotation_convention':'No unconditional unique answer established. B is recovered only if the viewer knows the red/blue ear edges are comparison annotations to ignore as original drawing content.'
    },
    'actual_visual_inspection':{
        'actual_images_viewed':[str(ROOT/'PlaneGeometry/originals/Plane295.jpg'),str(ROOT/'PlaneGeometry/image/Plane295.png'),str(CAND/'candidate.png')],
        'native_full_image_review':True,
        'diagnostic_native_and_nearest_neighbor_4x_crops_viewed':True,
        'candidate_size':[768,768],
        'source_size':list(Image.open(ROOT/'PlaneGeometry/originals/Plane295.jpg').size),
        'native_face_width_px':pixels['face_width_px'],
        'inner_white_vertex_difference_px':pixels['inner_vertex_height_difference_px'],
        'colored_stroke_width_px':pixels['stroke_width_px'],
        'readability_findings':'The 2 pt strokes are about 2.78 px on heads about 62.46 px wide. The diagnostic corner-height change is about 5.39 px, so it is not erased wholesale. The original sloping red/blue edges and C\'s almost horizontal ones can still be seen, especially in isolated native crops. However, the stroke occupies part of each small white interior, and the immediate visual signal is matching red-left/blue-right cat-ear ink. Magnified crops explain the pixels; they are not evidence of effortless normal-size recognition.',
        'text_fill_and_foreground':'A-E labels, all noses, eye polygons, mouth curves and head outlines are unchanged outside the four ear regions. No new closed contour, separate ink island, crosscut, equality glyph or eye is introduced.',
        'pixel_audit':pixels
    },
    'human_semantics_disposition':{
        'status':'failed for this frozen image',
        'not_a_blanket_color_rule':'Authorized style marks do not automatically become mathematical givens. In a geometry relation problem these strokes could simply identify two edges. This task instead asks whether an unfinished drawing is preserved as it is completed; colored ink on its ear boundaries is itself a plausible drawing detail.',
        'annotation_reading':'A reader informed of the Special comparison convention can ignore color as source content, compare the white ear regions, reject C and recover B.',
        'drawing_content_reading':'An ordinary reader sees red on the given left ear and blue on the right, with matching colors only in C. No legend, separate annotation layer label or request sentence says to exclude these features when checking preservation. Such a reader reasonably judges plain-black B as having lost existing ink. Exact preservation still rejects C for the lower ear shoulders, producing no exact match; coarse feature reading instead favors C.',
        'why_decisive':'The candidate therefore requires an unstated choice of what counts as the given drawing. The raw answers illustrate that ambiguity but do not prove geometry or establish human prevalence. My rejection rests on the actual image and wording, not a model narrative, a numeric mark cap, or a general ban on selective color.',
        'no_new_given_automatically_imputed':True,
        'independent_of_two_hit_success':True
    },
    'per_marker_review':markers,
    'render_and_preservation':{
        'current_normalization_and_path_hashes_rechecked':True,
        'native_no_op_equals_formal_pixels':render['no_op_pixel_equals_formal'],
        'independently_reproduced_candidate_equals_frozen_bytes':render['candidate_reproduced_byte_equal'],
        'current_context_equals_precall_context':render['current_context_identical_to_frozen'],
        'original_fill_artists_preserved':render['fills_preserved'],
        'fill_artist_count':render['fill_artist_count'],
        'original_text_preserved':render['text_preserved'],
        'text_count':render['text_count'],
        'viewport_and_aspect_preserved':render['limits_preserved'],
        'geometry_proof':'Each selected path is the original three-segment triangle. The exact second-edge controls are recorded per marker. Partial styling does not move vertices or change the frozen scene; the rendered byte match confirms the tested artifact follows those operations.',
        'raster_caveat':'All 241 changed pixels lie in the four target ear regions. Partial path reserialization also changes a few boundary/corner antialias pixels; I do not claim every changed pixel is only inside the colored segment or that unchanged fill artists imply unchanged visible white area.',
        'threeD_projection_visibility':'Not applicable: a planar cat illustration with polygon/ellipse layering. No 3D, projection, visibility or hidden-edge input is changed. Frozen 2D draw order and opaque head layering are retained.',
        'schema_historical_binding_limit':'The primary broad frozen-input manifest does not include plugin.schema.json. Current schema is hashed and actual normalization/path validation passes; historical schema identity is not independently timestamp-proven by that manifest.',
        'environment':render['environment']
    },
    'exact_raw_full_final_preset_profile_bindings':evidence,
    'raw_pair_assessment':{
        'two_complete_finals':['C','C'],
        'pre_call_wrong_preset':'C',
        'original_intended_answer':'B',
        'observed_pair_matches_preset':True,
        'run_1_narrative_observation':'Calls the ear strokes red/blue triangles and incorrectly reports a mouth line in the given. The actual given has no mouth. Its terminal C:C is explicit, complete, and not contradicted by another final.',
        'run_2_narrative_observation':'Selects C for retaining red/blue marks. Its final C is explicit and complete. Neither response independently analyzes the diagnostic white-ear geometry.',
        'interpretive_limit':'These are two recorded wrong original-answer finals, not proof of an unambiguous adversarial problem or a demonstrated geometry-confusion mechanism. The color-as-drawing-content narrative aligns with a reasonable competing reading of this particular task.'
    },
    'controls_and_effect_limits':{
        'Plane295_original_controls':{'calls':0,'found':False},
        'no_incremental_effect_established_for_Plane295':True,
        'Solid197_cross_candidate_disclosure':{'relevance':'Disclosed as requested; it is a different question and supplies no Plane295 baseline. The two raw original-control responses were read in full.', 'original_control_image_hash':control_binding['image_sha256'],'control_image_equals_current_formal_Solid197':sha(Path(control_binding['image_path']))==sha(ROOT/'SolidGeometry/image/Solid197.png'),'original_finals':['450','450'],'runs':controls,'implication':'The supplied Solid197 candidate also has 450/450; those controls do not establish incremental effect there. No causal improvement is inferred or transferred to Plane295.'},
        'not_extra_hard_gates':['correct original controls','identical narratives','new human study','statistical significance or gain','causal effect','per-marker ablation'],
        'limits':['Only two observed candidate calls; no rate estimate.','No Plane295 original baseline, human study or causal/per-marker ablation.','A filesystem audit cannot rule out undisclosed external calls; no extra/retry/alternate binding was found in the supplied runtime.']
    },
    'current_authoritative_eligibility':eligibility,
    'timestamps_and_immutable_artifact_hashes':file_dates,
    'timestamp_limit':'Filesystem mtimes are diagnostic, not proof of authorship or tamper resistance. Pre-call order is established by saved design/binding/start/run content and matching immutable bytes; hashes do not independently attest wall-clock history.',
    'reviewed_source_evidence_hashes':manifest,
    'concrete_objections':[
        {'severity':'blocking','code':'PICTURE_CONTENT_VS_COMPARISON_ANNOTATION','finding':'The only-colored-in-given-and-C ear borders supply a reasonable drawing-content reading incompatible with B as the single clear completion. The image provides no annotation convention resolving it.'},
        {'severity':'supporting','code':'SMALL_DIAGNOSTIC_WHITE_EAR_FEATURE','finding':'The 2.78 px colored outlines occupy small white-ear boundaries on 62.46 px heads. The 5.39 px difference remains recoverable, so complete occlusion is not claimed, but native-size clarity is weakened.'},
        {'severity':'source_caveat','code':'EYES_ONLY_WORDING_AND_COMMON_MOUTHS','finding':'The given lacks mouths; every source/formal choice includes the same mouth arcs. Unique B proof applies to preservation of preexisting anatomy under the natural completion reading, not exact literal eyes-only raster addition.'}
    ],
    'workspace_and_process_discipline':{
        'all_new_files_caches_temp_inside_assigned_root':True,
        'strict_write_guard_before_project_imports_rendering':True,
        'shared_runtime_isolation_installed':True,
        'network_and_child_process_execution_blocked_in_audit':True,
        'solver_calls':0,
        'approval_Pass_Collect_publication_APIs_called':False,
        'formal_library_prior_runtime_helper_source_env_git_modified':False,
        'unrelated_concurrent_edits_and_historical_progress_preserved':True,
        'scope_of_hash_conclusion':'Only scoped Plane295 frozen inputs, candidate and evidence are asserted unchanged. Mutable exploration_report/remaining_questions and unrelated workbench changes are diagnostic; no files restored and no authorship attribution or whole-workspace-unchanged claim.',
        'all_own_figures_closed':True,
        'all_own_processes':'Only synchronous audit processes were launched; rendering process completed with exit 0. This final report writer exits normally; no server, background helper or solver was started.'
    },
    'approval_status':'Independent review only. Rejection of this frozen candidate; no user approval, Pass, Collect or publication.'
}
assert all(evidence[k] for k in ('exact_request_body_hash_matches','exact_reconstructed_request_bytes_equal','no_leak_request_exactly_formal_question_single_candidate_and_reference_system','design_snapshot_bytes_identical','preset_before_binding_before_both_calls','decoded_png_equals_frozen_candidate_bytes'))
assert all(r['status']=='completed' and r['finish_reason']=='stop' and not r['truncated'] and r['raw_matches_recorded_hash'] and r['raw_matches_run_answer'] and r['same_request_image_design'] for r in evidence['runs'])
assert all(sha(ROOT/p)==value for p,value in manifest.items()), 'Previously reviewed evidence changed while reviewing'
assert digest(content(ROOT,'PlaneGeometry',FORMAL))==eligibility['current_content_sha256']
save('independent_review.json',report)
out({'decision':report['decision'],'report':str(OWN/'independent_review.json'),'report_sha256':sha(OWN/'independent_review.json'),'size_bytes':(OWN/'independent_review.json').stat().st_size})
