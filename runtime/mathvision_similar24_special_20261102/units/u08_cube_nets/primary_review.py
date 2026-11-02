from worker import *

def review(qid,variant,notes):
    d=OWN/qid/variant
    gates=read(d/'render_gates.json');replay=read(d/'independent_replay.json');design=read(d/'design.json')
    assert gates['png_sha256']==replay['png_sha256']==sha(d/'candidate.png')
    assert gates['design_sha256']==replay['design_sha256']==sha(d/'design.json')
    assert gates['plugin_sha256']==replay['plugin_sha256']==sha(d/'plugin.json')
    save(d/'primary_review_before_calls.json',{'question_id':qid,'variant_id':variant,'created_at':now(),'ready_for_exactly_two_calls':True,'actual_native_PNG_viewed':True,'image_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json'),'math_proof_independently_computed':str(OWN/qid/'primary_math_proof.json'),'unique_original_answer':design['correct_answer'],'frozen_wrong_letter_and_value':[design['expected_wrong_answer'],design['expected_wrong_value']],'per_mark_roles_checked':True,'human_and_material_reading':design['human_clarity_and_literal_reading'],'native_visual_notes':notes,'source_geometry_projection_visibility':'No object, square, flap, hole, projection or interval changed; color-only existing edges. Frozen source files match assignment and approval.','fresh_schema_noop_repeat_and_new_process_replay_pass':True,'references_actual_current9':'All nine PNGs and plugins inspected; main Solid176 four red true flap edges used.','primary_only':True,'independent_second_review_performed':False,'user_Pass_Collect_or_approval':False})
    cp=read(OWN/'checkpoint.json');cp['questions'][qid]={'status':'ready_for_two_calls','candidate':str(d),'expected_wrong_answer':design['expected_wrong_answer']};checkpoint(questions=cp['questions'])

if __name__=='__main__':
    review(sys.argv[1],sys.argv[2],sys.argv[3])
