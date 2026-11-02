from local_env import *
from api_gate import check_eligibility, check_frozen
import json, subprocess, hashlib

entries=read_json(OWN/'primary_design_manifest.json')+read_json(OWN/'supplementary_design_manifest.json')
assignment=read_json(OWN/'assignment.json')
queue=read_json(OWN/'second_review_queue.json')
results=[]; all_api=[]
for entry in entries:
    candidate=Path(entry['candidate_directory'])
    design=check_frozen(candidate)
    review=read_json(candidate/'manual_full_final_review.json')
    invocation=Path(review['summary_path']).parent
    summary=read_json(invocation/'summary.json')
    finished=read_json(candidate/'api_process_finished.json')
    assert summary['two_completed'] and finished['status']=='completed' and finished['actual_network_requests_seen']==2
    assert len(list(invocation.glob('run_*_started.json')))==2
    assert sha(candidate/'candidate.png')==summary['image_sha256']
    assert sha(candidate/'design.json')==summary['design_sha256']==sha(invocation/'design_snapshot.json')
    assert sha(invocation/'request.json')==summary['request_body_sha256']
    for i,result in enumerate(summary['results'],1):
        raw=read_json(invocation/f'run_{i:02d}_response.json')
        assert raw['choices'][0]['finish_reason']=='stop' and not result.get('truncated')
        assert raw['choices'][0]['message']['content']==review['finals'][i-1]['full_answer_exact']
        assert sha(invocation/f'run_{i:02d}_response.json')==result['response_sha256']
        all_api.append({'question_id':entry['question_id'],'variant_id':entry['variant_id'],'run_index':i,
                        'run_id':result['run_id'],'pid':finished['pid'],'status':'completed','finish_reason':'stop',
                        'preset':design['expected_wrong_answer'],'manual_final':review['finals'][i-1]['final_choice_manually_resolved'],
                        'preset_hit':review['finals'][i-1]['matches_frozen_letter_and_value'],
                        'raw_path':str(invocation/f'run_{i:02d}_response.json'),'raw_sha256':result['response_sha256']})
    results.append({**entry,'manual_finals':[x['final_choice_manually_resolved'] for x in review['finals']],
                    'two_complete_target_hits':review['two_complete_target_hits'],'status':review['classification'],
                    'manual_review':str(candidate/'manual_full_final_review.json'),'summary':str(invocation/'summary.json'),
                    'image_sha256':sha(candidate/'candidate.png'),'plugin_sha256':sha(candidate/'plugin.json'),
                    'design_sha256':sha(candidate/'design.json'),'actual_requests':2})
assert len({x['run_id'] for x in all_api})==len(all_api)==14
assert not any(x['two_complete_target_hits'] for x in results)
assert queue==[]

