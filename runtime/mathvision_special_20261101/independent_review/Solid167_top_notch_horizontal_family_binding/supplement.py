from pathlib import Path
import os,sys,json,hashlib
from datetime import datetime,timezone
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
SESSION=ROOT/'runtime/mathvision_special_20261101'
SOURCE=SESSION/'background_07/solid_worker/Solid167'
CAND=SOURCE/'top_notch_horizontal_family_binding'
for key,sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    os.environ[key]=str(HERE/sub)
os.environ['PYTHONDONTWRITEBYTECODE']='1'
def allowed(path):
    if path is not None and not isinstance(path,int) and not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):
        raise PermissionError('Outside review directory: '+str(path))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):allowed(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):allowed(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):allowed(args[0]);allowed(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(SESSION))
from runtime_isolation import install
install(HERE/'render_tmp')
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from PIL import Image
import numpy as np
from workbench_io import load_config
import quick_test
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
audit=read(HERE/'audit_results.json')
binding=read(next((CAND/'tests').iterdir())/'binding.json')
request=read(next((CAND/'tests').iterdir())/'request.json')
scene=read(ROOT/'SolidGeometry/dataset_generator/scenes/Solid167.json')
ctx=read(CAND/'context.json')
with Image.open(CAND/'candidate.png') as im:a=np.array(im.convert('RGBA')).astype(int)
with Image.open(ROOT/'SolidGeometry/image/Solid167.png') as im:b=np.array(im.convert('RGBA')).astype(int)
delta=np.max(np.abs(a-b),axis=2)
small=[]
large=[]
for comp in audit['pixel_difference']['components']:
    x0,y0,x1,y1=comp['bbox_inclusive']
    part={**comp,'maximum_channel_change':int(delta[y0:y1+1,x0:x1+1].max())}
    (small if comp['changed_pixels']<10 else large).append(part)
tr=np.array(ctx['canvas']['data_to_pixel'])
p=scene['points']
holes={}
for label,fid in zip('ABCDE',['face19','face26','face33','face40','face47']):
    obj=next(o for o in scene['objects'] if o['id']==fid)
    data=[]
    for ids in obj['holes']:
        xy=np.array([p[v][:2] for v in ids]);extent=np.ptp(xy,axis=0)
        ctr=tr@np.r_[xy.mean(0),1]
        x,y=np.rint(ctr[:2]).astype(int)
        data.append({'point_ids':ids,'width_height_ratio':float(extent[0]/extent[1]),'centre_pixel':[int(x),int(y)],'centre_RGBA':a[y,x].tolist(),'pixel_extents':(np.abs(tr[:2,:2])@extent).tolist()})
    holes[label]={'hole_count':len(data),'fill':obj['fill'],'holes':data}
def project(pt):
    pr=scene['projection'];return (np.array(pr['matrix'])@(np.array(pt)-np.array(pr['origin']))+np.array(pr['offset'])).tolist()
notch_projection={}
for flat,drawn in [('p49','p16'),('p50','p15'),('p51','p14'),('p52','p20'),('p53','p19'),('p54','p18')]:
    notch_projection[flat]={'flat':p[flat],'drawn_id':drawn,'drawn_world':p[drawn],'projected_drawn':project(p[drawn])}
helper_paths=['runtime/mathvision_special_20261101/runtime_isolation.py','runtime/mathvision_special_20261101/harness/quicktest3_isolated.py','runtime/mathvision_special_20261101/background_07/solid_worker/bridge_adapter_local.py','runtime/mathvision_special_20261101/background_07/solid_worker/run_candidate.py','runtime/mathvision_special_20261101/background_07/solid_worker/prepare167_second.py','runtime/mathvision_special_20261101/background_07/solid_worker/design_tools.py','runtime/mathvision_special_20261101/background_07/second_review_queue.json','runtime/mathvision_special_20261101/background_07/source_preservation_classification_final.json']
extra={'checked_at':datetime.now(timezone.utc).isoformat(),'small_raster_components':small,'six_substantive_mark_components':large,'option_fill_hole_and_native_size_checks':holes,'notch_projection_correspondence':notch_projection,'helper_sha256':{s:sha(ROOT/s) for s in helper_paths},'extra_checks':{'small_differences_only_at_most_one_gray_level':all(c['maximum_channel_change']<=1 for c in small),'exactly_six_substantive_mark_components':len(large)==6,'current_reference_system_prompt_exact':request['messages'][0]['content']==quick_test.SYSTEM_PROMPT,'current_reference_profile_exact':binding['settings']=={**quick_test.TEST_PROFILES['quicktest3'],'api_base':load_config()['quick_test']['mimo_api_base']},'runtime_original_copy_exact_formal_png':(SOURCE/'original.png').read_bytes()==(ROOT/'SolidGeometry/image/Solid167.png').read_bytes(),'source_scene_snapshot_equals_current_formal_scene':read(SOURCE/'source_scene_snapshot.json')==scene,'runtime_adapter_hash_exact':sha(SESSION/'background_07/solid_worker/bridge_adapter_local.py')==read(SOURCE/'frozen_inputs.json')['runtime_adapter_sha256'],'all_hole_centres_remain_white':all(h['centre_RGBA']==[255,255,255,255] for d in holes.values() for h in d['holes'])}}
with (HERE/'supplement_results.json').open('x',encoding='utf-8') as f:json.dump(extra,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(extra,ensure_ascii=False,indent=2))
