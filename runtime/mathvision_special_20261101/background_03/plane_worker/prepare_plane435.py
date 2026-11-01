import os,sys,json,hashlib,shutil
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for variable,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    path=HERE/name;path.mkdir(parents=True,exist_ok=True);os.environ[variable]=str(path)
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
isolation=install(HERE/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def write(path,value):
    with path.open('x',encoding='utf-8') as stream:json.dump(value,stream,ensure_ascii=False,indent=2);stream.write('\n')
def eligibility(qid):
    base=ROOT/'PlaneGeometry/special_variant';reasons=[];files={}
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        path=base/name
        if path.exists():files[str(path.relative_to(ROOT))]=file_hash(path)
        if any(r.get('question_id')==qid and r.get('status')==status for r in read_jsonl(path)):reasons.append(name)
    path=base/qid/'recipes.json'
    if path.exists():
        files[str(path.relative_to(ROOT))]=file_hash(path);data=json.loads(path.read_text(encoding='utf-8-sig'))
        entries=data if isinstance(data,list) else data.get('recipes',data.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('recipes')
    path=base/qid/'collection.json'
    if path.exists():
        files[str(path.relative_to(ROOT))]=file_hash(path);data=json.loads(path.read_text(encoding='utf-8-sig'));current=data.get('current',{})
        if current.get('status')=='collected' or current.get('collected_at') or current.get('special_case'):reasons.append('collection')
    return {'eligible':not reasons,'exclusion_reasons':reasons,'checked_at':datetime.now(timezone.utc).isoformat(),'index_sha256':files}
config=load_config();config['runtime_dir']=str(HERE/'render_runtime');config['output_dir']=str(HERE/'render_output')
adapter=RendererAdapter(config);qid='Plane435'
check=eligibility(qid);assert check['eligible'],check
metadata=adapter.inspect_question(qid)
renderer=PluginRenderer(config,adapter,{qid:metadata})
record=adapter.records[qid]
paths=[record['image'],record['scene'],record['script'],record['original_image'],*record.get('runtime_dependencies',[])]
inputs={str((ROOT/'PlaneGeometry'/p).relative_to(ROOT)):file_hash(ROOT/'PlaneGeometry'/p) for p in sorted(set(paths))}
if not (HERE/'question_eligibility.json').exists():write(HERE/'question_eligibility.json',check)
if not (HERE/'fresh_context.json').exists():write(HERE/'fresh_context.json',metadata)
if not (HERE/'original.png').exists():shutil.copyfile(adapter.original_paths[qid],HERE/'original.png')
if not (HERE/'formal_record.json').exists():write(HERE/'formal_record.json',record)
for vid in ['v01','v02']:
    source=ROOT/'runtime/mathvision_special_20261101/plane_explore'/qid/vid
    target=HERE/qid/vid;target.mkdir(parents=True,exist_ok=True)
    for name in ['plugin.json','candidate.png','design.json']:
        dest=target/('prepared_source_design.json' if name=='design.json' else name)
        if not dest.exists():shutil.copyfile(source/name,dest)
        assert dest.read_bytes()==(source/name).read_bytes()
    plugin=json.loads((target/'plugin.json').read_text(encoding='utf-8'))
    before=canonical_hash(record)
    normalized,data,digest=renderer.render(plugin)
    normalized2,data2,digest2=renderer.render(normalized,frozen=True)
    assert normalized==plugin and normalized2==normalized
    assert data==data2==(target/'candidate.png').read_bytes() and digest==digest2
    assert inputs=={str((ROOT/'PlaneGeometry'/p).relative_to(ROOT)):file_hash(ROOT/'PlaneGeometry'/p) for p in sorted(set(paths))}
    design=json.loads((target/'prepared_source_design.json').read_text(encoding='utf-8'))
    design.update(expected_wrong_answer=design['predicted_wrong_answer'],prepared_source=str(source.relative_to(ROOT)),image_path=str(target/'candidate.png'),plugin_path=str(target/'plugin.json'),prepared_design_sha256=file_hash(target/'prepared_source_design.json'),created_at=datetime.now(timezone.utc).isoformat(),review_status='PRIMARY_EXPLORATION_ONLY_REQUIRES_NEW_INDEPENDENT_SECOND_REVIEW')
    if not (target/'design.json').exists():write(target/'design.json',design)
    write(target/'render_check.json',{'question_id':qid,'variant_id':vid,'baseline_matches_formal':True,'schema_normalization_exact':True,'twice_byte_identical':True,'prepared_image_byte_identical':True,'pixel_sha256':digest,'png_sha256':file_hash(target/'candidate.png'),'plugin_sha256':file_hash(target/'plugin.json'),'design_sha256':file_hash(target/'design.json'),'question_record_sha256':before,'frozen_inputs':inputs,'isolation':isolation,'actions':normalized['params']['actions']})
    print(qid,vid,'fresh baseline/schema/replay OK',flush=True)
