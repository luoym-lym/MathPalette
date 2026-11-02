from worker_env import *
import argparse

p=argparse.ArgumentParser();p.add_argument('question',choices=['Plane194','Plane245']);a=p.parse_args();qid=a.question
var={'Plane194':'r01_fold_axes_to_square_hole','Plane245':'r01_fold_motion_to_square_aperture'}[qid]
directory=OWN/qid/var
invocations=list((directory/'tests').glob('quicktest3_*'));assert len(invocations)==1
invocation=invocations[0];summary=read(invocation/'summary.json');assert summary['two_completed']
actual={'Plane245':['B','B'],'Plane194':['A','E']}[qid]
finals=[]
for index,result in enumerate(summary['results'],1):
    rawpath=invocation/f'run_{index:02d}_response.json';raw=read(rawpath)
    message=raw['choices'][0]['message']['content']
    assert message==result['answer']
    assert raw['choices'][0]['finish_reason']=='stop' and not result['truncated']
    assert message.rstrip().endswith(actual[index-1]) or message.rstrip().endswith(actual[index-1]+'**')
    finals.append({'run_index':index,'complete_answer':message,'manual_final_letter':actual[index-1],
       'manual_final_value':{'Plane245':['Choice B; body misdescribes B as four side-midpoint notches','Choice B, central diamond aperture'],
                             'Plane194':['Choice A, all four exterior corners clipped','Choice E; body hallucinates two nested holes although actual E has one axis-aligned square hole']}[qid][index-1],
       'complete_nontruncated':True,'expected_wrong_answer':summary['expected_wrong_answer'],
       'hit':actual[index-1]==summary['expected_wrong_answer'],'raw_response_sha256':sha(rawpath)})
    assert sha(rawpath)==result['response_sha256']
review={'reviewed_at':now(),'review_scope':'PRIMARY manual full raw/final reading only','question_id':qid,'variant_id':var,
 'two_complete_original_quicktest3_calls':True,'manual_finals':finals,'expected_wrong_answer':summary['expected_wrong_answer'],
 'both_match_frozen_preset':all(f['hit'] for f in finals),'status':'PAIR_MISS_DO_NOT_RETEST_IDENTICAL_INPUT',
 'summary_path':str(invocation/'summary.json'),'binding_sha256':sha(invocation/'binding.json'),
 'design_snapshot_matches':sha(invocation/'design_snapshot.json')==sha(directory/'design.json'),
 'request_body_matches':sha(invocation/'request.json')==summary['request_body_sha256'],
 'note':'Neither an incidental wrong claim in reasoning nor an off-preset error is counted. The frozen preset is unchanged. No third call or selected pair.'}
write(directory/'manual_final_review.json',review,True)
checkpoint=read(OWN/'checkpoint.json');checkpoint['updated_at']=now()
checkpoint['questions'][qid]={'status':'r01_pair_miss_new_substantive_hypothesis_under_review','new_API_calls':2,'r01_manual_finals':actual,'candidate_directory':str(directory)}
checkpoint['new_API_calls']=len(list(OWN.rglob('run_*_started.json')))
write(OWN/'checkpoint.json',checkpoint)
print(json.dumps({'question_id':qid,'manual_finals':actual,'frozen_preset':summary['expected_wrong_answer'],'paired_hit':False},ensure_ascii=False))
