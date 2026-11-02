"""Low-memory reporting: stdlib only, own-root guard before any project import."""
import os,sys,json,hashlib
from pathlib import Path
OWN=Path(__file__).resolve().parent
PROJECT=OWN.parents[2]
SESSION=OWN.parent
IDS=['Plane480','Plane481','Plane482','Plane483','Plane484','Plane488','Plane489','Plane490']
def install():
    sys.dont_write_bytecode=True
    for key,leaf in [('TEMP','tmp'),('TMP','tmp'),('MPLCONFIGDIR','mpl'),('XDG_CACHE_HOME','cache')]:
        p=OWN/leaf;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
    def check(path):
        if path is None or isinstance(path,int):return
        p=Path(os.fsdecode(path)).resolve()
        if not p.is_relative_to(OWN):raise PermissionError('Own-root write guard: '+str(p))
    def guard(event,args):
        if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
        elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
        elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
    sys.addaudithook(guard)
    return {'strict_own_root':str(OWN),'renderer_imported':False,'purpose':'stdlib evidence/checkpoint reporting after host OpenBLAS memory failure; no drawing or API calls'}
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def eligibility(qid,leaf='eligibility_final.json'):
    from datetime import datetime,timezone
    branch=PROJECT/'PlaneGeometry';row=next(json.loads(line) for line in (branch/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip() and json.loads(line)['id']==qid)
    initial=load(OWN/qid/'eligibility_initial.json')
    files={p:sha(branch/p) for p in initial['content']['files']}
    notes=load(PROJECT/'provenance/source_notes.json').get(qid,{})
    content={'branch':'PlaneGeometry','record':row,'files':files,'source_notes':notes}
    approval=load(PROJECT/'provenance/approvals.json')['approvals'][qid]
    def rows(p):return [json.loads(line) for line in p.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    special=branch/'special_variant'
    accepted=[r for r in rows(special/'accepted_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collected=[r for r in rows(special/'collected_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    cp=special/qid/'collection.json';collection=load(cp) if cp.exists() else None
    fp=digest(content)
    eligible=row['source_dataset']=='MathVision' and approval['reviewer']=='user' and bool(approval['instruction']) and fp==approval['content_sha256'] and not accepted and not collected and not collection
    result={'question_id':qid,'checked_at_utc':datetime.now(timezone.utc).isoformat(),'formal_record':row,'formal_record_sha256':digest(row),'original_approval':approval,'content':content,'current_content_sha256':fp,'approval_fingerprint_matches':fp==approval['content_sha256'],'accepted_records':accepted,'collected_records':collected,'collection':collection,'eligible':bool(eligible),'audit_implementation':'same catalog.content/digest construction, stdlib only; no renderer or API import'}
    assert result['eligible']
    save(OWN/qid/leaf,result)
    return result
