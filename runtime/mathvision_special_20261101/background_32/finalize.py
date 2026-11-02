from prepare import *
from quick_test import SYSTEM_PROMPT, TEST_PROFILES

MANUAL = {
 'r32_ear_content_preserving_comparison': {
   'finals':['D','C'],
   'notes':[
    'Explicit Final Answer: D. It incorrectly distinguishes common mouth arcs and treats D as preserving the original nose; D actually reverses the preexisting nose. No conflicting terminal letter/value.',
    'Explicit Answer: C. It mislocates blue on the left and falsely says B lacks colored ears, despite both B source-matching shoulders being colored in the actual frozen PNG. No conflicting terminal letter/value.'
   ]},
 'r32_wedge_print_preserved_halfturn_alternative': {
   'finals':['A','B'],
   'notes':[
    'Explicit A:A. It hallucinates a red bottom/top border and describes A as red even though the actual A is uncolored. Frozen preset is D, so A is a miss; not relabeled.',
    'Explicit Final Answer: B. Correct option, with inaccurate axis/quadrant descriptions. Frozen preset D missed. No contradictory terminal letter/value.'
   ]},
 'r32_nose_extent_preserved_comparison': {
   'finals':['B','C'],
   'notes':[
    'Explicit Final Answer: B, also consistent with initial and concluding B. It correctly notices colored A/B noses but invents differing eye orientations; actual eyes are common. Correct letter, preset A missed.',
    'Explicit terminal C. It incorrectly claims C preserves the red nose, although actual C nose is black, and invents a B-ear narrowing. Preset A missed; no contradictory terminal letter/value.'
   ]},
 'r32_diagonal_print_preserved_singleflip': {
   'finals':['A','B'],
   'notes':[
    'Explicit A:A matches preset A on this one run. It treats the second flip as a quarter-turn and misreads the actual rising A diagonal as descending and the actual A left wedge as bottom. This narrative does not prove the intended single-reflection mechanism.',
    'Explicit Choice B, consistent with its final descending diagonal. Correct option despite inaccurate quadrant and partial-color language. Preset A missed. The A/B pair is not a two-hit candidate.'
   ]}
}

def all_bindings():
    return [read(next((ROOT/p['qid']/p['variant']/'tests').glob('*/binding.json'))) for p in PLANS]

