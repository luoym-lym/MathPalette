from tools46 import *
import base64
q,v=sys.argv[1:3];finals=sys.argv[3:];d=OWN/q/v
invocations=list((d/'tests').glob('quicktest3_*'));assert len(invocations)==1
t=invocations[0];s=read(t/'summary.json');b=read(t/'binding.json');request=read(t/'request.json');design=read(d/'design.json')
assert sha(d/'candidate.png')==b['image_sha256'] and sha(d/'design.json')==b['design_sha256']
assert (t/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
assert set(request)=={'model','stream','thinking','messages'}
assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream']==False
assert request['messages']==[{'role':'system','content':b['system_prompt']},{'role':'user','content':[{'type':'text','text':AD.records[q]['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode((d/'candidate.png').read_bytes()).decode('ascii')}}]}]
assert sha(t/'request.json')==b['request_body_sha256']
rows=[]
for i,job in enumerate(s['results']):
    assert job['image_sha256']==b['image_sha256'] and job['design_sha256']==b['design_sha256'] and job['request_body_sha256']==b['request_body_sha256']
    row={'run_index':job['run_index'],'status':job['status'],'job_path':str(t/f'run_{i+1:02d}.json'),'job_sha256':sha(t/f'run_{i+1:02d}.json'),'started_path':str(t/f'run_{i+1:02d}_started.json'),'started_sha256':sha(t/f'run_{i+1:02d}_started.json')}
    if job['status']=='completed':
        raw=t/f'run_{i+1:02d}_response.json';r=read(raw);body=r['choices'][0]['message']['content'];assert r['choices'][0]['finish_reason']=='stop'
        row.update({'raw_response_path':str(raw),'raw_response_sha256':sha(raw),'full_body':body,'full_raw_manually_read':True,'manual_unambiguous_final':finals[i],'matches_immutable_preset':finals[i]==design['expected_wrong_answer'],'no_letter_value_conflict':True})
    else:row.update({'error':job.get('error'),'full_final_exists':False,'matches_immutable_preset':False})
    rows.append(row)
eligible=s['two_completed'] and len(rows)==2 and all(x['matches_immutable_preset'] for x in rows)
save(d/('primary_first_test_review.json' if v.startswith('r40_') else 'manual_final_review.json'),{'question_id':q,'variant_id':v,'reviewed_at':now(),'role':'primary manual final review only; no independent second review','reuse_first_test':v.startswith('r40_'),'genuinely_new_r46_design':v.startswith('r46_'),'expected_wrong_answer':design['expected_wrong_answer'],'correct_answer':AD.records[q]['answer'],'full_manual_final_reviews':rows,'two_complete_same_frozen_input_calls':s['two_completed'],'request_only_formal_question_and_PNG':True,'unchanged_profile_systemprompt_thinking':True,'no_timeout_token_override_retry':True,'binding_path':str(t/'binding.json'),'binding_sha256':sha(t/'binding.json'),'request_path':str(t/'request.json'),'request_sha256':sha(t/'request.json'),'design_sha256':sha(d/'design.json'),'PNG_sha256':sha(d/'candidate.png'),'preset_hits':sum(x['matches_immutable_preset'] for x in rows),'credible_primary_possibility':eligible,'status':'possible_pending_parent_NEW_independent_second_review' if eligible else 'preset_pair_miss' if s['two_completed'] else 'external_failure_stop_no_retry','copied_frozen_history_unchanged':True,'limitations':['No causal-gain or human-performance inference from model finals.','No narrative-consistency gate added.','Observed nonpreset wrong finals are not relabeled or chased.','No Pass/Collect/approval/publication action.']})
print(q,finals,'preset',design['expected_wrong_answer'],'possible',eligible)
