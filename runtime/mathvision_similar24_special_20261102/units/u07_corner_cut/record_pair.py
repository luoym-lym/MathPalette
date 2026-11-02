from worker_env import *
import argparse
import re

p=argparse.ArgumentParser();p.add_argument('question',choices=['Plane194','Plane245']);p.add_argument('variant');p.add_argument('finals');a=p.parse_args()
assert re.fullmatch('[A-E],[A-E]',a.finals)
final_letters=a.finals.split(',');directory=OWN/a.question/a.variant
assert directory.is_relative_to(OWN/a.question)
invocations=list((directory/'tests').glob('quicktest3_*'));assert len(invocations)==1
invocation=invocations[0];summary=read(invocation/'summary.json');assert summary['two_completed']
values={'Plane194':{'A':'Four original exterior corners clipped','B':'Top/bottom V notches','C':'One central diamond aperture','D':'Left/right V notches','E':'One central axis-aligned square aperture'},
        'Plane245':{'A':'Intact square with a central axis-aligned square aperture','B':'Intact square with a central diamond aperture','C':'Outer diamond with no hole','D':'Cross outline with no hole','E':'Cross outline plus central diamond aperture'}}
finals=[]
for index,(result,letter) in enumerate(zip(summary['results'],final_letters),1):
    rawpath=invocation/f'run_{index:02d}_response.json';raw=read(rawpath)
    msg=raw['choices'][0]['message']['content'];assert msg==result['answer']
    assert raw['choices'][0]['finish_reason']=='stop' and not result['truncated']
    tail=msg[-300:]
    assert re.search(r'(?<![A-Za-z])'+letter+r'(?![A-Za-z])',tail)
    assert sha(rawpath)==result['response_sha256']
    hit=letter==summary['expected_wrong_answer']
    finals.append({'run_index':index,'complete_answer':msg,'manual_final_letter':letter,
       'manual_final_value':values[a.question][letter],'complete_nontruncated':True,'hit_letter_and_value':hit,
       'raw_path':str(rawpath),'raw_response_sha256':sha(rawpath)})
paired=all(f['hit_letter_and_value'] for f in finals)
review={'reviewed_at':now(),'question_id':a.question,'variant_id':a.variant,'review_scope':'PRIMARY manual complete raw and final reading',
 'frozen_expected_wrong_answer':summary['expected_wrong_answer'],'manual_finals':finals,'both_match_frozen_preset':paired,
 'two_complete_original_quicktest3_calls':True,'summary_path':str(invocation/'summary.json'),
 'binding_sha256':sha(invocation/'binding.json'),'design_snapshot_matches':sha(invocation/'design_snapshot.json')==sha(directory/'design.json'),
 'request_body_matches':sha(invocation/'request.json')==summary['request_body_sha256'],
 'status':'PRIMARY_TWO_HIT_REQUIRES_NEW_PARENT_REVIEW' if paired else 'PAIR_MISS_DO_NOT_RETEST_IDENTICAL_INPUT',
 'note':'Full final statements are read manually; incidental intermediate errors or other wrong letters do not count. No third call, chosen pair or changed preset. Primary only, no approval or delivery.'}
write(directory/'manual_final_review.json',review,True)
checkpoint=read(OWN/'checkpoint.json');checkpoint['updated_at']=now()
checkpoint['new_API_calls']=len(list(OWN.rglob('run_*_started.json')))
checkpoint['questions'][a.question]={'status':'primary_candidate_pending_new_parent_review' if paired else 'pair_miss_further_valid_new_hypotheses_under_assessment',
 'last_variant_id':a.variant,'last_actual_finals':final_letters,'last_expected_wrong_answer':summary['expected_wrong_answer'],
 'new_API_calls':len(list((OWN/a.question).rglob('run_*_started.json'))),'candidate_directory':str(directory)}
write(OWN/'checkpoint.json',checkpoint)
if paired:
    queue=read(OWN/'second_review_queue.json')
    queue.append({'question_id':a.question,'variant_id':a.variant,'candidate_directory':str(directory),
      'image_sha256':sha(directory/'candidate.png'),'plugin_sha256':sha(directory/'plugin.json'),'design_sha256':sha(directory/'design.json'),
      'correct_answer':read(directory/'design.json')['correct_answer'],'frozen_wrong_preset':summary['expected_wrong_answer'],
      'complete_final_answers':finals,'summary_path':str(invocation/'summary.json'),'primary_review_path':str(directory/'primary_review.json'),
      'reference_transfer_path':str(directory/'reference_transfer_and_history_difference.json'),
      'restrictions':['PRIMARY only','Requires new independent parent-created second review','No user Pass/Collect or delivery','Two observations only; no causal or general success-rate claim']})
    write(OWN/'second_review_queue.json',queue)
print(json.dumps({'question_id':a.question,'variant':a.variant,'actual_finals':final_letters,'preset':summary['expected_wrong_answer'],'paired_hit':paired},ensure_ascii=False))