def finish():
    process=read(ROOT/'process_audit_final.json')
    assert process['all_own_api_processes_closed']
    first_call=min(datetime.fromisoformat(b['created_at']) for b in all_bindings())
    oldchecks=[]
    for path,expected in read(ROOT/'old_evidence_hashes_start.json').items():
        p=PROJECT/path
        oldchecks.append({'path':path,'before':expected,'after':sha(p) if p.exists() else None,'unchanged':p.is_file() and sha(p)==expected})
    assert all(x['unchanged'] for x in oldchecks)
    save(ROOT/'old_evidence_preservation_final.json',{'checked_at':now(),'checked_files':oldchecks,'all_unchanged':True,'no_global_or_old_evidence_rewrite':True})
    report=read(BASE/'exploration_report.json')
    inv=read(BASE/'inventory.json')
    remains=[r for r in rows(BASE/'remaining_questions.jsonl') if r.get('question_id') in IDS]
    attempts=[a for a in report.get('attempts',[]) if a.get('question_id') in IDS]
    assert len(attempts)==2 and all(a['independent_review']['decision']=='reject' for a in attempts)
    save(ROOT/'allocation_history_final.json',{'read_at':now(),'all_inventory_json_read':True,'inventory_sha256':sha(BASE/'inventory.json'),'remaining_assigned_records':remains,'old_completed_attempts':attempts,'runtime_progress_is_diagnostic_not_authoritative':True,'no_other_old_same_question_design_found':True,'assigned_scope':IDS,'delivered_exclusion_checked_authoritatively_per_question':True})
    protocol_files=['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json']
    protocol_files += [str((BASE/p).relative_to(PROJECT)) for p in ['background_32_brief.txt','background_32_assignment.json','annotation_semantics_lessons_20261102.json','refinement_dispatch_20261102.json','continuation_brief.txt']]
    save(ROOT/'protocol_read_log.json',{'read_in_full_before_design':True,'paths_and_current_hashes':{p:sha(PROJECT/p) for p in protocol_files},'authorization':'User explicitly authorizes independent runtime exploration and exact two calls per new frozen design, overrides workbench manual-only exploration wording; no authorization for Pass/Collect/publication/formal review API.'})
    source_audits={}
    cfg,ad=make_adapter()
    for qid in IDS:
        e=eligibility(qid);assert e['eligible'],e['reasons']
        save(ROOT/qid/'eligibility_final.json',e)
        before=read(ROOT/qid/'input_manifest_start.json');after=input_manifest(ad,qid)
        drifts=[{'path':p,'before':h,'after':after['files'].get(p)} for p,h in before['files'].items() if after['files'].get(p)!=h]
        global_meta={'PlaneGeometry/dataset.jsonl','provenance/approvals.json','provenance/source_notes.json'}
        material=[d for d in drifts if d['path'] not in global_meta]
        assert not material
        assert before['record_sha256']==e['formal_record_sha256']
        start=read(ROOT/qid/'eligibility_start.json')
        assert start['original_approval']==e['original_approval'] and start['current_content_sha256']==e['current_content_sha256']
        diagnostic={}
        for path,old in start['mutable_progress_diagnostic_only'].items():
            p=PROJECT/path
            diagnostic[path]={'historical_hash_preserved':old,'current_hash':sha(p),'differs':sha(p)!=old,'classification':'mutable shared progress metadata; not frozen original input; not rewritten'}
        audit={'question_id':qid,'checked_at':now(),'all_material_source_files_unchanged':True,'global_metadata_drifts':drifts,'formal_record_and_original_approval_and_content_unchanged':True,'formal_png_equals_start_copy':sha(BRANCH/e['formal_record']['image'])==sha(ROOT/qid/'formal.png'),'source_jpg_equals_start_copy':sha(BRANCH/e['formal_record']['original_image'])==sha(ROOT/qid/'source.jpg'),'current_eligibility':e['eligible'],'current_manifest':after,'mutable_progress_classification':diagnostic,'unrelated_concurrent_workbench_changes':'Preserved. Strict own-root write guard prevented our writes elsewhere. No restore, actor attribution, or whole-workspace-unchanged claim.'}
        assert audit['formal_png_equals_start_copy'] and audit['source_jpg_equals_start_copy']
        save(ROOT/qid/'source_audit_final.json',audit);source_audits[qid]=str(ROOT/qid/'source_audit_final.json')
    results=[]
    for plan in PLANS:
        qid=plan['qid'];out=ROOT/qid/plan['variant']; paths=list((out/'tests').iterdir());assert len(paths)==1
        test=paths[0];b=read(test/'binding.json');summary=read(test/'summary.json');design=read(out/'design.json');req=read(test/'request.json')
        png=(out/'candidate.png').read_bytes()
        assert b['image_sha256']==sha(out/'candidate.png') and b['design_sha256']==sha(out/'design.json')
        assert b['pixel_sha256']==pixel_hash(png)
        assert (test/'design_snapshot.json').read_bytes()==(out/'design.json').read_bytes()
        assert (out/'repeat.png').read_bytes()==png
        assert b['expected_wrong_answer']==plan['wrong']==design['expected_wrong_answer']
        assert b['request_body_sha256']==sha(test/'request.json')
        assert b['question']==eligibility(qid)['formal_record']['question']
        expected={'model':TEST_PROFILES['quicktest3']['model'],'stream':False,'thinking':TEST_PROFILES['quicktest3']['thinking'],'messages':[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':[{'type':'text','text':b['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(png).decode('ascii')}}]}]}
        assert req==expected and (test/'request.json').read_bytes()==json.dumps(expected,ensure_ascii=False).encode('utf-8')
        assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'}
        assert datetime.fromisoformat(design['created_at'])<first_call
        assert datetime.fromisoformat(read(out/'design_difference_audit.json')['created_at'])<first_call
        assert datetime.fromisoformat(read(out/'primary_review.json')['created_at'])<datetime.fromisoformat(b['created_at'])
        assert len(list(test.glob('run_*_started.json')))==2 and len(list(test.glob('run_*_response.json')))==2
        manual=[]
        for i,letter in enumerate(MANUAL[plan['variant']]['finals'],1):
            run=read(test/f'run_{i:02d}.json');raw=read(test/f'run_{i:02d}_response.json');started=read(test/f'run_{i:02d}_started.json')
            full=raw['choices'][0]['message']['content']
            assert run['status']=='completed' and run['finish_reason']=='stop' and not run.get('truncated')
            assert raw['choices'][0]['finish_reason']=='stop' and full==run['answer']
            assert run['response_sha256']==sha(test/f'run_{i:02d}_response.json')
            assert all(run[k]==b[k] and started[k]==b[k] for k in ['image_sha256','design_sha256','request_body_sha256'])
            assert run['run_id']==started['run_id']
            assert datetime.fromisoformat(design['created_at'])<datetime.fromisoformat(started['started_at'])
            assert run['response_model']=='mimo-v2.6-flash'
            manual.append({'run_index':i,'status':'completed','full_final_answer_manually_read':full,'manual_final_letter':letter,'manual_final_value':None,'contradictory_terminal_letter_or_value':False,'matches_immutable_pre_call_preset':letter==plan['wrong'],'narrative_review':MANUAL[plan['variant']]['notes'][i-1],'raw_response_path':str(test/f'run_{i:02d}_response.json'),'raw_response_sha256':run['response_sha256'],'run_record_path':str(test/f'run_{i:02d}.json'),'run_record_sha256':sha(test/f'run_{i:02d}.json'),'run_started_path':str(test/f'run_{i:02d}_started.json'),'run_started_sha256':sha(test/f'run_{i:02d}_started.json')})
        assert summary['two_completed'] and summary['results']==[read(test/'run_01.json'),read(test/'run_02.json')]
        hit=all(x['matches_immutable_pre_call_preset'] for x in manual)
        assert not hit
        m={'created_at':now(),'stage':'material_refinement','review_level':'PRIMARY manual full-final read only','question_id':qid,'variant_id':plan['variant'],'predeclared_wrong_answer':plan['wrong'],'original_correct_answer':'B','runs':manual,'manual_finals':[x['manual_final_letter'] for x in manual],'two_completed_same_frozen_request_png_design':True,'raw_pair_matches_own_preset':hit,'credible_candidate_for_new_parent_review':False,'decision':'miss; preserve frozen evidence and do not retest or relabel','binding':str(test/'binding.json'),'request':str(test/'request.json'),'summary':str(test/'summary.json'),'original_controls':'None available for these IDs; none repeated. No incremental effect claimed.','limits':['Only two calls per design, no human study, rate, causal or per-marker effect estimate.','Different erroneous narratives are disclosed; identical narratives and correct controls were not extra gates.']}
        save(out/'manual_final_review.json',m)
        immutable=[out/'design_difference_audit.json',out/'design.json',out/'plugin.json',out/'plugin_submitted.json',out/'candidate.png',out/'repeat.png',out/'fresh_context.json',out/'per_marker_grounding.json',out/'primary_review.json',out/'render_audit.json',out/'eligibility_immediately_before_calls.json',out/'api_process.json',out/'api_process_finished.json',test/'binding.json',test/'request.json',test/'design_snapshot.json',test/'summary.json']
        immutable += [test/f'run_{i:02d}{suffix}.json' for i in (1,2) for suffix in ('','_response','_started')]
        save(out/'evidence_binding_audit.json',{'checked_at':now(),'checks':{'exact_original_question_and_only_one_candidate_png_in_request':True,'exact_existing_system_prompt_profile_thinking_disabled':True,'no_correct_answer_preset_intent_history_plugin_in_solver_input':True,'no_token_limit_profile_timeout_override':True,'request_exact_bytes_bound':True,'same_frozen_png_and_preset_both_calls':True,'all_four_presets_and_difference_audits_predate_first_new_call':True,'primary_native_review_before_calls':True,'two_complete_stop_responses_no_extra_retry_or_selection':True,'full_raw_finals_read_manually':True,'source_and_current_eligibility_valid':True,'no_original_control_repetition':True},'immutable_files':{str(p.relative_to(PROJECT)):sha(p) for p in immutable},'raw_finals':m['manual_finals'],'own_preset':plan['wrong'],'two_hit':False,'new_independent_review_required_before_any_future_delivery':True})
        result={'question_id':qid,'variant_id':plan['variant'],'expected_wrong_answer':plan['wrong'],'finals':m['manual_finals'],'raw_paired_hit':False,'primary_possible_candidate':False,'status':'completed_pair_missed_preset','candidate_png':str(out/'candidate.png'),'image_sha256':sha(out/'candidate.png'),'plugin':str(out/'plugin.json'),'design':str(out/'design.json'),'design_sha256':sha(out/'design.json'),'old_new_difference':plan['difference'],'design_difference_audit':str(out/'design_difference_audit.json'),'primary_math_visual_marker_review':str(out/'primary_review.json'),'manual_full_finals':str(out/'manual_final_review.json'),'binding':str(test/'binding.json'),'evidence_summary':str(test/'summary.json'),'request':str(test/'request.json'),'evidence_binding_audit':str(out/'evidence_binding_audit.json'),'source_audit':source_audits[qid]}
        results.append(result)
    alternatives={
      'Plane295':[
        {'family':'Detached or cross-image external shoulder guides','decision':'prescreened; no call','reason':'Direct grounded connectors between vertically stacked tiny ear features pass through head/ear drawing regions; long offset multisegment routes need implicit projection anchors and overwhelm the small diagnostics. Detached short colored copies can reasonably be additional cat strokes without a textual convention. No cleaner simple information-bearing repair was established.'},
        {'family':'Other nose/ear color permutations and width variants','decision':'no call','reason':'Would repeat the two tested feature families with only palette/width/target-option changes. The observed D/C or B/C letters do not authorize a changed preset. No new matched information or concrete repair beyond the tested preserved-source cases.'}
      ],
      'Plane342':[
        {'family':'Style existing external flip references alone','decision':'prescreened; no call','reason':'Clearly external, but highlighting the actual motion references does not supply a distinct false source-to-option geometric correspondence. Styling an option to echo an unrelated arrow color alone would be salience, not a rigorous mapping.'},
        {'family':'New guides or other wedge/diagonal palettes','decision':'no call','reason':'New guides risk new arrows/cut/region interpretations or visually intrusive traversals; no simple grounded external comparison improved on the exact color-transport repair. Recoloring or renaming the completed wedge/diagonal designs would be cosmetic repetition. No use of observed A/B to relabel the failed D preset.'}
      ]}
    for qid in IDS:
        save(ROOT/qid/'assessment.json',{'question_id':qid,'stage':'material_refinement','assessed_at':now(),'tested_variants':[r['variant_id'] for r in results if r['question_id']==qid],'outcomes':[{'variant':r['variant_id'],'preset':r['expected_wrong_answer'],'finals':r['finals']} for r in results if r['question_id']==qid],'unique_math':str(ROOT/qid/'primary_original_math.json'),'source_mouth_caveat':read(ROOT/qid/'primary_original_math.json').get('source_wording_caveat'),'further_families_prescreened':alternatives[qid],'stop_reason':'The reasonable simple actual-feature families and concrete semantic repair have been assessed. No further materially new, clearly legal simple hypothesis was established; no quota-based calls.'})
    save(ROOT/'second_review_queue.json',{'unit':'background_32','stage':'material_refinement','created_at':now(),'question_ids':[],'candidates':[],'count':0,'reason':'All four new pairs missed their own immutable presets. Old rejected C/C and D/D variants remain rejected and are not promoted.','parent_rule':'Every eventual delivery requires a NEW parent-commissioned independent review; no self-approval, Pass/Collect/publication or formal review API used.'})
    checkpoint={'unit':'background_32','stage':'material_refinement','status':'completed_all_assigned','finished_at':now(),'stop_reason':'Both assigned questions assessed with four substantive designs and further family prescreens; zero credible pairs. Reasonable simple substantive hypotheses exhausted for this finite unit.','assigned_question_ids':IDS,'assessed_question_ids':IDS,'actual_assessed_question_ids':IDS,'unworked_question_ids':[],
       'counts':{'assigned_questions':2,'assessed_questions':2,'new_designs':4,'completed_candidate_pairs':4,'actual_quicktest3_calls':8,'completed_calls':8,'original_control_calls':0,'api_errors':0,'aborted_calls':0,'retries':0,'credible_two_hit_candidates':0,'new_independent_reviews':0,'delivered':0,'local_preparation_issues':3},
       'candidates_and_failed_pairs':results,'second_review_queue':str(ROOT/'second_review_queue.json'),'question_assessment_paths':{q:str(ROOT/q/'assessment.json') for q in IDS},'source_and_eligibility_audits':source_audits,'old_evidence_preservation':str(ROOT/'old_evidence_preservation_final.json'),'prior_history_and_reference_audit':str(ROOT/'prior_history_and_reference_audit.json'),'allocation_history':str(ROOT/'allocation_history_final.json'),'protocol_read_log':str(ROOT/'protocol_read_log.json'),'process_audit':str(ROOT/'process_audit_final.json'),'isolation':str(ROOT/'isolation.json'),'all_own_api_processes_closed':True,'failures':[{'question_id':r['question_id'],'variant_id':r['variant_id'],'type':'completed_pair_miss','preset':r['expected_wrong_answer'],'full_manual_finals':r['finals']} for r in results],'api_errors':[],'aborts':[],'preparation_issues_preserved':[str(ROOT/'preparation_errors.json'),str(ROOT/'additional_preparation_errors.json')],'limits':['No original controls for these assigned IDs were available; no repeats, statistical or incremental/causal claim.','Plane295 inherited common-mouth/eyes-only wording caveat remains explicit; no literal raster-extension claim.','Native inspection and proofs are PRIMARY only. No independent self-approval or formal action.','Guarded scoped source preservation is asserted; unrelated concurrent changes and mutable global progress are preserved, not restored or mislabeled as frozen-source corruption.']}
    save(ROOT/'checkpoint.json',checkpoint)
    print(json.dumps({'assessed':2,'designs':4,'complete_calls':8,'possible_candidates':0,'api_errors':0,'aborts':0,'retries':0,'old_evidence_all_unchanged':True,'all_own_api_processes_closed':True,'checkpoint':str(ROOT/'checkpoint.json')}),flush=True)

if __name__=='__main__': finish()
