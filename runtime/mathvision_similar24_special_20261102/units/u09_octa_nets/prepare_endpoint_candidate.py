from own_bootstrap import *
from unit_tools import eligibility

variant='r05_endpoint_x_four'
directory=OWN/'Solid166'/variant
directory.mkdir(parents=True,exist_ok=False)
e=eligibility('Solid166');save(directory/'eligibility_before_design.json',e,exclusive=True)
context=load(OWN/'Solid166/context.json')
math=load(OWN/'Solid166/primary_math.json')
world={tuple(v['flat']):tuple(v['world']) for f in math['folded_faces'].values() for v in f}
objects={o['id']:o for o in context['objects']}
sources=[tuple(p[:2]) for p in objects['netedge15']['geometry']['points']]
receivers=[tuple(p[:2]) for p in objects['netedge2']['geometry']['points']]
common=set(world[p] for p in sources)&set(world[p] for p in receivers)
assert common=={(0,0,1)}
actions=[];roles=[]
for group,points in [('x',sources),('four',receivers)]:
    for p in points:
        same=world[p] in common
        color='#2563EB' if same else '#DC2626'
        color_name='blue' if same else 'red'
        snap=next(s for s in context['snap_points'] if tuple(s['xy'])==p)
        idx=len(actions)
        actions.append({'type':'add_point','id':'endpoint_'+group+'_'+color_name,'xy':snap['xy'],
            'filled':True,'color':color,'size_pt2':50,'edge_linewidth_pt':1.0})
        roles.append({'action_index':idx,'source_snap_id':snap['id'],'exact_original_projected_xy':snap['xy'],
           'original_edge':'netedge15' if group=='x' else 'netedge2','original_edge_identifier':'x' if group=='x' else '4',
           'actual_folded_vertex':world[p],'color':color,
           'use':('Query endpoint source for a two-vertex seam comparison.' if group=='x' else
                  'Receiving endpoint on edge4 for the corresponding '+color_name+' query endpoint.'),
           'pair_truth':'Both blue endpoints are the same actual folded vertex+e3.' if same else
                        'Red endpoints are actual opposite vertices-e1 and+e1; the comparison must not be treated as a new equality condition.'})
assert len({tuple(a['xy']) for a in actions})==4
assert {world[p] for p in sources if world[p] not in common}=={(-1,0,0)}
assert {world[p] for p in receivers if world[p] not in common}=={(1,0,0)}
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
 'description':'Compare the actual endpoints of original edge x and original edge4 using red/blue endpoint pairs.',
 'intent':'Track one common folded endpoint and compare the two remaining endpoints, preserving the net.',
 'params':{'actions':actions}}
save(directory/'plugin.json',plugin,exclusive=True)
transfer={'primary_reference':'Solid203','primary_current_png_sha256':sha(TASK/'references/Solid203/C01.png'),
 'primary_current_plugin_sha256':sha(TASK/'references/Solid203/C01.json'),
 'primary_method':'Current user C01 compares the two actual original boundariesx andC, not legacy optionA.',
 'secondary_reference':'Plane308','secondary_current_png_sha256':sha(TASK/'references/Plane308/C01.png'),
 'secondary_current_plugin_sha256':sha(TASK/'references/Plane308/C01.json'),
 'secondary_actual_method':'Current user C01 uses red odd-numbered points1/3/5 and blue even-numbered2/4/6 as a source-to-target grouping; not legacy consecutive1/2/3 versus4/5/6.',
 'migration':'Refine original-edge correspondence into its two actual endpoint correspondences. Onx and4, blue marks are the genuine same folded vertex+e3. Red marks compare the two other, opposite folded vertices. The candidate shortcut is falsely closing this nearly corresponding boundarypair as a whole and choosing4.',
 'all_current_nine_PNGs_actually_viewed':True,'roles':roles,
 'minimality':'Four markers, one per distinct original vertex. Each completes one source/recipient endpoint pair. No extra line, region, cut, label, equality sign, or repeated attribute.',
 'human_reading':'All dots lie exactly on existing visible original vertices and do not change their incidence. Original labels and edge boundaries remain readable. Ink at vertices is not required to merge with equal ink by the question; physical folded edge equality remains5.'}
save(directory/'reference_transfer.json',transfer,exclusive=True)
old=[]
for p in (OWN/'Solid166').glob('*/design.json'):
 if p.parent==directory:continue
 d=load(p);m=p.parent/'manual_final_review.json'
 old.append({'design_path':str(p),'variant':d['variant_id'],'preset':d['expected_wrong_answer'],
     'plugin_sha256':sha(p.parent/'plugin.json'),'image_sha256':sha(p.parent/'candidate.png'),
     'manual_review_path':str(m) if m.exists() else None,
     'final_values':[r['manual_final_value'] for r in load(m)['reviews']] if m.exists() else None})
audit={'question_id':'Solid166','old_parent_index':str(OWN/'history_selected.json'),
 'current_attempts':old,'new_material_difference':'No edge is recolored here. This introduces two precisely snapped endpoint source/receiver pairs, one geometrically correct and one geometrically opposite, to test a vertex-identification shortcut. Oldx–4 line comparison andx–2/blue1–4 images are retained and not repeated.',
 'no_change_to_failed_png_or_preset':True,'substantive_information_gain':'Endpoint incidence and identity are now individually available; the old edge-color pair did not distinguish which endpoints were compared.',
 'old_reference_and_raw_read_preserved':True}
save(directory/'history_difference.json',audit,exclusive=True)
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':variant,'created_at':now(),
 'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number','expected_wrong_answer':'4',
 'preset_semantics':{'letter':None,'value':'4','meaning':'The printed edge identifier4.'},
 'information_hypothesis':'The genuine blue common vertex and paired red endpoint salience may cause the opposite red vertices to be identified, falsely closing the boundaryx against4. The concrete expected wrong edge is4, frozen before testing.',
 'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
 'endpoint_math':{'blue_pair_folded_vertices':[[0,0,1],[0,0,1]],'red_pair_folded_vertices':[[-1,0,0],[1,0,0]],
   'false_receiver4_does_not_coincide':True,'only_edge5_has_both_correct_endpoints':True},
 'plugin_sha256':sha(directory/'plugin.json'),'reference_transfer_path':str(directory/'reference_transfer.json'),
 'reference_transfer_sha256':sha(directory/'reference_transfer.json'),'history_difference_path':str(directory/'history_difference.json'),
 'history_difference_sha256':sha(directory/'history_difference.json'),'eligibility_sha256':sha(directory/'eligibility_before_design.json'),
 'human_semantics_and_mark_roles':roles,
 'paper_ink_reading':'Dots are on unchanged existing vertices. No condition requires matching red/blue ink, and all ink can remain on the physically folded paper; resulting seam identity is still5.',
 'two_run_rule':'Exactly two original quicktest3 runs; both complete final edge identifiers must be4. No third, relabel, replay of failed inputs, retry or picking successes.',
 'scope':'PRIMARY research only; new independent review belongs to parent; no approval/Pass/Collect/delivery.'}
save(directory/'design.json',design,exclusive=True)
print('Frozen endpoint mapping candidate',str(directory))
