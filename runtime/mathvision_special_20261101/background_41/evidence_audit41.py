from env41 import *
import base64,io
from PIL import Image
audits=[]
for q in ASSIGNED:
    for p in (HERE/q).glob('r41_*/tests/*/summary.json'):
        out=p.parents[2];b=read(p.parent/'binding.json');s=read(p);d=read(out/'design.json');request_bytes=(p.parent/'request.json').read_bytes();req=json.loads(request_bytes)
        image_bytes=base64.b64decode(req['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1]);record=eligibility(q)['formal_record']
        checks={'binding_image_hash':b['image_sha256']==file_hash(out/'candidate.png'),'embedded_png_exact':image_bytes==(out/'candidate.png').read_bytes(),'design_sha256':b['design_sha256']==file_hash(out/'design.json'),'design_snapshot_exact':(p.parent/'design_snapshot.json').read_bytes()==(out/'design.json').read_bytes(),'request_sha256':b['request_body_sha256']==hashlib.sha256(request_bytes).hexdigest(),'formal_question_exact':req['messages'][1]['content'][0]['text']==record['question'],'formal_record_sha256':b['question_record_sha256']==canonical_hash(record),'original_profile':req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'} and req['stream'] is False,'no_token_limit_or_timeout_payload':set(req)=={'model','stream','thinking','messages'},'preset_frozen':b['expected_wrong_answer']==d['expected_wrong_answer'],'exactly_two_requested':b['requested_runs']==2,'two_completed':s['two_completed'],'harness_source_bytes_equal':(HERE/'harness/quicktest3_isolated.py').read_bytes()==(BASE/'harness/quicktest3_isolated.py').read_bytes(),'system_prompt_reference_exact':b['system_prompt']==req['messages'][0]['content']}
        runs=[]
        for i in (1,2):
            j=read(p.parent/f'run_{i:02d}.json');r=read(p.parent/f'run_{i:02d}_response.json')
            runs.append({'run_index':i,'status':j['status'],'finish_reason':r['choices'][0]['finish_reason'],'response_sha256_matches':j['response_sha256']==file_hash(p.parent/f'run_{i:02d}_response.json'),'same_request':j['request_body_sha256']==b['request_body_sha256'],'same_image':j['image_sha256']==b['image_sha256'],'same_design':j['design_sha256']==b['design_sha256'],'model':r['model'],'started_at_utc':j['started_at'],'finished_at_utc':j['finished_at']})
        assert all(checks.values()),(q,checks)
        assert all(v['response_sha256_matches'] and v['same_request'] and v['same_image'] and v['same_design'] and v['status']=='completed' and v['finish_reason']=='stop' for v in runs)
        files={str(f.relative_to(HERE)):file_hash(f) for f in out.rglob('*') if f.is_file() and 'tmp' not in f.parts}
        audits.append({'question_id':q,'variant_id':d['variant_id'],'checks':checks,'binding_path':str(p.parent/'binding.json'),'summary_path':str(p),'runs':runs,'all_design_render_evidence_hashes':files,'no_solver_prompt_leakage':'Only exact existing solver system prompt, formal question, candidatePNG. No answer/preset/intent/original/control/parameters.'})
write(HERE/('evidence_audit_'+now().replace(':','').replace('.','')+'.json'),audits)
print(json.dumps({'complete_pairs_audited':len(audits),'all_checks_passed':True,'question_ids':[x['question_id'] for x in audits]}))
