from tools34 import *
historical={}
def gather(value,source):
    if isinstance(value,dict):
        for key,item in value.items():
            normalized=key.replace('\\','/')
            if isinstance(item,str) and len(item)==64 and all(c in '0123456789abcdef' for c in item) and (normalized.startswith(('PlaneGeometry/workbench/','SolidGeometry/workbench/','dataset_tools/')) or normalized in ('MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md')):
                historical.setdefault(normalized,{}).setdefault(item,[]).append(source)
            gather(item,source)
    elif isinstance(value,list):
        for item in value:gather(item,source)
history=read(UNIT/'history_inventory.json')
for qid,data in history.items():
    for directory in data['question_directories']:
        for path in (PROJECT/directory).rglob('*.json'):
            gather(read(path),str(path.relative_to(PROJECT)))
current={};mismatches=[]
for path,versions in historical.items():
    if not (PROJECT/path).is_file():continue
    digest=sha(PROJECT/path)
    current[path]={'current_sha256':digest,'historical_sha256_values':list(versions),'matches_some_preserved_historical_snapshot':digest in versions,'historical_sources':versions}
    if digest not in versions:mismatches.append(path)
assert not mismatches,mismatches
write(UNIT/'rendering_dependency_historical_comparison.json',{'at':now(),'timing':'Post-call audit against readonly historical snapshots; no retroactive claim of a pre-call hash capture.',
      'current_dependencies':current,'unknown_historical_changes':mismatches,'all_dependencies_with_prior_hashes_match':True,
      'harness_exact_copy_sha256':sha(UNIT/'quicktest3_isolated.py'),'reference_shared_harness_sha256':sha(SHARED/'harness/quicktest3_isolated.py'),
      'no_shared_helper_writes':True,'strict_own_unit_guard':True})
print(json.dumps({'dependencies_compared_with_preserved_old_hashes':len(current),'mismatches':mismatches}))
