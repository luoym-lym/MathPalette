from audit import *

ev=read(OUT/'evidence_verification.json')
math=read(OUT/'math_verification.json')
img=read(OUT/'image_verification.json')
render=read(OUT/'render_verification.json')
contour=read(OUT/'contour_preservation_conclusion.json')
elig=read(OUT/'eligibility_current.json')
design=read(C/'design.json')
binding=read(T/'binding.json')
checks=read(OUT/'input_hash_comparisons.json')
unchanged={p:sha(ROOT/p)==h for p,h in read(OUT/'existing_evidence_start_hashes.json').items()}
assert all(unchanged.values())
assert all(sha(ROOT/p)==d['current_sha256'] for p,d in checks.items())
assert elig['eligible'] and render['exact_frozen_candidate_byte_match']
assert contour['all_76_original_edges_represented_once'] and not contour['unmatched_added_segments']
assert math['unique_halfturn_match']==['C']

def stamp(p):
    return {'path':str(p.relative_to(ROOT)),'sha256':sha(p),'size_bytes':p.stat().st_size,'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat()}

state_final={str(p.relative_to(ROOT)):{'sha256':sha(p) if p.exists() else None,'Plane259_rows':[r for r in rows(p) if r.get('question_id',r.get('id'))=='Plane259'] if p.suffix=='.jsonl' else None} for p in [ROOT/'PlaneGeometry/dataset.jsonl',ROOT/'provenance/approvals.json',ROOT/'PlaneGeometry/special_variant/accepted_index.jsonl',ROOT/'PlaneGeometry/special_variant/collected_index.jsonl',ROOT/'PlaneGeometry/special_variant/Plane259/recipes.json',ROOT/'PlaneGeometry/special_variant/Plane259/collection.json']}
assert all(v['sha256']==elig['authoritative'][k]['sha256'] for k,v in state_final.items())
write(OUT/'authoritative_state_final.json',{'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'same_as_initial_current_eligibility':True,'state':state_final})

roles=[
    ('Input 5 long top cap','Identifies the actual horizontal cap as the first directed feature, rather than coloring the complete input numeral.','Without this source mark, the red target edge loses its feature correspondence. It is an information role, not a mathematical prerequisite or empirically established causal necessity.'),
    ('Input 5 left upright','Identifies the second, perpendicular feature and its order around the original cap/stem corner. Together with the cap it determines orientation and distinguishes a quarter-turn from single reflections.','Without it the blue target mark is unpaired and the two-feature orientation comparison is lost. No per-marker ablation was performed.'),
    ('D right vertical edge, the quarter-turned cap','Pairs the input cap with its exact clockwise-quarter-turned copy in D. The actual horizontal-to-vertical change is relevant to the wrong transformation being suggested.','Without this target mark the red source feature has no candidate endpoint. This is feature-specific salience, not whole-choice highlighting.'),
    ('D upper horizontal edge, the quarter-turned upright','Pairs the input upright with its exact clockwise-quarter-turned copy, completing the ordered two-feature comparison. This is the companion of the same wrong transformation.','Without it the second source feature has no candidate endpoint and the two nonparallel feature mapping is incomplete. No claim of minimality or causal necessity.')
]
markers=[]
for i,(title,role,necessity) in enumerate(roles):
    a=read(C/'plugin.json')['params']['actions'][i];live=render['live_path_checks'][i]
    markers.append({'action_index':i,'feature':title,'action':a,'exact_controls':live['controls'],'visible_length_px_at_768':live['length_px'],'informational_role':role,'necessity_assessment':necessity,'legality':'Permitted set_object_style on one original p0 segment; correct live path hash and exact normalized endpoints; wrap=false. Red/blue are whitelisted and 2 pt is whitelisted. Solid linestyle is inherited. No text, fill, coordinate, mirror, or answer label change.','normal_size_assessment':'A continuous, discernible colored boundary stroke about 2.78 pixels wide at 100 dpi. At the shared cap/stem corner the colors meet without masking the glyph structure; the black numeral body remains recognizable.','legal':True,'informative':True})

runs=[]
for i,r in enumerate(ev['runs'],start=1):
    record=r['full_record']
    raw=read(T/f'run_{i:02d}_response.json')
    narrative=(
        'Misplaces the final worked 4 in the bottom-left; swaps the input marker colors (actual cap red, upright blue); falsely claims a red marker on C and calls D upside down. It also mentions the correct 180-degree composition but selects D based on mistaken shape/color readings.' if i==1 else
        'Mislabels the first reflection axis, misidentifies B/C, and says the red edge on D is a bottom horizontal bar, whereas it is the right vertical edge. It states the correct 180-degree transformation in prose but misreads which option has it.'
    )
    runs.append({'run_index':i,'full_record_path':str((T/f'run_{i:02d}.json').relative_to(ROOT)),'full_record_sha256':r['run_file_sha256'],'raw_response_path':str((T/f'run_{i:02d}_response.json').relative_to(ROOT)),'raw_response_sha256':r['raw_response_sha256'],'response_id':raw['id'],'started_at_utc':record['started_at'],'finished_at_utc':record['finished_at'],'provider_created_at_utc':r['raw_response_created_utc'],'http_status':record['http_status'],'finish_reason':record['finish_reason'],'model':record['response_model'],'truncated':record['truncated'],'reasoning_tokens':raw['usage']['completion_tokens_details']['reasoning_tokens'],'full_content_manually_read':True,'complete_raw_content':raw['choices'][0]['message']['content'],'actual_final_excerpt':'**Final Answer:**\nThe correct option is **D**.' if i==1 else '**Final Answer:** D','manual_final_letter':'D','matches_predeclared_wrong_answer':True,'contradictory_final_letter_or_value':False,'final_consistency_assessment':'The final option letter is explicit D, with no competing terminal letter or numeric answer. The erroneous prose description of D as a half-turn is a narrative mismatch; it is not an alternative terminal letter/value.','narrative_objections':narrative,'all_raw_record_summary_bindings_verified':all(v for k,v in r.items() if isinstance(v,bool))})

frozen_stamps=[stamp(p) for p in [ROOT/'PlaneGeometry/originals/Plane259.jpg',ROOT/'PlaneGeometry/image/Plane259.png',ROOT/'PlaneGeometry/dataset_generator/scenes/Plane259.json',P/'formal_record.json',P/'input_fingerprints.json',P/'context.json',P/'source_scene_snapshot.json',C/'candidate.png',C/'plugin.json',C/'design.json',C/'path_fingerprints.json',C/'render_check.json',T/'request.json',T/'binding.json',T/'design_snapshot.json',ROOT/'PlaneGeometry/workbench/quick_test.py']]

report={
    'question_id':'Plane259','branch':'PlaneGeometry','variant_id':'cap_stem_quarterturn_binding','decision':'recommended',
    'reviewer':{'role':'New independent second reviewer','independence':'Read assignment and protocols, inspected actual source/formal/candidate images, independently derived the transformations and recomputed geometry/evidence checks. Did not accept primary assertions as proof. No parent research history, subagents, delegates, threads, or worktrees.','reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},
    'scope_and_authority':'Independent recommendation only. No Pass, Collect, publication, formal question review API, or new solver call. Existing files, formal state, helpers, .env, .runtime and .git were not edited.',
    'recommendation_reasons':[
        'Original mathematics has the unique answer C: reflect in the vertical line and then the horizontal line, giving (x,y) -> (-x,-y). All five actual glyphs independently checked.',
        'All four legal partial-style marks identify the original cap/stem features and their exact clockwise-quarter-turned copies in D. Normal-size glyphs, mirrors, counters, labels and question mark remain legible; no new cut or region was introduced.',
        'The two complete raw quicktest3 MiMo-V2.6-Flash nonthinking responses explicitly conclude D/D against the immutable predeclared D, on the identical frozen PNG. Request, record, snapshot, response and live path bindings verify.',
        'Formal MathVision approval is valid now, with no Pass, Collect, special completion or prior batch delivery for Plane259. Exact frozen replay succeeds.'
    ],
    'protocols_read_in_full':['runtime/mathvision_special_20261101/Plane259_unit07_independent_review_brief.txt','AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json'],
    'original_mathematics':{
        'formal_question':elig['formal_record']['question'],'source_dataset':'MathVision','source_key':'test:779','unique_correct_answer':'C',
        'independent_proof':'The source JPG and formal PNG show an upright 4 in the upper-left, its left/right reflection in the upper-right, and the reflection of that second glyph across the horizontal line into the lower-right. Each white counter follows the same operations. Relative to the crossing, the two maps are V(x,y)=(-x,y) and H(x,y)=(x,-y); H(V(x,y))=(-x,-y). Thus the input 5 must be rotated by 180 degrees. Its horizontal top cap becomes a bottom cap, its left upright becomes a right upright, and its curved lower lobe becomes an upper lobe. Only actual choice C has all these features. This is derived without using the stored answer; the stored answer C agrees afterward.',
        'actual_option_comparison':{
            'A':'Vertical-line reflection of the input 5: top cap stays on top, lateral orientation reverses. One reflection, not the required two.',
            'B':'Horizontal-line reflection only: cap moves to bottom but lateral handedness differs from C. One reflection.',
            'C':'Half-turn of the input 5: bottom cap and right upright with matching upper lobe. Unique correct glyph.',
            'D':'Clockwise 90-degree rotation of the input 5: cap becomes right vertical edge and upright becomes upper horizontal edge. Wrong quarter-turn.',
            'E':'Reflection in a descending diagonal in centered coordinates (matrix [[0,-1],[-1,0]]), with a vertical cap on the other side. It is not a half-turn; independent full-vertex comparison rules it out.'
        },
        'numeric_verification':math,
        'geometry_context_authentication':'The current live renderer context is exactly equal to the frozen context used for the vertex comparison; formal scene bytes equal the saved scene snapshot. Both outlines and white counters of the worked 4 verify both reflections exactly.',
        'three_dimensional_projection_visibility':'Not applicable: this is a planar glyph reflection problem. Existing viewport and original visibility are preserved; no 3D or projection change exists.'
    },
    'per_marker_review':markers,
    'actual_image_human_semantics':{
        'images_actually_viewed':[str((ROOT/'PlaneGeometry/originals/Plane259.jpg').resolve()),str((ROOT/'PlaneGeometry/image/Plane259.png').resolve()),str((C/'candidate.png').resolve())],
        'tool':'view_image on the actual source JPG, actual formal PNG and actual frozen candidate PNG; native 768-pixel candidate inspection.',
        'source_formal_correspondence':'All three worked 4 orientations, both mirror crosses, the upright input 5, question-mark field, and five choice orientations agree. Original source wrapper text <image1>/<image2> and blue separator are source packaging, not mathematical conditions.',
        'normal_size_readability':'All five numeral silhouettes, worked 4 white counters, A)-E) labels, and the question mark are clearly readable at 768x768. The input cap/stem marks are about 47.75/41.91 px long; D counterparts are about 42.45/37.25 px. The 2 pt strokes are visible and confined to the original boundary. No text or mirror overlap is visible.',
        'ink_contours_regions':'The only new visible pixels are in two small cap/stem corner neighborhoods of the input and D (562 RGBA pixel differences total). The marks follow four existing open edge portions. They create no new interior line, closed contour, cutting boundary, partition, vertex symbol, mirror, or arrow. Existing closed glyph outlines are original and complete. This has no Plane233-style new fixed partition conflict.',
        'color_as_given_assessment':'The wording asks for the number 5 after the same reflections; it does not require physical transport or preservation of annotation ink. Thin selective colored boundary strokes on the existing black digit are recognizable comparison annotations. They do suggest an incorrect source-to-D correspondence, which a reader can reject using the untouched worked 4. I do not treat this permitted annotation as a new given. Treating the colors as obligatory physical ink would demand red at the bottom and blue at the right on the half-turn glyph, which the choices do not provide; that reading is an annotation-related distraction, not a second valid geometric answer.',
        'information_targeting':'D is salient, but each colored edge corresponds exactly to a specific source edge under a wrong clockwise quarter-turn. Both nonparallel features participate. No full option, answer letter or arbitrary unrelated contour is highlighted. Four actions are concise for this two-feature pairing; no numerical mark cap or claim of globally minimal markers is imposed.',
        'assessment':'Human-readable with unique original geometric answer under the authorized annotation semantics. This is reviewer judgment from actual images, not a human study.',
        'image_difference_verification':img,
        'exact_contour_preservation':{k:v for k,v in contour.items() if k not in ('new_outline_patches','edge_coverage_counts')}
    },
    'observed_two_hit_evidence':{
        'predeclared_wrong_answer':'D','independent_correct_answer':'C','actual_completed_final_letters':['D','D'],'two_hit_requirement_satisfied':True,
        'design_declared_at_utc':design['created_at'],'binding_created_at_utc':binding['created_at'],'ordering':'Design declares D at 15:09:21.993564 UTC, before the binding at 15:10:10.223420 and first started record at 15:10:10.226364. Design snapshot bytes equal current design; both run records bind the identical design hash.',
        'model':'mimo-v2.6-flash','thinking':{'type':'disabled'},'request_contents':'Exactly the fixed neutral solver system message, the exact formal question, and the base64 candidate PNG. No preset, correct answer, design, plugin, annotation intent, original-control image or explanation was sent. No max_tokens or max_completion_tokens.',
        'same_frozen_png_sha256':binding['image_sha256'],'same_request_sha256':binding['request_body_sha256'],'same_design_sha256':binding['design_sha256'],
        'complete_responses':runs,
        'calls_and_selection_audit':'The candidate has exactly one test directory, two started records, two completed run records, and two complete raw responses, with distinct run/provider response IDs and sequential times. The runtime MathVision ledger contains exactly one Plane259 binding. The existing harness has one call per loop iteration, no retry loop, and stops on error; both runs here succeeded. No other Plane259 candidate or retry/selection evidence was found in this ledger. No solver call was made during this independent review.',
        'no_fishing_within_audited_ledger':True,'only_existing_two_candidate_calls_counted':True,
        'mechanism_limit':'Both responses mention the correct 180-degree composition yet select D after visual misidentification. Thus D/D is a verified observed final-answer result, not proof that the model consistently believed a quarter-turn rule, nor proof of the authors proposed causal mechanism. Their narratives differ and contain color-as-given assumptions.',
        'evidence_details_path':str((OUT/'evidence_verification.json').relative_to(ROOT))
    },
    'exact_hashes_and_timestamps':{
        'files':frozen_stamps,'canonical_formal_question_record_sha256':ev['question_record_sha256'],'current_formal_approved_content_sha256':elig['computed_content_sha256'],'formal_user_approved_at_utc':elig['current_formal_approval']['approved_at_utc'],'candidate_pixel_hash_convention':'SHA256 of b"768x768:RGBA:" followed by decoded RGBA bytes','candidate_pixel_sha256':img['pixel_sha256'],'full_record_and_raw_response_hashes':[{'run':r['run_index'],'run_sha256':r['full_record_sha256'],'response_sha256':r['raw_response_sha256']} for r in runs],
        'all_3420_primary_input_fingerprints_match_now':len(checks)==3420 and all(d['unchanged'] for d in checks.values()),'current_live_context_and_all_marked_path_hashes_match':render['live_context_equal_frozen'] and all(x['frozen_path_hash_match'] for x in render['live_path_checks']),
        'complete_existing_evidence_manifest_path':str((OUT/'existing_evidence_start_hashes.json').relative_to(ROOT)),
        'request_image_decoded_bytes_equal_frozen_candidate':ev['decoded_png_byte_identical'],'question_hash_matches_binding':ev['question_record_hash_matches_binding'],'raw_response_content_equals_full_run_and_summary':all(r['full_content_exact_run_match'] and r['summary_full_run_exact'] for r in ev['runs']),
        'timestamp_limits':'File mtimes are local metadata, not independent tamper-proof timestamp attestations. source_scene_snapshot.json was created at 15:11:57 after the calls; its bytes match the current formal scene and its hash was already in the pre-call 15:05:21 input_fingerprints/context. No claim that the later snapshot itself predates testing.'
    },
    'render_and_preservation':{
        'two_additional_offline_frozen_replays_byte_identical_to_tested_png':render['two_frozen_replays_byte_identical'] and render['exact_frozen_candidate_byte_match'],'schema_normalization_and_live_intervals_verified':render['schema_and_normalization_valid'] and all(x['start_exact'] and x['end_exact'] for x in render['live_path_checks']),'environment':render['environment'],'all_existing_candidate_evidence_unchanged_during_review':all(unchanged.values()),'all_primary_input_hashes_still_unchanged_at_report_write':True,
        'diagnostic_resolution':'The initial broad equality checks in render_verification.json and render_preservation_supplement.json are false because legal partial styling removes two original unfilled outline artists and adds six unfilled split paths. They were retained as diagnostics. contour_preservation_conclusion.json verifies the same original path values, fill and text/view data, every original filled patch retained, no unmatched new segment, and all 76 target contour edges covered exactly once. These false broad comparisons do not indicate changed mathematics or fill.',
        'review_processes':'Finite synchronous Python processes only; no solver, server or subprocess was launched. All rendering scenes closed; renderer reports no open Matplotlib figures.',
        'files_written_only_under':str(OUT),'cache_temp_and_write_guard':'TEMP/TMP/TMPDIR, MPLCONFIGDIR, XDG_CACHE_HOME and PYTHONPYCACHEPREFIX routed under this assigned review directory; bytecode disabled. A stricter directory-specific Python audit write guard was installed before project imports, followed by the shared runtime_isolation guard. Existing helper files were only read.',
        'read_only_paths_respected':['formal library','workbench state','approvals','.env','.runtime','.git','all preexisting runtime evidence','published batches','helpers']
    },
    'current_authoritative_eligibility':elig,
    'concurrent_workspace_changes':{
        'unit07_classification_read':str((ROOT/'runtime/mathvision_special_20261101/background_07/source_preservation_classification_final.json').relative_to(ROOT)),
        'observed_existing_unrelated_drift':'unit07 documents Author-designed Plane492..503 workbench changes, aggregate question_bank and .runtime/plane_special activity. Current accepted/collected index aggregate hashes differ from the historical pre-call files, but neither contains Plane259. I did not restore or rewrite any of these files and do not identify their author from hashes.',
        'whole_workspace_unchanged_claimed':False,'relevant_frozen_math_and_evidence_unchanged':True,
        'runtime_progress_classification':'remaining_questions and exploration_report are mutable diagnostic bookkeeping, separate from frozen geometry and exact solver request/responses. Their hashes currently equal this candidates historical snapshot; future unrelated drift alone would not corrupt the frozen evidence or change authoritative eligibility.'
    },
    'objections':[
        {'severity':'nonblocking','finding':'Primary source_primary_audit.json contains unrelated Plane237 car-color wording in source_visual_findings. This copy/paste is not evidence for Plane259; actual Plane259 source JPG, formal PNG and candidate were independently inspected and corresponding glyphs verified. Frozen primary evidence was not repaired.'},
        {'severity':'nonblocking','finding':'The mechanism describes recolorings, but the actual plugin also explicitly sets 2 pt on each selected edge. This width is legal and readable; this review records the full operation.'},
        {'severity':'nonblocking','finding':'Both solver explanations have shape/color errors and sometimes treat annotation as transported ink. They do not provide a reliable mathematical proof or causal account, although the final D/D letters are unambiguous.'}
    ],
    'blocking_objections':[],
    'limitations':[
        'Exactly two candidate observations. No original-image solver control was run; no comparative gain, statistical reliability, or causality is established.',
        'No human study, accessibility study, per-marker ablation, or proof of minimal marking set. Human readability and semantics are independent reviewer judgments on actual images.',
        'Auditing local evidence and harness control flow cannot independently certify the absence of unrecorded external calls or provide cryptographic provider attestation; no contrary retry/selection evidence appears in the audited runtime ledger.',
        'Narratives are inconsistent and erroneous; recommendation relies on independently verified original mathematics plus explicit completed final letters and exact bindings, not narrative agreement.',
        'This recommendation is tied to these exact source/question/plugin/design/PNG/request/response hashes and current eligibility. It records no user approval, Pass, Collect, or publication.',
        'No original-control, narrative-consistency, human-study, statistical-gain or causal/per-marker-ablation extra hard gate was imposed.'
    ],
    'approval_or_publication_performed':False,'new_solver_calls':0
}
write(OUT/'independent_review.json',report)
emit({'decision':report['decision'],'report_path':str(OUT/'independent_review.json'),'report_sha256':sha(OUT/'independent_review.json'),'existing_evidence_files_unchanged':len(unchanged),'current_eligible':elig['eligible'],'all_inputs_rechecked':len(checks)})
