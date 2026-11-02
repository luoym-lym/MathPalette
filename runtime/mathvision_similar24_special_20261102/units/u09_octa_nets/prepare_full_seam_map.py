from own_bootstrap import *
from unit_tools import eligibility

preset=sys.argv[1];assert preset in ('4','3','2','1')
num={'4':'12','3':'13','2':'14','1':'15'}[preset]
d=OWN/'Solid166'/('r'+num+'_full_seam_context_x_'+{'4':'four','3':'three','2':'two','1':'one'}[preset])
d.mkdir(parents=True,exist_ok=False)
save(d/'eligibility_before_design.json',eligibility('Solid166'),exclusive=True)
m=load(OWN/'Solid166/primary_math.json')
edge_world=m['all_net_edge_endpoints']
receiver=m['exhaustive_numbered_edge_test'][preset]['target']
blue=['netedge13','netedge9'] if preset in ('4','1') else ['netedge11','netedge2']
groups=[{'name':'red_query_comparison','color':'#DC2626','edges':['netedge15',receiver],'truth':'proposed comparison, not a true seam'},
 {'name':'blue_numbered_true_closure','color':'#2563EB','edges':blue,'truth':'true folded seam'},
 {'name':'green_top_flap_true_closure','color':'#16A34A','edges':['netedge5','netedge14'],'truth':'true folded seam'},
 {'name':'orange_bottom_flap_true_closure','color':'#EA580C','edges':['netedge8','netedge16'],'truth':'true folded seam'}]
assert edge_world['netedge15']!=edge_world[receiver]
for g in groups[1:]:
 a,b=g['edges'];assert edge_world[a]==edge_world[b]
assert len({e for g in groups for e in g['edges']})==8
actions=[];roles=[]
for g in groups:
 for i,target in enumerate(g['edges']):
  roles.append({'action_index':len(actions),'target':target,'group':g['name'],'color':g['color'],
   'source_or_recipient':'source' if i==0 else 'recipient','source_object':g['edges'][0],
   'folded_endpoints':edge_world[target],'relation_truth':g['truth'],
   'use':('Query-boundary comparison against the particular printed edge'+preset+'. No equality condition is added.' if g==groups[0] else
       'Tracks one side of a verified actual free-boundary seam, providing a distinct top/bottom flap closure reference for orienting the red query pair.')})
  actions.append({'type':'set_object_style','target':target,'color':g['color']})
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
 'description':'Compare x with edge'+preset+' in red, using three independently verified true seam pairs as color-group references.',
 'intent':'Trace specific original free-boundary correspondences of the same folded octahedron without changing the net.',
 'params':{'actions':actions}}
save(d/'plugin.json',plugin,exclusive=True)
transfer={'primary_reference':'Solid203','primary_current_png_sha256':sha(TASK/'references/Solid203/C01.png'),
 'primary_current_plugin_sha256':sha(TASK/'references/Solid203/C01.json'),'actual_primary_method':'Current user C01 compares originalx with upper-leftC in red; old optionA is not used.',
 'method_transfer':'Extend the actual-boundary source/recipient correspondence method to four distinct groups. The query pair is red; the three other groups are exact true folded seams independently established from the original net. Each extra pair supplies new geometric closure information, not isolated wrong-option salience.',
 'palette_authority':'Four fixed schema-whitelisted colors; green and orange are new explicit seam-group roles in this design, not colors inherited from any old18 delivery.',
 'all_nine_current_PNGs_actually_viewed':True,'groups':groups,'roles':roles,
 'proof_of_extra_information_path':str(OWN/'Solid166/all_true_free_seams.json'),
 'proof_of_extra_information_sha256':sha(OWN/'Solid166/all_true_free_seams.json'),
 'minimality':'Eight distinct existing boundary edges, two per useful comparison group. One color-only action per target, no repeated attributes, no linewidth or linestyle changes. No added lines, points, labels, regions or cuts.',
 'human_semantics':'All colored segments are actual original outer paper boundaries, not new internal subdivisions. Three paired seams are true. The red pair is a comparison, not a requirement that matching ink must meet. Ink on the paper preserves the unique geometric seamx–5.'}
save(d/'reference_transfer.json',transfer,exclusive=True)
prior=[]
for p in sorted((OWN/'Solid166').glob('*/design.json')):
 r=p.parent/'manual_final_review.json'
 prior.append({'path':str(p),'sha256':sha(p),'png_sha256':sha(p.parent/'candidate.png'),
  'preset':load(p)['expected_wrong_answer'],'manual_review':str(r),'finals':[v['manual_final_value'] for v in load(r)['reviews']]})
audit={'question_id':'Solid166','old_full_history_index':str(OWN/'history_selected.json'),'all_current_attempts':prior,
 'new_material_difference':'The green free seam netedge5–netedge14 and orange free seam netedge8–netedge16 are new, independently proved source/recipient correspondences. They locate top and bottom flap closures that none of the simpler failed comparisons encoded. This changes available folding information and the orientation hypothesis; it is not cosmetic styling or an extra call on a failed PNG.',
 'specific_error_hypothesis':'The three real closure pairs may establish a perceived color-pair closure system, causing the remaining red comparison to be accepted as another closure and the specific receiving edge'+preset+' to be selected.',
 'previous_frozen_images_and_presets_preserved':True,'no_arbitrary_mark_count_limit_or_complexity_shortcut':True}
save(d/'history_difference.json',audit,exclusive=True)
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':d.name,'created_at':now(),
 'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number','expected_wrong_answer':preset,
 'preset_semantics':{'letter':None,'value':preset,'meaning':'Printed original boundary identifier'+preset+'.'},
 'information_hypothesis':audit['specific_error_hypothesis'],
 'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
 'all_true_free_seams_path':str(OWN/'Solid166/all_true_free_seams.json'),'all_true_free_seams_sha256':sha(OWN/'Solid166/all_true_free_seams.json'),
 'closure_math':{'query_x':edge_world['netedge15'],'red_receiver':edge_world[receiver],
  'blue_true_seam':{'objects':blue,'equal_endpoints':edge_world[blue[0]]},
  'green_true_seam':{'objects':['netedge5','netedge14'],'equal_endpoints':edge_world['netedge5']},
  'orange_true_seam':{'objects':['netedge8','netedge16'],'equal_endpoints':edge_world['netedge8']},
  'unique_actual_matching_edge':'5'},
 'plugin_sha256':sha(d/'plugin.json'),'reference_transfer_path':str(d/'reference_transfer.json'),
 'reference_transfer_sha256':sha(d/'reference_transfer.json'),'history_difference_path':str(d/'history_difference.json'),
 'history_difference_sha256':sha(d/'history_difference.json'),'eligibility_sha256':sha(d/'eligibility_before_design.json'),
 'human_semantics_and_mark_roles':roles,'paper_ink_reading':transfer['human_semantics'],
 'two_run_rule':'Exactly two complete unambiguous own quicktest3 final edge identifiers'+preset+' on this distinct frozen PNG; no third call, relabel, retry or failed-image repeat.',
 'scope':'PRIMARY only; no independent second review, approval, Pass, Collect or delivery.'}
save(d/'design.json',design,exclusive=True)
print('Frozen',d.name,'preset',preset,'useful_actions',len(actions))
