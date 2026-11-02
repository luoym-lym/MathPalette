from tools72 import *

q=sys.argv[1]
variant={'Plane335':'r72_congruent_apex_wedge_binding','Plane355':'r72_width_to_fold_measurement_role'}[q]
d=HERE/q/variant
e=eligibility(q);assert e['eligible']
adapter,Renderer,cfg=setup();context=adapter.inspect_question(q)
renderer=Renderer(cfg,adapter,{q:context})
plugin=read(d/'plugin.json');assert renderer.normalize(plugin)==plugin
_,data,pix=renderer.render(plugin,frozen=True)
assert data==(d/'candidate.png').read_bytes()
(d/'offline_replay.png').write_bytes(data)
write(d/'offline_replay_check.json',{'question_id':q,'fresh_process':True,'fresh_source_context':context,'fresh_eligibility':e,'normalized_exact':True,'replay_bytes_equal':True,'candidate_sha256':sha(d/'candidate.png'),'offline_replay_sha256':sha(d/'offline_replay.png'),'plugin_sha256':sha(d/'plugin.json'),'design_sha256':sha(d/'design.json'),'pixel_sha256':pix,'renderer_operations_unchanged':True})
import matplotlib.pyplot as plt
plt.close('all')
print(q,'fresh-process exact offline replay passed',flush=True)
