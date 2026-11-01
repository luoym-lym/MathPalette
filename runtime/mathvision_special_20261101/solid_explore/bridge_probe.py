from pathlib import Path
import os,sys,json,time
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
for key,name in {'MPLCONFIGDIR':'mpl_cache','TEMP':'temp','TMP':'temp','XDG_CACHE_HOME':'cache'}.items():
    target=OUT/name;target.mkdir(parents=True,exist_ok=True);os.environ[key]=str(target)
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
isolation=install(OUT/'bridge_render_tmp')
from dataset_tools.mathvision_workbench import build_scene,png_bytes
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import pixel_hash
records={r['id']:r for r in map(json.loads,(ROOT/'SolidGeometry/dataset.jsonl').read_text(encoding='utf-8').splitlines())}
results=[]
for qid in sys.argv[1:] or ['Solid166','Solid203','Solid171','Solid106','Solid169','Solid240']:
    start=time.monotonic()
    try:
        scene=build_scene(ROOT/'SolidGeometry',records[qid])
        try:
            data=png_bytes(scene);original=pixel_hash(ROOT/'SolidGeometry'/records[qid]['image']);actual=pixel_hash(data)
            result={'question_id':qid,'baseline_matches_formal':actual==original,'original_pixel_sha256':original,'bridge_pixel_sha256':actual,'object_count':len(scene.objects),'styleable_objects':[o['id'] for o in scene.objects if o.get('styleable')],'snap_point_count':len(scene.snap_points),'isolation':isolation,'elapsed_seconds':round(time.monotonic()-start,2)}
            if actual==original:(OUT/f'{qid}_bridge_original.png').write_bytes(data)
        finally:scene.close()
    except Exception as error:result={'question_id':qid,'error':str(error),'elapsed_seconds':round(time.monotonic()-start,2)}
    results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'bridge_probe_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
