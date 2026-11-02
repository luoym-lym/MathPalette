from env56 import *
import base64
qid=sys.argv[1]
manuals={
'Plane354': [('20','20',False,'Both complete finals explicitly derive72 and18 degrees and answer20; the many intermediate mentions of5 are not terminal preset5 hits.'),('20','20',False,'Full final ends20 consistently after the same correct72/18-degree derivation; no copying of the five-copy source role observed.')],
}
if len(sys.argv)>2:
    manuals[qid]=read(Path(sys.argv[2]))
c=next(x for x in read(OWN/'prepared_candidates.json') if x['question_id']==qid)
p=Path(c['path'])
ev=list((p/'tests').glob('quicktest3_*'))
assert len(ev)==1
ev=ev[0];b=read(ev/'binding.json');s=read(ev/'summary.json');req=read(ev/'request.json');d=read(p/'design.json')
assert s['two_completed']
assert b['design_sha256']==sha(p/'design.json')==c['design_sha256']
assert b['image_sha256']==sha(p/'candidate.png')==c['image_sha256']
assert (ev/'design_snapshot.json').read_bytes()==(p/'design.json').read_bytes()
assert sha(ev/'request.json')==b['request_body_sha256']
assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'}
assert set(req)=={'model','stream','thinking','messages'}
assert len(req['messages'])==2 and req['messages'][0]=={'role':'system','content':b['system_prompt']}
assert req['messages'][1]['content'][0]=={'type':'text','text':read(OWN/qid/'formal_record.json')['question']}
assert len(req['messages'][1]['content'])==2
url=req['messages'][1]['content'][1]['image_url']['url']
assert base64.b64decode(url.split(',',1)[1])==(p/'candidate.png').read_bytes()
review=[]
for i,(letter,value,hit,note) in enumerate(manuals[qid],1):
    raw=read(ev/f'run_{i:02d}_response.json');job=read(ev/f'run_{i:02d}.json');ch=raw['choices'][0]
    assert ch['finish_reason']=='stop' and job['status']=='completed'
    assert sha(ev/f'run_{i:02d}_response.json')==job['response_sha256']
    review.append({'run_index':i,'raw_response_path':str(ev/f'run_{i:02d}_response.json'),'raw_response_sha256':job['response_sha256'],'complete_final_text':ch['message']['content'],'complete_final_manually_read':True,'manual_final_letter_or_number':letter,'manual_final_value':value,'preset_hit':hit,'manual_notes':note,'request_sha256':job['request_body_sha256'],'image_sha256':job['image_sha256'],'design_sha256':job['design_sha256']})
save(p/'manual_full_final_review.json',{'question_id':qid,'variant_id':c['variant_id'],'at':now(),'immutable_predeclared_wrong_answer':d['expected_wrong_answer'],'correct_answer':d['correct_answer'],'runs':review,'exact_two_complete_frozen_calls':True,'two_preset_hits':all(r['preset_hit'] for r in review),'not_independent_second_review':True})
save(p/'evidence_binding_audit.json',{'at':now(),'question_id':qid,'variant_id':c['variant_id'],'binding_path':str(ev/'binding.json'),'binding_sha256':sha(ev/'binding.json'),'summary_path':str(ev/'summary.json'),'summary_sha256':sha(ev/'summary.json'),'request_path':str(ev/'request.json'),'request_sha256':sha(ev/'request.json'),'design_sha256':sha(p/'design.json'),'plugin_sha256':sha(p/'plugin.json'),'image_sha256':sha(p/'candidate.png'),'same_design_snapshot':True,'exact_only_formal_question_and_candidatePNG_plus_original_system_prompt':True,'original_model_profile_thinking_disabled_no_overrides':True,'two_stop_completed':True,'full_finals_manually_reviewed':True,'no_extra_test_control_ping_retry':True,'no_independent_review_or_approval':True})
print(qid,'manual review saved; preset hits',[r['preset_hit'] for r in review])
