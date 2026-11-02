from worker import *
import base64

save(OWN/'Solid193/remaining_semantic_assessment.json',{'created_at':now(),'status':'UNRESOLVED_NO_PRIMARY_CANDIDATE','not_an_impossibility_claim':True,'original_unique_correct':{'letter':'E','value':'3 and 5'},'new_tests':[
    {'variant':'C01_flap_count_versus_destination','preset':'A:1and3','finals':['B:1and5','B:1and5'],'result':'Both missed A; not relabeled as B success'},
    {'variant':'C02_truthful_diagonal_with_false_strip_analogy','preset':'B:1and5','finals':['B:1and5','C or D with stated3and4'],'result':'One target hit, second ambiguous and letter/value conflict'},
    {'variant':'C03_cross_hinge_offset_ignored','preset':'B:1and5','finals':['C or D:2and4','D:2and4'],'result':'Both miss B; repeated wrong value does not identify one frozen letter'}
    ],'earlier_history':'Old cut_seam_false_pairing was E/B against B; both full raw responses and its complete design/review files read and preserved. No old PNG retested.',
    'remaining_directions_examined':[
        {'idea':'Repeat false source alternating half-seam pairing to1and3','reason_not_called':'Duplicates the old tested design, even with thicker lines, swapped colors or more V sides.'},
        {'idea':'Count all four quarter flaps as a complete missing face','reason_not_called':'C01 explicitly tested this versus actual destination and failed. No new independent correspondence by adding still more red edges.'},
        {'idea':'Make strips1and5 look equivalent','reason_not_called':'C02 uses exact true source seams on every valid net and a new false1-to5 planar strip analogy; failed. Simple re-groupings of the same sides do not create a new structural claim.'},
        {'idea':'Treat shifted cross3 as symmetric cross2','reason_not_called':'C03 specifically tested the hinge-offset correspondence; failed. All four actual triangle destinations remain available in the proof.'},
        {'idea':'Select C or D after the observed2and4 outputs','reason_not_called':'Forbidden relabeling; C and D are duplicated text and raw responses explicitly alternate/hedge them. There is no new geometry-based mark that independently selects one duplicate letter. Not counted as preset hits and not used for a new arbitrary call.'},
        {'idea':'Change a flap, cut, gray fill, number or add text to clarify','reason_not_called':'Changes the formal problem or introduces extra information and violates fixed source/human clarity.'}
    ],'why_unfinished':'Three genuinely new correspondence hypotheses failed their immutable exact-two tests. Remaining identified directions repeat tested geometry or require unsupported conditions/letter selection. No reliable fresh useful mapping presently remains; no impossibility or global exhaustion claim. No quota-based or fixed-three-candidate stop rule applied.','actual_new_calls':6,'errors_or_aborts':0,'formal_actions':0,'independent_second_review':False})

def preserve():
    changes=[];checked=[]
    for qid in QIDS:
        result=eligibility(qid,OWN/qid/'eligibility_final.json')
        checked.extend({'path':p,**h} for p,h in result['source_checks'].items())
    for entry in read(OWN/'history_actual_files_read.json'):
        actual=sha(PROJECT/entry['path'])
        checked.append({'path':entry['path'],'expected':entry['sha256'],'actual':actual})
    for entry in read(OWN/'reference_read_ledger.json'):
        actual=sha(entry['path']);checked.append({'path':entry['path'],'expected':entry['sha256'],'actual':actual})
    for name,h in read(OWN/'scope_original_bytes.json').items():
        checked.append({'path':str(OWN/name),'expected':h,'actual':sha(OWN/name)})
    changes=[c for c in checked if c['expected']!=c['actual']]
    save(OWN/'source_preservation_final.json',{'created_at':now(),'all_frozen_sources_and_old_evidence_unchanged':not changes,'checks':checked,'changes':changes,'formal_dataset_approval_checks':'Recomputed catalog content fingerprint for each assigned at initial, each design/render/replay, immediately before request loop, before EACH actual started write, after calls and final. No approval updated.','parent_metadata_policy':'Parent progress/brief append files are not restored or treated as source-image drift; only exact frozen assignment bytes and original evidence checked.','all_writes_under':str(OWN)})
    assert not changes

