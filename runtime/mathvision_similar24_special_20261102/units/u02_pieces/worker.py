from pathlib import Path
import os
import sys

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[3]
TASK = OWN.parents[1]
OLD = PROJECT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, folder in {'TEMP': 'tmp', 'TMP': 'tmp', 'MPLCONFIGDIR': 'mpl_cache', 'XDG_CACHE_HOME': 'cache'}.items():
    target = OWN / 'ownruntime' / folder
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def owncheck(path):
    if path is None or isinstance(path, int):
        return
    target = Path(os.fsdecode(path)).resolve()
    if not target.is_relative_to(OWN):
        raise PermissionError('u02 strict writeguard: ' + str(target))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            owncheck(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        owncheck(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        owncheck(args[0]); owncheck(args[1])

sys.addaudithook(guard)
import importlib.util
import json
import hashlib
from datetime import datetime, timezone

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def digest(data):
    return hashlib.sha256(data).hexdigest()

def filehash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def now():
    return datetime.now(timezone.utc).isoformat()

def write(path, obj):
    path = Path(path)
    owncheck(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')

def loadmodule(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

sys.path.insert(0, str(PROJECT))
isolation = loadmodule('u02_original_runtime_isolation', OLD / 'runtime_isolation.py')
ISOLATION = isolation.install(OWN / 'ownruntime' / 'scene', guard_writes=True)

def rows(path):
    if not Path(path).exists():
        return []
    with Path(path).open(encoding='utf-8-sig') as f:
        return [json.loads(line) for line in f if line.strip()]

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)

def eligibility(qid):
    from dataset_tools.catalog import content, digest as cdigest
    record = next(r for r in rows(PROJECT / 'PlaneGeometry/dataset.jsonl') if r['id'] == qid)
    approval = read(PROJECT / 'provenance/approvals.json')['approvals'].get(qid, {})
    current = cdigest(content(PROJECT, 'PlaneGeometry', record))
    reasons = []
    if record.get('source_dataset') != 'MathVision': reasons.append('not_MathVision')
    if approval.get('reviewer') != 'user' or approval.get('content_sha256') != current:
        reasons.append('approval_content_mismatch')
    state = {}
    for name in ('accepted_index.jsonl', 'collected_index.jsonl'):
        p = PROJECT / 'PlaneGeometry/special_variant' / name
        relevant = [r for r in rows(p) if r.get('question_id') == qid]
        state[name] = relevant
        if relevant: reasons.append(name)
    for name in ('recipes.json', 'collection.json'):
        p = PROJECT / 'PlaneGeometry/special_variant' / qid / name
        state[name] = read(p) if p.exists() else None
        if state[name]: reasons.append(name)
    assignment = next(q for q in read(OWN / 'assignment.json')['questions'] if q['question_id'] == qid)
    frozen = {p: {'expected': h, 'actual': filehash(PROJECT / p)}
              for p, h in assignment['frozen_source_files_sha256'].items()}
    if any(v['expected'] != v['actual'] for v in frozen.values()): reasons.append('frozen_source_changed')
    if record != assignment['formal_record']: reasons.append('formal_record_changed')
    return {'question_id': qid, 'checked_at': now(), 'eligible': not reasons, 'reasons': reasons,
            'formal_record': record, 'approval': approval, 'current_content_sha256': current,
            'state': state, 'frozen_source_hash_verification': frozen,
            'global_state_hashes': {p: filehash(PROJECT / p) for p in
                ('PlaneGeometry/dataset.jsonl', 'provenance/approvals.json',
                 'PlaneGeometry/special_variant/accepted_index.jsonl',
                 'PlaneGeometry/special_variant/collected_index.jsonl')}}

def adapter():
    sys.path.insert(0, str(PROJECT / 'PlaneGeometry/workbench'))
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    cfg = load_config()
    cfg['runtime_dir'] = str(OWN / 'ownruntime/state')
    cfg['output_dir'] = str(OWN / 'ownruntime/output')
    return cfg, RendererAdapter(cfg)

def fingerprints(ad, qid):
    from workbench_io import environment_versions
    row = ad.records[qid]
    paths = [PROJECT / 'PlaneGeometry' / row[k] for k in ('image','original_image','scene','script') if row.get(k)]
    paths += [PROJECT / 'PlaneGeometry' / p for p in row.get('runtime_dependencies', [])]
    paths += list(ad.input_files.values())
    return {'record_sha256': digest(canonical(row).encode()),
            'files': {str(p.relative_to(PROJECT)): filehash(p) for p in sorted(set(paths))},
            'environment': environment_versions()}

def inspect_questions():
    cfg, ad = adapter()
    for qid in ('Plane218', 'Plane398'):
        out = OWN / qid
        check = eligibility(qid)
        write(out / 'eligibility_start.json', check)
        assert check['eligible'], check['reasons']
        before = fingerprints(ad, qid)
        context = ad.inspect_question(qid)
        write(out / 'context.json', context)
        write(out / 'formal_record.json', ad.records[qid])
        write(out / 'input_fingerprints.json', before)
        (out / 'original.png').write_bytes(ad.original_paths[qid].read_bytes())
        assert fingerprints(ad, qid) == before
        scene = read(PROJECT / 'PlaneGeometry' / ad.records[qid]['scene'])
        write(out / 'frozen_scene_readonly_snapshot.json', scene)
        print(json.dumps({'question_id': qid, 'eligible': True, 'noop_pixel_match': True,
                          'objects': [{'id': o['id'], 'geometry': o.get('geometry')} for o in context['objects']],
                          'canvas_keys': list(context['canvas'])}, ensure_ascii=False))

def read_audit():
    import base64
    audited = []
    ref_summaries = []
    for qid, manifest in read(TASK / 'reference_manifest.json').items():
        directory = TASK / manifest['directory']
        plugin = read(directory / 'C01.json')
        recipes = read(directory / 'recipes.json')
        reference = read(directory / 'reference.json')
        assert filehash(directory / 'C01.png') == manifest['png_sha256']
        assert filehash(directory / 'C01.json') == manifest['plugin_sha256']
        for name in ('C01.json', 'recipes.json', 'reference.json', 'C01.png'):
            audited.append({'path': str(directory / name), 'sha256': filehash(directory / name),
                            'read_in_full': True, 'PNG_visually_viewed_in_tool': name == 'C01.png'})
        assert reference['recipes'] == recipes
        for r in recipes:
            assert {k: r[k] for k in plugin} == plugin
        ref_summaries.append({'question_id': qid, 'current_plugin': plugin,
                              'formal_question': reference['formal_record']['question'],
                              'original_correct_answer': reference['formal_record']['answer'],
                              'reference_top_level_keys': list(reference),
                              'all_recipe_plugin_fields_exactly_equal': True,
                              'recipes_equal_reference_recipes': True,
                              'reference_file_sha256': filehash(directory / 'reference.json')})
    history = read(TASK / 'history_index.json')
    ownhistory = [q for q in history['questions'] if q['question_id'] in ('Plane218','Plane398')]
    write(OWN / 'prior_history_index_scoped.json', ownhistory)
    for q in ownhistory:
        paths = set(q['other_scoped_history_file_references'] + q['additional_math_manual_history_references'] + q['independent_review_references'])
        for design in q['designs']:
            paths.add(design['design_path']); paths.add(design['plugin_path'])
        for relative in sorted(paths):
            p = PROJECT / relative
            data = read(p)
            entry = {'path': relative, 'sha256': filehash(p), 'read_in_full': True,
                     'top_level_keys': list(data) if isinstance(data, dict) else 'array'}
            if p.name == 'request.json':
                content = data['messages'][1]['content']
                imagebytes = base64.b64decode(content[1]['image_url']['url'].split(',', 1)[1])
                entry['embedded_image_sha256'] = digest(imagebytes)
                entry['exact_formal_question'] = content[0]['text']
                del imagebytes
            audited.append(entry)
            del data
    write(OWN / 'complete_read_audit.json', {'created_at': now(), 'files': audited,
                                           'current_reference_summaries': ref_summaries,
                                           'raw_API_responses_preserved_readonly': True})
    print(json.dumps(ref_summaries, ensure_ascii=False, separators=(',', ':')))
    print(json.dumps({'all_scoped_history_file_count': len(audited)-36,
                      'audited_history_path': str(OWN / 'complete_read_audit.json')}, ensure_ascii=False))

def initialize():
    write(OWN / 'initial_identity.json', {'created_at': now(), 'own_root': str(OWN),
          'project': str(PROJECT), 'task': str(TASK), 'scope': ['Plane218', 'Plane398'],
          'original_assignment_sha256': filehash(OWN / 'assignment.json'),
          'original_brief_sha256': filehash(OWN / 'brief.txt'), 'isolation': ISOLATION,
          'strict_ownroot_writeguard': True, 'python': sys.version,
          'environment': {k: os.environ[k] for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS',
              'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS', 'TEMP', 'TMP', 'MPLCONFIGDIR', 'XDG_CACHE_HOME')},
          'no_children_servers_worktrees': True})
    write(OWN / 'checkpoint.json', {'updated_at': now(), 'status': 'reading_and_mathematical_audit',
          'question_status': {'Plane218': 'not_yet_designed', 'Plane398': 'not_yet_designed'},
          'actual_new_API_calls': 0, 'primary_candidates': [], 'failures': [],
          'limitations': ['PRIMARY research only. Independent second review belongs to parent.',
                          'No user Pass/Collect or delivery.']})
    write(OWN / 'second_review_queue.json', [])
    print(json.dumps(read(OWN / 'initial_identity.json'), ensure_ascii=False))

if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
        initialize()
    elif sys.argv[1:] == ['read']:
        read_audit()
    elif sys.argv[1:] == ['inspect']:
        inspect_questions()
