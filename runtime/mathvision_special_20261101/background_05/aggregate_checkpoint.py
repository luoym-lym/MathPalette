from research import *
import copy
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def relative(p):return Path(p).relative_to(ROOT).as_posix()
a=read(HERE/'plane_a/checkpoint.json');b=read(HERE/'plane_b/checkpoint.json');s=read(HERE/'solid_worker/checkpoint.json');ext=read(HERE/'plane_b/extension_checkpoint.json')
qa=read(HERE/'plane_a/second_review_queue.json');qb=read(HERE/'plane_b/second_review_queue.json');qs=read(HERE/'solid_worker/second_review_queue.json');qe=read(HERE/'plane_b/extension_second_review_queue.json')
binding=read(HERE/'evidence_binding_audit.json');preservation=read(HERE/'source_preservation_final.json');processes=read(HERE/'process_snapshot_final.json')
assignment=read(BASE/'background_05_assignment.json')['question_ids']
assessed=copy.deepcopy(a['assessed_questions'])+copy.deepcopy(b['assessed_questions'])+copy.deepcopy(s['assessed_questions'])
assert len(assessed)==20 and {v['question_id'] for v in assessed}==set(assignment)
for question in assessed:
    if question['question_id']=='Plane223':
        question['initial_preserved_worker_checkpoint_status']=question['status'];question['status']='ASSESSED_TESTED_REJECTED_BY_FINITE_EXTENSION';question['completed_calls']=2;question['variants']=[ext['candidate']];question['completion_overlay_path']=relative(HERE/'plane_b/extension_checkpoint.json')
possible=copy.deepcopy(qa['possible_candidates'])+copy.deepcopy(qb['possible_candidates'])+copy.deepcopy(qe.get('possible_candidates',[]))
assert len(possible)==2
for candidate in possible:
    candidate['qualification_status']='POSSIBLE_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'
    if candidate['question_id']=='Plane234':candidate['parent_review_focus']='Critical original gray ray remains semantically unchanged but is small. Source gray-pixel count in the green outlined feature drops from27 to16 visible pixels; reviewer must inspect actual original/candidate clarity and reject if ambiguous. No human performance or ablation claim.'
queue={'created_at':datetime.now(timezone.utc).isoformat(),'unit':'background_05','status':'TWO_PRIMARY_POSSIBILITIES_REQUIRE_NEW_PARENT_INDEPENDENT_REVIEW','possible_count':len(possible),'possible_question_ids':[p['question_id'] for p in possible],'possible_candidates':possible,'prepared_untested':[],'rejected_cases_evidence':[relative(HERE/'plane_a/checkpoint.json'),relative(HERE/'plane_b/checkpoint.json'),relative(HERE/'plane_b/extension_checkpoint.json'),relative(HERE/'solid_worker/checkpoint.json')],'parent_review_instructions':['Create a NEW independent review task; none of these primary authors has independently second-reviewed or approved a candidate.','Recheck exact input/source/context/path hashes, schema/default normalization, no-op equality, repeat tested PNG bytes and both complete raw finals.','Independently prove unchanged unique mathematical answer and inspect actual PNGs for readable givens, original fills and labels, no changed counted target or false explicit condition.','Assess every marker role and concrete input-feature/transform/edge correspondence. Many purposeful marks are allowed.','Original controls need not be correct; identical reasoning, human performance measurement and per-marker ablations are not extra hard gates. Disclose limitations.','Only after independent recommendation may parent reproduce tested bytes and package an immutable delivery. No Pass/Collect here.'],'approval_status':'No candidate in this unit is approved or delivered'}
write(HERE/'second_review_queue.json',queue)
designs=[]
prior=read(HERE/'previous_evidence_before.json');prior_hashes={v for v in prior.values() if isinstance(v,str)}
for p in sorted(HERE.rglob('design.json')):
    if not (p.parent/'candidate.png').is_file():continue
    d=read(p);kind='original_control' if 'original_control' in p.parts else 'candidate'
    png_hash=digest(p.parent/'candidate.png')
    designs.append({'question_id':d['question_id'],'variant_directory':relative(p.parent),'kind':kind,'expected_wrong_answer':d['expected_wrong_answer'],'design_sha256':digest(p),'png_sha256':png_hash,'identical_to_any_prior_runtime_file':png_hash in prior_hashes})
