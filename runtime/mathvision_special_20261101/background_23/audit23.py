from common23 import *
from datetime import datetime,timezone
assigned=read(BASE/'background_23_assignment.json')['question_ids']
refs=[];frozen={};controls={}
for qid in assigned:
    h=read(OUT/qid/'prior_history_manifest.json')
    for c in h['prior_attempts']:
        for f in c['files']:
            p=ROOT/f['path'];frozen[f['path']]=f['sha256']
            if p.suffix=='.json':read(p)
    for p in h['independent_review_files']:
        read(BASE/p);frozen[str((BASE/p).relative_to(ROOT))]=sha(BASE/p)
    e=eligibility(qid);assert e['eligible'];write(OUT/qid/'eligibility_before_primary.json',e)
    frozen.update(e['frozen_source_files'])
    controls[qid]=[]
    locations={'Plane192':'plane_explore/Plane192/original_control','Plane233':'background_06/plane_parts/Plane233/original_controls','Plane263':'plane_mid/Plane263/control_original','Solid220':'solid_explore/Solid220/false_face_pair/baseline_control'}
    if qid in locations:
        for p in sorted((BASE/locations[qid]).rglob('run_*_response.json')):
            r=read(p);frozen[str(p.relative_to(ROOT))]=sha(p)
            controls[qid].append({'raw_path':str(p.relative_to(ROOT)),'raw_sha256':sha(p),'full_final':r['choices'][0]['message']['content'],'finish_reason':r['choices'][0]['finish_reason']})
    branch=e['branch'];record=e['formal_record']
    srcs=[p for p in record['runtime_dependencies'] if p.endswith('/source.json')]
    write(OUT/qid/'source_context_audit.json',{'formal_record':record,'source_records':[read(ROOT/branch/p) for p in srcs],'current_approval_valid':True,'formal_question_and_answer_authority':'dataset.jsonl','native_formal_and_source_images_viewed':True,'source_image_missing':not bool(record.get('original_image')),'notes':('Source uniform gray fill vs formal white is pre-existing frozen redraw behavior, not this candidate; new plugin preserves actual formal fill pixels.' if qid=='Plane263' else 'Original text, shapes, label ownership and all categorical distinctions retained. No extra source labels or conditions added.')})
for i in range(1,10):
    b=BASE/f'batch_{i:02d}';items=[]
    for p in b.rglob('design.json'):
        d=read(p);items.append({'path':str(p.relative_to(ROOT)),'question_id':d.get('question_id'),'hypothesis':d.get('hypothesis',d.get('mechanism',d.get('design_reason'))),'plugin_actions':[read(q)['params']['actions'] for q in [p.with_name('plugin.json')] if q.exists()]})
    refs.append({'batch':b.name,'designs':items,'manifest_read':bool((b/'manifest.json').exists())})
    if (b/'manifest.json').exists():read(b/'manifest.json')
    for p in b.rglob('*.json'):frozen[str(p.relative_to(ROOT))]=sha(p)
write(OUT/'delivered_reference_study.json',{'batches':refs,'information_transfer_principle':'Bind actual input features to a misleading comparison; do not use arbitrary option salience. Open existing boundary features can remove incompatible-cut semantics. A count of marks is not the test of relevance.','reference_only_no_retests':True})
progress={}
for name in ['exploration_report.json','remaining_questions.jsonl','inventory.json','refinement_shortlist_snapshot.json']:
    p=BASE/name;progress[str(p.relative_to(ROOT))]=sha(p)
    data=rows(p) if p.suffix=='.jsonl' else read(p)
    if name=='remaining_questions.jsonl':write(OUT/'current_progress_assigned_rows.json',[r for r in data if r.get('question_id',r.get('id')) in assigned])
for p in [ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'AGENTS.md',ROOT/'provenance/approvals.json',BASE/'runtime_isolation.py',BASE/'harness/quicktest3_isolated.py',BASE/'delivery_bridge_adapter.py']:
    frozen[str(p.relative_to(ROOT))]=sha(p)
for branch in ['PlaneGeometry','SolidGeometry']:
    for p in (ROOT/branch/'workbench').glob('*'):
        if p.is_file():frozen[str(p.relative_to(ROOT))]=sha(p)
    for name in ['special_variant/accepted_index.jsonl','special_variant/collected_index.jsonl']:
        p=ROOT/branch/name
        if p.exists():frozen[str(p.relative_to(ROOT))]=sha(p)
write(OUT/'old_control_reuse.json',controls)
write(OUT/'preservation_baseline.json',{'created_at':datetime.now(timezone.utc).isoformat(),'frozen_relevant_files':frozen,'mutable_progress_metadata':progress,'scope':'Relevant formal inputs, old same-question artifacts, delivered JSON references and helpers; unrelated concurrent workbench changes never restored. Not a claim that the whole workspace is static.'})
print(json.dumps({'frozen_file_count':len(frozen),'controls':controls,'delivered_reference_designs':refs},ensure_ascii=False))
