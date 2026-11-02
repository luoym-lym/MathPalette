import research_core as core
rt=core.rt
import sys,json,hashlib,os
from pathlib import Path

d=Path(sys.argv[1]).resolve()
rt.check_write(d)
design=rt.read(d/'design.json');qid=design['question_id']
e=core.eligibility(qid)
assert e['eligible'],e['reasons']
cfg,ad=core.adapter()
meta=ad.inspect_question(qid)
assert json.loads(json.dumps(meta))==rt.read(d/'context.json')
plugin=rt.read(d/'plugin.json')
renderer=core.PluginRenderer(cfg,ad,{qid:meta})
normal,data,pixel=renderer.render(plugin,frozen=True)
assert normal==plugin
assert data==(d/'candidate.png').read_bytes()
assert hashlib.sha256(data).hexdigest()==design['image_sha256']
rt.save(d/'independent_process_replay.json',{'pid':os.getpid(),'completed_at':rt.now(),'byte_exact':True,
    'fresh_adapter':True,'fresh_context_exact_json_normalized':True,'fresh_schema':True,
    'image_sha256':hashlib.sha256(data).hexdigest(),'plugin_sha256':rt.sha(d/'plugin.json'),
    'design_sha256':rt.sha(d/'design.json'),'pixel_sha256':pixel,'source_eligibility':e})
g=rt.read(d/'render_gates.json');g['new_independent_process_exact_replay']=True
rt.save(d/'render_gates.json',g)
print(qid,'FRESH PROCESS EXACT REPLAY',os.getpid(),flush=True)
