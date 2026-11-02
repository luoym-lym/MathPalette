import bootstrap
from bootstrap import OWNROOT,PROJECT,BASE
import json,hashlib,base64,gc
from pathlib import Path
from datetime import datetime,timezone
from dataset_tools.catalog import read,rows,content,digest

IDS=['Solid83','Solid85','Solid121','Solid130','Solid132','Solid151','Solid211','Solid221']
OUT=OWNROOT/'Solid151/face_center_inventory_to_core_confusion'
TEST=OUT/'tests/quicktest3_20261102T010639_9d5c932f0faf'
def shab(b):return hashlib.sha256(b).hexdigest()
def sha(p):return shab(p.read_bytes())
def save(p,obj,exclusive=True):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x' if exclusive else 'w',encoding='utf-8',newline='\n') as f:json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')

summary=read(TEST/'summary.json');binding=read(TEST/'binding.json')
assert summary['two_completed'] and len(summary['results'])==2
design_bytes=(OUT/'design.json').read_bytes();png=(OUT/'candidate.png').read_bytes()
assert (TEST/'design_snapshot.json').read_bytes()==design_bytes
assert shab(design_bytes)==binding['design_sha256'] and shab(png)==binding['image_sha256']
assert binding['expected_wrong_answer']=='E' and binding['requested_runs']==2
request=(TEST/'request.json').read_bytes();payload=json.loads(request)
assert shab(request)==binding['request_body_sha256']
assert set(payload)=={'model','stream','thinking','messages'}
assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
assert [m['role'] for m in payload['messages']]==['system','user']
assert payload['messages'][0]['content']==binding['system_prompt']
u=payload['messages'][1]['content']
assert [p['type'] for p in u]==['text','image_url'] and u[0]['text']==binding['question']
decoded=base64.b64decode(u[1]['image_url']['url'].split(',',1)[1]);assert decoded==png
del decoded,u,payload,png,request;gc.collect()
assert sha(PROJECT/'SolidGeometry/workbench/quick_test.py')==binding['reference_quick_test_sha256']

finals=[]
for i in [1,2]:
    response=TEST/f'run_{i:02d}_response.json';raw=response.read_bytes();j=json.loads(raw);body=j['choices'][0]['message']['content'];job=read(TEST/f'run_{i:02d}.json');start=read(TEST/f'run_{i:02d}_started.json')
    assert job['status']=='completed' and j['choices'][0]['finish_reason']=='stop'
    assert shab(raw)==job['response_sha256']
    assert start['request_body_sha256']==binding['request_body_sha256'] and start['image_sha256']==binding['image_sha256'] and start['design_sha256']==binding['design_sha256']
    finals.append({'run_index':i,'status':'completed','provider_finish_reason':'stop','full_final_body_manually_read':True,'full_final_body':body,'final_body_sha256':shab(body.encode()),'raw_response_path':str(response),'raw_response_sha256':shab(raw),'terminal_letter':'A','contradictory_letter_reference':i==1,'manual_hit_on_frozen_preset_E':False,'manual_reason':('Prose names diagram E but calls it Choice A and ends Final Answer A. Inconsistent final label mapping is explicitly ineligible as a preset E hit.' if i==1 else 'Concludes Choice A and final A. Reasoning miscounts face incidences and invents a typo, but it never gives frozen preset E as its final answer.')})
    del raw,j,body,job,start;gc.collect()
