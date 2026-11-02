"""u04 read-only source research; every Python write confined to OWN."""
from pathlib import Path
import os
import sys
OWN = Path(__file__).resolve().parent
PROJECT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = OWN.parent.parent
OLD = PROJECT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, suffix in {'TEMP':'ownruntime/tmp', 'TMP':'ownruntime/tmp',
                    'MPLCONFIGDIR':'ownruntime/mpl', 'XDG_CACHE_HOME':'ownruntime/cache'}.items():
    target = OWN / suffix
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def write_check(path):
    if isinstance(path, int) or path is None:
        return
    actual = Path(os.fsdecode(path)).resolve()
    if not actual.is_relative_to(OWN):
        raise PermissionError('u04 strict writeguard: ' + str(actual))

def audit(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
        write_check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        write_check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        write_check(args[0]); write_check(args[1])
sys.addaudithook(audit)
sys.path.insert(0, str(PROJECT))
import json
import hashlib
import importlib.util
from datetime import datetime, timezone

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path, data, new=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x' if new else 'w', encoding='utf-8', newline='\n') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')

def install():
    spec = importlib.util.spec_from_file_location('_u04_isolation', OLD/'runtime_isolation.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.install(OWN/'ownruntime/native', guard_writes=False)

def eligibility(qid):
    from dataset_tools import catalog
    assignment = read(OWN/'assignment.json')
    frozen = next(q for q in assignment['questions'] if q['question_id'] == qid)
    record = next(r for r in catalog.rows(PROJECT/'PlaneGeometry/dataset.jsonl') if r['id'] == qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    content = catalog.content(PROJECT, 'PlaneGeometry', record)
    current = catalog.digest(content)
    special = PROJECT/'PlaneGeometry/special_variant'
    entries = {}
    for index in ('accepted_index.jsonl', 'collected_index.jsonl'):
        entries[index] = [r for r in catalog.rows(special/index) if r.get('question_id', r.get('id')) == qid] if (special/index).exists() else []
    recipes = read(special/qid/'recipes.json') if (special/qid/'recipes.json').exists() else []
    collection = read(special/qid/'collection.json') if (special/qid/'collection.json').exists() else None
    actual_hashes = {p:sha(PROJECT/p) for p in frozen['frozen_source_files_sha256']}
    drift = {p: {'expected':h, 'actual':actual_hashes[p]} for p,h in frozen['frozen_source_files_sha256'].items() if actual_hashes[p] != h}
    eligible = record == frozen['formal_record'] and record['source_dataset'] == 'MathVision' and current == approval['content_sha256'] == frozen['current_content_sha256'] and not any(entries.values()) and not recipes and not collection and not drift
    return {'question_id':qid, 'checked_at':now(), 'eligible':eligible, 'record':record,
            'approval':approval, 'recomputed_content_sha256':current,
            'content':content, 'indices':entries, 'recipes':recipes, 'collection':collection,
            'source_files_sha256':actual_hashes, 'source_drift':drift}

def setup_renderer(qid):
    isolation = install()
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from workbench_io import load_config
    config = load_config(PROJECT/'PlaneGeometry/workbench/config.json')
    config['runtime_dir'] = str(OWN/'ownruntime/workbench')
    config['output_dir'] = str(OWN/'ownruntime/output')
    adapter = RendererAdapter(config)
    context = adapter.inspect_question(qid)
    renderer = PluginRenderer(config, adapter, {qid:context})
    return adapter, renderer, context, isolation

def initial():
    files = [OWN/'brief.txt', OWN/'assignment.json', TASK/'task.json', TASK/'reference_manifest.json', TASK/'reference_style_summary.json', TASK/'history_index.json',
             PROJECT/'AGENTS.md', PROJECT/'MATHPALETTE_PROTOCOL.md', PROJECT/'PlaneGeometry/REDRAW_PROTOCOL.md',
             PROJECT/'PlaneGeometry/dataset_generator/protocol.json', PROJECT/'PlaneGeometry/workbench/README.md',
             PROJECT/'PlaneGeometry/workbench/agent_prompt.md', PROJECT/'PlaneGeometry/workbench/plugin.schema.json',
             OLD/'runtime_isolation.py', OLD/'annotation_semantics_lessons_20261102.json', OLD/'annotation_semantics_lesson_plane242_r24_20261102.json']
    references = {}
    for q, entry in read(TASK/'reference_manifest.json').items():
        directory = TASK/entry['directory']
        data = {name:read(directory/name) for name in ('C01.json','recipes.json','reference.json')}
        references[q] = data
        files.extend(directory/name for name in ('C01.json','C01.png','recipes.json','reference.json','original.png'))
        assert sha(directory/'C01.png') == entry['png_sha256']
        assert sha(directory/'C01.json') == entry['plugin_sha256']
    save(OWN/'initial_read_manifest.json', {'created_at':now(),'files':{str(p.relative_to(PROJECT)):sha(p) for p in files},'no_formal_writes':True}, new=True)
    history = read(TASK/'history_index.json')
    scoped = [q for q in history['questions'] if q['question_id'] in ('Plane321','Plane490')]
    save(OWN/'history_scoped_index.json',scoped,new=True)
    save(OWN/'reference_full_read.json', references,new=True)
    for qid in ('Plane321','Plane490'):
        result = eligibility(qid)
        save(OWN/qid/'eligibility_initial.json',result,new=True)
        save(OWN/qid/'formal_record.json',result['record'],new=True)
        assert result['eligible'], (qid, 'source or eligibility drift')
    save(OWN/'checkpoint.json', {'unit_id':'u04_angles','updated_at':now(),'status':'reading_history_and_primary_math',
         'questions':{q:{'status':'in_progress','new_actual_calls':0} for q in ('Plane321','Plane490')},
         'primary_candidates':[], 'new_actual_calls':0,'formal_actions':0,'independent_second_review':False})
    save(OWN/'second_review_queue.json',[])
    print(json.dumps({'initialized':str(OWN),'eligibility_both':True},ensure_ascii=False))

def context(qid):
    adapter,renderer,ctx,isolation = setup_renderer(qid)
    save(OWN/qid/'context.json',ctx,new=True)
    save(OWN/qid/'adapter_manifest.json',adapter.manifest,new=True)
    scene = adapter.scene(qid)
    try:
        from dataset_tools.mathvision_workbench import png_bytes
        from workbench_io import pixel_hash, environment_versions
        data = png_bytes(scene)
        (OWN/qid/'noop.png').write_bytes(data)
        result = {'png_sha256':hashlib.sha256(data).hexdigest(), 'pixel_sha256':pixel_hash(data),
                  'formal_pixel_sha256':pixel_hash(adapter.original_paths[qid]),
                  'noop_pixels_equal':pixel_hash(data)==pixel_hash(adapter.original_paths[qid]),
                  'isolation':isolation,'strict_write_guard_root':str(OWN),
                  'environment':environment_versions(),
                  'env':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')}}
        save(OWN/qid/'noop_check.json',result,new=True)
        assert result['noop_pixels_equal']
    finally:
        scene.close()
    print(json.dumps({'qid':qid, 'objects':ctx['objects'], 'snap_points':ctx['snap_points'],'canvas':ctx['canvas']}, ensure_ascii=False))

def history_read():
    index = read(TASK/'history_index.json')
    files = set()
    for question in index['questions']:
        if question['question_id'] not in ('Plane321','Plane490'):
            continue
        for key in ('other_scoped_history_file_references','additional_math_manual_history_references','independent_review_references'):
            files.update(question[key])
        for design in question['designs']:
            files.update(str(p.relative_to(PROJECT)).replace('\\','/') for p in (PROJECT/design['directory']).rglob('*') if p.is_file())
    hashes, decoded, responses = {}, [], []
    for relative in sorted(files):
        path = PROJECT/relative
        hashes[relative] = sha(path)
        expected = index['tracked_readonly_source_sha256'].get(relative)
        if expected is not None:
            assert hashes[relative] == expected, relative
        if path.suffix != '.json':
            continue
        data = read(path)
        if path.name == 'request.json':
            import base64
            items = data['messages'][1]['content']
            image_bytes = base64.b64decode(items[1]['image_url']['url'].split(',',1)[1], validate=True)
            decoded.append({'path':relative, 'question':items[0]['text'],
                            'image_sha256':hashlib.sha256(image_bytes).hexdigest(),
                            'payload_top_keys':list(data),'model':data['model'],
                            'thinking':data['thinking'],'system':data['messages'][0]})
            del image_bytes, data
        elif path.name.endswith('_response.json'):
            responses.append({'path':relative,'raw_sha256':hashes[relative], 'raw':data})
        else:
            del data
    save(OWN/'history_full_read_manifest.json',{'created_at':now(), 'files_sha256':hashes,
         'complete_file_count':len(hashes), 'requests_decoded':decoded,
         'raw_response_count':len(responses),'streamed_sequentially':True,
         'independent_review_references_for_both':[],
         'scope':'All actual scoped history paths in parent index plus entire four Plane321 candidate trees'},new=True)
    save(OWN/'history_full_raw_responses.json',responses,new=True)
    print(json.dumps({'full_file_count':len(hashes),'requests':decoded,
                     'responses':[{k:v for k,v in r.items() if k!='raw'} for r in responses]},ensure_ascii=False))

def prepare():
    reference = {'question_id':'Plane427','png':str(TASK/'references/Plane427/C01.png'),
                 'png_sha256':sha(TASK/'references/Plane427/C01.png'),
                 'plugin_sha256':sha(TASK/'references/Plane427/C01.json'),
                 'actual_png_viewed':True,
                 'observed':'Current ST and TV red; original dotted SV blue. Original70 arc and target arc retained.',
                 'not_old18':'Uses actual current nine C01s; not old reversed colors, old option labels or delivered18 mechanisms.'}
    math321 = {
        'question_id':'Plane321','correct_answer':{'letter':'E','value':'300 degrees'},
        'given_and_placement':'Two congruent equilateral triangles ABC and ACD share AC and lie on its opposite sides. A is fixed; direction is counterclockwise; cover means full containment, not first contact or partial overlap.',
        'exact_model':'Normalize A=(0,0), B=(-1,0), C=(-1/2,-sqrt(3)/2), D=(1/2,-sqrt(3)/2). This is a common translation and positive scaling of the frozen diagram (with preserved orientation).',
        'coverage_implies_equality':'Both triangles have the same positive area. If one closed nondegenerate triangle contains the other and the sets differ, its interior contains a nonempty open region outside the other, giving strictly larger area. Thus complete cover here forces equality of triangles.',
        'exhaustive_vertex_correspondence':'A remains A. A rotation of an entire convex triangle permutes its extreme vertices, so the two other vertices C,D must be sent bijectively to B,C. Case1: C->B requires theta=300 mod360 since arg(AC)=240 and arg(AB)=180; D->C also requires300 since arg(AD)=300 and arg(AC)=240. Case2: C->C requires theta=0 mod360; D->B requires theta=240 mod360, incompatible. These two cases exhaust both permutations.',
        'first_time':'Thus the full-cover times are exactly theta=300+360k for integer k; the first strictly positive counterclockwise angle is300. A60 is the clockwise shortcut; B120 is an interior sum, C180 and D240 fail the two simultaneous vertex mappings.',
        'source_check':'Original JPG and formal PNG independently viewed; orientation preserved; the frozen points B=(0,3sqrt(3)), A=(6,3sqrt(3)), C=(3,0), D=(9,0) realize this model. No inference from previous solver answers.'}
    math490 = {
        'question_id':'Plane490','correct_answer':{'value':'180 degrees'},
        'center':'C=(0,0); darker left arrow and lighter right arrow identified from original JPG and current formal black/gray outlines.',
        'light_vertices':[[-4,0],[4,0],[4,-2],[6,1],[4,4],[4,2],[-4,2]],
        'dark_vertices':[[4,0],[-4,0],[-4,2],[-6,-1],[-4,-4],[-4,-2],[4,-2]],
        'existence':'Each dark vertex and each of its incident edges is sent by x->-x to the light vertex/edge at the same cyclic index. Hence the entire boundary and enclosed polygon rotate exactly180 around C.',
        'uniqueness':'Any rotation mapping these nondegenerate polygonal shapes maps their seven genuine corners bijectively; none of the seven is collinear with its two neighbors. The arithmetic mean of dark corners is(-2,-1) and of light corners is(2,1). A linear rotation must map the first nonzero vector to the second. The only angle modulo360 doing so is180. Direct corner mapping proves existence, and the mean proves uniqueness; no dependence on an assumed arrow-tip correspondence.',
        'zero_excluded':'At0 the dark tip(-6,-1) remains there, while the light unique tip is(6,1). Thus exact overlap of the shared boundary is insufficient to map the whole object.',
        'interval_note':'Current actual path has7 ordered segments; one parameter interval1/7 denotes one original vector segment, not one seventh of arc length.'}
    save(OWN/'Plane321/primary_math_proof.json',math321,new=True)
    save(OWN/'Plane490/primary_math_proof.json',math490,new=True)
    specs = [
      ('Plane321','a01_pivot_legs_vs_true_bases','B','120',[
        {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':1.5}
        for oid,color in [('o0','#2563EB'),('o1','#DC2626'),('o2','#2563EB'),('o3','#2563EB'),('o4','#DC2626')]],
       'Both equilateral triangles have their A-incident legs blue and their opposite bases BC/CD red. The red bases meet at C, exposing the actual120-degree sum of the two60-degree angles. A solver may substitute that static two-angle opening (also the outer blue opening at A) for the directed rotation. Preset B=120, frozen without seeing any new response.',
       [
        {'target':'o0','source':'AB: target A-incident side','receiver':'blue AC/AD A-incident sides','use':'Completes the true two-blue-leg target group; under correct rotation AC->AB.'},
        {'target':'o1','source':'BC: target side opposite fixedA','receiver':'red CD source side opposite fixedA','use':'Genuine whole-triangle opposite-base correspondence; exposes red opening atC.'},
        {'target':'o2','source':'AC: existing shared side','receiver':'both blue incident-leg groups','use':'Shows the shared leg as part of each triangle; at correct rotation AD->AC and AC->AB. Does not assert it stays fixed.'},
        {'target':'o3','source':'AD: source A-incident side','receiver':'blue target AC/AB','use':'Completes source two-leg structure; contrasts pivot sides against red nonpivot base.'},
        {'target':'o4','source':'CD: source side opposite fixedA','receiver':'red BC target base','use':'Actual base correspondence, not arbitrary outer rayD->B.'}],
       'Under300, blue AC->blue AB, blue AD->blue AC, and red CD->red BC. Therefore even a literal colored-edge reading preserves exactly the original mapping. Labels are ordinary geometric names, as in the original. All coordinates, solid lines, equilateral conditions, direction, center and full-cover meaning are retained. No new cuts, arcs, arrowheads, symbols or equality assumptions.',
       'All four old tested designs concern the A-incident outer rays AB/AD, short sector AB/AC, or endpointB/D markers. This design instead colors the actual nonpivot base pair CD/BC red and closes both two-leg blue groups. This is a different correspondence partition with an intrinsic-color-compatible correct mapping, not a color/width-only permutation of an old failed input.'),
      ('Plane490','a01_shared_boundary_invariance','0','0',None,
       'The two genuine arrows share exactly the central Z-shaped boundary: horizontal[-4,4] at y0 and its left/up and right/down vertical end walls. Red equal end walls and blue common horizontal make an exactly coincident local subset salient. That subset admits identity0 as well as180, so a solver may confuse local coincidence with whole-object mapping and return0. The two opposite arrowheads and black/gray identity remain decisive for a careful human. Preset value0, frozen without seeing any new response.',
       [
        {'target':'o1 interval0..1/7','source':'common horizontal boundary from(4,0) to(-4,0)','receiver':'same visible boundary belonging also to light arrow','use':'Blue same-location comparison of the actual shared boundary, not an invented translation match.'},
        {'target':'o1 interval1/7..2/7','source':'shared left vertical wall(-4,0)->(-4,2)','receiver':'red shared right vertical wall','use':'Equal true shared end-wall pair, interchanged by180; the path end is preserved.'},
        {'target':'o1 interval6/7..1','source':'shared right vertical wall(4,-2)->(4,0)','receiver':'red shared left vertical wall','use':'Completes the actual180-invariant shared Z path; all colored material maps to identical colored material.'}],
       'The shown sharedZ is an actual boundary of both arrows and has the same visible colors for each. Under180 the blue middle segment maps to itself and the two red end walls swap. Thus interpreting the strokes as intrinsic edging still leaves180 possible and uniquely necessary for full shapes. The rest of light outline remains gray and dark outline black, including both tips and sloped edges. No4th wall, closed false region, label, new shaft or moved center is introduced. The colors do not assert endpointwise fixation; the target is the entire lighter arrow, explicitly in the unchanged question.',
       'No old actual candidate/call exists for this question in the saved index. Two old primary prescreens rejected unrelated same-side shafts as translation cues and perpendicular arbitrary edges as90 cues. This design marks only the coincident common boundary, whose set is invariant under180 as well as0, with colored parts also invariant under180. It neither pairs different same-side shafts nor requires a color-incompatible map. It is a new local-subset-versus-global-map hypothesis, not a repeat of a tested or abandoned PNG.')]
    for qid,variant,preset,value,actions,mechanism,roles,semantics,difference in specs:
        directory=OWN/qid/variant
        checked=eligibility(qid)
        assert checked['eligible']
        save(directory/'eligibility_before_design.json',checked,new=True)
        if qid=='Plane490':
            context=read(OWN/qid/'context.json')
            target=next(t for t in context['canvas']['targets'] if t['id']=='o1')
            path=target['partial_paths'][0]
            s=[v[2] for v in path['samples']]
            actions=[]
            for a,b,color in [(s[0],s[1],'#2563EB'),(s[1],s[2],'#DC2626'),(s[6],s[7],'#DC2626')]:
                actions.append({'type':'set_object_style','target':'o1','color':color,'linewidth_pt':1.5,
                      'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':a,'end':b,'wrap':False}})
        plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
                'description':'Primary research: true existing boundary correspondence from current user C01 method.',
                'intent':'Research only; no Pass, Collect, independent second review or delivery.',
                'params':{'actions':actions}}
        save(directory/'plugin_input.json',plugin,new=True)
        save(directory/'design_proposal.json',{'question_id':qid,'variant_id':variant,'created_at':now(),
             'expected_wrong_answer':preset,'expected_wrong_value_degrees':value,
             'correct_answer':checked['record']['answer'], 'mechanism':mechanism,
             'mark_roles':roles,'human_semantics':semantics,
             'primary_math_proof':str(OWN/qid/'primary_math_proof.json'),
             'substantive_history_difference':difference,'reference':reference,
             'review_status':'PRIMARY_PROPOSAL_BEFORE_RENDER_AND_CALLS','calls':0},new=True)
        save(directory/'reference_transfer.json',{'reference':reference,'transferred':'Existing two-color edge/leg/base comparison; no new constraints or text.',
             'difference_from_old':difference,'mark_roles':roles,'semantics':semantics},new=True)
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint.update(updated_at=now(),status='two_primary_proposals_before_render_and_calls')
    for qid in checkpoint['questions']: checkpoint['questions'][qid]['status']='primary_proposal_prepared'
    save(OWN/'checkpoint.json',checkpoint)
    print('Two primary proposals saved; no model calls.')

def render_candidate(qid,variant):
    directory=OWN/qid/variant
    before=eligibility(qid)
    assert before['eligible']
    save(directory/'eligibility_before_render.json',before,new=True)
    adapter,renderer,ctx,isolation=setup_renderer(qid)
    from render_plugins import check_schema
    from workbench_io import pixel_hash, environment_versions
    plugin=renderer.normalize(read(directory/'plugin_input.json'))
    check_schema(plugin,read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'))
    one,data,digest=renderer.render(plugin,frozen=True)
    two,data2,digest2=renderer.render(plugin,frozen=True)
    assert one==two==plugin and data==data2 and digest==digest2
    save(directory/'plugin.json',plugin,new=True)
    (directory/'candidate.png').write_bytes(data)
    (directory/'repeat.png').write_bytes(data2)
    save(directory/'context.json',ctx,new=True)
    fresh= json.loads(json.dumps(ctx,ensure_ascii=False,allow_nan=False))
    saved=read(OWN/qid/'context.json')
    assert fresh==saved,'context drift under exact JSON tuple/list canonicalization'
    old=read(TASK/'history_index.json')
    candidates=[]
    for q in old['questions']:
        for d in q['designs']:
            if d['frozen_candidate_png_sha256']==hashlib.sha256(data).hexdigest(): candidates.append(d['design_path'])
        for t in q['all_saved_transport_groups_for_question']:
            if t['image_sha256']==hashlib.sha256(data).hexdigest(): candidates.extend(t['aliases'])
    assert not candidates, candidates
    report={'created_at':now(),'fresh_schema':True,'normalization_fixed_point':renderer.normalize(plugin)==plugin,
            'repeat_png_bytes_identical':data==data2,'png_sha256':sha(directory/'candidate.png'),
            'pixel_sha256':digest,'plugin_sha256':sha(directory/'plugin.json'),
            'fresh_context_exact_json_equal':True,'formal_noop':read(OWN/qid/'noop_check.json'),
            'old_candidate_or_transport_exact_png_matches':candidates,
            'schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),
            'renderer_sha256':sha(PROJECT/'PlaneGeometry/workbench/mathvision_plugins.py'),
            'adapter_sha256':sha(PROJECT/'PlaneGeometry/workbench/mathvision_adapter.py'),
            'environment':environment_versions(),'isolation':isolation,'strict_write_guard_root':str(OWN)}
    save(directory/'render_gates.json',report,new=True)
    print(json.dumps(report,ensure_ascii=False))

def replay(qid,variant):
    directory=OWN/qid/variant
    before=eligibility(qid)
    assert before['eligible']
    adapter,renderer,ctx,isolation=setup_renderer(qid)
    original=read(directory/'render_gates.json')
    assert json.loads(json.dumps(ctx,ensure_ascii=False,allow_nan=False))==read(directory/'context.json')
    plugin=read(directory/'plugin.json')
    norm,data,digest=renderer.render(plugin,frozen=True)
    assert norm==plugin and data==(directory/'candidate.png').read_bytes() and digest==original['pixel_sha256']
    (directory/'independent_process_replay.png').write_bytes(data)
    save(directory/'independent_process_replay.json',{'pid':os.getpid(),'created_at':now(),
         'png_bytes_equal':True,'pixel_sha256':digest,'plugin_sha256':sha(directory/'plugin.json'),
         'candidate_png_sha256':sha(directory/'candidate.png'),'context_exact_JSON_equal':True,
         'numeric_tolerance_used':False,'eligibility':before},new=True)
    print('New independent process exact replay passed: '+qid+'/'+variant)

def freeze(qid,variant):
    directory=OWN/qid/variant
    assert (directory/'independent_process_replay.json').is_file()
    assert read(directory/'independent_process_replay.json')['png_bytes_equal']
    before=eligibility(qid)
    assert before['eligible']
    save(directory/'eligibility_before_freeze.json',before,new=True)
    import base64
    import zipfile
    image_hash=sha(directory/'candidate.png')
    scanned,matched,errors={},[],[]
    def inspect_request(raw,label):
        scanned[label]=hashlib.sha256(raw).hexdigest()
        try:
            obj=json.loads(raw.decode('utf-8-sig'))
            for message in obj.get('messages',[]):
                content=message.get('content')
                if not isinstance(content,list): continue
                text='\n'.join(c.get('text','') for c in content if c.get('type')=='text')
                for c in content:
                    url=c.get('image_url',{}).get('url','') if isinstance(c,dict) else ''
                    if url.startswith('data:image/'):
                        decoded=base64.b64decode(url.split(',',1)[1],validate=True)
                        digest=hashlib.sha256(decoded).hexdigest()
                        if digest==image_hash:
                            matched.append({'path':label,'question_text':text,
                                            'same_formal_text':text==before['record']['question'],
                                            'image_sha256':digest})
                        del decoded
            del obj
        except Exception as error:
            errors.append({'path':label,'type':type(error).__name__,'error':str(error)})
    for file in (PROJECT/'runtime').rglob('request.json'):
        if file.is_relative_to(directory): continue
        inspect_request(file.read_bytes(),str(file.relative_to(PROJECT)))
    for file in OLD.rglob('*.zip'):
        scanned[str(file.relative_to(PROJECT))]=sha(file)
        with zipfile.ZipFile(file) as archive:
            for name in archive.namelist():
                if name.endswith('/request.json') or name=='request.json':
                    inspect_request(archive.read(name),str(file.relative_to(PROJECT))+'::'+name)
    report={'created_at':now(),'candidate_sha256':image_hash,'all_runtime_request_and_old_ZIP_request_scan':True,
            'scanned_sha256':scanned,'exact_image_matches':matched,'parse_errors':errors,
            'rule':'No same failed/aborted/unknown PNG is tested again; exact question text compared separately.'}
    save(directory/'global_prior_request_audit.json',report,new=True)
    assert not matched, 'Any prior actual identical-image transport requires separate audit; no automatic retest.'
    assert not errors, 'Unparsed request evidence requires investigation before calls.'
    proposal=read(directory/'design_proposal.json')
    proposal.update(created_at=now(),review_status='PRIMARY_FROZEN_BEFORE_BOTH_CALLS',
                    png_sha256=image_hash, plugin_sha256=sha(directory/'plugin.json'),
                    pixel_sha256=read(directory/'render_gates.json')['pixel_sha256'],
                    context_sha256=sha(directory/'context.json'),
                    proof_sha256=sha(OWN/qid/'primary_math_proof.json'),
                    proposal_sha256=sha(directory/'design_proposal.json'),
                    render_gates_sha256=sha(directory/'render_gates.json'),
                    independent_process_replay_sha256=sha(directory/'independent_process_replay.json'),
                    global_prior_request_audit_sha256=sha(directory/'global_prior_request_audit.json'),
                    manual_native_image_review='Actual768PNG viewed after legal rendering: clear full geometry and all names; no obstruction; every listed mark visible and useful. Original source JPG/formal PNG also viewed.',
                    image_immutable_after_this_point=True,
                    restrictions=['Exactly2 original quicktest3 calls only; no control, no third, no retry, no preset change.',
                                  'Primary only; independent second review to be created fresh by parent; no delivery/Pass/Collect.',
                                  'Two observed final answers do not establish a population success rate or causal gain.'])
    save(directory/'design.json',proposal,new=True)
    save(directory/'primary_review_before_calls.json',{'created_at':now(),'question_id':qid,
         'review_role':'PRIMARY','rigorous_unique_proof':str(OWN/qid/'primary_math_proof.json'),
         'formal_and_source_individually_viewed':True,'candidate_native_png_individually_viewed':True,
         'mark_roles':proposal['mark_roles'],'human_semantics':proposal['human_semantics'],
         'difference':proposal['substantive_history_difference'],
         'all_offline_gates_passed':True,'design_sha256':sha(directory/'design.json'),
         'reference_transfer_path':str(directory/'reference_transfer.json'),
         'decision':'Ready for exactly2 research calls; not an approval or independent second review.'},new=True)
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint['questions'][qid].update(status='frozen_ready_for_two_calls',variant_id=variant,design_sha256=sha(directory/'design.json'))
    checkpoint.update(updated_at=now())
    save(OWN/'checkpoint.json',checkpoint)
    print(json.dumps({'question_id':qid,'frozen':True,'design_sha256':sha(directory/'design.json'),
                      'global_requests_scanned':len(scanned),'exact_old_matches':len(matched)},ensure_ascii=False))

def harness_copy():
    import difflib
    original=OLD/'harness/quicktest3_isolated.py'
    raw=original.read_bytes()
    old=b'PROJECT = Path(__file__).resolve().parents[3]'
    new=('PROJECT = Path('+repr(str(PROJECT))+')').encode('utf-8')
    assert raw.count(old)==1
    copied=raw.replace(old,new)
    output=OWN/'ownruntime/harness/quicktest3_isolated.py'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes(copied)
    assert copied.replace(new,old)==raw
    save(OWN/'harness_integrity.json',{'created_at':now(),'original':str(original),
         'original_sha256':sha(original),'copy':str(output),'copy_sha256':sha(output),
         'exact_diff':''.join(difflib.unified_diff(raw.decode('utf-8').splitlines(True),copied.decode('utf-8').splitlines(True),fromfile=str(original),tofile=str(output))),
         'reverse_replacement_bytes_equal':True,'only_change':'Local PROJECT locator; HARNESS/cache naturally remain below ownruntime.',
         'payload_system_model_thinking_key_loading_timeout_response_limit_and_call_logic_unchanged':True},new=True)
    print('Original harness copied with only PROJECT locator replacement, exact reverse verified.')

def test(qid,variant):
    import runpy
    directory=OWN/qid/variant
    assert read(directory/'primary_review_before_calls.json')['all_offline_gates_passed']
    assert not (directory/'tests').exists(),'Do not resume/retry a started candidate'
    assert not (OWN/'api_failure_stop.json').exists(),'Earlier API failure ends all batch calls'
    design=read(directory/'design.json')
    assert sha(directory/'candidate.png')==design['png_sha256']
    harness=OWN/'ownruntime/harness/quicktest3_isolated.py'
    integrity=read(OWN/'harness_integrity.json')
    assert sha(harness)==integrity['copy_sha256'] and sha(OLD/'harness/quicktest3_isolated.py')==integrity['original_sha256']
    count=0
    def before_request(event,args):
        nonlocal count
        if event!='urllib.Request': return
        count+=1
        assert count<=2,'Third request forbidden'
        current=eligibility(qid)
        save(directory/f'eligibility_before_actual_request_{count:02d}.json',current,new=True)
        assert current['eligible'],'Eligibility/source changed before actual request'
        assert sha(directory/'candidate.png')==design['png_sha256']
        assert sha(directory/'plugin.json')==design['plugin_sha256']
        assert sha(directory/'design.json')==read(directory/'primary_review_before_calls.json')['design_sha256']
    sys.addaudithook(before_request)
    pid=os.getpid()
    save(directory/'api_process_started.json',{'pid':pid,'created_at':now(),'command':sys.argv,
         'harness_runs':2,'wrapper_instrumentation':'strict own writeguard and pre-request read-only source eligibility audit only'},new=True)
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint['questions'][qid]['status']='two_call_harness_running'
    checkpoint.update(updated_at=now())
    save(OWN/'checkpoint.json',checkpoint)
    previous=list(sys.argv)
    sys.argv=[str(harness),'--branch','PlaneGeometry','--question',qid,'--image',str(directory/'candidate.png'),
              '--design',str(directory/'design.json'),'--output',str(directory/'tests'),'--runs','2']
    try:
        runpy.run_path(str(harness),run_name='__main__')
    finally:
        sys.argv=previous
        save(directory/'api_process_finished.json',{'pid':pid,'created_at':now(),
             'actual_urllib_request_events':count,'all_synchronous_requests_returned':True,
             'child_processes_started':0,'servers_started':0,'note':'Process exit must additionally be checked from parent OS after command returns.'},new=True)
        summaries=list((directory/'tests').glob('*/summary.json'))
        if summaries:
            summary=read(summaries[0])
            if any(r['status']!='completed' for r in summary['results']):
                save(OWN/'api_failure_stop.json',{'created_at':now(),'question_id':qid,'summary':str(summaries[0]),'later_calls_forbidden':True},new=True)
        checkpoint=read(OWN/'checkpoint.json')
        cumulative=len(list((OWN/qid).glob('*/tests/*/run_*_started.json')))
        checkpoint['questions'][qid].update(status='two_calls_returned_pending_manual_full_raw_review',new_actual_calls=cumulative)
        checkpoint['new_actual_calls']=sum(q['new_actual_calls'] for q in checkpoint['questions'].values())
        checkpoint.update(updated_at=now())
        save(OWN/'checkpoint.json',checkpoint)

def review321():
    qid='Plane321'; variant='a01_pivot_legs_vs_true_bases'; directory=OWN/qid/variant
    evidence=next((directory/'tests').glob('*/summary.json')).parent
    summary=read(evidence/'summary.json'); binding=read(evidence/'binding.json')
    design=read(directory/'design.json'); reviews=[]
    manual=[
       {'final_letter':'B','final_value_degrees':'120',
        'exact_final':'The correct choice is **B: $120^{\\circ}$**.',
        'interpretation':'The unambiguous last mathematical answer is B120. The following plain phrase System Instruction: has no mathematical answer, no competing option and no tool/system authority. It is retained verbatim in the full provider raw. HTTP200, finish_reason stop and no length truncation.',
        'mechanism_caution':'This narrative falsely calls BAD straight180, then subtracts60. It does not independently verify the proposed red-base120 mechanism, although the frozen final preset is hit.'},
       {'final_letter':'B','final_value_degrees':'120',
        'exact_final':'Therefore, the angle of rotation is $120^{\\circ}$.\n\nChoice: B',
        'interpretation':'The final angle120 and the final letterB agree. The incorrect intermediate C->A mapping is part of its false solution, not evidence against the independently proved300 answer.',
        'mechanism_caution':'It sums two60-degree angles while reversing the directed motion and using the wrong D->B correspondence. This is compatible with static-opening substitution, but no causal inference from two responses is justified.'}]
    import base64
    payload=read(evidence/'request.json')
    sent=base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1],validate=True)
    assert sent==(directory/'candidate.png').read_bytes()
    assert payload['messages'][1]['content'][0]['text']==eligibility(qid)['record']['question']
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'}
    assert sha(directory/'design.json')==binding['design_sha256']==summary['design_sha256']
    assert sha(directory/'candidate.png')==binding['image_sha256']==summary['image_sha256']
    assert sha(evidence/'request.json')==binding['request_body_sha256']
    assert (evidence/'design_snapshot.json').read_bytes()==(directory/'design.json').read_bytes()
    assert len(summary['results'])==2
    assert len(list(evidence.glob('run_*_started.json')))==2
    for index,manual_read in enumerate(manual,1):
        raw=read(evidence/f'run_{index:02d}_response.json')
        run=read(evidence/f'run_{index:02d}.json')
        assert run==summary['results'][index-1]
        assert sha(evidence/f'run_{index:02d}_response.json')==run['response_sha256']
        assert run['status']=='completed' and run['http_status']==200 and run['finish_reason']=='stop' and not run['truncated']
        content=raw['choices'][0]['message']['content']
        assert raw['choices'][0]['finish_reason']=='stop' and content==run['answer']
        assert manual_read['exact_final'] in content
        assert manual_read['final_letter']==design['expected_wrong_answer']=='B'
        assert manual_read['final_value_degrees']==design['expected_wrong_value_degrees']=='120'
        reviews.append({'run_index':index,'run_id':run['run_id'],'raw_path':str(evidence/f'run_{index:02d}_response.json'),
             'raw_sha256':run['response_sha256'],'complete_response_read_in_full':True,'full_answer':content,
             'complete':True,'truncated':False,'finish_reason':'stop',**manual_read,'matches_frozen_wrong_preset':True})
    current=eligibility(qid); assert current['eligible']
    save(directory/'eligibility_after_calls.json',current,new=True)
    manual_report={'created_at':now(),'question_id':qid,'role':'PRIMARY_MANUAL_FULL_RAW_REVIEW',
         'frozen_design_sha256':sha(directory/'design.json'),'preset_before_both':{'letter':'B','degrees':'120'},
         'original_correct':{'letter':'E','degrees':'300'},'responses':reviews,'two_complete_hits':True,
         'exactly_two_started_no_third':True,'request_PNG_equals_frozen':True,'formal_full_text_equals_sent':True,
         'binding_request_raw_snapshot_hashes_verified':True,
         'limitations':['Primary only; fresh independent second review required from parent.',
                        'No Pass, Collect, user approval or final delivery.',
                        'Raw1 has an irrelevant trailing System Instruction: phrase; full service response has finish_reason stop and clear B120 final.',
                        'The two narratives contain different errors; two matching final answers do not prove that both followed the proposed mechanism or establish causal gain.']}
    save(directory/'manual_final_review.json',manual_report,new=True)
    save(directory/'primary_review.json',{'created_at':now(),'question_id':qid,'variant_id':variant,
         'decision':'PRIMARY_CANDIDATE_TWO_COMPLETE_PRESET_HITS_PENDING_FRESH_INDEPENDENT_SECOND_REVIEW',
         'pretest_review':str(directory/'primary_review_before_calls.json'),
         'mathematical_proof':str(OWN/qid/'primary_math_proof.json'),'manual_final_review':str(directory/'manual_final_review.json'),
         'summary':str(evidence/'summary.json'),'mark_count':5,'all_marks_targeted_useful_and_visible':True,
         'human_colored_edge_reading_preserves_original_unique_answer':True,
         'source_eligibility_preserved':True,'restrictions':manual_report['limitations']},new=True)
    queue=read(OWN/'second_review_queue.json')
    queue.append({'question_id':qid,'variant_id':variant,'candidate_directory':str(directory),
         'image_sha256':sha(directory/'candidate.png'),'plugin_sha256':sha(directory/'plugin.json'),
         'design_sha256':sha(directory/'design.json'),'original_correct_answer':{'letter':'E','degrees':'300'},
         'frozen_wrong_preset':{'letter':'B','degrees':'120'},
         'two_complete_final_answers':[r['exact_final'] for r in reviews],
         'full_raw_manual_read_path':str(directory/'manual_final_review.json'),
         'summary_path':str(evidence/'summary.json'),'primary_review_path':str(directory/'primary_review.json'),
         'reference_transfer_path':str(directory/'reference_transfer.json'),'mathematical_proof_path':str(OWN/qid/'primary_math_proof.json'),
         'status':'PRIMARY_ONLY_PENDING_NEW_INDEPENDENT_SECOND_REVIEW','restrictions':manual_report['limitations']})
    save(OWN/'second_review_queue.json',queue)
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint['questions'][qid].update(status='PRIMARY_candidate_pending_fresh_independent_second_review',two_complete_preset_hits=True,
          manual_review_path=str(directory/'manual_final_review.json'),summary_path=str(evidence/'summary.json'))
    checkpoint['primary_candidates']=[{'question_id':q['question_id'],'variant_id':q['variant_id']} for q in queue]
    checkpoint.update(updated_at=now()); save(OWN/'checkpoint.json',checkpoint)
    print('Plane321 PRIMARY candidate queued; two full finals B120, no independent second review claimed.')

def review490(variant):
    qid='Plane490'; directory=OWN/qid/variant
    evidence=next((directory/'tests').glob('*/summary.json')).parent
    summary=read(evidence/'summary.json'); binding=read(evidence/'binding.json')
    design=read(directory/'design.json')
    import base64
    payload=read(evidence/'request.json')
    assert base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1],validate=True)==(directory/'candidate.png').read_bytes()
    assert payload['messages'][1]['content'][0]['text']==eligibility(qid)['record']['question']
    assert sha(directory/'design.json')==binding['design_sha256']==summary['design_sha256']
    assert sha(directory/'candidate.png')==binding['image_sha256']==summary['image_sha256']
    assert sha(evidence/'request.json')==binding['request_body_sha256']
    assert (evidence/'design_snapshot.json').read_bytes()==(directory/'design.json').read_bytes()
    assert len(summary['results'])==len(list(evidence.glob('run_*_started.json')))==2
    if variant=='a01_shared_boundary_invariance':
        finals=['**Answer:** The angle of rotation is **180 degrees**.', '**Answer:** 180 degrees']
        values=['180','180']
        diagnosis='Both saw opposite arrow directions and concluded180. Run1 explicitly discusses the red end walls, so the annotated common boundary was perceived but did not replace global orientation.'
    elif variant=='a02_corresponding_arrowhead_flank_directions':
        finals=['**Final Answer:** 90','**Final Answer:**\nThe angle of rotation is **$90^{\\circ}$** (clockwise).']
        values=['90','90']
        diagnosis='Both give90 clockwise, outside frozen0. Run1 describes light head incorrectly at top-left; run2 explicitly discusses red/blue flanks but describes lighter arrow as pointing up. These are complete wrong outputs but neither is a preset hit. The model narrative does not make the actual preserved right-pointing tip ambiguous. Frozen A02 remains failed and cannot be relabeled90.'
    elif variant=='a03_true_corresponding_notch_right_angles':
        finals=['**Answer:**\nThe angle of rotation is **$180^\\circ$**.','**Answer:** 180 degrees']
        values=['180','180']
        diagnosis='Both give correct180, outside frozen90. Run1 follows actual red vertical-wall positions from bottom-left to top-right aboutC and correctly obtains a halfturn; run2 uses opposite complete arrowheads. Thus the local90 notch-opening substitution did not occur in these two observations. Frozen design remains failed.'
    else:
        raise ValueError('New full response review required; do not auto-label unseen responses.')
    reviews=[]
    for index,final in enumerate(finals,1):
        raw=read(evidence/f'run_{index:02d}_response.json'); run=read(evidence/f'run_{index:02d}.json')
        assert sha(evidence/f'run_{index:02d}_response.json')==run['response_sha256']
        assert run==summary['results'][index-1]
        assert run['status']=='completed' and run['http_status']==200 and run['finish_reason']=='stop' and not run['truncated']
        content=raw['choices'][0]['message']['content']
        assert content==run['answer'] and final in content
        reviews.append({'run_index':index,'run_id':run['run_id'],'raw_path':str(evidence/f'run_{index:02d}_response.json'),
           'raw_sha256':sha(evidence/f'run_{index:02d}_response.json'),'full_answer':content,
           'complete_response_manually_read_in_full':True,'exact_final':final,'final_value_degrees':values[index-1],
           'preset_value_degrees':design['expected_wrong_value_degrees'],'matches_frozen_wrong_preset':False,
           'finish_reason':'stop','truncated':False,'decision':'Does not match frozen wrong'+design['expected_wrong_value_degrees']+' preset; no relabeling.'})
    current=eligibility(qid); assert current['eligible']
    save(directory/'eligibility_after_calls.json',current,new=True)
    save(directory/'manual_final_review.json',{'created_at':now(),'question_id':qid,'variant_id':variant,
         'role':'PRIMARY_MANUAL_FULL_RAW_REVIEW','responses':reviews,'two_complete_preset_hits':False,
         'complete_calls':2,'request_binding_snapshot_raw_hashes_verified':True,
         'no_third_call_no_relabeling_no_retry':True,
         'diagnosis':diagnosis,
         'decision':'FAILED_FROZEN_WRONG_PRESET_RETAIN_ALL_EVIDENCE'},new=True)
    save(directory/'primary_review.json',{'question_id':qid,'variant_id':variant,'decision':'FAILED_0_OF_2_PRESET_HITS',
         'original_correct_answer':'180','frozen_wrong_preset':design['expected_wrong_answer'],'observed_finals':values,
         'manual_review_path':str(directory/'manual_final_review.json'),'summary_path':str(evidence/'summary.json'),
         'not_a_second_review':True,'no_formal_actions':True,'retain_frozen_failed_input':True},new=True)
    checkpoint=read(OWN/'checkpoint.json')
    failed=checkpoint['questions'][qid].get('failed_variants',[])
    if variant not in failed: failed.append(variant)
    checkpoint['questions'][qid].update(status='design_failed_further_distinct_correspondence_under_review',
        failed_variants=failed,observed_finals=values,unfinished_reason='No double-hit PRIMARY yet; assessing substantively different true correspondence.')
    checkpoint.update(updated_at=now()); save(OWN/'checkpoint.json',checkpoint)
    print('Plane490 '+variant+' failed preset'+design['expected_wrong_answer']+' with two complete '+','.join(values)+' finals; retained unchanged.')

