import review_bootstrap as r
import json
import os

integrity=r.read(r.OWN/'integrity_checks.json')
math=r.read(r.OWN/'independent_math.json')
replay=r.read(r.OWN/'replay.json')
eligibility=r.read(r.OWN/'current_eligibility.json')
history=r.read(r.OWN/'history_audit.json')
raw=r.read(r.OWN/'complete_raw_readings.json')
test=next((r.CAND/'tests').iterdir())
binding=r.read(test/'binding.json')
design=r.read(r.CAND/'design.json')

# Recompute scoped preservation now. Do not restore a source or update authority.
before=r.read(r.OWN/'scoped_before.json')
after=r.snapshot()
r.save(r.OWN/'scoped_after.json',after)
diffs=[{'path':p,'before':before.get(p),'after':after.get(p)} for p in sorted(set(before)|set(after)) if before.get(p)!=after.get(p)]
oldbefore=r.read(r.OWN/'additional_old_sources_before.json')
oldafter={p:r.sha(r.PROJECT/p) for p in oldbefore}
r.save(r.OWN/'additional_old_sources_after.json',oldafter)
olddiffs=[{'path':p,'before':v,'after':oldafter[p]} for p,v in oldbefore.items() if v!=oldafter[p]]
preservation={'checked_at_utc':r.now(),'initial_scope_files':len(before),'same_scope_files_after':len(after),
    'exact_scope_differences':diffs,'relevant_old_trial_files':len(oldbefore),'relevant_old_trial_differences':olddiffs,
    'primary_initial_old_reference_manifest_files':len(r.read(r.OWN/'old_readonly_preservation.json')),
    'all_primary_initial_hashes_exact':all(x['expected']==x['current'] for x in r.read(r.OWN/'old_readonly_preservation.json')),
    'scope':'The whole completed u01 unit tree, frozen Plane217 reference directory, Plane461/217 formal source dependency lists, named protocols, task/history/preflight/steering, finite parent native_u01_u04 audit tree, and two relevant old Plane461 trial trees. Authority fingerprint/current target status independently recomputed.',
    'claim_limit':'No whole-workspace unchanged claim. Mutable parent progress and unrelated user workbench changes are not restored or misrepresented. No original approvals, source, formal, reference, primary or raw files edited.'}
r.save(r.OWN/'source_preservation.json',preservation)

markers=[
 {'action_index':0,'target':'o14','color':'#DC2626','existing_geometry':{'points':[[12.09,5.29],[12.41,5.61]],'slope_exact':'1'},
  'actual_role':'One original stroke of the circled X that specifies the punch location, not a physical crease or two hole centers.',
  'information_judgment':'Its red direction is opposite to the red D hole-pair slope -1. As one half of an unordered X it contributes shape resemblance, but does not supply the claimed same-color directional match or a physical unfolding correspondence.'},
 {'action_index':1,'target':'o15','color':'#2563EB','existing_geometry':{'points':[[12.09,5.61],[12.41,5.29]],'slope_exact':'-1'},
  'actual_role':'Second original X stroke; same punch location as o14.',
  'information_judgment':'Its blue direction is opposite to the blue D hole-pair slope +1. Blue crosses over red at the original crossing; both strokes remain visible, neither is an extra puncture.'},
 {'action_index':2,'target':'o40','color':'#2563EB','existing_geometry':{'center':[19.75,0.75],'radius':0.22},
  'actual_role':'Original D bottom-left hole outline; forms the rising blue pair with o43.',
  'information_judgment':'Useful to identify a diagonal opposite-hole pair within D, but its source blue stroke falls. The selection does not track a genuine punched-hole or fold-distance invariant from the source.'},
 {'action_index':3,'target':'o41','color':'#DC2626','existing_geometry':{'center':[20.25,0.75],'radius':0.22},
  'actual_role':'Original D bottom-right hole outline; forms the falling red pair with o42.',
  'information_judgment':'Completes the red opposite-hole grouping, but that pair falls while red X rises. No supported same-color geometric correspondence.'},
 {'action_index':4,'target':'o42','color':'#DC2626','existing_geometry':{'center':[19.75,1.25],'radius':0.22},
  'actual_role':'Original D top-left hole outline; other member of the red falling pair.',
  'information_judgment':'Makes red grouping visible, with the same unresolved reversed-direction objection as o41; it does not encode the preserved distance from the original free top edge.'},
 {'action_index':5,'target':'o43','color':'#2563EB','existing_geometry':{'center':[20.25,1.25],'radius':0.22},
  'actual_role':'Original D top-right hole outline; other member of the blue rising pair.',
  'information_judgment':'Makes blue grouping visible, with the same unresolved reversed-direction objection as o40; quartet remains the wrong central square.'}
]
for m in markers:
    m.update({'operation':'set_object_style','interval':'whole original object; no partial interval field',
        'linewidth_pt':1.5,'schema_legal':True,'coordinates_radius_linestyle_fill_text_preserved':True,
        'native_768_visible':True,'fully_overwritten_or_useless_action':False,
        'passes_required_targeted_source_to_recipient_information_test':False})

