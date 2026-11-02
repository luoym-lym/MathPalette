from bootstrap import *
from publish_batch import verify_evidence
d=OWN/'Plane213/user233_exterior_concave_corner_to_B_v2'
s,rec,sp=verify_evidence(d);ev=sp.parent
assert s['requested_runs']==len(s['results'])==2 and s['two_completed']
assert sha(d/'design.json')==sha(ev/'design_snapshot.json')==s['design_sha256']
assert sha(ev/'request.json')==s['request_body_sha256']
assert s['image_sha256']==sha(d/'candidate.png')==read(OWN/'prelaunch_gate.json')['PNG_sha256']
assert s['expected_wrong_answer']=='B' and rec['answer']=='A'
assert s['settings']['model']=='mimo-v2.6-flash' and s['settings']['thinking']=={'type':'disabled'}
design=read(d/'design.json');assert datetime.fromisoformat(design['created_at'])<datetime.fromisoformat(s['created_at'])
answers=[]
for i,r in enumerate(s['results'],1):
 raw=read(ev/f'run_{i:02d}_response.json');answer=raw['choices'][0]['message']['content']
 assert answer==r['answer'] and raw['choices'][0]['finish_reason']=='stop'
 assert r['status']=='completed' and not r.get('truncated') and r['http_status']==200
 assert r['request_body_sha256']==s['request_body_sha256']
 answers.append(answer)
manual_finals=['B','E'] # Personally read both full raw responses before writing this review.
reasoning=[
 '完整终答明确为B。正文将实际外边界色线幻读为internal lines/cut seams，又声称B能三份铺满；错误几何与枚举不符。存在颜色匹配叙述，但不能据此证明因果或内部机制。',
 '完整终答明确为E。正文把15格棋盘幻读成5×5减2×2=21，并错误计数所有选项；主要依据幻读面积，不支持预设外凹角对应机制。'
]
hits=[x=='B' for x in manual_finals];assert hits==[True,False]
save(d/'manual_final_review.json',{'at_utc':now(),'manually_read_all_full_raw_answers':True,'frozen_wrong_preset':'B','correct_answer':'A','final_answers':manual_finals,'matches_original_preset':hits,'two_hit':False,'complete_raw_answers':answers,'per_response_reasoning_limitations':reasoning,'no_incidental_mention_counted_as_final':True,'no_posthoc_relabel_or_retry':True,'classification':'MISS; not a qualified candidate; no independent review queue','no_causal_or_statistical_gain_claim':True})
reaped=read(OWN/'pair_reaped.json');assert reaped['reaped'] and reaped['returncode']==0
assert read(OWN/'pair_process_finished.json')['finished']
before=read(OWN/'readonly_before_calls.json');changed=[]
for p,h in before.items():
 if sha(p)!=h:changed.append(p)
assert not changed
elig=eligibility()
save(OWN/'readonly_preservation_final.json',{'checked_at_utc':now(),'tracked_file_count':len(before),'all_tracked_original_formal_reference_helper_and_old_evidence_hashes_unchanged':True,'changed_files':changed,'scope':'Exactly the files in readonly_before_calls.json; no whole-workspace claim.','source_hashes':before})
save(OWN/'second_review_queue.json',[])
save(OWN/'process_closure_audit.json',{'at_utc':now(),'API_child_pid':reaped['pid'],'API_child_reaped':True,'API_child_returncode':0,'pair_process_finished_record_present':True,'active_owned_API_requests':0,'no_additional_worker_or_server_started':True,'API_errors':0,'API_aborts':0,'API_retries':0})
save(OWN/'checkpoint.json',{'at_utc':now(),'unit':'u10_plane213_refine','scope':['Plane213'],'assessed_question_ids':['Plane213'],'unworked_question_ids':[],'new_material_designs':1,'completed_API_calls':2,'API_errors':0,'API_aborts':0,'API_retries':0,'active_owned_API_requests':0,'candidate_directory':str(d),'variant_id':design['variant_id'],'PNG_sha256':sha(d/'candidate.png'),'expected_wrong_answer':'B','correct_answer':'A','manually_read_final_answers':manual_finals,'preset_hits':hits,'credible_two_hit_candidates':0,'second_review_queue':[],'status':'completed_finite_one_material_hypothesis; preset MISS','finite_scope_note':'Parent assigned exactly one material new hypothesis/pair this turn. Further substantive design work, if needed, belongs to a new parent assignment; unchanged frozen picture may not be retested.','root_prior_new_task_transfer_preserved':{'directory':str(TASK/'root_213/Plane213/user233_boundary_spine_foot_transfer_v1'),'preset':'C','final_answers':['B','C'],'status':'MISS'},'current_eligibility':elig,'formal_source_and_old_evidence_unchanged':True,'independent_review_performed':False,'Pass_Collect_or_user_approval_performed':False,'proposed_next_parent_step':'Retain this MISS and root MISS; no delivery. If continuing Plane213, require a new targeted substantive hypothesis and immutable preset, not a recolor/width retry.','model_reasoning_limitations':reasoning})
manifest={p.relative_to(OWN).as_posix():sha(p) for p in sorted(OWN.rglob('*')) if p.is_file()}
save(OWN/'closing_artifact_sha256.json',manifest)
print(json.dumps({'unit':'u10_plane213_refine','question_id':'Plane213','preset':'B','finals':manual_finals,'two_hit':False,'candidate_count':0,'completed_calls':2,'source_files_unchanged':len(before),'own_API_requests':0},ensure_ascii=False))
