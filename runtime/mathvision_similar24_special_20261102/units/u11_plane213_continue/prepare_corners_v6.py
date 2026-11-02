from bootstrap import *
from runtime_isolation import install
iso=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from math_tools import prove,cells,is_exterior
vid='user233_C_convex_concave_inventory_v6';d=OWN/'Plane213'/vid;d.mkdir(parents=True,exist_ok=False)
assert not read(OWN/'second_review_queue.json')
e=eligibility();save(d/'eligibility_before_design.json',e)
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);c=adapter.inspect_question('Plane213');save(d/'fresh_context.json',c)
assert c==read(OWN/'current_context.json')
board,proof=prove(c)
objects={o['id']:o for o in c['objects']};targets={t['id']:t for t in c['canvas']['targets']}
proposal=read(OWN/'corner_inventory_hypothesis_before_E_outputs.json')
inventories={k:proposal['inventories'][k] for k in ('board','C')}
actions=[];roles=[];counts={}
for diagram,prefix in [('board','given_'),('C','C_')]:
    cs=cells(c,prefix);counts[diagram]={'convex90':0,'concave270':0}
    for corner in inventories[diagram]:
        vertex=tuple(corner['xy']);kind=corner['kind'];counts[diagram][kind]+=1
        x,y=vertex;n=sum((x+dx,y+dy) in cs for dx,dy in ((-1,-1),(-1,0),(0,-1),(0,0)))
        assert n==(1 if kind=='convex90' else 3)
        incident=[]
        for t,o in objects.items():
            if not t.startswith(prefix):continue
            ps=o['geometry']['points']
            if vertex in map(tuple,ps) and is_exterior(ps,cs):incident.append(t)
        assert len(incident)==2
        for t in sorted(incident):
            ps=objects[t]['geometry']['points'];partial=targets[t]['partial_paths'];assert len(partial)==1
            path=partial[0];assert not path['closed'] and path['id']=='p0' and len(path['samples'])==2
            start,end=(0.0,0.35) if tuple(ps[0])==vertex else (0.65,1.0)
            color='#2563EB' if kind=='convex90' else '#DC2626'
            a={'type':'set_object_style','target':t,'color':color,'linewidth_pt':1.5,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':start,'end':end,'wrap':False}}
            actions.append(a)
            roles.append({'action_index':len(actions)-1,'target':t,'interval':a['interval'],'corner_xy':list(vertex),'corner_type':kind,'diagram':diagram,'paired_information_group':('C' if diagram=='board' else 'board')+' '+kind+' inventory','actual_exterior_edge':True,'specific_role':'此短臂与同顶点的另一短臂共同显示一个真实'+('90度凸角，计入蓝色五角组。' if kind=='convex90' else '270度凹角，计入红色单角组。'),'why_both_arms':'一个短直线端部不足以显示凸/凹转向和占据侧；两短臂直接沿真实外边，未新增角弧/符号/条件。','not_a_full_choice_highlight':True})
assert counts['board']==counts['C']=={'convex90':5,'concave270':1} and len(actions)==24
for i,a in enumerate(actions):
    for b in actions[i+1:]:
        if a['target']==b['target']:assert a['interval']['end']<=b['interval']['start'] or b['interval']['end']<=a['interval']['start']
mechanism='以短蓝角臂显示源轮廓与C各五个真实90度凸角，以短红角臂显示各唯一270度凹角；将相同的角类型数量误作三份C可以铺满的充分依据。A也有同样角数，完整铺满仍只可能A。'
difference='本图比较完整凸/凹角数量这一真实组合结构，不比较旧C四格柱/两格脚，不重复B内部U、B凹角两边、B3×2凸底角、D全宽条或E四连阶梯。所有外角短臂均承担计数类别信息，覆盖完整6个角而不按输出挑角。没有内部源边、闭合源拼块或整幅选项描边。'
save(d/'marker_roles.json',roles)
save(d/'math_primary_proof.json',{'at_utc':now(),'method':'Fresh exact current-edge whole-cell D4 placement enumeration plus all unordered triples and independent first-uncovered-cell recursion.','convention':'Geometric congruent whole-grid-cell cutouts can turn over; no printed-pattern or same-face-only constraint.','board_cells':sorted(board),'options':proof,'unique_correct_answer':'A','actual_corner_inventories':inventories,'corner_counts':counts,'all_option_corner_counts':proposal['counts'],'important_nonunique_invariant':'A and C both match the entire board5 convex/1 concave corner counts. This boundary invariant is not a tiling proof and is not claimed to isolate C geometrically.','source_styled_internal_edges':0,'components_if_source_marks_as_cut_barriers':[15],'no_single_rigid_map_of_entire_source_outline_to_C_claimed':True})
save(d/'reference_transfer.json',{'at_utc':now(),'reference_directory':str(TASK/'references/Plane233'),'current_C01_PNG_sha256':sha(TASK/'references/Plane233/C01.png'),'current_C01_plugin_sha256':sha(TASK/'references/Plane233/C01.json'),'actual_current_reference_PNG_and_plugin_read':True,'migration':'Use the current paired red/blue existing-boundary method for another explicitly permitted true convex/concave relation. Source and C both show complete angle-type inventory. No older reference label/color imported.','preserved_formal_question':e['formal_record']['question'],'new_invariant_proposal_frozen_before_E_outputs':str(OWN/'corner_inventory_hypothesis_before_E_outputs.json'),'proposal_sha256':sha(OWN/'corner_inventory_hypothesis_before_E_outputs.json')})
save(d/'design_difference_audit.json',{'at_utc':now(),'difference':difference,'all_previous_results_path':str(OWN/'checkpoint.json'),'predeclared_wrong_answer':'C','not_a_three_candidate_early_stop':True,'not_a_cosmetic_retry':True,'not_using_arbitrary_mark_count_to_pass':True,'why24_actions':'6 actual corners in each of2 diagrams,2 incident short arms per corner;24 effective nonoverlapping interval overrides. Color and width merged in each. No fake or repeated corner.','native_clarity_still_requires_actual_PNG_inspection':True,'new_hypothesis_not_prior_final_C_relabel':True})
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
save(d/'design.json',{'question_id':'Plane213','branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':'C','expected_wrong_value':'C: The depicted L pentomino with4-cell leg and one extra end cell.','correct_answer':'A','mechanism':mechanism,'substantive_difference':difference,'per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'source_reference':'Actual current user Plane233 C01 source/option red-blue boundary comparisons; extended to true convex/concave structure.','status':'PRIMARY_DRAFT; NOT ADMITTED UNTIL NATIVE CLARITY; NEW PARENT SECOND REVIEW REQUIRED; NO Pass/Collect'})
eligibility()
ck=read(OWN/'checkpoint.json');ck.update(at_utc=now(),status='v6_corner_inventory_rendered_pending_native_clarity',candidate_directory=str(d));save('checkpoint.json',ck,replace=True)
print(json.dumps({'variant_id':vid,'preset':'C','actions':len(actions),'counts':counts,'PNG_sha256':sha(d/'candidate.png')}))
