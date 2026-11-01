"""Verify the portable delivery bridge against the actual tested Solid203 PNG."""
import hashlib
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
OUT=HERE/'delivery_validation'/'Solid203'
OUT.mkdir(parents=True,exist_ok=True)
for variable,sub in [('MPLCONFIGDIR','mpl'),('TEMP','tmp'),('TMP','tmp'),('XDG_CACHE_HOME','cache')]:
    p=OUT/sub;p.mkdir(exist_ok=True);os.environ[variable]=str(p)
sys.path.insert(0,str(HERE))
from runtime_isolation import install
install(OUT/'render_tmp')
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import load_config
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer

SOURCE=HERE/'background_03/solid_worker/Solid203/bridge_terminal_edge_pair'
config=load_config()
config['runtime_dir']=str(OUT/'state')
config['output_dir']=str(OUT/'output')
adapter=RendererAdapter(config)
metadata=adapter.inspect_question('Solid203')
renderer=PluginRenderer(config,adapter,{'Solid203':metadata})
plugin=json.loads((SOURCE/'plugin.json').read_text(encoding='utf-8'))
normalized,image,pixels=renderer.render(plugin,frozen=True)
assert image==(SOURCE/'candidate.png').read_bytes()
normalized2,image2,pixels2=renderer.render(plugin,frozen=True)
assert image2==image and pixels2==pixels
(OUT/'reproduced.png').write_bytes(image)
result={'question_id':'Solid203','dedicated_bridge_delivery_adapter':True,
        'formal_noop_baseline_matches':True,'matches_tested_png_bytes':True,
        'two_delivery_replays_identical':True,'png_sha256':hashlib.sha256(image).hexdigest(),
        'pixel_sha256':pixels,'new_solver_calls':0,'quality_second_review':'still_required'}
(OUT/'replay_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
