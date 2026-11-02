"""Run the original isolated harness with only its cache directory redirected."""
from research import *
import traceback

qid,variant=sys.argv[1:]
assert qid in IDS
folder=OWN/qid/variant
if (OWN/'EXTERNAL_FAILURE_STOP.json').exists():
    raise RuntimeError('An external failure already stopped this unit; no further calls permitted')
assert not (folder/'api_process.json').exists(), 'No invocation repeat allowed'
elig=eligibility(qid,folder/'eligibility_immediately_before_calls.json')
assert elig['eligible']
design=read(folder/'design.json')
primary=read(folder/'primary_prescreen.json')
assert design['status']=='FROZEN_BEFORE_BOTH_CALLS' and primary['human_unique_solution_and_semantics_primary_pass']
assert sha(folder/'candidate.png')==design['candidate_png_sha256']==primary['candidate_sha256']
assert sha(folder/'design.json')==primary['design_sha256']
assert elig['formal_input_binding']==read(folder/'render_check.json')['formal_binding_before']
original=SHARED/'harness/quicktest3_isolated.py'
code=original.read_text(encoding='utf-8')
old='HARNESS = Path(__file__).resolve().parent'
assert code.count(old)==1
new='HARNESS = Path('+repr(str(OWN/'harness_cache'))+')'
routed=code.replace(old,new)
dump(folder/'harness_environment_routing.json',{'original_harness_path':str(original),'original_harness_sha256':sha(original),'only_in_memory_change':{'old':old,'new':new},'reason':'Original top-level cache loop unconditionally uses HARNESS; route all TEMP/MPL/cache writes to own root before imports. No API/model/profile/payload/timeout/token/retry logic changed.','routed_source_sha256':hashlib.sha256(routed.encode()).hexdigest(),'own_write_guard':True,'isolation':ISOLATION})
ns={'__file__':str(original),'__name__':'_background53_original_harness'}
exec(compile(routed,str(original),'exec'),ns)
dump(folder/'api_process.json',{'pid':os.getpid(),'parent_pid':os.getppid(),'argv':sys.argv,'started_at':now(),'question_id':qid,'variant_id':variant,'design_sha256':sha(folder/'design.json'),'png_sha256':sha(folder/'candidate.png'),'model_profile_override':False,'runs':2})
try:
    result=ns['run_tests']('SolidGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',2)
    failures=[x for x in result['results'] if x['status']!='completed']
    if failures:
        dump(OWN/'EXTERNAL_FAILURE_STOP.json',{'at':now(),'question_id':qid,'variant_id':variant,'evidence_dir':result['evidence_dir'],'failures':failures,'no_retry':True,'further_calls_forbidden':True})
    dump(folder/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed'],'failures':failures,'no_child_API_process_spawned':True})
    print(json.dumps({'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed'],'external_failure':bool(failures)},ensure_ascii=False),flush=True)
except BaseException as error:
    dump(OWN/'EXTERNAL_FAILURE_STOP.json',{'at':now(),'question_id':qid,'variant_id':variant,'error_type':type(error).__name__,'error':str(error),'traceback':traceback.format_exc(),'no_retry':True,'further_calls_forbidden':True})
    dump(folder/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'exception':type(error).__name__,'no_child_API_process_spawned':True})
    raise