reasons={
 'Solid146':{
   'unique_answer':'D',
   'uncompleted_reason':'The only new clean slope-direction comparison gave D/C against frozen E. There is no specified source cut to pair without adding a new given. No further materially distinct reliable correspondence was found that also preserves the impossible-choice semantics under literal color reading.',
   'considered_and_rejected':[
     {'hypothesis':'Draw two colored cuts on the blank folded packet','reason':'The source allows freely chosen straight cuts. Fixed new lines would change the question and require a different original approval.'},
     {'hypothesis':'Color one of possible A/B/C/E as a source-to-choice false match','reason':'With a blank uncolored source, an intrinsic colored-edge reading can make that additional possible choice impossible, destroying unique D. Source/answer/legend edits are prohibited.'},
     {'hypothesis':'Swap the red/blue grouping of the same eight D slants from direction classes to top/bottom classes','reason':'This is a recoloring of the same tested cut-edge information, without a sufficiently independent new correspondence; not used to restart the failed input.'},
     {'hypothesis':'Add large dots on V tips, new guides or rendered fold/visibility style changes','reason':'Fixed 50pt2 dots would cover the diagnostic notch tips; new guides can be read as additional cuts, and changing the boundary into a fold changes the shape interpretation. No useful concise unambiguous design selected.'}],
   'mathematical_basis':'Two cutting support lines in the once-folded half cannot make the four distinct D support lines. A/B/C/E have explicit two-cut witnesses. This is not a claim that no possible Special could ever work.'},
 'Solid174':{
   'unique_answer':'D',
   'uncompleted_reason':'The independent scissors-containing formal question was tested separately and returned C/D against E. The uncut packet still provides no particular cut to bind; coloring tool blades into given cutting directions would invent restrictions. No further material, semantically valid correspondence found.',
   'considered_and_rejected':[
     {'hypothesis':'Treat illustrated scissors blades as specified cut directions','reason':'The scissors are a motion/tool symbol. Their current position does not specify the two allowed free straight cuts.'},
     {'hypothesis':'Borrow Solid146 outcome or image evidence','reason':'Different formal question and source image. Evidence must remain separate; neither result can be transferred or pooled.'},
     {'hypothesis':'Possible-option edge coloring or D palette/width/partition changes','reason':'The same literal-color ambiguity and non-material retry issues as Solid146 apply. No extra calls made.'}],
   'mathematical_basis':'Separate one-fold support-line argument and explicit constructions retained. The source scissors do not change the line-count invariant.'},
 'Solid239':{
   'unique_answer':'E',
   'uncompleted_reason':'The new cut-to-border-notch image returned C/E against B; the endpoint-to-four-border-orbits image returned D/A against A. Neither yielded two preset hits. The other geometrically distinct wrong-hole classes already have protected old D and C failed images. No new valid cut/crease/endpoint relation remained beyond these inspected classes.',
   'considered_and_rejected':[
     {'hypothesis':'Central triangular D by stopping after one unfold','reason':'Already a protected old D-preset design with full E/E responses. Its original image must not be retried or merely re-tinted.'},
     {'hypothesis':'Axis-aligned square C from crease directions','reason':'Already a protected old C-preset design with full E/E responses. Cut slopes remain diagonal and creases cannot become cut boundaries.'},
     {'hypothesis':'Move an endpoint, remove a layer/band, add a second cut or recolor reverse-side bands','reason':'Would change the given cut, four-layer state, visibility or categorical paper-side content.'},
     {'hypothesis':'Select the single A final from the new endpoint design or relabel to D','reason':'Frozen preset A must be hit twice on that one image. D/A is a failed pair; no third call, selection or preset change.'}],
   'mathematical_basis':'Four reflections of the removed corner triangle give exactly one strictly internal diamond; its boundary slopes exclude C, symmetry excludes D and interior location excludes A/B.'},
 'Plane220':{
   'unique_answer':'D',
   'uncompleted_reason':'Three new useful comparison hypotheses were separately frozen and each received exactly two complete calls: nested completion duplication B/E against E; near-tangent contact B/D against B; false mirror-extremity pair E/E against C. No paired preset hit exists. The final repeated wrong E cannot be relabeled to qualify.',
   'considered_and_rejected':[
     {'hypothesis':'Source arc/star copying to C or disconnected raw copies A','reason':'The two protected old images already failed A/C against C and E/A against A. They cannot be resumed. Source colored contours also raise the explicit paper-ink ambiguity from the lessons.'},
     {'hypothesis':'Another B-versus-A direction swap, or exchange inner/outer/left/right colors in the tested E image','reason':'Only an option/partition/palette substitution in an already examined relation, not a new informative correspondence.'},
     {'hypothesis':'New seam, bridging line, second fold, source-edge ink or extra tip dots','reason':'Would add a cut/fold, turn point contact into a real connection, create intrinsic source content absent in D, or obscure diagnostic small tips.'},
     {'hypothesis':'Reuse the E/E output with an E preset','reason':'The immutable preset of that image is C. Both wrong E finals remain zero target hits. A separate E-preset image already failed its pair and cannot supply a second E.'}],
   'mathematical_basis':'The source half-opening joins the fold on a positive interval; reflection creates one connected double-zigzag opening D. A/B/E have distinct interiors and C is asymmetric. Fold-side exhaustion is explicitly recorded in mathematics_fold_side_exhaustion.json.'}
}

source_checks={};old_preservation=[]
for q in assignment['questions']:
    qid=q['question_id']
    eligibility=check_eligibility(qid,'end_of_assigned_research')
    save(OWN/qid/'eligibility_end.json',eligibility,True)
    assert eligibility['eligible'],eligibility['reasons']
    evidence=read_json(OWN/qid/'history_files_read.json')
    for f in evidence:
        current=sha(PROJECT/f['path']);assert current==f['sha256'], f['path']
        old_preservation.append({'path':f['path'],'sha256':current})
    assessment={'question_id':qid,'assessed_at':now(),'status':'UNFINISHED_NO_QUALIFIED_PRIMARY',
      **reasons[qid],'new_attempts':[x for x in results if x['question_id']==qid],
      'current_eligible':True,'input_hold':False,'all_saved_old_raws_read_in_full':True,
      'new_all_raws_manually_read_in_full':True,'no_quota_saving_stop':True,'no_three_candidate_stop':True,
      'claim_limit':'No theorem that all future Special designs are impossible. These concrete hypotheses failed; no further credible, materially different correspondence was identified under the stated gates.',
      'no_Pass_Collect_delivery_or_second_review':True}
    save(OWN/qid/'refinement_assessment.json',assessment,True)
    source_checks[qid]={'frozen_source_files_sha256':eligibility['source_sha256'],'approval_content_sha256':eligibility['current_content_sha256'],
                        'eligible':True,'formal_record_equal_assignment':True}

