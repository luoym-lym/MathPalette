from tools72 import *

q=sys.argv[1];values=sys.argv[2:]
v={'Plane335':'r72_congruent_apex_wedge_binding','Plane355':'r72_width_to_fold_measurement_role'}[q]
d=HERE/q/v;design=read(d/'design.json')
tests=list((d/'tests').glob('quicktest3_*'));assert len(tests)==1
t=tests[0];summary=read(t/'summary.json');assert summary['two_completed'] and len(values)==2
answers=[];runs=[]
for i in [1,2]:
    r=read(t/f'run_{i:02d}.json');raw=read(t/f'run_{i:02d}_response.json')
    assert r['status']=='completed' and raw['choices'][0]['finish_reason']=='stop'
    answers.append(raw['choices'][0]['message']['content'])
    runs.append({'run_index':i,'run_path':str(t/f'run_{i:02d}.json'),'raw_path':str(t/f'run_{i:02d}_response.json'),'raw_sha256':sha(t/f'run_{i:02d}_response.json'),'manually_selected_final_value':values[i-1]})
write(d/'manual_final_review.json',{'question_id':q,'variant_id':v,'reviewed_at':now(),'review_type':'PRIMARY full-final manual read, not independent review','full_complete_finals_manually_read':True,'manual_final_values':values,'complete_model_answers':answers,'runs':runs,'predeclared_wrong_answer':design['expected_wrong_answer'],'preset_hits':[v==design['expected_wrong_answer'] for v in values],'both_hit_preset':all(v==design['expected_wrong_answer'] for v in values),'no_preset_relabel_or_cherry_pick':True,'interpretation_notes':(['Run1 explicitly concludes 2 after accepting only corresponding upper/lower far vertices and incorrectly excluding valid joins to the near-right apex.','Run2 explicitly concludes 9, with a mistaken left/right orientation description and accepts every pair. Both fail preset1; neither is a success even though both answers are wrong.'] if q=='Plane335' else ['Manual final letter and value checked against complete final, rather than incidental option mentions.']),'no_new_control_calls':True,'no_causal_gain_or_human_population_claim':True})
print(q,values,'preset',design['expected_wrong_answer'],'hits',[v==design['expected_wrong_answer'] for v in values],flush=True)
