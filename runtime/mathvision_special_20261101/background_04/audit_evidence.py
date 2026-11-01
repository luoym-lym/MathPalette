from research import *
import base64
def canonical(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
def audit_bindings(destination):
    rows=[]
    for binding in HERE.rglob('binding.json'):
        data=json.loads(binding.read_text(encoding='utf-8-sig'));folder=binding.parent
        image_path=Path(data['image_path']);design_path=Path(data['design_path'])
        request=(folder/'request.json').read_bytes();payload=json.loads(request)
        design=json.loads(design_path.read_text(encoding='utf-8-sig'))
        record=next(r for r in jsonl(ROOT/data['branch']/'dataset.jsonl') if r['id']==data['question_id'])
        expected=data['expected_wrong_answer']
        messages=payload['messages'];parts=messages[1]['content']
        outgoing_image=base64.b64decode(parts[1]['image_url']['url'].split(',',1)[1])
        from PIL import Image
        with Image.open(image_path) as img:
            img.load();pixel=hashlib.sha256(b'768x768:RGBA:'+img.convert('RGBA').tobytes()).hexdigest()
            size_ok=img.size==(768,768)
        checks={
            'design_sha256':digest(design_path)==data['design_sha256'],
            'design_snapshot_byte_identical':(folder/'design_snapshot.json').read_bytes()==design_path.read_bytes(),
            'image_sha256':digest(image_path)==data['image_sha256'],
            'pixel_sha256':pixel==data['pixel_sha256'],
            'canvas_768':size_ok,
            'request_body_sha256':hashlib.sha256(request).hexdigest()==data['request_body_sha256'],
            'model_thinking_exact':payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'},
            'no_settings_overrides':set(payload)=={'model','stream','thinking','messages'} and payload['stream'] is False,
            'two_message_request':len(messages)==2 and messages[0]['role']=='system' and messages[1]['role']=='user',
            'original_system_prompt_exact':messages[0]['content']==data['system_prompt'],
            'formal_question_exact':parts[0]=={'type':'text','text':record['question']} and data['question']==record['question'],
            'only_question_and_candidate':len(parts)==2 and parts[1]['type']=='image_url' and outgoing_image==image_path.read_bytes(),
            'immutable_preset_matches_design':str(design.get('expected_wrong_answer'))==str(expected),
            'preset_differs_from_correct':str(expected).strip()!=str(record['answer']).strip(),
            'formal_record_hash':canonical(record)==data['question_record_sha256'],
            'formal_dataset_hash':digest(ROOT/data['branch']/'dataset.jsonl')==data['dataset_sha256'],
        }
        responses=[]
        for p in sorted(folder.glob('run_??.json')):
            job=json.loads(p.read_text(encoding='utf-8-sig'));run=int(job['run_index'])
            checks[f'run_{run}_request_image_design_binding']=all(job.get(k)==data[k] for k in ['request_body_sha256','image_sha256','design_sha256'])
            if job.get('status')=='completed':
                raw=folder/f'run_{run:02d}_response.json'
                checks[f'run_{run}_raw_response_hash']=raw.is_file() and digest(raw)==job['response_sha256']
                checks[f'run_{run}_complete_not_truncated']=not job.get('truncated') and job.get('finish_reason')!='length' and bool(job.get('answer','').strip())
            responses.append({'run_index':run,'status':job.get('status'),'finish_reason':job.get('finish_reason'),'truncated':job.get('truncated'),'final_answer_text':job.get('answer',job.get('text',job.get('content'))),'job_path':str(p)})
        aborted=[str(p) for p in folder.glob('*aborted*.json')]
        rows.append({'question_id':data['question_id'],'preset':expected,'binding_path':str(binding),'checks':checks,'all_checks_pass':all(checks.values()),'runs':responses,'aborted_evidence':aborted})
    result={'checked_at':datetime.now(timezone.utc).isoformat(),'invocation_count':len(rows),'all_checks_pass':all(r['all_checks_pass'] for r in rows),'invocations':rows}
    write(HERE/destination,result)
    print(json.dumps({'invocation_count':len(rows),'all_checks_pass':result['all_checks_pass'],'path':str(HERE/destination)},ensure_ascii=False))
if __name__=='__main__':audit_bindings(sys.argv[1])
