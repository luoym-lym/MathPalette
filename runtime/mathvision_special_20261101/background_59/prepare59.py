from env59 import *
import gc
from dataset_tools import catalog

RELATED=['Solid185']
protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
refs=['annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json','selection58_59_parent_eligibility.json','preparation58_59.json','background_59_brief.txt','background_59_assignment.json']
sources=set(protocols+['dataset_tools/catalog.py','dataset_tools/geometry_dataset.py','dataset_tools/mathvision_workbench.py','SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/renderer_adapter.py','SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/workbench_io.py','SolidGeometry/workbench/quick_test.py','SolidGeometry/workbench/config.json','provenance/source_notes.json','provenance/approvals.json','SolidGeometry/dataset.jsonl','SolidGeometry/special_variant/accepted_index.jsonl','SolidGeometry/special_variant/collected_index.jsonl'])
sources.update('runtime/mathvision_special_20261101/'+n for n in refs+['runtime_isolation.py','delivery_bridge_adapter.py','harness/quicktest3_isolated.py'])
history={q:[] for q in QIDS+RELATED}
for p in BASE.rglob('*'):
    if not p.is_file() or p.is_relative_to(OWN): continue
    for q in history:
        if q in p.parts or p.name.startswith(q+'_'):
            history[q].append(str(p.relative_to(PROJECT)))
            sources.add(str(p.relative_to(PROJECT)))
for q in QIDS+RELATED:
    rec=next(r for r in catalog.rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']==q)
    sources.update('SolidGeometry/'+rec[k] for k in catalog.PATH_FIELDS if rec.get(k))
    sources.update('SolidGeometry/'+p for p in rec['runtime_dependencies'])
for p in BASE.glob('batch_*'):
    for f in ([p] if p.is_file() else p.rglob('*')):
        if f.is_file(): sources.add(str(f.relative_to(PROJECT)))
for folder in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly','Plane263_v01','Plane192_v03','Solid220_false_face_pair']:
    for f in (BASE/'independent_review'/folder).rglob('*'):
        if f.is_file(): sources.add(str(f.relative_to(PROJECT)))
save('old_history_manifest.json',history)
hashes={}
for rel in sorted(sources):
    p=PROJECT/rel
    if p.is_file(): hashes[rel]=sha(p)
save('readonly_hashes_start.json',hashes)
save('protocol_read_log.json',{'complete_protocols':{p:hashes[p] for p in protocols},'complete_brief_assignment_continuation_snapshots':'readin_snapshots/','at':now()})
save('isolation.json',{'at':now(),'strict_write_guard_before_project_imports':True,'env':{k:os.environ[k] for k in ('TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},'ownroot':str(OWN)})
for q in QIDS:
    e=eligibility(q)
    save(f'{q}/eligibility_start.json',e)
    save(f'{q}/formal_record.json',e['formal_record'])
    print(q,'original approval',e['approval_matches'],'eligible',e['eligible'],flush=True)
    del e
save('preparation_stage.json',{'at':now(),'old_files':sum(map(len,history.values())),'readonly_files':len(hashes),'no_API_calls':True})
isolation=install_render()
save('render_isolation.json',isolation)
from delivery_bridge_adapter import RendererAdapter
from workbench_io import load_config,pixel_hash
from dataset_tools.mathvision_workbench import png_bytes
adapter=RendererAdapter(load_config())
for q in QIDS:
    context=adapter.inspect_question(q)
    save(f'{q}/context.json',context)
    capture=adapter.scene(q)
    try: png=png_bytes(capture)
    finally: capture.close()
    (OWN/q/'no_op.png').write_bytes(png)
    assert pixel_hash(png)==context['original_pixel_sha256']
    save(f'{q}/baseline.json',{'native_noop_matches_formal_pixels':True,'native_noop_sha256':sha(OWN/q/'no_op.png'),'formal_png_sha256':sha(PROJECT/'SolidGeometry/image'/f'{q}.png'),'context_sha256':sha(OWN/q/'context.json')})
    print(q,'fresh native context and no-op PASS',len(context['objects']),'objects',flush=True)
    del context,png,capture
    gc.collect()
