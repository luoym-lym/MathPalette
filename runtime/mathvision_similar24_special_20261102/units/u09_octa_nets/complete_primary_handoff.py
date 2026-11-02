from own_bootstrap import *
from unit_tools import eligibility

d=OWN/'Solid166/r12_full_seam_context_x_four'
manual=load(d/'manual_final_review.json');assert manual['double_hit']
design=load(d/'design.json');transfer=load(d/'reference_transfer.json')
gate=load(d/'render_gate.json');replay=load(d/'independent_replay_gate.json')
assert design['expected_wrong_answer']=='4' and manual['correct_answer']=='5'
review={'question_id':'Solid166','variant_id':d.name,'reviewed_at':now(),
 'review_role':'PRIMARY researcher; no independent second review has been performed.',
 'decision':'PRIMARY_CANDIDATE_PENDING_NEW_INDEPENDENT_REVIEW',
 'candidate_directory':str(d),'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),
 'design_sha256':sha(d/'design.json'),'correct_answer':'5','frozen_wrong_preset':design['preset_semantics'],
 'original_mathematics':{'proof_path':str(OWN/'Solid166/primary_math.json'),'proof_sha256':sha(OWN/'Solid166/primary_math.json'),
   'method':'Independent adjacent-face propagation on the actual8equilateral original triangles. Across an octahedron edge, replace the third axis vertex by its negative; obtain all8distinct faces and6vertices. Exhaustively compare both folded endpoints of all numbered edges1..5 withx.',
   'unique_derived_answer':'5','world_projection_and_frozen_visibility_separately_verified':True,
   'complete_true_free_seam_path':str(OWN/'Solid166/all_true_free_seams.json')},
 'information_and_native_human_review':{
   'actual_candidate_PNG_viewed':True,'native_768x768_opaque':True,
   'visual_review_path':str(d/'primary_visual_review.json'),'group_legibility_path':str(d/'primary_color_group_legibility.json'),
   'reference_transfer_path':str(d/'reference_transfer.json'),'reference_transfer_sha256':sha(d/'reference_transfer.json'),
   'actual_current_user9_reference_read_audit':str(OWN/'current_nine_reference_read_audit.json'),
   'main_current_reference':'Solid203 actualx/C red original-boundary pair, not legacyx/A.',
   'all8mark_roles':transfer['roles'],'groups':transfer['groups'],
   'why_extra_marks_are_useful':'Blue, green and orange are three distinct true free-boundary closures, verified by actual folded endpoint equality. They show separate numbered, upper-flap and lower-flap routes. Red compares queriedx with specific boundary4. Each source/recipient edge has one color-only action; no duplicated, overwritten or inert operation.',
   'human_unique_reading':'The question asks for a numbered geometric seam, not a matching colored result picture. If every color stroke is literal ink attached to the paper, the convex fold remains unchanged and no condition requires equal ink to coincide. x still joins5; redx–4 remains only a comparison. There are no new cut lines, partitions, regions, symbols, points or labels.',
   'source_gray_fill_numbers_labels_visibility_and_right_shape':'Retained exactly by official color-only plugin operations; no original geometry, projection, frozen visibility or glyph is edited.'},
 'legal_render_gates':{'fresh_schema_and_exact_default_normalization':True,'noop_pixels_equal_formal':True,
   'repeat_candidate_bytes_equal':True,'independent_new_process_exact_replay':True,
   'first_process_PID':gate['pid'],'independent_replay_PID':replay['pid'],
   'render_gate_path':str(d/'render_gate.json'),'replay_gate_path':str(d/'independent_replay_gate.json'),
   'renderer':'Original delivery_bridge_adapter.RendererAdapter + formal render_plugins.PluginRenderer; original runtime_isolation memory-only temp redirection and strictOWNROOTwriteguard.',
   'schema_sha256':gate['source']['SolidGeometry/workbench/plugin.schema.json']},
 'transport_and_full_final_review':{
   'manual_review_path':str(d/'manual_final_review.json'),'manual_review_sha256':sha(d/'manual_final_review.json'),
   'summary_path':manual['summary_path'],'summary_sha256':manual['summary_sha256'],
   'own_complete_final_values':['4','4'],'final_letters':[None,None],
   'both_complete_nontruncated':True,'only_two_calls_on_this_frozen_PNG':True,
   'call_1_pre_network_eligibility':str(d/'tests/pre_network_run_01.json'),
   'call_2_pre_network_eligibility':str(d/'tests/pre_network_run_02.json'),
   'payload':'Original formal question and exactsamePNG only, original system/mimo-v2.6-flash/thinking.disabled/private credentials/timeoutNone/no max_tokens; no control or diagnostic API calls.',
   'harness_copy_integrity_path':str(OWN/'harness/copy_integrity.json'),
   'mechanism_scope':'Run1 commits4 via a mistaken strip closure; run2 commits4 while describing red edges and inconsistent pole/vertex geometry. These texts are not mathematical proof and do not establish that every extra group caused the error. The result supports only the two observed frozen-preset finals.'},
 'history_and_novelty':{'full_assigned_old_history_path':str(OWN/'history_selected.json'),
   'full_raw_read_audit_path':str(OWN/'history_read_audit.json'),
   'frozen_pretest_history_difference_path':str(d/'history_difference.json'),
   'material_novelty':'Compared with r08 redx–4/blue3–2, this adds two actual verified seam correspondences: green netedge5–netedge14 and orange netedge8–netedge16. No previously failed PNG is repeated or relabelled.',
   'strict_failures_kept':'Every earlier attempt remains failed. r05 two3 finals are not a preset4 hit; r09 initial1 is not its final3; ambiguous alternatives and off-query edge-pair conclusions are not hits.'},
 'current_eligibility':eligibility('Solid166'),
 'source_preservation_final_path':str(OWN/'source_preservation_final.json'),
 'process_cleanup_path':str(OWN/'process_cleanup.json'),
 'limitations':['Only these two observations; no population success rate, causal gain or per-marker effect is established.',
    'A new independent reviewer must recheck the complete original mathematics, native PNG, individual mark roles, human semantics, full raw finals and all binding hashes.',
    'This is not a second review, user approval, Special Pass/Collect or delivery.',
    'Solid240 is a separately documented original-orientation uniqueness hold and has0newAPIcalls.']}
save(d/'primary_review.json',review,exclusive=True)
queue=load(OWN/'second_review_queue.json');assert len(queue)==1 and queue[0]['variant_id']==d.name
queue[0]['manual_final_review_path']=str(d/'manual_final_review.json')
queue[0]['primary_review_path']=str(d/'primary_review.json')
queue[0]['primary_review_sha256']=sha(d/'primary_review.json')
queue[0]['source_preservation_final_path']=str(OWN/'source_preservation_final.json')
queue[0]['all_true_free_seams_path']=str(OWN/'Solid166/all_true_free_seams.json')
queue[0]['color_group_legibility_path']=str(d/'primary_color_group_legibility.json')
queue[0]['process_cleanup_path']=str(OWN/'process_cleanup.json')
save(OWN/'second_review_queue.json',queue)
cp=load(OWN/'checkpoint.json');cp.update(updated_at=now(),phase='source_preservation_and_process_cleanup')
cp['questions']['Solid166']['primary_review_path']=str(d/'primary_review.json')
save(OWN/'checkpoint.json',cp)
print('PRIMARY handoff evidence assembled; independent second review still pending.')