proof=[
 'Read the exact formal words and options and personally view both the actual 1930x980 source JPG and 768x768 formal PNG. The first upward arrows fold the lower half onto the upper half; the second rightward arrows fold the left half onto the right. The final upper and right boundaries are free outer edges, while the lower and left boundaries are hinges.',
 'Normalize the initial sheet to [0,4]x[0,2]. The first fold maps lower y to 2-y, retaining [0,4]x[1,2]. The second maps left x to 4-x, retaining [2,4]x[1,2]. No rotation of the final packet is shown.',
 'The actual final display packet has corners (12,4.7),(14,4.7),(14,5.7),(12,5.7), and the circled X center is (12.25,5.45). Undo only the diagram translation to obtain retained coordinates (9/4,7/4). The X is near a hinge on its left but near a FREE edge above it; it is not at either fold intersection.',
 'The two independent inverse reflections give x in {7/4,9/4} and y in {1/4,7/4}. Their Cartesian product is the complete four-center orbit. Radius 11/50 is smaller than the minimum 1/4 center-to-boundary distance, so clearance is 3/100: the punch crosses neither a fold nor an outer edge, and produces exactly four separate congruent circular holes.',
 'Enumerate all unchanged option centers after removing each option horizontal translation. Only B equals that orbit and all radii agree. A lacks the required separate horizontal and vertical reflection symmetry; C uses x={1/4,15/4}; D uses y={3/4,5/4}; E uses both that wrong x and that wrong y. The full exact rational sets are included below. Therefore B alone is possible. This proof does not use the approved answer, parent calculation or model outputs as premises.'
]

