"""Write only this independent review, using existing deterministic audit outputs."""
from pathlib import Path
_audit_path = Path(__file__).resolve().with_name('audit.py')
# Reuse only our guard/bootstrap and utility definitions, before any analysis or
# project import. Do not rerun rendering or overwrite the initial snapshots.
exec(compile(_audit_path.read_text(encoding='utf-8').split('started = now()')[0], str(_audit_path), 'exec'))

from dataset_tools import catalog
from PIL import Image

checks = read(OUT / 'render_and_legality_checks.json')
math_proof = read(OUT / 'independent_math_enumeration.json')
binding_audit = read(OUT / 'raw_binding_audit.json')
start_evidence = read(OUT / 'evidence_manifest_start.json')
start_sources = read(OUT / 'source_hashes_start.json')
preservation = read(OUT / 'source_preservation_checks.json')
candidate = binding_audit['candidate']['invocations'][0]
control = binding_audit['original_control']['invocations'][0]
design = read(CAND / 'design.json')
plugin = read(CAND / 'plugin.json')
record = next(r for r in rows(ROOT / 'PlaneGeometry/dataset.jsonl') if r['id'] == 'Plane324')
scene_path = ROOT / 'PlaneGeometry' / record['scene']
scene = read(scene_path)
native_base = ROOT / 'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane324'
source = read(native_base / 'source.json')
native_scene = read(native_base / 'scene.json')
certificate = read(PARENT / 'exact_integer_math_certificate.json')
triples = {tuple(t) for t in math_proof['all_equilateral_triples']}
sets3 = set(itertools.combinations(range(10), 3))
certificate_witness_checks = []
for item in certificate['three_removal_counterexamples']:
    removed = tuple(item['removed']); survivor = tuple(item['surviving_equilateral'])
    certificate_witness_checks.append(removed in sets3 and survivor in triples and not set(removed).intersection(survivor))
certificate_verified = (len(certificate_witness_checks) == 120 and all(certificate_witness_checks)
    and {tuple(w['removed']) for w in certificate['three_removal_counterexamples']} == sets3
    and certificate['upper_bound_all_four_removal_solutions'] == math_proof['all_minimum_removal_sets']
    and certificate['unique_minimum_answer'] == 4)

