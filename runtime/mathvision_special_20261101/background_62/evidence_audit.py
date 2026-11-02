from bootstrap import install,OWN,PROJECT,SESSION
install()
from gates import sha,load,save,now
import json,sys,base64,hashlib
from pathlib import Path

def audit(q,complete=False):
    item=next(x for x in load(SESSION/'background_62_assignment.json')['questions'] if x['question_id']==q)
    d=OWN/q/item['variant_id'];inv=next((d/'tests').glob('quicktest3_*'))
    binding=load(inv/'binding.json');req=load(inv/'request.json')
    row=load(OWN/q/'qualification_immediately_before_API.json')['formal_record']
    assert sha(inv/'request.json')==binding['request_body_sha256']
    assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'} and req['stream'] is False
    assert set(req)=={'model','stream','thinking','messages'}
    assert len(req['messages'])==2 and req['messages'][0]=={'role':'system','content':binding['system_prompt']}
    assert req['messages'][1]['role']=='user'
    c=req['messages'][1]['content'];assert len(c)==2 and c[0]=={'type':'text','text':row['question']}
    assert c[1]['type']=='image_url'
    image=base64.b64decode(c[1]['image_url']['url'].split(',',1)[1],validate=True)
    imagehash=hashlib.sha256(image).hexdigest();assert image==(d/'candidate.png').read_bytes()
    del image,req
    assert imagehash==item['PNG_sha256']==binding['image_sha256']
    assert sha(d/'design.json')==binding['design_sha256']==sha(inv/'design_snapshot.json')
    assert binding['expected_wrong_answer']==item['expected_wrong_answer'] and binding['requested_runs']==2
    results=[]
    for start in sorted(inv.glob('run_*_started.json')):
        r=load(start);i=r['run_index']
        assert r['image_sha256']==imagehash and r['request_body_sha256']==binding['request_body_sha256']
        result=inv/f'run_{i:02d}.json';raw=inv/f'run_{i:02d}_response.json'
        record={'run_index':i,'started_path':str(start),'started_sha256':sha(start),'result_path':str(result) if result.exists() else None}
        if result.exists():
            rr=load(result);record.update({'status':rr['status'],'finish_reason':rr.get('finish_reason'),'truncated':rr.get('truncated'),'result_sha256':sha(result)})
            if raw.exists():
                assert sha(raw)==rr['response_sha256']
                rd=load(raw);assert rd['choices'][0]['message']['content']==rr['answer']
                record.update({'raw_path':str(raw),'raw_sha256':sha(raw),'full_answer':rr['answer'],'response_model':rd.get('model')})
            if complete:assert rr['status']=='completed' and rr['finish_reason']=='stop' and not rr['truncated']
        results.append(record)
    if complete:assert len(results)==2 and load(inv/'summary.json')['two_completed']
    audit={'at':now(),'question_id':q,'variant_id':item['variant_id'],'evidence_dir':str(inv),'binding_sha256':sha(inv/'binding.json'),'request_sha256':binding['request_body_sha256'],'frozen_image_sha256':imagehash,'frozen_design_sha256':binding['design_sha256'],'frozen_plugin_sha256':sha(d/'plugin.json'),'copied_source_hashes_exact':True,'payload_only_existing_system_prompt_formal_question_identical_PNG':True,'no_answer_preset_intent_params_history_sent':True,'unchanged_profile_no_timeout_tokens_retry_override':True,'results':results,'complete_audit':complete}
    save(d/('complete_evidence_audit.json' if complete else 'request_audit.json'),audit)
    print(json.dumps(audit,ensure_ascii=False,indent=2))

if __name__=='__main__':audit(sys.argv[1],len(sys.argv)>2 and sys.argv[2]=='complete')