refchecks=[]
for reference in read_json(OWN/'reference_read_inventory.json'):
    for f in reference['all_files']:
        assert sha(f['path'])==f['sha256']
        refchecks.append(f)
start=read_json(OWN/'source_start.json')
for path,expected in start['assignment_brief_original_hashes'].items(): assert sha(path)==expected
source_hashes={}
for branch in ['PlaneGeometry','SolidGeometry']:
    for leaf in ['render_plugins.py','renderer_adapter.py','workbench_io.py','partial_style.py','drawing_board.py','plugin.schema.json','quick_test.py','config.json']:
        path=PROJECT/branch/'workbench'/leaf
        source_hashes[str(path)]=sha(path)
    if branch=='PlaneGeometry':
        for leaf in ['mathvision_adapter.py','mathvision_plugins.py']:
            path=PROJECT/branch/'workbench'/leaf;source_hashes[str(path)]=sha(path)
for path in [OLD/'runtime_isolation.py',OLD/'delivery_bridge_adapter.py',OLD/'harness/quicktest3_isolated.py',PROJECT/'dataset_tools/mathvision_workbench.py']:
    source_hashes[str(path)]=sha(path)
save(OWN/'source_preservation_end.json',{'checked_at':now(),'questions':source_checks,'reference_files_unchanged':refchecks,
  'old_evidence_files_unchanged':old_preservation,'assignment_brief_unchanged':start['assignment_brief_original_hashes'],
  'executor_fingerprints_observed_at_end':source_hashes,'formal_sources_and_old_evidence_modified_by_this_unit':False,
  'preexisting_root_runtime_others_dotruntime_env_git_kept_readonly':True,
  'metadata_policy':'Parent progress/brief metadata was not restored or treated as geometry drift.'},True)

