from own_bootstrap import *
from unit_tools import eligibility

preset=sys.argv[1]
assert preset in ('3','1')
variant='r10_three_with_true_one_four' if preset=='3' else 'r11_one_with_true_three_two'
d=OWN/'Solid166'/variant;d.mkdir(parents=True,exist_ok=False)
save(d/'eligibility_before_design.json',eligibility('Solid166'),exclusive=True)
m=load(OWN/'Solid166/primary_math.json')
redtarget=m['exhaustive_numbered_edge_test'][preset]['target']
blue_labels=['1','4'] if preset=='3' else ['3','2']
blue_targets=[m['exhaustive_numbered_edge_test'][k]['target'] for k in blue_labels]
assert m['exhaustive_numbered_edge_test'][blue_labels[0]]['folded_endpoints']==m['exhaustive_numbered_edge_test'][blue_labels[1]]['folded_endpoints']
assert not m['exhaustive_numbered_edge_test'][preset]['coincides_with_x']
targets=['netedge15',redtarget]+blue_targets
assert len(set(targets))==4
actions=[{'type':'set_object_style','target':t,'color':'#DC2626' if i<2 else '#2563EB'} for i,t in enumerate(targets)]
roles=[{'action_index':0,'target':'netedge15','source':'actual query boundaryx','use':'Defines the queried boundary as the comparison source.'},
 {'action_index':1,'target':redtarget,'source':'red query boundaryx','use':'Receiving original numbered boundary'+preset+' for the specific proposed false closure.'},
 {'action_index':2,'target':blue_targets[0],'source':'actual known folded seam at labelled boundary'+blue_labels[0],
   'use':'True closure source, derived independently by opposite-third-vertex fold propagation.'},
 {'action_index':3,'target':blue_targets[1],'source':'true folded endpoint pair of boundary'+blue_labels[0],
   'use':'Receiving boundary'+blue_labels[1]+' for the mathematically correct blue closure; gives a concrete comparison beside the red query pair.'}]
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
 'description':'Compare x with original edge'+preset+' in red and compare the true seam'+blue_labels[0]+'–'+blue_labels[1]+' in blue.',
 'intent':'Compare a specific queried closure with one independently verified real closure, preserving the paper net.',
 'params':{'actions':actions}}
save(d/'plugin.json',plugin,exclusive=True)
transfer={'primary_reference':'Solid203','primary_current_png_sha256':sha(TASK/'references/Solid203/C01.png'),
 'primary_current_plugin_sha256':sha(TASK/'references/Solid203/C01.json'),'actual_primary_method':'Current originalx and upper-leftC boundarypair, not legacy optionA.',
 'secondary_reference':'Plane308','secondary_current_png_sha256':sha(TASK/'references/Plane308/C01.png'),
 'secondary_current_plugin_sha256':sha(TASK/'references/Plane308/C01.json'),'actual_secondary_method':'Current true odd/even point groups red1/3/5 blue2/4/6, not legacy consecutive groups.',
 'migration':'Red compares actual queryx against printed edge'+preset+'. Blue compares the true folded seam'+blue_labels[0]+'–'+blue_labels[1]+', so both colors have a concrete source and recipient instead of isolated option salience.',
 'roles':roles,'all_nine_current_PNGs_actually_viewed':True,
 'minimality':'Four distinct original boundaries; exactly one source and one recipient per group; no overwritten or redundant attribute.',
 'human_semantics':'Blue seams truly coincide; red boundaries are a comparison, not a new equality or mating rule. Literal colored paper still folds to the same unique x–5 seam. No result-picture alternatives require preserving a displayed ink arrangement.'}
save(d/'reference_transfer.json',transfer,exclusive=True)
prior=[]
for p in sorted((OWN/'Solid166').glob('*/design.json')):
 r=p.parent/'manual_final_review.json'
 prior.append({'design_path':str(p),'sha256':sha(p),'png_sha256':sha(p.parent/'candidate.png'),
  'preset':load(p)['expected_wrong_answer'],'manual_review':str(r),'finals':[v['manual_final_value'] for v in load(r)['reviews']]})
audit={'question_id':'Solid166','all_parent_old_evidence_index':str(OWN/'history_selected.json'),'all_current_attempts':prior,
 'new_material_difference':'Adds the distinct true blue closure'+blue_labels[0]+'–'+blue_labels[1]+' to the redx–'+preset+' boundary hypothesis. The unanchored red pair and point-group representations have failed and are not repeated. The new blue pair contributes two independently verified folded endpoint identities and a concrete comparison relation; no existing action is merely recolored or widened.',
 'why_receiver_distinct_from_other_anchor_attempts':'The actual original paper receiver'+preset+' is neither the receiver of the previous supported red closure nor an interchangeable label. Its flat location and propagation path are different even where a different free paper edge closes to the same final octahedral edge.',
 'new_hypothesis':'A valid blue closure beside the redx–'+preset+' comparison may make the red pair appear like another closure, producing the single printed edge identifier'+preset+'.',
 'not_relabelled_from_prior_finals':True,'old_PNGs_preserved_and_not_retested':True}
save(d/'history_difference.json',audit,exclusive=True)
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':variant,'created_at':now(),
 'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number','expected_wrong_answer':preset,
 'preset_semantics':{'letter':None,'value':preset,'meaning':'The printed edge identifier'+preset+', not any ordinal face count.'},
 'information_hypothesis':audit['new_hypothesis'],
 'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
 'closure_math':{'query_x_endpoints':m['target_x']['world'],'red_receiver_endpoints':m['exhaustive_numbered_edge_test'][preset]['folded_endpoints'],
   'red_receiver_is_not_correct_seam':True,'blue_source_label':blue_labels[0],'blue_receiver_label':blue_labels[1],
   'blue_common_folded_endpoints':m['exhaustive_numbered_edge_test'][blue_labels[0]]['folded_endpoints'],
   'blue_closure_verified_exactly':True,'actual_unique_matching_edge':'5'},
 'plugin_sha256':sha(d/'plugin.json'),'reference_transfer_path':str(d/'reference_transfer.json'),
 'reference_transfer_sha256':sha(d/'reference_transfer.json'),'history_difference_path':str(d/'history_difference.json'),
 'history_difference_sha256':sha(d/'history_difference.json'),'eligibility_sha256':sha(d/'eligibility_before_design.json'),
 'human_semantics_and_mark_roles':roles,'paper_ink_reading':transfer['human_semantics'],
 'two_run_rule':'Exactly two own complete unambiguous final printed edge identifiers'+preset+' on this frozen PNG. No third call, relabel, retry, old-image replay or alternative-selection.',
 'scope':'PRIMARY only; no independent second review, approval, Pass, Collect or delivery.'}
save(d/'design.json',design,exclusive=True)
print('Frozen',variant,'preset',preset)
