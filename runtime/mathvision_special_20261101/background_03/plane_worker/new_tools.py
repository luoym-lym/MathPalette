import os,sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for variable,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    path=HERE/name;path.mkdir(parents=True,exist_ok=True);os.environ[variable]=str(path)
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write('\n')
def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
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
        files[str(path.relative_to(ROOT))]=file_hash(path);current=json.loads(path.read_text(encoding='utf-8-sig')).get('current',{})
        if current.get('status')=='collected' or current.get('collected_at') or current.get('special_case'):reasons.append('collection')
    return {'eligible':not reasons,'reasons':reasons,'checked_at':datetime.now(timezone.utc).isoformat(),'index_hashes':files}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'new_state');cfg['output_dir']=str(HERE/'new_outputs')
    return cfg,RendererAdapter(cfg)
def inspect(qids):
    cfg,ad=adapter();report=json.loads((ROOT/'runtime/mathvision_special_20261101/exploration_report.json').read_text(encoding='utf-8-sig'))
    seen={r['question_id'] for r in report['attempts']}
    remaining={r['question_id'] for r in read_jsonl(ROOT/'runtime/mathvision_special_20261101/remaining_questions.jsonl')}
    for qid in qids:
        assert qid not in seen and qid in remaining
        check=eligibility(qid);assert check['eligible'],check
        metadata=ad.inspect_question(qid);folder=HERE/qid
        write(folder/'eligibility_at_start.json',check);write(folder/'fresh_context.json',metadata);write(folder/'formal_record.json',ad.records[qid])
        (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
        print(json.dumps({'qid':qid,'question':ad.records[qid]['question'],'answer':ad.records[qid]['answer'],'objects':[{k:v for k,v in r.items() if k in ['id','type','name','points']} for r in metadata['objects']],'snap_points':metadata['snap_points']},ensure_ascii=False),flush=True)
if __name__=='__main__':inspect(sys.argv[1:])