groups = [(7,8,9),(0,1,4),(2,3,6)]
group_names = ['top red', 'bottom-left blue', 'bottom-right green']
per_marker = []
for result in checks['per_marker_exact_legality']:
    i = result['action_index']; group = groups[i//3]
    per_marker.append({**result, 'legal':True,
        'targeting':f"Exact existing marked dots dot{result['original_dot_indices'][0]} and dot{result['original_dot_indices'][1]}; no inferred hidden point.",
        'actual_equilateral_group':list(group),'group_name':group_names[i//3],
        'mathematical_correspondence':f"One of the three unit-length sides of actual equilateral triple {group}. That triple is an actual removal constraint in the independent exhaustive enumeration.",
        'information_role':f"Closes or traces this side of the {group_names[i//3]} local constraint; its shared color binds it to the group's other two edges. The three disjoint outlined triples suggest one removal per group, while twelve further real triples remain eligible.",
        'necessity_assessment':'A separate real triangle side, with no repeated edge or decorative framing. Omitting it leaves that group with an open two-edge contour. This supports a useful role, not a claim that the nine-action design is the unique minimal design or that each action has independently proven causal effect.',
        'human_semantics':'Thin connecting side between two clearly visible existing black dot disks. No removed-dot symbol, fill, label, new vertex, crossing at an unmarked point, or restriction of the set of eligible dot triples.',
        'endpoint_binding_qualification':'Stored and independently recaptured snap_points are empty. These endpoints are exact explicit circle-object dot centers, not registered snap API targets. Free finite coordinates are allowed by schema; actual visible dot centers supply their semantic legality.'})

uv = math_proof['uv_coordinates']
def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
crossings = []
for a,b in itertools.combinations(per_marker,2):
    ai,bi=a['original_dot_indices'],b['original_dot_indices']
    if set(ai).intersection(bi): continue
    p,q=[uv[i] for i in ai]; r,s=[uv[i] for i in bi]
    if orient(p,q,r)*orient(p,q,s)<0 and orient(r,s,p)*orient(r,s,q)<0:
        crossings.append([a['id'],b['id']])

manual_notes = [
    'Complete raw answer read independently. It ends **Answer:** 3 and also explicitly says the smallest number is 3. This is an unambiguous numeric target hit. Its seven-triangle inventory is incomplete; it incorrectly sees three bottom-most dots although there are four. Even removing every dot in the bottom row leaves the top triple (7,8,9), directly refuting its construction. Its central-dot and medium-triangle statements are also wrong.',
    'Complete raw answer read independently. Its final sentence says the smallest number is **3**, consistently with its preceding conclusion. It treats the three colored outlines as the only allowed triangles and invents a missing central vertex. Actual dot5 is visible and unchanged. Its proposed deletion of the top, bottom-left and bottom-right dots is {9,0,3}; triple (1,2,5) survives. This is a color-as-given/constraint-subset error, not evidence of an alternative mathematically valid interpretation of the unchanged all-dot question.'
]
final_texts = ['**Answer:** 3', '**Final Answer:**\nThe smallest number of dots that need to be removed is **3**.']
manual_runs=[]
for i, run in enumerate(candidate['runs']):
    manual_runs.append({**run, 'complete_answer_manually_read':True,
        'literal_final_text':final_texts[i], 'explicit_final':'3',
        'numeric_answer_consistent_with_final':True, 'contradictory_final_letter_or_value':False,
        'target_hit':True, 'mathematically_correct':False,
        'reviewer_findings':manual_notes[i]})
control_notes = [
    'Complete raw answer independently read: final Answer: **2**. Removing top row2 (dots7,8) leaves (0,1,4) and many further triangles. Incorrect original control.',
    'Complete raw answer independently read: final sentence concludes minimum 3. It counts only ten triangles, asserts surviving triangles are broken, and gives the invalid deletion {7,5,2}; (0,1,4) and (0,3,9) survive. Incorrect original control.'
]
control_runs = [{**r,'complete_answer_manually_read':True,'explicit_final':str([2,3][i]),
    'reviewer_findings':control_notes[i],'mathematically_correct':False} for i,r in enumerate(control['runs'])]

# Re-read authoritative eligibility now; runtime inventories are diagnostic only.
special = ROOT / 'PlaneGeometry/special_variant'
approval = read(ROOT/'provenance/approvals.json')['approvals']['Plane324']
current_content = catalog.digest(catalog.content(ROOT,'PlaneGeometry',record))
accepted = [r for r in rows(special/'accepted_index.jsonl') if r.get('question_id')=='Plane324']
collected = [r for r in rows(special/'collected_index.jsonl') if r.get('question_id')=='Plane324']
special_files = [rel(p) for p in (special/'Plane324').rglob('*') if p.is_file()] if (special/'Plane324').exists() else []
manifests = sorted(BASE.glob('batch_*/manifest.json'))
manifest_hits = [rel(p) for p in manifests if 'Plane324' in p.read_text(encoding='utf-8-sig')]
state_paths=[ROOT/'PlaneGeometry/dataset.jsonl',ROOT/'provenance/approvals.json',
    special/'accepted_index.jsonl',special/'collected_index.jsonl',
    special/'Plane324/recipes.json',special/'Plane324/collection.json']+manifests
current_eligibility={'checked_at':now(),'formal_MathVision':record['source_dataset']=='MathVision',
    'question_record_sha256':canonical(record),'formal_original_approval':approval,
    'computed_current_approval_content_sha256':current_content,
    'approved_content_matches':current_content==approval['content_sha256'],
    'noPass':not accepted,'notCollected':not collected,
    'noSpecialCompletion':not collected and not special_files,
    'accepted_index_rows':accepted,'collected_index_rows':collected,
    'per_question_special_files':special_files,'published_batch_manifest_hits':manifest_hits,
    'authoritative_state_sha256':{rel(p):fh(p) for p in state_paths}}
current_eligibility['eligible'] = all(current_eligibility[k] for k in ['formal_MathVision','approved_content_matches','noPass','notCollected','noSpecialCompletion']) and not manifest_hits

# Inventory existing test bindings for this formal ID anywhere in the task tree.
found_bindings=[]
for path in BASE.rglob('binding.json'):
    if path.is_relative_to(OUT): continue
    data=read(path)
    if data.get('question_id')=='Plane324':
        found_bindings.append({'path':rel(path),'sha256':fh(path),'image_sha256':data.get('image_sha256'),
            'expected_wrong_answer':data.get('expected_wrong_answer'),'requested_runs':data.get('requested_runs')})
candidate_bindings=[b for b in found_bindings if b['image_sha256']==candidate['binding']['image_sha256']]

key_paths=[ROOT/'AGENTS.md',ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'PlaneGeometry/REDRAW_PROTOCOL.md',
    ROOT/'PlaneGeometry/dataset_generator/protocol.json',ROOT/'PlaneGeometry/workbench/README.md',
    ROOT/'PlaneGeometry/workbench/agent_prompt.md',ROOT/'PlaneGeometry/workbench/plugin.schema.json',
    ROOT/'PlaneGeometry/image/Plane324.png',ROOT/'PlaneGeometry/originals/Plane324.jpg',
    scene_path,ROOT/'PlaneGeometry'/record['script'],native_base/'scene.json',native_base/'source.json',
    PARENT/'original.png',CAND/'candidate.png',CAND/'repeat.png',CAND/'plugin.json',CAND/'design.json',
    CAND/'source_inputs.json',CAND/'fresh_context.json',PARENT/'equilateral_hitting_set_proof.json',
    PARENT/'exact_integer_math_certificate.json',BASE/'runtime_isolation.py',BASE/'harness/quicktest3_isolated.py']
key_paths += [ROOT/'PlaneGeometry'/p for p in record['runtime_dependencies']]
hashes = {rel(p):describe(p) for p in sorted(set(key_paths))}
binding_paths=[ROOT/candidate['invocation']/n for n in ['binding.json','request.json','design_snapshot.json','summary.json','run_01.json','run_02.json','run_01_response.json','run_02_response.json','run_01_started.json','run_02_started.json']]
hashes.update({rel(p):describe(p) for p in binding_paths})

drift_evidence=[{'path':p,'start':v,'end':describe(ROOT/p)} for p,v in start_evidence.items() if describe(ROOT/p)!=v]
drift_sources=[{'path':p,'start_sha256':v,'end_sha256':fh(ROOT/p)} for p,v in start_sources.items() if fh(ROOT/p)!=v]
diagnostic_current={rel(BASE/n):fh(BASE/n) for n in ['remaining_questions.jsonl','exploration_report.json']}
original_img=Image.open(ROOT/'PlaneGeometry/image/Plane324.png')
noop_img=Image.open(OUT/'noop.png')
png_metadata={'formal_original':original_img.info,'independent_noop':noop_img.info}
original_img.close(); noop_img.close()

verification={
    'unique_math_minimum_is_4':math_proof['minimum']==4,
    'fresh_integer_triples_count_15':len(triples)==15,
    'all_120_three_removal_sets_fail':math_proof['enumeration_counts']['3']=={'subsets_checked':120,'hitting_sets':0},
    'exactly_three_four_removal_solutions':len(math_proof['all_minimum_removal_sets'])==3,
    'primary_float_proof_agrees_after_independent_solution':math_proof['primary_triples_match'] and math_proof['primary_minimum_sets_match'],
    'every_primary_integer_certificate_witness_valid':certificate_verified,
    'source_original_jpeg_hash_matches_retained_source_record':fh(ROOT/'PlaneGeometry/originals/Plane324.jpg')==source['source_sha256'],
    'native_and_formal_dot_objects_equal':native_scene['objects']==scene['objects'],
    'native_and_formal_view_equal':native_scene['view']==scene['view'],
    'source_question_matches_formal_after_image_tag_removal':source['record']['question'].replace('\n<image1>','')==record['question'],
    'formal_record_equals_frozen_primary_record':record==read(PARENT/'formal_record.json'),
    'exact_schema_normalization':checks['normalized_exactly_equal'],
    'fresh_actual_context_equals_frozen_context':checks['fresh_context_equal_stored'],
    'no_op_pixel_identity':checks['no_op_pixel_identical_original'],
    'two_rerenders_same_frozen_candidate_bytes':checks['render_1']['byte_identical_candidate'] and checks['render_2']['byte_identical_candidate'] and checks['two_rerenders_byte_equal'],
    'nine_distinct_legal_original_dot_segments':len(per_marker)==9 and len({tuple(sorted(x['original_dot_indices'])) for x in per_marker})==9 and all(x['exact_existing_dot_center_matches'] and x['id_legal_noncolliding'] and x['line_width_pt']==1 and not x['other_dot_on_segment_interior'] for x in per_marker),
    'no_nonendpoint_line_crossings':not crossings,
    'all_pixel_changes_accounted_for_by_thin_added_segments':checks['pixel_difference']['changed_pixels_outside_2_5px_segment_corridors']==0,
    'no_added_black_dot_pixels':checks['pixel_difference']['added_black_pixels']==0,
    'candidate_768_square_opaque':checks['pixel_difference']['opaque'] and checks['pixel_difference']['size']==[768,768],
    'both_candidate_raw_finals_manually_read_as_3':all(x['explicit_final']=='3' and x['target_hit'] and x['complete_answer_manually_read'] for x in manual_runs),
    'all_candidate_raw_request_binding_checks_pass':all(candidate['checks'].values()) and all(all(x['checks'].values()) for x in candidate['runs']),
    'one_frozen_candidate_invocation_exactly_two_completed_calls':len(candidate_bindings)==1 and candidate['checks']['exactly_two_run_records'] and candidate['checks']['two_completed'],
    'preset_design_predates_calls_and_snapshot_identical':design['created_at']<candidate['binding']['created_at'] and design['expected_wrong_answer']=='3' and candidate['checks']['design_snapshot_byte_identical_current'],
    'source_snapshot_hash_bound_to_design':fh(CAND/'source_inputs.json')==design['source_inputs_sha256'],
    'plugin_hash_bound_to_design':fh(CAND/'plugin.json')==design['plugin_sha256'],
    'image_and_pixel_hash_bound_to_design':fh(CAND/'candidate.png')==design['image_sha256'] and checks['render_1']['pixel_sha256']==design['pixel_sha256'],
    'current_authoritative_eligibility':current_eligibility['eligible'],
    'all_3422_historical_frozen_input_hashes_unchanged':not preservation['changed_since_historical_snapshot'] and len(start_sources)==3422,
    'all_existing_audited_evidence_unchanged_through_final_check':not drift_evidence,
    'all_source_hashes_stable_through_final_check':not drift_sources}
assert all(verification.values()), [k for k,v in verification.items() if not v]

report={
    'schema_version':'1.0.0','review_type':'NEW independent second review',
    'question_id':'Plane324','candidate_id':'Plane324/three_corner_triangle_groups',
    'decision':'recommended','reviewed_at_utc':now(),
    'decision_reasons':[
        'Fresh exact enumeration from all ten original dot coordinates proves a unique minimum answer of 4.',
        'Nine normalized legal 1pt segments connect real existing dots and trace three genuine disjoint local equilateral constraints; the all-dot question and removal semantics remain intelligible.',
        'Two complete untruncated quicktest3 mimo-v2.6-flash nonthinking responses explicitly conclude the immutable wrong numeric preset 3 on the exact same frozen PNG and request.',
        'Two independent deterministic replays match the tested PNG byte for byte, sources and evidence are preserved, and current authoritative state remains eligible.'
    ],
    'authorization_and_scope':{
        'review_only':True,'approval_or_Pass':False,'Collect_or_publication':False,
        'solver_calls_made':0,'child_agents_threads_worktrees':0,
        'frozen_sources_helpers_design_images_raw_evidence_modified':False,
        'all_new_files_and_cache_TEMP_within':str(OUT),
        'guards':'Own directory-only write audit hook installed and cache/TEMP redirected before shared runtime_isolation.install and all project/Matplotlib/Pillow analysis imports. Shared guard installed. Network and subprocess launches blocked in review Python.',
        'excluded':'Plane373 and unrelated concurrent workbench work were not adjudicated, restored, or attributed.'},
    'formal_problem':{'record':record,'source_record':source,
        'formal_record_sha256':canonical(record),'source_image_hash_verified':True,
        'intended_point_universe':'The centers of the ten original filled dot disks. Disk circumference positions and line-interior points are not additional dots.'},
    'unique_answer_proof':{
        'independent_method':math_proof['method'],'all_original_dot_coordinates':math_proof['points'],
        'integer_lattice_coordinates':uv,'metric':math_proof['metric'],
        'float_to_lattice_max_error':math_proof['reconstruction_max_error'],
        'all_120_possible_triples_checked':True,'all_15_equilateral_triples':math_proof['all_equilateral_triples'],
        'enumeration_counts':math_proof['enumeration_counts'],
        'lower_bound':'Every deletion set of sizes 0,1,2,3 has a surviving equilateral triple; independent witness file lists all 176 cases, including all 120 size-three sets. Hence at least 4 removals are necessary.',
        'upper_bound':'Each of the three listed four-dot sets intersects all 15 triples, so 4 suffices.',
        'all_minimum_removal_sets':math_proof['all_minimum_removal_sets'],
        'unique_correct_numeric_answer':'4','multiple_optimal_deletion_sets_allowed':True,
        'primary_certificate_rechecked':{'all_120_witnesses_valid_and_distinct_complete':certificate_verified,
            'triangles_and_coordinates_match':math_proof['certificate_triples_match'] and math_proof['certificate_uv_match'],
            'certificate_mtime_after_solver_calls':True,
            'qualification':'The detailed integer certificate was written after the two calls. The earlier proof file and unchanged pretest design already state the same minimum and sets. This review recomputed all results rather than treating any certificate as authority.'},
        'own_proof_artifact':{'path':rel(OUT/'independent_math_enumeration.json'),'sha256':fh(OUT/'independent_math_enumeration.json')}},
    'per_marker_review':per_marker,
    'schema_and_endpoint_findings':{
        'action_types':{'add_line':9,'add_point':0,'set_object_style':0},
        'normalization_exact_no_missing_defaults':checks['normalized_exactly_equal'],
        'styles':'All solid, 1.0pt; red #DC2626, blue #2563EB, green #16A34A; no dash_pattern_pt on solid lines. IDs tri_edge0..tri_edge8 are unique and noncolliding.',
        'snap_points_count':0,'registered_snap_target_claim':False,
        'exact_endpoint_legality':'All 18 endpoints equal explicit original dot-object center coordinate arrays exactly, including full stored floating precision. The centers are the ten actual marked dots in source/original, not unmarked geometric circle centers. The schema permits finite free endpoints in the unchanged viewport. No GUI snap event is claimed.',
        'marker_bindings_original_target_null':'Expected for add_line with endpoint coordinates; it is not a set_object_style target. Independent endpoint-to-dot checks provide the missing semantic binding.'},
    'visual_and_human_semantics':{
        'actual_image_tools_used':[
            {'path':rel(ROOT/'PlaneGeometry/originals/Plane324.jpg'),'view':'native 240x191 source'},
            {'path':rel(ROOT/'PlaneGeometry/image/Plane324.png'),'view':'native 768x768 formal original'},
            {'path':rel(CAND/'candidate.png'),'view':'native 768x768 candidate'},
            {'path':rel(OUT/'rerender_1.png'),'view':'independent native replay, verified byte-identical to candidate'}],
        'normal_size_readability':'All ten large black dot disks remain individually obvious at native 768px. The nine thin (~1.39px) lines are readable; no labels are present, no text is added or hidden, and the isolated center dot5 is unchanged. Original dot diameter is approximately 39px, much thicker than the overlaid strokes.',
        'dot_inventory':{'original':10,'candidate':10,'new_apparent_dots':0,'removed_or_hidden_dots':0,
            'no_new_line_crossings':True,'original_center_dot5_fully_unchanged':True},
        'geometry_fill_text_preservation':'Source/original files, dot centers/radii, viewport, original Circle face/edge parameters and empty labels remain frozen. Only nine overlay lines are added. No polygon fill or original-object style operation occurs. Replay and the bounded pixel difference account for the entire candidate.',
        'overlay_qualification':'The raster dot pixels are not literally unchanged: the high-zorder added strokes overpaint small wedges of nine dot disks. Under a max-RGB<40 black-pixel test, each touched dot retains 91.70% to 95.15% of its original black pixels (threshold-dependent diagnostic). Dot5 retains 100%. This is visible line overlap, not fill recoloring, dot erasure, or changed dot status.',
        'pixel_checks':checks['pixel_difference'],
        'triangle_semantics':'Each colored contour is an actual triangle formed by original dot centers, not a cut, physical partition, filled region, or new fixed component. The question quantifies over any three remaining dots and does not require drawn sides. No same-color, connected-component or inside-region restriction is stated. All twelve unoutlined equilateral triples remain relevant.',
        'human_ambiguity_decision':'No material dot-removal ambiguity found. A human can count ten dot disks and reason over every triple. Reading only the outlined triangles is an erroneous attentional/subset strategy, not an equally valid interpretation of the wording. Removing a dot is hypothetical; no dot has been crossed out or pre-removed.',
        'information_targeting':'The marks correspond to three true vertex-disjoint constraints, each of which really requires at least one deletion. They distract from interleaved and larger constraints. Every added side contributes to one real group; no choice highlighting or arbitrary decoration.',
        'necessity_limit':'Useful per-side roles are established. No marker-count cap, minimum-ink optimality, human study or per-marker statistical ablation is imposed or claimed.'},
    'deterministic_render_verification':{k:v for k,v in checks.items() if k not in ['per_marker_exact_legality','pixel_difference']},
    'noop_PNG_metadata':png_metadata,
    'quicktest_pair':{
        'profile':'quicktest3','model':'mimo-v2.6-flash','thinking':{'type':'disabled'},
        'preset':'3','preset_immutable_as_bound':True,
        'design_created_at':design['created_at'],'binding_created_at':candidate['binding']['created_at'],
        'filesystem_timestamps':{rel(p):start_evidence[rel(p)] for p in [CAND/'candidate.png',CAND/'plugin.json',CAND/'design.json']},
        'requested_and_completed_candidate_calls':2,'candidate_invocation_count':1,
        'no_retry_selection_or_fishing_found_in_preserved_corpus':True,
        'all_Plane324_bindings_found':found_bindings,
        'exact_common_binding':candidate['binding'],
        'binding_sha256':candidate['binding_sha256'],'request_sha256':candidate['request_sha256'],
        'design_snapshot_sha256':candidate['design_snapshot_sha256'],
        'solver_payload_without_base64':candidate['request_without_base64'],
        'no_answers_preset_design_intent_supplied_to_solver':True,
        'exact_common_checks':candidate['checks'],
        'manual_complete_raw_responses':manual_runs,
        'observed_final_pair':['3','3'],'both_wrong_under_independent_proof':True,
        'narrative_agreement_required':False,
        'interpretation':'Two observed completed target hits on this frozen pair. Run1 and run2 make different mathematical/visual errors; both finals consistently specify 3. Incidental numeric mentions, valid reasoning, and equal narratives are not used as substitutes for or additional gates on the explicit finals.'},
    'original_controls':{
        'separate_from_candidate_pair':True,'image_sha256':control['binding']['image_sha256'],
        'binding_sha256':control['binding_sha256'],'request_sha256':control['request_sha256'],
        'all_binding_checks_pass':all(control['checks'].values()) and all(all(r['checks'].values()) for r in control['runs']),
        'final_pair':['2','3'],'both_wrong':True,'complete_raw_manual_readings':control_runs,
        'causal_or_statistical_gain_established':False,
        'correct_original_control_is_not_a_hard_gate':True},
    'current_authoritative_eligibility':current_eligibility,
    'source_and_evidence_preservation':{
        **preservation,'final_checked_at':now(),
        'frozen_input_files_rehashed':len(start_sources),'final_source_drift_during_review':drift_sources,
        'existing_evidence_files_rehashed':len(start_evidence),'final_evidence_drift_during_review':drift_evidence,
        'diagnostic_progress_final':diagnostic_current,
        'runtime_hash_classification':'remaining_questions.jsonl and exploration_report.json changed since the historical snapshots. They are mutable progress diagnostics; this is separate from the unchanged 3422 frozen input hashes and the candidate/request/raw-response evidence. Historical snapshots were preserved.',
        'shared_workspace_scope':'Only the named frozen input and evidence sets are asserted preserved. This is not a claim that the entire shared workspace is unchanged. Concurrent Author-designed/workbench/aggregate work was not restored, altered, or attributed.'},
    'exact_file_fingerprints':hashes,
    'complete_final_verification':{'checked_at':now(),'all_required_checks_pass':all(verification.values()),'checks':verification},
    'concrete_objections':[
        {'severity':'nonblocking factual qualification','issue':'Any statement that all original dot raster pixels or black visibility are literally unchanged is too strong.',
         'resolution':'Original objects/fills/geometry remain frozen, but the nine legal lines visibly overpaint small parts of nine disks. All ten dots remain clear, with no change of removal status. Quantified and disclosed above; no frozen file repaired.'},
        {'severity':'nonblocking binding qualification','issue':'The context has no registered snap_points, and primary add_line original_target fields are null.',
         'resolution':'No GUI snapping is asserted. Every endpoint was independently bound exactly to a real explicit original dot center from the frozen object geometry. Free endpoints are schema-legal and these are visibly marked dots, so the ban on invented or unmarked centers is not implicated.'}],
    'blocking_objections':[],
    'limits':[
        'Exactly two observed candidate calls; two target hits are not a calibrated reliability estimate.',
        'Both original controls are wrong. Causality, statistical gain and superiority over the original are not established.',
        'The two incorrect narratives differ; run2 treats colors/outlined groups as restricting the givens. Those errors are disclosed rather than promoted as correct geometry.',
        'No human study or per-marker ablation; readability/ambiguity conclusions are this independent reviewer\'s inspection and mathematical/renderer audit.',
        'Preserved local requests, hashes, timestamps and raw responses establish the recorded bindings and observed call inventory; they are not externally signed evidence capable of excluding hypothetical unlogged calls elsewhere.',
        'No-op re-render matches every decoded pixel but not original PNG file bytes; the candidate re-renders match both bytes and pixels. PNG metadata is recorded explicitly.',
        'Recommendation is a review outcome only; original/Special approval, Pass, Collect and publication were not performed.'
    ],
    'process_hygiene':{'analysis_process_completed_via_tool_exit':True,'no_children_or_network':True,
        'post_exit_process_audit_path':rel(OUT/'process_audit.json'),
        'note':'All rendering figures were closed in finally blocks. Post-exit process scan verifies zero matching review or background_10 solver processes; unrelated processes are left untouched.'},
    'review_artifacts':{rel(p):fh(p) for p in OUT.glob('*.json') if p.name!='independent_review.json'}
}
save('independent_review.json',report)
save('final_evidence_manifest.json',{p:describe(ROOT/p) for p in start_evidence})
print(json.dumps({'decision':report['decision'],'report':str(OUT/'independent_review.json'),
    'report_sha256':fh(OUT/'independent_review.json'),'all_checks_pass':all(verification.values()),
    'input_files_preserved':len(start_sources),'evidence_files_preserved':len(start_evidence)},indent=2))
