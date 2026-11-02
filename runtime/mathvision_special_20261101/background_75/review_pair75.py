import bootstrap75 as boot
from research75 import *
from designs75 import specifications

def main():
    q=sys.argv[1];manual=sys.argv[2:4];notes=sys.argv[4]
    target=OWN/q/specifications(q)[0]
    sums=list((target/'tests').glob('quicktest3_*/summary.json'))
    assert len(sums)==1
    summary=read(sums[0]);inv=sums[0].parent;design=read(target/'design.json')
    assert summary['expected_wrong_answer']==design['expected_wrong_answer']
    results=[]
    for i,final in enumerate(manual,1):
        rawpath=inv/f'run_{i:02d}_response.json';job=read(inv/f'run_{i:02d}.json');raw=read(rawpath)
        full=raw['choices'][0]['message']['content'];finish=raw['choices'][0].get('finish_reason')
        results.append({'run_index':i,'complete_final_manually_read':True,'full_final_text':full,'explicit_terminal_answer':final,'consistent_terminal_value':True,'finish_reason':finish,'complete_for_grading':job['status']=='completed' and finish!='length','target_hit':final==str(design['expected_wrong_answer']) and job['status']=='completed' and finish!='length','raw_response':str(rawpath),'raw_response_sha256':sha(rawpath.read_bytes()),'job':str(inv/f'run_{i:02d}.json'),'job_sha256':sha((inv/f'run_{i:02d}.json').read_bytes())})
    review={'question_id':q,'variant_id':design['variant_id'],'review_role':'primary manual full-final reading, not independent','reviewed_at':now(),'unchanged_predeclared_wrong_answer':design['expected_wrong_answer'],'formal_correct_answer':design['correct_answer'],'results':results,'manual_notes':notes,'two_complete_finals_hit_own_preset':len(results)==2 and all(x['target_hit'] for x in results),'no_incidental_mention_grading_or_posthoc_relabeling':True,'image_sha256':design['image_sha256'],'design_sha256':sha((target/'design.json').read_bytes()),'request_sha256':summary['request_body_sha256'],'summary':str(sums[0])}
    put(target/'manual_final_review.json',review)
    assessment=read(OWN/q/'assessment.json');assessment.update(status='PRIMARY_doublehit_needs_NEW_parent_independent_review' if review['two_complete_finals_hit_own_preset'] else 'tested_pair_missed_frozen_preset_do_not_retest_unchanged',solver_calls_so_far=len(summary['results']),full_manual_review=str(target/'manual_final_review.json'),complete_pair=summary['two_completed']);put(OWN/q/'assessment.json',assessment)
    cp=read(OWN/'checkpoint.json');cp['updated_at']=now();cp['status']='candidate_testing_in_progress';cp['primary_assessments']=[read(OWN/x/'assessment.json') for x in IDS];cp['current_API_calls']=len(list(OWN.glob('Plane*/r75_*/tests/quicktest3_*/run_*_started.json')));cp['complete_candidate_pairs']=len(list(OWN.glob('Plane*/r75_*/manual_final_review.json')));put(OWN/'checkpoint.json',cp)
    print(json.dumps({'question_id':q,'preset':design['expected_wrong_answer'],'actual_full_finals':manual,'doublehit':review['two_complete_finals_hit_own_preset']},ensure_ascii=False))

if __name__=='__main__':main()
