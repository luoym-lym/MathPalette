from tools08 import *
decisions={
('Plane362','unchanged_digit_side_binding'):{'finals':['C','A'],'hits':[False,True],'notes':['Final C is not preset A and the described digit value does not match the drawn C.','Final A=2008 is consistent with option A, so this individual call hits preset A. Pair fails.']},
('Plane362','reverse_order_side_binding'):{'finals':['C','A'],'hits':[False,False],'notes':['Final C is accompanied by the value 2005, whereas drawn C is 8002. Inconsistent final letter/value is not accepted as a hit even though the letter equals preset C.','Final A, not preset C. Pair fails.']},
('Plane371','letter_handedness_shortcut'):{'finals':['D','B'],'hits':[False,False],'notes':['Final D, not preset A; narrative misdescribes options.','Final B, not preset A; narrative misdescribes glyphs.']},
('Plane404','unreflected_first_digit_binding'):{'finals':['A','A'],'final_values':['2:6:9','2:6:9'],'hits':[True,True],'notes':['Complete final conclusion 2:6:9 explicitly matches option A, preset A. Reasoning falsely counts strokes but final is unambiguous.','Complete conclusion ends A and 2:6:9. An earlier intermediate mention of 8 is erroneous; final letter/value agree. Narrative differs from first call; no causal attribution.']},
('Plane446','square_skeleton_symmetry'):{'finals':['1','1'],'hits':[False,False],'notes':['Final1, preset3. Pair of same wrong answers does not meet frozen preset.','Final1, preset3; no post-hoc change.']},
('Plane446','tail_orientation_correspondence'):{'finals':['2','1'],'hits':[False,True],'notes':['Final2 is formal correct answer, not preset1.','Final1 matches preset1; pair fails.']},
('Plane292','tail_ear_mirror_binding'):{'finals':['C','C'],'hits':[False,False],'notes':['FinalC, presetB; wrong reflection count.','FinalC, presetB; no post-hoc change despite C/C.']},
('Plane404','original_control'):{'finals':['B','C'],'final_values':['2:6:6','5:6:9'],'hits':[False,False],'notes':['Original control finalB2:6:6, incorrect. Claims A is absent, which is false.','Original control concludes5,6,9, consistent with C despite no standalone last letter. Narrative misreads options; final value correct. Controls do not establish causality.']}}
for (q,v),dec in decisions.items():
    folder=HERE/q/v;evidence=list((folder/'tests').glob('quicktest3_*'));assert len(evidence)==1
    d=json.loads((folder/'design.json').read_text(encoding='utf-8'));records=[]
    for n in (1,2):
        p=evidence[0]/f'run_{n:02d}.json';r=json.loads(p.read_text(encoding='utf-8'));assert r['status']=='completed' and not r.get('truncated') and r['finish_reason']=='stop'
        records.append({'run':n,'run_path':str(p),'response_path':str(evidence[0]/f'run_{n:02d}_response.json'),'complete_answer_text':r['answer'],'manual_final':dec['finals'][n-1],'manual_final_value':dec.get('final_values',[None,None])[n-1],'preset_hit':dec['hits'][n-1],'manual_note':dec['notes'][n-1]})
    write(folder/'manual_final_review.json',{'reviewed_at':now(),'complete_final_answers_manually_read':True,'expected_wrong_answer_frozen':d['expected_wrong_answer'],'both_preset_hits':all(dec['hits']),'role':'original_control' if v=='original_control' else 'candidate','records':records,'binding_path':str(evidence[0]/'binding.json'),'independent_second_review':False})
print(json.dumps({'manual_pairs_saved':len(decisions)}))
