from review_bootstrap import *

def run():
    report=load(OWN/'independent_review.json')
    closure=load(OWN/'process_closure.json')
    assert not closure['own_review_python_remaining']
    assert not closure['original_unit_python_remaining']
    report['process_closure']['actual_process_snapshot']=closure
    report['process_closure']['owned_processes_remaining']=[]
    report['own_audit_support_file_hashes']={p.name:sha(p) for p in OWN.glob('*.json') if p.name!='independent_review.json'}
    report['completed_at_utc']=now()
    assert report['decision']=='recommended'
    assert report['method_fidelity']['classification']=='extension'
    assert report['independently_derived_original_answer']=='5'
    assert [r['final_value'] for r in report['actual_complete_final_readings']]==['4','4']
    assert len(report['per_marker_information_legal_human_review'])==8
    assert len(report['history_and_process_objections']['all_current_presets_images_raw_hashes_and_failures'])==12
    assert report['image_sha256']==sha(CANDIDATE/'candidate.png')
    assert report['plugin_sha256']==sha(CANDIDATE/'plugin.json')
    assert report['design_sha256']==sha(CANDIDATE/'design.json')
    assert report['summary_sha256']==sha(report['summary_path'])
    for p,checks in load(OWN/'scoped_preservation_final.json')['checks'].items():
        assert sha(p)==checks['after_sha256'],p
    save('independent_review.json',report)
    reread=load(OWN/'independent_review.json')
    assert canonical(reread)==canonical(report)
    print(canonical({'path':str(OWN/'independent_review.json'),'sha256':sha(OWN/'independent_review.json'),
        'decision':'recommended','method_fidelity':'extension','original_answer':'5',
        'complete_wrong_final_values':['4','4'],'new_calls':0,'no_background_processes_started':True,
        'user_approval_Pass_Collect':False}))

if __name__=='__main__': main(run)