def prepare490_flanks():
    qid='Plane490'; variant='a02_corresponding_arrowhead_flank_directions'; directory=OWN/qid/variant
    current=eligibility(qid); assert current['eligible']
    save(directory/'eligibility_before_design.json',current,new=True)
    ctx=read(OWN/qid/'context.json')
    actions=[]; roles=[]
    for target_id, name in [('o0','light'),('o1','dark')]:
        target=next(t for t in ctx['canvas']['targets'] if t['id']==target_id)
        path=target['partial_paths'][0]; s=[v[2] for v in path['samples']]
        for edge,color in [(2,'#DC2626'),(3,'#2563EB')]:
            start=s[edge]+(s[edge+1]-s[edge])/4
            end=s[edge]+3*(s[edge+1]-s[edge])/4
            actions.append({'type':'set_object_style','target':target_id,'color':color,'linewidth_pt':1.5,
                 'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':start,'end':end,'wrap':False}})
            roles.append({'target':target_id,'edge_index':edge,'color':color,'interval':[start,end],
                 'source':name+' arrow original sloped head edge, middle half only',
                 'receiver':('dark' if name=='light' else 'light')+' arrow same cyclic sloped edge under true180 rotation',
                 'use':'Compares the true parallel unoriented side-direction class across actual arrowheads. Partial marks retain original black/gray tips and shoulders; no mark is fully covered or invented.'})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
            'description':'Compare true corresponding sloped arrowhead sides by red/blue middle strips.',
            'intent':'PRIMARY research only; original gray identity, endpoints and arrow directions retained.',
            'params':{'actions':actions}}
    save(directory/'plugin_input.json',plugin,new=True)
    reference=read(OWN/qid/'a01_shared_boundary_invariance/reference_transfer.json')['reference']
    semantics='The red middle strip on dark cyclic head edge2 maps exactly to red light edge2 under180; blue dark edge3 maps to blue light edge3. The identical parameter fractions on negated vertices preserve strip lengths and endpoint incidence. Reading the color strips as intrinsic edging therefore retains180 and cannot supply a different valid rotation because the full polygon mean still forces180. Unmarked tips/shoulders and nearly all shafts retain original black/gray contrast, so darker/lighter source identity remains clear. The strips are continuous strokes on actual sloped boundaries, not cuts, new points, detachable pieces or changing head direction.'
    difference='A01 compared actual common-boundary spatial coincidence, an invariant Z subset already at the same positions. This A02 entirely removes those shaft marks and instead pairs two distinct sloped head edges on each of the two arrows, using true180 correspondences whose undirected slopes agree. Its error hypothesis is parallel unoriented directions mistaken for zero angular change despite opposite directed heads, rather than local positional overlap. Old prescreens mentioned same-side shafts and arbitrary perpendicular edges; neither is used. This is not a recolor/width-only adjustment to the failed input.'
    mechanism='The red true corresponding slants have the same unoriented line slope, as do the blue pair. A solver might match direction classes as already aligned and return0 without tracking the orientation of endpoints and the reversed heads. Preset0, before both calls; correct full-object angle remains180. This distinct hypothesis uses arrowheads rather than omitting them.'
    proposal={'question_id':qid,'variant_id':variant,'created_at':now(),'expected_wrong_answer':'0',
         'expected_wrong_value_degrees':'0','correct_answer':'180','mechanism':mechanism,'mark_roles':roles,
         'human_semantics':semantics,'primary_math_proof':str(OWN/qid/'primary_math_proof.json'),
         'substantive_history_difference':difference,'reference':reference,
         'review_status':'PRIMARY_PROPOSAL_BEFORE_RENDER_AND_CALLS','calls':0}
    save(directory/'design_proposal.json',proposal,new=True)
    save(directory/'reference_transfer.json',{'reference':reference,'transferred':'Compare real paired sides using two colors; existing head geometry only.',
         'difference_from_old':difference,'mark_roles':roles,'semantics':semantics},new=True)
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint['questions'][qid].update(status='second_distinct_proposal_before_render',variant_id=variant)
    checkpoint.update(updated_at=now()); save(OWN/'checkpoint.json',checkpoint)
    print('Plane490 distinct arrowhead-flank direction hypothesis proposed; no further calls yet.')