report={
 'review_schema_version':'1.0.0','created_at_utc':r.now(),'review_role':'NEW_INDEPENDENT_SECOND_REVIEW_ONLY',
 'decision':'reject','review_complete':True,'blocking_incomplete_review':False,
 'question_id':'Plane461','variant_id':'u01_symbol_X_diagonals_to_central_hole_pairs',
 'candidate_directory':str(r.CAND),'own_writable_root':str(r.OWN),
 'candidate_png_path':str(r.CAND/'candidate.png'),'candidate_png_sha256':r.sha(r.CAND/'candidate.png'),
 'image_sha256':r.sha(r.CAND/'candidate.png'),'plugin_path':str(r.CAND/'plugin.json'),'plugin_sha256':r.sha(r.CAND/'plugin.json'),
 'design_path':str(r.CAND/'design.json'),'design_sha256':r.sha(r.CAND/'design.json'),
 'summary_path':str(test/'summary.json'),'summary_sha256':r.sha(test/'summary.json'),
 'context_sha256':r.sha(r.CAND/'context.json'),'design_snapshot_sha256':r.sha(test/'design_snapshot.json'),
 'request_sha256':r.sha(test/'request.json'),'binding_sha256':r.sha(test/'binding.json'),
 'raw_sha256':[x['raw_sha256'] for x in raw],
 'decision_reason':'The exact image fails targeted information correspondence and the requested imitation fidelity. There is a real unordered X/square-diagonal resemblance, but both frozen same-color direction identities are reversed. A symbolic punch locator is substituted for actual hole/fold geometry, so the six legal styles largely promote D without the specific clear same-color physical comparison in current Plane217. The two explicit D selections do not cure this semantic/information defect.',
 'method_fidelity':{
    'classification':'too distant','current_reference':'Plane217 current user C01, option A comparison',
    'reference_png_sha256':r.sha(r.REF/'C01.png'),'reference_plugin_sha256':r.sha(r.REF/'C01.json'),
    'actual_reference_observation':'Four existing source holes: top-left and bottom-right red, bottom-left and top-right blue. In option A, the actual falling dotted diagonal is red and rising dotted diagonal is blue. Same-color hole pair and line genuinely share a direction category; no equality or exact parallelism is newly given.',
    'preserved_surface_features':'Two colors; two original direction objects and four existing hole outlines; no added line or point; modest 1.5 pt widths.',
    'concrete_departure':'Plane461 colors the glyph strokes of X instead of physical holes or fold boundaries. These strokes designate a location and carry no original physical unfolding direction. Additionally red rising X is paired with a red falling hole pair, and blue falling X with a blue rising pair. This is a conceptual extension beyond a reversed-role imitation, and its information mapping is worse defined.',
    'residual_true_commonality':'As unordered sets, both pairs of directions are {+1,-1}; D is a central square of holes. That coarse glyph-to-shape resemblance is specific enough to explain why the design is not a random whole-choice tint, but it does not validate either same-color correspondence or a physical source relation.',
    'latest_user_steering_applied':'以模仿为主就好，不要探索太多了。 This existing exact image is rejected; no replacement, color swap, reflection-parity explanation or further exploration made.',
    'not_a_reference_approval_judgment':'The existing current user Plane217 annotation is provenance and a visual reference; this report does not reapprove it or substitute old option labels/colors.'},
 'original_mathematics':{'independent_proof':proof,'exact_calculation':math,'unique_answer':'B','parent_proof_challenged_and_result':'Independently derived the same orbit from the actual source arrows and exact scene. Parent arithmetic agrees; that agreement was not used as proof.'},
 'per_marker_review':markers,
 'mark_group_judgment':{
    'technical_legality':'All six actions pass the unchanged schema and normalized frozen render. Each affects a distinct complete existing vector object. No added line, point, text, cut, printed identity, partition or auxiliary condition; no fully overwritten action. Count six is descriptive, not an acceptance cap.',
    'informational_failure':'Each same-color source/recipient direction identity is opposite. To rescue it one must ignore color identities and compare the unordered X shape, or invent an unpredeclared reflection. I do neither. Symbol shape resemblance alone does not establish the intended physical information comparison under this assignment.',
    'why_not_accept_on_hits':'Both D selections are empirical records only. Independent mark usefulness fails even though integrity and mathematical uniqueness pass.',
    'native_readability':'At actual 768x768, choice letters, circle count, black dashed center axes, final circled X, packet edges and folding arrows remain recognizable. Source X is very small; its two colors are visible in short strokes. D circle borders are thicker and nearly touch at native size, but four white hole interiors remain visible. I do not invent a new illegibility veto.',
    'all_original_marks':'o0/o6/o12 packet outlines; o1/o7 stage fold dashes; o2/o4/o8/o10 curved arrows and o3/o5/o9/o11 black filled heads; o13 original punch circle; all option boundaries, ten option dashed axes, untouched A/B/C/E holes and five black text labels retained. Target has no semantic-gray region. Only o14/o15 and o40..o43 styles change; no partial intervals or geometry changes.',
    'overlays':'The two X strokes cross at their original intersection; blue may cover red only at the existing crossing. Their widened endpoints may touch the existing black circle contour. No complete stroke disappears. D colored outlines can visually emphasize apparent touching/layers; none of this adds a physical condition.',
    'three_dimensional_freezing':'Not applicable: this is a frozen 2D paper-fold diagram. The scene geometry, viewport/projection mapping and every original line-style visibility remain fixed separately.'},
 'physical_color_semantics':{
    'annotation_reading':'X explicitly means the location at which one circular hole is punched. Its two colored strokes are annotations on that existing symbol; they are not two cuts or two physical hole trajectories. Colored D outlines annotate existing absent-paper boundaries, not printed paper content.',
    'reasonable_literal_reading_checked':'If the X strokes were literally ink on the packet, the wording still asks for the circular hole AT X, and does not ask to reproduce a printed X pattern. A hole removes the center ink rather than turning its two strokes into four circular holes. Color on a hole boundary is not a given four-color printed pattern. No reasonable added printed-pattern condition is licensed by these words. Under the ordinary stated task B stays unique.',
    'observed_bad_reading':'Run 2 explicitly treats red/blue circles as overlapping paper layers. That is not a condition of the formal problem and does not validate a physical interpretation of the colors.',
    'semantic_result':'I do not claim the original unique answer was changed. The rejection is the poor source-to-recipient information mapping and imitation distance; possible layer cue is a documented concern, not an invented new printed condition.'},
 'two_complete_final_readings':raw,
 'final_selection_assessment':{
    'frozen_wrong_preset':'D','frozen_wrong_value':'D central four-hole cluster','preset_frozen_at':design['created_at'],
    'test_binding_created_at':binding['created_at'],'actual_complete_calls':2,'final_letters':['D','D'],
    'matches_explicit_preset_selections':[True,True],
    'value_caveat':'Both explicitly select D and intend a central four-hole result. Run1 describes a cardinal cross instead of the actual 2x2 square; I retain that false prose and do not call it exact geometry agreement. Run2 explicitly identifies D central four-hole cluster. Neither response gives a different explicit terminal option/numeric value.',
    'reasoning_divergence':['Run1 wrongly locates X at both fold intersections and invents cardinal above/below/left/right holes.','Run2 mislabels the free top edge as a hinge, claims an on-edge punch and assigns red/blue to overlapping paper layers. It also misdescribes B and E positions.'],
    'mechanism_not_established':'Neither complete raw response performs the predeclared same-color X-stroke to opposite-hole-pair comparison. No post-hoc reflection explanation inferred.'},
 'frozen_evidence_integrity':{
    'all_35_exact_offline_integrity_checks_passed':not integrity['failed_checks'],'checks':integrity,
    'request_contents':'Exactly configured system prompt, exact formal question/options and this candidate PNG. model mimo-v2.6-flash, stream false, thinking disabled. No answer, intention, history, reference, source JPG, design text, max_tokens or max_completion_tokens in request.',
    'chronology':'Design created 2026-11-02T09:38:58.124694+00:00; binding 09:44:00.355352; run starts 09:44:00.359763 and 09:44:12.929491. Design snapshot, PNG, plugin, context and actual-request digests bind the same frozen objects. Both raw finishes stop, HTTP 200, distinct provider IDs, reasoning tokens zero; no truncation or transport errors for assigned image.',
    'exact_transport_and_no_retry':'Saved transport process reports exactly two urllib requests and exit zero; current candidate has exactly one invocation and two starts, jobs and raws. Independent retained-files scan found exactly two unique starts for its image, no matching orphan starts, no retry or hidden third in retained evidence.',
    'hashes':integrity['test_hashes'],'external_attestation_limit':'This verifies retained local evidence, not an independent audit of unrecorded provider traffic.'},
 'offline_replay':replay,
 'current_eligibility':eligibility,
 'historical_record_review':{
    'audit_path':str(r.OWN/'history_audit.json'),'audit_sha256':r.sha(r.OWN/'history_audit.json'),
    'examined_request_files':history['retained_request_files_examined'],'examined_started_files':history['all_started_files_examined'],
    'current_image_unique_run_count':len(history['assigned_question_and_PNG_unique_started_run_ids']),
    'parse_errors':history['parse_errors_preserved_not_repaired'],
    'relevant_old_trials':[{'variant':x['directory'],'preset':x['preset'],'image_sha256':x['image_sha256'],'finals':x['independent_manual_final_letters'],'preset_hits':x['independent_preset_hits']} for x in history['old_designs_and_complete_raw_readings']],
    'failures_preserved':'Earlier C preset was C/D, one hit only. Earlier D preset was B/B, zero hits; its central-cluster narrative must not be relabelled D. All four old complete raw texts personally read. Current image hash differs from both old failed images. Neither old image rerun.',
    'other_unit_errors':'Read retained unit ndarray serialization error and untested Plane202 proof-text correction records as history. They are unrelated offline preparation failures, not an excuse to delete or relabel tested evidence. Unit tree remains unchanged.',
    'cross_ID_authorization':history['cross_ID_transfer']},
 'parent_objections_independently_assessed':[
    'Read parent preflight and finite native_u01_u04 audit/method_fidelity plus primary caveat. Their exact hashes and raw D/D records agree with the new offline verification.',
    'Accepted the slope objection only after deriving actual slopes from the original scene and viewing the exact PNG. Red +1 versus -1 and blue -1 versus +1 are exact, not approximate.',
    'The claim that this directly transfers current Plane217 with roles reversed is too strong: it changes physical-hole information to a location glyph and reverses the color direction identities. This report corrects that characterization only here, leaving primary design and posttest caveat untouched.',
    'The parent noted divergent false narratives. New full-raw reading confirms them. Preset hits are preserved as explicit D selections and not treated as proof of each mark or causal mechanism.'
 ],
 'concrete_objections':[
    {'id':'O1','severity':'reject','finding':'Both source/recipient same-color signed directions are opposite in the exact frozen image.','evidence':'o14 slope +1 versus red o41/o42 slope -1; o15 slope -1 versus blue o40/o43 slope +1.','resolution':'Unresolved in this image. No color repair or post-hoc reflection story allowed.'},
    {'id':'O2','severity':'reject','finding':'Glyph-to-hole shape substitution is too distant from the current reference physical comparison under the imitation preference.','evidence':'X is solely the puncture-location symbol. Original physical variables are hole center offsets and two hinge/free-edge distinctions. Color grouping does not track these.','resolution':'Unordered diagonal resemblance acknowledged, but insufficient for required targeted true correspondence.'},
    {'id':'O3','severity':'limitation','finding':'Two wrong explicit D choices do not establish the proposed mechanism; run1 shape prose is inaccurate and run2 invents colored layers.','evidence':'Both complete raw contents embedded above.','resolution':'Empirical final choices retained; no causal/general-rate claim.'}
 ],
 'limitations':[
    'No correct-control or incremental causal gain requirement imposed. Existing controls may be wrong; no new control or API call made.',
    'Two observations do not establish a rate, statistical gain, reliable internal mechanism or individual mark causal necessity.',
    'Exact replay and schema legality are necessary technical checks, not proof of mathematical or informational merit.',
    'No whole-workspace preservation claim and no claim to audit unrecorded external calls.',
    'Decision is an independent research rejection, not user approval, Pass, Collect, publication or original-question re-review authority.'
 ],
 'source_preservation':preservation,
 'process_closure':{'owned_solver_API_calls':0,'child_agents':0,'servers':0,'background_jobs_started':0,
    'all_review_commands_foreground_or_awaited':True,'numeric_replay_process_exit_code':0,'matplotlib_figures_remaining_after_replay':[],
    'report_writer_pid':os.getpid(),'report_writer_exits_on_completion':True,
    'final_OS_process_query_evidence':'process_closure.json (written after this report writer exits)',
    'primary_worker_shutdown_records_read':['process_shutdown_evidence.json','process_shutdown_verified.json'],
    'workbench_state_unchanged_by_review':True,'authority_changes':[]},
 'own_offline_errors':[r.read(r.OWN/'offline_error_001.json')],
 'review_boundaries':{'exact_one_candidate':True,'alternatives_designed':0,'colors_or_presets_repaired':False,
    'primary_or_old_sources_edited':False,'model_or_provider_switched':False,'solver_or_API_calls':0,
    'Pass_Collect_original_approval_publication':False,'recommendation_would_mean_research_only':True}
}

assert not integrity['failed_checks']
assert not diffs and not olddiffs
assert history['assigned_question_and_PNG_exactly_two_unique_started_runs']
assert not history['same_image_starts_without_request'] and not history['parse_errors_preserved_not_repaired']
assert report['decision'] in ('recommended','reject')
assert len(report['per_marker_review'])==6 and len(raw)==2
r.save(r.OWN/'independent_review.json',report)
print(json.dumps({'decision':report['decision'],'report':str(r.OWN/'independent_review.json'),
    'sha256':r.sha(r.OWN/'independent_review.json'),'preservation':{'scoped_files':len(before),'old_trial_files':len(oldbefore),'differences':diffs+olddiffs},
    'reason':'Same-color directions reversed; glyph-to-hole extension fails required targeted information correspondence and imitation fidelity.'},ensure_ascii=False))
