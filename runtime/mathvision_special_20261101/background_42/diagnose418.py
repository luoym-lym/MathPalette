from env42 import *
from dataset_tools.mathvision_workbench import png_bytes
cfg,ad=adapter();m=ad.inspect_question('Plane418');s=ad.scene('Plane418')
out={'created_at':now(),'prior_failure':'Local rendering only, no PNG or API request; exact interval hash rejection preserved in original draft difference audit.','context':{t['id']:t['partial_paths'][0]['sha256'] for t in m['canvas']['targets']}}
def paths():return {o['id']:[{'id':p['id'],'sha256':p['sha256'],'controls':[t['control'].tolist() for t in p['segments']]} for p in object_paths(s,o['id'])] for o in s.objects if o['styleable']}
out['initial']=paths();s.fig.canvas.draw();out['after_canvas_draw']=paths();png_bytes(s);out['after_png_serialization']=paths();s.close()
write(HERE/'Plane418/local_path_diagnostic.json',out)
print(json.dumps({k:{o:(p[0]['sha256'] if isinstance(p,list) else p) for o,p in v.items()} for k,v in out.items() if isinstance(v,dict)},ensure_ascii=False))
