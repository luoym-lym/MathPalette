from unit_env import *

for qid,vid in [('Plane211','paired_chord_motif_partial_completion'),
                ('Plane364','square_opposite_vector_comparison'),('Plane423','square_opposite_vector_comparison')]:
    folder=OWN/qid/vid
    d=read(folder/'design.json')
    replay=read(folder/'independent_replay.json')
    assert replay['exact_replay']
    value={'review_kind':'PRIMARY_AUTHOR_ONLY','reviewed_at':now(),
           'actual_source_JPG_viewed':True,'actual_formal_PNG_viewed_native_size':True,
           'actual_candidate_PNG_viewed_native_size':True,'all_nine_current_C01s_actually_viewed':True,
           'mathematical_proof_path':str(OWN/qid/'mathematical_proof.json'),
           'correct_answer_E_unique':True,'mathematics_independent_of_formal_answer_and_model_outputs':True,
           'each_mark_role':d['marker_roles'],'literal_presentation_analysis':d['human_semantics'],
           'visual_findings':('The red first source chord and blue second source chord are clear; they are preserved identically in the three panels that contain them. A also has red 6-8 and blue 8-1, which are actual skip-two chords. The decisive A adjacent 5-6 edge stays black and fully visible. All numerals, every black point center, circle and all other option edges remain legible. No new point or crossing is introduced.' if qid=='Plane211'
                             else 'Four thin colored lines connect four original black dots into a tilted square. Red opposite edges have displacement (2,2); blue opposite edges have displacement (2,-2). Their one unmarked grid crossing per diagonal side is just an ordinary grid intersection, with no extra dot. All six original dots, including the two rightmost outside the square, are plainly visible. Grid unit spacing and scope remain readable. This square is a true drawable example, with no line or text declaring it exhaustive.'),
           'conciseness_check':('Ten actions have separate chord-mapping or literal-source-preservation roles; no overwritten action or option-letter styling.' if qid=='Plane211'
                               else 'Four single-stroke vectors form the minimum complete two-opposite-pair comparison; no point overlay, text, repeated action, or decorative color.'),
           'preset_frozen_before_calls':{'letter':d['expected_wrong_answer'],'value':d['expected_wrong_value']},
           'fresh_schema_repeat_and_new_process_exact_replay_passed':True,
           'ready_for_exact_two_calls':True,'image_sha256':d['candidate_sha256'],
           'plugin_sha256':d['plugin_sha256'],'design_sha256':sha((folder/'design.json').read_bytes()),
           'limitations':[d['remaining_risk'],'No approval, Pass, Collect, delivery, independent second review, causal gain, or general success rate is claimed.']}
    save(folder/'primary_review_before_calls.json',value)
checkpoint=read(OWN/'checkpoint.json')
checkpoint.update(updated_at=now(),status='precall_gates_complete',
                  question_status={q:'frozen_candidate_ready_exact_two_calls' for q in QIDS})
save(OWN/'checkpoint.json',checkpoint,replace=True)
