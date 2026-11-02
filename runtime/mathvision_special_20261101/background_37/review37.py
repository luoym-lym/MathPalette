from tools37 import *
import base64
JUDGMENTS={
'Solid102': [('6',False,'Final6liters; mixes paint with unit faces and speculates about hidden contacts. Does not end at12.9375.'),('14',False,'Final14liters; treats whole rectangular-prism faces as comparable and even counts6pieces despite8stated. Still not preset12.9375.')],
'Solid126': [('A',True,'Explicit0%andchoiceA. Overgeneralizes top/side area replacement to entire through-cut and omits two27end losses.'),('A',True,'Explicit0%andA. Invents trapezoid areas and replacement end surfaces; final0%andletterA consistent with preset. Incorrect intermediate geometry is preserved, not adopted as proof.')],
'Solid160': [('B',False,'FinalB=64cm2. Counts16exteriorunitfaces including unpictured opposites. Does not end atD=32.'),('B',False,'FinalB=64cm2. Both facecount and double-sided contact subtraction give64. PresetDmiss.')],
'Solid196': [('80',True,'Final80cm2 hits numeric preset. Reason counts two whole contact planes as two joins, hiding4faces; differs from intended4joins eachsingle-sided. Do not rewrite intended mechanism.'),('64',False,'Final64cm2 after correctly counting fourjoins/twohiddenfaces each. Alternative exterior recount is corrected to16faces. Not80.')],
'Solid224': [('33',False,'Final33m2; correctly excludes onlyground9andcomputestop9plusvertical24. Notpreset28.'),('54',False,'Final54m2; includesgroundandwronglyfull3x3side silhouettes. Differenterrornotpreset28.')],
'Solid230': [('42',True,'Explicit final42. Counts BOTH1pipfaces; middle-right6misreadas5 givesvisible21. Numericpreset hit, but frozenvalue/identitydedup hypothesis NOT observed. Do not relabel mechanism.'),('42',True,'Explicit final42. Again counts both1faces and reads middle-right6as5. Numericpreset hit with same unrelatedpipreadingerror; no evidence that red1facecorrespondence caused it.')],
'Solid231': [('26',False,'Final26squareinches; counts5pairs and subtracts10faces. Describes some branches incorrectly but finalnot31.'),('28',False,'Firstmethod24, secondmethod28, explicitfinal28. Missesonecontactinsecondmethod. Entireanswerread; finalnot24or31. Frozenpreset31unchanged.')]
}
def verify(q,f):
    summaries=list(f.glob('tests/*/summary.json'));assert len(summaries)==1
    s=read(summaries[0]);b=read(summaries[0].with_name('binding.json'));d=read(f/'design.json');r=read(f/'render_check.json');free=read(f/'pretest_freeze.json')
    for n,h in free['files'].items():assert file_hash(f/n)==h,(q,n)
    assert s['two_completed'] and b['requested_runs']==2 and len(s['results'])==2
    assert b['expected_wrong_answer']==d['expected_wrong_answer']
    assert b['design_sha256']==file_hash(f/'design.json') and (f/'design.json').read_bytes()==summaries[0].with_name('design_snapshot.json').read_bytes()
    assert b['image_sha256']==file_hash(f/'candidate.png')==r['png_sha256']
    assert b['pixel_sha256']==pixel_hash(f/'candidate.png')
    assert b['question_record_sha256']==canonical_hash(AD.records[q])
    req=summaries[0].with_name('request.json');assert file_hash(req)==b['request_body_sha256']
    payload=read(req);assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'}
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['messages'][0]=={'role':'system','content':b['system_prompt']}
    user=payload['messages'][1];assert len(payload['messages'])==2 and len(user['content'])==2
    assert user['content'][0]=={'type':'text','text':AD.records[q]['question']}
    assert base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])==(f/'candidate.png').read_bytes()
    for i in [1,2]:
        p=summaries[0].with_name(f'run_{i:02d}.json');job=read(p);raw=p.with_name(f'run_{i:02d}_response.json')
        assert job['status']=='completed' and job['response_sha256']==file_hash(raw)
        assert job['image_sha256']==b['image_sha256'] and job['design_sha256']==b['design_sha256'] and job['request_body_sha256']==b['request_body_sha256']
    return {'binding_path':str(summaries[0].with_name('binding.json')),'binding_sha256':file_hash(summaries[0].with_name('binding.json')),'summary_path':str(summaries[0]),'summary_sha256':file_hash(summaries[0]),'request_path':str(req),'request_sha256':file_hash(req),'image_sha256':b['image_sha256'],'design_sha256':b['design_sha256'],'expected_wrong_answer':b['expected_wrong_answer'],'exact_two_completed':True,'request_only_unchanged_system_formal_question_and_frozen_png':True,'profile_unchanged':True,'retries':0,'all_pretest_hashes_unchanged':True}
