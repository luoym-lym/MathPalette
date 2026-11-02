from review_bootstrap import *
import re

receipts=[]
def load(p):
    obj=read(p)
    receipts.append({'path':str(p),'sha256':sha(p),'fully_decoded':True,'top_level_keys':list(obj) if isinstance(obj,dict) else None})
    return obj

def pertinent(obj):
    if isinstance(obj,dict):
        if obj.get('question_id',obj.get('id'))=='Plane427': return obj
        out={}
        for key,value in obj.items():
            if key=='Plane427': out[key]=value
            elif isinstance(value,(list,dict)):
                filtered=pertinent(value)
                if filtered not in ({},[],None):out[key]=filtered
            elif isinstance(value,str) and ('Plane427' in value or key in ['status','unit','created_at','created_at_utc','stop_reason']):out[key]=value
        return out
    if isinstance(obj,list):
        return [part for item in obj if (part:=pertinent(item)) not in ({},[],None)]
    return obj if isinstance(obj,str) and 'Plane427' in obj else None

candidate_docs={}
for p in sorted(CAND.glob('*.json')):
    obj=load(p)
    if p.name.startswith('eligibility_'):
        candidate_docs[p.name]={k:v for k,v in obj.items() if k not in ['formal_record','frozen_content']}
    elif p.name=='render_check.json':
        candidate_docs[p.name]={k:v for k,v in obj.items() if k!='all_original_frozen_inputs'}
    else: candidate_docs[p.name]=obj
write('candidate_documents_full_read_receipts.json',receipts)

background={}
for name in ['checkpoint.json','second_review_queue.json','source_preservation_audit.json','no_live_api_processes.json','old_manual_final_review.json','delivered_reference_mechanisms.json']:
    p=TASK/'background_41'/name
    obj=load(p)
    background[name]={'all_top_level_keys':list(obj) if isinstance(obj,dict) else None,'Plane427_relevant':pertinent(obj),
                      'global_scalars':{k:v for k,v in obj.items() if not isinstance(v,(dict,list))} if isinstance(obj,dict) else None}
    if name in ['source_preservation_audit.json','no_live_api_processes.json','old_manual_final_review.json']:background[name]['full']=obj

old={}
for p in sorted((TASK/'background_20/Plane427').glob('*.json')):
    obj=load(p)
    if p.name=='input_fingerprints.json':old[p.name]={'entry_count':len(obj),'structure':list(obj)[:5] if isinstance(obj,dict) else None}
    elif p.name=='context.json':old[p.name]={'equals_current_background41_context':obj==read(CAND.parent/'context.json')}
    else:old[p.name]=obj
for p in sorted((TASK/'background_20').glob('*.json')):
    obj=load(p)
    old['root/'+p.name]={'all_top_level_keys':list(obj) if isinstance(obj,dict) else None,'Plane427_relevant':pertinent(obj)}
    if p.name=='checkpoint.json':old['root/'+p.name]['counts']=obj.get('counts')
old['root/report.txt']=(TASK/'background_20/report.txt').read_text(encoding='utf-8-sig')
old['exact_Plane427_tree_files']=[str(p.relative_to(TASK)) for p in sorted((TASK/'background_20/Plane427').rglob('*')) if p.is_file()]

references={}
ref_paths=[TASK/'annotation_semantics_lesson_plane242_r24_20261102.json',TASK/'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json',TASK/'batch_13/manifest.json']
for directory in (TASK/'independent_review').iterdir():
    if directory.is_dir() and any(x in directory.name for x in ['Solid128','Solid197','Plane192','Plane233']):
        p=directory/'independent_review.json'
        if p.is_file():ref_paths.append(p)
for p in ref_paths:
    obj=load(p)
    if 'Plane242' in str(p) or p.name.startswith('annotation_'):
        references[str(p)]={k:v for k,v in obj.items() if any(x in k.lower() for x in ['decision','reason','objection','limitation','correction','semantic','summary'])}
    elif p.parent.name=='batch_13':
        references[str(p)]={'top_level_keys':list(obj),'counts':obj.get('counts'),'Plane427_relevant':pertinent(obj)}
    else:
        references[str(p)]={k:v for k,v in obj.items() if k in ['question_id','variant_id','decision','summary','decision_rationale','limitations','nonblocking_limitations','concrete_objections','blocking_objections']}

hash_checks={}
for p in [CAND.parent/'adapter_input_hashes.json',TASK/'background_41/source_hashes_before.json',TASK/'background_20/Plane427/input_fingerprints.json']:
    obj=load(p)
    # Adapter entries are native stable keys and are checked by the freshly built adapter.
    if 'files' in obj:hash_checks[str(p)]={'files_count':len(obj['files']),'environment':obj.get('environment'),'fingerprint':obj.get('fingerprint'),'checked_against_fresh_adapter_in':'native_render_audit.json'}
    else:
        matches=[];misses=[];unresolved=[]
        for name,expected in obj.items():
            if not isinstance(expected,str) or not re.fullmatch('[0-9a-f]{64}',expected):
                unresolved.append(name);continue
            actual_path=Path(name)
            if not actual_path.is_absolute():actual_path=PROJECT/name
            if actual_path.is_file():
                actual=sha(actual_path)
                (matches if actual==expected else misses).append({'path':str(actual_path),'recorded':expected,'actual':actual})
            else:unresolved.append(name)
        hash_checks[str(p)]={'matches_count':len(matches),'mismatches':misses,'unresolved_keys':unresolved,'matches':matches}

write('documents_history_audit.json',{'read_receipts':receipts,'candidate_documents':candidate_docs,'background41':background,'background20_complete_relevant_history':old,'reference_lessons':references,'historical_hash_checks':hash_checks})
print(json.dumps({'background41':background,'background20_complete_relevant_history':old,'reference_lessons':references,
                  'candidate_render_check':candidate_docs.get('render_check.json'),
                  'read_receipts_count':len(receipts),'historical_hash_check_summary':{k:{a:b for a,b in v.items() if a!='matches'} for k,v in hash_checks.items()}},ensure_ascii=False,indent=2))
