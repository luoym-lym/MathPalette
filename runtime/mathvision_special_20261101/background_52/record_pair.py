from audit_io import install,OWN,PROJECT,load,save,sha
install()
import sys,json,base64,hashlib
from datetime import datetime,timezone

qid=sys.argv[1];finals=sys.argv[2:]
assert len(finals)==2
folder=next((OWN/qid).glob('r52_*'));design=folder/'design.json';d=load(design)
summary=next((folder/'tests').glob('*/summary.json'));s=load(summary);binding=load(summary.parent/'binding.json')
assert s['two_completed'] and s['requested_runs']==2
assert binding['image_sha256']==sha(folder/'candidate.png')==d['image_sha256']
assert binding['design_sha256']==sha(design)==sha(summary.parent/'design_snapshot.json')
assert d['expected_wrong_answer']==binding['expected_wrong_answer']
request=summary.parent/'request.json';payload=load(request)
assert sha(request)==binding['request_body_sha256']
record=load(OWN/qid/'formal_record.json')
assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'}
assert set(payload)=={'model','stream','thinking','messages'}
assert payload['messages'][0]=={'role':'system','content':binding['system_prompt']}
assert payload['messages'][1]['role']=='user'
content=payload['messages'][1]['content']
assert len(content)==2 and content[0]=={'type':'text','text':record['question']}
assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==(folder/'candidate.png').read_bytes()
responses=[]
for i,final in enumerate(finals,1):
    p=summary.parent/f'run_{i:02}_response.json';raw=load(p);job=load(summary.parent/f'run_{i:02}.json')
    assert job['status']=='completed' and sha(p)==job['response_sha256']
    assert job['request_body_sha256']==binding['request_body_sha256']
    assert job['image_sha256']==binding['image_sha256'] and job['design_sha256']==binding['design_sha256']
    assert raw['choices'][0]['finish_reason']=='stop'
    responses.append({'run':i,'manually_read_complete_raw_final':True,'manual_final_answer':final,'full_final_body':raw['choices'][0]['message']['content'],'raw_path':str(p),'raw_sha256':sha(p),'job_path':str(summary.parent/f'run_{i:02}.json'),'job_sha256':sha(summary.parent/f'run_{i:02}.json'),'finish_reason':'stop','matches_unchanged_preset':final.strip()==str(d['expected_wrong_answer']).strip()})
hit=all(r['matches_unchanged_preset'] for r in responses)
review={'question_id':qid,'variant_id':d['variant_id'],'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'background_52 primary worker, manually selected full terminal answers','independent_second_review':False,'immutable_wrong_preset':d['expected_wrong_answer'],'manual_final_answers':finals,'full_response_reviews':responses,'exact_frozen_bindings_verified':True,'exact_two_calls_only':True,'solver_input_only_formal_question_and_same_PNG':True,'profile_systemprompt_APIconfig_unmodified':True,'summary_path':str(summary),'binding_path':str(summary.parent/'binding.json'),'request_path':str(request),'request_sha256':sha(request),'design_path':str(design),'design_sha256':sha(design),'image_path':str(folder/'candidate.png'),'image_sha256':sha(folder/'candidate.png'),'pretest_primary_review':str(folder/'primary_review_before_calls.json'),'possible_primary_two_hit':hit,'status':'possible_candidate_requires_NEW_parent_second_review' if hit else 'MISS_of_original_unchanged_preset','no_preset_or_image_change_after_response':True,'controls':[],'limits':['Two calls do not establish statistical reliability or incremental original-image gain.','No mechanism-faithfulness, human prevalence or per-marker causal claim.','Even matching wrong finals are a MISS if they differ from the frozen preset.']}
save(folder/'manual_final_review.json',review)
print(json.dumps({'qid':qid,'preset':d['expected_wrong_answer'],'manual_finals':finals,'possible_candidate':hit},ensure_ascii=False))
