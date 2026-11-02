from review_env import *

def prose(v):
    if isinstance(v, dict):
        return {k: prose(x) for k,x in v.items()
                if k not in ('hash_bindings','file_hashes','all_read_candidate_evidence_files',
                             'source_file_hashes','current_hashes','immutable_input_hashes',
                             'all_files','source_fingerprints','read_file_hashes')
                and not (isinstance(x,dict) and len(x)>15 and
                         sum(('\\' in a or '/' in a) for a in x)>len(x)*0.7)}
    if isinstance(v, list):
        if len(v)>30 and all(isinstance(x,dict) and ('sha256' in x or 'current_sha256' in x) for x in v):
            return {'machine_read_entries':len(v)}
        return [prose(x) for x in v]
    return v

mode=sys.argv[1]
if mode=='prior':
    for rel in [
        'independent_review/Plane233_two_U_partial_partition_binding/independent_review.json',
        'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
        'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']:
        if len(sys.argv)>2 and sys.argv[2] not in rel:continue
        data=read(BATCH/rel)
        def walk(v, path=''):
            if isinstance(v,dict):
                for k,x in v.items():
                    if k in ('hash_bindings','evidence_binding','two_call_evidence','raw_evidence','two_call_audit',
                             'controls_and_effect_limits','all_read_candidate_evidence_files','source_hashes',
                             'two_complete_predeclared_candidate_calls','original_controls_kept_separate'):continue
                    walk(x, path+'.'+k)
            elif isinstance(v,list):
                for i,x in enumerate(v):walk(x,path+f'[{i}]')
            elif isinstance(v,str) and len(v)>65 and '\\' not in v and not ('/' in v and ' ' not in v):
                print(path+': '+v)
        print(rel)
        walk(data)
elif mode=='candidate':
    names=['fresh_drawn_path_verification.json','render_check.json','pixel_difference_diagnostics.json',
           'precall_path_freeze_audit.json','evidence_binding_audit.json','manual_final_review.json',
           'api_process.json','api_process_finished.json','harness_runtime_routing.json']
    for name in names:
        emit({'file':name,'content':read(CAND/name)})
    for name in ['binding.json','summary.json','run_01_started.json','run_02_started.json']:
        emit({'file':name,'content':read(TEST/name)})
elif mode=='context':
    c=read(CAND/'fresh_context.json')
    emit({'context_keys':list(c),'nonobject_context':{k:v for k,v in c.items() if k not in ('objects','targets','snap_points')}})
    s=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane233.json')
    emit({'source_scene_nonobjects':{k:v for k,v in s.items() if k!='objects'},
          'all_source_objects_compact':[(o['id'],o['type'],o.get('points')) for o in s['objects']]})
elif mode=='histories':
    paths=[BATCH/'background_06/plane_parts/Plane233/local_cross_global_tiling',
           BATCH/'background_06/plane_parts/Plane233/two_U_partial_partition_binding',
           BATCH/'background_23/Plane233/r23_exterior_notch_correspondence']
    for path in paths:
        for name in ['design.json','plugin.json','primary_review.json','primary_post_test_review.json','manual_final_review.json']:
            p=path/name
            if p.exists():
                v=read(p)
                omit=('per_marker_roles','all_originals','old_original_variants','preceding_new_design_full_artifacts_read',
                      'originals_manifest','all_hashed_files','files','frozen_input_manifest')
                v={k:x for k,x in v.items() if k not in omit and not (isinstance(x,dict) and len(x)>15)}
                if name=='plugin.json':v={'actions':v['params']['actions'],'description':v.get('description'),'intent':v.get('intent')}
                emit({'file':str(p.relative_to(ROOT)),'content':prose(v)})
    emit({'finite_hypotheses':read(BATCH/'background_23/Plane233/finite_hypothesis_assessment.json')})
