from env70 import *
from design70 import NAMES,directory
import runpy
import traceback

qid=sys.argv[sys.argv.index('--question')+1]
assert qid in NAMES and sys.argv[sys.argv.index('--runs')+1]=='2'
d=directory(qid)
assert not (OWN/'external_failure_stop.json').exists()
assert not list(OWN.glob('local_failure_*.json'))
assert not list((d/'tests').glob('**/run_*_started.json'))
e=eligibility(qid);assert e['eligible']
save(d/'eligibility_immediately_before_calls.json',e)
frozen=read(OWN/'readonly_hashes_start.json')
changed=[{'path':p,'old':h,'current':sha(PROJECT/p)} for p,h in frozen.items() if sha(PROJECT/p)!=h]
save(d/'frozen_readonly_pre_call_check.json',{'checked_at':now(),'files':len(frozen),'changes':changed})
assert not changed
design=read(d/'design.json')
assert sha(d/'candidate.png')==design['image_sha256']
assert sha(d/'plugin.json')==design['plugin_sha256']
assert sha(d/'design_difference_audit.json')==design['design_difference_audit_sha256']
assert read(d/'primary_review.json')['proceed_to_API']
assert read(d/'offline_replay_check.json')['exact_byte_replay']
zero=read(OWN/'global_new_PNG_zero_call_audit.json')
assert zero['zero_exact_old_PNG_requests_and_files'] and zero['new_frozen_PNG_hashes'][qid]==design['image_sha256']
for path,digest in read(OWN/'source58_all_files_start.json').items():assert sha(PROJECT/path)==digest
save(d/'api_process.json',{'created_at':now(),'pid':os.getpid(),'executable':sys.executable,
      'argv':sys.argv,'python_flags':'-X utf8 -B','own_root':str(OWN),
      'profile_changes':False,'requests_before_launch':0})
before=set((d/'tests').glob('quicktest3_*'))
try:
    runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
    after=set((d/'tests').glob('quicktest3_*'))-before
    assert len(after)==1
    result=read(next(iter(after))/'summary.json')
    if not result['two_completed']:
        save('external_failure_stop.json',{'at':now(),'question_id':qid,'evidence_dir':result['evidence_dir'],
              'results':result['results'],'stop_subsequent_calls':True,'no_retry':True})
finally:
    save(d/'api_process_finished.json',{'finished_at':now(),'pid':os.getpid(),'wrapper_finally_reached':True,
          'no_background_API_children_started':True})
