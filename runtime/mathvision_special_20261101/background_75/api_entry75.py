"""Strict own-root entry for the original isolated harness; no payload overrides."""
import bootstrap75 as boot
from research75 import read,put,now,sha,eligible
from pathlib import Path
import sys
import os
import runpy

def main():
    args=sys.argv[1:]
    def arg(name):return args[args.index(name)+1]
    q=arg('--question');target=Path(arg('--design')).resolve().parent
    assert target.is_relative_to(boot.OWN) and arg('--runs')=='2'
    if (boot.OWN/'remote_error_stop.json').exists() or (boot.OWN/'stop_after_external_stall.json').exists():raise RuntimeError('A preceding remote error/stall prohibits subsequent calls')
    if (target/'api_process_started.json').exists():raise RuntimeError('This frozen image was already started; no retry')
    primary=read(target/'primary_review.json');replay=read(target/'offline_replay_audit.json');design=read(target/'design.json')
    assert primary['actual_candidate_native_PNG_viewed'] and primary['proceed_to_two_calls']
    assert replay['byte_identical']
    assert sha(Path(arg('--image')).read_bytes())==design['image_sha256']==primary['image_sha256']==replay['sha256']
    e=eligible(q);put(target/'eligibility_immediately_before_calls.json',e)
    if not e['eligible']:raise RuntimeError('Current original eligibility failed')
    for f,key in [('plugin.json','plugin_sha256'),('math_proof_snapshot.json','math_proof_sha256'),('design_difference_audit.json','difference_audit_sha256')]:
        if sha((target/f).read_bytes())!=design[key]:raise RuntimeError('Frozen '+f+' changed')
    origargv=sys.orig_argv[:]
    put(target/'api_process_started.json',{'pid':os.getpid(),'process_command_argv':origargv,'started_at':now(),'question_id':q,'entry':str(Path(__file__).resolve()),'harness':str(boot.OWN/'harness/quicktest3_isolated.py'),'request_count_before_start':0,'all_output_inside':str(boot.OWN)})
    status='error'
    try:
        sys.argv=[str(boot.OWN/'harness/quicktest3_isolated.py')]+args
        runpy.run_path(str(boot.OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
        summaries=list(Path(arg('--output')).glob('quicktest3_*/summary.json'))
        if len(summaries)!=1:raise RuntimeError('Unexpected invocation count; preserve without retry')
        result=read(summaries[0])
        if not result['two_completed']:
            put(boot.OWN/'remote_error_stop.json',{'question_id':q,'stopped_at':now(),'summary':str(summaries[0]),'results':result['results'],'no_retry':True})
            status='remote_error_stop';return 5
        status='two_completed';return 0
    finally:
        put(target/'api_process_finished.json',{'pid':os.getpid(),'process_command_argv':origargv,'finished_at':now(),'status':status,'wrapper_main_finished':True,'no_spawned_API_children':True})

if __name__=='__main__':sys.exit(main())

