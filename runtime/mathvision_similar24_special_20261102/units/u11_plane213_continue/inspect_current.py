from bootstrap import *
from runtime_isolation import install
iso=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,environment_versions,pixel_hash
from mathvision_adapter import RendererAdapter
from dataset_tools.mathvision_workbench import png_bytes
cfg=load_config();cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg)
c=adapter.inspect_question('Plane213')
save('current_context.json',c)
cap=adapter.scene('Plane213')
try: data=png_bytes(cap)
finally:cap.close()
assert pixel_hash(data)==c['original_pixel_sha256']
(OWN/'fresh_noop.png').write_bytes(data)
save('environment_and_noop.json',{'at_utc':now(),'isolation':iso,'strict_writeguard':str(OWN),'environment':environment_versions(),'threads':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},'noop_png_sha256':sha(OWN/'fresh_noop.png'),'noop_pixel_sha256':pixel_hash(data),'formal_original_pixel_sha256':c['original_pixel_sha256']})
print(json.dumps({'question':c.get('question'),'objects':[{'id':o['id'],'geometry':o['geometry']} for o in c['objects']]},ensure_ascii=False))
