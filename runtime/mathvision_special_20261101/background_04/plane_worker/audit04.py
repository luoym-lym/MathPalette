from tools04 import *
import base64
def audit():
    inputs_before={}
    for qid in ASSIGNED:
        for k,v in json.loads((HERE/qid/'input_fingerprints.json').read_text(encoding='utf-8')).items():
            if k in inputs_before:assert inputs_before[k]==v
            inputs_before[k]=v
    changed=[k for k,v in inputs_before.items() if not (ROOT/k).is_file() or file_hash(ROOT/k)!=v]
    evidence=[]
    for binding_path in HERE.glob('**/tests/*/binding.json'):
        folder=binding_path.parent;b=json.loads(binding_path.read_text(encoding='utf-8'))
        imagepath=Path(b['image_path']);designpath=Path(b['design_path']);request=(folder/'request.json').read_bytes();payload=json.loads(request)
        record=next(r for r in rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']==b['question_id'])
        content=payload['messages'][1]['content']
        checks={'image_hash':file_hash(imagepath)==b['image_sha256'],'design_hash':file_hash(designpath)==b['design_sha256'],'snapshot':(folder/'design_snapshot.json').read_bytes()==designpath.read_bytes(),'request_hash':hashlib.sha256(request).hexdigest()==b['request_body_sha256'],'formal_question_exact':content[0]=={'type':'text','text':record['question']},'only_question_and_image_user_blocks':len(content)==2 and content[1]['type']=='image_url','image_bytes_exact':base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==imagepath.read_bytes(),'exact_payload_keys':set(payload)=={'model','stream','thinking','messages'},'model':payload['model']=='mimo-v2.6-flash','thinking_disabled':payload['thinking']=={'type':'disabled'},'only_system_and_user_messages':len(payload['messages'])==2 and payload['messages'][0]=={'role':'system','content':b['system_prompt']}}
        run_checks=[]
        for run_path in folder.glob('run_??.json'):
            run=json.loads(run_path.read_text(encoding='utf-8'));raw=folder/(run_path.stem+'_response.json')
            run_checks.append({'path':str(run_path.relative_to(ROOT)),'status':run['status'],'completed':run['status']=='completed' and not run.get('truncated'),'bound_image':run['image_sha256']==b['image_sha256'],'bound_design':run['design_sha256']==b['design_sha256'],'bound_request':run['request_body_sha256']==b['request_body_sha256'],'response_hash':raw.exists() and file_hash(raw)==run.get('response_sha256')})
        evidence.append({'binding_path':str(binding_path.relative_to(ROOT)),'checks':checks,'runs':run_checks,'paired_completed':len(run_checks)==2 and all(c['completed'] for c in run_checks),'all_checks_pass':all(checks.values()) and all(all(v for k,v in c.items() if k not in {'path','status'}) for c in run_checks)})
    out={'checked_at':datetime.now(timezone.utc).isoformat(),'formal_input_files_checked':len(inputs_before),'formal_inputs_changed':changed,'all_frozen_inputs_unchanged':not changed,'evidence':evidence,'all_available_evidence_bindings_pass':all(r['all_checks_pass'] for r in evidence),'scope':'Only worker-assigned Plane questions and own new evidence. No independent second review performed.'}
    write(HERE/(sys.argv[1] if len(sys.argv)>1 else 'evidence_binding_audit.json'),out)
    print(json.dumps({'checked_files':len(inputs_before),'changed':changed,'bindings':len(evidence),'all_bindings_pass':out['all_available_evidence_bindings_pass']},ensure_ascii=False))
if __name__=='__main__':audit()
