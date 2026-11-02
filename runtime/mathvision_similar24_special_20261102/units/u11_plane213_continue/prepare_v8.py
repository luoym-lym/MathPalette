from bootstrap import *
from runtime_isolation import install
iso=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from math_tools import prove,cells,is_exterior
h=read(OWN/'hypothesis_v8_complete_invariant_table.json');vid=h['variant_id'];d=OWN/'Plane213'/vid;d.mkdir(parents=True,exist_ok=False)
assert not read(OWN/'second_review_queue.json')
e=eligibility();save(d/'eligibility_before_design.json',e)
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);c=adapter.inspect_question('Plane213');save(d/'fresh_context.json',c);assert c==read(OWN/'current_context.json')
objects={o['id']:o for o in c['objects']};board,proof=prove(c);src=cells(c,'given_');dst=cells(c,'C_')
actions=[];roles=[]
for group,color,source_targets,destination_targets,T in [('maximal_straight_run4','#DC2626',h['source_red'],h['C_red'],lambda p:(p[0]+1,p[1]-7)),('ALL_concave_corners1','#2563EB',h['source_blue'],h['C_blue'],lambda p:(p[0]-1,9-p[1]))]:
    for st in source_targets:
        ps=objects[st]['geometry']['points'];mapped=set(map(T,ps));tt=next(t for t in destination_targets if set(map(tuple,objects[t]['geometry']['points']))==mapped)
        for target,cs,other in [(st,src,tt),(tt,dst,st)]:
            points=objects[target]['geometry']['points'];assert is_exterior(points,cs)
            actions.append({'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5})
            roles.append({'action_index':len(actions)-1,'target':target,'points':points,'paired_target':other,'information_group':group,'actual_exterior_edge':True,'role':'完整最长4单位直边的一单位。' if color=='#DC2626' else '该轮廓唯一凹角的一条单位臂；两臂共同显示270度转向，且已覆盖全部凹角。','independent_group_comparison_not_one_spatial_map':True})
assert len(actions)==12
table=h['fully_edge_derived_invariant_table'];assert (table['board']['maximum_straight_exterior_run'],table['board']['complete_concave_corner_count'])==(4,1)
assert [k for k in 'ABCDE' if (table[k]['maximum_straight_exterior_run'],table[k]['complete_concave_corner_count'])==(4,1)]==['C']
for cs,(x,y) in [(src,(14,8)),(dst,(13,1))]:
    vertices={(a+dx,b+dy) for a,b in cs for dx,dy in ((0,0),(1,0),(0,1),(1,1))}
    cc=[v for v in vertices if sum((v[0]+dx,v[1]+dy) in cs for dx,dy in ((-1,-1),(-1,0),(0,-1),(0,0)))==3]
    assert cc==[(x,y)]
mechanism=h['new_information']
save(d/'marker_roles.json',roles)
save(d/'math_primary_proof.json',{'at_utc':now(),'method':'Fresh current-edge extraction, allD4 and all valid translations, all unordered triples plus independent first-uncovered-cell recursion.','convention':'Geometric grid-cell cutouts may turn over; no printed-pattern-preservation or same-face-only condition.','board_cells':sorted(board),'options':proof,'unique_correct_answer':'A','full_two_invariant_table':table,'unique_matching_whole_board_signature_among_options':'C','warning':'A valid3-copy tiling does not require a single piece to have the whole board maximal run or corner count. The actual mathematical answer is A, not the invariant-matching C.','red_exact_map':'Source->C (x,y)->(x+1,y-7)','blue_exact_map':'Source->C (x,y)->(x-1,9-y)','groups_independent_not_one_map':True,'source_styled_internal_edges':0,'components_if_source_marks_as_cut_barriers':[15]})
save(d/'reference_transfer.json',{'at_utc':now(),'reference_directory':str(TASK/'references/Plane233'),'C01_PNG_sha256':sha(TASK/'references/Plane233/C01.png'),'C01_plugin_sha256':sha(TASK/'references/Plane233/C01.json'),'migration':'Current red/blue source-option existing-boundary comparisons. Blue now compares complete real concavity inventory, unlike old C01 convex foot.','formal_question':e['formal_record']['question'],'hypothesis_frozen_at':h['at_utc'],'hypothesis_sha256':sha(OWN/'hypothesis_v8_complete_invariant_table.json'),'no_other_question_or_old_call_reused':True})
save(d/'design_difference_audit.json',{'at_utc':now(),'difference':h['difference'],'new_signature_information':h['new_information'],'not_old_C01_spine_foot_retest':True,'not_v6_corner_total_retest':True,'not_v7_sampled_D_concavity_retest':True,'not_an_old_outcome_relabel':True,'concision':'12 unit styles: complete4-unit red runs in both diagrams and2 arms at ALL1 concave corner in each.','no_common_rigid_map_claim':True})
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
save(d/'design.json',{'question_id':'Plane213','branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':'C','expected_wrong_value':'C: The depicted L pentomino with4-cell leg and one extra end cell.','correct_answer':'A','mechanism':mechanism,'substantive_difference':h['difference'],'per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'source_reference':'Actual current user Plane233 paired boundary features; new complete maximal-run/concavity-inventory signature.','status':'PRIMARY_DRAFT; native and all gates needed; no additionalAPI while prior pair pending; NEW parent second review required; NO Pass/Collect'})
eligibility();ck=read(OWN/'checkpoint.json');ck.update(at_utc=now(),next_offline_prepared_variant=vid,next_offline_variant_API_calls=0);save('checkpoint.json',ck,replace=True)
print(json.dumps({'variant_id':vid,'preset':'C','PNG_sha256':sha(d/'candidate.png'),'actions':len(actions),'new_API_calls':0}))
