from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,stamp
from prepare import SPECS
import json

for q,s in SPECS.items():
    d=HERE/q/s['id']
    markers=read(d/'marker_geometry_audit.json')
    result={'question_id':q,'variant_id':s['id'],'time':stamp(),'review_type':'PRIMARY actual native image review; not an independent second review','source_JPG_formal_PNG_old_candidate_and_new_candidate_actually_viewed':True,'candidate_sha256':sha(d/'candidate.png'),'all_original_labels_dimensions_and_geometry_readable':True,'unique_formal_answer_proof':str(HERE/q/'primary_math_native.json'),'every_marker':markers,'same_color_not_a_new_numerical_equality':True,'human_semantics':s['semantics'],'material_difference':s['difference'],'new_markers_useful_targeted_source_receiver_information':True,'no_arbitrary_marker_cap':True,'no_added_text_arrows_relations_faces_paint_targets_routes_or_fixed_partitions':True,'no_isolated_wrong_option_salience':True,'render_audit':str(d/'render_check.json'),'fresh_offline_replay_required_before_API':True,'global_frozen_image_zero_call_scan':str(HERE/'frozen_images_zero_prior_request_audit.json'),'limits':['Error mechanism is a prospective hypothesis, not a demonstrated causal route.','No statistical improvement, human study, per-marker necessity or original-control correctness is claimed or imposed.','Any exact2hit possibility remains PRIMARY and requires a NEW independent parent review before delivery.']}
    if q=='Solid227':
        result['native_findings']='Source radial10 ends at the rim; axial5 remains beside left silhouette. C axial10 is red and radial5 blue, leaving the top ellipse/center-to-rim endpoint and height/radius distinction visible. The labels5/10 and A-D captions remain unchanged. No other option geometry is highlighted or obscured. Red10 and blue5 comparisons are true numerical correspondences across different geometric roles; a careful reader applies squared radius and findsB.'
    else:
        result['native_findings']='Every colored pair marks adjacent existing edges of a real unit top face. C/B/A use front-width plus left-depth; D uses visible rear-width plus right-depth because its front is occluded. All four output labels and heights1/2,1/3,1/17 are readable, the four slab count and stepped outline remain clear, and the continuous bottom edge remains visible. No hidden edge is exposed, no face receives fill, and marking only the top faces does not stipulate that the unmarked bottoms are absent or uncounted. Total-area question still uniquely gives11.'
    save(d/'primary_review.json',result)
print('Both actual native primary reviews saved; no independent review or approval')
