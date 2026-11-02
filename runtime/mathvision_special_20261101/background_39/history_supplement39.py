from tools39 import *
import re
pattern=re.compile(r'\b(?:'+'|'.join(ASSIGNED)+r')\b')
helpers=[];files=[];focused=[];errors=[]
for p in BASE.rglob('*.py'):
    if p.is_relative_to(HERE):continue
    s=p.read_text(encoding='utf-8-sig')
    if pattern.search(s):helpers.append({'path':str(p),'sha256':file_hash(p),'full_read':True,'relevant_lines':[x for x in s.splitlines() if pattern.search(x)]})
counts={}
for q in ASSIGNED:
    cnt=0
    for folder in BASE.rglob(q):
        if not folder.is_dir() or folder.is_relative_to(HERE):continue
        for p in folder.rglob('*.json'):
            raw=p.read_text(encoding='utf-8-sig');item={'path':str(p),'sha256':file_hash(p),'full_raw_read':True}
            try:d=json.loads(raw);item['parsed_in_full']=True
            except json.JSONDecodeError as err:
                errors.append({'path':str(p),'sha256':file_hash(p),'error':str(err),'raw_preserved_in_place':True,'raw_text':raw});item['parsed_in_full']=False;d={}
            files.append(item);cnt+=1
            if isinstance(d,dict) and any(s in p.name for s in ('prescreen','review','assessment')):
                focused.append({'question_id':q,'path':str(p),'content':{k:v for k,v in d.items() if k in ('reason','specific_reason','prescreen_reason','mathematical_solution','mathematical_context','math_context','decision','status','notes')}})
    counts[q]=cnt
write(HERE/'history_supplement_read_audit.json',{'created_at':now(),'old_question_JSON_raw_read':files,'file_count_per_question':counts,'root_and_shared_helper_records':helpers,'focused_historical_objections':focused,'historical_malformed_JSON':errors,'local_audit_exception':'Earlier read-only broad JSON scan raised JSONDecodeError on an existing malformed historical file; no API action was involved. This robust reader preserves raw bytes and records rather than repairs it.','historical_raw_final_read':'Plane276 D60/D60 against E72 remains MISS; no other matching old completed candidate bindings found.'})
print('Read old JSON counts',counts,'helpers',len(helpers),'historical malformed files',len(errors));print(json.dumps(errors,ensure_ascii=False));print(json.dumps(focused,ensure_ascii=False))
