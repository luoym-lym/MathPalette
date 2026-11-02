import env
from env import OWN, PROJECT, SHARED
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from dataset_tools import catalog

IDS = ['Plane400','Plane401','Plane402','Plane405','Plane407','Plane409','Plane410','Plane412']
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8')
def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def eligibility(qid):
    branch = PROJECT/'PlaneGeometry'
    record = next(r for r in catalog.rows(branch/'dataset.jsonl') if r['id']==qid)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    current = catalog.content(PROJECT,'PlaneGeometry',record)
    indexes={}
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p=branch/'special_variant'/name
        indexes[name]={'sha256':sha(p) if p.exists() else None,'matching_records':[]}
        if p.exists():
            indexes[name]['matching_records']=[r for r in catalog.rows(p) if r.get('question_id',r.get('id'))==qid]
    folder=branch/'special_variant'/qid
    state={name:read(folder/name) for name in ['collection.json','recipes.json'] if (folder/name).is_file()}
    eligible=(record['source_dataset']=='MathVision' and approval.get('reviewer')=='user' and bool(approval.get('instruction')) and bool(approval.get('approved_at_utc')) and catalog.digest(current)==approval['content_sha256'] and not any(i['matching_records'] for i in indexes.values()) and not state)
    return {'at_utc':datetime.now(timezone.utc).isoformat(),'question_id':qid,'current_formal_record':record,'approval':approval,'computed_approval_content_sha256':catalog.digest(current),'approval_matches':catalog.digest(current)==approval['content_sha256'],'special_indexes':indexes,'per_question_special_files':state,'eligible':eligible,'source_files':current['files']}

def setup():
    dump(OWN/'isolation.json',{'strict_own_write_guard':True,**env.ISOLATION,'environment':{v:__import__('os').environ[v] for v in ['TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME']}})
    # Preserve exact API implementation; only relocate project discovery and isolate writes.
    source=SHARED/'harness/quicktest3_isolated.py'
    text=source.read_text(encoding='utf-8')
    old='PROJECT = Path(__file__).resolve().parents[3]'
    assert text.count(old)==1
    text=text.replace(old,'sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nimport env\nPROJECT = env.PROJECT')
    target=OWN/'harness/quicktest3_isolated.py'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text,encoding='utf-8')
    dump(OWN/'harness_isolation.json',{'source':str(source),'source_sha256':sha(source),'copy':str(target),'copy_sha256':sha(target),'only_change':'project-root discovery replaced with own env import before project imports; harness cache paths naturally inside own copy; API/model/systemprompt/timeout/limits unchanged'})
    adapter,config=env.renderer()
    protected={}
    history=[]
    for qid in IDS:
        root=OWN/qid
        e=eligibility(qid); dump(root/'eligibility_start.json',e)
        assert e['eligible'], qid
        context=adapter.inspect_question(qid)
        dump(root/'context.json',context)
        dump(root/'formal_record.json',e['current_formal_record'])
        scene=adapter.scene(qid)
        try:
            from dataset_tools.mathvision_workbench import png_bytes
            data=png_bytes(scene)
            (root/'noop.png').write_bytes(data)
        finally: scene.close()
        for relative,h in e['source_files'].items():
            p=(PROJECT/'PlaneGeometry'/relative).resolve()
            protected[str(p)]=h
        oldfiles=[]
        for p in SHARED.rglob('*'):
            if not p.is_file() or p.is_relative_to(OWN): continue
            if qid in p.parts or qid in p.name:
                if p.suffix in ['.json','.jsonl','.png','.jpg','.bin','.txt','.py']:
                    oldfiles.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
                    protected[str(p)]=sha(p)
        dump(root/'history_files.json',oldfiles)
        history.append({'id':qid,'old_file_count':len(oldfiles),'current_eligible':True,'approval_match':True,'context_objects':len(context['objects'])})
    for p in [PROJECT/'provenance/approvals.json',PROJECT/'PlaneGeometry/dataset.jsonl',PROJECT/'PlaneGeometry/workbench/mathvision_adapter.py',PROJECT/'PlaneGeometry/workbench/mathvision_plugins.py',SHARED/'refinement_dispatch_20261102.json',SHARED/'background_43_assignment.json',SHARED/'background_43_brief.txt']:
        protected[str(p)]=sha(p)
    dump(OWN/'protected_inputs_start.json',protected)
    dump(OWN/'preparation_summary.json',history)
    print(json.dumps(history))

if __name__=='__main__': setup()
