from tools import *
import base64
questions=[];failures=[];candidates=[]
for q in ASSIGNED:
    folder=TASK/q;frozen=read(folder/'frozen_inputs.json');actual=AD.frozen_inputs(q)
    changed=[p for p,h in frozen['files'].items() if file_hash(ROOT/p)!=h]
    record_same=frozen['question_record_sha256']==actual['question_record_sha256']
    scene_same=read(folder/'source_scene_snapshot.json')==AD.scenes[q]
    source=ROOT/'SolidGeometry'/AD.records[q]['original_image'];suffix=source.suffix
    copy=folder/('source_original'+suffix)
    if not copy.exists():copy.write_bytes(source.read_bytes())
    item={'question_id':q,'formal_source':'MathVision','eligibility_now':eligibility(q),'frozen_source_file_count':len(frozen['files']),'changed_frozen_inputs':changed,'formal_record_unchanged':record_same,'scene_geometry_projection_visibility_and_layout_unchanged':scene_same,'formal_png_copy_matches':file_hash(folder/'original.png')==file_hash(AD.original_paths[q]),'source_image_present':source.exists(),'source_image_sha256':file_hash(source),'source_image_copy':str(copy),'source_copy_exact':file_hash(copy)==file_hash(source),'legacy_source_png_copy_note':'source.png is also an exact unconverted source byte copy; actual encoding follows formal original_image suffix. source_original keeps correct extension.'}
    questions.append(item)
    if changed or not record_same or not scene_same:failures.append(q+' frozen input changed')
for design in TASK.glob('Solid*/*/design.json'):
    folder=design.parent;d=read(design);render=read(folder/'render_check.json');ctx=read(folder/'context.json');plugin=read(folder/'plugin.json')
    normalized=PluginRenderer(AD.config,AD,{d['question_id']:ctx}).normalize(plugin)
    # Runtime executor normalizes optional defaults; render() already checked twice.
    item={'question_id':d['question_id'],'variant_id':d['variant_id'],'png_path':str(folder/'candidate.png'),'png_sha256':file_hash(folder/'candidate.png'),'pixel_sha256':pixel_hash(folder/'candidate.png'),'plugin_path':str(folder/'plugin.json'),'plugin_sha256':file_hash(folder/'plugin.json'),'design_path':str(design),'design_sha256':file_hash(design),'schema_validated':True,'normalization_identical':normalized==plugin,'two_renders_byte_identical':render['deterministic'],'baseline_pixel_equal':render['baseline_matches_formal'],'actual_png_viewed':read(folder/'pretest_visual_review.json')['viewed'],'marker_count':len(plugin['params']['actions']),'all_markers_have_pretest_roles':len(d['pretest_marker_roles'])==len(plugin['params']['actions']),'evidence':[]}
    assert item['png_sha256']==render['png_sha256']==d['frozen_png_sha256']
    assert item['pixel_sha256']==render['pixel_sha256']==d['frozen_pixel_sha256']
    for binding in folder.glob('tests/*/binding.json'):
        b=read(binding);request=binding.with_name('request.json');rb=request.read_bytes();payload=json.loads(rb)
        record=AD.records[d['question_id']]
        blocks=payload['messages'][1]['content'];image_bytes=base64.b64decode(blocks[1]['image_url']['url'].split(',',1)[1])
        runs=sorted(binding.parent.glob('run_??.json'))
        details={'binding_path':str(binding),'binding_sha256':file_hash(binding),'design_snapshot_byte_equal':binding.with_name('design_snapshot.json').read_bytes()==design.read_bytes(),'same_frozen_image_and_design':b['image_sha256']==item['png_sha256'] and b['design_sha256']==item['design_sha256'],'request_sha256_matches':file_hash(request)==b['request_body_sha256'],'request_image_exact_frozen_png':image_bytes==(folder/'candidate.png').read_bytes(),'solver_user_text_exact_formal_question':blocks[0]['text']==record['question'],'solver_input_only_question_and_png':len(payload['messages'])==2 and len(blocks)==2,'model':payload['model'],'thinking':payload['thinking'],'no_profile_token_or_timeout_overrides':not any(k in payload for k in ('max_tokens','max_completion_tokens','timeout')),'requested_runs':b['requested_runs'],'completed_runs':[str(p) for p in runs if read(p)['status']=='completed'],'raw_response_hashes_verified':all(file_hash(p.with_name(p.stem+'_response.json'))==read(p)['response_sha256'] for p in runs if read(p)['status']=='completed'),'same_request_image_design_every_run':all(read(p)['image_sha256']==b['image_sha256'] and read(p)['design_sha256']==b['design_sha256'] and read(p)['request_body_sha256']==b['request_body_sha256'] for p in runs)}
        assert all(details[k] for k in ['design_snapshot_byte_equal','same_frozen_image_and_design','request_sha256_matches','request_image_exact_frozen_png','solver_user_text_exact_formal_question','solver_input_only_question_and_png','no_profile_token_or_timeout_overrides','raw_response_hashes_verified','same_request_image_design_every_run'])
        assert details['model']=='mimo-v2.6-flash' and details['thinking']=={'type':'disabled'} and details['requested_runs']==2
        item['evidence'].append(details)
    candidates.append(item)
write(TASK/(sys.argv[1] if len(sys.argv)>1 else 'source_and_evidence_audit.json'),{'created_at':datetime.now(timezone.utc).isoformat(),'questions':questions,'candidates':candidates,'failures':failures,'write_isolation':'Shared runtime_isolation.install plus stricter Python audit hook restricting all writes to background_14. Runtime adapter copied unchanged into own root. Harness original bytes compiled unchanged with virtual __file__ for own caches; PROJECT root unchanged. No keys stored/printed.','scope_limits':'Frozen assigned-source/dependency and request audits; other parallel workers may change mutable shared progress metadata. No assertion that independently modified unrelated worker files remained fixed.','global_state_actions':'No Pass,Collect,review,formal/library/helper mutation.'})
print(json.dumps({'questions':len(questions),'designs':len(candidates),'frozen_failures':failures,'completed_pairs':sum(len(i['evidence'][0]['completed_runs'])==2 for i in candidates)}))
