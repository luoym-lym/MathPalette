from own_bootstrap import *
from unit_tools import eligibility

directory=OWN/'Solid166/r06_antipodal_endpoint_x_three'
directory.mkdir(parents=True,exist_ok=False)
save(directory/'eligibility_before_design.json',eligibility('Solid166'),exclusive=True)
math=load(OWN/'Solid166/primary_math.json');context=load(OWN/'Solid166/context.json')
world={tuple(v['flat']):tuple(v['world']) for f in math['folded_faces'].values() for v in f}
objects={o['id']:o for o in context['objects']}
actions=[];roles=[]
for group,edge in [('x','netedge15'),('three','netedge13')]:
    for raw in objects[edge]['geometry']['points']:
        p=tuple(raw[:2]);v=world[p]
        assert v[1]==0 and (abs(v[0])==1 or abs(v[2])==1)
        color_name='red' if abs(v[0])==1 else 'blue'
        color='#DC2626' if color_name=='red' else '#2563EB'
        snap=next(s for s in context['snap_points'] if tuple(s['xy'])==p)
        i=len(actions)
        actions.append({'type':'add_point','id':'antipodal_'+group+'_'+color_name,'xy':snap['xy'],
            'filled':True,'color':color,'size_pt2':50,'edge_linewidth_pt':1.0})
        roles.append({'action_index':i,'source_snap_id':snap['id'],'exact_original_projected_xy':snap['xy'],
            'original_edge':edge,'edge_identifier':'x' if group=='x' else '3','folded_vertex':v,'color':color,
            'source_and_use':('Query vertex source for its octahedral antipodal-axis group.' if group=='x' else
              'Receiving original edge3 vertex on the same antipodal axis as the matching-color query endpoint; compare opposite vertices without asserting they coincide.'),
            'mathematical_group':'{+e1,-e1}' if color_name=='red' else '{+e3,-e3}'})
assert len({tuple(a['xy']) for a in actions})==4
for color in ('#DC2626','#2563EB'):
    vs=[r['folded_vertex'] for r in roles if r['color']==color]
    assert len(vs)==2 and tuple(-v for v in vs[0])==vs[1]
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
 'description':'Compare the original x and3 boundaries through their two pairs of antipodal octahedral vertices.',
 'intent':'Group actual vertices by antipodal axis and track the candidate boundary endpoints.',
 'params':{'actions':actions}}
save(directory/'plugin.json',plugin,exclusive=True)
transfer={'primary_reference':'Solid203','primary_current_png_sha256':sha(TASK/'references/Solid203/C01.png'),
 'primary_current_plugin_sha256':sha(TASK/'references/Solid203/C01.json'),
 'actual_primary_method':'Current user image pairsx and upper-left C, not old optionA.',
 'secondary_reference':'Plane308','secondary_current_png_sha256':sha(TASK/'references/Plane308/C01.png'),
 'secondary_current_plugin_sha256':sha(TASK/'references/Plane308/C01.json'),
 'actual_secondary_method':'Current source points1/3/5 are red and2/4/6 blue; a real group classification, not the legacy consecutive-number grouping.',
 'migration':'Use the concrete upper-left boundary comparison from current203, rebound to numbered edge3 in Solid166. Refine it into red/blue original-vertex groups that are independently proved antipodal pairs, transferring the genuine group-comparison aspect of current308. Same-colored antipodal vertices are compared, not identified.',
 'roles':roles,'all_nine_current_PNGs_actually_viewed':True,
 'minimality':'Four distinct original vertex markers, one source and one receiver per true antipodal group. No recolored line, extra edge, label, cut, equality sign or redundant action.',
 'human_semantics':'Antipodal color classes do not change the net or declare equal vertices. Literal ink at these four vertices is compatible with the same physical octahedron and the same unique edge5 seam. Color-matching is not an assembly condition in the question.'}
save(directory/'reference_transfer.json',transfer,exclusive=True)
prior=[]
for p in sorted((OWN/'Solid166').glob('*/design.json')):
    m=p.parent/'manual_final_review.json'
    prior.append({'design_path':str(p),'design_sha256':sha(p),'image_sha256':sha(p.parent/'candidate.png'),
      'preset':load(p)['expected_wrong_answer'],'manual_final_review_path':str(m),
      'observed_finals':[r['manual_final_value'] for r in load(m)['reviews']]})
audit={'question_id':'Solid166','all_old_designs_and_raw_index':str(OWN/'history_selected.json'),'all_current_attempts':prior,
 'new_material_difference':'The receiver is the actual edge3 with its top-flap apex, rather than edge4 with its lower-left strip vertex. The former blue identity pair is replaced with a distinct antipodal (+e3,-e3) group. Now BOTH color groups are true antipodal-axis comparisons. This changes vertex identity, incidence of the selected boundary and mathematical grouping; it is not a width/color/filename-only change.',
 'old_r05_disposition':'r05 observed3 twice but preset4, so it remains a failed candidate. Its frozen image, design and two responses are unchanged and cannot be relabelled or reused.',
 'why_new_preset3':'The new receiving boundary between the selected red/blue original vertices is printed edge3, as in the concrete current203 upper-left comparison. The expected error is confusing same-axis opposite vertices for identical folded vertices, hence selecting this specific marked boundary3.',
 'no_retest_of_any_failed_image':True}
save(directory/'history_difference.json',audit,exclusive=True)
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':directory.name,'created_at':now(),
 'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number','expected_wrong_answer':'3',
 'preset_semantics':{'letter':None,'value':'3','meaning':'The printed edge identifier3, whose two actual endpoints receive the two color groups.'},
 'information_hypothesis':'The pair of real antipodal-axis classes may be misread as two vertex-identification pairs, making x and the marked upper-left boundary3 look like one closure seam. The geometric shortcut specifically predicts3 on this new endpoint presentation.',
 'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
 'endpoint_math':{'red_group':[[-1,0,0],[1,0,0]],'blue_group':[[0,0,1],[0,0,-1]],
    'both_are_true_antipodal_pairs':True,'each_pair_is_distinct_not_coincident':True,
    'x_folded_edge':[[-1,0,0],[0,0,1]],'edge3_folded_edge':[[1,0,0],[0,0,-1]],
    'unique_actual_matching_edge':'5','exhaustive_1_to_5_endpoint_test_path':str(OWN/'Solid166/primary_math.json')},
 'plugin_sha256':sha(directory/'plugin.json'),'reference_transfer_path':str(directory/'reference_transfer.json'),
 'reference_transfer_sha256':sha(directory/'reference_transfer.json'),'history_difference_path':str(directory/'history_difference.json'),
 'history_difference_sha256':sha(directory/'history_difference.json'),'eligibility_sha256':sha(directory/'eligibility_before_design.json'),
 'human_semantics_and_mark_roles':roles,
 'paper_ink_reading':'Ink remains at unchanged original vertices. There is no requirement to identify equal-colored ink. True seam remains5 even when all dots are treated as intrinsic paper marks.',
 'two_run_rule':'Exactly two original isolated quicktest3 runs. Only two complete unambiguous final edge identifiers3 qualify. No third call, alternative-selection, relabelling, retry or failed-input replay.',
 'scope':'PRIMARY research only; independent second review belongs to parent; no approval/Pass/Collect/delivery.'}
save(directory/'design.json',design,exclusive=True)
print('Frozen antipodal endpoint candidate',directory.name)
