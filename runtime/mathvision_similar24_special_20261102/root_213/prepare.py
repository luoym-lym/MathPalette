from bootstrap import *
import itertools,copy
from runtime_isolation import install
isolated=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
q='Plane213';vid='user233_boundary_spine_foot_transfer_v1'
d=OWN/q/vid;d.mkdir(parents=True,exist_ok=False)
e=eligibility();save(d/'eligibility_before_design.json',e)
ref=TASK/'references/Plane233'
assert sha(ROOT/'PlaneGeometry/image/Plane213.png')==sha(ref/'original.png')
plugin=read(ref/'C01.json');assert plugin['question_id']=='Plane233'
# Coalesce disjoint property edits on the same target. Final appearance is unchanged.
merged={}
for a in plugin['params']['actions']:
 assert a['type']=='set_object_style' and 'interval' not in a
 merged.setdefault(a['target'],{}).update(a)
actions=list(merged.values());assert len(actions)==12
plugin['question_id']=q
plugin['params']['actions']=actions
plugin['description']='沿用用户Plane233 C01：原棋盘与选项C的四格红竖边、两格蓝底边对应。'
plugin['intent']='诱导把真实局部可放入误作三份全等拼块能铺满。'
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg);context=adapter.inspect_question(q)
renderer=PluginRenderer(cfg,adapter,{q:context})
save(d/'fresh_context.json',context)
def norm(s):
 return frozenset((x-min(a for a,b in s),y-min(b for a,b in s)) for x,y in s)
def cells(prefix):
 edges=set()
 for obj in context['objects']:
  if not obj['id'].startswith(prefix):continue
  pts=obj['geometry']['points']
  assert len(pts)==2 and all(float(v).is_integer() for p in pts for v in p)
  edges.add(frozenset((int(x),int(y)) for x,y in pts))
 coords=[p for edge in edges for p in edge];out=set()
 for x in range(min(p[0] for p in coords),max(p[0] for p in coords)):
  for y in range(min(p[1] for p in coords),max(p[1] for p in coords)):
   vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
   if all(frozenset([vs[i],vs[(i+1)%4]]) in edges for i in range(4)):out.add((x,y))
 return norm(out)
def forms(s):
 out=set()
 for flip in [-1,1]:
  t={(flip*x,y) for x,y in s}
  for i in range(4):out.add(norm(t));t={(-y,x) for x,y in t}
 return out
board=cells('given_');assert len(board)==15
proof={}
for letter in 'ABCDE':
 shape=cells(letter+'_');assert len(shape)==5
 placements=set()
 for f in forms(shape):
  for x,y in itertools.product(range(4),repeat=2):
   p=frozenset((x+a,y+b) for a,b in f)
   if p<=board:placements.add(p)
 tilings=[t for t in itertools.combinations(placements,3) if len(set().union(*t))==15]
 proof[letter]={'cells':sorted(shape),'placements':len(placements),'tilings':len(tilings),'witnesses':[[sorted(p) for p in t] for t in tilings]}
assert [proof[k]['tilings'] for k in 'ABCDE']==[2,0,0,0,0]
objects={o['id']:o for o in context['objects']}
roles=[]
for prefix in ['given_','C_']:
 pts=[p for o in context['objects'] if o['id'].startswith(prefix) for p in o['geometry']['points']]
 x0=min(p[0] for p in pts);y0=min(p[1] for p in pts)
 for a in [a for a in actions if a['target'].startswith(prefix)]:
  ps=objects[a['target']]['geometry']['points']
  if a['color']=='#DC2626':assert all(p[0]==x0 for p in ps);role='四格竖直外边界的一格，与另一图的同长竖边对应'
  else:assert a['color']=='#2563EB' and all(p[1]==y0 for p in ps) and max(p[0] for p in ps)<=x0+2;role='外底边左端两格中的一格，定位与另一图同长的底脚'
  roles.append({'target':a['target'],'points':ps,'color':a['color'],'role':role,'source_is_external_boundary':True})
capture=adapter.scene(q)
try:noop=png_bytes(capture)
finally:capture.close()
assert pixel_hash(noop)==context['original_pixel_sha256']
normalized,data,px=renderer.render(plugin)
n2,data2,px2=renderer.render(normalized,frozen=True)
assert n2==normalized and data==data2 and px==px2
(d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2)
save(d/'plugin_submitted.json',plugin);save(d/'plugin.json',normalized)
save(d/'math_primary_proof.json',{'method':'Fresh exact-cover enumeration from current Plane213 frozen unit edges; all D4 orientations, translations and all triples.','board':sorted(board),'options':proof,'unique_correct_answer':'A'})
save(d/'marker_roles.json',roles)
save(d/'reference_transfer.json',{'source_question':'Plane233','source_C01_png_sha256':sha(ref/'C01.png'),'source_C01_plugin_sha256':sha(ref/'C01.json'),'same_formal_base_PNG':True,'source_action_count':13,'merged_action_count':12,'merge':'Coalesce the separate color and width edits of C_1, preserving all final target properties.','candidate_PNG_matches_user_C01_bytes':sha(d/'candidate.png')==sha(ref/'C01.png'),'no_internal_source_partition':True})
save(d/'render_check.json',{'at':now(),'schema_actual_normalization':True,'formal_noop_pixels_match':True,'twice_byte_identical':True,'pixel_sha256':px,'PNG_sha256':sha(d/'candidate.png'),'environment':environment_versions(),'isolation':isolated})
save(d/'design.json',{'question_id':q,'branch':'PlaneGeometry','variant_id':vid,'created_at':now(),'expected_wrong_answer':'C','correct_answer':'A','mechanism':plugin['intent'],'source_reference':'Plane233 current user C01 frozen in reference_manifest.json','per_marker_roles':roles,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':px,'status':'PRIMARY_DRAFT; NEW INDEPENDENT REVIEW REQUIRED; NO Pass/Collect'})
assert eligibility()['formal_record']==e['formal_record']
print(json.dumps({'question_id':q,'candidate':str(d),'preset':'C','correct':'A','PNG_sha256':sha(d/'candidate.png'),'matches_current_user_C01_bytes':sha(d/'candidate.png')==sha(ref/'C01.png')},ensure_ascii=False))
