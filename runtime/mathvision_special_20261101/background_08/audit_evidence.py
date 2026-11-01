from tools08 import *
import base64
audits=[]
for binding in sorted(HERE.glob('Plane*/*/tests/quicktest3_*/binding.json')):
    folder=binding.parent;candidate=folder.parent.parent;b=json.loads(binding.read_text(encoding='utf-8'));d=json.loads((candidate/'design.json').read_text(encoding='utf-8'));qid=b['question_id']
    request=(folder/'request.json').read_bytes();payload=json.loads(request)
    record=json.loads((HERE/qid/'formal_record.json').read_text(encoding='utf-8'))
    checks={'image_sha256':file_hash(candidate/'candidate.png')==b['image_sha256'],'design_sha256':file_hash(candidate/'design.json')==b['design_sha256'],'design_snapshot_byte_identical':(candidate/'design.json').read_bytes()==(folder/'design_snapshot.json').read_bytes(),'request_sha256':hashlib.sha256(request).hexdigest()==b['request_body_sha256'],'preset_frozen_unchanged':d['expected_wrong_answer']==b['expected_wrong_answer'],'requested_runs_exact_two':b['requested_runs']==2,'correct_model':payload['model']=='mimo-v2.6-flash','thinking_disabled':payload['thinking']=={'type':'disabled'},'no_token_or_timeout_overrides':not any(k in payload for k in ['max_tokens','max_completion_tokens','timeout']),'only_exact_formal_question_and_image':len(payload['messages'])==2 and payload['messages'][1]['content'][0]=={'type':'text','text':record['question']} and len(payload['messages'][1]['content'])==2,'request_image_byte_identical':base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(candidate/'candidate.png').read_bytes(),'same_existing_system_prompt':payload['messages'][0]=={'role':'system','content':b['system_prompt']}}
    runs=[]
    for n in (1,2):
        p=folder/f'run_{n:02d}.json';start=folder/f'run_{n:02d}_started.json'
        if not p.exists():
            runs.append({'run':n,'state':'started_incomplete' if start.exists() else 'not_started'});continue
        r=json.loads(p.read_text(encoding='utf-8'));rr=folder/f'run_{n:02d}_response.json';ok=r['image_sha256']==b['image_sha256'] and r['design_sha256']==b['design_sha256'] and r['request_body_sha256']==b['request_body_sha256']
        if r['status']=='completed':ok=ok and file_hash(rr)==r['response_sha256'] and not r.get('truncated') and r.get('finish_reason')=='stop'
        checks['run_'+str(n)+'_binding']=ok;runs.append({'run':n,'state':r['status'],'response_sha256':file_hash(rr) if rr.exists() else None,'run_record_sha256':file_hash(p)})
    assert all(checks.values()),(str(folder),checks)
    audits.append({'question_id':qid,'variant_id':candidate.name,'evidence_dir':str(folder),'binding_sha256':file_hash(binding),'checks':checks,'runs':runs,'preset':d['expected_wrong_answer']})
write(HERE/(sys.argv[1] if len(sys.argv)>1 else 'evidence_binding_audit.json'),{'audited_at':now(),'all_completed_evidence_checks_passed':True,'invocations':audits,'raw_evidence_not_modified':True,'note':'Pending/aborted transport states are explicitly listed and are not valid paired evidence. No automatic retry or response selection is performed.'})
print(json.dumps({'invocations_checked':len(audits),'all_bindings_valid':True}))
