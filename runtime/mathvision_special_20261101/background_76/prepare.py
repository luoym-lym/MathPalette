import bootstrap
from bootstrap import OWNROOT, PROJECT, BASE
import hashlib
import json
from datetime import datetime, timezone
from dataset_tools.catalog import content, digest, read, rows

IDS = ['Solid83','Solid85','Solid121','Solid130','Solid132','Solid151','Solid211','Solid221']
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8')

manifest = []
for name in ['background_76_brief.txt','background_76_assignment.json','background_66_brief.txt','background_66_assignment.json','background_65_brief.txt','background_65_assignment.json','continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','quota_resume74_76_20261102.json','quota_resume67_73_20261102.json','refinement_dispatch_20261102.json','selection65_66_parent_eligibility.json','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json']:
    p = BASE/name
    data=p.read_bytes()
    (OWNROOT/'snapshots'/name).write_bytes(data)
    manifest.append({'source':str(p),'snapshot':str(OWNROOT/'snapshots'/name),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'mutable_parent_metadata': name in ['continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json']})
save(OWNROOT/'audit'/'initial_snapshot_manifest.json',manifest)
assignment=read(BASE/'background_76_assignment.json')
old=read(BASE/'background_66_assignment.json')
equivalence=[]
for q,oq in zip(assignment['questions'],old['questions']):
    equivalence.append({'id':q['question_id'],'76_nested_equals_66_question':q['source_assignment_question']==oq,'formal_record_equals_inherited':q['formal_record']==oq['formal_record_at_assignment']})
save(OWNROOT/'audit'/'assignment_equivalence.json',equivalence)

records={r['id']:r for r in rows(PROJECT/'SolidGeometry/dataset.jsonl')}
approvals=read(PROJECT/'provenance/approvals.json')['approvals']
notes=read(PROJECT/'provenance/source_notes.json')
audits=[]
for q in IDS:
    r=records[q]
    c=content(PROJECT,'SolidGeometry',r,source_notes=notes)
    a=approvals[q]
    special=PROJECT/'SolidGeometry/special_variant'/q
    recipes=read(special/'recipes.json') if (special/'recipes.json').exists() else []
    eligible=r['source_dataset']=='MathVision' and not recipes and not (special/'collection.json').exists() and digest(c)==a['content_sha256'] and a['reviewer']=='user' and bool(a['instruction'])
    obj={'question_id':q,'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':eligible,'formal_record':r,'original_approval':a,'current_content_sha256':digest(c),'content':c,'no_passed_variant':not recipes,'not_collected':not (special/'collection.json').exists(),'no_special_completion':not (special/'collection.json').exists(),'formal_dataset_sha256':sha(PROJECT/'SolidGeometry/dataset.jsonl'),'approvals_file_sha256':sha(PROJECT/'provenance/approvals.json'),'source_notes_file_sha256':sha(PROJECT/'provenance/source_notes.json'),'special_recipes_exists':(special/'recipes.json').exists(),'special_collection_exists':(special/'collection.json').exists()}
    save(OWNROOT/q/'eligibility_start.json',obj)
    audits.append({'id':q,'eligible':eligible,'approval_fingerprint_match':digest(c)==a['content_sha256'],'question':r['question'],'answer':r['answer']})
save(OWNROOT/'audit'/'eligibility_summary.json',audits)
save(OWNROOT/'checkpoint.json',{'unit':'background_76','stage':'material_refinement','status':'initial_reading','question_ids':IDS,'assessed_question_ids':[],'unworked_question_ids':IDS,'actual_api_calls':0,'owned_live_requests':0,'errors':[],'eligibility_audit':'audit/eligibility_summary.json'})
save(OWNROOT/'second_review_queue.json',{'unit':'background_76','candidates':[],'independent_review_by_parent_required':True})
print(json.dumps({'assignment_equivalence':equivalence,'eligibility':audits},ensure_ascii=False))
