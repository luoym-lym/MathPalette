from own_bootstrap import *
from unit_tools import eligibility
import copy

d=OWN/'Solid166/r07_antipodal_endpoint_x_two';d.mkdir(parents=True,exist_ok=False)
save(d/'eligibility_before_design.json',eligibility('Solid166'),exclusive=True)
ctx=load(OWN/'Solid166/context.json');math=load(OWN/'Solid166/primary_math.json')
world={tuple(v['flat']):tuple(v['world']) for f in math['folded_faces'].values() for v in f}
objs={o['id']:o for o in ctx['objects']}
actions=[];roles=[]
for group,edge in [('x','netedge15'),('two','netedge9')]:
 for raw in objs[edge]['geometry']['points']:
  p=tuple(raw[:2]);v=world[p]
  assert v[1]==0 and (abs(v[0])==1 or abs(v[2])==1)
  name='red' if abs(v[0])==1 else 'blue';color='#DC2626' if name=='red' else '#2563EB'
  snap=next(s for s in ctx['snap_points'] if tuple(s['xy'])==p)
  roles.append({'action_index':len(actions),'source_snap_id':snap['id'],'exact_original_projected_xy':snap['xy'],
    'original_edge':edge,'edge_identifier':'x' if group=='x' else '2','folded_vertex':v,'color':color,
    'source_and_use':'Query endpoint source for the antipodal-axis comparison.' if group=='x' else
       'Receiving point on upper free strip boundary2, compare its true antipodal-axis group with the matching-color query vertex.',
    'mathematical_group':'{+e1,-e1}' if name=='red' else '{+e3,-e3}'})
  actions.append({'type':'add_point','id':'antipodal_'+group+'_'+name,'xy':snap['xy'],'filled':True,'color':color,'size_pt2':50,'edge_linewidth_pt':1.0})
assert len({tuple(a['xy']) for a in actions})==4
for c in ('#DC2626','#2563EB'):
 vs=[r['folded_vertex'] for r in roles if r['color']==c];assert len(vs)==2 and tuple(-v for v in vs[0])==vs[1]
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
 'description':'Compare existing x and upper strip boundary2 using their real antipodal endpoint groups.',
 'intent':'Track endpoints across the free top rim and bottom flap without identifying opposite vertices.',
 'params':{'actions':actions}}
save(d/'plugin.json',plugin,exclusive=True)
transfer={'primary_reference':'Solid203','primary_current_png_sha256':sha(TASK/'references/Solid203/C01.png'),
 'primary_current_plugin_sha256':sha(TASK/'references/Solid203/C01.json'),
 'actual_primary_method':'Current x/C concrete-boundary comparison, not legacy optionA.',
 'secondary_reference':'Plane308','secondary_current_png_sha256':sha(TASK/'references/Plane308/C01.png'),
 'secondary_current_plugin_sha256':sha(TASK/'references/Plane308/C01.json'),
 'actual_secondary_method':'True current odd1/3/5 red and even2/4/6 blue point classes.',
 'migration':'Group the actual endpoint vertices of x and upper free strip edge2 by antipodal axis: red+-e1 and blue+-e3. Unlike the earlier far terminal flap3, this asks for comparison across the strip from a free upper-rim boundary to the hanging bottom flap.',
 'roles':roles,'all_nine_current_PNGs_actually_viewed':True,
 'minimality':'Four distinct original vertices, one source and receiver per true antipodal group. No redundant marks or added lines.',
 'human_semantics':'Colored paper dots do not alter edge coincidence and are not a required matching rule. Opposite vertices can carry identical ink while staying distinct. The actual seam is uniquely5.'}
save(d/'reference_transfer.json',transfer,exclusive=True)
prior=[]
for p in sorted((OWN/'Solid166').glob('*/design.json')):
 m=p.parent/'manual_final_review.json'
 prior.append({'path':str(p),'design_sha256':sha(p),'image_sha256':sha(p.parent/'candidate.png'),
  'preset':load(p)['expected_wrong_answer'],'manual_review_path':str(m),'finals':[r['manual_final_value'] for r in load(m)['reviews']]})
audit={'question_id':'Solid166','parent_old_full_history':str(OWN/'history_selected.json'),'all_current_attempts':prior,
 'new_material_difference':'Receiver moves from actual left terminal-flap edge3 to actual top strip boundary2. Those edges close together in the correct fold but have distinct original paper vertices and different propagation routes. Both target2 endpoints are newly marked and both former edge3 receiver markers are absent; the visual relation is across-strip closure rather than end-to-end flap closure. This is not a recoloring, line-width change, renaming or relabel of an old image.',
 'new_concrete_hypothesis':'True antipodal-axis endpoint classes across the strip may be mistaken for vertex identities, causing the specifically bounded upper rim edge2 to be chosen.',
 'prior_ambiguous_1_or_2_not_counted_as2':True,'no_retest_or_relabel':True}
save(d/'history_difference.json',audit,exclusive=True)
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':d.name,'created_at':now(),
 'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number','expected_wrong_answer':'2',
 'preset_semantics':{'letter':None,'value':'2','meaning':'Printed identifier2 on the upper free strip boundary.'},
 'information_hypothesis':audit['new_concrete_hypothesis'],
 'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
 'endpoint_math':{'red_group':[[-1,0,0],[1,0,0]],'blue_group':[[0,0,1],[0,0,-1]],
  'both_groups_true_antipodal_not_identical_vertices':True,'x_folded_edge':[[-1,0,0],[0,0,1]],
  'edge2_folded_edge':[[1,0,0],[0,0,-1]],'unique_actual_matching_edge':'5'},
 'plugin_sha256':sha(d/'plugin.json'),'reference_transfer_path':str(d/'reference_transfer.json'),
 'reference_transfer_sha256':sha(d/'reference_transfer.json'),'history_difference_path':str(d/'history_difference.json'),
 'history_difference_sha256':sha(d/'history_difference.json'),'eligibility_sha256':sha(d/'eligibility_before_design.json'),
 'human_semantics_and_mark_roles':roles,'paper_ink_reading':transfer['human_semantics'],
 'two_run_rule':'Exactly two complete original quicktest3 final edge identifiers2, no alternatives, third call, relabel, retry or reused failed PNG.',
 'scope':'PRIMARY only, no independent second review, approval, Pass, Collect or delivery.'}
save(d/'design.json',design,exclusive=True)
print('Frozen',d.name)
