from research import *
folder=HERE/'Plane280/unit_to_double_span'
write(folder/'primary_visual_review.json',{
    'question_id':'Plane280','actual_candidate_png_viewed':True,'decision':'REJECT_BEFORE_API','api_calls':0,
    'reason':'The formal PNG identifies the asked path by black-versus-grey contrast. Actual frozen artist widths for both grid0 andthick3 are1pt; semantic_linewidth_pt2.5 in scene metadata is not the executed stroke width. Recoloringthick3 red removes its membership cue while a non-target grid0 is also red and same width. A human cannot reliably infer which red edge remains part of the asked thick path from the finalPNG alone. The mechanism therefore fails the nonambiguity gate.',
    'design_metadata_correction':'The immutable untested design says original2.5pt width for thick3. This is incorrect for actual renderer output; target_paths.json records the actual1pt frozen style. The tested image/design are not altered; candidate is rejected and never sent to the solver.',
    'math':'Original answer is uniquelyB=18cm, from9 square-side units times2cm. Geometry/fills/labels are preserved, but that does not cure the target-membership ambiguity.',
    'markers':[
        {'target':'grid0','color':'#DC2626','intended_role':'One-unit visual reference; actual1pt original width.'},
        {'target':'thick3','color':'#DC2626','intended_role':'Two-unit path span matched to reference; actual1pt width and removal of black path cue undermine clarity.'}],
    'new_design_recommendation':'Do not retest this identicalPNG. No clean redesign was identified within the root assignment.',
    'independent_second_review_performed':False})
write(HERE/'root_results.json',{'assessed_question_ids':['Plane224','Plane280','Solid206','Solid247'],'assessed_count':4,'prescreen_only':['Plane224','Solid206','Solid247'],'rendered_then_rejected_pre_api':['Plane280'],'saved_candidate_count':1,'complete_pair_tests':0,'completed_calls':0,'credible_two_hit_candidates':[],'primary_review_paths':[str(HERE/q/'primary_prescreen.json') for q in ['Plane224','Plane280','Solid206','Solid247']]+[str(folder/'primary_visual_review.json')],'no_live_root_api_processes':True})
print('Root4 assessments recorded;1 pre-API rejected render;0 API calls.')
