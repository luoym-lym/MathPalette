from research import *
import base64

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

plane_path=HERE/'plane_worker/checkpoint.json'
solid_path=HERE/'solid_worker/checkpoint.json'
if not plane_path.exists() or not solid_path.exists():
    raise SystemExit('Wait for both native worker final checkpoints before aggregation.')
plane=read(plane_path)
solid=read(solid_path)
root=read(HERE/'root_manual_results.json')
source_verification=read(HERE/'root_source_verification.json')

audit=[]
for binding_path in sorted(HERE.rglob('binding.json')):
    binding=read(binding_path)
    request_path=binding_path.parent/'request.json'
    payload=read(request_path)
    messages=payload.get('messages',[])
    content=messages[1]['content']
    encoded=content[1]['image_url']['url'].split(',',1)[1]
    record=eligible(binding['branch'],binding['question_id'])['record']
    checks={
        'model':payload.get('model')=='mimo-v2.6-flash',
        'thinking_disabled':payload.get('thinking')=={'type':'disabled'},
        'no_token_limit_or_extra_request_parameters':set(payload)=={'model','stream','thinking','messages'},
        'only_two_messages':len(messages)==2,
        'existing_solver_system_prompt':messages[0]=={'role':'system','content':binding['system_prompt']},
        'only_formal_question_and_candidate_image':len(content)==2 and content[0]=={'type':'text','text':record['question']},
        'frozen_request_body_hash':sha(request_path)==binding['request_body_sha256'],
        'sent_png_matches_frozen_image_hash':hashlib.sha256(base64.b64decode(encoded)).hexdigest()==binding['image_sha256'],
        'current_png_matches_binding':sha(Path(binding['image_path']))==binding['image_sha256'],
        'current_design_matches_binding':sha(Path(binding['design_path']))==binding['design_sha256'],
        'predeclared_design_snapshot_matches_binding':sha(binding_path.parent/'design_snapshot.json')==binding['design_sha256'],
    }
    started=sorted(binding_path.parent.glob('run_??_started.json'))
    runs=[]
    for path in started:
        index=read(path)['run_index']
        completion=binding_path.parent/f'run_{index:02d}.json'
        aborted=sorted(binding_path.parent.glob(f'run_{index:02d}*aborted*.json'))
        if completion.exists():
            data=read(completion)
            raw=binding_path.parent/f'run_{index:02d}_response.json'
            raw_hash_ok=(raw.exists() and sha(raw)==data.get('response_sha256')) if data['status']=='completed' else ((not raw.exists()) or sha(raw)==data.get('response_sha256'))
            runs.append({'run_index':index,'status':data['status'],'evidence':str(completion.relative_to(PROJECT)),
                         'raw_response_hash_matches':raw_hash_ok,'finish_reason':data.get('finish_reason'),
                         'truncated':data.get('truncated')})
            checks[f'run_{index:02d}_raw_hash']=raw_hash_ok
        elif aborted:
            runs.append({'run_index':index,'status':'aborted','evidence':[str(p.relative_to(PROJECT)) for p in aborted]})
        else:
            runs.append({'run_index':index,'status':'PENDING_UNRESOLVED','started':str(path.relative_to(PROJECT))})
    audit.append({'question_id':binding['question_id'],'expected_wrong_answer':binding['expected_wrong_answer'],
                  'binding':str(binding_path.relative_to(PROJECT)),'requested_runs':binding['requested_runs'],
                  'checks':checks,'all_binding_checks_pass':all(checks.values()),'runs':runs})
write(HERE/'evidence_binding_audit.json',audit)
if not all(row['all_binding_checks_pass'] for row in audit):
    raise SystemExit('Evidence binding check failed; inspect audit before finalizing.')
if any(r['status']=='PENDING_UNRESOLVED' for a in audit for r in a['runs']):
    raise SystemExit('Unresolved request evidence; inspect before finalizing.')

candidate=HERE/'solid_worker/Solid203/bridge_terminal_edge_pair'
current=eligible('SolidGeometry','Solid203')
write(HERE/'Solid203_eligibility_at_checkpoint.json',current)
queue=[{'question_id':'Solid203','variant_id':'bridge_terminal_edge_pair',
        'status':'POSSIBLE_CANDIDATE_REQUIRES_NEW_INDEPENDENT_SECOND_REVIEW',
        'formal_correct_answer':'E','predeclared_wrong_answer':'A',
        'manually_read_candidate_finals':['A','A'],'manually_read_original_control_finals':['A','B'],
        'causal_limitation':'Original control also wrong on both calls; one original A matches candidate target. Two candidate hits are not a causal or statistical guarantee.',
        'candidate_folder':str(candidate.relative_to(PROJECT)),
        'primary_review':str((candidate/'primary_review.md').relative_to(PROJECT)),
        'exact_fold_proof':str((candidate/'folding_verification.json').relative_to(PROJECT)),
        'fresh_replay':str((candidate/'fresh_replay_check.json').relative_to(PROJECT)),
        'png_sha256':sha(candidate/'candidate.png'),'design_sha256':sha(candidate/'design.json'),
        'currently_eligible':current['eligible'],
        'required_parent_action':'Create a NEW independent second-review task covering mathematical rigor, actual PNG/labels, every marker role/necessity and concrete geometric information before any delivery.'}]
