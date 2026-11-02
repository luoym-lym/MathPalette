from tools import *
import base64,subprocess
MANUAL={
 'Solid134':[
  ('A',False,True,'Complete final is A. Its narrative misdescribes several shapes/areas, but it never concludes the preset B.'),
  ('B',True,True,'Complete final is B. It explicitly uses the colored source/option side correspondence, but one such run alone is not a paired hit.')],
 'Solid140':[
  ('D; 1m',False,True,'Complete final derives conserved volume2m^3 and new base2m^2, concludes D=1m.'),
  ('D; 1m',False,True,'Complete final independently concludes D=1m.')],
 'Solid153':[
  ('A',False,True,'Complete final selects A from narrow lower capacity.'),
  ('A',False,True,'Complete final compares all five shapes and selects A. No preset E conclusion.')],
 'Plane402':[
  ('26/3',True,True,'Complete final is8 2/3 or26/3, despite acknowledging problems in its own fold reasoning. This one run matches the frozen numerical preset.'),
  ('8',False,True,'Complete final is8. Its consistency check recognizes a length conflict, then still concludes8. It is not26/3.')],
 'Plane409':[
  ('C; incompatible asserted perimeter3b',False,False,'The final explicitly calls the perimeter3b and then claims it corresponds to C=6b-3a, ending C. Because the final letter/expression pair is inconsistent, this is NOT counted as a preset-C hit.'),
  ('B; 3b-6a',False,True,'Complete final concludes3b-6a, corresponding to B. It is not preset C.')],
 'Plane476':[
  ('D; 2/3',False,True,'Complete final derives XQ=.4,QY=.6 and concludes D=2/3.'),
  ('E; 2/3',False,False,'Complete final derives the correct ratio2/3 but labels it E, whose actual choice is3/4. Inconsistent letter/value; not a hit and not a consistent correct final.')],
 'Plane378':[
  ('E; incompatible asserted ratio4/3',False,False,'Complete final calculates4/3, says it is absent from the choices, conjectures a standard variant leading9/8, then ends E while retaining4/3 as the strict-grid calculation. Not preset D; final value/letter not consistent.')],
 'Solid90':[
  ('sqrt(-17); no real solution asserted',False,True,'Complete final misidentifies the face/body/edge roles and explicitly gives sqrt(-17), claiming no such real box. It is not the predeclared sqrt(55).'),
  ('9',False,True,'Complete final gives9 after incorrect diagonal equations. It is not sqrt(55).')],
 'Solid159':[
  ('13',True,True,'Complete final uses an incorrect list of six faces, assigns the blue pair5 and red triple1, and explicitly concludes13. One preset hit.'),
  ('17',False,True,'Complete final eventually derives all three equatorial vertices5 and both apices1, and concludes17. No paired hit.')]
}

# A newly completed Plane378 second final must be read manually and entered here
# before this finalizer can run. An aborted call has no invented manual final.
EXTRA=TASK/'Plane378_second_manual.json'
if EXTRA.exists():
    m=read(EXTRA);MANUAL['Plane378'].append(tuple(m[k] for k in ['final','matches_preset','internally_consistent','reason']))

api_command="Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'python' -and $_.CommandLine -like '*background_17*' -and $_.CommandLine -match 'run_candidate[.]py|run_plane_pairs[.]py' } | Select-Object ProcessId,ParentProcessId,CommandLine | ConvertTo-Json -Compress"
raw=subprocess.run(['powershell','-NoProfile','-Command',api_command],capture_output=True,text=True,encoding='utf-8',check=True).stdout.strip()
live=json.loads(raw) if raw else []
if isinstance(live,dict):live=[live]
assert not live,live
process_audit={'checked_at':datetime.now(timezone.utc).isoformat(),'own_api_processes':live,'no_live_own_api_processes':True,'native_or_T3_children_started':0,'verified_commands':'background_17 run_candidate.py and run_plane_pairs.py; all actual launch PIDs retained per design','abandoned_process_record':str(TASK/'aborted_process.json') if (TASK/'aborted_process.json').exists() else None}
write(TASK/'no_live_api_processes.json',process_audit)

