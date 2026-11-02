from review_bootstrap import *

def run():
    proof=load(OWN/'independent_math.json')
    replay=load(OWN/'exact_replay.json')
    transport=load(OWN/'candidate_transport_audit.json')
    all_trials=load(OWN/'all_twelve_trial_transport_audit.json')['trials']
    eligibility=load(OWN/'current_eligibility.json')
    old_checks=load(OWN/'old_evidence_preservation.json')
    initial=load(OWN/'scoped_preservation_initial.json')
    unchanged={p:{'before_sha256':h,'after_sha256':sha(p)} for p,h in initial['sha256'].items()}
    changed={p:v for p,v in unchanged.items() if v['before_sha256']!=v['after_sha256']}
    # Parent progress metadata can change without changing any frozen source.
    diagnostic_paths={str(TASK/p) for p in ('parent_review_preflight.json','parent_imitation_priority_20261102.txt')}
    source_changes={p:v for p,v in changed.items() if p not in diagnostic_paths}
    assert not source_changes
    assert sha(TASK/'references/Solid203/C01.png')==sha(PROJECT/'SolidGeometry/special_variant/Solid203/images/C01.png')
    assert sha(TASK/'references/Solid203/C01.json')==sha(PROJECT/'SolidGeometry/special_variant/Solid203/plugins/C01.json')
    # Recompute eligibility at report completion; no catalog/state writers.
    from dataset_tools import catalog
    record=next(r for r in catalog.rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid166')
    approval=load(PROJECT/'provenance/approvals.json')['approvals']['Solid166']
    fingerprint=catalog.digest(catalog.content(PROJECT,'SolidGeometry',record))
    assert canonical(record)==canonical(eligibility['formal_record'])
    assert canonical(approval)==canonical(eligibility['approval'])
    assert fingerprint==approval['content_sha256']==eligibility['recomputed_content_sha256']
    special=PROJECT/'SolidGeometry/special_variant'
    current_status={f:[r for r in catalog.rows(special/f) if r.get('question_id',r.get('id'))=='Solid166'] for f in ('accepted_index.jsonl','collected_index.jsonl')}
    for f in ('recipes.json','collection.json'):
        p=special/'Solid166'/f
        current_status[f]=load(p) if p.exists() else None
    assert not any(current_status.values())
    from PIL import Image, ImageChops
    with Image.open(PROJECT/'SolidGeometry/image/Solid166.png') as formal, Image.open(CANDIDATE/'candidate.png') as candidate:
        a=formal.convert('RGB'); b=candidate.convert('RGB')
        diff=ImageChops.difference(a,b)
        bbox=diff.getbbox()
        assert a.crop((420,0,768,768)).tobytes()==b.crop((420,0,768,768)).tobytes()
        changed_pixels=sum(x!=y for x,y in zip(a.getdata(),b.getdata()))
    save('scoped_preservation_final.json',{'checked_at':now(),'initial_snapshot_sha256':sha(OWN/'scoped_preservation_initial.json'),
       'checks':unchanged,'frozen_source_changes':source_changes,'mutable_parent_diagnostics':{p:v for p,v in changed.items() if p in diagnostic_paths},
       'old_source_reference_preservation_report':str(OWN/'old_evidence_preservation.json'),
       'all_76_preexisting_read_manifest_files_match':old_checks['all_match'],
       'current_formal_fingerprint':fingerprint,'current_target_special_status':current_status,
       'whole_workspace_unchanged_claimed':False,'source_or_old_evidence_restored':False})
    facts={
      'netedge15':('red','x, lower flap right side','netedge2','Query boundary for the concrete x-versus4 comparison. Its genuine mate is printed5; the annotation does not assert equality.'),
      'netedge2':('red','printed4, far-left sloping side','netedge15','Specific proposed receiving boundary for x; it shares only one folded endpoint with x. It is paired with the query rather than an isolated highlighted answer.'),
      'netedge13':('blue','printed3, upper flap left side','netedge9','One free side of the upper flap, tracked to its exact strip receiving side printed2.'),
      'netedge9':('blue','printed2, right upper strip boundary','netedge13','Receiving side for printed3; marks one true upper flap closure and orients the strip relative to that flap.'),
      'netedge5':('green','middle upper horizontal boundary','netedge14','Receiving side for the upper flap other free side; distinguishes it from the adjacent blue horizontal boundary.'),
      'netedge14':('green','upper flap right side','netedge5','Tracks the upper flap second free side. Blue and green together identify both of its actual closure sides, rather than coloring its whole face.'),
      'netedge8':('orange','middle lower horizontal boundary','netedge16','Receiving side for the lower flap left side, introducing a lower closure reference distinct from the upper blue/green closures.'),
      'netedge16':('orange','lower flap left side','netedge8','Tracks the lower flap non-query free side, locating the neighboring closure to x without adding an edge or a cut.')}
    actions=load(CANDIDATE/'plugin.json')['params']['actions']
    marks=[]
    for i,a in enumerate(actions):
        e=a['target'];color,location,pair,role=facts[e]
        assert set(a)=={'type','target','color'}
        marks.append({'action_index':i,'target':e,'color_name':color,'color_hex':a['color'],
          'actual_native_location':location,'comparison_partner':pair,'specific_information_role':role,
          'folded_endpoint_signature':proof['all_edge_signatures'][e],
          'pair_is_actual_seam':proof['all_edge_signatures'][e]==proof['all_edge_signatures'][pair],
          'full_original_object':True,'interval':None,'original_solid_line_and_1pt_width_retained':True,
          'legal_schema_and_exact_replay':'passed','visually_readable_at_768':True,
          'overwritten_or_useless_action':False,'causal_necessity_demonstrated':False})
    manual_finals=[['1','4'],['UNRESOLVED_NO_EDGE_IDENTIFIER','1'],['AMBIGUOUS_1_OR_2','2'],['3','4'],['3','3'],['2','5'],['2','1'],['4','3'],['3','5'],['5','OTHER_PAIR_1_MEETS_3'],['MULTIPLE_2_AND_5','4'],['4','4']]
    history=[]
    for t,finals in zip(all_trials,manual_finals):
        history.append({k:t[k] for k in ('variant_id','preset','PNG_sha256','plugin_sha256','design_sha256','summary_sha256','request_sha256')})
        history[-1].update(final_readings=finals,paired_preset_hit=all(x==t['preset'] for x in finals),
            raw_response_sha256=[r['raw_sha256'] for r in t['runs']],all_transport_exact=True,
            original_evidence_unchanged=True,manual_prior_final_scope='r12 and closest r08/r10/r11 complete raw personally read; other prior final classifications checked against full saved manual reviews and parent objections; not relabelled')
    assert sum(h['paired_preset_hit'] for h in history)==1 and history[-1]['paired_preset_hit']
    finals=[]
    divergences=[
      'Miscounts/locates the strip using five main triangles and invents a strip-end closure. Its reference to printed5 is not a correct x-to5 proof. The final unequivocally chooses printed4.',
      'Explicitly notices the two red edges, assigns them to opposite north/south poles, then treats meeting at one front vertex as an entire joining seam. Distinct pole endpoints cannot coincide to make the same edge. It unequivocally concludes4.']
    for r,divergence in zip(transport['runs'],divergences):
        finals.append({**r,'personally_read_entire_original_raw_JSON_and_entire_final_content':True,
           'final_value':'4','final_letter':None,'printed_edge_identifier_not_option_letter':True,
           'exact_frozen_preset_match':True,'final_letter_value_conflict':False,
           'actual_reasoning_divergence':divergence,'context_group_uptake_demonstrated':False})
    errors=sorted(p.name for p in OWN.glob('offline_error_*.json'))
    report={
      'decision':'recommended','review_role':'NEW independent SECOND REVIEW of exactly one existing frozen candidate',
      'reviewed_at_utc':now(),'question_id':'Solid166','variant_id':'r12_full_seam_context_x_four',
      'candidate_directory':str(CANDIDATE),'candidate_directory_binding_exact':True,
      'own_output_root':str(OWN),'candidate_PNG_path':str(CANDIDATE/'candidate.png'),
      'image_sha256':sha(CANDIDATE/'candidate.png'),'pixel_sha256':replay['candidate_pixel_sha256'],
      'plugin_sha256':sha(CANDIDATE/'plugin.json'),'design_sha256':sha(CANDIDATE/'design.json'),
      'summary_path':str(Path(transport['runs'][0]['raw_path']).parent/'summary.json'),
      'summary_sha256':transport['summary_sha256'],'request_sha256':transport['request_sha256'],
      'binding_sha256':transport['binding_sha256'],'design_snapshot_sha256':transport['design_snapshot_sha256'],
      'candidate_directory_binding_sha256':hashlib.sha256(str(CANDIDATE).encode('utf-8')).hexdigest(),
      'frozen_wrong_preset':{'letter':None,'value':'4','meaning':'Printed original boundary identifier4'},
      'freeze_created_at_utc':transport['frozen_at'],'request_binding_created_at_utc':transport['binding_at'],
      'independently_derived_original_answer':'5',
      'recommendation_reason':'The exact candidate preserves the uniquely determined geometric x-to5 seam and readable original structure, uses legal color-only comparisons of eight actual free boundaries with three proved contextual seams, and its only two saved complete calls both finish with the original numeric wrong preset4. It is an extension of the current two-edge method, with stated simplicity and causal limits.',
      'authority':'Research recommendation only. No original-question approval, Special Pass, Collect, publication or authorization for further exploration.',
      'protocols_read':{'AGENTS.md':sha(PROJECT/'AGENTS.md'),'root_protocol':sha(PROJECT/'MATHPALETTE_PROTOCOL.md'),
         'solid_redraw':sha(PROJECT/'SolidGeometry/REDRAW_PROTOCOL.md'),'machine_protocol':sha(PROJECT/'SolidGeometry/dataset_generator/protocol.json'),
         'workbench_README':sha(PROJECT/'SolidGeometry/workbench/README.md'),'agent_prompt':sha(PROJECT/'SolidGeometry/workbench/agent_prompt.md'),
         'plugin_schema':sha(PROJECT/'SolidGeometry/workbench/plugin.schema.json'),'task':sha(TASK/'task.json'),
         'reference_style_summary':sha(TASK/'reference_style_summary.json'),'latest_user_steering':sha(TASK/'parent_imitation_priority_20261102.txt')},
      'reference':{'question_id':'Solid203','current_C01_native_image_personally_viewed':True,
         'complete_plugin_personally_read':True,'live_current_files_equal_task_reference_bytes':True,
         'image_sha256':sha(TASK/'references/Solid203/C01.png'),'plugin_sha256':sha(TASK/'references/Solid203/C01.json'),
         'actual_method':'Only original x and upper-left C boundaries red; other boundaries/labels and right solid unchanged.',
         'old18_option_A_used':False,'cross_ID_transfer_authority':'Explicit current9-to24 task instruction; this does not make cross-ID images the same formal request.'},
      'method_fidelity':{'classification':'extension','close_imitation':False,'too_distant':False,
         'reason':'Retains the same two-existing-boundary color comparison primitive, line width and unchanged geometry. The red x–4 comparison is the direct analogue. Three additional source/receiver seam pairs supply concrete closure context, expanding one pair/two edges to four pairs/eight edges. This is materially broader than current Solid203 C01 and must not be described as a minimal copy.',
         'latest_preference_assessment':'Acceptable existing extension for research recommendation, with visible useful context and no added dots/lines/cuts. Twelve completed trials and earlier endpoint departures are retained as history, not endorsed as an exploration plan. No further attempts are recommended or authorized.',
         'conciseness':'Each selected edge belongs to one concrete pair; no orphan mark, repeated style, decoration, width inflation or useless overwritten action. Both upper flap sides and the other lower flap side can be traced. The information roles justify their presence, but global minimality and individual necessity are not established.',
         'no_arbitrary_count_cap':True},
      'original_mathematical_proof':proof,
      'world_projection_visibility':load(OWN/'world_projection_visibility.json'),
      'per_marker_information_legal_human_review':marks,
      'native_visual_review':{'personally_viewed_at_original_resolution':[
        str(TASK/'references/Solid203/C01.png'),str(PROJECT/'SolidGeometry/originals/Solid166.jpg'),
        str(PROJECT/'SolidGeometry/image/Solid166.png'),str(CANDIDATE/'candidate.png'),
        *[str(UNIT/'Solid166'/n/'candidate.png') for n in ('r08_four_with_true_three_two','r10_three_with_true_one_four','r11_one_with_true_three_two')]],
        'all_8_faces_17_net_segments_12_display_solid_edges_and_6_labels_checked':True,
        'colors':'Red/blue/green/orange distinguish the four pairs on native768. Red and orange meet at the lower apex but remain distinguishable along their full sloping sides. Upper green/blue horizontal segments join at an original vertex; they do not create a new vertex.',
        'text':'All original1,2,3,4,5,x labels stay black and unambiguous, away from the colored edges; no labels moved or hidden.',
        'original_linework':'Internal folds and unmarked printed1/5 boundaries remain black solid; all 4 display-solid hidden edges remain dashed and all 8 visible edges solid. No partial interval, marker dot, endpoint object, cut, new crease, closed fake partition or overlay outside existing boundaries.',
        'fill_correction':'The JPG has uniform gray paper shading, while both the approved formal PNG and candidate visibly have white triangle interiors. Frozen scene objects have semantic_fill_reason strings but no rendered gray facecolor. Therefore primary statements implying visible gray preservation are too broad. This inherited uniform-fill omission encodes no distinction among faces and does not change net incidence, labels or unique seam; r12 introduces no fill change. No source edit or repair is performed.',
        'pixel_difference_bbox':bbox,'changed_RGB_pixels_against_formal':changed_pixels,
        'right_solid_region_exact_pixel_equality':True,'no_line_width_or_visibility_override':True},
      'human_and_literal_paper_semantics':{
        'annotation_reading':'Colors ask the reader to compare actual boundary segments; the red comparison is false as an asserted seam, while the other three are true. Same color is not a given equality or a binding seam rule.',
        'literal_ink_reading':'If these strokes are literally ink on the physical sheet, they remain attached to those existing edges. Folding a colored edge against an edge of another color is allowed; neither the words nor a result-picture option imposes color matching. The physical octahedron still has x–5 as its only coincident numbered seam.',
        'printed_pattern_distinction':'There is no original colored printed pattern, picture-selection matching condition, added instruction or legend. Imposing same-color edges must join would be an invented inconsistent extra rule, not a reasonable literal ink requirement in this formal question. The contextual true pairs can tempt that mistaken inference; they do not make it a mathematical condition.',
        'meaning_of_meets':'Read as coinciding as a full edge during net closure. Several labeled edges touch x at vertices under a broad contact reading even before annotations; this inherited terminology is resolved by the conventional net question and unique seam geometry. Annotation does not introduce or increase this ambiguity.',
        'original_unique_interpretation_preserved':True},
      'actual_complete_final_readings':finals,
      'frozen_transport_and_integrity':{
        'exactly_two_actual_complete_nontruncated_saved_quicktest3_calls':True,
        'profile':'quicktest3','provider':'mimo','model':'mimo-v2.6-flash','thinking':{'type':'disabled'},
        'request_content':'Exact configured system plus one user message containing only exact formal question and frozen candidatePNG; no answer, intent, design, original image or history.',
        'request_byte_comparison':True,'preset_timestamp_precedes_both_starts':True,
        'exact_PNG_plugin_design_snapshot_request_binding_raw_summary_queue_hash_checks':True,
        'all_twelve_transport_report':str(OWN/'all_twelve_trial_transport_audit.json'),
        'candidate_transport_report':str(OWN/'candidate_transport_audit.json'),
        'no_extra_r12_binding_found_across_task_and_old_root':True,
        'limitation':'Saved evidence supports two calls with no recorded third call/retry; local artifacts cannot prove the absence of arbitrary external unrecorded activity.'},
      'history_and_process_objections':{
        'history_index_sha256':sha(TASK/'history_index.json'),'current_attempt_count':12,'current_call_count':24,
        'current_complete_call_count':24,'current_API_errors_or_aborts_found':0,
        'old_unique_tested_image':{'sha256':'a31f8ad7700db30b4a1aa2da041c1cb14c70eb7e96a4ac27717101db14762dd4',
           'preset':'1','finals':['3','4'],'unique_calls':2,'aliases_not_additional_calls':True,'remains_failed_and_not_retested':True},
        'all_current_presets_images_raw_hashes_and_failures':history,
        'r08_vs_r12':'Same exact red x–4 and blue3–2 comparisons. r12 adds green netedge5–14 and orange netedge8–16, respectively the upper flap other closure and lower flap non-query closure. Both are proved real geometrical pairings and visibly introduce missing orientation/closure comparisons. This is a material information change, not a palette/width/filename-only repeat of r08.',
        'r10_vs_r12':'r10 compares x–3 in red and true1–4 in blue. r12 changes the compared receiver to4, changes the numbered context to true3–2, and adds the two flap closure groups. These are different actual endpoints, not just relabelled option letters.',
        'r11_vs_r12':'r11 red x–1 with same blue3–2 context. r12 changes receiver1 to4 and adds green/orange closures. r11 final2and5/4 remains an unsuccessful preset1 trial.',
        'preceding_partial_hit_preserved':'r08 preset4 observed4/3 remains a miss; its single hit is not counted toward r12. r05 observed3/3 with frozen preset4 remains a miss, not a success after relabelling.',
        'test_selection_objection':'r12 was selected after eleven unsuccessful variants. The changed seam information permits reviewing the distinct frozen image, but adaptive design selection prevents treating4/4 as a general success rate or causal evidence. No statistical or mechanism validation is inferred.',
        'endpoint_departures':'r05–r07 and r09 added original-vertex endpoint dots. They are more distant from current Solid203 C01 and remain unsuccessful history; r12 uses none.',
        'parent_audits_read_as_objections':{'audit_json':sha(TASK/'parent_audits/native_u09/audit.json'),
          'method_fidelity_json':sha(TASK/'parent_audits/native_u09/method_fidelity.json'),
          'accepted_objections':['Reference is x/C, not oldA.','r12 is materially broader than two red edges.','r08 partial hit remains failure.','Model prose does not validate green/orange roles.','No proven individual necessity or causal gain.']},
        'Solid240_hold':'Background only; not investigated, repaired or tested in this assignment.'},
      'fresh_exact_offline_replay':replay,
      'current_eligibility':{**eligibility,'rechecked_at_report_completion':now(),
         'final_recomputed_content_sha256':fingerprint,'final_target_special_status':current_status},
      'concrete_objections_and_corrections':[
        {'issue':'Imitation breadth','assessment':'Extension, not close imitation. Eight edge strokes carry four comparisons; no necessity/minimality claim. Existing candidate is acceptable on concrete role/clarity grounds, without approving the twelve-trial research breadth.'},
        {'issue':'Model mechanism claim','assessment':'Run1 invents strip closure. Run2 conflates vertex contact and a coincident seam despite its opposite-pole account. Neither explains the new green/orange pair roles. Their errors support the two observed final4 values only.'},
        {'issue':'Uniform source gray','assessment':'SourceJPG gray shading is absent from the current formalPNG and candidate. Corrected primary overstatement in this own report; uniform shading has no face-pattern role or effect on the unique seam, and no new fill omission is attributable to r12.'},
        {'issue':'Colored seam matching temptation','assessment':'Three correct context pairs may encourage accepting false red pairing; literal colored paper has no color-matching condition. Full-edge geometry, not color identity, decides5.'},
        {'issue':'Own offline path error','assessment':'An initial read omitted SolidGeometry from the branch-relative scene path. The original traceback was preserved, only this review helper path was corrected, and the complete replay/proof then passed. No source or numeric comparison was weakened.','preserved_files':errors}],
      'unresolved_blocking_objections':[],
      'limitations':[
         'Two observed same-PNG final4 answers do not estimate a general rate, reliable mechanism, causal/statistical gain or individual marker necessity.',
         'No new control is required or run. Existing controls could also be wrong; this recommendation is based on independent geometry, readable targeted marks and exact two-call frozen evidence.',
         'Color discrimination assessment is a personal native-resolution visual review, not a universal accessibility claim.',
         'No claim that sourceJPG and approved formalPNG are pixel-identical; no-op replay checks the formalPNG pixels, while candidate replay is byte-identical.',
         'Scoped formal sources, old/current evidence and live current reference were checked; unrelated user updates and whole-workspace immutability are not claimed.'],
      'source_preservation':{'scoped_file_count':len(unchanged),'scoped_frozen_changes':source_changes,
        'old_read_manifest_file_count':len(old_checks['checks']),'old_read_manifest_all_match':True,
        'report_path':str(OWN/'scoped_preservation_final.json'),'whole_workspace_unchanged_claimed':False,
        'primary_or_old_sources_corrected':False},
      'process_closure':{'new_solver_API_calls':0,'new_designs':0,'child_agents':0,'workbench_server_or_state_changes':0,
        'original_approvals_Pass_Collect_publication':0,'provider_model_switch':False,
        'all_Python_B':True,'strict_own_writeguard_before_project_numeric_imports':True,
        'own_thread_env_all_1':True,'own_cache_TEMP':True,'subprocess_and_network_denied_by_own_python_guard':True,
        'foreground_tools_only':True,'owned_background_processes_started':0,
        'final_external_process_snapshot':str(OWN/'process_closure.json'),
        'all_output_files_beneath_own_review_root':True},
      'own_audit_support_file_hashes':{p.name:sha(p) for p in OWN.glob('*.json') if p.name!='independent_review.json'}
    }
    save('independent_review.json',report)
    print(canonical({'decision':report['decision'],'method_fidelity':'extension','math_answer':'5',
      'two_complete_final_values':['4','4'],'source_files_checked':len(unchanged),'old_files_checked':len(old_checks['checks']),
      'own_errors_preserved':errors,'report':str(OWN/'independent_review.json')}))

if __name__=='__main__': main(run)