write(HERE/'second_review_queue.json',queue)
processes=read(HERE/'no_live_processes.json')
if processes.get('live_matching_processes'):
    raise SystemExit('Local QuickTest processes remain; do not finalize.')

new_ids=['Plane425','Plane407','Plane313','Plane471','Plane250',
         'Solid120','Solid138','Solid205','Solid212','Solid227',
         'Solid238','Solid245','Solid246','Solid242','Solid213']
completed=sum(r['status']=='completed' for a in audit for r in a['runs'])
aborted=sum(r['status']=='aborted' for a in audit for r in a['runs'])
checkpoint={
    'created_at':datetime.now(timezone.utc).isoformat(),'status':'FINITE_RESEARCH_WORK_UNIT_COMPLETE',
    'stop_reason':'Prepared drafts and the selected fifteen-question work exhausted; all permitted purposeful designs closed, failed or prescreened. One credible two-hit possibility remains for parent independent review.',
    'all_outputs_under':str(HERE),'new_question_ids':new_ids,'new_question_count':len(new_ids),
    'prepared_five_drafts':[
        {'qid':'Plane435','variant':'v01','preset':'4','finals':['2','2'],'result':'target_miss'},
        {'qid':'Plane435','variant':'v02','preset':'5','finals':['3','2'],'result':'target_miss'},
        {'qid':'Solid166','variant':'bridge_terminal_edge_pair','preset':'1','finals':['3','4'],'result':'target_miss'},
        {'qid':'Solid203','variant':'bridge_terminal_edge_pair','preset':'A','finals':['A','A'],'result':'possible_for_new_second_review'},
        {'qid':'Solid240','variant':'bridge_false_hinge_mapping','preset':'6','finals':[],
         'result':'prescreen_reject_actual_hidden_edge_is_not_Q_question_mark_hinge',
         'review':str((HERE/'prepared_Solid240/prescreen_rejection.json').relative_to(PROJECT))}],
    'root_exact_attempts':root,
    'plane_worker_complete_checkpoint':str(plane_path.relative_to(PROJECT)),
    'plane_worker_results':plane,
    'solid_worker_complete_checkpoint':str(solid_path.relative_to(PROJECT)),
    'solid_worker_results':solid,
    'possible_candidates_for_parent_new_independent_second_review':queue,
    'new_qualified_deliveries':0,'independent_second_reviews_performed_by_this_worker':0,
    'evidence_audit':str((HERE/'evidence_binding_audit.json').relative_to(PROJECT)),
    'test_invocations_including_control':len(audit),'completed_calls_including_control':completed,
    'aborted_calls':aborted,'all_binding_checks_pass':True,
    'root_frozen_input_verification':source_verification,
    'formal_library_workbench_env_protocol_approvals_recipes_indices_mutated':False,
    'previous_exploration_reports_batches_or_test_evidence_mutated':False,
    'pass_collect_or_review_APIs_used':False,
    'no_live_process_confirmation':processes,'native_workers_finished':True,
    'remaining_recommendations':[
        'Parent: independently review Solid203 in a NEW task before any qualified delivery. Preserve its A/B incorrect original control disclosure.',
        'Do not revive Solid240 prepared draft: its selected spatial edge does not delimit Q and ?.',
        'Do not combine individual target hits from different Plane425, Solid120 or Solid138 images, and do not retry aborted identical requests.',
        'Future unattempted leads, after fresh eligibility and report checks: Plane197 midpoint path length, Plane258 nested-square unit basis, Plane225 repeated-reflection feature mapping, Plane238 hole/number-grid correspondence, Solid170 hole-to-net mapping, Solid188 diagonal-to-net mapping, Solid169 and Solid185 surface-route measurement.',
        'All future units require new immutable hypotheses, exact context/path coordinates, actual PNG inspection and a fresh independent review of each possible delivery.'
    ]
}
write(HERE/'checkpoint.json',checkpoint)
print(json.dumps({'checkpoint':str(HERE/'checkpoint.json'),'invocations':len(audit),'completed_calls':completed,
                  'aborted_calls':aborted,'possible_candidates':len(queue),'new_questions':len(new_ids)},ensure_ascii=False))
