from unit_env import *
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from workbench_io import pixel_hash, environment_versions

folder=Path(sys.argv[1]).resolve()
assert folder.is_relative_to(OWN)
design=read(folder/'design.json')
qid=design['question_id']
assert qid in QIDS
eligible=eligibility(qid)
assert eligible['eligible']
config,adapter,meta=adapter_context(qid)
canon=lambda v:json.loads(json.dumps(v,ensure_ascii=False,allow_nan=False))
assert canon(meta)==read(folder/'context.json')
original=adapter.scene(qid)
try:
    noop=png_bytes(original)
finally:
    original.close()
assert pixel_hash(noop)==pixel_hash(PROJECT/'PlaneGeometry/image'/f'{qid}.png')
renderer=PluginRenderer(config,adapter,{qid:meta})
plugin=read(folder/'plugin.json')
assert renderer.normalize(plugin)==plugin
norm,data,pix=renderer.render(plugin,frozen=True)
assert norm==plugin
assert data==(folder/'candidate.png').read_bytes()==(folder/'repeat.png').read_bytes()
assert sha(data)==design['candidate_sha256']
assert sha((folder/'plugin.json').read_bytes())==design['plugin_sha256']
assert sha((folder/'context.json').read_bytes())==design['context_sha256']
gates=read(folder/'offline_gates.json')
assert canon(adapter.manifest)==gates['adapter_manifest']
assert environment_versions()==gates['environment']
(folder/'independent_replay.png').write_bytes(data)
save(folder/'independent_replay.json',{'created_at':now(),'pid':os.getpid(),'argv':sys.argv,
     'exact_replay':True,'no_op_pixel_equal':True,'full_context_exact':True,
     'adapter_manifest_exact':True,'environment_exact':True,'fresh_schema_normalized':True,
     'candidate_sha256':sha(data),'pixel_sha256':pix,'design_sha256':sha((folder/'design.json').read_bytes()),
     'plugin_sha256':sha((folder/'plugin.json').read_bytes()),'eligibility':eligible,
     'isolation':ISOLATION,'numeric_tolerance_used':False,'tuple_list_comparison':'exact JSON normalization only'})
print(json.dumps({'qid':qid,'replay_exact':True,'pid':os.getpid()},ensure_ascii=False))