candidate_designs=[v for v in designs if v['kind']=='candidate'];controls=[v for v in designs if v['kind']=='original_control']
assert len(candidate_designs)==11 and len(controls)==1
assert binding['all_bindings_valid'] and binding['pair_count']==12 and binding['completed_call_count']==24
assert all(not v['identical_to_any_prior_runtime_file'] for v in candidate_designs)
assert not preservation['changed'] and not preservation['added'] and not preservation['deleted'] and not preservation['prior_evidence_changed_or_deleted']
assert processes['no_live_unit_python_processes']
checkpoint={
 'created_at':datetime.now(timezone.utc).isoformat(),'unit':'background_05','status':'FINITE_BACKGROUND_05_COMPLETE',
 'stop_reason':'All exactly20 assigned new categorical geometry questions assessed. All11 saved purposeful candidate designs received their own complete two-call tests. No further clean purposeful design was identified; finite work unit exhausted with two primary possibilities. No identical failed/aborted image was retested.',
 'all_outputs_under':relative(HERE),'assigned_question_ids':assignment,'assessed_question_ids':assignment,'assessed_question_count':20,'questions_with_saved_designs':10,'prescreen_only_question_count':10,
 'saved_candidate_design_count':11,'complete_candidate_pair_tests':11,'completed_candidate_calls':22,'optional_original_control_pair_tests':1,'optional_original_control_completed_calls':2,'total_completed_calls':24,'aborted_or_incomplete_calls':0,'untested_complete_design_count':0,
 'possible_two_hit_count':2,'possible_question_ids':['Plane217','Plane234'],'possible_status':'Primary research possibilities, not independent recommendations or approved/delivered variants.',
 'assessed_questions':assessed,'all_design_records':designs,
 'worker_checkpoints':{'plane_a':relative(HERE/'plane_a/checkpoint.json'),'plane_b_initial_preserved':relative(HERE/'plane_b/checkpoint.json'),'plane_b_final_extension':relative(HERE/'plane_b/extension_checkpoint.json'),'solid_worker':relative(HERE/'solid_worker/checkpoint.json')},
 'second_review_queue_path':relative(HERE/'second_review_queue.json'),'possible_candidates':possible,
 'manual_final_review_paths':[relative(HERE/'plane_a/manual_final_reviews.json'),relative(HERE/'plane_b/checkpoint.json'),relative(HERE/'plane_b/extension_manual_final_review.json'),relative(HERE/'solid_worker/manual_final_reviews.json')],
 'evidence_binding_audit_path':relative(HERE/'evidence_binding_audit.json'),'source_preservation_audit_path':relative(HERE/'source_preservation_final.json'),
 'source_preservation':{'existing_non_runtime_non_git_file_count':preservation['existing_non_runtime_non_git_file_count'],'prior_runtime_evidence_count':preservation['prior_runtime_evidence_count'],'changed_or_deleted':[],'added_outside_runtime':[],'formal_files_protocols_approvals_indices_env_runtime_and_git_untouched':True},
 'request_audit':{'pair_count_including_original_control':12,'complete_calls':24,'exact_formal_question_plus_candidate_png_plus_existing_system_only':True,'same_frozen_image_and_preset_per_pair':True,'settings':'Unchanged quicktest3 mimo-v2.6-flash thinking.disabled, no token/profile/local-timeout overrides or automatic retries.','raw_evidence_binding_details_path':relative(HERE/'evidence_binding_audit.json')},
 'no_live_process_confirmation_path':relative(HERE/'process_snapshot_final.json'),'no_live_own_api_or_python_processes':True,'native_children':{'spawned':2,'task_names':['/root/plane_a','/root/plane_b'],'both_finished':True,'no_top_level_threads_worktrees_or_t3_delegates_created':True},
 'rejected_and_untested_cases':['Nine tested candidates lack two unambiguous preset hits and must not be retested as identical images.','Solid144 terminal B is paired with inconsistent X/Y or X/Y/Z object sets; it is not a target hit.','Solid187 two distinct mechanisms (unmatched B caps versus adjacent D hole pairs) both missed their own presets; all histories retained.','Plane223 was initially held untested only by the child stop rule; finite extension completed C/D, so no prepared complete candidate remains untested.','Ten questions are prescreen-only and retained with explicit reasons. Solid105/Solid149 prescreens do not claim completed independent unique-answer proofs.'],
 'limitations':['These are primary author reviews only; parent must create a NEW independent second review for each proposed delivery.','Two stateless calls on one frozen image do not estimate general success rates or causal effects.','Plane217 original controls are C/C, with imperfect verbal descriptions; exact frozen geometry supports primary proof.','Plane234 has no original control and its small gray feature needs careful human-readability review.','No per-marker statistical ablation or human performance study was performed.','Original controls need not be correct and two explanations need not be identical; those are not added gates.'],
 'next_recommendations':['Parent independently review exact Plane217 and Plane234 packages, including full finals and actual PNGs, before any packaging or delivery.','Parent may aggregate this unit into global reports/remaining queue; this research agent left those prior files unchanged.','Choose genuinely new questions in any next authorized finite work unit; do not revive previously rejected/failed identical images.'],
 'approval_status':'No Pass, Collect, review API, formal change, approval or delivery performed.'}
write(HERE/'checkpoint.json',checkpoint)
write(HERE/'artifact_manifest.json',{'created_at':datetime.now(timezone.utc).isoformat(),'checkpoint_sha256':digest(HERE/'checkpoint.json'),'second_review_queue_sha256':digest(HERE/'second_review_queue.json'),'evidence_binding_audit_sha256':digest(HERE/'evidence_binding_audit.json'),'source_preservation_final_sha256':digest(HERE/'source_preservation_final.json'),'candidate_designs':candidate_designs,'original_controls':controls,'meaning':'Research artifact binding only, not publication or approval.'})
print(json.dumps({'assessed':20,'candidate_designs':11,'candidate_pairs':11,'candidate_calls':22,'control_calls':2,'total_calls':24,'possible':2,'queue':relative(HERE/'second_review_queue.json'),'checkpoint':relative(HERE/'checkpoint.json')}))
