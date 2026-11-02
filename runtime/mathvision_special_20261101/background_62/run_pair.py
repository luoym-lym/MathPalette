from bootstrap import install,OWN,PROJECT,SESSION
install()
from gates import sha,load,save,now,eligibility
import sys,os,subprocess,json,traceback
from pathlib import Path

q=sys.argv[1]
assert q in ('Plane482','Plane488')
assert not (OWN/'STOP_SUBSEQUENT_CALLS.json').exists()
try:
    item=next(i for i in load(SESSION/'background_62_assignment.json')['questions'] if i['question_id']==q)
    d=OWN/q/item['variant_id']
    assert not (d/'api_process.json').exists(),'A first pair was already launched; no retry.'
    e=eligibility(q,'qualification_immediately_before_API.json');assert e['eligible']
    provenance=load(d/'reuse_provenance.json')
    for r in provenance['all_copy_equality']:
        assert sha(r['source'])==r['sha256']==sha(r['copy'])
    assert load(OWN/q/'fresh_validation/fresh_primary_review.json')['passes_fresh_primary_gates']
    assert load(OWN/'zero_prior_invocation_scan.json')['zero_old_call_gate_pass']
    assert load(OWN/'zero_call_duplicate_path_scan.json')['passed']
    cmd=[sys.executable,'-X','utf8','-B',str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',q,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
    env=os.environ.copy()
    for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):env[k]='1'
    before=now()
    with (d/'API_stdout.log').open('wb') as out:
        proc=subprocess.Popen(cmd,cwd=PROJECT,env=env,stdout=out,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0)
        save(d/'api_process.json',{'pid':proc.pid,'command_argv':cmd,'expected_command_line':subprocess.list2cmdline(cmd),'started_at_utc':before,'question_id':q,'first_pair_only':True,'requested_runs':2,'own_root':str(OWN),'local_env':{k:env[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')}})
        print(json.dumps({'launched_question':q,'pid':proc.pid,'command':subprocess.list2cmdline(cmd)}),flush=True)
        code=proc.wait()
    save(d/'api_process_finished.json',{'pid':proc.pid,'expected_command_line':subprocess.list2cmdline(cmd),'exit_code':code,'finished_at_utc':now(),'process_wait_returned':True,'no_termination_or_retry':True})
    summaries=list((d/'tests').glob('*/summary.json')) if (d/'tests').exists() else []
    if code or len(summaries)!=1 or not load(summaries[0])['two_completed']:
        save(OWN/'STOP_SUBSEQUENT_CALLS.json',{'at':now(),'question_id':q,'exit_code':code,'reason':'API pair incomplete or process failure; no subsequent API calls permitted','stdout_log':str(d/'API_stdout.log'),'summaries':[str(x) for x in summaries]})
    print((d/'API_stdout.log').read_text(encoding='utf-8'),flush=True)
except BaseException as e:
    save(OWN/'STOP_SUBSEQUENT_CALLS.json',{'at':now(),'question_id':q,'type':type(e).__name__,'reason':str(e),'traceback':traceback.format_exc(),'subsequent_calls_stopped':True})
    raise
