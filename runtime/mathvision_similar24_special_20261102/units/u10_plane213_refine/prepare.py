from bootstrap import *
import itertools
from runtime_isolation import install
isolation=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
q='Plane213';vid='user233_exterior_concave_corner_to_B_v2';d=OWN/q/vid;d.mkdir(parents=True,exist_ok=False)
e=eligibility();save(d/'eligibility_before_design.json',e)
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);context=adapter.inspect_question(q);save(d/'fresh_context.json',context)
objects={o['id']:o for o in context['objects']}
R='#DC2626';B='#2563EB'
actions=[{'type':'set_object_style','target':t,'color':c,'linewidth_pt':1.5} for t,c in [('given_27',R),('B_11',R),('given_29',B),('B_8',B)]]
expected={'given_27':[[14,7],[14,8]],'given_29':[[14,8],[15,8]],'B_11':[[8,1],[8,2]],'B_8':[[7,1],[8,1]]}
for t,ps in expected.items():assert objects[t]['geometry']['points']==ps
H=lambda p:(22-p[0],9-p[1])
assert set(map(H,expected['given_27']))==set(map(tuple,expected['B_11']))
assert set(map(H,expected['given_29']))==set(map(tuple,expected['B_8']))
def norm(s):
 x0=min(x for x,y in s);y0=min(y for x,y in s)
 return frozenset((x-x0,y-y0) for x,y in s)
def rawcells(prefix):
 edges=set()
 for o in context['objects']:
  if not o['id'].startswith(prefix):continue
  ps=o['geometry']['points'];assert len(ps)==2 and all(float(v).is_integer() for p in ps for v in p)
  edges.add(frozenset((int(x),int(y)) for x,y in ps))
 coords=[p for edge in edges for p in edge];out=set()
 for x in range(min(p[0] for p in coords),max(p[0] for p in coords)):
  for y in range(min(p[1] for p in coords),max(p[1] for p in coords)):
   vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
   if all(frozenset([vs[i],vs[(i+1)%4]]) in edges for i in range(4)):out.add((x,y))
 return out
def forms(s):
 out=set()
 for flip in [-1,1]:
  t={(flip*x,y) for x,y in s}
  for i in range(4):out.add(norm(t));t={(-y,x) for x,y in t}
 return out
board=norm(rawcells('given_'));assert len(board)==15
proof={}
for letter in 'ABCDE':
 shape=norm(rawcells(letter+'_'));assert len(shape)==5
 placements=set()
 for f in forms(shape):
  for x,y in itertools.product(range(4),repeat=2):
   p=frozenset((x+a,y+b) for a,b in f)
   if p<=board:placements.add(p)
 tilings=[t for t in itertools.combinations(placements,3) if len(set().union(*t))==15]
 proof[letter]={'cells':sorted(shape),'forms':len(forms(shape)),'placements':len(placements),'tilings':len(tilings),'witnesses':[[sorted(p) for p in t] for t in tilings]}
assert [proof[k]['tilings'] for k in 'ABCDE']==[2,0,0,0,0]
# Each marked source/option segment is an actual exterior edge, incident to exactly one cell.
for a in actions:
 ps=expected[a['target']];cells=rawcells('given_' if a['target'].startswith('given_') else 'B_');edge=frozenset(map(tuple,ps));incident=0
 for x,y in cells:
  vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
  incident+=any(frozenset([vs[i],vs[(i+1)%4]])==edge for i in range(4))
 assert incident==1,(a['target'],incident)
for prefix,corner in [('given_',(14,8)),('B_',(8,1))]:
 x,y=corner;assert sum((x+dx,y+dy) in rawcells(prefix) for dx,dy in [(-1,-1),(-1,0),(0,-1),(0,0)])==3
roles=[{'target':a['target'],'color':a['color'],'points':expected[a['target']],'role':('红色竖边：真实凹角的一条单位臂，对应另一图半周旋转后的单位竖边。' if a['color']==R else '蓝色横边：同一真实凹角的另一单位臂，与竖边共同固定对应方向。'),'actual_exterior_edge':True} for a in actions]
mechanism='用红色单位竖边、蓝色单位横边，将原棋盘缺角处的真实外凹角与选项B的内凹槽角作半周旋转对应，诱导把局部边界兼容误作三份B能铺满。'
difference='旧Plane213的三边红U使用内部网格并指向B；root当前用户C01迁移使用完整四格外竖边与两格底脚并指向C，B/C未双中。本方案改为实际外边界的270度凹角两单位臂与B对应；零内部源边、无完整源拼块轮廓、没有原C长边配对。不是旧目标图的改色/加粗重试。旧Plane233 r23外凹角方案仅为不同正式题干下的历史参考，旧D/B保留；此图颜色方向与当前用户红竖蓝横习惯一致，且不是其旧PNG。'
save(d/'design_difference_audit.json',{'at_utc':now(),'expected_wrong_answer_before_calls':'B','new_mechanism':mechanism,'substantive_difference':difference,'preserved_old_Plane213_wrong_B_finals':['C','B'],'preserved_root_transfer_wrong_C_finals':['B','C'],'preserved_old_Plane233_wrong_B_finals':['D','B'],'no_posthoc_relabel':True,'per_marker_roles':roles})
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
capture=adapter.scene(q)
try:noop=png_bytes(capture)
finally:capture.close()
assert pixel_hash(noop)==context['original_pixel_sha256']
renderer=PluginRenderer(cfg,adapter,{q:context});normalized,data,px=renderer.render(plugin);n2,data2,px2=renderer.render(normalized,frozen=True)
assert n2==normalized and data==data2 and px==px2
(d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2)
save(d/'plugin_submitted.json',plugin);save(d/'plugin.json',normalized)
save(d/'math_primary_proof.json',{'at_utc':now(),'method':'Fresh exhaustive exact-cover enumeration extracted from CURRENT frozen object edges. All D4 orientations, valid translations, and unordered triples; no shape inferred from colored pixels.','board':sorted(board),'options':proof,'unique_correct_answer':'A','concave_corner_transform':'(x,y)->(22-x,9-y)','source_marked_edges_incident_to_one_cell':True,'source_and_B_corner_incident_to_three_quadrant_cells':True})
save(d/'render_check.json',{'at_utc':now(),'schema_actual_normalization':True,'formal_noop_pixels_match':True,'twice_byte_identical':True,'pixel_sha256':px,'PNG_sha256':sha(d/'candidate.png'),'environment':environment_versions(),'runtime_isolation':isolation})
save(d/'design.json',{'question_id':q,'branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':'B','correct_answer':'A','mechanism':mechanism,'substantive_difference':difference,'per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'source_reference':'Current user Plane233 C01: red vertical / blue horizontal feature correspondence; adapted to actual exterior concavity instead of failed long spine.','status':'PRIMARY_DRAFT; REQUIRES FRESH INDEPENDENT REVIEW; NO Pass/Collect'})
assert eligibility()['formal_record']==e['formal_record']
assert sha(d/'candidate.png')!=sha(TASK/'root_213/Plane213/user233_boundary_spine_foot_transfer_v1/candidate.png')
assert sha(d/'candidate.png')!='11ec2082b45eb8db6a001d538a0c4b7755fbbc6943c364589c4684c7ab4e1c6a'
print(json.dumps({'question_id':q,'candidate':str(d),'preset':'B','correct':'A','PNG_sha256':sha(d/'candidate.png'),'actions':4},ensure_ascii=False))
