"""Independent read-only Plane324 audit. No network, solver, or approval calls."""
import os
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in OUT.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
BASE = ROOT / 'runtime/mathvision_special_20261101'
PARENT = BASE / 'background_10/Plane324'
CAND = PARENT / 'three_corner_triangle_groups'
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def own_guard(event, args):
    def check(value):
        if value is None or isinstance(value, int):
            return
        if not Path(os.fsdecode(value)).resolve().is_relative_to(OUT):
            raise PermissionError('Independent review write outside assigned directory: ' + str(value))
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check(args[0]); check(args[1])
    elif event in ('subprocess.Popen', 'os.system', 'os.fork'):
        raise PermissionError('No child processes in independent review')
    elif event == 'socket.connect':
        raise PermissionError('No network in independent review')

sys.addaudithook(own_guard)
for var, name in {'TEMP': 'tmp', 'TMP': 'tmp', 'TMPDIR': 'tmp',
                  'MPLCONFIGDIR': 'mplcache', 'XDG_CACHE_HOME': 'cache',
                  'PYTHONPYCACHEPREFIX': 'pycache'}.items():
    location = OUT / name
    location.mkdir(exist_ok=True)
    os.environ[var] = str(location)
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(OUT / 'render_tmp', guard_writes=True)

import base64
import hashlib
import io
import itertools
import json
import math
from datetime import datetime, timezone

def now():
    return datetime.now(timezone.utc).isoformat()
def sha(data):
    return hashlib.sha256(data).hexdigest()
def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()] if Path(path).exists() else []
def fh(path):
    return sha(Path(path).read_bytes()) if Path(path).is_file() else None