save(OUT/'manual_final_review.json',{'question_id':'Solid151','immutable_wrong_preset':'E','formal_correct_answer':'A','exactly_two_actual_complete_calls':True,'same_frozen_request_PNG_design':True,'no_retry_third_call_or_cherrypick':True,'new_independent_review_not_started':True,'finals':finals,'qualifying_doublehit':False,'disposition':'failed_predeclared_pair; do not retest unchanged or relabel preset','causal_limit':'No control pair or per-marker ablation was run; these two observations do not prove the intended center/core mechanism.'})
save(OWNROOT/'Solid151/assessment.json',{'question_id':'Solid151','stage':'material_refinement','status':'new_material_design_tested_pair_missed_preset','eligible':True,'original_and_formal_and_candidate_native_images_viewed':True,'fresh_noop_repeat_and_offline_replay_passed':True,'independent_math_audit':str(OWNROOT/'Solid151/primary_cube_identity_audit.json'),'unique_math_answer':'A','new_design':str(OUT),'wrong_preset':'E','new_api_calls':2,'qualifying_doublehit':False,'manual_disposition':'Run1 names E then maps it to ChoiceA/finalA; inconsistent, no E hit. Run2 finalA; no E hit.','new_vs_old_difference_audit':str(OUT/'design_difference_audit.json'),'every_marker_role':str(OUT/'marker_path_bindings.json'),'native_primary_review':str(OUT/'primary_native_visual_review.json'),'no_original_controls_or_causal_gain_hardgate':True,'new_independent_review_required_before_any_future_delivery':True,'no_reuse_or_old_preset_relabel':True})

old_manifest=read(OWNROOT/'audit/old_scope_file_manifest.json');old_bad=[]
for e in old_manifest:
    p=Path(e['path'])
    if not p.exists() or sha(p)!=e['sha256']:old_bad.append(str(p))
assert not old_bad
save(OWNROOT/'audit/old_frozen_evidence_terminal_integrity.json',{'checked_old_scope_files':len(old_manifest),'changed_or_missing':old_bad,'all_exact':not old_bad,'no_rewrite_or_restore_of_historical_files':True})

records={r['id']:r for r in rows(PROJECT/'SolidGeometry/dataset.jsonl')};approvals=read(PROJECT/'provenance/approvals.json')['approvals'];elig={};assessments={}
for q in IDS:
    r=records[q];c=content(PROJECT,'SolidGeometry',r);a=approvals[q];start=read(OWNROOT/q/'eligibility_start.json');sp=PROJECT/'SolidGeometry/special_variant'/q
    assert c==start['content'] and digest(c)==a['content_sha256'] and a['reviewer']=='user' and a['instruction']
    assert not (sp/'recipes.json').exists() and not (sp/'collection.json').exists()
    assert all(not [v for v in rows(sp.parent/n) if v['question_id']==q] for n in ['accepted_index.jsonl','collected_index.jsonl'])
    elig[q]={'source_dataset':r['source_dataset'],'source_key':r['source_key'],'current_approval_fingerprint_matches':True,'current_content_sha256':digest(c),'all_initial_source_hashes_still_exact':True,'no_passed_variant':True,'not_collected':True,'no_special_completion':True,'original_approval':a,'formal_record':r,'content_files':c['files']}
    assessments[q]=read(OWNROOT/q/'assessment.json')
save(OWNROOT/'audit/eligibility_terminal.json',elig)

mutable=[]
for e in read(OWNROOT/'audit/initial_snapshot_manifest.json'):
    if not e['mutable_parent_metadata']:continue
    old=Path(e['snapshot']).read_bytes();p=Path(e['source']);new=p.read_bytes()
    same=new==old;prefix=new.startswith(old)
    target=OWNROOT/'terminal_parent_snapshots'/p.name;target.parent.mkdir(exist_ok=True);target.write_bytes(new)
    mutable.append({'parent_path':str(p),'original_full_snapshot':e['snapshot'],'original_sha256_unchanged':e['sha256'],'original_snapshot_hash_still_exact':shab(old)==e['sha256'],'current_snapshot':str(target),'current_sha256':shab(new),'classification':'unchanged' if same else 'exact_prefix_parent_append' if prefix else 'parent_metadata_update_not_exact_prefix','exact_prefix':prefix,'appended_bytes':len(new)-len(old) if prefix else None,'role':'diagnostic mutable runtime metadata; never substituted for frozen source/design/PNG/request/raw or restored/rewritten'})
    del old,new;gc.collect()
save(OWNROOT/'audit/parent_metadata_terminal_classification.json',mutable)

