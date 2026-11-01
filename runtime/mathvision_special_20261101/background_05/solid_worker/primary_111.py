from tools_local import *
folder=TASK/'Solid111/local_corner_to_wrong_net'
write(folder/'primary_visual_math_review.json',{
 'question_id':'Solid111','variant_id':folder.name,'review_role':'Primary researcher; not independent second review',
 'reviewed_at':datetime.now(timezone.utc).isoformat(),'actual_candidate_png_viewed':True,
 'visual_evidence':'Viewed the actual 768x768 candidate. All A-E labels, six-face layouts, H crosshatching, original white and gray semantic fills remain distinguishable. Seven colored seam strokes align with original edges, with no new edges or text. The blue pair shows two free boundaries; no colored point changes a count.',
 'unchanged_unique_answer':'E, proved by all three opposite-face comparisons on all five folded nets in math_fold_audit.json. D is H/H, W/G, W/G and fails two pairs.',
 'targeted_information':'Each source seam has one matching net hinge or closing pair. The marks form the same H/W/G local corner in D under a proper rotation. This supplies a real necessary local match whose sufficiency is the intended mistake; it does not merely color the option label or contour.',
 'every_mark_has_role':True,'labels_clear':True,'no_false_explicit_condition':True,'semantic_fills_preserved':True,
 'world_geometry_projection_visibility_unchanged':True,'eligible_for_initial_two_calls':True,
 'limits':['No original control or ablation; cannot establish causal contribution of individual strokes.','Human readability is a primary visual assessment, not a human performance measurement.','Parent must obtain new independent review before delivery.']})