def results():
    tests=[];actual=0;errors=[];images=set()
    for p in sorted(OWN.glob('Solid*/*/tests/*/summary.json')):
        s=read(p);d=p.parent.parent.parent;b=read(p.parent/'binding.json');manual=read(d/'manual_final_review.json')
        starts=list(p.parent.glob('run_*_started.json'));responses=list(p.parent.glob('run_*_response.json'))
        assert len(starts)==len(responses)==len(s['results'])==2
        actual+=len(starts)
        assert b['image_sha256']==sha(d/'candidate.png') and b['design_sha256']==sha(d/'design.json')
        assert b['design_sha256']==sha(p.parent/'design_snapshot.json')
        assert sha(p.parent/'request.json')==b['request_body_sha256']
        payload=read(p.parent/'request.json')
        assert set(payload)=={'model','stream','thinking','messages'}
        assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
        assert payload['messages'][0]['role']=='system' and payload['messages'][0]['content']==b['system_prompt']
        assert payload['messages'][1]['content'][0]=={'type':'text','text':b['question']}
        assert base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(d/'candidate.png').read_bytes()
        image_key=(b['question_id'],b['image_sha256']);assert image_key not in images;images.add(image_key)
        for i,r in enumerate(s['results'],1):
            if r['status']!='completed' or r.get('truncated'):errors.append({'summary':str(p),'run':i,'status':r['status']})
            assert sha(p.parent/f'run_{i:02d}_response.json')==r['response_sha256']
            assert read(p.parent/f'run_{i:02d}_response.json')['choices'][0]['message']['content']==manual['runs'][i-1]['complete_answer_text']
            assert (d/f'run_{i:02d}_started_eligibility.json').exists()
        tests.append({'question_id':b['question_id'],'variant_id':read(d/'design.json')['variant_id'],'preset_letter':manual['frozen_preset_letter'],'preset_value':manual['frozen_preset_value'],'final_letters':[r['manual_final_letter'] for r in manual['runs']],'final_values':[r['manual_final_value'] for r in manual['runs']],'complete_responses':all(r['complete_nontruncated'] for r in manual['runs']),'two_hits':manual['both_hit_frozen_preset'],'summary_path':str(p),'manual_review_path':str(d/'manual_final_review.json'),'image_sha256':b['image_sha256'],'design_sha256':b['design_sha256'],'request_sha256':b['request_body_sha256']})
    assert actual==16 and not errors
    assert not read(OWN/'second_review_queue.json')
    save(OWN/'research_results.json',{'created_at':now(),'question_ids':QIDS,'new_tested_frozen_images':len(tests),'actual_calls':actual,'all_requests_exactly_two_no_retry_or_third_call':True,'all_raws_manually_read':True,'API_errors_or_aborts':errors,'tests':tests,'PRIMARY_candidates':[],'pretest_rejections':[str(OWN/'Solid228/C02_moving_hinge_axis_accumulation/pretest_rejection.json')],'offline_coding_errors':[str(OWN/'offline_error_01.json'),str(OWN/'offline_error_02.json')],'formal_actions':0,'independent_second_review':False,'delivery_performed':False})
    cp=read(OWN/'checkpoint.json')
    for qid in QIDS:
        cp['questions'][qid]={'status':'unresolved_no_primary','actual_new_api_calls':sum(2 for x in tests if x['question_id']==qid),'reason_path':str(OWN/qid/'remaining_semantic_assessment.json'),'math_proof_path':str(OWN/qid/'primary_math_proof.json'),'all_new_tests_finalized':True}
    checkpoint(status='research_checkpoint_unresolved_no_primary',actual_new_api_calls=actual,questions=cp['questions'],primary_candidate_count=0,api_errors_or_aborts=0,unworked=[],holds=[],unresolved=QIDS,pretest_rejection_count=1)
    print(json.dumps({'actual_calls':actual,'tested_images':len(tests),'primary':0,'unresolved':QIDS},ensure_ascii=False))

def manifest():
    rows=[]
    for p in sorted(OWN.rglob('*')):
        if p.is_file() and 'cache' not in p.relative_to(OWN).parts and p.name!='artifact_sha256_manifest.json':rows.append({'path':str(p.relative_to(OWN)),'sha256':sha(p),'bytes':p.stat().st_size})
    save(OWN/'artifact_sha256_manifest.json',{'created_at':now(),'files':rows,'scope':'All research/source-binding/plugin/design/process/raw evidence files excluding rebuildable own cache and this self-referential manifest'})

if __name__=='__main__':preserve();results();manifest()
