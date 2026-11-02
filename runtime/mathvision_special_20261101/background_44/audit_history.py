import task_env
from task_env import OWN, PROJECT, BASE
from inspect_sources import read, save, sha, QIDS
from pathlib import Path
import json

def nodes(v,qid):
    if isinstance(v,dict):
        if v.get('question_id',v.get('id'))==qid:
            yield v
        else:
            for k,x in v.items():
                if k==qid: yield {qid:x}
                else: yield from nodes(x,qid)
    elif isinstance(v,list):
        for x in v: yield from nodes(x,qid)

audits={}
for qid in QIDS:
    inv=read(OWN/qid/'old_file_inventory.json')
    history=[];malformed=[];responses=[]
    for it in inv:
        p=Path(it['path'])
        if p.suffix=='.json':
            try:
                val=read(p)
                if p.name.endswith('_response.json'):
                    responses.append({'path':str(p),'sha256':sha(p),'raw':val})
            except Exception as e:
                malformed.append({**it,'error':str(e),'preserved_verbatim':True,'not_repaired':True})
    roots={next(p for p in Path(it['path']).parents if p.parent==BASE) for it in inv}
    for root in sorted(roots):
        for p in sorted(root.glob('*.json')):
            try:
                v=read(p); extract=list(nodes(v,qid))
                mentions=qid in p.read_text(encoding='utf-8-sig')
                if extract or mentions:
                    history.append({'path':str(p),'sha256':sha(p),'question_nodes':extract,
                                    'question_mentioned_elsewhere':mentions})
            except Exception as e:
                malformed.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'error':str(e),'preserved_verbatim':True,'not_repaired':True})
    audits[qid]={'all_question_subtree_JSON_bytes_read':True,'old_file_inventory':inv,
                 'initial_checkpoint_and_root_history':history,'complete_raw_responses':responses,
                 'malformed_old_files':malformed,'old_pending_status_not_used_as_call_count':True}
    save(OWN/qid/'old_history_audit.json',audits[qid])
    print(qid,'history_roots',[p.name for p in sorted(roots)],'root_records',len(history),'raws',len(responses),'malformed',len(malformed))
    for h in history:
        for n in h['question_nodes']:
            print(json.dumps(n,ensure_ascii=False,separators=(',',':'))[:6000])
save(OWN/'old_history_audit.json',audits)

refs=[]
for i in range(1,13):
    root=BASE/f'batch_{i:02d}'
    manifest=root/'manifest.json'
    if not manifest.exists():continue
    v=read(manifest)
    designs=[]
    for p in root.rglob('*design*.json'):
        try:
            d=read(p)
            designs.append({'path':str(p),'sha256':sha(p),'question_id':d.get('question_id'),
                            'roles':{k:d[k] for k in ['mechanism','hypothesis','design_reason','marker_roles'] if k in d}})
        except Exception as e:designs.append({'path':str(p),'sha256':sha(p),'error':str(e)})
    refs.append({'batch':root.name,'manifest_sha256':sha(manifest),'designs':designs})
save(OWN/'delivered_reference_study.json',refs)
for r in refs:
    print('REFERENCE',r['batch'],json.dumps(r['designs'][:2],ensure_ascii=False,separators=(',',':'))[:2200])
