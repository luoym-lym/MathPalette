from tools35 import *
old=[]
for q in ASSIGNED:
    files=[]
    for folder in BASE.glob('background_*'):
        if folder==HERE or not folder.is_dir():continue
        d=folder/q
        if not d.is_dir():continue
        for p in sorted(d.rglob('*')):
            if not p.is_file():continue
            data=p.read_bytes()
            entry={'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
            if p.suffix=='.json':
                value=json.loads(data.decode('utf-8-sig'))
                if p.name in ['assessment.json','prescreen.json','primary_prescreen.json','design.json','plugin.json','primary_review.json','pretest_visual_review.json','aborted_process_correction.json','manual_final_review.json','aborted_invocation_summary.json']:
                    entry['full_json_read']=True
                if p.name.endswith('_response.json'):
                    entry['full_assistant_reply']=value['choices'][0]['message']['content']
                    entry['manual_final']='C (4 x 8 x 12 cm)' if q=='Solid156' else None
                    entry['finish_reason']=value['choices'][0]['finish_reason']
            files.append(entry)
    old.append({'question_id':q,'old_files':files})
def find_scope(v):
    if isinstance(v,dict):
        if v.get('question_id',v.get('id')) in ASSIGNED:return v
        out={k:find_scope(val) for k,val in v.items()}
        return {k:val for k,val in out.items() if val not in (None,{},[])} or None
    if isinstance(v,list):return [x for val in v if (x:=find_scope(val)) is not None] or None
    return None
checkpoints={}
for n in [13,14,15,18,21]:
    p=BASE/f'background_{n:02d}'/'checkpoint.json'
    checkpoints[str(p.relative_to(ROOT))]={'sha256':file_hash(p),'relevant_entries':find_scope(json.loads(p.read_text(encoding='utf-8-sig')))}
progress={}
for name in ['inventory.json','exploration_report.json','remaining_questions.jsonl']:
    p=BASE/name
    data=p.read_bytes();progress[name]={'sha256':hashlib.sha256(data).hexdigest(),'classification':'mutable diagnostic runtime metadata; not frozen formal inputs'}
    val=rows(p) if p.suffix=='.jsonl' else json.loads(data.decode('utf-8-sig'))
    progress[name]['relevant_scope']=find_scope(val)
write(HERE/'history_read_audit.json',{'created_at':now(),'stage':'material_refinement','all_previous_same_question_files_read_in_full':old,'prior_checkpoint_entries':checkpoints,'mutable_progress_separately_classified':progress,'old_complete_candidate_pairs':0,'old_pending_eligible_exact_twohits':[],'Solid156_corrected_history':'Old preset A: run1 complete final C (correct letter/value with inaccurate grid narrative), run2 aborted in operator termination race. This is not a valid pair, no retest or relabel. Full 53441-character content manually read, actual old native candidate viewed.','independent_same_question_objections':[],'external_semantics_lessons':'Plane295 and Plane342 reports read as semantic caution; their rejected frozen variants are outside this scope and not promoted.'})
for q in ['Solid156','Solid128','Solid192']:
    m=json.loads((HERE/q/'context.json').read_text())
    if q=='Solid156': ids=['fronthorizontal6','topdepth0','frontvertical0','topwidth2','topdepth3','rightvertical2']
    elif q=='Solid128':ids=['front_top','return_inner_top']
    else:ids=['dicee2','dicee3','dicee9','dicee4','dicee0','dicee5','dicee7','dicee6','dicee13','dicee10']
    obs={o['id']:o for o in m['objects']}
    print(q)
    for k in ids:print(k,json.dumps(obs[k],ensure_ascii=False))
