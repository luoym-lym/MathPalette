from unit_env import *
for qid,vid in [('Plane211','adjacent_gap_to_short_closure'),('Plane364','native_orthogonal_span_comparison'),('Plane423','native_orthogonal_span_comparison')]:
    folder=OWN/qid/vid
    d=read(folder/'design.json')
    assert read(folder/'independent_replay.json')['exact_replay']
    findings=('The six red circle intervals all occupy the same genuine neighboring-label gap between 9 and 1. The red B closure is the existing short chord between those very labels. This relation is not a source added chord; it compares arc proximity with a candidate connection. The entire blue given prefix is preserved in source/A/B/E. All labels 9,1,2 and the decisive E 9-2 line remain clear; the wrong B 9-1 closure is fully visible.' if qid=='Plane211'
              else 'Only original straight grid intervals change color/width. Their endpoints are original black dots. The blue vertical span P5-P1 and upper red horizontal P1-P2 have length 4 each. No extra dot is drawn at crossings. All six point centers and every grid unit remain clear. '+('The lower red P3-P4 span has the same length 4 and its true horizontal offset is apparent; no missing axis-aligned corner is invented.' if qid=='Plane364' else 'The two colored intervals make an open L at original P1; no triangle edge or closed region is introduced.'))
    report={'review_kind':'PRIMARY_AUTHOR_ONLY','reviewed_at':now(),
            'actual_source_and_formal_PNG_viewed':True,'actual_candidate_native_PNG_viewed':True,
            'mathematics_proof_path':str(OWN/qid/'mathematical_proof.json'),'unique_correct_answer':'E',
            'all_current_reference_PNGs_viewed':True,'visual_findings':findings,
            'every_mark_role':d['marker_roles'],'human_literal_reading':d['human_semantics'],
            'information_comparison':d['mechanism'],'substantive_change':d['difference_from_old'],
            'conciseness':('The source arc/candidate closing-edge pair supplies the only new inference. Other repeated intervals/prefix styles preserve literal source ink in each result; none is overwritten or decorative.' if qid=='Plane211'
                           else 'Two or three original grid intervals supply orthogonal/equal-span comparisons. No additional helper construction is needed.'),
            'ready_for_exact_two_calls':True,'fresh_schema_repeat_new_process_replay_passed':True,
            'preset_frozen':{'letter':d['expected_wrong_answer'],'value':d['expected_wrong_value']},
            'candidate_sha256':d['candidate_sha256'],'design_sha256':sha((folder/'design.json').read_bytes()),
            'limitations':[d['remaining_risk'],'No delivery, independent review, user approval, Pass, Collect, causal gain, or general success rate claimed.']}
    save(folder/'primary_review_before_calls.json',report)
checkpoint=read(OWN/'checkpoint.json')
checkpoint.update(updated_at=now(),status='refinement_preflight_complete',
                  question_status={q:'second_distinct_design_ready_for_two_calls' for q in QIDS})
save(OWN/'checkpoint.json',checkpoint,replace=True)
