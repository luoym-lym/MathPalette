from bootstrap import *
from runtime_isolation import install
isolation=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from math_tools import prove,cells,is_exterior
index=int(sys.argv[1]);h=read(OWN/'research_hypotheses_before_new_outputs.json')['possible_material_followups_if_no_PRIMARY_candidate'][index]
assert not read(OWN/'second_review_queue.json')
vid=h['variant_id'];wrong=h['wrong_preset'];d=OWN/'Plane213'/vid;d.mkdir(parents=True,exist_ok=False)
e=eligibility();save(d/'eligibility_before_design.json',e)
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);c=adapter.inspect_question('Plane213');save(d/'fresh_context.json',c)
assert c==read(OWN/'current_context.json')
objects={o['id']:o for o in c['objects']}
board,proof=prove(c)
src=cells(c,'given_');dst=cells(c,wrong+'_')
if wrong=='D':
    T=lambda p:(33-p[0],11-p[1])
    inverse=T
    mapping='Source -> D: (x,y)->(33-x,11-y), half-turn'
    mechanism='以蓝色比较源棋盘完整四格顶边与D完整四格底边，红色比较相邻一格外侧边；对应一次能放入源图顶行的D局部试放，诱导把贯穿全宽的直条兼容误作三份全等铺满。'
    difference='新信息为贯穿整个棋盘宽度的4格横条及端侧1格；指向D长条上偏心附格结构。旧C比较4高+2脚；Bv3比较2高+3底；旧B比较内U或270度单位凹角。它们均不是本图的4宽顶行试放，且本图零内部源边。'
else:
    assert wrong=='E'
    T=lambda p:(p[0]+12,p[1]-7)
    inverse=lambda p:(p[0]-12,p[1]+7)
    mapping='Source -> E: (x,y)->(x+12,y-7), translation'
    mechanism='把源缺格处已有的右-上-右-上四单位外边阶梯，按横蓝竖红对应E十字下右侧相同四连边阶梯。此对应固定一个真实可放入的十字局部位置；诱导忽略十字无法覆盖棋盘外凸角的全局障碍。'
    difference='新比较不是旧B凹角两射线，也不是旧内部U三边或凸底角L。比较完整四连阶梯：两个端部凸角加中间凹角的连续转向和占据侧，来源为缺格及两邻格的现有外轮廓，接受对象为E下臂和右臂。局部X真能放入，但任意X不能覆盖(0,0)。'
local=set()
for x,y in dst:
    vertices=[inverse((x,y)),inverse((x+1,y)),inverse((x+1,y+1)),inverse((x,y+1))]
    local.add((min(p[0] for p in vertices),min(p[1] for p in vertices)))
