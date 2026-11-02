from review_bootstrap import *
d=read(OWN/'documents_history_audit.json')
refs={}
for p,obj in d['reference_lessons'].items():
    refs[p]={k:v for k,v in obj.items() if k in ['question_id','variant_id','decision','summary','decision_rationale','limitations','nonblocking_limitations','blocking_reason','blocking_objections','scope','concrete_objections']}
old=read(TASK/'background_20/checkpoint.json')
current=read(TASK/'background_41/checkpoint.json')
queue=read(TASK/'background_41/second_review_queue.json')
def shrink(o):
    if isinstance(o,dict):return {k:shrink(v) for k,v in o.items() if k not in ['full_assistant_content','frozen_content','formal_record','all_original_frozen_inputs','files','complete_raw_manual_finals','results','per_marker_roles','evidence_paths','prior_files']}
    if isinstance(o,list):return [shrink(v) for v in o]
    return o
source=read(OWN/'eligibility_current.json')['original_content']['source_notes']
print(json.dumps({'source_notes':source,'documents_read':d['read_receipts'],
 'background20_full_checkpoint_candidates':[{'question_id':o.get('question_id'),'candidate_id':o.get('candidate_id'),'expected_wrong_answer':o.get('expected_wrong_answer'),'manual_final_answers':o.get('manual_final_answers'),'status':o.get('status')} for o in old['candidates']],
 'background20_global_counts':old['counts'],'background41_all_global_fields':{k:v for k,v in current.items() if k not in ['cases','new_vs_old_audits']},
 'Plane427_refinement_full':read(CAND.parent/'refinement_result.json'),'Plane427_queue_entry':shrink(d['background41']['second_review_queue.json']),
 'reference_semantics':refs,'historical_hash_summary':{k:{a:b for a,b in v.items() if a not in ['matches','unresolved_keys']} for k,v in d['historical_hash_checks'].items()}},ensure_ascii=False,indent=2))
