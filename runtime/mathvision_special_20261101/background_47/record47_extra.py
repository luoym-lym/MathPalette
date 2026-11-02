from env47 import *
import json
import base64
from datetime import datetime,timezone
from inspect47 import eligibility,BRANCH

def main():
    qid=sys.argv[1];answers=sys.argv[2].split(',');note=sys.argv[3]
    assert len(answers)==2
    root=OWN/qid/'r47_equal_legs_triangle_area_to_square';assert qid=='Plane456'
    summaries=list((root/'tests').glob('*/summary.json'));assert len(summaries)==1
    invocation=summaries[0].parent
    b=json.loads((invocation/'binding.json').read_text(encoding='utf-8'))
    summary=json.loads(summaries[0].read_text(encoding='utf-8'))
    d=json.loads((root/'design.json').read_text(encoding='utf-8'))
    request=json.loads((invocation/'request.json').read_text(encoding='utf-8'))
    e=eligibility(qid);assert e['eligible']
    assert summary['two_completed']
    checks={
      'candidate_sha_matches_binding_and_design':sha(root/'candidate.png')==b['image_sha256']==d['image_sha256'],
      'design_sha_matches_binding_and_snapshot':sha(root/'design.json')==b['design_sha256']==sha(invocation/'design_snapshot.json'),
      'design_snapshot_byte_equal':(root/'design.json').read_bytes()==(invocation/'design_snapshot.json').read_bytes(),
      'request_sha_matches_binding':sha(invocation/'request.json')==b['request_body_sha256'],
      'image_bytes_equal_embedded_png':base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(root/'candidate.png').read_bytes(),
      'formal_question_exact':request['messages'][1]['content'][0]['text']==e['record']['question']==b['question'],
      'only_formal_question_and_image_in_user_message':len(request['messages'][1]['content'])==2,
      'payload_keys_exact':set(request)=={'model','stream','thinking','messages'},
      'model_and_thinking_exact':request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False,
      'reference_system_prompt_exact':request['messages'][0]=={'role':'system','content':b['system_prompt']},
      'reference_quick_test_unchanged':sha(BRANCH/'workbench/quick_test.py')==b['reference_quick_test_sha256'],
      'preset_frozen_and_wrong':str(d['expected_wrong_answer'])==str(b['expected_wrong_answer'])!=str(e['record']['answer']),
      'exactly_two_starts_and_responses':len(list(invocation.glob('run_*_started.json')))==2 and len(list(invocation.glob('run_*_response.json')))==2,
      'no_error_or_incomplete_artifact':not list(invocation.glob('*incomplete*')),
      'preset_and_difference_and_png_precede_both_calls':max((root/n).stat().st_mtime_ns for n in ['design.json','design_difference_audit.json','candidate.png'])<min((invocation/f'run_{i:02d}_started.json').stat().st_mtime_ns for i in [1,2])
    }
    assert all(checks.values()),checks
    manual=[]
    for i,answer in enumerate(answers,1):
        rawp=invocation/f'run_{i:02d}_response.json';runp=invocation/f'run_{i:02d}.json'
        raw=json.loads(rawp.read_text(encoding='utf-8'));run=json.loads(runp.read_text(encoding='utf-8'))
        full=raw['choices'][0]['message']['content']
        assert run['status']=='completed' and raw['choices'][0]['finish_reason']=='stop'
        assert run['response_sha256']==sha(rawp)
        assert run['request_body_sha256']==b['request_body_sha256'] and run['image_sha256']==b['image_sha256'] and run['design_sha256']==b['design_sha256']
        manual.append({'run_index':i,'full_final_text':full,'manually_read_complete_raw_final':True,'manual_final_answer':answer,'matches_predeclared_wrong_answer':str(answer)==str(d['expected_wrong_answer']),'matches_formal_answer':str(answer)==str(e['record']['answer']),'contradictory_final_letter_value_pair':False,'status':'completed','finish_reason':'stop','raw_response_path':str(rawp),'raw_response_sha256':sha(rawp),'run_record_path':str(runp),'run_record_sha256':sha(runp)})
    hits=sum(x['matches_predeclared_wrong_answer'] for x in manual)
    possible=hits==2
    result={'question_id':qid,'variant_id':d['variant_id'],'reviewed_at':datetime.now(timezone.utc).isoformat(),'preset':d['expected_wrong_answer'],'formal_correct_answer':e['record']['answer'],'manual_final_answers':answers,'full_manual_finals':manual,'manual_notes':note,'preset_hit_count':hits,'two_complete_hits':possible,'possible_candidate_for_parent_NEW_independent_review':possible,'status':'possible_twohit_primary_only' if possible else 'MISS','binding_checks':checks,'binding_path':str(invocation/'binding.json'),'summary_path':str(summaries[0]),'request_path':str(invocation/'request.json'),'request_sha256':sha(invocation/'request.json'),'image_path':str(root/'candidate.png'),'image_sha256':sha(root/'candidate.png'),'design_path':str(root/'design.json'),'design_sha256':sha(root/'design.json'),'original_control_calls':0,'limitations':['Two observations do not prove a mechanism, causal gain or statistical benefit.','No same-image retries, changed presets, selected successes or paired different images.','No independent second review, approval, Pass/Collect or publication performed.']}
    dump(root/'manual_final_review.json',result)
    dump(root/'eligibility_after_calls.json',e)
    print(json.dumps({'qid':qid,'answers':answers,'preset':d['expected_wrong_answer'],'hits':hits,'possible':possible},ensure_ascii=False))

if __name__=='__main__':main()
