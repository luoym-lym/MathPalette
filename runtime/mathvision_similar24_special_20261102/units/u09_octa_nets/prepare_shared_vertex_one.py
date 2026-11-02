from own_bootstrap import *
from unit_tools import eligibility

d=OWN/'Solid166/r09_shared_vertex_x_one';d.mkdir(parents=True,exist_ok=False)
save(d/'eligibility_before_design.json',eligibility('Solid166'),exclusive=True)
ctx=load(OWN/'Solid166/context.json');math=load(OWN/'Solid166/primary_math.json')
world={tuple(v['flat']):tuple(v['world']) for f in math['folded_faces'].values() for v in f}
objs={o['id']:o for o in ctx['objects']}
x=[tuple(p[:2]) for p in objs['netedge15']['geometry']['points']]
one=[tuple(p[:2]) for p in objs['netedge11']['geometry']['points']]
common=set(x)&set(one);assert len(common)==1
joint=next(iter(common));x_free=next(p for p in x if p!=joint);one_free=next(p for p in one if p!=joint)
assert world[joint]==(0,0,1)
assert world[x_free]==(-1,0,0) and world[one_free]==(1,0,0)
actions=[];roles=[]
for name,p,color,use in [('common_blue',joint,'#2563EB','True shared original vertex of x and1, used as the fixed endpoint reference for comparing the other endpoints. This one marker serves both boundaries and is not duplicated.'),
 ('x_red',x_free,'#DC2626','Query free-endpoint source; actual folded vertex-e1.'),
 ('one_red',one_free,'#DC2626','Receiving free endpoint on actual boundary1; actual folded vertex+e1. Compare the red antipodal pair without identifying it.')]:
 snap=next(s for s in ctx['snap_points'] if tuple(s['xy'])==p)
 roles.append({'action_index':len(actions),'source_snap_id':snap['id'],'exact_original_projected_xy':snap['xy'],
   'actual_folded_vertex':world[p],'color':color,'use':use})
 actions.append({'type':'add_point','id':'pair_'+name,'xy':snap['xy'],'filled':True,'color':color,'size_pt2':50,'edge_linewidth_pt':1.0})
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
 'description':'Compare existing x and1 using their true shared endpoint and their two antipodal free endpoints.',
 'intent':'Trace a fixed shared vertex and a concrete opposite-vertex comparison, without adding a seam condition.',
 'params':{'actions':actions}}
save(d/'plugin.json',plugin,exclusive=True)
transfer={'primary_reference':'Solid203','primary_current_png_sha256':sha(TASK/'references/Solid203/C01.png'),
 'primary_current_plugin_sha256':sha(TASK/'references/Solid203/C01.json'),'actual_primary_method':'Current x/C actual-boundary pairing, not old optionA.',
 'secondary_reference':'Plane308','secondary_current_png_sha256':sha(TASK/'references/Plane308/C01.png'),
 'secondary_current_plugin_sha256':sha(TASK/'references/Plane308/C01.json'),'actual_secondary_method':'Current true odd/even source point classes, red1/3/5 blue2/4/6.',
 'migration':'Compare concrete boundariesx and1 through the common blue original endpoint and the red antipodal free-endpoint pair. The shared point is already one flat vertex; merge its source/recipient roles into one marker, so there are exactly three useful markers.',
 'roles':roles,'all_nine_current_PNGs_actually_viewed':True,
 'minimality':'One common endpoint reference plus one source and one recipient for the red antipodal comparison. No coincident duplicate dots or added edge.',
 'physical_color_reading':'Three ink dots remain on unchanged original vertices. Ink does not require opposite red vertices to merge. The exact same physical net still has unique seam5.'}
save(d/'reference_transfer.json',transfer,exclusive=True)
prior=[]
for p in sorted((OWN/'Solid166').glob('*/design.json')):
 m=p.parent/'manual_final_review.json'
 prior.append({'path':str(p),'sha256':sha(p),'png_sha256':sha(p.parent/'candidate.png'),
  'frozen_preset':load(p)['expected_wrong_answer'],'manual_review':str(m),'finals':[r['manual_final_value'] for r in load(m)['reviews']]})
audit={'question_id':'Solid166','parent_history_index':str(OWN/'history_selected.json'),'prior_current_attempts':prior,
 'new_material_difference':'Old x–1 only recolored both entire boundaries; it had two failed calls and is never repeated. This new three-vertex representation explicitly distinguishes the one truly shared original point from the two genuinely antipodal free endpoints. No earlier candidate supplied this source/recipient endpoint relation at the adjacent1/x corner.',
 'difference_from_r05_x4':'r05 compared spatially separated paper copies of a common folded blue vertex. Here x and1 already share the same original flat vertex, so only one blue marker is used. The receiving boundary and free endpoint are different actual paper objects.',
 'new_concrete_hypothesis':'The true common endpoint may encourage a mistaken identification of the red antipodal free vertices, causing the two original boundaries to be identified as edge1.',
 'no_color_width_filename_only_repeat':True,'all_prior_failures_unchanged':True}
save(d/'history_difference.json',audit,exclusive=True)
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':d.name,'created_at':now(),
 'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number','expected_wrong_answer':'1',
 'preset_semantics':{'letter':None,'value':'1','meaning':'The printed boundary identifier1, not a triangle count.'},
 'information_hypothesis':audit['new_concrete_hypothesis'],
 'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
 'endpoint_math':{'blue_common_original_xy':joint,'blue_shared_world':world[joint],
  'red_query_world':world[x_free],'red_receiver_world':world[one_free],
  'red_vertices_true_antipodal_not_equal':True,'unique_actual_matching_edge':'5'},
 'plugin_sha256':sha(d/'plugin.json'),'reference_transfer_path':str(d/'reference_transfer.json'),
 'reference_transfer_sha256':sha(d/'reference_transfer.json'),'history_difference_path':str(d/'history_difference.json'),
 'history_difference_sha256':sha(d/'history_difference.json'),'eligibility_sha256':sha(d/'eligibility_before_design.json'),
 'human_semantics_and_mark_roles':roles,'paper_ink_reading':transfer['physical_color_reading'],
 'two_run_rule':'Exactly two complete original quicktest3 finals must unambiguously give edge1. No third call, relabel, alternative selection, old-PNG replay or retry.',
 'scope':'PRIMARY only; no independent second review, approval, Pass, Collect or delivery.'}
save(d/'design.json',design,exclusive=True)
print('Frozen',d.name)