def review(q):
    fs=[p.parent for p in (TASK/q).glob('*/design.json')];assert len(fs)==1;f=fs[0]
    evidence=verify(q,f);runs=[]
    for i,(answer,hit,interpretation) in enumerate(JUDGMENTS[q],1):
        p=Path(evidence['summary_path']).with_name(f'run_{i:02d}_response.json');raw=read(p)
        runs.append({'run':i,'raw_response_path':str(p),'raw_response_sha256':file_hash(p),'finish_reason':raw['choices'][0]['finish_reason'],'complete_raw_final_answer_text':raw['choices'][0]['message']['content'],'entire_response_read_manually':True,'manually_extracted_final':answer,'letter_and_value_consistent':True,'matches_immutable_preset':hit,'interpretation':interpretation})
    paired=all(x[1] for x in JUDGMENTS[q]);write(f/'manual_final_review.json',{'question_id':q,'variant_id':f.name,'created_at':now(),'preset':read(f/'design.json')['expected_wrong_answer'],'manual_results':runs,'numeric_two_hit':paired,'primary_candidate_for_parent_review':paired,'information_mechanism_confirmed_by_outputs':(False if q=='Solid230' else (True if q=='Solid126' else None)),'old_misses_unchanged':True,'preset_not_reassigned':True,'new_independent_second_review_required':paired})
    write(f/'evidence_binding_audit.json',evidence)
    pre=read(f/'pretest_visual_review.json');d=read(f/'design.json')
    write(f/'primary_review.json',{'question_id':q,'variant_id':f.name,'kind':'PRIMARY AUTHOR REVIEW ONLY; never an independent review','created_at':now(),'mathematical_answer':AD.records[q]['answer'],'unique_answer_proof':d['pretest_math_proof'],'markers':d['pretest_marker_roles'],'native_png_review':pre,'evidence':evidence,'full_manual_finals_path':str(f/'manual_final_review.json'),'numeric_two_hit':paired,'primary_candidate_for_parent_review':paired,'information_targeting_caution':('BOTHoutputs count bothmarked1faces. Intendedequal-valueidentitycollapse is unobserved; bothmisreadunmarkedmiddle-right6as5. Numeric42/42is validbutdoesnotdemonstrateintendedmechanism orincrementaleffect. Parent NEW reviewer must judge whether twoopen1facerimscorrespondence is sufficientlyinformative; do not presentasqualified.' if q=='Solid230' else None),'math_scope_qualification':'Generic box union helper includes diagnostic ground-excluded areas; onlySolid224asksground exclusion. Solid102andSolid231usefull_surface_area46and26respectively.','limits':['Original controls absent in prior evidence for these assigned cases; no new control calls. No incremental or causal effect established.','Solid126oldheightvariantA/AstillmissesoldpresetC; its outcomes are different-image history, never new evidence.','Human clarity is primary native visual inspection; parent must create a NEW independent review before delivery.'],'approval_status':'No Pass/Collect/formal approval/publication'})
    print(q,'PRIMARY_TWO_HIT' if paired else 'MISS',[x[0] for x in JUDGMENTS[q]])
if __name__=='__main__':
    for q in sys.argv[1:]:review(q)
