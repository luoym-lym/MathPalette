from worker import *
import base64

def review(qid, variant, manual_letters):
    out = OWN/qid/variant
    invocations = list((out/'tests').glob('quicktest3_*'))
    assert len(invocations) == 1
    invocation = invocations[0]
    summary = read(invocation/'summary.json')
    binding = read(invocation/'binding.json')
    design = read(out/'design.json')
    request = read(invocation/'request.json')
    assert request['messages'][1]['content'][0]['text'] == read(out/'eligibility_immediately_before_calls.json')['formal_record']['question']
    embedded = base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
    assert digest(embedded) == binding['image_sha256'] == filehash(out/'candidate.png')
    del embedded
    assert binding['request_body_sha256'] == filehash(invocation/'request.json')
    assert binding['design_sha256'] == filehash(out/'design.json') == filehash(invocation/'design_snapshot.json')
    assert request['model'] == 'mimo-v2.6-flash' and request['thinking'] == {'type':'disabled'}
    assert set(request) == {'model','stream','thinking','messages'}
    assert len(summary['results']) == len(manual_letters) == 2
    complete = []
    for i, manual in enumerate(manual_letters,1):
        rawpath = invocation/f'run_{i:02d}_response.json'
        raw = read(rawpath)
        result = summary['results'][i-1]
        text = raw['choices'][0]['message']['content']
        assert filehash(rawpath) == result['response_sha256']
        assert result['status'] == 'completed' and result['truncated'] is False
        assert raw['choices'][0]['finish_reason'] == result['finish_reason'] == 'stop'
        assert text == result['answer']
        complete.append({'run_index':i,'manual_final_letter':manual,'manual_final_value':manual,
                         'complete_response_text':text,'manually_read_in_full':True,
                         'no_terminal_letter_value_conflict':True,
                         'preset_hit':manual==str(design['expected_wrong_answer']),
                         'finish_reason':'stop','truncated':False,
                         'raw_response_path':str(rawpath),'raw_response_sha256':filehash(rawpath)})
    twohit = all(r['preset_hit'] for r in complete)
    audit = {'question_id':qid,'variant_id':variant,'reviewed_at':now(),
      'role':'PRIMARY author manual full-final review',
      'correct_answer':design['correct_answer'],'frozen_wrong_preset':design['expected_wrong_answer'],
      'two_complete_finals':complete,'two_preset_hits':twohit,'exactly_two_actual_requests':True,
      'original_settings_and_payload_preserved':True,'no_third_call_no_relabel_no_retry':True,
      'same_exact_PNG_both_calls':True,'formal_question_exact':True,
      'summary_path':str(invocation/'summary.json'),'summary_sha256':filehash(invocation/'summary.json'),
      'binding_path':str(invocation/'binding.json'),'binding_sha256':filehash(invocation/'binding.json'),
      'request_sha256':filehash(invocation/'request.json'),
      'image_sha256':filehash(out/'candidate.png'),'plugin_sha256':filehash(out/'plugin.json'),
      'design_sha256':filehash(out/'design.json'),
      'decision':'PRIMARY_TWO_HIT_PENDING_NEW_INDEPENDENT_SECOND_REVIEW' if twohit else 'FAILED_FROZEN_PRESET_DO_NOT_RETEST',
      'model_narrative_limit':'Only final letter/value matching is asserted. Wrong counts, coverage assumptions or incompatible mechanisms in the narratives are not evidence that the proposed mechanism was followed.',
      'no_Pass_Collect_user_approval_or_delivery':True}
    write(out/'manual_full_final_review.json',audit)
    checkpoint = read(OWN/'checkpoint.json')
    checkpoint['updated_at'] = now()
    checkpoint['actual_new_API_calls'] = len(list(OWN.glob('Plane*/*/tests/*/run_*_started.json')))
    checkpoint.setdefault('attempts',{})[qid+'/'+variant] = {'status':audit['decision'],
        'preset':design['expected_wrong_answer'],'manual_finals':manual_letters,
        'review_path':str(out/'manual_full_final_review.json')}
    checkpoint['question_status'][qid] = audit['decision']
    if not twohit and qid+'/'+variant not in checkpoint['failures']:
        checkpoint['failures'].append(qid+'/'+variant)
    queue = read(OWN/'second_review_queue.json')
    if twohit:
        entry = {'question_id':qid,'variant_id':variant,'candidate_directory':str(out),
            'image_sha256':audit['image_sha256'],'plugin_sha256':audit['plugin_sha256'],
            'design_sha256':audit['design_sha256'],'original_correct_answer':design['correct_answer'],
            'frozen_wrong_preset':design['expected_wrong_answer'],
            'two_complete_finals':complete,'summary_path':audit['summary_path'],
            'primary_review_path':str(out/'primary_visual_review_before_calls.json'),
            'manual_full_final_review_path':str(out/'manual_full_final_review.json'),
            'primary_math_proof_path':design['primary_mathematical_proof_path'],
            'reference_transfer_path':str(out/'reference_transfer.json'),
            'limitations':['PRIMARY only; parent must commission fresh independent second review.',
                           'No user approval, Pass/Collect or delivery.',
                           'Two observations only; no causal or population-success claim.',
                           'Detached bracket adaptation and native clarity require independent scrutiny.']}
        assert not any(q['question_id']==qid for q in queue)
        queue.append(entry)
        checkpoint['primary_candidates'].append(qid+'/'+variant)
    write(OWN/'checkpoint.json',checkpoint)
    write(OWN/'second_review_queue.json',queue)
    print(json.dumps({'question_id':qid,'variant':variant,'preset':design['expected_wrong_answer'],
                      'manual_finals':manual_letters,'twohit':twohit,'actual_total_calls':checkpoint['actual_new_API_calls']}))

if __name__ == '__main__':
    review(sys.argv[1],sys.argv[2],sys.argv[3:])
