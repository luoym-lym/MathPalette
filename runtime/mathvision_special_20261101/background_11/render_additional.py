from tools_local import *
from render_designs import render
cfg,ad=adapter()
for qid,vid in [('Plane282','exposed_step_unit_transfer'),('Plane293','triangle_count_scale_transfer')]:render(qid,vid,cfg,ad)
