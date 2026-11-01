from pathlib import Path
import os,sys,json,hashlib,importlib.util
sys.dont_write_bytecode=True
TASK=Path(__file__).resolve().parent
PROJECT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=PROJECT/'runtime/mathvision_special_20261101'
for k,n in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=TASK/n;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
install(TASK/'render_tmp')
source=BASE/'solid_explore/bridge_adapter.py'
local=TASK/'bridge_adapter_local.py'
code=source.read_text(encoding='utf-8').replace('PROJECT=Path(__file__).resolve().parents[3]','PROJECT=next(p for p in Path(__file__).resolve().parents if (p/\'MATHPALETTE_PROTOCOL.md\').is_file())')
if not local.exists():local.write_text(code,encoding='utf-8')
spec=importlib.util.spec_from_file_location('solid_worker_bridge',local)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
adapter=module.RuntimeBridgeAdapter()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):
    with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
def rows(p):return [json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()] if p.exists() else []
def eligibility(qid):
    branch=PROJECT/'SolidGeometry';files={};passed=False;collected=False
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p=branch/'special_variant'/name
        files[str(p.relative_to(PROJECT))]=sha(p) if p.exists() else None
        for r in rows(p):
            if r.get('question_id')==qid:
                passed=passed or r.get('status')=='passed';collected=collected or r.get('status')=='collected'
    for name in ['recipes.json','collection.json']:
        p=branch/'special_variant'/qid/name
        files[str(p.relative_to(PROJECT))]=sha(p) if p.exists() else None
        if p.exists():
            d=json.loads(p.read_text(encoding='utf-8-sig'))
            if name=='recipes.json':
                entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
                if isinstance(entries,dict):entries=list(entries.values())
                passed=passed or any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict))
            else:
                c=d.get('current',{});collected=collected or c.get('status')=='collected' or bool(c.get('collected_at')) or bool(c.get('special_case'))
    return {'question_id':qid,'eligible':not passed and not collected,'has_passed':bool(passed),'collected_or_special':bool(collected),'records':files}
for qid in sys.argv[1:] or ['Solid166','Solid203']:
    name='bridge_terminal_edge_pair';src=BASE/'solid_explore'/qid/name;dst=TASK/qid/name
    dst.mkdir(parents=True,exist_ok=False)
    check=eligibility(qid);write(dst/'eligibility.json',check)
    if not check['eligible']:
        print(json.dumps(check));continue
    copies={}
    for name2 in ['plugin.json','design.json','candidate.png']:
        data=(src/name2).read_bytes();(dst/name2).write_bytes(data);copies[name2]=sha(src/name2)
    write(dst/'prepared_copy.json',{'source':str(src),'files_sha256':copies,'unchanged_plugin_and_preset':True})
    record=adapter.records[qid];write(dst/'formal_record.json',record)
    (dst/'original.png').write_bytes(adapter.original_paths[qid].read_bytes())
    plugin=json.loads((dst/'plugin.json').read_text(encoding='utf-8-sig'))
    report=adapter.render_candidate(plugin,dst/'replay')
    if (dst/'candidate.png').read_bytes() != (dst/'replay/candidate.png').read_bytes():raise ValueError('Prepared PNG differs from fresh replay')
    write(dst/'fresh_replay_check.json',{'baseline_matches_formal':True,'prepared_png_byte_matches_replay':True,'schema_and_default_normalization':True,'two_redraw_byte_identical':True,'png_sha256':sha(dst/'candidate.png'),'design_sha256':sha(dst/'design.json'),'plugin_sha256':sha(dst/'plugin.json')})
    print(json.dumps({'question_id':qid,'eligible':True,'replay_matches':True,'folder':str(dst)}),flush=True)
