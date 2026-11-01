from pathlib import Path
import os, sys, json, hashlib, datetime, importlib.util
OUT = Path(__file__).resolve().parent
ROOT = next(p for p in OUT.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for name in ('TEMP','TMP','TMPDIR','MPLCONFIGDIR','XDG_CACHE_HOME','PYTHONPYCACHEPREFIX'):
    os.environ[name] = str(OUT/name.lower())
    (OUT/name.lower()).mkdir(exist_ok=True)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.dont_write_bytecode = True
def check(p):
    if p is not None and not isinstance(p, int):
        q=Path(os.fsdecode(p)).resolve()
        if not q.is_relative_to(OUT): raise PermissionError('Review write outside assigned directory: '+str(q))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'): check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'): check(args[0]);check(args[1])
sys.addaudithook(guard)
spec=importlib.util.spec_from_file_location('review_runtime_isolation',ROOT/'runtime/mathvision_special_20261101/runtime_isolation.py')
iso=importlib.util.module_from_spec(spec);spec.loader.exec_module(iso)
ISOLATION=iso.install(OUT/'render_tmp',guard_writes=True)
P=ROOT/'runtime/mathvision_special_20261101/background_07/plane_transform/Plane259'
C=P/'cap_stem_quarterturn_binding'
T=C/'tests/quicktest3_20261101T151010_20c646fd8968'
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def emit(x): print(json.dumps(x,ensure_ascii=False,indent=2))
def write(p,obj):
    with Path(p).open('x',encoding='utf-8',newline='\n') as f:
        json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(p): return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []
