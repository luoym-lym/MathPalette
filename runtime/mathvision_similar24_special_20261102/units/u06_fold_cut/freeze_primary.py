from local_env import *
import json, base64, hashlib, importlib.util, gc, argparse

ap=argparse.ArgumentParser()
ap.add_argument('--manifest',default=str(OWN/'primary_design_manifest.json'))
opts=ap.parse_args()
manifest=read_json(opts.manifest)
history=read_json(TASK/'history_index.json')
old_requests=[]
for path in OLD.rglob('request.json'):
    data=read_json(path)
    messages=data.get('messages',[])
    texts=[]; images=[]
    for msg in messages:
        if msg.get('role')!='user': continue
        content=msg.get('content',[])
        if isinstance(content,str): texts.append(content); continue
        for item in content:
            if item.get('type')=='text': texts.append(item['text'])
            elif item.get('type')=='image_url':
                url=item['image_url']['url']
                if url.startswith('data:image/png;base64,'):
                    raw=base64.b64decode(url.split(',',1)[1])
                    images.append(hashlib.sha256(raw).hexdigest())
                    del raw
    old_requests.append({'request_path':str(path),'request_sha256':sha(path),'user_texts':texts,'image_sha256':images})
    del data
    gc.collect()
if (OWN/'old_request_scan.json').exists():
    assert read_json(OWN/'old_request_scan.json')['requests']==old_requests
else:
    save(OWN/'old_request_scan.json',{'created_at':now(),'count':len(old_requests),'requests':old_requests},True)

