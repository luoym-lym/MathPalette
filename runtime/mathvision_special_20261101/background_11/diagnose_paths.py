from tools_local import *
from dataset_tools.mathvision_workbench import png_bytes
cfg,ad=adapter();qid='Plane473';result=[]
for action in ['draw','png','draw_png','none']:
    s=ad.scene(qid)
    try:
        if 'draw' in action:s.fig.canvas.draw()
        if 'png' in action:png_bytes(s)
        paths={oid:[{'id':p['id'],'sha256':p['sha256'],'controls':[v['control'].tolist() for v in p['segments']]} for p in object_paths(s,oid)] for oid in ['c03','center']}
        result.append({'phase':action,'paths':paths})
    finally:s.close()
write(HERE/'partial_path_diagnostic.json',result)
print(json.dumps(result))
