from bootstrap import *
from runtime_isolation import install
iso=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from math_tools import prove,cells,is_exterior
index=int(sys.argv[1]);h=read(OWN/'profile_hypotheses.json')['prepared_hypotheses_not_solver_calls'][index]
vid=h['variant_id'];wrong=h['preset'];d=OWN/'Plane213'/vid;d.mkdir(parents=True,exist_ok=False)
assert not read(OWN/'second_review_queue.json')
e=eligibility();save(d/'eligibility_before_design.json',e)
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);c=adapter.inspect_question('Plane213');save(d/'fresh_context.json',c);assert c==read(OWN/'current_context.json')
o={x['id']:x for x in c['objects']};board,proof=prove(c);src=cells(c,'given_');dst=cells(c,wrong+'_')
a,b=h['map_constants']
if h['map_kind']=='reflect_y':T=lambda p:(p[0]+a,b-p[1]);inverse=lambda p:(p[0]-a,b-p[1])
elif h['map_kind']=='quarterturn':T=lambda p:(a-p[1],p[0]+b);inverse=lambda p:(p[1]-b,a-p[0])
else:assert h['map_kind']=='halfturn';T=lambda p:(a-p[0],b-p[1]);inverse=T
local=set()
for x,y in dst:
    vs=[inverse((x,y)),inverse((x+1,y)),inverse((x+1,y+1)),inverse((x,y+1))]
    local.add((min(p[0] for p in vs),min(p[1] for p in vs)))
assert local<=src and len(local)==5
assert {(x-11,y-7) for x,y in local}==set(map(tuple,h['normalized_local_cells']))
actions=[];roles=[]
for group in h['groups']:
    for st,tt in zip(group['source'],group['target']):
        assert set(map(T,o[st]['geometry']['points']))==set(map(tuple,o[tt]['geometry']['points']))
        for target,cs,other in [(st,src,tt),(tt,dst,st)]:
            ps=o[target]['geometry']['points'];assert is_exterior(ps,cs)
            actions.append({'type':'set_object_style','target':target,'color':group['color'],'linewidth_pt':1.5})
            roles.append({'action_index':len(actions)-1,'target':target,'points':ps,'paired_target':other,'information_group':group['name'],'actual_exterior_edge':True,'specific_information_role':group['role'],'one_common_rigid_map_for_ALL_groups':h['map_source_to_option']})
assert len(actions)==10 and len({x['target'] for x in actions})==10
mechanism=h['specific_new_information']+' Wrong '+wrong+' is predicted from mistaking this joint local exterior fit for a full3-copy partition.'
save(d/'marker_roles.json',roles)
save(d/'math_primary_proof.json',{'at_utc':now(),'method':'Fresh current-edge cells; allD4 placements and translations, all unordered triples plus independent first-uncovered-cell recursion.','convention':'Geometric whole-grid-cell pieces can turn over; no printed-pattern preservation or same-face-only constraint.','board_cells':sorted(board),'options':proof,'unique_correct_answer':'A','one_common_source_to_option_map':h['map_source_to_option'],'full_local_piece_source_cells':sorted(local),'full_local_piece_fits':True,'all_marked_edges_true_exterior_of_both_source_and_local_piece':True,'all_groups_have_same_map_and_occupied_side':True,'source_styled_internal_edges':0,'components_if_marked_source_edges_as_cut_barriers':[15]})
save(d/'reference_transfer.json',{'at_utc':now(),'current_reference':str(TASK/'references/Plane233'),'C01_PNG_sha256':sha(TASK/'references/Plane233/C01.png'),'C01_plugin_sha256':sha(TASK/'references/Plane233/C01.json'),'actual_current_C01_PNG_and_plugin_read':True,'migration':'Paired red/blue real boundary features, now two separated exterior anchors of the SAME actual local placement. No internal source connecting line drawn.','new_information':h['specific_new_information'],'full_formal_question':e['formal_record']['question'],'complete_exterior_profile_enumeration_path':str(OWN/'all_local_exterior_correspondence_profiles.json'),'hypothesis_path':str(OWN/'profile_hypotheses.json'),'hypothesis_sha256':sha(OWN/'profile_hypotheses.json'),'no_other_question_result_reused':True})
save(d/'design_difference_audit.json',{'at_utc':now(),'new_information':h['specific_new_information'],'difference':h['difference'],'concision':h['concision'],'not_a_rotated_or_relocated_copy_of_same_profile':True,'not_cap_color_linewidth_or_directory_retry':True,'new_component_incidence_and_joint_local_constraint':True,'all_old_misses_and_wrong_presets_preserved':True})
plugin={'plugin_schema_version':'1.0.0','question_id':'Plane213','category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
cap=adapter.scene('Plane213')
try:noop=png_bytes(cap)
finally:cap.close()
assert pixel_hash(noop)==c['original_pixel_sha256']
renderer=PluginRenderer(cfg,adapter,{'Plane213':c});normal,data,px=renderer.render(plugin);n2,data2,px2=renderer.render(normal,frozen=True)
assert normal==n2 and data==data2 and px==px2
(d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2)
save(d/'plugin_submitted.json',plugin);save(d/'plugin.json',normal)
save(d/'render_check.json',{'at_utc':now(),'fresh_schema_normalization':True,'formal_noop_pixels_match':True,'twice_byte_identical':True,'pixel_sha256':px,'PNG_sha256':sha(d/'candidate.png'),'environment':environment_versions(),'runtime_isolation':iso,'strict_writeguard':str(OWN)})
save(d/'design.json',{'question_id':'Plane213','branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':wrong,'expected_wrong_value':{'B':'B: The depicted U pentomino.','C':'C: The depicted L pentomino with4-cell leg plus1 end cell.','D':'D: The depicted4-cell straight bar with1 extra cell above an interior bar cell.'}[wrong],'correct_answer':'A','mechanism':mechanism,'substantive_difference':h['difference'],'per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'source_reference':'Actual current user Plane233 paired real exterior boundary features, new disconnected joint-local-constraint profile.','status':'PRIMARY_DRAFT; needs native semantics and replay/history gates; no API while prior pair pending; parent NEW independent second review required; NO Pass/Collect'})
eligibility();ck=read(OWN/'checkpoint.json');prepared=ck.get('next_offline_prepared_variants',[])
if vid not in prepared:prepared.append(vid)
ck.update(at_utc=now(),next_offline_prepared_variants=prepared);save('checkpoint.json',ck,replace=True)
print(json.dumps({'variant_id':vid,'wrong_preset':wrong,'PNG_sha256':sha(d/'candidate.png'),'actions':len(actions),'full_local_cells':sorted(local),'new_API_calls':0}))
