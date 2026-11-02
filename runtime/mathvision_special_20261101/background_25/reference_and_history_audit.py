from tools_local import *
refs=[]
for p in sorted(TASK.parent.glob('batch_*/manifest.json')):
    d=json.loads(p.read_text(encoding='utf-8-sig'));items=[]
    for c in d['candidates']:
        item={k:c.get(k) for k in ('question_id','mechanism','expected_wrong_answer','quality_review','candidate_source')};items.append(item)
    refs.append({'batch':p.parent.name,'manifest_sha256':file_hash(p),'candidates':items})
write(TASK/'delivered_reference_audit.json',{'references_read_only':refs,'actual_native_relevant_reference_images_viewed':['batch_01/Solid176/candidate.png','batch_03/Solid203/candidate.png','batch_07/Solid167/candidate.png'],'information_binding_principle':'Marks must encode specific seam,feature,point,orientation,scale or composition correspondences. A receiver contour is justified only by a source geometric role. No arbitrarylabelhighlighting; local compatibility can be a misleading but legitimate necessarycondition, while actualmathematicalconstraints remain readable.','new_designs_apply_principle':'Slab/pillar overlap; bent/flat opening topology; globalonepair sufficiency; hinge-normal relation transfer; diagonal/faceadjacency; foreshortenedunitcount; sourcehalf-to-whole identity.'})
print(json.dumps(refs,ensure_ascii=False,indent=2))
prior=json.loads((TASK/'all_prior_same_question_evidence.json').read_text(encoding='utf-8'))
independent=[]
for p in (TASK.parent/'independent_review').rglob('*'):
    if p.is_file() and p.suffix in ('.json','.txt','.md'):
        text=p.read_text(encoding='utf-8-sig')
        if any(q in text for q in ASSIGNED):independent.append({'path':str(p.relative_to(ROOT)),'sha256':file_hash(p),'text':text})
assert not independent,'Previouslyunknownindependentobjections mustbe readbeforeclosingaudit'
controls=[]
for q in ASSIGNED:
    paths=set()
    for x in prior[q]:
        parent=(ROOT/x['folder']).parent
        paths.update(p for p in parent.rglob('binding.json') if 'control' in str(p).lower())
    for p in sorted(paths):controls.append({'question_id':q,'binding_path':str(p.relative_to(ROOT)),'binding_sha256':file_hash(p),'data':json.loads(p.read_text(encoding='utf-8-sig'))})
write(TASK/'prior_history_completion_audit.json',{'assigned_question_ids':ASSIGNED,'all_prior_candidates':{q:[{'path':x['folder'],'preset':x['design'].get('expected_wrong_answer'),'files_sha256':x['files']} for x in vv] for q,vv in prior.items()},'old_designs_and_native_images_viewed':True,'complete_old_raw_final_answers_manually_read':True,'primary_reviews_and_math_read':True,'current_exact_question_variant_independent_objection_reports':independent,'independent_report_search_scope':str(TASK.parent/'independent_review'),'old_qualifying_unchanged_designs_to_queue':[],'controls_reused_by_reference':controls,'no_existing_controls_found':not controls,'control_policy':'No controls repeated. Currentold samequestion folders have no separateoriginalcontrol bindings; no originalcontrolcausal estimate claimed.','historical_mutable_progress_files':'Diagnostic-only. Existingprogresshashdrift isclassifiedseparately; authoritativeeligibility isfromcurrentformaldataset+approvals+Specialrecords.'})
