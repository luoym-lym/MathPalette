from bootstrap import *
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
import gc
sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
from workbench_io import load_config,environment_versions
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools.mathvision_workbench import png_bytes
from PIL import Image
import matplotlib.pyplot as plt

qid=sys.argv[1]
assert qid in ('Solid206','Solid207')
assert read(HERE/'zero_prior_invocation_qualified.json')['zero_visible_exact_prior_invocations']
e=read(HERE/qid/'fresh_eligibility_and_approval.json');assert e['eligible']
q=next(q for q in read(BASE/'background_63_assignment.json')['questions'] if q['question_id']==qid)
src=Path(q['source_directory']);d=HERE/qid
cfg=load_config();cfg['runtime_dir']=str(HERE/'state');cfg['output_dir']=str(HERE/'output')
adapter=RendererAdapter(cfg)
ctx=adapter.inspect_question(qid);write(d/'fresh_context.json',ctx)
assert ctx==read(src/'context.json')
scene=adapter.scene(qid)
try:
    data=png_bytes(scene);(d/'fresh_baseline.png').write_bytes(data)
    with Image.open(PROJECT/'SolidGeometry'/e['record']['image']) as a,Image.open(d/'fresh_baseline.png') as b:
        assert a.size==b.size==(768,768) and a.convert('RGBA').tobytes()==b.convert('RGBA').tobytes()
    scene.fig.canvas.draw()
    paths={o['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'controls':[seg['control'].tolist() for seg in p['segments']]} for p in object_paths(scene,o['id'])] for o in ctx['objects'] if o.get('styleable')}
    write(d/'fresh_exact_paths.json',paths)
finally: scene.close()
plugin=read(src/'plugin.json');renderer=PluginRenderer(cfg,adapter,{qid:ctx})
normalized,data,pixels=renderer.render(plugin,frozen=True)
normalized2,data2,pixels2=renderer.render(plugin,frozen=True)
assert normalized==normalized2==plugin
assert data==data2==(src/'candidate.png').read_bytes()==(src/'repeat.png').read_bytes()
assert pixels==pixels2==read(src/'design.json')['pixel_sha256']
(d/'fresh_replay.png').write_bytes(data)
scene=read(PROJECT/'SolidGeometry'/e['record']['scene'])
write(d/'fresh_schema_native_replay.json',dict(checked_at=now(),no_op_pixel_equal=True,context_exactly_equals_old=True,actual_schema_normalization=True,plugin_normalization_unchanged=True,twice_byte_identical=True,fresh_replay_exactly_equals_frozen=True,png_sha256=sha(d/'fresh_replay.png'),pixel_sha256=pixels,environment=environment_versions(),projection=scene['projection'],visibility=scene['visibility'],scene_sha256=sha(PROJECT/'SolidGeometry'/e['record']['scene']),original_JPG_sha256=sha(PROJECT/'SolidGeometry'/e['record']['original_image']),formal_PNG_sha256=sha(PROJECT/'SolidGeometry'/e['record']['image']),actions_with_actual_paths=[{'action':a,'object':next(o for o in ctx['objects'] if o['id']==a['target']),'paths':paths[a['target']]} for a in plugin['params']['actions']],isolation=ISOLATION))
plt.close('all')
del ctx,paths,scene,renderer,adapter,data,data2,plugin,normalized,normalized2;gc.collect()
print(qid,'fresh context/native/no-op/schema/replay exact; figures closed',flush=True)
