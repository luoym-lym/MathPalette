from env56 import *
from dataset_tools import catalog
from workbench_io import load_config, pixel_hash
from mathvision_adapter import RendererAdapter
from dataset_tools.mathvision_workbench import png_bytes

QIDS = read(BASE/'background_56_assignment.json')['question_ids']
RELATED = ['Plane382','Plane244','Plane340']
protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json']
history={q:[] for q in QIDS+RELATED}
for p in BASE.rglob('*'):
    if not p.is_file() or p.is_relative_to(OWN): continue
    for q in history:
        if q in p.parts or p.name.startswith(q+'_'):
            history[q].append({'path':str(p.relative_to(PROJECT)),'sha256':sha(p),'bytes':p.stat().st_size})
save('old_history_manifest.json',history)
source_paths=set(protocols+['dataset_tools/catalog.py','dataset_tools/geometry_dataset.py','dataset_tools/mathvision_workbench.py','PlaneGeometry/workbench/mathvision_adapter.py','PlaneGeometry/workbench/mathvision_plugins.py','PlaneGeometry/workbench/render_plugins.py','PlaneGeometry/workbench/renderer_adapter.py','PlaneGeometry/workbench/partial_style.py','PlaneGeometry/workbench/config.json','PlaneGeometry/workbench/quick_test.py','provenance/source_notes.json','runtime/mathvision_special_20261101/runtime_isolation.py','runtime/mathvision_special_20261101/harness/quicktest3_isolated.py','runtime/mathvision_special_20261101/background_56_brief.txt','runtime/mathvision_special_20261101/background_56_assignment.json'])
for q in QIDS+RELATED:
    rec=next(r for r in catalog.rows(PROJECT/'PlaneGeometry/dataset.jsonl') if r['id']==q)
    source_paths.update('PlaneGeometry/'+rec[f] for f in catalog.PATH_FIELDS if rec.get(f))
    source_paths.update('PlaneGeometry/'+p for p in rec['runtime_dependencies'])
for p in BASE.glob('batch_*'):
    if p.is_file() or p.is_dir():
        for f in ([p] if p.is_file() else p.rglob('*')):
            if f.is_file(): source_paths.add(str(f.relative_to(PROJECT)))
for entries in history.values(): source_paths.update(e['path'] for e in entries)
save('readonly_hashes_start.json',{p:sha(PROJECT/p) for p in sorted(source_paths)})
save('isolation.json',{'at':now(),'own_root':str(OWN),'strict_write_guard_before_project_imports':True,'runtime_isolation':ISOLATION,'env':{k:os.environ[k] for k in ('TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')}})
config=load_config()
adapter=RendererAdapter(config)
for q in QIDS:
    e=eligibility(q)
    save(f'{q}/eligibility_start.json',e)
    save(f'{q}/formal_record.json',e['formal_record'])
    if not e['eligible']:
        print(q, 'INELIGIBLE',e['reasons'],flush=True); continue
    context=adapter.inspect_question(q)
    save(f'{q}/context.json',context)
    scene=adapter.scene(q)
    try: data=png_bytes(scene)
    finally: scene.close()
    (OWN/q/'noop.png').write_bytes(data)
    assert pixel_hash(data)==context['original_pixel_sha256']
    save(f'{q}/baseline.json',{'no_op_pixel_match':True,'png_sha256':sha(OWN/q/'noop.png'),'formal_png_sha256':sha(PROJECT/'PlaneGeometry'/e['formal_record']['image']),'pixel_sha256':pixel_hash(data)})
    print(q, 'eligible; native baseline matches;',len(context['objects']),'objects',flush=True)
save('protocol_read_log.json',{'protocols':{p:sha(PROJECT/p) for p in protocols},'brief':sha(BASE/'background_56_brief.txt'),'assignment':sha(BASE/'background_56_assignment.json'),'continuation':sha(BASE/'continuation_brief.txt'),'read_complete_utf8':True})