source_audits=[read(TASK/(b+'_source_audit_final.json')) for b in ['PlaneGeometry','SolidGeometry']]
assert all(x['all_passed'] for x in source_audits)
candidates=[];prescreens=[];started=0;completed=0;aborted=0;api_errors=0
for qid in ASSIGNED:
    folder=TASK/qid
    if (folder/'prescreen.json').exists():prescreens.append(read(folder/'prescreen.json'));continue
    design_dirs=[p.parent for p in folder.glob('*/design.json')]
    assert len(design_dirs)==1
    d=design_dirs[0];design=read(d/'design.json');plugin=read(d/'plugin.json');visual=read(d/'primary_visual_review.json');render=read(d/'render_check.json')
    assert design['png_sha256']==file_hash(d/'candidate.png')==visual['candidate_sha256']
    assert design['plugin_sha256']==file_hash(d/'plugin.json')==visual['plugin_sha256']
    assert render['repeat_bytes_identical'] and render['normalized_by_actual_schema'] and visual['legal_and_readable']
    invs=list((d/'tests').glob('quicktest3_*'));assert len(invs)==1
    inv=invs[0];bind=read(inv/'binding.json');payload=read(inv/'request.json')
    harness_isolation=read(d/'harness_isolation.json')
    assert harness_isolation['source_modified'] is False
    assert harness_isolation['sha256']==file_hash(SHARED/'harness/quicktest3_isolated.py')
    assert bind['reference_quick_test_sha256']==file_hash(ROOT/bind['branch']/'workbench/quick_test.py')
    assert bind['expected_wrong_answer']==design['expected_wrong_answer']
    assert bind['image_sha256']==design['png_sha256']
    assert bind['design_sha256']==file_hash(d/'design.json')
    assert (inv/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
    assert bind['request_body_sha256']==file_hash(inv/'request.json')
    assert bind['requested_runs']==2
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    assert len(payload['messages'])==2 and payload['messages'][0]=={'role':'system','content':bind['system_prompt']}
    assert payload['messages'][1]['role']=='user'
    content=payload['messages'][1]['content'];assert len(content)==2
    assert content[0]=={'type':'text','text':read(folder/'formal_record.json')['question']}
    assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==(d/'candidate.png').read_bytes()
    runs=[]
    for index in [1,2]:
        start_path=inv/f'run_{index:02d}_started.json';assert start_path.exists()
        started+=1;s=read(start_path)
        assert s['request_body_sha256']==bind['request_body_sha256'] and s['image_sha256']==bind['image_sha256'] and s['design_sha256']==bind['design_sha256']
        path=inv/f'run_{index:02d}.json'
        if not path.exists():
            a=read(TASK/'aborted_process.json')
            assert a['question_id']==qid and a['run_index']==index
            aborted+=1;runs.append({'run_index':index,'status':'aborted','complete_final':None,'manual_hit':False,'reason':'No complete response; verified own stalled process was terminated without retry.','abort_record':str(TASK/'aborted_process.json'),'started_record':str(start_path)})
            continue
        job=read(path)
        if job['status']!='completed':
            api_errors+=1;runs.append({'run_index':index,'status':job['status'],'manual_hit':False,'raw':str(path)});continue
        completed+=1
        assert not job.get('truncated') and job['finish_reason']=='stop'
        assert job['image_sha256']==bind['image_sha256'] and job['design_sha256']==bind['design_sha256'] and job['request_body_sha256']==bind['request_body_sha256']
        response_path=inv/f'run_{index:02d}_response.json';assert job['response_sha256']==file_hash(response_path)
        response=read(response_path);assert response['choices'][0]['message']['content'].strip()==job['answer']
        assert response['choices'][0]['finish_reason']=='stop'
        manual=MANUAL[qid][index-1]
        runs.append({'run_index':index,'status':'completed','complete_final':job['answer'],'read_complete_final_manually':True,'manual_final':manual[0],'manual_hit':manual[1],'internally_consistent_final':manual[2],'manual_reason':manual[3],'raw_run':str(path),'raw_response':str(response_path),'response_sha256':job['response_sha256'],'elapsed_seconds':job['elapsed_seconds']})
    two_complete=len(runs)==2 and all(x['status']=='completed' for x in runs)
    credible=two_complete and all(x['manual_hit'] and x['internally_consistent_final'] for x in runs)
    review={'question_id':qid,'candidate_name':design['name'],'expected_wrong_answer':design['expected_wrong_answer'],'correct_answer':design['correct_answer'],'complete_pair':two_complete,'credible_paired_hit_primary':credible,'manual_reviews':runs,'evidence_dir':str(inv),'binding':bind,'request_path':str(inv/'request.json'),'raw_request_verified_only_formal_question_and_candidate_png':True,'design_path':str(d/'design.json'),'design':design,'plugin_path':str(d/'plugin.json'),'candidate_png':str(d/'candidate.png'),'render_check_path':str(d/'render_check.json'),'primary_visual_review_path':str(d/'primary_visual_review.json'),'source_audit_path':str(folder/'source_audit_final.json'),'controls':[],'independent_second_review':'NOT performed by this primary researcher. Parent must start NEW independent reviewer before delivery.'}
    write(d/'manual_final_review.json',review);candidates.append(review)

assessed=[qid for qid in ASSIGNED if (TASK/qid/'prescreen.json').exists() or any((TASK/qid).glob('*/manual_final_review.json'))]
assert assessed==ASSIGNED
queue=[c for c in candidates if c['credible_paired_hit_primary']]
counts={'assigned_questions':len(ASSIGNED),'assessed_questions':len(assessed),'unworked_questions':len(set(ASSIGNED)-set(assessed)),'saved_designs':len(candidates),'prescreened_without_design':len(prescreens),'actual_api_calls_started':started,'completed_api_calls':completed,'complete_candidate_pairs':sum(c['complete_pair'] for c in candidates),'aborted_calls':aborted,'api_error_calls':api_errors,'original_controls':0,'credible_paired_hit_possibilities':len(queue),'render_bookkeeping_errors_resolved':1,'retries':0,'formal_or_approval_mutations':0,'Pass_or_Collect_actions':0}
second={'unit':'background_17','created_at':datetime.now(timezone.utc).isoformat(),'primary_only':True,'counts':counts,'candidates':queue,'note':'Empty queue means no credible paired-hit possibility. No delivery authorized by this checkpoint. Any future credible new design requires a NEW parent independent reviewer; never repeat an unchanged failed/aborted image.'}
write(TASK/'second_review_queue.json',second)
checkpoint={'unit':'background_17','status':'terminal_finite_batch_checkpoint','stopping_reason':'All20 assigned questions assessed; all own API processes ended.','created_at':datetime.now(timezone.utc).isoformat(),'assigned_question_ids':ASSIGNED,'actual_assessed_question_ids':assessed,'assessed_question_ids':assessed,'unworked_question_ids':[],'counts':counts,'candidates':candidates,'prescreens':prescreens,'source_audits':[str(TASK/(b+'_source_audit_final.json')) for b in ['PlaneGeometry','SolidGeometry']],'current_source_eligibility_and_approval_audits_all_passed':True,'second_review_queue':str(TASK/'second_review_queue.json'),'process_audit':process_audit,'errors_and_aborts':{'render_bookkeeping':{'question_id':'Plane402','error':'Missing optional appearance_changes method on Plane renderer; own bookkeeping helper fixed, actual frozen bytes reverified twice, no API retry.','record':str(TASK/'Plane402/exposed_strip_extent_binding/render_bookkeeping_error.json')},'aborted_process':read(TASK/'aborted_process.json') if (TASK/'aborted_process.json').exists() else None},'controls':[],'limitations':['No separate original controls, human studies or per-marker causal ablations were run. They are not additional hard gates, but no causal or statistical reliability claim is made.','Single preset hits are retained as failures of the paired criterion. Inconsistent final letter/value pairs are explicitly excluded.','Formal source answer E for Plane281,6 for Solid195 and12 for Solid141 were retained without claiming a complete independent proof in those no-design prescreens.','Source JPEG binary copies have the historical local filename source.png; their bytes and actual formal paths are separately audited.','Concurrent unrelated Author-designed workbench activity and mutable aggregate runtime progress are preserved; no whole-workspace hash equality is asserted.'],'next_recommendations':['No candidate from this finite batch is eligible for delivery.','Preserve all nine presets, all raw requests/responses and all single-hit/inconsistent/aborted history. Do not retest unchanged candidates.','Coverage of this allocation is complete. Parent may aggregate actual assessed IDs and terminal status; no unworked IDs to release.','A materially new legal information-binding hypothesis would need its own predeclared two-call pair and a NEW independent reviewer before any delivery.']}
write(TASK/'checkpoint.json',checkpoint)
summary='background_17 terminal checkpoint\n'+json.dumps(counts,ensure_ascii=False,indent=2)+'\nNo qualified delivery; primary research only. See checkpoint.json and second_review_queue.json.\n'
(TASK/'report.txt').write_text(summary,encoding='utf-8')
files={str(p.relative_to(TASK)):{'sha256':file_hash(p),'bytes':p.stat().st_size} for p in TASK.rglob('*') if p.is_file()}
write(TASK/'artifact_manifest.json',{'created_at':datetime.now(timezone.utc).isoformat(),'files':files,'note':'Manifest records this unit only; includes immutable tested designs, raw bindings and complete manual finals. Caches may be non-evidence runtime files.'})
print(json.dumps(counts,ensure_ascii=False))
