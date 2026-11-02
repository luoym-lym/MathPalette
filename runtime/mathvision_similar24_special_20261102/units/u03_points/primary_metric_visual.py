from unit_env import *
folder=OWN/'Plane364/square_side_diagonal_role_comparison'
d=read(folder/'design.json')
assert read(folder/'independent_replay.json')['exact_replay']
save(folder/'primary_review_before_calls.json',{'reviewed_at':now(),'review_kind':'PRIMARY_AUTHOR_ONLY',
     'actual_source_JPG_formal_PNG_candidate_PNG_viewed':True,'actual_candidate_viewed_native_size':True,
     'unique_correct_answer':'E','mathematical_proof_path':str(OWN/'Plane364/mathematical_proof.json'),
     'every_mark_role':d['marker_roles'],'human_literal_reading':d['human_semantics'],
     'visual_findings':'The four blue segments visibly form the genuine tilted square. Two red segments are its original horizontal/vertical diagonals on existing grid lines. Their center crossing remains unmarked. All six black point centers remain distinct, including two outside the square. The true side lengths sqrt(8) versus diagonals4 can be counted from the unchanged grid. No edge, numeral, dot or unit spacing is hidden.',
     'conciseness':'Six marks convey two complete actual point-pair roles. There are no repeated/overwritten actions, new labels, new points, angle ticks, or false equality conditions.',
     'substantive_new_hypothesis':d['difference_from_old'],
     'preset_frozen_before_both_calls':{'letter':'A','value':'square'},
     'fresh_schema_repeat_and_new_process_replay_passed':True,'ready_for_exact_two_calls':True,
     'candidate_sha256':d['candidate_sha256'],'design_sha256':sha((folder/'design.json').read_bytes()),
     'limitations':[d['remaining_risk'],'Only PRIMARY author review. A double-hit would still require new independent parent review. No delivery, Pass, Collect or user approval.']})
