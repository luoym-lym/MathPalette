from tools10 import *
import base64,itertools
manual={
('Plane159','simultaneous_class_binding'):{'finals':['B','A'],'consistent':[True,True],'notes':['Run1 explicitly concludes B and its simultaneous sequence is B; it fails to propagate newlywhite throughstep3.','Run2 concludes A and correctly performs allthree sequentialsteps.']},
('Plane373','initial_spoke_orientation_binding'):{'finals':['E','E'],'consistent':[True,True],'notes':['Run1 final E; its narration misdescribes sectors, so correctletter does not establish accuratevisualreading.','Run2 final E; hallucinates a greenrayinE, thoughE is unmarked.']},
('Plane385','axis_aligned_square_subset'):{'finals':['6','3'],'consistent':[True,True],'notes':['Run1 explicitly totals6 using duplicate/nonexistent squares.','Run2 explicitly totals3, overlooking tiltedsquare. Onepreset hit is insufficient.']},
('Plane324','three_corner_triangle_groups'):{'finals':['3','3'],'consistent':[True,True],'notes':['Run1 concludes remove3bottomdots, incorrectly claiming allsmall/mediumtriangles are hit; it also misreads bottomdotcount.','Run2 concludes3 fromthethree outlined disjointtriangles and explicitlydismisses othertriangles. Both finalnumbers equal immutablepreset3; narratives differ and are mathematically wrong.']},
('Plane373','halfturn_reflected_sector_binding'):{'finals':['C','C'],'consistent':[True,True],'notes':['Run1 final C explicitly followsgreen/red/blueboundaryrays and ignoresoriginalgrayscalewrongchirality.','Run2 finalC; describes nonexistent redsectors but explicitlymatches the180degreecoloredraypattern. Primaryhumansemanticsobjection retained.']},
('Plane385','tilted_square_family_only'):{'finals':['6','6'],'consistent':[True,True],'notes':['Run1 final6, invents full9dotgrid.','Run2 final6, again reads9dots, with inconsistent intermediatearithmetic; preset1notmet.']},
('Plane159','first_stage_black_transfer'):{'finals':['D','A'],'consistent':[False,True],'notes':['Run1 finalD with an8cell sequence that doesnotmatch actualD; inconsistentletter/content, andnotpresetB.','Run2 finalA although itmiscounts8cells; notpresetB.']},
}
def rel(p):return str(Path(p).resolve().relative_to(ROOT)).replace('\\','/')
def final_audit():
    records=[];expected_files={};conflicts=[]
    for p in HERE.glob('Plane*/input_fingerprints.json'):
        for name,h in json.loads(p.read_text(encoding='utf-8'))['files'].items():
            if name in expected_files and expected_files[name]!=h:conflicts.append(name)
            expected_files[name]=h
    diffs={n:{'expected':h,'current':file_hash(ROOT/n) if (ROOT/n).exists() else None} for n,h in expected_files.items() if not (ROOT/n).exists() or file_hash(ROOT/n)!=h}
    sourceaudit={'checked_at':now(),'checked_source_file_count':len(expected_files),'conflicting_start_snapshots':conflicts,'changed_or_missing':diffs,'all_frozen_sources_preserved':not conflicts and not diffs,'mutable_runtime_progress_metadata':'Historical hashes kept as diagnostics; excluded fromfrozenoriginalsourcecomparison.'}
    write(HERE/'source_preservation_audit.json',sourceaudit);assert sourceaudit['all_frozen_sources_preserved']
    for (q,v),m in manual.items():
        out=HERE/q/v;d=json.loads((out/'design.json').read_text(encoding='utf-8'));evs=list((out/'tests').glob('*/summary.json'));assert len(evs)==1
        sp=evs[0];s=json.loads(sp.read_text(encoding='utf-8'));ep=sp.parent;binding=json.loads((ep/'binding.json').read_text(encoding='utf-8'));req=json.loads((ep/'request.json').read_text(encoding='utf-8'))
        assert s['two_completed'] and len(s['results'])==2
        assert file_hash(out/'candidate.png')==file_hash(out/'repeat.png')==s['image_sha256']==d['image_sha256']
        assert file_hash(out/'design.json')==s['design_sha256']==file_hash(ep/'design_snapshot.json')
        assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'}
        assert set(req)=={'model','stream','thinking','messages'}
        assert req['messages'][0]=={'role':'system','content':s['system_prompt']}
        content=req['messages'][1]['content'];assert len(content)==2 and content[0]=={'type':'text','text':s['question']}
        assert s['question']==json.loads((HERE/q/'formal_record.json').read_text(encoding='utf-8'))['question']
        assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==(out/'candidate.png').read_bytes()
        assert file_hash(ep/'request.json')==s['request_body_sha256']
        results=[]
        for i,r in enumerate(s['results']):
            assert r['status']=='completed' and not r['truncated'] and r['finish_reason']=='stop' and r['thinking']==''
            assert file_hash(ep/f'run_{i+1:02d}_response.json')==r['response_sha256']
            assert r['image_sha256']==s['image_sha256'] and r['design_sha256']==s['design_sha256'] and r['request_body_sha256']==s['request_body_sha256']
            results.append({'run_index':i+1,'complete_answer_manually_read':True,'complete_final_answer_text':r['answer'],'explicit_final':m['finals'][i],'letter_or_number_content_consistent':m['consistent'][i],'target_hit':m['consistent'][i] and m['finals'][i]==str(d['expected_wrong_answer']),'manual_notes':m['notes'][i],'run_evidence':rel(ep/f'run_{i+1:02d}.json'),'raw_response':rel(ep/f'run_{i+1:02d}_response.json'),'response_sha256':r['response_sha256']})
        paired=all(r['target_hit'] for r in results)
        status='paired_hit_primary_credible_pending_NEW_independent_review' if q=='Plane324' else ('paired_hit_HELD_primary_human_semantics_objection' if paired else 'failed_preset_pair_do_not_retest_unchanged')
        write(out/'manual_final_review.json',{'reviewed_at':now(),'review_type':'Primary manual completeanswerreading','expected_wrong_answer_unchanged':d['expected_wrong_answer'],'results':results,'paired_target_hit':paired,'status':status,'image_sha256':s['image_sha256'],'design_sha256':s['design_sha256'],'request_body_sha256':s['request_body_sha256']})
        records.append({'question_id':q,'candidate_id':q+'/'+v,'expected_wrong_answer':d['expected_wrong_answer'],'finals':m['finals'],'paired_target_hit':paired,'status':status,'design_path':rel(out/'design.json'),'plugin_path':rel(out/'plugin.json'),'image_path':rel(out/'candidate.png'),'image_sha256':s['image_sha256'],'pixel_sha256':s['pixel_sha256'],'design_sha256':s['design_sha256'],'plugin_sha256':file_hash(out/'plugin.json'),'binding_path':rel(ep/'binding.json'),'request_path':rel(ep/'request.json'),'summary_path':rel(sp),'manual_final_review_path':rel(out/'manual_final_review.json'),'source_inputs_path':rel(out/'source_inputs.json'),'fresh_context_path':rel(out/'fresh_context.json'),'primary_review_path':rel(out/'primary_review.json'),'marker_bindings_path':rel(out/'marker_bindings.json'),'primary_math_proof':d['primary_math_proof'],'per_marker_roles':d['per_marker_roles']})
    write(HERE/'candidate_evidence_audit.json',{'checked_at':now(),'records':records,'complete_pairs':len(records),'calls':2*len(records),'all_request_source_and_frozen_evidence_checks_pass':True,'profile':'mimo-v2.6-flash thinkingdisabled; nooverrides; originalsolverprompt; onlyformalquestion+frozenPNG','new_independent_review_performed':False})
    return records,sourceaudit
if __name__=='__main__':
    recs,sa=final_audit();print(json.dumps({'designs':len(recs),'paired_hits':sum(x['paired_target_hit'] for x in recs),'source_files':sa['checked_source_file_count']}))
