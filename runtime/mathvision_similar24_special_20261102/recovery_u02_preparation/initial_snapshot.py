from bootstrap import *
report=read(SOURCE/'unit_report.json');drafts=report['unfinished_native_drafts'];assert len(drafts)==2
hashes={str(p):sha(p) for p in SOURCE.rglob('*') if p.is_file()}
for q in ['Plane218','Plane398']:
 e=eligibility(q);save(q+'/eligibility_initial.json',e)
 for p,h in e['source_file_sha256'].items():hashes[str(ROOT/p)]=h
for relative in ['MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/mathvision_adapter.py','PlaneGeometry/workbench/mathvision_plugins.py','PlaneGeometry/workbench/partial_style.py','PlaneGeometry/workbench/workbench_io.py','PlaneGeometry/workbench/renderer_adapter.py','dataset_tools/catalog.py','dataset_tools/mathvision_workbench.py','provenance/approvals.json','runtime/mathvision_special_20261101/runtime_isolation.py','runtime/mathvision_special_20261101/validate_candidate_replay.py']:
 hashes[str(ROOT/relative)]=sha(ROOT/relative)
for p in (TASK/'references/Plane233').rglob('*'):
 if p.is_file():hashes[str(p)]=sha(p)
save('source_sha256_initial.json',hashes)
save('identified_drafts.json',drafts)
save('initial_gate.json',{'at_utc':now(),'scoped_old_file_count':len(hashes),'drafts':[{k:d[k] for k in ['question_id','variant_id','candidate_directory','wrong_preset','image_sha256','plugin_sha256','design_sha256']} for d in drafts],'no_API_calls':True,'formal_writes':0})
print(json.dumps({'scoped_files':len(hashes),'drafts':[d['question_id']+'/'+d['variant_id'] for d in drafts]}))
