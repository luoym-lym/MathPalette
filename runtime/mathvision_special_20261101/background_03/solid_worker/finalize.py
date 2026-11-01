from pathlib import Path
import sys
source=Path(__file__).with_name('prepare.py').read_text(encoding='utf-8').split('\nfor qid in sys.argv[1:]')[0]
exec(compile(source,str(Path(__file__).with_name('prepare.py')),'exec'))
import base64
from datetime import datetime,timezone
manual=[
 ('Solid166','bridge_terminal_edge_pair',['3','4'],'reject_preset_miss'),
 ('Solid203','bridge_terminal_edge_pair',['A','A'],'possible_candidate_pending_NEW_independent_second_review'),
 ('Solid120','false_tick_correspondence',['37','50'],'reject_preset_miss'),
 ('Solid120','false_tick_chain_v2',['48','48'],'reject_preset_miss'),
 ('Solid120','false_tick_nodes_v3',['48','48'],'reject_preset_miss'),
 ('Solid138','false_tick_correspondence',['64','50'],'reject_preset_miss'),
 ('Solid138','false_tick_chain_v2',['72','70.5'],'reject_preset_miss'),
 ('Solid138','false_tick_nodes_v3',['17','22'],'reject_preset_miss'),
 ('Solid227','linear_radius_volume_pair',['E','B'],'reject_preset_miss')
]
solutions={
 'Solid166':'Octahedron antipodal basis propagation yields x={e3,-e1}=edge5 uniquely; all8 folded faces distinct. Exact proof file retained.',
 'Solid203':'Octahedron antipodal basis propagation yields x={e3,-e1}=edgeE uniquely; all8 folded faces distinct. Exact proof file retained.',
 'Solid120':'One full turn advances27-6=21, confirmed by22-1=21 and32-11=21. The question is two turns above6, giving48.',
 'Solid138':'One full turn advances27-6=21, confirmed by22-1=21 and32-11=21. The question is three turns above6, giving69.',
 'Solid227':'With V=πr²h, volume ratios of A,B,C,D to the given cylinder are4,2,1/2,8. B is uniquely twice the reference volume. The common radius/diameter convention would not change these ratios.'
}
results=[];checks=[]
for qid,name,finals,decision in manual:
    dst=TASK/qid/name;design=json.loads((dst/'design.json').read_text(encoding='utf-8-sig'));plugin=json.loads((dst/'plugin.json').read_text(encoding='utf-8-sig'))
    reports=list((dst/'tests').glob('*/summary.json'));assert len(reports)==1
    summary=json.loads(reports[0].read_text(encoding='utf-8-sig'));evidence=reports[0].parent
    assert summary['two_completed'] and len(summary['results'])==2
    assert summary['image_sha256']==sha(dst/'candidate.png')
    assert summary['design_sha256']==sha(dst/'design.json')
    assert summary['expected_wrong_answer']==design['expected_wrong_answer']
    assert (evidence/'design_snapshot.json').read_bytes()==(dst/'design.json').read_bytes()
    request=json.loads((evidence/'request.json').read_text(encoding='utf-8'))
    assert set(request)=={'model','stream','thinking','messages'}
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
    assert len(request['messages'])==2 and request['messages'][0]=={'role':'system','content':summary['system_prompt']}
    content=request['messages'][1]['content'];assert request['messages'][1]['role']=='user' and len(content)==2
    assert content[0]=={'type':'text','text':adapter.records[qid]['question']}
    assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==(dst/'candidate.png').read_bytes()
    for i,r in enumerate(summary['results'],1):
        assert r['status']=='completed' and r['finish_reason']=='stop' and r['truncated'] is False
        assert r['response_sha256']==sha(evidence/f'run_{i:02d}_response.json')
        assert r['image_sha256']==sha(dst/'candidate.png') and r['design_sha256']==sha(dst/'design.json')
    render_path=dst/'replay/render_check.json' if name=='bridge_terminal_edge_pair' else dst/'render_check.json'
    report=json.loads(render_path.read_text(encoding='utf-8'))
    unchanged=adapter.frozen_inputs(qid)==report['frozen_inputs'];assert unchanged
    assert report['baseline_matches_formal'] and report['deterministic'] and report['png_sha256']==sha(dst/'candidate.png')
    if name=='bridge_terminal_edge_pair':
        copy=json.loads((dst/'prepared_copy.json').read_text(encoding='utf-8'))
        for f,h in copy['files_sha256'].items():assert sha(Path(copy['source'])/f)==h and sha(dst/f)==h
    record=adapter.records[qid]
    entry={'question_id':qid,'variant':name,'predeclared_wrong_answer':design['expected_wrong_answer'],'formal_correct_answer':record['answer'],'manually_read_final_answers':finals,'full_final_answers_manually_read':True,'decision':decision,'candidate_folder':str(dst.relative_to(TASK)),'evidence_summary':str(reports[0].relative_to(TASK)),'design_sha256':sha(dst/'design.json'),'candidate_png_sha256':sha(dst/'candidate.png'),'plugin_sha256':sha(dst/'plugin.json'),'source_dataset':record['source_dataset'],'source_key':record['source_key'],'source_revision':record.get('source_revision'),'formal_record_snapshot':str((TASK/qid/'formal_record.json').relative_to(TASK)) if (TASK/qid/'formal_record.json').exists() else str((dst/'formal_record.json').relative_to(TASK)),'mathematical_check':solutions[qid],'actual_png_viewed':True,'visual_check':'Every added/recolored mark checked on actual PNG; original labels readable and uncovered. Original question, endpoints, fills, geometry, projection and frozen visibility unchanged.','marker_roles':design.get('mechanism'),'render_report':str(render_path.relative_to(TASK)),'current_formal_input_fingerprints_unchanged':unchanged,'two_calls_same_frozen_image_and_design':True,'payload_restricted_to_formal_question_candidate_png_existing_system_prompt':True,'independent_second_review':'required; not performed by this worker'}
    if qid=='Solid203':
        controls=list((dst/'control_tests').glob('*/summary.json'));assert len(controls)==1
        cs=json.loads(controls[0].read_text(encoding='utf-8'));assert cs['two_completed']
        assert cs['image_sha256']==sha(dst/'original.png')==sha(adapter.original_paths[qid])
        entry.update(primary_review=str((dst/'primary_review.md').relative_to(TASK)),folding_verification=str((dst/'folding_verification.json').relative_to(TASK)),original_control_final_answers=['A','B'],original_control_summary=str(controls[0].relative_to(TASK)),causal_limitation='Both original controls already wrong against E. Same targetA occurs in original run1; two candidate target hits do not establish causal improvement or reliability.')
    results.append(entry);checks.append({'question_id':qid,'variant':name,'binding_hashes_verified':True,'all_formal_frozen_inputs_unchanged':True,'no_retries_or_preset_changes':True})
