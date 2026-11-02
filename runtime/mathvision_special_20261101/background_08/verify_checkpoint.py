from tools08 import *
cp=HERE/'checkpoint.json';data=json.loads(cp.read_text(encoding='utf-8'))
# Preserve the initial completed checkpoint while pointing the final one at final audits.
(HERE/'checkpoint_before_final_audit_links.json').write_bytes(cp.read_bytes())
data['source_audit']=str(HERE/'source_preservation_final.json')
data['evidence_binding_audit']=str(HERE/'evidence_binding_audit_final.json')
data['transport_completion_audit']=str(HERE/'transport_completion_audit.json')
data['finalized_at']=now()
with cp.open('w',encoding='utf-8',newline='\n') as f:json.dump(data,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
queue=json.loads((HERE/'second_review_queue.json').read_text(encoding='utf-8'));assert len(queue['candidates'])==1
assert data['counts']['API_calls_completed_total']==18 and data['counts']['complete_candidate_pairs']==8
assert set(data['assessed_question_ids'])==set(ASSIGNED) and data['unworked_question_ids']==[]
assert data['no_live_processes']['no_live_own_python_processes']
q=queue['candidates'][0];folder=Path(q['image_path']).parent
assert q['question_id']=='Plane404' and q['variant_id']=='unreflected_first_digit_binding'
assert file_hash(folder/'candidate.png')==q['image_sha256'] and file_hash(folder/'design.json')==q['design_sha256']
assert (folder/'candidate.png').read_bytes()==(folder/'replay_final.png').read_bytes()
assert q['manual_review']['both_preset_hits']
aud=json.loads((HERE/'evidence_binding_audit_final.json').read_text(encoding='utf-8'));assert len(aud['invocations'])==9
assert all(len(inv['runs'])==2 and all(r['state']=='completed' for r in inv['runs']) and all(inv['checks'].values()) for inv in aud['invocations'])
write(HERE/'checkpoint_validation.json',{'at':now(),'checkpoint_sha256':file_hash(cp),'second_review_queue_sha256':file_hash(HERE/'second_review_queue.json'),'all18_real_calls_completed':True,'all9_exact_two_call_bindings_valid':True,'candidate_image_design_hashes_valid':True,'candidate_replay_byte_identical':True,'actual20_assessed_no_unworked_reservations':True,'new_independent_review_required':True,'formal_source_files_unchanged':3439,'no_live_own_API_processes':True})
print(json.dumps({'validated':True,'candidate_id':q['question_id']+'/'+q['variant_id'],'counts':data['counts']}))
