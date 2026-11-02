import review_bootstrap as r
import ast
import base64
import io
import json
import sys
import traceback
from fractions import Fraction as F

checks={}
def check(name, condition, details=None):
    checks[name]={'passed':bool(condition)}
    if details is not None: checks[name]['details']=details

def main():
    isolation=r.bridge()
    sys.path.insert(0,str(r.PROJECT/'PlaneGeometry/workbench'))
    from dataset_tools import catalog
    from workbench_io import load_config, environment_versions, pixel_hash
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from dataset_tools.mathvision_workbench import png_bytes
    from render_plugins import check_schema
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt

    branch=r.PROJECT/'PlaneGeometry'
    qid='Plane461'
    row=next(x for x in catalog.rows(branch/'dataset.jsonl') if x['id']==qid)
    expected=next(x for x in r.read(r.UNIT/'assignment.json')['questions'] if x['question_id']==qid)
    approval=r.read(r.PROJECT/'provenance/approvals.json')['approvals'][qid]
    fingerprint=catalog.digest(catalog.content(r.PROJECT,'PlaneGeometry',row))
    check('current_formal_row_exact_frozen_assignment',row==expected['formal_record'])
    check('original_approval_current_content_exact',fingerprint==approval['content_sha256']==expected['current_content_sha256'])
    source_checks=[]
    for path,digest in expected['frozen_source_files_sha256'].items():
        source_checks.append({'path':path,'expected':digest,'current':r.sha(r.PROJECT/path)})
    check('all_target_frozen_source_hashes_exact',all(x['expected']==x['current'] for x in source_checks))
    special={}
    for name in ('accepted_index.jsonl','collected_index.jsonl'):
        path=branch/'special_variant'/name
        special[name]=[x for x in catalog.rows(path) if x.get('question_id',x.get('id'))==qid] if path.exists() else []
    for name in ('recipes.json','collection.json'):
        path=branch/'special_variant'/qid/name
        special[name]=r.read(path) if path.exists() else None
    check('current_target_no_Pass_Collect',not any(special.values()))
    r.save(r.OWN/'current_eligibility.json',{'checked_at':r.now(),'formal_record':row,'approval':approval,
        'current_content_sha256':fingerprint,'source_checks':source_checks,'special_state':special,
        'authority_file_hashes':{p:r.sha(r.PROJECT/p) for p in ('PlaneGeometry/dataset.jsonl','provenance/approvals.json','PlaneGeometry/special_variant/accepted_index.jsonl','PlaneGeometry/special_variant/collected_index.jsonl')}})

    cfg=load_config()
    cfg['runtime_dir']=str(r.OWN/'ownruntime/workbench')
    cfg['output_dir']=str(r.OWN/'ownruntime/outputs')
    ad=RendererAdapter(cfg)
    meta=ad.inspect_question(qid)
    saved=r.read(r.CAND/'context.json')
    check('fresh_adapter_context_exact_JSON_types_order_keys_values',json.dumps(meta,ensure_ascii=False)==json.dumps(saved,ensure_ascii=False))
    r.save(r.OWN/'fresh_context.json',meta)
    scene=ad.scene(qid)
    try:
        noop=png_bytes(scene)
        base_artist={k:[{'class':type(a).__name__,'linewidth':float(a.get_linewidth()),
            'linestyle':str(a.get_linestyle()),'visible':bool(a.get_visible()),
            'edgecolor':str(a.get_edgecolor()) if hasattr(a,'get_edgecolor') else str(a.get_color()),
            'facecolor':str(a.get_facecolor()) if hasattr(a,'get_facecolor') else None} for a in v]
            for k,v in scene.artists.items()}
        r.save(r.OWN/'original_artist_styles.json',base_artist)
    finally: scene.close()
    (r.OWN/'noop.png').write_bytes(noop)
    check('noop_formal_pixels_exact',pixel_hash(noop)==pixel_hash(branch/row['image'])==saved['original_pixel_sha256'])
    check('noop_original_byte_hash_matches_primary_noop',r.sha(r.OWN/'noop.png')==r.sha(r.UNIT/qid/'native_noop.png'))
    plugin=r.read(r.CAND/'plugin.json')
    renderer=PluginRenderer(cfg,ad,{qid:meta})
    check_schema(plugin,renderer.schema,renderer.schema)
    normalized,data,ph=renderer.render(plugin,frozen=True)
    check('schema_and_frozen_normalization_exact',list(normalized)==list(plugin) and json.dumps(normalized,ensure_ascii=False)==json.dumps(plugin,ensure_ascii=False))
    (r.OWN/'replayed_candidate.png').write_bytes(data)
    check('candidate_PNG_byte_exact',data==(r.CAND/'candidate.png').read_bytes())
    check('candidate_pixels_exact',ph==pixel_hash(r.CAND/'candidate.png'))
    check('six_unique_whole_original_objects_only',len(plugin['params']['actions'])==6 and
        [x['target'] for x in plugin['params']['actions']]==['o14','o15','o40','o41','o42','o43'] and
        all(x['type']=='set_object_style' and 'interval' not in x and set(x)=={'type','target','color','linewidth_pt'} for x in plugin['params']['actions']))
    a=np.array(Image.open(io.BytesIO(noop)).convert('RGBA'))
    b=np.array(Image.open(io.BytesIO(data)).convert('RGBA'))
    diff=np.any(a!=b,axis=2)
    yy,xx=np.where(diff)
    check('opaque_native_768_square',a.shape==b.shape==(768,768,4) and bool(np.all(b[:,:,3]==255)))
    # Exact changed-pixel coordinates retained; bounds are diagnostics, never a tolerance gate.
    r.save(r.OWN/'pixel_change_coordinates.json',np.argwhere(diff).tolist())
    r.save(r.OWN/'replay.json',{'at':r.now(),'isolation':isolation,'environment':environment_versions(),
        'schema_sha256':r.sha(branch/'workbench/plugin.schema.json'),
        'adapter_sha256':r.sha(branch/'workbench/mathvision_adapter.py'),
        'plugin_executor_sha256':r.sha(branch/'workbench/mathvision_plugins.py'),
        'formal_pixel_sha256':pixel_hash(noop),'candidate_pixel_sha256':ph,'candidate_png_sha256':r.sha(r.OWN/'replayed_candidate.png'),
        'noop_png_sha256':r.sha(r.OWN/'noop.png'),'formal_png_sha256':r.sha(branch/row['image']),
        'context_JSON_exact':checks['fresh_adapter_context_exact_JSON_types_order_keys_values']['passed'],
        'changed_pixel_count':int(diff.sum()),'changed_bbox':[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())],
        'figures_remaining':plt.get_fignums(),'geometry_projection_visibility':'Plane 2D scene; frozen viewport, complete object paths, original line styles and labels preserved by unchanged adapters. No 3D inputs.'})
    check('no_open_matplotlib_figures',plt.get_fignums()==[])

    tests=list((r.CAND/'tests').glob('quicktest3_*'))
    check('exactly_one_candidate_test_invocation',len(tests)==1)
    test=tests[0]
    binding=r.read(test/'binding.json'); summary=r.read(test/'summary.json'); design=r.read(r.CAND/'design.json')
    request=r.read(test/'request.json')
    check('predeclared_D_before_both_requests',design['expected_wrong_answer']==binding['expected_wrong_answer']=='D' and design['created_at']<binding['created_at']<r.read(test/'run_01_started.json')['started_at']<r.read(test/'run_02_started.json')['started_at'])
    check('design_snapshot_bytes_exact',(test/'design_snapshot.json').read_bytes()==(r.CAND/'design.json').read_bytes())
    check('binding_paths_exact',binding['image_path']==str(r.CAND/'candidate.png') and binding['design_path']==str(r.CAND/'design.json') and summary['evidence_dir']==str(test))
    check('binding_image_design_request_hashes_exact',binding['image_sha256']==r.sha(r.CAND/'candidate.png') and binding['design_sha256']==r.sha(r.CAND/'design.json') and binding['request_body_sha256']==r.sha(test/'request.json') and binding['pixel_sha256']==ph)
    check('binding_formal_record_hash_exact',binding['question_record_sha256']==catalog.digest(row))
    # Only parse constants; do not import quick_test or the transport harness.
    constants={}
    for node in ast.parse((branch/'workbench/quick_test.py').read_text(encoding='utf-8')).body:
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name) and target.id in ('SYSTEM_PROMPT','TEST_PROFILES'):
                    constants[target.id]=ast.literal_eval(node.value)
    check('request_exact_configured_system_formal_text_PNG_only',request=={
        'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},
        'messages':[{'role':'system','content':constants['SYSTEM_PROMPT']},
                    {'role':'user','content':[{'type':'text','text':row['question']},
                    {'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(data).decode('ascii')}}]}]})
    check('request_exact_serialized_bytes',json.dumps(request,ensure_ascii=False).encode('utf-8')==(test/'request.json').read_bytes())
    check('quicktest_reference_hash_exact',binding['reference_quick_test_sha256']==r.sha(branch/'workbench/quick_test.py'))
    check('binding_settings_exact',binding['profile']=='quicktest3' and binding['settings']=={**constants['TEST_PROFILES']['quicktest3'],'api_base':'https://token-plan-cn.xiaomimimo.com/v1'})
    check('summary_binding_all_keys_exact',all(summary[k]==v for k,v in binding.items()))
    check('exactly_two_actual_run_files',sorted(p.name for p in test.glob('run_*.json'))==['run_01.json','run_01_response.json','run_01_started.json','run_02.json','run_02_response.json','run_02_started.json'])
    readings=[]
    for i in (1,2):
        stem=f'run_{i:02d}'
        raw=r.read(test/(stem+'_response.json')); job=r.read(test/(stem+'.json')); start=r.read(test/(stem+'_started.json'))
        audit=r.read(r.CAND/f'actual_request_{i:02d}_audit.json')
        choice=raw['choices'][0]
        check(stem+'_complete_nontruncated_raw_exact',len(raw['choices'])==1 and job['status']=='completed' and job['http_status']==200 and job['finish_reason']==choice['finish_reason']=='stop' and not job['truncated'] and job['answer']==choice['message']['content'] and job['thinking']=='' and job['usage']==raw['usage'] and job['response_model']==raw['model']=='mimo-v2.6-flash' and job['response_sha256']==r.sha(test/(stem+'_response.json')) and job==summary['results'][i-1])
        check(stem+'_immutable_start_binding_and_actual_request',all(start[k]==job[k] for k in start) and all(job[k]==binding[k] for k in ('image_sha256','design_sha256','request_body_sha256')) and audit['request_body_sha256']==binding['request_body_sha256'] and audit['url']=='https://token-plan-cn.xiaomimimo.com/v1/chat/completions' and all(audit['frozen'][n]==r.sha(r.CAND/n) for n in ('candidate.png','plugin.json','design.json','context.json')))
        readings.append({'run_index':i,'raw_response_path':str(test/(stem+'_response.json')),'raw_sha256':r.sha(test/(stem+'_response.json')),'raw_provider_id':raw['id'],'full_content':choice['message']['content'],'full_characters':len(choice['message']['content']),'finish_reason':choice['finish_reason'],'final_letter_personally_read':'D','preset_value':'D central four-hole cluster','value_reading_caveat':('Explicit D selection and central four-hole intent; cardinal cross described in prose is not the actual square of D. Do not rewrite this narrative into geometric correctness.' if i==1 else 'Explicit central four-hole cluster and D; falsely interprets the annotation colors as overlapping physical paper layers.'),'full_raw_personally_read':True})
    check('distinct_provider_response_ids_and_run_ids',r.read(test/'run_01_response.json')['id']!=r.read(test/'run_02_response.json')['id'] and r.read(test/'run_01.json')['run_id']!=r.read(test/'run_02.json')['run_id'])
    completed=r.read(r.CAND/'process_completed.json')
    check('actual_transport_process_exactly_two_exit_zero',completed['actual_urllib_request_count']==2 and completed['exit_code']==0 and completed['frozen_inputs_unchanged'])
    r.save(r.OWN/'complete_raw_readings.json',readings)

    # Exact rational proof derived from actual frozen geometry, not approved answer.
    g={x['id']:x['geometry'] for x in saved['objects']}
    xy=lambda v: tuple(F(str(x)) for x in v)
    punch=xy(g['o13']['center'])
    translated=(punch[0]-10,punch[1]-F('4.7')+1)
    orbit=sorted((x,y) for x in (translated[0],4-translated[0]) for y in (translated[1],2-translated[1]))
    options={}
    for j,letter in enumerate('ABCDE'):
        first=19+7*j
        centers=sorted((xy(g[f'o{k}']['center'])[0]-6*j,xy(g[f'o{k}']['center'])[1]) for k in range(first,first+4))
        options[letter]={'centers_exact':[[str(x),str(y)] for x,y in centers],'equals_orbit':centers==orbit,'radii':[str(F(str(g[f'o{k}']['radius']))) for k in range(first,first+4)]}
    check('independent_exact_unique_answer_B',[k for k,v in options.items() if v['equals_orbit']]==['B'])
    source_slopes={k:(xy(g[k]['points'][1])[1]-xy(g[k]['points'][0])[1])/(xy(g[k]['points'][1])[0]-xy(g[k]['points'][0])[0]) for k in ('o14','o15')}
    pair_slope=lambda a,b:(xy(g[b]['center'])[1]-xy(g[a]['center'])[1])/(xy(g[b]['center'])[0]-xy(g[a]['center'])[0])
    r.save(r.OWN/'independent_math.json',{'method':'Exact Fraction arithmetic on decimal JSON coordinates; no tolerance, numeric solver or API. Physical fold directions independently read from JPG and formal PNG.',
        'fold_maps':'Fold y<1 to 2-y, then x<2 to 4-x; retained packet [2,4]x[1,2]. Display final packet is shifted +10 in x and +3.7 in y.',
        'punch_retained_coordinates':[str(x) for x in translated],'inverse_orbit':[[str(x),str(y)] for x,y in orbit],
        'radius':str(F(str(g['o13']['radius']))),'minimum_clearance_to_packet_boundaries':str(F('0.25')-F('0.22')),
        'why_complete':'Both fold maps are independent two-to-one reflections off their axes. Interior disk radius 11/50 does not touch either fold or free edge: minimum center distance 1/4, clearance 3/100. Exactly four disjoint congruent disks, one from each preimage. Enumerate all five unchanged option center sets and radii.',
        'options':options,'unique_answer':'B','source_X_slopes':{k:str(v) for k,v in source_slopes.items()},
        'D_same_color_pair_slopes':{'red_o41_o42':str(pair_slope('o41','o42')),'blue_o40_o43':str(pair_slope('o40','o43'))},
        'unordered_commonality':'Both X and D opposite-hole pairs form an unordered pair of perpendicular diagonals with slopes +1 and -1. This is a real coarse shape resemblance; frozen same-color identities reverse the two directions.'})

    # Rehash initial old evidence from primary manifest without editing it.
    old_checks=[]
    for entry in r.read(r.UNIT/'readonly_inputs_initial.json')['files']:
        old_checks.append({'path':entry['path'],'expected':entry['sha256'],'current':r.sha(entry['path'])})
    check('primary_initial_160_readonly_evidence_hashes_exact',all(x['expected']==x['current'] for x in old_checks))
    r.save(r.OWN/'old_readonly_preservation.json',old_checks)
    check('current_reference_C01_exact_frozen_copy',r.sha(r.REF/'C01.png')==r.sha(branch/'special_variant/Plane217/images/C01.png') and r.sha(r.REF/'C01.json')==r.sha(branch/'special_variant/Plane217/plugins/C01.json'))
    oldh=r.read(r.PROJECT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py') if False else (r.PROJECT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py').read_bytes()
    local=(r.UNIT/'harness/quicktest3_isolated.py').read_bytes()
    ha=r.read(r.UNIT/'harness/isolation_audit.json')
    check('canonical_harness_only_recorded_runtime_root_substitution',r.sha(r.PROJECT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py')==ha['original_sha256'] and local.replace(ha['allowed_substitutions']['new'].encode(),ha['allowed_substitutions']['old'].encode())==oldh)
    r.save(r.OWN/'integrity_checks.json',{'at':r.now(),'checks':checks,'failed_checks':[k for k,v in checks.items() if not v['passed']],
        'candidate_hashes':{n:r.sha(r.CAND/n) for n in ('candidate.png','plugin.json','design.json','context.json','reference_transfer.json','primary_final_review.json','primary_posttest_geometry_caveats.json')},
        'test_hashes':{p.name:r.sha(p) for p in sorted(test.iterdir()) if p.is_file()},
        'review_new_solver_API_calls':0,'interpretation':'These checks establish offline integrity and current eligibility, not targeted usefulness or user approval.'})
    print(json.dumps({'checks':len(checks),'failed_checks':[k for k,v in checks.items() if not v['passed']],'math':options,'replay':r.read(r.OWN/'replay.json')},ensure_ascii=False))

if __name__=='__main__':
    try: main()
    except BaseException as exc:
        r.save(r.OWN/('offline_error_'+r.now().replace(':','_')+'.json'),{'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc(),'completed_checks':checks})
        raise
