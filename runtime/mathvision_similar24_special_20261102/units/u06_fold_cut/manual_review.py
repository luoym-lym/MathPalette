from local_env import *
from api_gate import check_frozen
import json, argparse, base64, hashlib

ap=argparse.ArgumentParser()
ap.add_argument('qid')
ap.add_argument('final1')
ap.add_argument('final2')
ap.add_argument('--notes',required=True)
ap.add_argument('--variant')
args=ap.parse_args()
entries=read_json(OWN/'primary_design_manifest.json')
if (OWN/'supplementary_design_manifest.json').exists(): entries+=read_json(OWN/'supplementary_design_manifest.json')
entry=next(x for x in entries if x['question_id']==args.qid and (args.variant is None or x['variant_id']==args.variant))
candidate=Path(entry['candidate_directory'])
design=check_frozen(candidate)
dirs=list((candidate/'tests').glob('quicktest3_*'));assert len(dirs)==1
invocation=dirs[0]
summary=read_json(invocation/'summary.json')
binding=read_json(invocation/'binding.json')
assert summary['two_completed'] and summary['requested_runs']==2 and len(summary['results'])==2
assert len(list(invocation.glob('run_*_started.json')))==2
assert read_json(candidate/'api_process_finished.json')['actual_network_requests_seen']==2
request=read_json(invocation/'request.json')
formal=read_json(OWN/args.qid/'formal_record.json')
assert request['messages'][1]['content'][0]['text']==formal['question']
rawimage=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
assert hashlib.sha256(rawimage).hexdigest()==sha(candidate/'candidate.png')
del rawimage,request
assert sha(invocation/'request.json')==binding['request_body_sha256']
assert sha(invocation/'design_snapshot.json')==sha(candidate/'design.json')==binding['design_sha256']
finals=[]
for i,letter in enumerate([args.final1,args.final2],1):
    rawpath=invocation/f'run_{i:02d}_response.json'
    raw=read_json(rawpath)
    result=summary['results'][i-1]
    choice=raw['choices'][0]
    assert result['status']=='completed' and not result.get('truncated') and choice['finish_reason']=='stop'
    assert sha(rawpath)==result['response_sha256']
    answer=choice['message']['content']
    assert answer==result['answer']
    assert letter in formal['choices']
    finals.append({'run_index':i,'manually_read_complete_raw':True,'raw_response_path':str(rawpath),
      'raw_response_sha256':sha(rawpath),'full_answer_exact':answer,'finish_reason':choice['finish_reason'],
      'final_choice_manually_resolved':letter,'final_value':formal['choices'][letter],
      'matches_frozen_letter_and_value':letter==design['expected_wrong_answer'] and formal['choices'][letter]==design['expected_wrong_value']})
pair=all(x['matches_frozen_letter_and_value'] for x in finals)
review={'review_kind':'PRIMARY_FULL_RAW_FINAL_READING_NOT_SECOND_REVIEW','reviewed_at':now(),
 'question_id':args.qid,'variant_id':entry['variant_id'],'formal_correct_answer':formal['answer'],
 'frozen_wrong_preset':design['expected_wrong_answer'],'frozen_wrong_value':design['expected_wrong_value'],
 'finals':finals,'notes_on_final_resolution':args.notes,'exactly_two_actual_calls':True,
 'request_formal_text_and_frozen_PNG_exact':True,'image_sha256':sha(candidate/'candidate.png'),
 'design_sha256':sha(candidate/'design.json'),'binding_sha256':sha(invocation/'binding.json'),
 'request_sha256':sha(invocation/'request.json'),'summary_path':str(invocation/'summary.json'),
 'two_complete_target_hits':pair,'classification':'PRIMARY_CANDIDATE_REQUIRES_FRESH_PARENT_SECOND_REVIEW' if pair else 'FAILED_PAIR_RETAINED_NO_RETEST',
 'no_postoutput_relabel':True,'no_third_call':True,'no_Pass_Collect_or_delivery':True,
 'limitations':['Only these two observations are established. No efficacy-rate or causal-benefit inference.',
                'Any PRIMARY candidate still requires a new independently created second reviewer.']}
save(candidate/'manual_full_final_review.json',review,True)
queue=read_json(OWN/'second_review_queue.json')
assert not any(x['question_id']==args.qid for x in queue)
if pair:
    queue.append({'question_id':args.qid,'variant_id':entry['variant_id'],'candidate_directory':str(candidate),
      'image_sha256':sha(candidate/'candidate.png'),'plugin_sha256':sha(candidate/'plugin.json'),'design_sha256':sha(candidate/'design.json'),
      'original_correct_answer':formal['answer'],'frozen_wrong_preset':design['expected_wrong_answer'],'frozen_wrong_value':design['expected_wrong_value'],
      'two_complete_finals':finals,'summary_path':str(invocation/'summary.json'),'primary_review_path':str(candidate/'primary_review_before_calls.json'),
      'manual_full_final_review_path':str(candidate/'manual_full_final_review.json'),'reference_transfer_path':str(candidate/'reference_transfer.json'),
      'mathematics_path':str(candidate/'mathematics.json'),'history_difference_path':str(candidate/'history_difference_audit.json'),
      'eligibility_path':str(candidate/'eligibility_before_actual_call_02.json'),'limits':review['limitations'],
      'status':'PRIMARY_ONLY_PENDING_NEW_PARENT_CREATED_INDEPENDENT_REVIEW','no_delivery':True})
save(OWN/'second_review_queue.json',queue)
cp=read_json(OWN/'checkpoint.json'); cp['updated_at']=now()
cp['questions'][args.qid].update({'status':'PRIMARY_PENDING_FRESH_SECOND_REVIEW' if pair else 'FAILED_PAIR_PENDING_MATERIAL_REFINEMENT_ASSESSMENT',
 'finals':[args.final1,args.final2],'preset':design['expected_wrong_answer'],'two_hits':pair,
 'calls':len(list((OWN/args.qid).glob('*/actual_call_*_payload_gate.json'))),
 'manual_review_path':str(candidate/'manual_full_final_review.json')})
save(OWN/'checkpoint.json',cp)
print(json.dumps({'question_id':args.qid,'manual_finals':[args.final1,args.final2],'frozen_preset':design['expected_wrong_answer'],'two_target_hits':pair},ensure_ascii=False))
