from new_tools import *
import base64
MANUAL={
    'Plane435/v01':['2','2'],
    'Plane435/v02':['3','2'],
    'Plane425/endpoint_correspondence':['none of T,U,V,W','B'],
    'Plane313/false_hole_clock_correspondence':['A',None],
    'Plane471/three_side_chain':['D','D'],
    'Plane250/diagonal_vertical_basis':['21.5','31.25'],
    'Plane425/paired_endpoint_links':['B',None],
    'Plane425/single_endpoint_radius_trap':['B','B'],
}
reviews={
    'Plane435/v01':'Rejected: both valid final answers2 missed immutable4. Circlepair mechanism is specific but not effective at the declared target.',
    'Plane435/v02':'Rejected: valid final answers3 and2 missed immutable5. Both circle-position and handedness correspondences are targeted, but declared hypothesis failed.',
    'Plane425/endpoint_correspondence':'Rejected: one final answer says none of the centres; second says onlyU (semantically optionB). Only1/2 target hits; cannot combine with any later image.',
    'Plane313/false_hole_clock_correspondence':'Incomplete/rejected: first finalA correct; second request aborted after verified own process stalled for more thanfive minutes. Rim sectors were visually clear, though solver called green near5 instead of4. No retry.',
    'Plane471/three_side_chain':'Rejected: both finalD correct. Model explicitly followed tempting marked chain then detected5/4 mismatch and recovered unique correct layout. Stronginformation targeting but ineffective.',
    'Plane250/diagonal_vertical_basis':'Rejected: both responses completed with final21.5/31.25, neither immutable43. Extensive path miscounting does not establish the intended units misbinding.',
    'Plane425/paired_endpoint_links':'HOLD regardless of final pair: blue link passes close toV label and redlink extends the horizontal support. Run1 misread it as a longer original segment. These clarity/interpretation concerns prevent treating it as a credible twohitcandidate.',
    'Plane425/single_endpoint_radius_trap':'Rejected: two complete final answersB/B are wrong relative to formalC but both MISS immutable predeclaredD. They MUST NOT be counted as a successful twohitcandidate or relabeled with targetB. ActualPNG clean and both endpoints exact; true90degree singleendpoint relation aboutV does not map the whole segment. Run1 mislocatedW, run2 keptW coordinates but tested only ordered endpoint matching; no claim that intended V-admission error occurred.',
}
def checkpoint(output):
    attempts=[]
    for token,manual in MANUAL.items():
        folder=HERE/token
        design=json.loads((folder/'design.json').read_text(encoding='utf-8-sig'))
        wrong=str(design.get('expected_wrong_answer',design.get('predicted_wrong_answer')))
        bindings=list((folder/'tests').glob('*/binding.json'))
        tests=[]
        for binding_path in bindings:
            evidence=binding_path.parent;binding=json.loads(binding_path.read_text(encoding='utf-8-sig'))
            assert binding['image_sha256']==file_hash(folder/'candidate.png')
            assert binding['design_sha256']==file_hash(folder/'design.json')
            request=json.loads((evidence/'request.json').read_text(encoding='utf-8-sig'))
            assert set(request)=={'model','stream','thinking','messages'}
            assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
            assert len(request['messages'])==2 and request['messages'][1]['content'][0]['text']==binding['question']
            assert len(request['messages'][1]['content'])==2
            encoded=request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1]
            assert hashlib.sha256(base64.b64decode(encoded)).hexdigest()==binding['image_sha256']
            runs=[]
            for index in [1,2]:
                path=evidence/f'run_{index:02d}.json';aborted=evidence/f'run_{index:02d}_aborted_by_worker.json'
                if path.exists():
                    run=json.loads(path.read_text(encoding='utf-8-sig'))
                    runs.append({'run_index':index,'status':run['status'],'manually_read_final_answer':manual[index-1],'full_answer':run.get('answer'),'finish_reason':run.get('finish_reason'),'truncated':run.get('truncated'),'evidence':str(path.relative_to(ROOT)),'raw_response':str((evidence/f'run_{index:02d}_response.json').relative_to(ROOT))})
                elif aborted.exists():runs.append({'run_index':index,'status':'aborted','manually_read_final_answer':None,'evidence':str(aborted.relative_to(ROOT))})
                else:runs.append({'run_index':index,'status':'pending' if (evidence/f'run_{index:02d}_started.json').exists() else 'not_started','manually_read_final_answer':None})
            tests.append({'binding':str(binding_path.relative_to(ROOT)),'evidence_directory':str(evidence.relative_to(ROOT)),'runs':runs,'same_frozen_image_and_design':True,'payload_only_formal_question_candidate_and_existing_system':True})
        attempts.append({'question_id':design['question_id'],'variant_id':design['variant_id'],'expected_wrong_answer':wrong,'correct_answer':design['correct_answer'],'manually_read_final_answers':manual,'two_target_final_hits':manual==[wrong,wrong],'candidate':str((folder/'candidate.png').relative_to(ROOT)),'plugin':str((folder/'plugin.json').relative_to(ROOT)),'design':str((folder/'design.json').relative_to(ROOT)),'render_check':str((folder/'render_check.json').relative_to(ROOT)),'png_sha256':file_hash(folder/'candidate.png'),'design_sha256':file_hash(folder/'design.json'),'actual_png_viewed':True,'primary_math_visual_review':reviews[token],'independent_second_review_performed':False,'qualified_or_approved':False,'tests':tests})
    snapshot=HERE/'process_snapshot_final.json'
    processes=json.loads(snapshot.read_text(encoding='utf-8-sig')) if snapshot.exists() else None
    write(HERE/output,{'created_at':datetime.now(timezone.utc).isoformat(),'status':'FINITE_SUBSET_COMPLETE','scope':'Prepared Plane435 v01,v02 plus new-question subset425,407,313,471,250; at most3 meaningful variants/question.','new_question_ids':['Plane425','Plane407','Plane313','Plane471','Plane250'],'attempted_variants':8,'actual_requests_started':16,'completed_valid_responses':14,'aborted_requests':2,'complete_two_response_pairs':6,'credible_new_two_hit_candidates':0,'pending_requests_or_drafts':[],'attempts':attempts,'prescreen_no_variant':[{'question_id':'Plane407','reason':'No sufficiently targeted clear mark design found; no API. Correct centreline sum18 independent of rectangle widths.','evidence':str((HERE/'mathematical_audit.json').relative_to(ROOT))}],'math_audit':str((HERE/'mathematical_audit.json').relative_to(ROOT)),'integrity_verification':str((HERE/'integrity_verification.json').relative_to(ROOT)),'credible_candidates_for_parent_second_review':[],'original_controls_performed':False,'original_control_reason':'No credible two-hit candidate meeting immutable preset in this subset.','global_previous_reports_mutated':False,'formal_library_or_workbench_writes':False,'Pass_Collect_or_review_APIs_called':False,'remaining_recommendations':['Do not repeat failed identical images or combine individual B hits across425 variants.','Do not relabel425 single_endpoint_radius_trap B/B as successful: its immutable target was D.','425 paired_endpoint_links remains HOLD for line/label ambiguity; one B then aborted is not two hits.','Plane407 remains untested; only pursue with a clear measurement-range mechanism.','All further experiments need new immutable predeclared designs and current eligibility recheck.'],'stopped_only_own_verified_processes':[9432,41568],'own_process_snapshot':processes,'no_live_process_confirmation':processes==[]})
if __name__=='__main__':checkpoint(sys.argv[1])
