from env58 import *
import gc

def inventory():
    protocols = ['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md',
                 'PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md',
                 'PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json']
    source_paths = set(protocols + ['dataset_tools/catalog.py','dataset_tools/geometry_dataset.py',
        'dataset_tools/mathvision_workbench.py','provenance/source_notes.json','provenance/approvals.json',
        'PlaneGeometry/dataset.jsonl','PlaneGeometry/special_variant/accepted_index.jsonl',
        'PlaneGeometry/special_variant/collected_index.jsonl'])
    for p in (PROJECT/'PlaneGeometry/workbench').glob('*.py'):
        source_paths.add(str(p.relative_to(PROJECT)))
    source_paths.add('PlaneGeometry/workbench/config.json')
    source_paths.add('PlaneGeometry/workbench/plugin.schema.json')
    for qid in QIDS + RELATED:
        rec = row(qid)
        for field in ('image','original_image','scene','script'):
            if rec.get(field): source_paths.add('PlaneGeometry/' + rec[field])
        source_paths.update('PlaneGeometry/' + p for p in rec.get('runtime_dependencies', []))
    history = {q:[] for q in QIDS + RELATED}
    for p in BASE.rglob('*'):
        if not p.is_file() or p.is_relative_to(OWN): continue
        for q in history:
            if q in p.parts or p.name.startswith(q+'_'):
                rel = str(p.relative_to(PROJECT))
                history[q].append({'path':rel, 'bytes':p.stat().st_size, 'sha256':sha(p)})
                source_paths.add(rel)
    for p in BASE.glob('batch_*'):
        for f in ([p] if p.is_file() else p.rglob('*')):
            if f.is_file(): source_paths.add(str(f.relative_to(PROJECT)))
    for p in (BASE/'runtime_isolation.py', BASE/'harness/quicktest3_isolated.py'):
        source_paths.add(str(p.relative_to(PROJECT)))
    save('old_history_manifest.json', history)
    save('readonly_hashes_start.json', {p:sha(PROJECT/p) for p in sorted(source_paths)})
    save('isolation.json', {'created_at':now(), 'own_root':str(OWN), 'strict_guard_before_project_imports':True,
        'runtime_isolation':ISOLATION, 'environment':{k:os.environ[k] for k in
        ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},
        'no_remote_settings_modified':True})
    print(json.dumps({'history_files':{q:len(v) for q,v in history.items()}, 'frozen_paths':len(source_paths)}),flush=True)

def prepare(qid):
    assert qid in QIDS
    e = eligibility(qid)
    save(f'{qid}/eligibility_start.json',e)
    save(f'{qid}/formal_record.json',e['formal_record'])
    if not e['eligible']:
        print(json.dumps({'question_id':qid,'eligible':False,'reasons':e['reasons']})); return
    from workbench_io import load_config, pixel_hash
    from mathvision_adapter import RendererAdapter
    from dataset_tools.mathvision_workbench import png_bytes
    adapter = RendererAdapter(load_config())
    context = adapter.inspect_question(qid)
    save(f'{qid}/context.json', context)
    native = adapter.scene(qid)
    try:
        data = png_bytes(native)
        save(f'{qid}/native_source_state.json', {'objects':native.objects,'snap_points':native.snap_points,
            'artist_types':{k:[type(a).__name__ for a in v] for k,v in native.artists.items()}})
    finally:
        native.close()
    (OWN/qid/'noop.png').write_bytes(data)
    assert pixel_hash(data) == context['original_pixel_sha256']
    save(f'{qid}/baseline.json', {'created_at':now(),'no_op_pixel_equality':True,
        'formal_png_sha256':sha(PROJECT/'PlaneGeometry'/e['formal_record']['image']),
        'noop_sha256':sha(OWN/qid/'noop.png'), 'pixel_sha256':pixel_hash(data)})
    print(json.dumps({'question_id':qid,'eligible':True,'approval_fingerprint_matches':True,
        'baseline_matches':True,'objects':len(context['objects'])}),flush=True)
    del context, data, native, adapter
    gc.collect()

def context(qid):
    c=read(OWN/qid/'context.json')
    print(json.dumps({'question_id':qid,'snap_points':c['snap_points'], 'objects':c['objects'],
                     'canvas_keys':list(c['canvas'])},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    import traceback
    try:
        command=sys.argv[1]
        if command=='inventory': inventory()
        elif command=='prepare': prepare(sys.argv[2])
        elif command=='context': context(sys.argv[2])
        else: raise ValueError(command)
    except Exception as exc:
        save('local_failure_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'.json',
             {'created_at':now(),'argv':sys.argv,'type':type(exc).__name__,'error':str(exc),
              'traceback':traceback.format_exc(),'no_API_in_this_script':True})
        raise
