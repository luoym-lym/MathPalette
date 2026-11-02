import research_core as core
rt=core.rt
import sys,os,runpy,json,hashlib
from pathlib import Path

d=Path(sys.argv[1]).resolve();rt.check_write(d)
design=rt.read(d/'design.json');qid=design['question_id']
assert rt.read(d/'render_gates.json')['new_independent_process_exact_replay'] is True
assert rt.read(d/'visual_primary_before_calls.json')['human_gate_passed'] is True
assert not list((d/'tests').glob('quicktest3_*')),'No resumption/retry or third call permitted'
pid=os.getpid();count=0
start={'pid':pid,'question_id':qid,'candidate_directory':str(d),'started_at':rt.now(),
    'command':[sys.executable,'-X','utf8','-B',str(Path(__file__).resolve()),str(d)],
    'source_harness':str(rt.OLD/'harness/quicktest3_isolated.py'),'runs':2,'writeguard':str(rt.OWN)}
rt.save(d/'process_launch.json',start)
initial={n:rt.sha(d/n) for n in ('candidate.png','plugin.json','design.json','context.json')}
def before_request(event,args):
    global count
    if event!='urllib.Request':return
    count+=1
    assert count<=2
    # The reference harness resets these to its local directory at import time.
    # Keep actual library caches in the unit's ownruntime tree before every call.
    for name,sub in (('TEMP','temp'),('TMP','temp'),('MPLCONFIGDIR','mpl'),('XDG_CACHE_HOME','cache')):
        os.environ[name]=str(rt.OWN/'ownruntime'/sub)
    e=core.eligibility(qid)
    rt.save(d/f'eligibility_before_actual_request_{count:02d}.json',e)
    assert e['eligible'],e['reasons']
    assert initial=={n:rt.sha(d/n) for n in initial},'Frozen candidate changed'
    rt.save(d/f'actual_request_{count:02d}_audit.json',{'pid':pid,'at':rt.now(),'url':args[0],
        'request_body_sha256':hashlib.sha256(args[1]).hexdigest(),'frozen':initial,
        'eligibility_passed':True,'no_payload_edits':True,
        'runtime_environment':{n:os.environ[n] for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')}})
sys.addaudithook(before_request)
sys.argv=['quicktest3_isolated.py','--branch','PlaneGeometry','--question',qid,'--image',str(d/'candidate.png'),
    '--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
exit_code=0
try:
    runpy.run_path(str(rt.OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
except BaseException as error:
    exit_code=1
    rt.save(d/'launcher_error.json',{'type':type(error).__name__,'message':str(error),'at':rt.now(),'request_count':count})
    raise
finally:
    rt.save(d/'process_completed.json',{'pid':pid,'finished_at':rt.now(),'actual_urllib_request_count':count,'exit_code':exit_code,
        'frozen_inputs_unchanged':initial=={n:rt.sha(d/n) for n in initial},'local_figures_closed':True})
