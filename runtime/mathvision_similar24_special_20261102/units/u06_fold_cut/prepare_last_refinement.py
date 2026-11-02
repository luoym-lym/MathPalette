from local_env import *
from api_gate import check_eligibility
qid='Plane220';vid='false_mirror_extremity_pair';candidate=OWN/qid/vid
ev=check_eligibility(qid,'before_new_axis_extremity_design')
assert ev['eligible'],ev['reasons']
save(candidate/'eligibility_before_design.json',ev,True)
p=read_json(OWN/qid/'raw_paths.json')['o11'][0];n=len(p['segments'])
def part(first,end):
    return {'type':'set_object_style','target':'o11','color':'#DC2626',
      'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':first/n,'end':end/n,'wrap':False}}
actions=[{'type':'set_object_style','target':'o10','color':'#2563EB'},part(19,31),part(50,56)]
save(candidate/'plugin.json',{'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
 'description':vid,'intent':'Compare two proposed reflected extremities about the existing dotted fold; keep the actual cut unchanged.',
 'params':{'actions':actions}},True)
first=OWN/qid/'nested_mirror_component_duplication'
save(candidate/'mathematics.json',read_json(first/'mathematics.json'),True)
roles=[
 {'action_index':0,'source':'C original dotted vertical fold axis','receiver':'The two red extremity neighborhoods on opposite sides (actions 1,2)',
  'information':'Blue identifies the existing proposed reflection axis. It adds neither a new fold nor a paper-boundary condition.','necessity':'Locates which opposite-side relation the red pair compares.'},
 {'action_index':1,'source':'C far-left smooth curved extremity','receiver':'C far-right zigzag (action 2)',
  'information':'Red supplies one side of a proposed mirror-extremity pair. The smooth arc shape, lack of left zigzag and different distance to the fold remain visible, so a human can reject the proposed match.',
  'necessity':'One concrete extremity counterpart, not a whole-oval style.'},
 {'action_index':2,'source':'C far-right three-point zigzag','receiver':'C smooth far-left extremity (action 1)',
  'information':'Same-red opposite-side pairing invites color-category correspondence to substitute for the actual reflected contour. Preset C follows this false mirror-pair rule.',
  'necessity':'Completes the explicit opposite-side comparison. The source star is uncolored and unchanged.'}]
save(candidate/'reference_transfer.json',{'current_nine_read_inventory':str(OWN/'reference_read_inventory.json'),
 'current_nine_PNGs_actually_viewed':True,'primary_refs':['Solid142','Solid167'],'supplemental_ref':'Solid176',
 'migration':'Transfer concrete counterpart edge comparison. Use the pre-existing option reflection axis as source of correspondence and pair two actual opposite-side extremity features. Current Solid176 also compares actual edges within one option. No new source paper colors, text, cuts or folds.',
 'old18_not_authority':True},True)
save(candidate/'history_difference_audit.json',{'question_id':qid,
 'difference':'Old C used red source star / blue source arcs copied to the full C star/oval, a one-sided profile-copy error. This C design leaves the source wholly unchanged, adds the actual C dotted fold as the blue correspondence anchor, and pairs only the left curved extremity and right star in the SAME red class as purported mirror partners. It is a false reflection-pair hypothesis, not source-profile copying, not a palette/width swap, and not reusing any old PNG. Initial new E tested local-completion duplication; B tested near-tangent connectivity. Neither supplied this axis-to-two-different-extremities relation. Preset C comes from that predeclared proposed mirror pairing; no prior new final has selected C on a Plane220 image.',
 'old_full_read_inventory':str(OWN/qid/'history_files_read.json'),
 'previous_new_reviews':[str(OWN/qid/v/'manual_full_final_review.json') for v in ['nested_mirror_component_duplication','near_tangent_fold_contact_alias']],
 'new_hypothesis_not_postoutput_relabel':True},True)
save(candidate/'premodel_primary_reasoning.json',{'created_at':now(),'question_id':qid,'variant_id':vid,
 'expected_wrong_answer':'C','expected_wrong_value':'C','formal_correct_answer':'D','each_action_role':roles,
 'human_semantics_both_readings':'Source and D stay exactly original. C remains impossible because its left smooth end is not the mirror of its right zigzag, even if the red pair is literal ink. D is unchanged and uniquely equals the actual one-fold reflection. The blue line is an already printed dotted fold instruction. Color creates no new equality condition, no new fold, no literal ink requirement on the source, and no alternative valid answer.',
 'conciseness':'Three disjoint color-only actions: one existing axis, one left curve neighborhood, one right zigzag. Original 1pt and all boundary samples are retained. No new points/lines/text/fill and no full-option color.',
 'primary_only':True,'new_candidate_calls_at_creation':0,
 'prior_unit_requests':len(list(OWN.glob('*/*/actual_call_*_payload_gate.json'))),'native_candidate_visual_review_pending':True},True)
entry={'question_id':qid,'variant_id':vid,'expected_wrong_answer':'C','correct_answer':'D','candidate_directory':str(candidate)}
manifest=read_json(OWN/'supplementary_design_manifest.json');manifest.append(entry)
save(OWN/'supplementary_design_manifest.json',manifest)
save(OWN/'last_refinement_manifest.json',[entry],True)
print(entry)
