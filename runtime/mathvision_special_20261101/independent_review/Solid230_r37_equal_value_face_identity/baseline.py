from review_env import *

record = next(r for r in rows(ROOT / 'SolidGeometry/dataset.jsonl') if r['id'] == 'Solid230')
paths = set()
for folder in [SHARED / 'background_37', SHARED / 'background_13/Solid230']:
    paths.update(p for p in folder.rglob('*') if p.is_file())
for name in [record[k] for k in ['image','original_image','scene','script']] + record['runtime_dependencies']:
    paths.add(ROOT / 'SolidGeometry' / name)
paths.update(ROOT / p for p in read(SHARED / 'background_37/Solid230/frozen_inputs.json')['files'])
extra = [
    'AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md',
    'SolidGeometry/dataset.jsonl','question_bank.jsonl','provenance/approvals.json','provenance/source_notes.json',
    'dataset_tools/catalog.py','dataset_tools/geometry_dataset.py','SolidGeometry/dataset_generator/common_renderer.py',
    'SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json',
    'SolidGeometry/workbench/quick_test.py','SolidGeometry/special_variant/accepted_index.jsonl',
    'SolidGeometry/special_variant/collected_index.jsonl',
    'runtime/mathvision_special_20261101/background_13/checkpoint.json',
    'runtime/mathvision_special_20261101/annotation_semantics_lesson_plane242_r24_20261102.json',
    'runtime/mathvision_special_20261101/independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json',
    'runtime/mathvision_special_20261101/Solid230_r37_equal_value_face_identity_independent_review_brief.txt',
    'runtime/mathvision_special_20261101/Solid230_r37_equal_value_face_identity_parent_binding_precheck.json',
]
paths.update(ROOT / p for p in extra if (ROOT / p).is_file())
for p in (SHARED / 'batch_12').glob('manifest.json'):
    paths.add(p)
for folder in (SHARED / 'independent_review').iterdir():
    if any(x in folder.name for x in ['Solid128','Solid197','Plane192','Plane233']):
        paths.update(folder.glob('independent_review.json'))
manifest = {rel(p):{'sha256':fh(p),'size':p.stat().st_size} for p in sorted(paths)}
write('read_only_before.json', {'at':now(),'scope':'Exact reviewed source/evidence/dependencies, not unrelated concurrent workspace files','files':manifest})
write('isolation.json', {'at':now(),'pid':os.getpid(),'python':sys.version,'own_guard_before_project_import':True,
    'cache_environment':{k:os.environ[k] for k in ['TEMP','TMP','TMPDIR','MPLCONFIGDIR','XDG_CACHE_HOME']},
    'runtime_isolation':ISOLATION,'network_and_subprocess_blocked':True,'no_background_processes_started':True})
print(json.dumps({'baseline_files':len(manifest),'own':str(OWN),'pid':os.getpid()}, ensure_ascii=False))
