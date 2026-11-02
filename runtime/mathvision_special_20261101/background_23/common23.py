import os,sys,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
BASE=OUT.parent
sys.dont_write_bytecode=True
for var,sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache'}.items():
    p=OUT/sub;p.mkdir(parents=True,exist_ok=True);os.environ[var]=str(p)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(OUT/'render_tmp')
# Narrow the shared guard to this unit, including child-process imports.
def _guard(event,args):
    if event=='open':
        if not args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):return
        paths=[args[0]]
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):paths=[args[0]]
    elif event in ('os.rename','os.replace','os.link','os.symlink'):paths=args[:2]
    else:return
    for p in paths:
        if isinstance(p,int) or p is None:continue
        if not Path(os.fsdecode(p)).resolve().is_relative_to(OUT):raise PermissionError('background_23 own-root write guard: '+str(p))
sys.addaudithook(_guard)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def rows(p):return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []
def eligibility(qid):
    from dataset_tools import catalog
    branch='PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry'
    b=ROOT/branch;r=next(r for r in rows(b/'dataset.jsonl') if r['id']==qid)
    a=read(ROOT/'provenance/approvals.json')['approvals'][qid]
    notes,_=catalog._source_notes_snapshot(ROOT)
    current=catalog.digest(catalog.content(ROOT,branch,r,source_notes=notes))
    accepted=[x for x in rows(b/'special_variant/accepted_index.jsonl') if x['question_id']==qid]
    collected=[x for x in rows(b/'special_variant/collected_index.jsonl') if x['question_id']==qid]
    d=b/'special_variant'/qid
    recipes=read(d/'recipes.json') if (d/'recipes.json').exists() else None
    collection=read(d/'collection.json') if (d/'collection.json').exists() else None
    entries=(recipes if isinstance(recipes,list) else recipes.get('recipes',recipes.get('variants',[]))) if recipes else []
    if isinstance(entries,dict):entries=list(entries.values())
    passed=any(x.get('status')=='passed' for x in accepted) or any(x.get('status')=='passed' or x.get('reviewed_at') for x in entries)
    cur=collection.get('current',{}) if collection else {}
    completed=any(x.get('status')=='collected' for x in collected) or bool(cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'))
    valid=a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and current==a['content_sha256']
    files={str((b/r[k]).relative_to(ROOT)):sha(b/r[k]) for k in ['image','scene','script','original_image'] if r.get(k)}
    files.update({str((b/p).relative_to(ROOT)):sha(b/p) for p in r.get('runtime_dependencies',[])})
    return {'question_id':qid,'branch':branch,'formal_record':r,'source_dataset':r['source_dataset'],'original_approval':a,'current_content_sha256':current,'approval_matches_current':bool(valid),'accepted_entries':accepted,'collected_entries':collected,'recipes':recipes,'collection':collection,'has_passed':passed,'collected_or_special_completed':completed,'eligible':r['source_dataset']=='MathVision' and bool(valid) and not passed and not completed,'frozen_source_files':files}
def history(qid):
    a=read(BASE/'background_23_assignment.json')
    q=next(q for q in a['questions'] if q['question_id']==qid)
    paths=[]
    for item in q['previous_completed_attempts']:
        d=BASE/item['candidate']
        files=[]
        for p in d.rglob('*'):
            if p.is_file() and p.suffix in ('.json','.txt','.png','.bin'):
                files.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size})
        paths.append({'candidate':item['candidate'],'files':files})
    write(OUT/qid/'prior_history_manifest.json',{'question_id':qid,'prior_attempts':paths,'independent_review_files':q['prior_independent_review_files']})
    return q
if __name__=='__main__':
    qid=sys.argv[1];q=history(qid)
    e=eligibility(qid);write(OUT/qid/'eligibility_start.json',e)
    print(json.dumps({'eligibility':{k:e[k] for k in ['question_id','eligible','approval_matches_current','has_passed','collected_or_special_completed']}},ensure_ascii=False))
    for item in q['previous_completed_attempts']:
        if len(sys.argv)>2 and sys.argv[2] not in item['candidate']:continue
        d=BASE/item['candidate'];print('\nPRIOR '+item['candidate'])
        for p in sorted(d.rglob('*.json')):
            if p.name in ('design.json','plugin.json','primary_review.json','primary_semantics_hold.json','review.json','primary_post_test_review.json','manual_final_review.json') or p.name.endswith('_response.json'):
                print(str(p.relative_to(BASE))+'\n'+json.dumps(read(p),ensure_ascii=False,separators=(',',':')))
    if len(sys.argv)==2 or sys.argv[2]=='reviews':
        for p in q['prior_independent_review_files']:print(p+'\n'+json.dumps(read(BASE/p),ensure_ascii=False,separators=(',',':')))
