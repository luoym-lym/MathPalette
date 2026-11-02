from tools57 import *
spec=read(sys.argv[1]);qid=spec['question_id'];assert qid in IDS
d=HERE/qid/spec['variant_id'];d.mkdir(exist_ok=False)
write(d/'design_difference_audit.json',spec['difference_audit'])
e=eligibility(qid);write(d/'eligibility_before_design.json',e);assert e['eligible']
adapter,Renderer,cfg=setup();c=adapter.inspect_question(qid);write(d/'context.json',c)
from workbench_io import environment_versions
plugin=dict(plugin_schema_version='1.0.0',question_id=qid,category='C',operation='C_manual',description=spec['description'],intent=spec['mechanism'],params={'actions':spec['actions']})
renderer=Renderer(cfg,adapter,{qid:c})
normalized,data,pixel=renderer.render(plugin)
normalized2,data2,pixel2=renderer.render(normalized,frozen=True)
assert data==data2 and pixel==pixel2 and normalized==normalized2
(d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2);write(d/'plugin.json',normalized)
design={k:v for k,v in spec.items() if k not in ['actions','difference_audit']}
design.update(created_at=now(),png_sha256=sha(d/'candidate.png'),plugin_sha256=sha(d/'plugin.json'),pixel_sha256=pixel,review_status='PRIMARY research only; parent must request NEW independent review; no approval')
write(d/'design.json',design)
write(d/'render_check.json',dict(no_op_pixel_equal=True,schema_default_normalization=True,twice_byte_identical=True,environment=environment_versions(),source_hashes=frozen_files(e['record'])))
print(qid,spec['variant_id'],'frozen',design['png_sha256'],flush=True)
