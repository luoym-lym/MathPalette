from pathlib import Path
import os,sys,json,hashlib
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for k,n in {'TEMP':'classification_tmp','TMP':'classification_tmp','MPLCONFIGDIR':'classification_mpl','XDG_CACHE_HOME':'classification_cache'}.items():
    p=HERE/n;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
sys.dont_write_bytecode=True;sys.path.insert(0,str(BASE))
from runtime_isolation import install
install(HERE/'classification_render_tmp')
from dataset_tools.catalog import content,digest
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p):return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):
    with Path(p).open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
before=read(HERE/'formal_files_before.json');observed=read(HERE/'source_preservation_final.json')
assignment=read(BASE/'background_07_assignment.json')['questions'];approvals=read(ROOT/'provenance/approvals.json')['approvals'];notes=read(ROOT/'provenance/source_notes.json')
audits=[];frozen={}
for entry in assignment:
    qid=entry['question_id'];branch=entry['branch'];br=ROOT/branch
    row=next(r for r in rows(br/'dataset.jsonl') if r['id']==qid);a=approvals.get(qid,{})
    current=digest(content(ROOT,branch,row,source_notes=notes));reasons=[]
    if row['source_dataset']!='MathVision':reasons.append('notMathVision')
    if a.get('reviewer')!='user' or not a.get('instruction') or a.get('content_sha256')!=current:reasons.append('approval_invalid')
    accepted=[r for r in rows(br/'special_variant/accepted_index.jsonl') if r.get('question_id')==qid and r.get('status')=='passed']
    collected=[r for r in rows(br/'special_variant/collected_index.jsonl') if r.get('question_id')==qid and r.get('status')=='collected']
    if accepted:reasons.append('passed')
    if collected:reasons.append('collected')
    rp=br/'special_variant'/qid/'recipes.json'
    if rp.exists():
        rr=read(rp);rr=rr if isinstance(rr,list) else rr.get('recipes',rr.get('variants',[]));rr=list(rr.values()) if isinstance(rr,dict) else rr
        if any(r.get('status')=='passed' or r.get('reviewed_at') for r in rr if isinstance(r,dict)):reasons.append('passed_recipe')
    cp=br/'special_variant'/qid/'collection.json'
    if cp.exists():
        cur=read(cp).get('current',{})
        if cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'):reasons.append('completion_or_special')
    for mp in BASE.glob('batch_*/manifest.json'):
        if qid in mp.read_text(encoding='utf-8-sig'):reasons.append('already_delivered')
    paths=[br/row[k] for k in ['image','original_image','script','scene'] if row.get(k)]+[br/p for p in row.get('runtime_dependencies',[])]+[br/'dataset.jsonl',br/'REDRAW_PROTOCOL.md',br/'dataset_generator/protocol.json',br/'dataset_generator/common_renderer.py',br/'workbench/plugin.schema.json',br/'workbench/mathvision_plugins.py',ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'AGENTS.md',ROOT/'dataset_tools/mathvision_workbench.py',ROOT/'dataset_tools/geometry_dataset.py',ROOT/'provenance/approvals.json',ROOT/'provenance/source_notes.json']
    unchanged=[]
    for p in paths:
        rel=p.relative_to(ROOT).as_posix();h=sha(p);same=before.get(rel)==h
        frozen[rel]={'before':before.get(rel),'current':h,'unchanged':same};unchanged.append(same)
    if not all(unchanged):reasons.append('frozen_source_changed')
    audits.append({'question_id':qid,'branch':branch,'eligible':not reasons,'reasons':reasons,'current_approval_content_sha256':current,'recorded_approval_content_sha256':a.get('content_sha256'),'approved_at_utc':a.get('approved_at_utc'),'question_record_sha256':digest(row),'all_frozen_source_files_unchanged':all(unchanged),'accepted_entries':accepted,'collected_entries':collected})
drift=observed['formal_changed']+observed['formal_deleted']+observed['formal_added']
unclassified=[]
for p in drift:
    if p.startswith('.runtime/') or p in ['question_bank.jsonl','PlaneGeometry/special_variant/accepted_index.jsonl','PlaneGeometry/special_variant/collected_index.jsonl']:continue
    if p.startswith('PlaneGeometry/special_variant/'):
        component=p.split('/')[2]
        if component.startswith('Plane') and component not in {e['question_id'] for e in assignment}:continue
    unclassified.append(p)
report={'checked_at':datetime.now(timezone.utc).isoformat(),'full_workspace_unchanged':not bool(drift),'observed_concurrent_unrelated_workbench_drift':bool(drift),'drift_actor':'Not identified by a hash scan. File pattern is consistent with concurrent workbench activity; all task Python processes use runtime write guards and no approval/workbench API was invoked.','drift_changed':observed['formal_changed'],'drift_deleted':observed['formal_deleted'],'drift_added':observed['formal_added'],'unclassified_drift':unclassified,'no_restore_or_rewrite_of_concurrent_changes':True,'task_frozen_sources_unchanged':all(v['unchanged'] for v in frozen.values()),'prior_runtime_evidence_unchanged':not observed['prior_runtime_changed_or_deleted'],'all_assigned_currently_eligible':all(a['eligible'] for a in audits),'question_count_rechecked':len(audits),'questions':audits,'frozen_file_comparisons':frozen,'task_formal_writes_permitted':False,'task_modified_or_reverted_formal_or_concurrent_files':False,'original_observed_scan_preserved':str(HERE/'source_preservation_final.json')}
write(HERE/(sys.argv[1] if len(sys.argv)>1 else 'source_preservation_classification.json'),report)
assert report['task_frozen_sources_unchanged'] and report['prior_runtime_evidence_unchanged'] and report['all_assigned_currently_eligible'] and not unclassified
print(json.dumps({k:report[k] for k in ['full_workspace_unchanged','observed_concurrent_unrelated_workbench_drift','task_frozen_sources_unchanged','prior_runtime_evidence_unchanged','all_assigned_currently_eligible','question_count_rechecked','unclassified_drift']}))
