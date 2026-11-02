from audit import *
from datetime import datetime, timezone
from dataset_tools.catalog import content, digest, validate_formal_row

def rows(p):
    return [json.loads(line) for line in p.read_text(encoding='utf-8-sig').splitlines() if line.strip()] if p.exists() else []

row=next(r for r in rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']=='Plane391')
approval=read(ROOT/'provenance/approvals.json')['approvals']['Plane391']
validate_formal_row(ROOT,'PlaneGeometry',row)
now_digest=digest(content(ROOT,'PlaneGeometry',row))
records={}
for name in ['accepted_index.jsonl','collected_index.jsonl']:
    records[name]=[r for r in rows(ROOT/'PlaneGeometry/special_variant'/name) if r.get('question_id',r.get('id'))=='Plane391']
for name in ['recipes.json','collection.json']:
    p=ROOT/'PlaneGeometry/special_variant/Plane391'/name
    records[name]=read(p) if p.exists() else None
checks={
    'formal_MathVision':row['source_dataset']=='MathVision',
    'record_still_equals_frozen_record':row==read(BASE/'formal_record.json'),
    'user_approval_current':now_digest==approval['content_sha256'] and approval['reviewer']=='user' and bool(approval['instruction']),
    'no_Pass_not_collected_no_special_completion':not any(records.values()),
    'no_delivered_manifest_membership':not any('Plane391' in p.read_text(encoding='utf-8-sig') for p in (ROOT/'runtime/mathvision_special_20261101').glob('batch_*/manifest.json')),
}
initial=read(OUT/'read_only_start_hashes.json')
changed=[]
for name,old in initial.items():
    path=ROOT/name
    actual=sha(path) if path.exists() else None
    if actual!=old:changed.append({'path':name,'start_sha256':old,'current_sha256':actual})
checks['existing_Plane391_evidence_and_relevant_source_files_unchanged']=not changed
process=read(OUT/'final_process_check.json')
checks['process_check_clear']=process['no_live_own_review_or_Plane391_solver_processes']
end={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'current_original_content_sha256':now_digest,'current_original_approval':approval,'current_Plane391_authoritative_records':records,'changed_original_evidence_or_relevant_source_files':changed,'process_check':process,'current_checker_is_a_synchronous_command_and_exits_before_handback':True}
dump('final_authoritative_recheck.json',end)
assert all(checks.values()), end
report=read(OUT/'independent_review.json')
report['current_authoritative_eligibility']['final_recheck']=end
report['isolation_and_state_preservation']['final_process_check']=process
report['isolation_and_state_preservation']['final_existing_evidence_and_relevant_sources_recheck_unchanged']=not changed
report['supporting_independent_artifacts'].update({'final_process_check.json':rel(OUT/'final_process_check.json'),'final_authoritative_recheck.json':rel(OUT/'final_authoritative_recheck.json')})
report['concrete_objections_and_limitations'].append({'id':'unselected_black_raster_rounding','severity':'nonblocking rendering detail','finding':'Independent pixel audit found256 changed pixels beyond the colored intervals on retained black outlines, including255 away from the large-triangle hypotenuse endpoints. Every one is an achromatic RGB channel difference of exactly1, and all image differences lie within1.919px of existing original edges. The source diagonal interior is pixel-identical.','impact_and_resolution':'The actual partial-style executor reconstructs retained black path portions and produces tiny antialias rounding changes. The report does not claim all off-interval pixels are identical. Original geometry, line locations, fills and human readability are preserved; native exact-candidate replay is byte-identical.'})
dump('independent_review.json',report)
verified=read(OUT/'independent_review.json')
assert verified['decision']=='recommended' and len(verified['per_marker_audit'])==5
assert all(x['entire_raw_assistant_content_manually_read'] for x in verified['complete_raw_final_and_binding_verification']['candidate']['runs'])
print(json.dumps({'decision':verified['decision'],'report':str(OUT/'independent_review.json'),'report_sha256':sha(OUT/'independent_review.json'),'final_checks':checks,'no_live_processes_at_final_query':checks['process_check_clear']},ensure_ascii=False,indent=2))
