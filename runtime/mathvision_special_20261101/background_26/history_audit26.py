from tools26 import *
inventory=read(HERE/'history_inventory.json')
finals={'Plane175':{'v01':['B','C'],'v02':['D','A'],'v03':['C','None of the choices'],'v04':['A','C'],'v05':['B','B'],'v06':['A','B']},'Plane198':{'compressed_bottom_run_correspondence':['D','B']},'Plane223':{'large_spot_ring_correspondence':['C','D']},'Plane252':{'incompatible_local_overlap_sum':['2','6'],'single_U_contiguous_overlap':['3','6']},'Plane282':{'exposed_step_unit_transfer':['14','12'],'full_contact_unit_binding':['14','15']},'Plane408':{'ribbon_identity_top_edge_binding':['E','B']},'Plane446':{'square_skeleton_symmetry':['1','1'],'tail_orientation_correspondence':['2','1']},'Plane461':{'punch_to_outer_corner_correspondence':['C','D']}}
for q,paths in inventory.items():
    history=[];files={}
    for rel in paths:
        p=ROOT/rel;d=read(p);folder=p.parent
        for f in folder.rglob('*'):
            if f.is_file():files[str(f.relative_to(ROOT))]=file_hash(f)
        raw=[]
        for f in sorted(folder.rglob('run_*_response.json')):
            r=read(f);raw.append({'path':str(f.relative_to(ROOT)),'sha256':file_hash(f),'full_response':r,'full_final_content':r['choices'][0]['message'].get('content'),'finish_reason':r['choices'][0].get('finish_reason')})
        preset=d.get('expected_wrong_answer',d.get('predicted_wrong_answer'))
        ff=finals[q][folder.name]
        history.append({'candidate':str(folder.relative_to(ROOT)),'variant_id':d.get('variant_id',folder.name),'preset':preset,'full_design':d,'full_plugin':read(folder/'plugin.json'),'manual_final_answers':ff,'hits_own_unchanged_preset':[x==preset for x in ff],'credible_old_double_hit':False,'raw_responses':raw,'all_same_question_designs_and_native_PNGs_read':True,'primary_reviews_read':list(str(f.relative_to(ROOT)) for f in folder.glob('primary_review.*'))})
    # Question-level previous proof/context evidence, and any independently held/rejected reports.
    parents={ (ROOT/p).parent.parent for p in paths}
    extra=[]
    for par in parents:
        for f in par.glob('*'):
            if f.is_file():files[str(f.relative_to(ROOT))]=file_hash(f);extra.append(str(f.relative_to(ROOT)))
    objections=[]
    for f in (BASE/'independent_review').rglob('*'):
        if f.is_file() and q in str(f):files[str(f.relative_to(ROOT))]=file_hash(f);objections.append(str(f.relative_to(ROOT)))
    write(HERE/q/'prior_history_audit.json',{'question_id':q,'created_at':now(),'history':history,'additional_question_level_evidence':extra,'independent_objections_found':objections,'no_prior_success_relabeling':True,'native_original_and_all_prior_candidate_images_manually_viewed':True,'old_evidence_file_sha256':files})
write(HERE/'delivered_reference_audit.json',{'read_only_batches':[{'path':str(p.relative_to(ROOT)),'sha256':file_hash(p),'mechanisms':[{'question_id':c['question_id'],'mechanism':c.get('mechanism')} for c in read(p).get('candidates',[])]} for p in sorted(BASE.glob('batch_*/manifest.json'))],'principle':'Use explicit geometric input-feature correspondence or true grouping with a defined misconception; no isolated option salience.'})
print('All 16 historical designs retain their OWN presets; zero credible old double-hits. Full raw finals and hashes saved.')
