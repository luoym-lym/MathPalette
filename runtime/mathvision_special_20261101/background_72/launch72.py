from bootstrap72 import *
from tools72 import read,write,sha,eligibility,now,IDS,BRANCH
import runpy

q=sys.argv[sys.argv.index('--question')+1]
assert q in ('Plane335','Plane355')
if (HERE/'external_failure_stop.json').exists() or (HERE/'local_failure_stop.json').exists():
    raise RuntimeError('A prior real failure requires checkpoint; no subsequent calls.')
image=Path(sys.argv[sys.argv.index('--image')+1]).resolve()
design=Path(sys.argv[sys.argv.index('--design')+1]).resolve()
d=design.parent
assert image==d/'candidate.png' and d.is_relative_to(HERE/q)
assert sys.argv[sys.argv.index('--runs')+1]=='2'
assert not list((d/'tests').glob('quicktest3_*'))
assert read(d/'primary_visual_review.json')['proceed_to_API']
assert read(d/'offline_replay_check.json')['replay_bytes_equal']
assert sha(image)==read(design)['candidate_sha256']==sha(d/'repeat.png')==sha(d/'offline_replay.png')
assert read(d/'wrong_preset.json')['expected_wrong_answer']==read(design)['expected_wrong_answer']
assert sha(d/'wrong_preset.json')==read(design)['wrong_preset_sha256']
assert sha(d/'design_difference_audit.json')==read(design)['design_difference_audit_sha256']
current=eligibility(q);write(d/'eligibility_immediately_before_calls.json',current)
assert current['eligible'] and current['approval_matches_current']
initial=read(HERE/q/'source_hashes_initial.json')
changed=[p for p,h in initial.items() if not (PROJECT/p).is_file() or sha(PROJECT/p)!=h]
assert not changed,changed
write(d/'source_hashes_immediately_before_calls.json',{'all_initial_frozen_hashes_exact':True,'source_hashes':initial,'approval_fingerprint':current['current_content_sha256']})
write(d/'api_process.json',{'pid':os.getpid(),'parent_pid':os.getppid(),'started_at':now(),'argv':sys.argv,'executable':sys.executable,'harness':str(HERE/'harness/quicktest3_isolated.py'),'runs':2,'no_model_profile_timeout_token_override':True,'strict_own_root_write_guard':True})
started=now();status='unknown'
try:
    sys.argv[0]=str(HERE/'harness/quicktest3_isolated.py')
    runpy.run_path(sys.argv[0],run_name='__main__')
    summaries=list((d/'tests').glob('*/summary.json'));assert len(summaries)==1
    result=read(summaries[0])
    if not result['two_completed']:
        status='external_failure_stop'
        write(HERE/'external_failure_stop.json',{'question_id':q,'at':now(),'summary':str(summaries[0]),'no_retry':True,'subsequent_calls_forbidden':True})
    else:status='two_completed'
except BaseException as err:
    status='local_failure_stop'
    write(HERE/'local_failure_stop.json',{'question_id':q,'at':now(),'error_type':type(err).__name__,'error':str(err),'no_retry':True,'subsequent_calls_forbidden':True})
    raise
finally:
    write(d/'api_process_finished.json',{'pid':os.getpid(),'started_at':started,'finished_at':now(),'status':status,'normal_process_exit_pending':True,'no_retry':True})