frozen_paths=[OUT/n for n in ['design.json','plugin.json','candidate.png','context.json','design_difference_audit.json','marker_path_bindings.json','render_check.json','offline_replay_check.json','primary_native_visual_review.json','global_zero_prior_call_audit.json','eligibility_immediately_before_calls.json','manual_final_review.json']]+list(TEST.iterdir())
save(OWNROOT/'audit/new_frozen_evidence_terminal_manifest.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in frozen_paths if p.is_file()])
finished=read(OWNROOT/'api_process_finished.json');assert finished['runpy_returned_normally']
checkpoint={'unit':'background_76','stage':'material_refinement','status':'finite_scope_assessed_complete_no_qualifying_candidate','completed_at':datetime.now(timezone.utc).isoformat(),'question_ids':IDS,'actual_assessed_question_ids':IDS,'assessed_question_ids':IDS,'unworked_question_ids':[],'new_design_count':1,'new_actual_api_calls':2,'completed_actual_calls':2,'errors':[],'aborted_calls':0,'retried_calls':0,'owned_live_requests':0,'process_exit_evidence':'api_process_finished.json; final exact-PID/CIM closure audit follows','credible_primary_doublehits':0,'reasoned_skip_question_ids':[q for q in IDS if q!='Solid151'],'new_vs_old':'Solid151 face-center inventory/core confusion materially differs from old checkerboard-corner-toC. No old PNG/preset reused; old B/C,4/onlyposition4,2/6 remain misses.','current_eligibility_and_source_audits':elig,'question_assessments':assessments,'new_test_full_manual_finals':finals,'new_design_path':str(OUT),'harness_byte_diff_audit':'audit/harness_relocation_byte_diff_audit.json','global_zero_prior_call_audit':str(OUT/'global_zero_prior_call_audit.json'),'frozen_bindings_and_hash_manifest':'audit/new_frozen_evidence_terminal_manifest.json','old_evidence_hash_integrity':'audit/old_frozen_evidence_terminal_integrity.json','parent_metadata_classification':'audit/parent_metadata_terminal_classification.json','process_audit':{'API_pid':finished['pid'],'exact_original_runs':2,'normal_harness_completion':True,'no_child_API_processes':True,'strict_OWNROOT_guard':True,'thread_and_TEMP_cache_env_only_owned_processes':True,'system_env_dotenv_git_formal_approvals_Special_unchanged_by_worker':True,'no_nested_agents_threads_worktrees_servers_or_scope_expansion':True,'inherited_Codex_gpt_6_1_sol_ultra_unchanged':True},'local_diagnostics':[{'kind':'corrected_local_math_extractor_assertion_before_any_API','detail':'Solid130 canonical scene uses *_front/right/top_*_fill IDs, rather than generic face IDs. Corrected own extractor; independent exact-cover proof and exposed-color consistency now pass. Not an allocation/import/render/API failure.'}],'approval_delivery_state':'No self-independent review, original review, user approval, Pass, Collect, publication, delivery, or formal edits.','next_parent_action':'Read completed checkpoint. Queue is empty; no unchanged candidate retest or preset relabel.'}
save(OWNROOT/'checkpoint.json',checkpoint,exclusive=False)
save(OWNROOT/'second_review_queue.json',{'unit':'background_76','stage':'material_refinement','assessed_question_ids':IDS,'unworked_question_ids':[],'candidates':[],'credible_primary_doublehits':0,'tested_nonqualifying_candidate':{'question_id':'Solid151','path':str(OUT),'immutable_preset':'E','manual_review':str(OUT/'manual_final_review.json'),'outcomes':['contradictory prose E / ChoiceA, terminalA; no hit','terminalA; no hit'],'doublehit':False},'reasoned_skips':[{'question_id':q,'assessment_path':str(OWNROOT/q/'assessment.json'),'math_audit':assessments[q]['independent_math_audit']} for q in IDS if q!='Solid151'],'all_original_eligibility_and_source_hashes_rechecked':True,'evidence_manifest':'audit/new_frozen_evidence_terminal_manifest.json','checkpoint':'checkpoint.json','actual_new_api_calls':2,'owned_live_requests':0,'no_independent_second_review_performed':True,'independent_parent_delegate_review_required_for_any_future_doublehit_before_delivery':True},exclusive=False)
print(json.dumps({'assessed':8,'new_designs':1,'complete_calls':2,'qualifying_doublehits':0,'skips':7,'old_files_exact':len(old_manifest),'all_approval_source_hashes_exact':True,'checkpoint':str(OWNROOT/'checkpoint.json')}))
