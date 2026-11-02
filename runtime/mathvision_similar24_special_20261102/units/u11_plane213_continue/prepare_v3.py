from bootstrap import *
import itertools
from runtime_isolation import install
isolation=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
q='Plane213';vid='user233_B_three_base_two_wall_local_fit_v3'
d=OWN/q/vid;d.mkdir(parents=True,exist_ok=False)
e=eligibility();save(d/'eligibility_before_design.json',e)
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);context=adapter.inspect_question(q);save(d/'fresh_context.json',context)
assert context==read(OWN/'current_context.json')
objects={o['id']:o for o in context['objects']}
def norm(s):
    x0=min(x for x,y in s);y0=min(y for x,y in s)
    return frozenset((x-x0,y-y0) for x,y in s)
def cells(prefix):
    edges=set()
    for o in context['objects']:
        if not o['id'].startswith(prefix):continue
        ps=o['geometry']['points'];assert len(ps)==2 and all(float(v).is_integer() for p in ps for v in p)
        edges.add(frozenset((int(x),int(y)) for x,y in ps))
    xy=[p for edge in edges for p in edge];out=set()
    for x in range(min(p[0] for p in xy),max(p[0] for p in xy)):
        for y in range(min(p[1] for p in xy),max(p[1] for p in xy)):
            v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
            if all(frozenset((v[i],v[(i+1)%4])) in edges for i in range(4)):out.add((x,y))
    return out
def forms(s,flips=(-1,1)):
    out=set()
    for flip in flips:
        t={(flip*x,y) for x,y in s}
        for _ in range(4):out.add(norm(t));t={(-y,x) for x,y in t}
    return out
board=norm(cells('given_'));assert len(board)==15
def search(placements,remaining):
    if not remaining:return 1
    c=min(remaining)
    return sum(search(placements,remaining-p) for p in placements if c in p and p<=remaining)
proof={}
for letter in 'ABCDE':
    shape=norm(cells(letter+'_'));assert len(shape)==5
    placements=set()
    for f in forms(shape):
        for x,y in itertools.product(range(4),repeat=2):
            p=frozenset((x+a,y+b) for a,b in f)
            if p<=board:placements.add(p)
    placements=sorted(placements,key=lambda s:sorted(s))
    tilings=[t for t in itertools.combinations(placements,3) if len(set().union(*t))==15]
    assert search(placements,board)==len(tilings)
    proof[letter]={'cells':sorted(shape),'D4_forms':len(forms(shape)),'all_valid_placements':[sorted(p) for p in placements],'placement_count':len(placements),'all_unordered_triples_count':len(list(itertools.combinations(placements,3))),'tiling_count':len(tilings),'witnesses':[[sorted(p) for p in t] for t in tilings]}
assert [proof[k]['tiling_count'] for k in 'ABCDE']==[2,0,0,0,0]
rotation_only={}
for letter in 'ABCDE':
    ps=set()
    for f in forms(norm(cells(letter+'_')),(1,)):
        for x,y in itertools.product(range(4),repeat=2):
            p=frozenset((x+a,y+b) for a,b in f)
            if p<=board:ps.add(p)
    rotation_only[letter]=search(ps,board)
R='#DC2626';B='#2563EB'
groups=[('red_two_cell_wall',['given_0','given_2'],['B_0','B_2'],R),('blue_three_cell_base',['given_1','given_10','given_19'],['B_1','B_6','B_10'],B)]
actions=[];roles=[]
source_cells=cells('given_');piece_cells=cells('B_')
T=lambda p:(p[0]-5,p[1]-7)
for group,src,targets,color in groups:
    for st,tt in zip(src,targets):
        sp=objects[st]['geometry']['points'];tp=objects[tt]['geometry']['points']
        assert set(map(T,sp))==set(map(tuple,tp))
        for target,pts,cs,other in [(st,sp,source_cells,tt),(tt,tp,piece_cells,st)]:
            edge=frozenset(map(tuple,pts));incident=0
            for x,y in cs:
                v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
                incident+=any(frozenset((v[i],v[(i+1)%4]))==edge for i in range(4))
            assert incident==1
            actions.append({'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5})
            roles.append({'action_index':len(actions)-1,'target':target,'points':pts,'color':color,'group':group,'paired_target':other,'actual_exterior_edge':True,'role':'两格高外侧壁的一格；定位B左下角真实局部试放的竖向范围。' if color==R else '三格长外底边的一格；定位同一局部试放的横向完整底边。','why_useful':'与配对图逐单位精确平移一致；两色共同确定3×2局部包围范围，单独突出B不能提供此来源信息。'})
local=frozenset((x+11,y+7) for x,y in norm(piece_cells))
assert local<=source_cells and len(local)==5
remaining=source_cells-local
# All source colored edges are exterior: removing them from cell adjacency leaves the original 15 connected cells.
reached={min(source_cells)}
while True:
    nxt=reached|{(x+dx,y+dy) for x,y in reached for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)) if (x+dx,y+dy) in source_cells}
    if nxt==reached:break
    reached=nxt