assert len(local)==5 and local<=src
groups=[('blue_horizontal','#2563EB',h['source_blue_horizontal'],h[wrong+'_blue_horizontal']),('red_vertical','#DC2626',h['source_red_vertical'],h[wrong+'_red_vertical'])]
actions=[];roles=[]
for group,color,source_targets,destination_targets in groups:
    for st in source_targets:
        sp=objects[st]['geometry']['points'];mapped=set(map(T,sp))
        tt=next(t for t in destination_targets if set(map(tuple,objects[t]['geometry']['points']))==mapped)
        for target,cs,other in [(st,src,tt),(tt,dst,st)]:
            ps=objects[target]['geometry']['points'];assert is_exterior(ps,cs)
            actions.append({'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5})
            roles.append({'action_index':len(actions)-1,'target':target,'points':ps,'paired_target':other,'group':group,'actual_exterior_edge':True,'role':('四格完整横向跨度中的一格；与相邻单位侧壁共同定位全宽直条试放。' if color=='#2563EB' else '全宽直条端点的一格外侧壁，固定半周转向与局部占据侧。') if wrong=='D' else ('完整四连阶梯的一条水平单位边；定位相邻凸/凹转向和该处占据侧。' if color=='#2563EB' else '完整四连阶梯的一条竖直单位边；同其两侧横边固定外边界相邻关系。')})
assert len({a['target'] for a in actions})==len(actions)
save(d/'math_primary_proof.json',{'at_utc':now(),'method':'Fresh CURRENT unmodified unit edges; fullD4 orientation/translation enumeration, all unordered triples plus independent first-uncovered-cell recursion.','convention':'Identical geometric grid-square cutouts may be turned over. No colored-print preservation or same-face-only constraint is stated.','board_cells':sorted(board),'options':proof,'unique_correct_answer':'A','exact_local_feature_transform':mapping,'local_piece_current_source_cells':sorted(local),'local_piece_fits':True,'wrong_global_tiling_count':0,'C_D_analytic_exclusion':'Three full four-cell straight runs must all be parallel: any full horizontal run intersects any full vertical run. They then occupy all3 available full rows or columns. The outermost run fifth cell lies outside or on an already occupied full run. Impossible.','E_analytic_exclusion':'No X can cover the existing corner cell(0,0): every possible center for it forces another arm outside the board.','source_marked_internal_edges':0,'components_if_source_marks_as_cut_barriers':[15]})
save(d/'marker_roles.json',roles)
save(d/'reference_transfer.json',{'at_utc':now(),'current_user_reference_directory':str(TASK/'references/Plane233'),'current_C01_png_sha256':sha(TASK/'references/Plane233/C01.png'),'current_C01_plugin_sha256':sha(TASK/'references/Plane233/C01.json'),'actual_nine_current_PNGs_and_plugins_read':True,'migration':'Current red-vertical/blue-horizontal existing-boundary comparison, without source internal cuts.','this_information':h['information'],'independent_formal_question':e['formal_record']['question'],'no_other_question_call_reused':True,'research_note_before_all_new_outputs_sha256':sha(OWN/'research_hypotheses_before_new_outputs.json')})
prior=[]
for p in sorted((OWN/'Plane213').glob('*/complete_binding_and_result_audit.json')):
    a=read(p);prior.append({'directory':str(p.parent),'preset':a['frozen_wrong_preset'],'finals':a['final_options'],'two_hit':a['two_hit']})
save(d/'design_difference_audit.json',{'at_utc':now(),'new_information':h['information'],'difference':difference,'prior_new_unit_results_preserved':prior,'original_213_old_presets_and_finals':[['B',['C','B']],['C',['B','C']],['B',['B','E']]],'no_cosmetic_retry':True,'no_posthoc_relabel':True,'no_old_failed_PNG_retest':True,'per_marker_information_roles_path':str(d/'marker_roles.json')})
plugin={'plugin_schema_version':'1.0.0','question_id':'Plane213','category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
cap=adapter.scene('Plane213')
try:noop=png_bytes(cap)
finally:cap.close()
assert pixel_hash(noop)==c['original_pixel_sha256']
renderer=PluginRenderer(cfg,adapter,{'Plane213':c});normal,data,px=renderer.render(plugin);n2,data2,px2=renderer.render(normal,frozen=True)
assert normal==n2 and data==data2 and px==px2
(d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2)
save(d/'plugin_submitted.json',plugin);save(d/'plugin.json',normal)
save(d/'render_check.json',{'at_utc':now(),'fresh_schema_normalization':True,'formal_noop_pixels_match':True,'twice_byte_identical':True,'pixel_sha256':px,'PNG_sha256':sha(d/'candidate.png'),'environment':environment_versions(),'runtime_isolation':isolation,'strict_writeguard':str(OWN)})
save(d/'design.json',{'question_id':'Plane213','branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':wrong,'expected_wrong_value':wrong+(': Four-cell straight base with one upper cell on an interior base cell (the shown offset T pentomino).' if wrong=='D' else ': Five-cell X/plus pentomino.'),'correct_answer':'A','mechanism':mechanism,'substantive_difference':difference,'per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'source_reference':'Actual current user Plane233 C01. New informative true boundary comparison.','status':'PRIMARY_DRAFT; NEEDS NEW PARENT INDEPENDENT SECOND REVIEW; NO Pass/Collect'})
eligibility()
checkpoint=read(OWN/'checkpoint.json');checkpoint.update(at_utc=now(),status='new_material_followup_rendered_pending_native_and_replay',candidate_directory=str(d));save('checkpoint.json',checkpoint,replace=True)
print(json.dumps({'variant_id':vid,'preset':wrong,'PNG_sha256':sha(d/'candidate.png'),'actions':len(actions),'local_piece':sorted(local)}))
