from tools27 import *
from PIL import Image
import numpy as np,io
q='Plane371';v='r27_word_end_reversal_bundle';folder=HERE/q/v
cfg,ad=adapter();m=ad.inspect_question(q);r=PluginRenderer(cfg,ad,{q:m})
p=json.loads((folder/'plugin.json').read_text(encoding='utf-8'));actual=np.array(Image.open(folder/'candidate.png').convert('RGBA'))
report=[]
for i in range(len(p['params']['actions'])):
    t=copy.deepcopy(p);t['params']['actions'].pop(i)
    _,data,_=r.render(t,frozen=True)
    count=int(np.any(np.array(Image.open(io.BytesIO(data)).convert('RGBA'))!=actual,axis=2).sum())
    report.append({'action_index':i,'target':p['params']['actions'][i]['target'],'pixels_individually_changed':count})
write(folder/'marker_visibility_pixel_audit.json',{'not_a_causal_or_statistical_study':True,'action_removal_visibility_only':report})
print(json.dumps(report))
