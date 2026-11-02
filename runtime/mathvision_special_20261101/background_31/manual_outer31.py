from bootstrap31 import *

q='Plane294';n='r31_outer_whole_side_to_part_transfer';d=OWN/q/n
ed=next((d/'tests').glob('quicktest3_*'));summary=read(ed/'summary.json');runs=[]
notes=[
 'Terminal final is136cm, explicitly outside all options; not presetE=232. The reply incorrectly makes all8 rectangles16cm long and then proposes several hypothetical textual changes. IncidentalE=232 in its option list is not a hit, nor is its discardedD=200 speculation a selected final.',
 'Terminal Answer72cm, outside all options; not presetE=232. The reply incorrectly counts one added width per concentric layer instead of two, and its summation conflicts with its asserted square area. Its narrative calls168 a possible intended answer for a supposed flawed statement, but final72 is explicit and noE final is selected.'
]
for i,final in enumerate(['136','72'],1):
 p=ed/f'run_{i:02d}_response.json';raw=read(p);entry=read(ed/f'run_{i:02d}.json');full=raw['choices'][0]['message']['content']
 assert full==entry['answer'] and raw['choices'][0]['finish_reason']=='stop' and entry['status']=='completed'
 runs.append({'run_index':i,'full_raw_final_manually_read':True,'full_assistant_content':full,'manual_final':final,'manual_final_value':final+' cm','selected_choice_letter':None,'final_is_outside_all_given_options':True,'manual_observation':notes[i-1],'preset_hit':False,'raw_response_path':str(p),'raw_response_sha256':sha(p)})
save(d/'manual_finals.json',{'question_id':q,'variant_id':n,'expected_wrong_answer_before_both_calls':summary['expected_wrong_answer'],'expected_wrong_value':'232 cm','formal_correct_answer':'D','formal_correct_value':'200 cm','same_frozen_image_sha256':summary['image_sha256'],'same_frozen_design_sha256':summary['design_sha256'],'complete_exact_two_calls':summary['two_completed'],'runs':runs,'two_preset_hits':False,'status':'MISSED_PRESET_NO_REVIEW_CANDIDATE','no_posthoc_relabel':True,'controls':[],'outer_preset_rationale_predeclared_before_reading_inner_variant_replies':True,'declaration_timestamp':read(d/'design_difference_audit.json')['created_at'],'effect_limits':'No original controls available; none repeated or newly called. No causal/statistical/human-study claim. All original problem text, dimensions and source geometry remain valid despite solver typo speculation.'})
