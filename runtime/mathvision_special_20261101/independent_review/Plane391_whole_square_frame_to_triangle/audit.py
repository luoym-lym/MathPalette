from pathlib import Path
import os
import sys
import json
import hashlib
import importlib.util

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
sys.dont_write_bytecode = True
for name, sub in [('TEMP','temp'),('TMP','temp'),('TMPDIR','temp'),('MPLCONFIGDIR','mpl'),('XDG_CACHE_HOME','cache'),('PYTHONPYCACHEPREFIX','pycache')]:
    path = OUT / sub
    path.mkdir(exist_ok=True)
    os.environ[name] = str(path)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['MPLBACKEND'] = 'Agg'

def allowed(path):
    if path is None or isinstance(path, int):
        return
    p = Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(OUT):
        raise PermissionError('Independent review write outside assigned directory: ' + str(p))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        allowed(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        allowed(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        allowed(args[0]); allowed(args[1])
    elif event in ('socket.connect','subprocess.Popen','os.system'):
        raise PermissionError('No network or child processes in independent audit')

sys.addaudithook(guard)
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location('review_runtime_isolation', ROOT / 'runtime/mathvision_special_20261101/runtime_isolation.py')
isolation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(isolation)
ISOLATION = isolation.install(OUT / 'render_tmp', guard_writes=True)

BASE = ROOT / 'runtime/mathvision_special_20261101/background_09/Plane391'
CAND = BASE / 'whole_square_frame_to_triangle'
def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def rel(path):
    return str(Path(path).resolve().relative_to(ROOT)).replace('\\','/')
def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
def compact(value, key=''):
    if isinstance(value, dict):
        if key == 'files' and len(value) > 80:
            return {'_total_entries':len(value), '_Plane391_and_authorities':{k:v for k,v in value.items() if '391' in k or k in ('provenance\\approvals.json','PlaneGeometry\\dataset.jsonl','provenance\\source_notes.json')}}
        return {k:compact(v,k) for k,v in value.items()}
    if isinstance(value, list):
        return [compact(v,key) for v in value]
    if isinstance(value,str) and len(value)>15000:
        return {'_length':len(value),'_sha256':hashlib.sha256(value.encode()).hexdigest(),'_prefix':value[:200]}
    return value

def technical():
    import io
    import base64
    import math
    from datetime import datetime, timezone
    from fractions import Fraction as F
    from itertools import combinations
    import numpy as np
    from PIL import Image
    sys.path.insert(0, str(ROOT/'PlaneGeometry/workbench'))
    from workbench_io import load_config, canonical_hash, pixel_hash, environment_versions
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from partial_style import object_paths, apply_partial_styles
    from dataset_tools.catalog import content, digest, validate_formal_row
    from dataset_tools.mathvision_workbench import png_bytes
    from quick_test import TEST_PROFILES, SYSTEM_PROMPT, parse_response
    rows=lambda p:[json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []
    row=next(r for r in rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']=='Plane391')
    input_paths=[ROOT/'PlaneGeometry'/p for p in [row[k] for k in ('image','original_image','scene','script')]+row['runtime_dependencies']]
    input_paths += [ROOT/p for p in ['dataset_tools/geometry_dataset.py','dataset_tools/mathvision_workbench.py','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/dataset_generator/common_renderer.py','MATHPALETTE_PROTOCOL.md','PlaneGeometry/workbench/plugin.schema.json','PlaneGeometry/workbench/mathvision_adapter.py','PlaneGeometry/workbench/mathvision_plugins.py','PlaneGeometry/workbench/partial_style.py','PlaneGeometry/workbench/render_plugins.py','PlaneGeometry/workbench/quick_test.py']]
    evidence_paths=[p for p in BASE.rglob('*') if p.is_file()]
    before={rel(p):sha(p) for p in evidence_paths+input_paths}
    dump('read_only_start_hashes.json',before)
    approval=read(ROOT/'provenance/approvals.json')['approvals']['Plane391']
    validate_formal_row(ROOT,'PlaneGeometry',row)
    current_content=content(ROOT,'PlaneGeometry',row)
    approval_digest=digest(current_content)
    authorities={}
    hits={}
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p=ROOT/'PlaneGeometry/special_variant'/name
        rr=rows(p)
        hits[name]=[r for r in rr if r.get('question_id',r.get('id'))=='Plane391']
        authorities[rel(p)]=sha(p) if p.exists() else None
    for name in ['recipes.json','collection.json']:
        p=ROOT/'PlaneGeometry/special_variant/Plane391'/name
        hits[name]=read(p) if p.exists() else None
        authorities[rel(p)]=sha(p) if p.exists() else None
    for name in ['PlaneGeometry/dataset.jsonl','provenance/approvals.json','provenance/source_notes.json']:
        authorities[name]=sha(ROOT/name)
    manifests={rel(p):{'sha256':sha(p),'contains_Plane391':'Plane391' in p.read_text(encoding='utf-8-sig')} for p in (ROOT/'runtime/mathvision_special_20261101').glob('batch_*/manifest.json')}
    eligible=row['source_dataset']=='MathVision' and approval_digest==approval['content_sha256'] and approval['reviewer']=='user' and bool(approval['instruction']) and not any(hits.values()) and not any(x['contains_Plane391'] for x in manifests.values())
    eligibility={'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':eligible,'row_matches_frozen_record':row==read(BASE/'formal_record.json'),'formal_record':row,'approval':approval,'recomputed_content_sha256':approval_digest,'approval_matches':approval_digest==approval['content_sha256'],'approved_file_hashes_current':current_content['files'],'authoritative_state_hashes':authorities,'authoritative_Plane391_records':hits,'delivered_manifest_checks':manifests}
    dump('current_eligibility.json',eligibility)
    historical=read(BASE/'input_fingerprints.json')
    changes=[]
    for name,old in historical['files'].items():
        p=ROOT/name
        new=sha(p) if p.exists() else None
        if new!=old:changes.append({'path':rel(p),'frozen':old,'current':new,'candidate_input':p.resolve() in {x.resolve() for x in input_paths}})
    eligibility_old=read(CAND/'eligibility_immediately_before_calls.json')
    progress=[]
    for name,old in eligibility_old['diagnostic_runtime_metadata']['hashes'].items():
        p=ROOT/name
        progress.append({'path':rel(p),'frozen':old,'current':sha(p),'drift':sha(p)!=old,'classification':'mutable runtime progress metadata, not frozen mathematical or model evidence'})
    dump('historical_input_comparison.json',{'question_record_matches':canonical_hash(row)==historical['question_record_sha256'],'environment_current':environment_versions(),'environment_frozen':historical['environment'],'checked_files':len(historical['files']),'changes':changes,'all_relevant_inputs_unchanged':not any(x['candidate_input'] for x in changes),'progress_metadata':progress})
    # Exact rational polygon audit, independent of primary mathematical calculations.
    scene=read(ROOT/'PlaneGeometry'/row['scene'])
    polygons={o['id']:[tuple(F(v) for v in scene['points'][p]) for p in o['points']] for o in scene['objects']}
    def cross(a,b):return a[0]*b[1]-a[1]*b[0]
    def sub(a,b):return (a[0]-b[0],a[1]-b[1])
    def twice(poly):return sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1]))
    def area(poly):return abs(twice(poly))/2
    def clip(subject,bound):
        sign=1 if twice(bound)>0 else -1
        out=subject[:]
        for a,b in zip(bound,bound[1:]+bound[:1]):
            inp=out;out=[]
            if not inp:break
            e=sub(b,a)
            for p,q in zip(inp,inp[1:]+inp[:1]):
                cp=sign*cross(e,sub(p,a));cq=sign*cross(e,sub(q,a))
                if cp>=0:out.append(p)
                if (cp<0 and cq>=0) or (cp>=0 and cq<0):
                    t=cp/(cp-cq)
                    out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        return out
    inventory={}
    for name,poly in polygons.items():
        vectors=[sub(b,a) for a,b in zip(poly,poly[1:]+poly[:1])]
        sides2=[v[0]**2+v[1]**2 for v in vectors]
        right=[i for i in range(len(poly)) if sum(x*y for x,y in zip(vectors[i-1],vectors[i]))==0]
        inventory[name]={'vertices':[[str(v) for v in p] for p in poly],'area':str(area(poly)),'squared_side_lengths':[str(x) for x in sides2],'right_angle_vertex_indices':right,'kind':'square' if len(poly)==4 else 'right_isosceles_triangle'}
    overlaps=[];adjacency=[]
    for names in [[f'piece{i}' for i in range(4)],[f'piece{i}' for i in range(4,11)]]:
        for x,y in combinations(names,2):
            inter=clip(polygons[x],polygons[y]);ar=area(inter) if len(inter)>2 else F(0)
            overlaps.append({'a':x,'b':y,'intersection_area':str(ar)})
            common=[]
            for a,b in zip(polygons[x],polygons[x][1:]+polygons[x][:1]):
                for c,d in zip(polygons[y],polygons[y][1:]+polygons[y][:1]):
                    e=sub(b,a)
                    if cross(e,sub(c,a))==0 and cross(e,sub(d,a))==0:
                        axis=0 if e[0] else 1
                        lo=max(min(a[axis],b[axis]),min(c[axis],d[axis]));hi=min(max(a[axis],b[axis]),max(c[axis],d[axis]))
                        if hi>lo:
                            ends=[]
                            for t in [lo,hi]:
                                u=(t-a[axis])/e[axis];ends.append([str(a[0]+u*e[0]),str(a[1]+u*e[1])])
                            common.append(ends)
            if common:adjacency.append({'a':x,'b':y,'shared_boundary_segments':common})
    math_audit={'method':'Independent exact rational shoelace, side vectors/right-angle dot products, convex half-plane polygon intersections, and collinear common-boundary intervals. Frozen coordinates verify the pictorial inventory; they are not extra givens.','inventory':inventory,'source_total':str(sum(area(polygons[f'piece{i}']) for i in range(4))),'assembly_total':str(sum(area(polygons[f'piece{i}']) for i in range(4,11))),'pairwise_intersections':overlaps,'all_interiors_disjoint':all(x['intersection_area']=='0' for x in overlaps),'edge_adjacency':adjacency}
    dump('independent_math_audit.json',math_audit)
    cfg=load_config();cfg['runtime_dir']=str(OUT/'render_state');cfg['output_dir']=str(OUT/'render_output')
    adapter=RendererAdapter(cfg)
    meta=adapter.inspect_question('Plane391')
    plugin=read(CAND/'plugin.json')
    renderer=PluginRenderer(cfg,adapter,{'Plane391':meta})
    normalized=renderer.normalize(plugin)
    _,png,pix=renderer.render(plugin,frozen=True)
    _,png2,pix2=renderer.render(plugin,frozen=True)
    (OUT/'replayed_candidate.png').write_bytes(png)
    baseline=adapter.scene('Plane391')
    try:
        baseline.fig.canvas.draw()
        base_png=png_bytes(baseline)
        (OUT/'replayed_original.png').write_bytes(base_png)
        path_audit=[]
        for action in plugin['params']['actions']:
            pp=object_paths(baseline,action['target'])[0]
            controls=[x['control'].tolist() for x in pp['segments']]
            n=len(controls);iv=action['interval']
            path_audit.append({'target':action['target'],'path_id':pp['id'],'current_path_sha256':pp['sha256'],'matches_frozen_interval':pp['sha256']==iv['path_sha256'],'matches_saved_path_controls':controls==read(CAND/'path_fingerprints.json')[action['target']][0]['exact_controls'],'closed_path':pp['closed'],'segment_count':n,'selected_segment_range':[iv['start']*n,iv['end']*n],'exact_controls':controls,'selected_controls':controls[round(iv['start']*n):round(iv['end']*n)],'pixels_per_unit':float(np.linalg.norm(baseline.ax.transData.transform([1,0])-baseline.ax.transData.transform([0,0])))})
        apply_partial_styles(baseline,plugin['params']['actions'])
        actual_strokes=[]
        for target in ['piece0','piece7','piece2','piece5','piece9']:
            for path in object_paths(baseline,target):
                for segment in path['segments']:
                    actual_strokes.append({'target':target,'controls':segment['control'].tolist(),'style':segment['style']})
    finally:baseline.close()
    frozen_native=read(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane391/scene.json')
    image_info={}
    for key,data in [('source', (ROOT/'PlaneGeometry'/row['original_image']).read_bytes()),('original',(BASE/'original.png').read_bytes()),('candidate',(CAND/'candidate.png').read_bytes()),('replay',png)]:
        im=Image.open(io.BytesIO(data));im.load()
        image_info[key]={'size':list(im.size),'mode':im.mode,'file_sha256':hashlib.sha256(data).hexdigest(),'pixel_sha256':pixel_hash(im),'alpha_extrema':list(im.convert('RGBA').getextrema()[3])}
    render={'isolation':ISOLATION,'strict_own_directory_guard_before_any_project_import':True,'network_and_subprocess_blocked':True,'normalized_equals_frozen_plugin':normalized==plugin,'baseline_pixel_matches_formal':pixel_hash(base_png)==pixel_hash(ROOT/'PlaneGeometry'/row['image']),'baseline_pixel_matches_saved_original':pixel_hash(base_png)==pixel_hash(BASE/'original.png'),'twice_identical_bytes':png==png2,'same_pixels':pix==pix2,'replay_byte_identical_to_tested_candidate':png==(CAND/'candidate.png').read_bytes(),'image_info':image_info,'current_metadata_equals_saved_context':meta==read(CAND/'context.json'),'native_and_canonical_geometry_equal':all(scene[k]==frozen_native[k] for k in ('points','objects','labels','constraints','view','ambiguities','distance_markers')),'paths':path_audit,'resulting_strokes':actual_strokes,'important_visible_overlap':'piece9 blue bottom edge (3,2)-(4,2) is later than and co-located with the right half of piece7 red horizontal leg (2,2)-(4,2). Final PNG shows only red (2,2)-(3,2) plus red vertical (4,2)-(4,0), separated by the blue unit segment; not a fully visible congruent red two-leg L.'}
    dump('independent_render_audit.json',render)
    def binding_audit(directory,image_path,design_path):
        testdirs=list((directory/'tests').iterdir());assert len(testdirs)==1
        test=testdirs[0];binding=read(test/'binding.json');req=read(test/'request.json');design=read(design_path)
        url=req['messages'][1]['content'][1]['image_url']['url'];embedded=base64.b64decode(url.split(',',1)[1],validate=True)
        expected_req={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},'messages':[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':[{'type':'text','text':row['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(image_path.read_bytes()).decode()}}]}]}
        runs=[]
        for i in (1,2):
            rp=test/f'run_{i:02d}.json';rawp=test/f'run_{i:02d}_response.json';started=read(test/f'run_{i:02d}_started.json');run=read(rp);raw=read(rawp);parsed=parse_response(raw,'mimo')
            checks={'start_fields_match':all(run[k]==v for k,v in started.items()),'request_hash':run['request_body_sha256']==sha(test/'request.json')==binding['request_body_sha256'],'image_hash':run['image_sha256']==sha(image_path)==binding['image_sha256']==hashlib.sha256(embedded).hexdigest(),'design_hash':run['design_sha256']==sha(design_path)==binding['design_sha256']==sha(test/'design_snapshot.json'),'raw_response_hash':sha(rawp)==run['response_sha256'],'raw_content_matches_run_answer':raw['choices'][0]['message']['content'].strip()==run['answer'],'parse_response_fields_match':all(run[k]==v for k,v in parsed.items()),'complete':run['status']=='completed' and run['http_status']==200 and not run['truncated'] and raw['choices'][0]['finish_reason']=='stop','no_thinking':run['thinking']=='' and run['usage']['completion_tokens_details']['reasoning_tokens']==0,'preset_before_call':design['created_at']<binding['created_at']<run['started_at'],'profile_model':'mimo-v2.6-flash'==raw['model']==run['response_model']}
            runs.append({'run_index':i,'checks':checks,'run_path':rel(rp),'run_sha256':sha(rp),'raw_path':rel(rawp),'raw_sha256':sha(rawp),'started_at':run['started_at'],'finished_at':run['finished_at'],'provider_created':raw['created'],'full_raw_assistant_content':raw['choices'][0]['message']['content'],'usage':run['usage'],'finish_reason':run['finish_reason']})
        summary=read(test/'summary.json')
        checks={'exact_reference_request_no_leak':req==expected_req,'embedded_image_bytes_equal':embedded==image_path.read_bytes(),'preset_matches_frozen_design_and_snapshot':binding['expected_wrong_answer']==design['expected_wrong_answer']==read(test/'design_snapshot.json')['expected_wrong_answer'],'settings_match_profile_and_endpoint':binding['settings']=={**TEST_PROFILES['quicktest3'],'api_base':'https://token-plan-cn.xiaomimimo.com/v1'},'quicktest_source_hash_current':sha(ROOT/'PlaneGeometry/workbench/quick_test.py')==binding['reference_quick_test_sha256'],'record_hash_current':canonical_hash(row)==binding['question_record_sha256'],'formal_question_exact':binding['question']==row['question'],'exactly_two_started_and_completed_files':len(list(test.glob('run_*_started.json')))==2 and len(list(test.glob('run_*_response.json')))==2 and len(list(test.glob('run_[0-9][0-9].json')))==2,'summary_matches_both_runs':summary['results']==[read(test/f'run_{i:02d}.json') for i in (1,2)],'two_completed':summary['two_completed'],'nonoverlapping_sequential_calls':runs[0]['finished_at']<runs[1]['started_at'],'all_run_checks':all(all(r['checks'].values()) for r in runs)}
        return {'evidence_directory':rel(test),'binding_sha256':sha(test/'binding.json'),'request_sha256':sha(test/'request.json'),'design_sha256':sha(design_path),'snapshot_sha256':sha(test/'design_snapshot.json'),'image_sha256':sha(image_path),'pixel_sha256':pixel_hash(image_path),'request_top_level_keys':list(req),'question':req['messages'][1]['content'][0]['text'],'design_created_at':design['created_at'],'binding_created_at':binding['created_at'],'expected_wrong_answer':binding['expected_wrong_answer'],'checks':checks,'runs':runs}
    cand_bind=binding_audit(CAND,CAND/'candidate.png',CAND/'design.json')
    control_bind=binding_audit(CAND/'original_control',BASE/'original.png',CAND/'original_control/design.json')
    dump('independent_binding_audit.json',{'candidate':cand_bind,'original_control':control_bind})
    # Look for repeated exact image tests; retain evidence of other predeclared designs.
    invocations=[]
    for p in (ROOT/'runtime/mathvision_special_20261101').rglob('binding.json'):
        if p.is_relative_to(OUT):continue
        data=read(p)
        if data.get('question_id')=='Plane391':
            invocations.append({'path':rel(p),'sha256':sha(p),'image_sha256':data.get('image_sha256'),'design_sha256':data.get('design_sha256'),'preset':data.get('expected_wrong_answer'),'created_at':data.get('created_at'),'completed_runs':[{'file':rp.name,'status':read(rp).get('status'),'answer':read(rp).get('answer')} for rp in p.parent.glob('run_[0-9][0-9].json')]})
    dump('Plane391_invocation_inventory.json',{'candidate_exact_image_invocation_count':sum(x['image_sha256']==sha(CAND/'candidate.png') for x in invocations),'all_Plane391_bindings_found':invocations,'scope_limit':'Available filesystem evidence and reviewed harness, not an external provider access log.'})
    after={rel(p):sha(p) for p in evidence_paths+input_paths}
    changes_during=[k for k,v in before.items() if after.get(k)!=v]
    dump('read_only_finish_hashes.json',{'hashes':after,'changed_existing_evidence_or_relevant_source_paths':changes_during})
    dump('technical_summary.json',{'eligible':eligible,'approval_matches':approval_digest==approval['content_sha256'],'unique_area':math_audit['assembly_total'],'all_interiors_disjoint':math_audit['all_interiors_disjoint'],'replay_matches':render['replay_byte_identical_to_tested_candidate'],'normalization_unchanged':normalized==plugin,'candidate_binding_checks':cand_bind['checks'],'control_binding_checks':control_bind['checks'],'all_candidate_run_checks':[all(r['checks'].values()) for r in cand_bind['runs']],'all_control_run_checks':[all(r['checks'].values()) for r in control_bind['runs']],'existing_evidence_and_relevant_sources_unchanged':not changes_during,'visible_red_L_fully_contiguous':False,'unrelated_historical_input_changes_count':len(changes)})
    print(json.dumps(read(OUT/'technical_summary.json'),ensure_ascii=False,indent=2))

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'technical':
        technical()
    elif mode == 'read':
        for item in sys.argv[2:]:
            p = ROOT / item
            print('FILE:', rel(p))
            print(json.dumps(compact(read(p)),ensure_ascii=False,indent=2))
    elif mode == 'checkpoint':
        for name in ['second_review_queue.json','checkpoint.json']:
            data=read(BASE.parent/name)
            if name=='checkpoint.json':
                def select(v):
                    if isinstance(v,dict):
                        return {k:select(x) for k,x in v.items() if not isinstance(x,(list,dict)) or k in ('aborts','transport_errors') or '391' in json.dumps(x)}
                    if isinstance(v,list):
                        return [select(x) for x in v if '391' in json.dumps(x)]
                    return v
                data=select(data)
            print(name,json.dumps(compact(data),ensure_ascii=False,indent=2))
    elif mode == 'details':
        c=read(CAND/'context.json')
        print('context_canvas',json.dumps(c['canvas'],ensure_ascii=False))
        q=read(BASE.parent/'second_review_queue.json')
        print('queue_relevant_structure',json.dumps({k:([{'keys':list(x),'candidate_id':x.get('candidate_id'),'status':x.get('status')} for x in v] if k=='candidates' else v) for k,v in q.items()},ensure_ascii=False))
        check=read(BASE.parent/'checkpoint.json')
        print('checkpoint_keys',list(check))
        print('checkpoint_scalars',{k:v for k,v in check.items() if not isinstance(v,(dict,list))})
        for k,v in check.items():
            if isinstance(v,list):
                selected=[x for x in v if isinstance(x,dict) and x.get('question_id')=='Plane391']
                print('checkpoint',k,'count',len(v),'Plane391',json.dumps([{a:b for a,b in x.items() if a not in ('complete_manual_finals',)} for x in selected],ensure_ascii=False))
        r=read(OUT/'independent_render_audit.json')
        print('render_checks',{k:v for k,v in r.items() if isinstance(v,bool)})
        print('image_info',r['image_info'])
        print('paths',json.dumps(r['paths'],ensure_ascii=False))
        print('harness_context',json.dumps(read(CAND/'harness_context.json'),ensure_ascii=False))
        p=read(BASE.parent/'process_audit.json')
        print('prior_process_audit_summary',{k:v for k,v in p.items() if k not in ('process_records','api_process_records','api_processes','finished_API_processes') and not isinstance(v,list)})