checkpoint={'created_at_utc':datetime.now(timezone.utc).isoformat(),'status':'finite_subset_exhausted','worker':'solid_prepared','all_outputs_under':str(TASK),'prepared_questions':['Solid166','Solid203'],'selected_new_questions':['Solid120','Solid138','Solid205','Solid212','Solid227'],'candidate_variants_tested':len(results),'candidate_api_calls':18,'original_control_api_calls':2,'valid_completed_calls_total':20,'transport_errors':[],'aborted_requests':[],'manually_read_results':results,'screened_out_before_API':json.loads((TASK/'prescreen_rejections.json').read_text(encoding='utf-8'))['questions'],'possible_candidates_for_parent_NEW_independent_review':['Solid203/bridge_terminal_edge_pair'],'pending_drafts':[],'remaining_recommendations':['Independently review Solid203 with its actual PNG, exact folding proof and A/B original-control limitation before any delivery.','Do not retest any identical failed image or combine hits from the tape variants. Solid120 andSolid138 each reached their3variant work-unit limit.','No extra question beyond the five assigned was started. Solid205 andSolid212 need a substantially different concrete information-bearing hypothesis before future calls.'],'formal_library_writes':False,'pass_collect_review_API_calls':False,'qualification_or_user_approval_claimed':False,'previous_runtime_evidence_modified':False,'verification':checks,'no_live_process_confirmation':json.loads((TASK/'no_live_processes.json').read_text(encoding='utf-8-sig'))}
write(TASK/'checkpoint.json',checkpoint)
print(json.dumps({'checkpoint':str(TASK/'checkpoint.json'),'variants':len(results),'complete_calls':20,'possible_candidates':['Solid203/bridge_terminal_edge_pair']}))