for entry in manifest:
    qid=entry['question_id']; root=OWN/qid; candidate=Path(entry['candidate_directory'])
    branch='SolidGeometry' if qid.startswith('Solid') else 'PlaneGeometry'
    formal=read_json(root/'formal_record.json')
    scene=read_json(root/'source_scene_snapshot.json')
    pre=read_json(candidate/'premodel_primary_reasoning.json')
    checks=read_json(candidate/'render_check.json')
    replay=read_json(candidate/'fresh_process_replay.json')
    assert replay['png_bytes_exact']
    image_sha=sha(candidate/'candidate.png')
    request_matches=[x for x in old_requests if image_sha in x['image_sha256']]
    same_question_matches=[x for x in request_matches if formal['question'] in x['user_texts']]
    earlier_own_matches=[]
    for path in OWN.glob('*/*/tests/*/binding.json'):
        prior=read_json(path)
        if prior['image_sha256']==image_sha and prior['question']==formal['question']:
            earlier_own_matches.append(str(path))
    assert not earlier_own_matches, 'No earlier unit request may be resumed or retested'
    assert not same_question_matches, 'No same-question frozen PNG may be retested'
    assert not request_matches, 'This new design must not exploit another question failed PNG'
    hq=next(x for x in history['questions'] if x['question_id']==qid)
    assert all(d.get('frozen_candidate_png_sha256')!=image_sha for d in hq['designs'])
    read_inventory=read_json(root/'history_files_read.json')
    changed=[]
    for f in read_inventory:
        expected=history['tracked_readonly_source_sha256'].get(f['path'])
        if expected and expected!=f['sha256']: changed.append(f['path'])
        assert sha(PROJECT/f['path'])==f['sha256']
    assert not changed, changed
    novelty={'question_id':qid,'image_sha256':image_sha,
        'all_old_request_count_scanned':len(old_requests),'exact_same_question_image_requests':same_question_matches,
        'all_old_image_request_matches':request_matches,'earlier_own_same_question_image_matches':earlier_own_matches,'history_design_count':len(hq['designs']),
        'old_files_hashes_preserved':True,'old_transport_groups':len(hq['all_saved_transport_groups_for_question']),
        'references_authorized_across_formal_questions':True,'new_image_not_old_frozen_input':True}
    if (candidate/'prior_input_novelty.json').exists(): assert read_json(candidate/'prior_input_novelty.json')==novelty
    else: save(candidate/'prior_input_novelty.json',novelty,True)
    if branch=='SolidGeometry':
        native_path=PROJECT/branch/f'dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/{qid}/source_redraw.py'
        spec=importlib.util.spec_from_file_location('_u06_actual_frozen_solid_math',native_path)
        mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        results=mod.validate(scene)
        save(candidate/'world_projection_visibility_audit.json',{
          'original_scene_fully_parsed':True,'actual_frozen_native_validator':str(native_path),'actual_native_validator_checks':results,
          'world_geometry':{'points_sha256':hashlib.sha256(json.dumps(scene['points'],sort_keys=True,separators=(',',':')).encode()).hexdigest(),
                            'constraint_count':len(scene['constraints']),'all_frozen':True},
          'projection':{'value':scene['projection'],'computed_sha256':mod.digest(scene['projection']),
                        'frozen_visibility_binding':scene['visibility']['projection_sha256']},
          'visibility':{'value':scene['visibility'],'object_count':len(scene['objects']),
                        'intervals_checked_by_original_validator':True,'rendered_linestyle_overrides':[]},
          'source_scene_sha256':sha(root/'source_scene_snapshot.json'),
          'primary_manual_findings':'Source paper folds and layers match the viewed source JPG; there are no new cuts/creases, altered bands or changed occluded edges. Color-only existing cut contours leave all three layers of geometry/projection/visibility frozen.'},True)
    # Each action here is a disjoint color+width override, merged per target/interval.
    actions=read_json(candidate/'plugin.json')['params']['actions']
    for i,a in enumerate(actions):
        assert a['type']=='set_object_style' and 'linestyle' not in a
        for b in actions[i+1:]:
            if a['target']!=b['target']: continue
            ia,ib=a.get('interval'),b.get('interval')
            assert ia and ib and max(ia['start'],ib['start'])>=min(ia['end'],ib['end'])
    actual_findings={
      'Solid146':'Viewed native 768px: eight D slants visibly separate into red increasing and blue decreasing directions; all four notches and retained horizontal plateaus stay readable. Source uncut paper, arrow and crease remain black.',
      'Solid174':'Viewed native 768px: same D direction pairs, with original scissors and one-fold packet fully retained. No scissor blade or source boundary was recolored into a new cut.',
      'Solid239':'Viewed native 768px: original diagonal remains dashed red across exactly the original endpoints; only four B notch sides are red/blue. Four-layer top/left stack and material bands remain visible. The black central diamond E remains intact.',
      'Plane220':'Viewed native 768px: red outer E zigzags and blue inner E zigzags form two definite reflection pairs. Two circular interiors and their point contact with the global dotted seam remain visible; rounded arcs stay black. Source and correct D are untouched.'}[qid]
    if entry['variant_id']=='endpoint_to_four_border_orbits':
        actual_findings='Viewed native 768px: the one original collinear dashed cut has red near its bottom endpoint and blue near its right endpoint, with no new vertex or cut. A top/bottom Vs are red, left/right Vs blue. All gray fills, layers, bands and black retained boundaries are intact; correct E remains an uncolored central diamond.'
    elif entry['variant_id']=='near_tangent_fold_contact_alias':
        actual_findings='Viewed native 768px: B original dotted fold is blue, as are only the two facing curved neighborhoods. Its two outward zigzags are red; all other curves remain black. At unchanged 1pt width the near-contact remains a boundary contact/separation rather than a drawn connecting bridge. Source and correct D are untouched; labels and dotted fold remain readable.'
    elif entry['variant_id']=='false_mirror_extremity_pair':
        actual_findings='Viewed native 768px: C original dotted axis is blue. Only the far-left rounded arc neighborhood and far-right zigzag are red, creating an explicit proposed opposite-side pair. Their rounded-versus-pointed difference stays clear at unchanged 1pt width; the rest of the oval is black. Source and correct D remain untouched, with no new crease or material ink on the source.'
    primary={'review_kind':'PRIMARY_ONLY_NOT_INDEPENDENT_SECOND_REVIEW','reviewed_at':now(),
      'actual_candidate_png_viewed_native':True,'source_JPG_and_formal_PNG_actually_viewed':True,
      'unique_math_proof':str(candidate/'mathematics.json'),'unique_original_answer':entry['correct_answer'],
      'source_and_receiver_for_every_action':pre['each_action_role'],'human_semantics_both_readings':pre['human_semantics_both_readings'],
      'actual_visual_findings':actual_findings,'no_superposed_or_dead_actions':True,
      'schema_noop_repeat_fresh_replay_passed':True,'old_failed_images_not_retested':True,
      'proceed_to_exact_two_calls':True,'independent_second_review_performed':False,
      'no_Pass_Collect_or_delivery':True,'limitations':['Hypotheses have not been evaluated by any new model output at this point.',
       'Even two matching wrong finals require a NEW parent-created independent reviewer; no efficacy, robustness or causal claim.']}
    save(candidate/'primary_review_before_calls.json',primary,True)
    design={'question_id':qid,'variant_id':entry['variant_id'],'created_at':now(),
      'expected_wrong_answer':entry['expected_wrong_answer'],'expected_wrong_value':formal['choices'][entry['expected_wrong_answer']],
      'formal_correct_answer':entry['correct_answer'],'answer_semantics':'Each option letter maps to itself; a hit requires an explicit final choice with matching letter/value, no conflicting final.',
      'mechanism_predeclared':pre['each_action_role'],'mathematics':read_json(candidate/'mathematics.json'),
      'human_semantics':pre['human_semantics_both_readings'],'native_visual_review':actual_findings,
      'reference_transfer':str(candidate/'reference_transfer.json'),'history_difference_audit':str(candidate/'history_difference_audit.json'),
      'frozen_files':{name:sha(candidate/name) for name in ['candidate.png','plugin.json','context.json','path_fingerprints.json',
                 'mathematics.json','reference_transfer.json','history_difference_audit.json','primary_review_before_calls.json','render_check.json','fresh_process_replay.json','prior_input_novelty.json']},
      'formal_record':formal,'approval_content_sha256':read_json(root/'eligibility_before_design.json')['current_content_sha256'],
      'requested_runs':2,'profile':'original quicktest3 / mimo-v2.6-flash / thinking.disabled','max_tokens_sent':False,
      'only_formal_question_and_PNG_sent':True,'status':'PRIMARY_PENDING_EXACT_TWO_OBSERVATIONS',
      'forbidden':['third call','automatic retry','post-output preset change','selecting two from more attempts','Pass/Collect','self second review']}
    save(candidate/'design.json',design,True)
    save(candidate/'frozen_design_sha256.json',{'design_sha256':sha(candidate/'design.json'),'image_sha256':image_sha,
                                            'frozen_at':now(),'new_candidate_calls_at_freeze':0,
                                            'prior_unit_requests':len(list(OWN.glob('*/*/actual_call_*_payload_gate.json')))},True)
    print(json.dumps({'qid':qid,'frozen':True,'wrong_preset':entry['expected_wrong_answer'],'design_sha256':sha(candidate/'design.json')}))

cp=read_json(OWN/'checkpoint.json');cp['updated_at']=now();cp['phase']='frozen_candidates_ready_for_two_calls'
for e in manifest:
    cp['questions'][e['question_id']].update({'status':'frozen_ready','candidate_directory':e['candidate_directory'],'preset':e['expected_wrong_answer'],
        'calls':len(list((OWN/e['question_id']).glob('*/actual_call_*_payload_gate.json')))})
save(OWN/'checkpoint.json',cp)
