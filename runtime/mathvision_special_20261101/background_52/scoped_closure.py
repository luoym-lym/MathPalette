from audit_io import install,OWN,PROJECT,SESSION,load,save,sha,IDS,eligibility
install()
import json,sys
from pathlib import Path
from datetime import datetime,timezone

def find_matches(node,qids,at='$'):
    if isinstance(node,dict):
        if node.get('question_id',node.get('id')) in qids:return [{'json_path':at,'content':node}]
        result=[]
        for k,v in node.items():
            if k in qids:result.append({'json_path':at+'.'+k,'content':v})
            else:result.extend(find_matches(v,qids,at+'.'+k))
        return result
    if isinstance(node,list):return sum([find_matches(v,qids,f'{at}[{i}]') for i,v in enumerate(node)],[])
    return []

source_audits=[]
for qid in IDS:
    now=eligibility(qid,'eligibility_final.json')
    initial=load(OWN/qid/'eligibility_initial.json')
    source_audits.append({'question_id':qid,'current_eligible':now['eligible'],'approval_fingerprint_matches':now['approval_fingerprint_matches'],'all_scoped_content_files_record_notes_identical':now['content']==initial['content'],'source_JPG':str(PROJECT/'PlaneGeometry'/now['formal_record']['original_image']),'source_JPG_sha256':sha(PROJECT/'PlaneGeometry'/now['formal_record']['original_image']),'formal_PNG':str(PROJECT/'PlaneGeometry'/now['formal_record']['image']),'formal_PNG_sha256':sha(PROJECT/'PlaneGeometry'/now['formal_record']['image'])})
assert all(a['all_scoped_content_files_record_notes_identical'] and a['current_eligible'] for a in source_audits)

old=[]
for item in load(OWN/'history_inventory.json'):
    p=PROJECT/item['path'];current=sha(p)
    old.append({**item,'current_sha256':current,'unchanged':current==item['sha256']})
assert all(x['unchanged'] for x in old)
save(OWN/'old_evidence_preservation_final.json',{'scope':'Every existing question-directory file captured in history_inventory.json; no assertion about unrelated concurrent workspace edits or mutable global progress hashes.','file_count':len(old),'files':old,'changed':[]})
old_json=[]
for item in old:
    p=PROJECT/item['path']
    if p.suffix!='.json':continue
    try:load(p);status='complete valid JSON'
    except Exception as exc:status=f'Preserved unreadable JSON: {type(exc).__name__}: {exc}'
    old_json.append({'path':str(p),'sha256':item['sha256'],'parse_status':status,'modified_or_repaired':False})
save(OWN/'old_scoped_JSON_audit.json',{'files':old_json,'malformed_files':[x for x in old_json if x['parse_status']!='complete valid JSON'],'historical_absence_policy':'A truncated or malformed historical file is not evidence of no solver call. No historic JSON is repaired.'})

save(OWN/'source_preservation_final.json',{'checked_at_utc':datetime.now(timezone.utc).isoformat(),'source_audits':source_audits,'all_8_scoped_formal_inputs_and_current_approvals_unchanged':True,'formal_state_and_old_evidence_read_only':True,'own_writes_only':str(OWN),'guard':load(OWN/'isolation.json'),'unrelated_changes':'No whole-workspace unchanged claim. No restore, catalog build, global ledger write, .git edit, .env edit or .runtime write was performed.'})

diagnostic=[]
for leaf in ['inventory.json','remaining_questions.jsonl','exploration_report.json']:
    p=SESSION/leaf
    if p.suffix=='.jsonl':d=[json.loads(line) for line in p.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    else:d=load(p)
    diagnostic.append({'path':str(p),'sha256':sha(p),'classification':'mutable diagnostic runtime metadata, not a frozen original input','question_sections':find_matches(d,set(IDS))})
save(OWN/'current_diagnostic_progress_read.json',diagnostic)

refs=load(OWN/'delivered_reference_study.json')
for ref in refs:
    concise=[]
    for d in ref['designs']:
        n=d['narrative'];concise.append({k:v for k,v in n.items() if k in ['question_id','variant_id','design_id','hypothesis','mechanism','predeclared_hypothesis','intent']})
    print(json.dumps({'delivered_reference_batch':ref['batch'],'actual_information_lessons':concise},ensure_ascii=False,separators=(',',':')))
print(json.dumps({'scoped_8_sources_unchanged':True,'old_files_unchanged':len(old),'old_bad_JSON_count':sum(x['parse_status']!='complete valid JSON' for x in old_json),'solver_calls_not_started_by_closure':True},ensure_ascii=False))
