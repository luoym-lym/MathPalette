from bootstrap import *
from runtime_isolation import install
iso=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from math_tools import prove,cells,is_exterior
h=read(OWN/'hypothesis_v7.json');vid=h['variant_id'];d=OWN/'Plane213'/vid;d.mkdir(parents=True,exist_ok=False)
assert not read(OWN/'second_review_queue.json')
e=eligibility();save(d/'eligibility_before_design.json',e)
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);c=adapter.inspect_question('Plane213');save(d/'fresh_context.json',c);assert c==read(OWN/'current_context.json')
objects={o['id']:o for o in c['objects']};board,proof=prove(c);src=cells(c,'given_');dst=cells(c,'D_')
groups=[('maximal4_unit_run','#DC2626',h['source_red'],h['D_red'],lambda p:(p[1]+11,11-p[0])),('concave270_corner','#2563EB',h['source_blue'],h['D_blue'],lambda p:(34-p[0],9-p[1]))]
actions=[];roles=[]
for group,color,stargets,dtargets,T in groups:
    for st in stargets:
        ps=objects[st]['geometry']['points'];mapped=set(map(T,ps))
        tt=next(t for t in dtargets if set(map(tuple,objects[t]['geometry']['points']))==mapped)
        for target,cs,other in [(st,src,tt),(tt,dst,st)]:
            points=objects[target]['geometry']['points'];assert is_exterior(points,cs)
            actions.append({'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5})
            roles.append({'action_index':len(actions)-1,'target':target,'points':points,'paired_target':other,'information_group':group,'actual_exterior_edge':True,'role':'完整最长4单位直边中的一单位，和对图同色边逐单位比较真实直边长度。' if color=='#DC2626' else '真实270度凹角的一条单位臂，和同顶点另一臂共同比较凹转向及占据侧。','groups_are_independent_not_one_spatial_map':True})
for cs,(x,y) in [(src,(14,8)),(dst,(20,1))]:assert sum((x+dx,y+dy) in cs for dx,dy in ((-1,-1),(-1,0),(0,-1),(0,0)))==3
assert len(actions)==12 and len({a['target'] for a in actions})==12
mechanism=h['new_reasoning_target']
save(d/'marker_roles.json',roles)
save(d/'math_primary_proof.json',{'at_utc':now(),'method':'Fresh current-edge unit-cell recovery; allD4 placements/translations; all unordered triples and first-uncovered-cell recursion agree.','convention':'Identical whole-grid geometric cutouts allow turning over; colors add no pattern-preservation requirement.','board_cells':sorted(board),'options':proof,'unique_correct_answer':'A','group1_exact_map':'source->D (x,y)->(y+11,11-x)','group2_exact_map':'source->D (x,y)->(34-x,9-y)','two_individually_true_invariants':{'straight_boundary_run_length':4,'selected_concave_angle_degrees':270},'one_common_rigid_map_is_not_claimed':True,'source_styled_internal_edges':0,'components_if_marks_as_cut_barriers':[15]})
save(d/'reference_transfer.json',{'at_utc':now(),'current_reference':str(TASK/'references/Plane233'),'C01_PNG_sha256':sha(TASK/'references/Plane233/C01.png'),'C01_plugin_sha256':sha(TASK/'references/Plane233/C01.json'),'migration':'Two actual existing-boundary features are paired source/option in red and blue. The explicit permitted new true concave structure is compared independently of global straight-run length. No common placement assumption is introduced.','full_formal_question':e['formal_record']['question'],'hypothesis_path':str(OWN/'hypothesis_v7.json'),'hypothesis_sha256':sha(OWN/'hypothesis_v7.json'),'no_reference_call_or_old_output_counted':True})
save(d/'design_difference_audit.json',{'at_utc':now(),'difference':h['substantive_difference'],'concision':h['concision'],'old_v6_presetC_finalD_D_stays_MISS':True,'new_preset_from_marked_D_feature_checklist_not_old_output_relabel':True,'not_cosmetic_change':True,'no_same_PNG_retry':True,'independent_group_maps_are_explicit':True})
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
save(d/'design.json',{'question_id':'Plane213','branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':'D','expected_wrong_value':'D: The depicted four-cell straight base with one upper cell on an interior base cell.','correct_answer':'A','mechanism':mechanism,'substantive_difference':h['substantive_difference'],'per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'source_reference':'Current actual user Plane233 red/blue boundary-feature comparisons, adapted to two separately true invariants.','status':'PRIMARY_DRAFT; NATIVE SEMANTICS NOT YET ADMITTED; NEW PARENT SECOND REVIEW REQUIRED; NO Pass/Collect'})
eligibility();ck=read(OWN/'checkpoint.json');ck.update(at_utc=now(),status='v7_rendered_pending_native_independent_group_semantics',candidate_directory=str(d));save('checkpoint.json',ck,replace=True)
print(json.dumps({'variant_id':vid,'preset':'D','actions':len(actions),'PNG_sha256':sha(d/'candidate.png')}))