def canonical(data):
    return sha(json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
def rel(path):
    return str(Path(path).resolve().relative_to(ROOT)).replace('\\', '/')
def save(name, data):
    with (OUT / name).open('w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')
def describe(path):
    path = Path(path)
    if not path.is_file():
        return {'sha256': None, 'exists': False}
    s = path.stat()
    return {'sha256': fh(path), 'size': s.st_size,
            'mtime_utc': datetime.fromtimestamp(s.st_mtime, timezone.utc).isoformat(),
            'ctime_utc': datetime.fromtimestamp(s.st_ctime, timezone.utc).isoformat()}

started = now()
source_inputs = read(CAND / 'source_inputs.json')
sources_start = {p: fh(ROOT / p) for p in source_inputs['files']}
existing_evidence = [p for p in PARENT.rglob('*') if p.is_file()]
existing_evidence += [BASE / 'background_10' / name for name in
    ['second_review_queue.json', 'primary_handoff.txt', 'source_preservation_audit.json',
     'candidate_evidence_audit.json', 'process_audit.json', 'render324.py', 'render_designs.py',
     'run_candidate.py', 'tools10.py']]
evidence_start = {rel(p): describe(p) for p in existing_evidence}
save('evidence_manifest_start.json', evidence_start)
save('source_hashes_start.json', sources_start)

sys.path.insert(0, str(ROOT / 'PlaneGeometry/workbench'))
from workbench_io import load_config, pixel_hash, environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools import catalog
from dataset_tools.mathvision_workbench import png_bytes
from PIL import Image
import numpy as np

record = next(r for r in rows(ROOT / 'PlaneGeometry/dataset.jsonl') if r['id'] == 'Plane324')
formal_scene = read(ROOT / 'PlaneGeometry' / record['scene'])
points = [o['center'] for o in formal_scene['objects']]
assert len(points) == 10 and all(o['type'] == 'circle' for o in formal_scene['objects'])
uv = [(round(2*x), round(2*y/math.sqrt(3))) for x, y in points]
reconstruction_errors = [max(abs(x-u/2), abs(y-v*math.sqrt(3)/2)) for (x,y),(u,v) in zip(points,uv)]
assert max(reconstruction_errors) < 1e-14
def d4(a,b):
    return (uv[a][0]-uv[b][0])**2 + 3*(uv[a][1]-uv[b][1])**2
triples = [t for t in itertools.combinations(range(10),3)
           if d4(t[0], t[1]) == d4(t[0], t[2]) == d4(t[1], t[2]) > 0]
by_size = {}
all_hitting = {}
witnesses = []
for size in range(5):
    subsets = list(itertools.combinations(range(10), size))
    all_hitting[size] = [s for s in subsets if all(set(s).intersection(t) for t in triples)]
    by_size[size] = {'subsets_checked': len(subsets), 'hitting_sets': len(all_hitting[size])}
    if size <= 3:
        for subset in subsets:
            survivor = next(t for t in triples if not set(subset).intersection(t))
            witnesses.append({'removed': subset, 'surviving_equilateral_triple': survivor})
minimum = next(k for k,v in all_hitting.items() if v)
proof = {'method': 'Fresh exhaustive exact integer squared-distance and hitting-set enumeration from all ten formal circle centers.',
         'points': points, 'uv_coordinates': uv, 'reconstruction_max_error': max(reconstruction_errors),
         'metric': '4*d^2=(delta u)^2+3*(delta v)^2', 'all_triples_checked': 120,
         'all_equilateral_triples': triples, 'distance4_by_triple': [{'triple': t, 'distance4': d4(t[0],t[1])} for t in triples],
         'enumeration_counts': by_size, 'minimum': minimum,
         'all_minimum_removal_sets': all_hitting[minimum],
         'all_size_0_through_3_survivor_witnesses': witnesses}
primary = read(PARENT / 'equilateral_hitting_set_proof.json')
certificate = read(PARENT / 'exact_integer_math_certificate.json')
proof['primary_triples_match'] = primary['all_equilateral_triples'] == [list(t) for t in triples]
proof['primary_minimum_sets_match'] = primary['all_minimum_removal_sets'] == [list(t) for t in all_hitting[minimum]]
proof['certificate_keys'] = list(certificate)
proof['certificate_triples_match'] = certificate['all_equilateral_triples'] == [list(t) for t in triples]
proof['certificate_uv_match'] = certificate['uv_coordinates'] == [list(t) for t in uv]
save('independent_math_enumeration.json', proof)

cfg = load_config()
cfg['runtime_dir'] = str(OUT / 'render_state')
cfg['output_dir'] = str(OUT / 'render_output')
adapter = RendererAdapter(cfg)
context = adapter.inspect_question('Plane324')
save('independent_context.json', context)
plugin = read(CAND / 'plugin.json')
renderer = PluginRenderer(cfg, adapter, {'Plane324': context})
normalized = renderer.normalize(plugin)
render_checks = {'environment': environment_versions(), 'isolation': ISOLATION,
                 'normalized_exactly_equal': normalized == plugin,
                 'fresh_context_equal_stored': context == read(CAND / 'fresh_context.json'),
                 'formal_original_pixel_sha256': pixel_hash(ROOT / 'PlaneGeometry/image/Plane324.png')}
scene = adapter.scene('Plane324')
try:
    noop = png_bytes(scene)
    (OUT / 'noop.png').write_bytes(noop)
    scene.fig.canvas.draw()
    pixels = scene.ax.transData.transform(points).tolist()
    pixels = [[float(x),float(768-y)] for x,y in pixels]
    original_artists = {oid: [{'class':type(a).__name__,
        'center':list(a.center) if hasattr(a,'center') else None,
        'radius':float(a.radius) if hasattr(a,'radius') else None,
        'facecolor':list(a.get_facecolor()) if hasattr(a,'get_facecolor') else None,
        'edgecolor':list(a.get_edgecolor()) if hasattr(a,'get_edgecolor') else None} for a in artists]
        for oid,artists in scene.artists.items()}
finally:
    scene.close()
render_checks['no_op_byte_identical_original'] = noop == (ROOT / 'PlaneGeometry/image/Plane324.png').read_bytes()
render_checks['no_op_pixel_identical_original'] = pixel_hash(noop) == render_checks['formal_original_pixel_sha256']
for i in (1,2):
    norm, data, pix = renderer.render(plugin, frozen=True)
    (OUT / f'rerender_{i}.png').write_bytes(data)
    render_checks[f'render_{i}'] = {'sha256':sha(data),'pixel_sha256':pix,
                                  'byte_identical_candidate':data==(CAND/'candidate.png').read_bytes(),
                                  'normalized_exactly_equal':norm==plugin}
render_checks['two_rerenders_byte_equal'] = (OUT/'rerender_1.png').read_bytes()==(OUT/'rerender_2.png').read_bytes()
render_checks['original_circle_artists'] = original_artists
render_checks['point_centers_image_pixels'] = pixels
endpoint_results=[]
all_ids = {o['id'] for o in context['objects']} | {p['id'] for p in context['snap_points']}
for index, action in enumerate(plugin['params']['actions']):
    endpoints = action['endpoints']
    matches = [[i for i,p in enumerate(points) if p==ep] for ep in endpoints]
    assert all(len(m)==1 for m in matches)
    a,b = [m[0] for m in matches]
    unrelated = []
    for j,p in enumerate(points):
        if j in (a,b): continue
        v=np.array(endpoints[1])-endpoints[0]; w=np.array(p)-endpoints[0]
        parameter=float(np.dot(v,w)/np.dot(v,v))
        if 0<parameter<1 and np.linalg.norm(w-parameter*v)<1e-10: unrelated.append(j)
    endpoint_results.append({'action_index':index,'id':action['id'],'endpoints':endpoints,
        'original_dot_indices':[a,b], 'exact_existing_dot_center_matches':True,
        'exact_snap_matches':[[p['id'] for p in context['snap_points'] if p['xy']==ep] for ep in endpoints],
        'id_legal_noncolliding':action['id'] not in all_ids,
        'line_width_pt':action['linewidth_pt'],'color':action['color'],'linestyle':action['linestyle'],
        'no_dash_pattern': 'dash_pattern_pt' not in action,'other_dot_on_segment_interior':unrelated})
render_checks['per_marker_exact_legality']=endpoint_results
original=np.array(Image.open(ROOT/'PlaneGeometry/image/Plane324.png').convert('RGBA'))
candidate=np.array(Image.open(CAND/'candidate.png').convert('RGBA'))
delta=np.any(original!=candidate,axis=2)
yy,xx=np.indices(delta.shape)
near_line=np.zeros(delta.shape,dtype=bool)
for result in endpoint_results:
    a,b=[np.array(pixels[i]) for i in result['original_dot_indices']]
    v=b-a
    tt=np.clip(((xx+.5-a[0])*v[0]+(yy+.5-a[1])*v[1])/np.dot(v,v),0,1)
    dd=np.sqrt((xx+.5-a[0]-tt*v[0])**2+(yy+.5-a[1]-tt*v[1])**2)
    near_line |= dd<=2.5
black_original = np.max(original[:,:,:3],axis=2)<40
black_candidate = np.max(candidate[:,:,:3],axis=2)<40
dot_stats=[]
for i,(x,y) in enumerate(pixels):
    local=(xx+.5-x)**2+(yy+.5-y)**2<21**2
    orig_count=int((black_original&local).sum())
    new_count=int((black_candidate&local).sum())
    dot_stats.append({'dot':i,'center_pixel':[x,y], 'original_black_pixels':orig_count,
                      'candidate_black_pixels':new_count,'black_pixel_retention':new_count/orig_count,
                      'changed_pixels_in_radius21':int((delta&local).sum())})
render_checks['pixel_difference']={'changed_pixels':int(delta.sum()),
    'changed_pixels_outside_2_5px_segment_corridors':int((delta&~near_line).sum()),
    'opaque':bool(np.all(candidate[:,:,3]==255)), 'size':list(candidate.shape[:2]),
    'added_black_pixels':int((black_candidate&~black_original).sum()), 'dot_stats':dot_stats}
save('render_and_legality_checks.json', render_checks)

def evidence_audit(folder):
    invocations = sorted((folder/'tests').glob('quicktest3_*'))
    findings=[]
    for invocation in invocations:
        binding=read(invocation/'binding.json'); request_bytes=(invocation/'request.json').read_bytes()
        request=json.loads(request_bytes); summary=read(invocation/'summary.json')
        user=request['messages'][1]['content']; embedded=base64.b64decode(user[1]['image_url']['url'].split(',',1)[1])
        snapshot=(invocation/'design_snapshot.json').read_bytes()
        runs=[]
        for i in (1,2):
            rp=invocation/f'run_{i:02d}.json'; rawp=invocation/f'run_{i:02d}_response.json'
            run=read(rp); raw=read(rawp); begun=read(invocation/f'run_{i:02d}_started.json')
            choice=raw['choices'][0]; content=choice['message']['content']
            tests={'request_matches':run['request_body_sha256']==sha(request_bytes),
                'image_matches':run['image_sha256']==sha(embedded)==binding['image_sha256']==fh(folder/'candidate.png'),
                'design_matches':run['design_sha256']==sha(snapshot)==binding['design_sha256']==fh(folder/'design.json'),
                'raw_response_hash_matches':run['response_sha256']==fh(rawp),
                'complete_content_matches_run':run['answer']==content,
                'completed':run['status']=='completed' and run['http_status']==200,
                'not_truncated':not run['truncated'] and choice['finish_reason']=='stop',
                'model_matches':raw['model']==run['response_model']==request['model']==binding['settings']['model']=='mimo-v2.6-flash',
                'summary_run_exact':summary['results'][i-1]==run,
                'started_record_matches':all(run[k]==v for k,v in begun.items()),
                'reasoning_tokens_zero':raw['usage']['completion_tokens_details']['reasoning_tokens']==0,
                'no_thinking_output':not run['thinking'],
                'pretest_created_order':read(folder/'design.json')['created_at']<binding['created_at']<=run['started_at']<run['finished_at']}
            runs.append({'run':i,'run_id':run['run_id'],'response_id':raw['id'],
                'started_at':run['started_at'],'finished_at':run['finished_at'],
                'provider_created':raw['created'],'raw_response_sha256':fh(rawp),'run_record_sha256':fh(rp),
                'finish_reason':choice['finish_reason'],'content_full':content,'checks':tests})
        findings.append({'invocation':rel(invocation),'binding':binding,'binding_sha256':fh(invocation/'binding.json'),
            'request_sha256':sha(request_bytes),'design_snapshot_sha256':sha(snapshot),
            'request_without_base64':{**request,'messages':[request['messages'][0],{'role':'user','content':[user[0],{'type':'image_url','image_url':{'url':'<PNG bytes SHA256 '+sha(embedded)+'>'}}]}]},
            'checks':{'only_model_stream_thinking_messages':set(request)=={'model','stream','thinking','messages'},
                'two_messages_only':len(request['messages'])==2,
                'only_formal_question_and_one_png':len(user)==2 and user[0]=={'type':'text','text':record['question']},
                'thinking_disabled':request['thinking']=={'type':'disabled'},'stream_false':request['stream'] is False,
                'binding_request_hash_matches':binding['request_body_sha256']==sha(request_bytes),
                'question_record_matches_current':binding['question_record_sha256']==canonical(record),
                'dataset_matches_current':binding['dataset_sha256']==fh(ROOT/'PlaneGeometry/dataset.jsonl'),
                'reference_quicktest_current_matches':binding['reference_quick_test_sha256']==fh(ROOT/'PlaneGeometry/workbench/quick_test.py'),
                'design_snapshot_byte_identical_current':snapshot==(folder/'design.json').read_bytes(),
                'summary_binding_equal':all(summary[k]==v for k,v in binding.items()),
                'two_completed':summary['two_completed'],'requested_runs_two':binding['requested_runs']==2,
                'exactly_two_run_records':len(list(invocation.glob('run_??.json')))==2,
                'no_errors_partial_extra_responses':len(list(invocation.glob('run_??_response.json')))==2 and not list(invocation.glob('*incomplete*')),
                'sequential_distinct_runs':runs[0]['run_id']!=runs[1]['run_id'] and runs[0]['finished_at']<=runs[1]['started_at']},
            'runs':runs})
    return {'invocation_count':len(invocations),'invocations':findings}

evidence={'candidate':evidence_audit(CAND),'original_control':evidence_audit(PARENT/'original_control')}
save('raw_binding_audit.json',evidence)

def eligibility():
    br=ROOT/'PlaneGeometry'; special=br/'special_variant'
    approval=read(ROOT/'provenance/approvals.json')['approvals']['Plane324']
    content=catalog.content(ROOT,'PlaneGeometry',record)
    paths=[br/'dataset.jsonl', ROOT/'provenance/approvals.json',special/'accepted_index.jsonl',
           special/'collected_index.jsonl',special/'Plane324/recipes.json',special/'Plane324/collection.json']
    manifests=sorted(BASE.glob('batch_*/manifest.json'))
    paths+=manifests
    accepted=[r for r in rows(special/'accepted_index.jsonl') if r.get('question_id',r.get('id'))=='Plane324']
    collected=[r for r in rows(special/'collected_index.jsonl') if r.get('question_id',r.get('id'))=='Plane324']
    per_question_files=[rel(p) for p in (special/'Plane324').rglob('*') if p.is_file()] if (special/'Plane324').exists() else []
    manifest_hits=[rel(p) for p in manifests if 'Plane324' in p.read_text(encoding='utf-8-sig')]
    reasons=[]
    if record['source_dataset']!='MathVision': reasons.append('not MathVision')
    if canonical(content)!=approval['content_sha256']: reasons.append('approval content mismatch')
    if accepted: reasons.append('accepted record exists')
    if collected: reasons.append('collected record exists')
    if per_question_files: reasons.append('formal special per-question files exist; inspect')
    if manifest_hits: reasons.append('published batch reference')
    diagnostic={rel(BASE/n):fh(BASE/n) for n in ['remaining_questions.jsonl','exploration_report.json']}
    return {'checked_at':now(),'eligible':not reasons,'reasons':reasons,'record':record,
        'record_sha256':canonical(record),'approval':approval,'computed_approval_content_sha256':canonical(content),
        'approval_content_matches':canonical(content)==approval['content_sha256'],
        'accepted_rows':accepted,'collected_rows':collected,'formal_special_per_question_files':per_question_files,
        'published_manifest_hits':manifest_hits,'authoritative_hashes':{rel(p):fh(p) for p in paths},
        'diagnostic_mutable_progress_hashes':diagnostic}
current=eligibility()
save('current_eligibility.json',current)
source_comparison=[]
for p,expected in source_inputs['files'].items():
    actual=sources_start[p]
    if expected!=actual:
        source_comparison.append({'path':p,'historical_sha256':expected,'current_sha256':actual,
            'classification':'pending_specific_classification'})
source_preservation={'source_snapshot_file_sha256':fh(CAND/'source_inputs.json'),
    'source_snapshot_file_count':len(source_inputs['files']),'changed_since_historical_snapshot':source_comparison,
    'observed_existing_evidence_unchanged_during_audit':all(describe(ROOT/p)==v for p,v in evidence_start.items()),
    'existing_evidence_file_count':len(evidence_start),
    'sources_unchanged_during_audit':all(fh(ROOT/p)==v for p,v in sources_start.items()),
    'diagnostic_progress_historical':read(PARENT/'eligibility_start.json')['diagnostic_runtime_metadata_hashes'],
    'diagnostic_progress_current':current['diagnostic_mutable_progress_hashes']}
save('source_preservation_checks.json',source_preservation)
save('audit_result.json',{'started_at':started,'finished_at':now(),'pid':os.getpid(),
    'minimum':minimum,'equilateral_triangle_count':len(triples),'render_checks_file':'render_and_legality_checks.json',
    'all_candidate_binding_checks':all(all(inv['checks'].values()) and all(all(r['checks'].values()) for r in inv['runs']) for inv in evidence['candidate']['invocations']),
    'current_eligible':current['eligible'],'source_preservation':source_preservation})
print(json.dumps({'minimum':minimum,'triples':triples,'minimum_sets':all_hitting[minimum],
    'render_checks':{k:v for k,v in render_checks.items() if k not in ['original_circle_artists','point_centers_image_pixels','per_marker_exact_legality']},
    'evidence_checks':{k:{'invocation_count':v['invocation_count'],'checks':[{'common':i['checks'],'runs':[r['checks'] for r in i['runs']]} for i in v['invocations']]} for k,v in evidence.items()},
    'eligibility':{k:v for k,v in current.items() if k!='record'},'source_preservation':source_preservation,
    'certificate_keys':list(certificate)},ensure_ascii=False,indent=2))