# Query only this unit's Python processes. The synchronous read-only PowerShell child exits here.
command="$u06Processes = Get-CimInstance Win32_Process -Filter \"Name = 'python.exe'\" | Where-Object { $_.CommandLine -like '*u06_fold_cut*' }; @($u06Processes | Select-Object ProcessId,ParentProcessId,CommandLine) | ConvertTo-Json -Compress"
child=subprocess.Popen(['powershell.exe','-NoLogo','-NoProfile','-NonInteractive','-Command',command],
    stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
stdout,stderr=child.communicate(timeout=30)
assert child.returncode==0, stderr
processes=json.loads(stdout) if stdout.strip() else []
if isinstance(processes,dict):processes=[processes]
other_processes=[p for p in processes if p['ProcessId']!=os.getpid()]
assert not other_processes, other_processes
processes_finished=[read_json(Path(e['candidate_directory'])/'api_process_finished.json') for e in entries]
save(OWN/'own_process_cleanup.json',{'checked_at':now(),'all_tracked_api_invocations_finished':processes_finished,
  'active_own_python_processes_except_this_final_auditor':other_processes,'final_auditor_pid':os.getpid(),
  'process_query_child_pid':child.pid,'process_query_child_exit_code':child.returncode,
  'no_server_subagent_or_worktree_started':True,'no_other_units_processes_stopped':True,
  'matplotlib_captures_closed_in_finally':True,'final_auditor_ends_normally_after_writing_report':True},True)

diagnostics=[str(OWN/'Solid146/diagnostics/context_serialization_01/error.json'),
 str(OWN/'Solid146/diagnostics/context_serialization_02/error.json'),str(OWN/'diagnostics/generic_validator_inapplicability.json')]
lessons=[]
for rel in ['annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json',
 'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
 'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']:
    p=OLD/rel;d=read_json(p)
    lessons.append({'path':str(p),'sha256':sha(p),'decision':d.get('decision'),'reason':d.get('reason',d.get('blocking_reason',d.get('rule'))),
      'concrete_objections':d.get('concrete_objections',[])})
save(OWN/'semantics_lessons_read.json',{'lessons':lessons,
  'applied':'Never assume colored source paper edging disappears. New source styling is restricted to the explicit cut instruction in Solid239; all Plane220 source paper contours remain untouched. Literal-reading answer preservation is addressed per design.',
  'supplemental_old_four_candidate_PNGs_viewed_at_end':True,
  'old_evidence_jsons_and_request_image_bytes_read_before_new_designs':True},True)

report={'unit_id':'u06_fold_cut','finished_at':now(),'status':'RESEARCH_ENDED_WITH_FOUR_UNFINISHED_SPECIALS',
 'assigned_question_ids':assignment['question_ids'],'assigned_all_assessed':True,'all_requested_qualified_Specials_achieved':False,
 'new_design_count':len(entries),'new_actual_request_count':len(all_api),'new_complete_response_count':len(all_api),
 'API_errors':0,'aborted_requests':0,'truncated_responses':0,'untested_frozen_candidates':[],
 'qualified_PRIMARY_candidates':[],'second_review_queue':str(OWN/'second_review_queue.json'),
 'unworked_question_ids':[],'unfinished_question_ids':assignment['question_ids'],'input_holds':[],
 'candidate_results':results,'all_actual_calls':all_api,
 'unfinished_reasons':{qid:v['uncompleted_reason'] for qid,v in reasons.items()},
 'per_question_refinement_assessments':{qid:str(OWN/qid/'refinement_assessment.json') for qid in assignment['question_ids']},
 'local_audit_command_errors_corrected_and_preserved':diagnostics,
 'all_offline_gates_passed_for_each_tested_image':['fresh schema/default normalization','formal no-op pixel equality','repeat candidate PNG byte equality','fresh independent process exact context/path/PNG replay'],
 'original_harness_routing_provenance':str(OWN/'ownruntime/harness/routing_provenance.json'),
 'source_preservation':str(OWN/'source_preservation_end.json'),'process_cleanup':str(OWN/'own_process_cleanup.json'),
 'constraints_observed':{'writes_only_own_root':True,'Python_B_and_four_numeric_thread_envs_one':True,
   'exact_two_per_frozen_image':True,'no_postoutput_preset_change':True,'no_failed_old_image_retest':True,
   'all_complete_raws_manually_read':True,'no_controls_ping_or_extra_provider_calls':True,
   'no_user_Pass_Collect_second_review_or_delivery_claim':True,'old457_general_exploration_still_paused':True},
 'interpretation_limit':'Repeated wrong answers on a different preset do not qualify. In particular Plane220 false_mirror_extremity_pair produced E/E against C and remains a failed design. No aggregate efficacy or causal claim.',
 'parent_handoff':'No candidate to send to a new independent second reviewer. All four requested Specials remain unfinished for the documented concrete reasons; retain every frozen attempt and raw response.'}
save(OWN/'research_report.json',report,True)
save(OWN/'checkpoint.json',{'unit_id':'u06_fold_cut','updated_at':now(),'phase':'RESEARCH_ENDED_NO_QUALIFIED_PRIMARY',
 'new_actual_calls':14,'new_complete_responses':14,'new_designs':7,'qualified_PRIMARY_count':0,
 'questions':{qid:{'status':'UNFINISHED_NO_QUALIFIED_PRIMARY','calls':sum(x['actual_requests'] for x in results if x['question_id']==qid),
   'attempts':[x for x in results if x['question_id']==qid],'unfinished_reason':reasons[qid]['uncompleted_reason'],
   'assessment':str(OWN/qid/'refinement_assessment.json'),'current_eligible':True} for qid in assignment['question_ids']},
 'second_review_queue_empty':True,'API_errors':0,'aborted':0,'unworked':[],
 'local_diagnostics':diagnostics,'source_preservation':str(OWN/'source_preservation_end.json'),
 'process_cleanup':str(OWN/'own_process_cleanup.json'),'formal_changes':False,
 'no_subagents_servers_worktrees':True,'all_requested_qualified_Specials_achieved':False})
save(OWN/'second_review_queue.json',[])
hashes={str(p.relative_to(OWN)):sha(p) for p in OWN.rglob('*') if p.is_file() and 'ownruntime' not in p.relative_to(OWN).parts and p.name!='immutable_evidence_sha256.json'}
hashes['ownruntime/harness/quicktest3_isolated.py']=sha(OWN/'ownruntime/harness/quicktest3_isolated.py')
hashes['ownruntime/harness/routing_provenance.json']=sha(OWN/'ownruntime/harness/routing_provenance.json')
hashes['ownruntime/harness/routing.diff']=sha(OWN/'ownruntime/harness/routing.diff')
save(OWN/'immutable_evidence_sha256.json',{'created_at':now(),'files':hashes,'excluded':'runtime caches and this self-referential manifest only'},True)
print(json.dumps({'report':str(OWN/'research_report.json'),'new_designs':7,'new_actual_calls':14,
 'complete_responses':14,'qualified_PRIMARY':0,'queue':[],'active_api_or_render_processes':other_processes,
 'per_question':{q:{'attempts':len([x for x in results if x['question_id']==q]),'finals':[x['manual_finals'] for x in results if x['question_id']==q]} for q in assignment['question_ids']}},ensure_ascii=False,indent=2))
