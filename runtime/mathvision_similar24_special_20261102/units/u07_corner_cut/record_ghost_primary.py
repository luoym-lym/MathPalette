from worker_env import *
import argparse
p=argparse.ArgumentParser();p.add_argument('question',choices=['Plane194','Plane245']);a=p.parse_args();qid=a.question
var={'Plane194':'r02_discarded_legs_to_square_aperture','Plane245':'r02_discarded_legs_to_extra_outer_notches'}[qid]
folder=OWN/qid/var
visual={'Plane194':'At 768px the final source removed top-right corner has a red vertical dashed ghost leg and blue horizontal dashed ghost leg; actual black diagonal clip remains clear. E square-hole vertical sides red, horizontal sides blue. The earlier first/second fold guides remain original black. A/B/C/D and all other geometry are unchanged.',
        'Plane245':'At 768px source removed lower-left corner has a red vertical dashed ghost leg and blue horizontal dashed ghost leg, wholly outside the retained gray pentagon except endpoints. Actual diagonal black clip remains clear. Eight E outer-notch edges are red vertical or blue horizontal; its actual central white diamond hole remains black. All source arrows, folds, A/B/C/D, grayscale and hole geometry stay unchanged.'}[qid]
write(folder/'primary_review.json',{'reviewed_at':now(),'scope':'PRIMARY ONLY; not independent second review',
 'actual_source_JPG_formal_PNG_candidate_PNG_viewed':True,'native_visual_review':visual,
 'mathematical_uniqueness':'All original options independently excluded/constructed in mathematical_audit.json; correct '+read(folder/'design.json')['correct_answer'],
 'human_unambiguity':'The colored source lines are dashed traces of absent material. They do not form new cuts and do not recolor any surviving material edge. Colored E is already impossible geometrically under both intrinsic-edge and external-highlight readings. All valid original samples remain unchanged. The source solid actual cut and ghost dash distinction is visible. No need for a new textual legend.',
 'every_marker_has_information_source_receiver_and_purpose':True,
 'conciseness':'Two existing discarded-corner legs and only their receiving existing edges. No redundant action or added line/region. No arbitrary mark cap used.',
 'substantive_novelty_review':'Changed source boundary role from operation guides/arrows to discarded old perimeter. Plane245 additionally changes receiver from inner A aperture to E exterior notches, and freezes an extra-boundary double-counting prediction. Not a color/width/filename-only change.',
 'expected_wrong_answer':read(folder/'design.json')['expected_wrong_answer'],
 'fresh_schema_defaults_noop_repeat_passed':True,'independent_exact_process_replay_required':True,
 'proceed_to_exact_two_calls':True,'restrictions':['Only two original quicktest3 calls','No failed/interrupted input retests','No third call','No post-output relabeling','PRIMARY only; parent must create new independent review','No Pass/Collect/delivery']},True)
checkpoint=read(OWN/'checkpoint.json');checkpoint['updated_at']=now()
checkpoint['questions'][qid]['next_candidate_directory']=str(folder)
checkpoint['questions'][qid]['next_status']='r02_primary_frozen_and_native_viewed'
write(OWN/'checkpoint.json',checkpoint)