assert reached==source_cells
mechanism='把源棋盘左下角三格完整底边（蓝）与其左侧下两格高外边（红），逐单位对应到B的三格底边及两格外侧壁；这是一份真实可放入的U形局部范围，诱导把局部兼容误作三份B全等铺满。'
difference='v3改变的是比较的真实几何量与对象：B的外凸3×2底角包围范围，在源棋盘左下角作同向平移试放。旧213内部红U比较凹槽三边；root v1比较C的4高柱+2长脚；u10 v2比较源缺角与B内凹槽的270度单位角。本图不再标任何旧内部U或缺格凹角，不标C，也不保留旧4高红柱；不是换色、线宽或重抽样。参考当前C01的方法仍为红竖/蓝横开放边长比较，新数据关系为2高/3长的B外凸底角。'
save(d/'math_primary_proof.json',{'at_utc':now(),'method':'Fresh exact whole-unit-square edge extraction from CURRENT unmodified scene. Enumerate all D4 orientations and valid translations; check every unordered triple and independent first-uncovered-cell recursive exact cover.','convention':'Original depicts congruent whole grid-square cutouts. Pieces may be turned over; no restriction to same-face rotations is stated. Reflection is allowed by ordinary geometric congruence. No colored-grid partition or new condition is assumed.','board_cells':sorted(board),'options':proof,'unique_correct_answer':'A','rotation_only_diagnostic':rotation_only,'A_requires_reflection_under_this_layout':rotation_only['A']==0,'B_local_placement_current_coordinates':sorted(local),'B_local_remaining_cells':sorted(remaining),'B_global_tiling_count':0,'C_D_analytic_exclusion':'Each contains a straight run of four. Each such run must occupy a full row y=1,2,3 or column x=0,1,2. Horizontal and vertical runs intersect; three disjoint runs must be parallel. They occupy all three available full rows or columns. The extra cell of the outermost piece then lies outside the board or in another occupied full run. Impossible.','E_analytic_exclusion':'No X-pentomino can cover the board convex corner (0,0): centers at (0,0) or any axial neighbor force an arm outside the board.','source_marked_internal_edges':0,'source_components_if_marked_edges_read_as_cut_barriers':[15],'exact_local_feature_transform':'Source -> B: (x,y) -> (x-5,y-7)'})
save(d/'marker_roles.json',roles)
save(d/'reference_transfer.json',{'at_utc':now(),'authoritative_reference':str(TASK/'references/Plane233'),'current_C01_png_sha256':sha(TASK/'references/Plane233/C01.png'),'current_C01_plugin_sha256':sha(TASK/'references/Plane233/C01.json'),'actual_PNG_and_complete_plugin_recipes_reference_read':True,'reference_has_4_high_red_2_long_blue_to_C':True,'this_transfer_has_2_high_red_3_long_blue_to_B':True,'source_and_target_share_formal_base_png_but_are_different_questions':{'Plane213':e['formal_record']['question'],'Plane233':read(TASK/'references/Plane233/reference.json')['formal_record']['question']},'no_reference_results_reused':True,'no_old18_label_or_color_substitution':True})
save(d/'design_difference_audit.json',{'at_utc':now(),'difference':difference,'old_213_B_preset_finals':['C','B'],'root_C_preset_finals':['B','C'],'u10_B_preset_finals':['B','E'],'old_233_notch_B_preset_finals':['D','B'],'no_posthoc_relabel':True,'no_old_failed_frozen_PNG_retested':True,'concision':'Five unit source edges and five exact translated counterparts; each contributes one unit to a complete2-high wall or3-long base, with color/width merged. No redundant overwritten action.'})
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
cap=adapter.scene(q)
try:noop=png_bytes(cap)
finally:cap.close()
assert pixel_hash(noop)==context['original_pixel_sha256']
renderer=PluginRenderer(cfg,adapter,{q:context})
normalized,data,px=renderer.render(plugin)
n2,data2,px2=renderer.render(normalized,frozen=True)
assert n2==normalized and data==data2 and px==px2
(d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2)
save(d/'plugin_submitted.json',plugin);save(d/'plugin.json',normalized)
save(d/'render_check.json',{'at_utc':now(),'fresh_schema_normalization':True,'formal_noop_pixels_match':True,'twice_byte_identical':True,'pixel_sha256':px,'PNG_sha256':sha(d/'candidate.png'),'environment':environment_versions(),'runtime_isolation':isolation,'strict_writeguard':str(OWN)})
save(d/'design.json',{'question_id':q,'branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':'B','expected_wrong_value':'B: U-pentomino consisting of three bottom cells and two upper end cells','correct_answer':'A','mechanism':mechanism,'substantive_difference':difference,'per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'source_reference':'Current user Plane233 C01, actual red-vertical/blue-horizontal open boundary comparison.','status':'PRIMARY_DRAFT; NEW INDEPENDENT REVIEW REQUIRED; NO Pass/Collect'})
assert eligibility()['formal_record']==e['formal_record']
save('checkpoint.json',{'at_utc':now(),'scope':[q],'status':'v3_offline_render_done_pending_visual_and_fresh_process_replay','candidate_directory':str(d),'new_API_calls':0,'second_review_queue':[]},replace=True)
print(json.dumps({'candidate':str(d),'preset':'B','actions':len(actions),'png_sha256':sha(d/'candidate.png'),'tilings':{k:p['tiling_count'] for k,p in proof.items()}},ensure_ascii=False))
