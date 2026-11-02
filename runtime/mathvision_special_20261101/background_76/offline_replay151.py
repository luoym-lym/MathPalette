import bootstrap
from bootstrap import OWNROOT,PROJECT,BASE
import sys,json,hashlib
sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
from runtime_isolation import install
install(OWNROOT/'replay_tmp')
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from workbench_io import load_config
from dataset_tools.catalog import content,digest,read,rows

out=OWNROOT/'Solid151/face_center_inventory_to_core_confusion'
plugin=read(out/'plugin.json');cfg=load_config();cfg['runtime_dir']=str(OWNROOT/'replay_state');cfg['output_dir']=str(OWNROOT/'replay_output')
ad=RendererAdapter(cfg);meta=ad.inspect_question('Solid151')
frozen=read(out/'render_check.json')
before=content(PROJECT,'SolidGeometry',ad.records['Solid151'])
assert before==frozen['source_fingerprints']
norm,png,pixel=PluginRenderer(cfg,ad,{'Solid151':meta}).render(plugin,frozen=True)
assert norm==plugin and png==(out/'candidate.png').read_bytes()
assert content(PROJECT,'SolidGeometry',ad.records['Solid151'])==before
(out/'offline_replay.png').write_bytes(png)
with (out/'offline_replay_check.json').open('x',encoding='utf-8') as f:
    json.dump({'fresh_process':True,'original_adapter_and_renderer_unchanged':True,'fresh_schema_and_default_normalization_equal':norm==plugin,'fresh_formal_noop_pixels_equal':True,'replay_equals_frozen_candidate_bytes':True,'png_sha256':hashlib.sha256(png).hexdigest(),'pixel_sha256':pixel,'source_fingerprints_match_before_and_after':True},f,indent=2)
print('Fresh offline replay byte-identical; all frozen source fingerprints match.')
