from tools45 import *
import types
q=sys.argv[1];assert q in IDS
folders=([TASK/q/sys.argv[2]] if len(sys.argv)>2 else [p.parent for p in (TASK/q).glob('*/design.json')]);assert len(folders)==1
folder=folders[0];assert not (folder/'process_launch.json').exists(),'No repeat invocation'
freeze=read(folder/'pretest_freeze.json');assert freeze['all_pretest_gates_pass']
if q=='Solid97':assert read(folder/'pip_pixel_preservation.json')['all16_native_pip_regions_identical']
for n,h in freeze['files'].items():assert file_hash(folder/n)==h,(n,'changed since freeze')
e=eligibility(q);assert e['eligible'];write(folder/'eligibility_immediately_before_calls.json',e)
write(folder/'process_launch.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'cwd':str(Path.cwd()),'runs':2})
source=SHARED/'harness/quicktest3_isolated.py'
module=types.ModuleType('isolated_harness45');module.__file__=str(TASK/'quicktest3_isolated.py')
exec(compile(source.read_bytes(),str(source),'exec'),module.__dict__)
assert module.PROJECT==ROOT and module.HARNESS==TASK
write(folder/'harness_isolation.json',{'source':str(source),'source_sha256':file_hash(source),'source_bytes_modified':False,'virtual_module_file':module.__file__,'project':str(module.PROJECT),'cache_root':str(module.HARNESS),'own_guard_installed_before_project_import':True,'profile_max_tokens_timeout_overrides':False,'retries':0})
try:
    result=module.run_tests('SolidGeometry',q,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
    write(folder/'process_completed.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
except Exception as ex:
    write(folder/'process_failed.json',{'pid':os.getpid(),'finished_at':now(),'exception_type':type(ex).__name__,'no_retry':True})
    raise
