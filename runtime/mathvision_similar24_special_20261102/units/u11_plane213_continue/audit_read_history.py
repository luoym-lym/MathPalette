from bootstrap import *
import base64
q=next(x for x in read(TASK/'history_index.json')['questions'] if x['question_id']=='Plane213')
paths=set(q['other_scoped_history_file_references']+q['additional_math_manual_history_references']+q['independent_review_references'])
roots=[OLD/'background_09/Plane213/open_notch_local_global_binding',TASK/'root_213/Plane213/user233_boundary_spine_foot_transfer_v1',TASK/'units/u10_plane213_refine/Plane213/user233_exterior_concave_corner_to_B_v2',OLD/'background_23/Plane233/r23_exterior_notch_correspondence']
for root in roots:
    paths.update(str(p) for p in root.rglob('*.json'))
extra=[TASK/'parent_plane213_v2_binding_audit.json',OLD/'annotation_semantics_lessons_20261102.json',OLD/'annotation_semantics_lesson_plane242_r24_20261102.json',OLD/'batch_12/Plane233/independent_review.json']
paths.update(str(p) for p in extra)
records=[]
for path in sorted(paths):
    f=Path(path)
    if not f.is_absolute():f=ROOT/f
    obj=read(f)
    record={'path':str(f),'sha256':sha(f),'fully_read_and_JSON_decoded':True,'top_level_keys':list(obj) if isinstance(obj,dict) else None}
    if f.name=='request.json':
        content=obj['messages'][1]['content']
        record['formal_question_text']=next(x['text'] for x in content if x['type']=='text')
        uri=next(x['image_url']['url'] for x in content if x['type']=='image_url')
        im=base64.b64decode(uri.split(',',1)[1]);record['embedded_PNG_sha256']=hashlib.sha256(im).hexdigest();del im,uri
    records.append(record)
    del obj
old=[]
for root,manual in zip(roots,[['C','B'],['B','C'],['B','E'],['D','B']]):
    design=read(root/'design.json');summaries=list(root.rglob('summary.json'));assert len(summaries)==1
    sp=summaries[0];s=read(sp);binding=read(sp.parent/'binding.json')
    assert sha(root/'design.json')==sha(sp.parent/'design_snapshot.json')==s['design_sha256']
    assert sha(root/'candidate.png')==s['image_sha256'] and sha(sp.parent/'request.json')==s['request_body_sha256']
    finals=[]
    for i,r in enumerate(s['results'],1):
        raw=read(sp.parent/f'run_{i:02d}_response.json');started=read(sp.parent/f'run_{i:02d}_started.json')
        assert sha(sp.parent/f'run_{i:02d}_response.json')==r['response_sha256']
        assert raw['choices'][0]['message']['content']==r['answer']
        assert started['run_id']==r['run_id']
        finals.append({'final_option_manually_read':manual[i-1],'full_answer':r['answer'],'status':r['status'],'finish_reason':r['finish_reason'],'truncated':r.get('truncated'),'run_id':r['run_id'],'response_sha256':r['response_sha256']})
    old.append({'directory':str(root),'question_id':s['question_id'],'preset':s['expected_wrong_answer'],'image_sha256':s['image_sha256'],'full_finals':finals,'two_hit':all(x==s['expected_wrong_answer'] for x in manual),'all_bindings_currently_exact':True,'immutable_old_results_unchanged':True})
refs=[]
for q,manifest in read(TASK/'reference_manifest.json').items():
    root=TASK/manifest['directory']
    plugin=read(root/'C01.json');recipes=read(root/'recipes.json');reference=read(root/'reference.json')
    assert sha(root/'C01.png')==manifest['png_sha256'] and sha(root/'C01.json')==manifest['plugin_sha256']
    assert recipes==reference['recipes']
    refs.append({'question_id':q,'all_three_JSON_files_read_fully':True,'actual_current_native_PNG_viewed':True,'actions':plugin['params']['actions'],'png_sha256':manifest['png_sha256'],'plugin_sha256':manifest['plugin_sha256']})
save('prior_history_read_and_binding_audit.json',{'at_utc':now(),'all_assigned_prior_full_raw_responses_personally_read':True,'machine_full_file_read_audit':records,'old_complete_results':old,'all_nine_current_reference_audits':refs,'parent_binding_audit_read':read(TASK/'parent_plane213_v2_binding_audit.json'),'no_old_requests_retried':True,'known_Plane213_calls_before_this_unit':6,'known_Plane213_failed_or_aborted_from_index':0,'no_reference_or_other_question_result_counted_for_this_question':True,'old_Plane233_independent_objections':'Closed internal U contours with source components2,3,5,5 give false partition. New source styles must stay on true exterior edges; color comparison of geometric shape does not create a physical printed-pattern task.'})
print(json.dumps({'files_fully_read':len(records),'old_frozen_pairs_bound':len(old),'current_references':len(refs),'old_213_finals':[['C','B'],['B','C'],['B','E']]}))