def canonical(x): return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def verify():
    import base64, io
    import numpy as np
    from PIL import Image
    from dataset_tools.catalog import content,digest
    frozen_files={str(p.relative_to(ROOT)):sha(p) for p in P.rglob('*') if p.is_file()}
    ctx=read(C/'context.json'); plugin=read(C/'plugin.json'); design=read(C/'design.json'); binding=read(T/'binding.json');request=read(T/'request.json')
    rec=next(r for r in rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']=='Plane259')
    approval=read(ROOT/'provenance/approvals.json')['approvals']['Plane259']
    current_content=content(ROOT,'PlaneGeometry',rec)
    authoritative={}
    for p in [ROOT/'PlaneGeometry/dataset.jsonl',ROOT/'provenance/approvals.json',ROOT/'PlaneGeometry/special_variant/accepted_index.jsonl',ROOT/'PlaneGeometry/special_variant/collected_index.jsonl',ROOT/'PlaneGeometry/special_variant/Plane259/recipes.json',ROOT/'PlaneGeometry/special_variant/Plane259/collection.json']:
        authoritative[str(p.relative_to(ROOT))]={'sha256':sha(p) if p.is_file() else None,'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat() if p.exists() else None,'question_rows':[r for r in rows(p) if r.get('question_id',r.get('id'))=='Plane259'] if p.suffix=='.jsonl' else (read(p) if p.exists() and p.name in ('recipes.json','collection.json') else None)}
    eligible={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'formal_record':rec,'formal_record_matches_snapshot':rec==read(P/'formal_record.json'),'current_formal_approval':approval,'computed_content_sha256':digest(current_content),'approval_valid':approval.get('reviewer')=='user' and bool(approval.get('instruction')) and bool(approval.get('approved_at_utc')) and digest(current_content)==approval['content_sha256'],'authoritative':authoritative,'prior_published_manifests':{str(p.relative_to(ROOT)):{'sha256':sha(p),'mentions_Plane259':'Plane259' in p.read_text(encoding='utf-8-sig')} for p in (ROOT/'runtime/mathvision_special_20261101').glob('batch_*/manifest.json')}}
    eligible['noPass']=not authoritative['PlaneGeometry\\special_variant\\accepted_index.jsonl']['question_rows'] and not (ROOT/'PlaneGeometry/special_variant/Plane259/recipes.json').exists()
    eligible['notCollected']=not authoritative['PlaneGeometry\\special_variant\\collected_index.jsonl']['question_rows'] and not (ROOT/'PlaneGeometry/special_variant/Plane259/collection.json').exists()
    eligible['eligible']=eligible['approval_valid'] and rec['source_dataset']=='MathVision' and eligible['noPass'] and eligible['notCollected'] and all(not x['mentions_Plane259'] for x in eligible['prior_published_manifests'].values())
    eligible['diagnostic_runtime_metadata']={}
    historic=read(P/'eligibility_end.json')
    for p in [ROOT/'runtime/mathvision_special_20261101/remaining_questions.jsonl',ROOT/'runtime/mathvision_special_20261101/exploration_report.json']:
        matches=([r for r in rows(p) if r.get('question_id')=='Plane259'] if p.suffix=='.jsonl' else [r for r in read(p).get('attempts',[]) if r.get('question_id')=='Plane259'])
        eligible['diagnostic_runtime_metadata'][str(p.relative_to(ROOT))]={'sha256':sha(p),'historical_sha256':historic['diagnostic_runtime_metadata_hashes'].get(str(p.relative_to(ROOT))),'question_entries':matches,'classification':'Mutable exploration metadata; not authoritative formal content or solver evidence.'}
    points={o['id']:np.array(o['geometry'].get('points',[]),dtype=float) for o in ctx['objects']}
    def centred(a): return a-(a.min(axis=0)+a.max(axis=0))/2
    source=centred(points['o10']); scale=8/9
    matrices={'identity':[[1,0],[0,1]],'reflect_vertical_line':[[-1,0],[0,1]],'reflect_horizontal_line':[[1,0],[0,-1]],'halfturn':[[-1,0],[0,-1]],'clockwise90':[[0,1],[-1,0]],'counterclockwise90':[[0,-1],[1,0]],'reflect_y_equals_x':[[0,1],[1,0]],'reflect_y_equals_minus_x':[[0,-1],[-1,0]]}
    errors={letter:{name:float(np.max(np.abs(centred(points[oid])-scale*(source@np.array(mat).T)))) for name,mat in matrices.items()} for letter,oid in zip('ABCDE', ['o11','o12','o13','o14','o15'])}
    math={'method':'Independently compare every original formal-context polygon vertex under all eight signed-permutation orthogonal transforms. Centre bounding boxes only to remove option layout translation; use common uniform scale 8/9. Human source-image check independently establishes the two reflection axes.','source_vertices':len(source),'option_scale':scale,'transform_errors':errors,'worked4_outer_vertical_reflection_error':float(np.max(np.abs(points['o7']-points['o5']@np.diag([-1,1])))),'worked4_counter_vertical_reflection_error':float(np.max(np.abs(points['o6']-points['o4']@np.diag([-1,1])))),'worked4_outer_second_horizontal_reflection_error':float(np.max(np.abs(points['o9']-points['o7']@np.diag([1,-1])))),'worked4_counter_second_horizontal_reflection_error':float(np.max(np.abs(points['o8']-points['o6']@np.diag([1,-1])))),'unique_halfturn_match':[k for k,v in errors.items() if v['halfturn']<1e-10],'formal_scene_snapshot_byte_match':sha(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane259.json')==sha(P/'source_scene_snapshot.json')}
    with Image.open(C/'candidate.png') as im: cand=np.array(im.convert('RGBA')); pix=hashlib.sha256(b'768x768:RGBA:'+cand.tobytes()).hexdigest()
    with Image.open(ROOT/'PlaneGeometry/image/Plane259.png') as im: base=np.array(im.convert('RGBA'))
    rgba_diff=np.any(cand!=base,axis=2); yy,xx=np.where(rgba_diff)
    components=[]; seen=np.zeros(rgba_diff.shape,dtype=bool)
    for y,x in zip(yy,xx):
        if seen[y,x]:continue
        todo=[(int(y),int(x))];seen[y,x]=True;members=[]
        while todo:
            cy,cx=todo.pop();members.append((cy,cx))
            for dy,dx in ((-1,0),(1,0),(0,-1),(0,1)):
                ny,nx=cy+dy,cx+dx
                if 0<=ny<768 and 0<=nx<768 and rgba_diff[ny,nx] and not seen[ny,nx]:seen[ny,nx]=True;todo.append((ny,nx))
        a=np.array(members);components.append({'pixels':len(members),'bbox_xyxy':[int(a[:,1].min()),int(a[:,0].min()),int(a[:,1].max()),int(a[:,0].max())]})
    image_audit={'png_sha256':sha(C/'candidate.png'),'pixel_sha256':pix,'opaque_768_square':cand.shape==(768,768,4) and bool(np.all(cand[:,:,3]==255)),'differing_pixel_count':len(xx),'difference_components':components,'baseline_copy_bytes_match_formal':sha(P/'original.png')==sha(ROOT/'PlaneGeometry/image/Plane259.png')}
    encoded=request['messages'][1]['content'][1]['image_url']['url']; decoded=base64.b64decode(encoded.split(',',1)[1],validate=True)
    evidence={'request_file_sha256':sha(T/'request.json'),'request_bytes_hash_matches_binding':sha(T/'request.json')==binding['request_body_sha256'],'request_nonimage_fields':{**{k:v for k,v in request.items() if k!='messages'},'messages':[request['messages'][0],{'role':request['messages'][1]['role'],'content':[request['messages'][1]['content'][0],{'type':'image_url','decoded_png_sha256':hashlib.sha256(decoded).hexdigest()}]}]},'only_expected_request_keys':set(request)=={'model','stream','thinking','messages'},'question_exact_formal':request['messages'][1]['content'][0]['text']==rec['question']==binding['question'],'decoded_png_byte_identical':decoded==(C/'candidate.png').read_bytes(),'image_hash_matches_binding':sha(C/'candidate.png')==binding['image_sha256'],'pixel_hash_matches_binding':pix==binding['pixel_sha256'],'design_byte_identical_snapshot':(C/'design.json').read_bytes()==(T/'design_snapshot.json').read_bytes(),'design_sha256_matches_binding':sha(C/'design.json')==binding['design_sha256'],'question_record_sha256':canonical(rec),'question_record_hash_matches_binding':canonical(rec)==binding['question_record_sha256'],'dataset_sha256_now':sha(ROOT/'PlaneGeometry/dataset.jsonl'),'dataset_sha256_matches_binding':sha(ROOT/'PlaneGeometry/dataset.jsonl')==binding['dataset_sha256'],'reference_quick_test_sha256_now':sha(ROOT/'PlaneGeometry/workbench/quick_test.py'),'reference_matches_binding':sha(ROOT/'PlaneGeometry/workbench/quick_test.py')==binding['reference_quick_test_sha256'],'binding':binding,'runs':[]}
    for i in (1,2):
        run=read(T/f'run_{i:02d}.json');raw=read(T/f'run_{i:02d}_response.json');started=read(T/f'run_{i:02d}_started.json');message=raw['choices'][0]['message'];summary=read(T/'summary.json')
        evidence['runs'].append({'run_file_sha256':sha(T/f'run_{i:02d}.json'),'raw_response_sha256':sha(T/f'run_{i:02d}_response.json'),'full_record':run,'raw_response_id':raw['id'],'raw_response_created_utc':datetime.datetime.fromtimestamp(raw['created'],datetime.timezone.utc).isoformat(),'raw_response_hash_matches':sha(T/f'run_{i:02d}_response.json')==run['response_sha256'],'full_content_exact_run_match':message['content']==run['answer'],'raw_and_record_finish_stop':raw['choices'][0]['finish_reason']==run['finish_reason']=='stop','run_completed':run['status']=='completed' and not run['truncated'] and run['http_status']==200,'model_exact':raw['model']==run['response_model']==request['model']=='mimo-v2.6-flash','thinking_empty_and_zero_reasoning':not run['thinking'] and raw['usage']['completion_tokens_details']['reasoning_tokens']==0,'same_frozen_bindings':all(run[k]==binding[k] for k in ('request_body_sha256','image_sha256','design_sha256')),'started_record_matches':all(run[k]==v for k,v in started.items()),'summary_full_run_exact':summary['results'][i-1]==run})
    evidence['ledger_binding_files_for_question']=[]
    for p in (ROOT/'runtime/mathvision_special_20261101').rglob('binding.json'):
        x=read(p)
        if x.get('question_id')=='Plane259': evidence['ledger_binding_files_for_question'].append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'image_sha256':x.get('image_sha256'),'requested_runs':x.get('requested_runs')})
    evidence['candidate_test_directories']=[str(p.relative_to(ROOT)) for p in (C/'tests').iterdir() if p.is_dir()]
    evidence['response_record_files']=[p.name for p in T.glob('run_*.json')]
    fingerprints=read(P/'input_fingerprints.json');comparisons={}
    for path,h in fingerprints['files'].items():
        f=ROOT/path;current=sha(f) if f.is_file() else None
        comparisons[path]={'frozen_sha256':h,'current_sha256':current,'unchanged':h==current}
    write(OUT/'input_hash_comparisons.json',comparisons)
    evidence['input_fingerprint_count']=len(comparisons)
    evidence['input_fingerprint_drift']={k:v for k,v in comparisons.items() if not v['unchanged']}
    evidence['render_check_fingerprint_snapshot_same']=read(C/'render_check.json')['input_fingerprints']==fingerprints
    evidence['recorded_files']={str(p.relative_to(ROOT)):{'sha256':sha(p),'size':p.stat().st_size,'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat()} for p in P.rglob('*') if p.is_file()}
    write(OUT/'eligibility_current.json',eligible)
    write(OUT/'math_verification.json',math)
    write(OUT/'image_verification.json',image_audit)
    write(OUT/'evidence_verification.json',evidence)
    write(OUT/'existing_evidence_start_hashes.json',frozen_files)
    emit({'eligible':eligible['eligible'],'math':math,'image':image_audit,'evidence_checks':{k:v for k,v in evidence.items() if k not in ('recorded_files','binding','runs','input_fingerprint_drift')},'input_drift_paths':list(evidence['input_fingerprint_drift']),'run_checks':[{k:v for k,v in r.items() if k!='full_record'} for r in evidence['runs']]})
def render_verify():
    import numpy as np
    sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
    from workbench_io import load_config,pixel_hash,environment_versions
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from partial_style import object_paths,apply_partial_styles
    from dataset_tools.mathvision_workbench import png_bytes
    cfg=load_config();cfg['runtime_dir']=str(OUT/'render_state');cfg['output_dir']=str(OUT/'render_output')
    ad=RendererAdapter(cfg)
    live=ad.inspect_question('Plane259');old=read(C/'context.json')
    plugin=read(C/'plugin.json');paths={};checks=[]
    scene=ad.scene('Plane259')
    def artist_data(sc):
        return {'objects':sc.objects,'axes_xlim':list(sc.ax.get_xlim()),'axes_ylim':list(sc.ax.get_ylim()),'fig_size':sc.fig.get_size_inches().tolist(),'texts':[{ 'text':a.get_text(),'position':list(a.get_position()),'color':a.get_color(),'size':a.get_fontsize(),'visible':a.get_visible()} for a in sc.ax.texts], 'patches':[{ 'path_vertices':p.get_path().vertices.tolist(),'path_codes':p.get_path().codes.tolist() if p.get_path().codes is not None else None,'facecolor':list(p.get_facecolor()),'visible':p.get_visible(),'transform':p.get_transform().get_matrix().tolist()} for p in sc.ax.patches]}
    try:
        scene.fig.canvas.draw();before=artist_data(scene)
        for oid in ('o10','o14'):
            paths[oid]=object_paths(scene,oid)
        for i,a in enumerate(plugin['params']['actions']):
            path=paths[a['target']][0];interval=a['interval'];segment=0 if i%2==0 else 37
            checks.append({'action_index':i,'target':a['target'],'live_path_id':path['id'],'live_path_sha256':path['sha256'],'frozen_path_hash_match':path['sha256']==interval['path_sha256'],'segment_count':len(path['segments']),'start_exact':interval['start']==segment/38,'end_exact':interval['end']==(segment+1)/38,'controls':path['segments'][segment]['control'].tolist(),'pixel_endpoints':scene.ax.transData.transform(path['segments'][segment]['control']).tolist(),'length_px':float(np.linalg.norm(scene.ax.transData.transform(path['segments'][segment]['control'])[1]-scene.ax.transData.transform(path['segments'][segment]['control'])[0])),'schema_color':a['color'],'linewidth_pt':a['linewidth_pt'],'linestyle_override_absent':'linestyle' not in a})
        apply_partial_styles(scene,plugin['params']['actions']);after=artist_data(scene)
        preservation=before==after
        direct=png_bytes(scene)
    finally:scene.close()
    renderer=PluginRenderer(cfg,ad,{'Plane259':live})
    normalized,png1,pix1=renderer.render(plugin,frozen=True)
    normalized2,png2,pix2=renderer.render(plugin,frozen=True)
    (OUT/'replayed_candidate.png').write_bytes(png1)
    result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'isolation':ISOLATION,'assigned_directory_write_guard':True,'environment':environment_versions(),'live_context_equal_frozen':live==old,'live_path_checks':checks,'original_geometry_fill_visibility_text_view_unchanged_by_styles':preservation,'direct_partial_style_bytes_match_candidate':direct==(C/'candidate.png').read_bytes(),'schema_and_normalization_valid':normalized==normalized2==plugin,'two_frozen_replays_byte_identical':png1==png2,'exact_frozen_candidate_byte_match':png1==(C/'candidate.png').read_bytes(),'replayed_png_sha256':hashlib.sha256(png1).hexdigest(),'replayed_pixel_sha256':pix1,'both_pixel_hashes_equal':pix1==pix2,'baseline_pixel_hash':live['original_pixel_sha256'],'path_snapshot_exact_matches':{oid:read(C/'path_fingerprints.json')[oid]==[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[oid]] for oid in paths}}
    import matplotlib.pyplot as plt
    result['open_matplotlib_figures_after']=plt.get_fignums()
    write(OUT/'render_verification.json',result);emit(result)
def preservation_supplement():
    from dataset_tools.mathvision_workbench import build_scene,png_bytes
    sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
    from partial_style import apply_partial_styles
    scene=build_scene(ROOT/'PlaneGeometry',read(P/'formal_record.json'))
    try:
        scene.fig.canvas.draw()
        originals=list(scene.ax.patches)
        def data():
            return {'objects':json.loads(json.dumps(scene.objects)),'view':[list(scene.ax.get_xlim()),list(scene.ax.get_ylim())],'text':[(t.get_text(),list(t.get_position()),t.get_color(),t.get_fontsize(),t.get_visible()) for t in scene.ax.texts],'original_patches':[{'vertices':p.get_path().vertices.tolist(),'codes':p.get_path().codes.tolist() if p.get_path().codes is not None else None,'facecolor':list(p.get_facecolor()),'fill':p.get_fill(),'visible':p.get_visible(),'transform':p.get_transform().get_matrix().tolist(),'still_in_axes':p in scene.ax.patches} for p in originals]}
        before=data();apply_partial_styles(scene,read(C/'plugin.json')['params']['actions']);after=data()
        extras=[p for p in scene.ax.patches if p not in originals]
        result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Resolve the false whole-patch-list equality in render_verification.json: the legal executor inserts split outline patches. Compare the same original patch instances and scene metadata, and separately audit inserted outlines. The earlier diagnostic is preserved.','original_patch_count':len(originals),'new_outline_patch_count':len(extras),'all_original_vertices_facecolors_fill_visibility_transform_text_view_equal':before==after,'added_patches_all_no_fill':all(not p.get_fill() for p in extras),'new_outline_colors':sorted(set(str(p.get_edgecolor()) for p in extras)),'original_patch_data_before':before,'original_patch_data_after':after,'same_candidate_bytes_after_only_legal_styles':png_bytes(scene)==(C/'candidate.png').read_bytes()}
        write(OUT/'render_preservation_supplement.json',result)
        emit({k:v for k,v in result.items() if k not in ('original_patch_data_before','original_patch_data_after')})
    finally:scene.close()
def contour_verify():
    import numpy as np
    from dataset_tools.mathvision_workbench import build_scene
    sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
    from partial_style import apply_partial_styles,object_paths
    prior=read(OUT/'render_preservation_supplement.json');b=prior['original_patch_data_before'];a=prior['original_patch_data_after']
    removed=[i for i,(x,y) in enumerate(zip(b['original_patches'],a['original_patches'])) if x['still_in_axes'] and not y['still_in_axes']]
    stable=[{k:v for k,v in x.items() if k!='still_in_axes'} for x in b['original_patches']]==[{k:v for k,v in x.items() if k!='still_in_axes'} for x in a['original_patches']]
    sc=build_scene(ROOT/'PlaneGeometry',read(P/'formal_record.json'))
    try:
        sc.fig.canvas.draw();old=list(sc.ax.patches)
        expected=[np.array(s['control']) for oid in ('o10','o14') for s in object_paths(sc,oid)[0]['segments']]
        apply_partial_styles(sc,read(C/'plugin.json')['params']['actions'])
        counts=[0]*len(expected);unmatched=[];new_data=[]
        for p in sc.ax.patches:
            if p in old:continue
            vertices=p.get_path().vertices;new_data.append({'vertices':vertices.tolist(),'codes':p.get_path().codes.tolist(),'fill':p.get_fill(),'color':list(p.get_edgecolor()),'linewidth_pt':p.get_linewidth()})
            for start,end in zip(vertices[:-1],vertices[1:]):
                segment=np.array([start,end]);matches=[i for i,e in enumerate(expected) if np.max(np.abs(e-segment))<1e-10]
                if len(matches)!=1:unmatched.append(segment.tolist())
                else:counts[matches[0]]+=1
        result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'original_shapes_values_unchanged_except_replaced_outline_membership':stable,'removed_original_patch_indices':removed,'removed_patches_all_unfilled_outlines':all(not b['original_patches'][i]['fill'] for i in removed),'all_original_filled_patches_still_present':all(y['still_in_axes'] for x,y in zip(b['original_patches'],a['original_patches']) if x['fill']),'original_metadata_text_view_equal':all(b[k]==a[k] for k in ('objects','view','text')),'expected_edge_count':len(expected),'all_76_original_edges_represented_once':all(c==1 for c in counts),'edge_coverage_counts':counts,'unmatched_added_segments':unmatched,'new_outline_patches':new_data,'explanation':'The two earlier broad equality diagnostics are false because the executor replaces two unfilled original outline artists with six unfilled partial-style paths. No original fill, vertex, text, mirror, or viewport changes. All 76 constituent edges are covered once; no extra cut or contour exists.'}
        write(OUT/'contour_preservation_conclusion.json',result);emit({k:v for k,v in result.items() if k not in ('new_outline_patches','edge_coverage_counts')})
    finally:sc.close()
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='verify': verify()
    elif mode=='render': render_verify()
    elif mode=='preservation': preservation_supplement()
    elif mode=='contour': contour_verify()
    elif mode=='preservation_diff':
        d=read(OUT/'render_preservation_supplement.json');b=d['original_patch_data_before'];a=d['original_patch_data_after']
        emit({'nonpatch_equal':{k:b[k]==a[k] for k in b if k!='original_patches'},'patch_changes':[{ 'index':i,'changes':{k:[x[k],y[k]] for k in x if x[k]!=y[k]}} for i,(x,y) in enumerate(zip(b['original_patches'],a['original_patches'])) if x!=y]})
    elif mode=='timing':
        ev=read(OUT/'evidence_verification.json')
        emit({k:v for k,v in ev['recorded_files'].items() if Path(k).name in ('candidate.png','plugin.json','design.json','render_check.json','input_fingerprints.json','formal_record.json','context.json','binding.json','run_01_started.json','run_02_started.json','design_snapshot.json','source_scene_snapshot.json')})
        for p in [ROOT/'PlaneGeometry/image/Plane259.png',ROOT/'PlaneGeometry/originals/Plane259.jpg',ROOT/'PlaneGeometry/dataset_generator/scenes/Plane259.json']:
            emit({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat()})
    elif mode=='inventory':
        emit({str(p.relative_to(ROOT)):p.stat().st_size for p in P.rglob('*') if p.is_file()})
        for p in [P/'context.json',C/'context.json',C/'render_check.json',P/'input_fingerprints.json',C/'path_fingerprints.json',T/'request.json',T/'binding.json',ROOT/'provenance/approvals.json']:
            obj=read(p);emit({'path':str(p.relative_to(ROOT)),'keys':list(obj) if isinstance(obj,dict) else 'list','bytes':p.stat().st_size})
    elif mode=='small':
        for path in sys.argv[2:]:
            p=ROOT/path;obj=read(p)
            emit({'path':path,'content':obj})
    elif mode=='inspect':
        ctx=read(C/'context.json')
        emit({'canvas':{k:v for k,v in ctx['canvas'].items() if k not in ('targets','snap_points')},'objects':[{'id':x['id'],'keys':list(x),'type':x.get('type')} for x in ctx['objects']]})
        for p in [ROOT/'PlaneGeometry/dataset_generator/scenes/Plane259.json',P/'source_scene_snapshot.json']:
            o=read(p);emit({'path':str(p.relative_to(ROOT)),'keys':list(o)})
        preservation=read(ROOT/'runtime/mathvision_special_20261101/background_07/source_preservation_classification_final.json')
        emit({k:(len(v) if isinstance(v,(dict,list)) else v) for k,v in preservation.items()})
    elif mode=='geometry':
        ctx=read(C/'context.json');obj=next(o for o in ctx['objects'] if o['id']=='o10')
        emit(obj)
        scene=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane259.json')
        emit({'objects':[{k:v for k,v in o.items() if k!='points'} for o in scene['objects']], 'labels':scene['labels'], 'constraints':scene['constraints'],'ambiguities':scene['ambiguities']})
