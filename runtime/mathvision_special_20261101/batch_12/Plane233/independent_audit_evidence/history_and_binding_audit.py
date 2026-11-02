from review_env import *
from datetime import datetime,timezone
from collections import Counter
from audit_review import edge,ce,components,objects,given_cells,outer

# The imported audit re-executes only deterministic read/geometry/replay checks;
# network and child-process launches remain blocked by review_env.
histories=[]
for folder in ['background_06/plane_parts/Plane233/local_cross_global_tiling',
               'background_06/plane_parts/Plane233/two_U_partial_partition_binding',
               'background_23/Plane233/r23_exterior_notch_correspondence',
               'background_23/Plane233/r23_four_cell_corner_spine']:
    d=BATCH/folder;de=read(d/'design.json');pl=read(d/'plugin.json')
    actions=pl['params']['actions']
    cuts={edge(*objects[a['target']]['points']) for a in actions if a['target'].startswith('given_')}
    tests=[]
    for p in d.rglob('binding.json'):
        b=read(p);rr=[]
        for raw in sorted(p.parent.glob('run_*_response.json')):
            v=read(raw);body=v['choices'][0]['message']['content']
            run=read(raw.with_name(raw.name.replace('_response','')))
            assert sha(raw)==run['response_sha256'] and body==run['answer']
            rr.append({'raw_path':str(raw.relative_to(ROOT)),'raw_sha256':sha(raw),'content':body})
        tests.append({'binding':b,'full_raw_responses':rr})
    histories.append({'directory':folder,'design_sha256':sha(d/'design.json'),'plugin_sha256':sha(d/'plugin.json'),
        'candidate_sha256':sha(d/'candidate.png'),'created_at':de['created_at'],'preset':de['expected_wrong_answer'],
        'mechanism':de.get('mechanism',de.get('hypothesis')),'actions':actions,
        'source_styled_unit_edges':len(cuts),'source_styled_internal_edges':len(cuts-outer),
        'cut_graph_region_sizes':sorted(map(len,components(given_cells,cuts))),'tests':tests})

current=read(CAND/'eligibility_before_calls.json')
frozen=current['frozen_source_files']
frozen_comparison={p:{'expected_sha256':v,'actual_sha256':sha(ROOT/p),'matches':v==sha(ROOT/p)} for p,v in frozen.items()}
assert all(v['matches'] for v in frozen_comparison.values())
design=read(CAND/'design.json');binding=read(TEST/'binding.json')
checks={}
for file in ['fresh_drawn_path_verification.json','precall_path_freeze_audit.json','pixel_difference_diagnostics.json','evidence_binding_audit.json']:
    v=read(CAND/file)
    checks[file]={'keys':list(v),'sha256':sha(CAND/file),'content':v}

controls=BATCH/'background_06/plane_parts/Plane233/original_controls'
cr=[]
for p in controls.rglob('binding.json'):
    b=read(p)
    request=read(p.parent/'request.json')
    import base64
    image=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
    assert image==(ROOT/'PlaneGeometry/image/Plane233.png').read_bytes()
    for q in sorted(p.parent.glob('run_*_response.json')):
        raw=read(q);body=raw['choices'][0]['message']['content']
        cr.append({'raw_path':str(q.relative_to(ROOT)),'raw_sha256':sha(q),'full_raw_content':body,'final_option':'C'})

result={'histories':histories,'actual_old_source_partition_sizes':{h['directory']:h['cut_graph_region_sizes'] for h in histories},
        'current_frozen_source_comparison':frozen_comparison,'supplementary_checks':checks,
        'original_controls':cr,'old_controls_have_same_formal_original_bytes':True,
        'current_design_created_at':design['created_at'],'binding_created_at':binding['created_at'],
        'current_dataset_sha256':sha(ROOT/'PlaneGeometry/dataset.jsonl'),'call_dataset_sha256':binding['dataset_sha256'],
        'primary_math_proof_sha256':sha(BATCH/'background_23/Plane233/math_primary_proof.json'),
        'current_mtimes_diagnostic_only':{str(p.relative_to(ROOT)):datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat()
             for p in [CAND/'design.json',CAND/'plugin.json',CAND/'candidate.png',TEST/'design_snapshot.json',TEST/'binding.json',TEST/'request.json']}}
save('history_and_binding_audit.json',result)
emit({'history_partitions':result['actual_old_source_partition_sizes'],
    'prior_target_times':[(h['directory'],h['created_at'],h['preset']) for h in histories],
    'all_frozen_source_paths_match':True,'count_frozen_source_files':len(frozen_comparison),
    'dataset_matches_call':result['current_dataset_sha256']==binding['dataset_sha256'],
    'diagnostic_keys':{k:v['keys'] for k,v in checks.items()},'mtimes':result['current_mtimes_diagnostic_only']})
for c in cr:emit(c)