def prepare490_corners():
    qid='Plane490'; variant='a03_true_corresponding_notch_right_angles'; directory=OWN/qid/variant
    current=eligibility(qid); assert current['eligible']
    save(directory/'eligibility_before_design.json',current,new=True)
    ctx=read(OWN/qid/'context.json'); actions=[]; roles=[]
    for target_id,name in [('o0','light'),('o1','dark')]:
        target=next(t for t in ctx['canvas']['targets'] if t['id']==target_id)
        path=target['partial_paths'][0]; s=[v[2] for v in path['samples']]
        for edge,color in [(4,'#DC2626'),(5,'#2563EB')]:
            actions.append({'type':'set_object_style','target':target_id,'color':color,'linewidth_pt':1.5,
                 'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':s[edge],'end':s[edge+1],'wrap':False}})
            roles.append({'target':target_id,'edge_index':edge,'color':color,
                 'source':name+' original '+('short vertical notch wall length2' if edge==4 else 'long horizontal outside shaft edge length8'),
                 'receiver':('dark' if name=='light' else 'light')+' corresponding '+('vertical notch wall' if edge==4 else 'horizontal shaft edge'),
                 'use':'Displays the actual two-edge L at the nonshared head/shaft notch; corresponding corner locations negate aboutC. Red versus blue tracks short wall versus long side, not arbitrary equal-length or perpendicular new assumptions.'})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
            'description':'Compare actual corresponding open L boundaries at the arrow notches.',
            'intent':'PRIMARY only: existing walls and shafts, gray arrowheads and shared center path retained.',
            'params':{'actions':actions}}
    save(directory/'plugin_input.json',plugin,new=True)
    reference=read(OWN/qid/'a01_shared_boundary_invariance/reference_transfer.json')['reference']
    reference['secondary_reference']={'question_id':'Plane233','png_sha256':sha(TASK/'references/Plane233/C01.png'),
           'plugin_sha256':sha(TASK/'references/Plane233/C01.json'),
           'actual_png_viewed':True,'method':'Current red vertical/blue horizontal open L boundary comparison in source and optionC; no copied option label is relevant here.'}
    semantics='Dark notch(-4,-2) has original red vertical edge from(-4,-4) and blue horizontal edge to(4,-2). Light corresponding notch(4,2) has red vertical edge from(4,4) and blue horizontal edge to(-4,2). Under180 the entire red/blue edge pattern maps exactly. The small white notch opening is90 degrees because its two existing edges are perpendicular; the polygon reflex interior there is270, not90. This is a local boundary angle, not a new rotation angle condition. Both arrowheads, all sloped lines, centerC, original dark/gray uncolored portions and shared centralZ remain unchanged. Literal colored edging still maps exactly under180, and the full corner mean still excludes every other angle.'
    difference='A01 colored the coincident shared centralZ and tested local positional identity0. A02 colored sloped head-edge middle strips and tested parallel unoriented directions0; its observed90/90 remains outside its preset and is not reused as passing evidence. A03 removes all those marks and instead pairs two true nonshared concave notch corners, each with a red short vertical side and a blue long horizontal side. Its concrete new wrong-angle hypothesis is substituting the90-degree notch opening for the rigid rotation. This changes the actual marked objects, their incidence structure, and their geometric role; it is not a relabeling, recolor, width or filename adjustment of either earlier input.'
    mechanism='The two open L boundaries display a local90-degree angle between actual short vertical and long horizontal sides. A solver might report the salient notch opening90 as the requested rotation, without using the opposite corner positions and complete arrowheads. Preset90 degrees is justified by the marked perpendicular boundary relation before either A03 call. It is not justified by treating the already observed A02 finals as hits; A02 stays failed0/2.'
    save(directory/'design_proposal.json',{'question_id':qid,'variant_id':variant,'created_at':now(),
         'expected_wrong_answer':'90','expected_wrong_value_degrees':'90','correct_answer':'180',
         'mechanism':mechanism,'mark_roles':roles,'human_semantics':semantics,
         'primary_math_proof':str(OWN/qid/'primary_math_proof.json'),
         'substantive_history_difference':difference,'reference':reference,
         'review_status':'PRIMARY_PROPOSAL_BEFORE_RENDER_AND_CALLS','calls':0},new=True)
    save(directory/'reference_transfer.json',{'reference':reference,'transferred':'Current427 real side-role comparison plus current233 openL red vertical/blue horizontal boundaries.',
         'difference_from_old':difference,'mark_roles':roles,'semantics':semantics},new=True)
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint['questions'][qid].update(status='new_notch_angle_proposal_before_render',variant_id=variant)
    checkpoint.update(updated_at=now()); save(OWN/'checkpoint.json',checkpoint)
    print('Plane490 true notch-L correspondence proposal saved with fresh preset90; A02 remains failed.')

if __name__ == '__main__':
    if sys.argv[1] == 'initial': initial()
    elif sys.argv[1] == 'context': context(sys.argv[2])
    elif sys.argv[1] == 'history': history_read()
    elif sys.argv[1] == 'prepare': prepare()
    elif sys.argv[1] == 'render': render_candidate(*sys.argv[2:4])
    elif sys.argv[1] == 'replay': replay(*sys.argv[2:4])
    elif sys.argv[1] == 'freeze': freeze(*sys.argv[2:4])
    elif sys.argv[1] == 'harness': harness_copy()
    elif sys.argv[1] == 'test': test(*sys.argv[2:4])
    elif sys.argv[1] == 'review321': review321()
    elif sys.argv[1] == 'review490': review490(sys.argv[2])
    elif sys.argv[1] == 'prepare490_flanks': prepare490_flanks()
    elif sys.argv[1] == 'prepare490_corners': prepare490_corners()
