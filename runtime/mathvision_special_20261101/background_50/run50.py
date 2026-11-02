from env50 import *
from inspect50 import eligibility,BRANCH
from prepare50 import DEFS
from datetime import datetime,timezone
import subprocess
def install_harness():
    p=ROOT/'harness/quicktest3_isolated.py';src=p.read_text(encoding='utf-8')
    old='PROJECT = Path(__file__).resolve().parents[3]'
    assert src.count(old)==1
    prefix='import sys\nfrom pathlib import Path\nsys.path.insert(0, '+repr(str(OWN))+')\nfrom env50 import *\n'
    changed=src.replace('from __future__ import annotations\n','from __future__ import annotations\n'+prefix,1).replace(old,'PROJECT = Path('+repr(str(PROJECT))+')')
    target=OWN/'harness/quicktest3_isolated.py';target.parent.mkdir(exist_ok=True)
    if target.exists():assert target.read_text(encoding='utf-8')==changed
    else:target.write_text(changed,encoding='utf-8')
    dump(OWN/'harness_source_audit.json',{'source':str(p),'source_sha256':sha(p),'own_copy':str(target),'own_copy_sha256':sha(target),'only_changes':['Install strict own-directory bootstrap before imports','Resolve PROJECT to actual original project because copy lives deeper'],'HARNESS_caches':'__file__.parent; own harness directory','run_tests_function_body_unchanged':src.split('def run_tests(',1)[1].split('\ndef main():',1)[0]==changed.split('def run_tests(',1)[1].split('\ndef main():',1)[0],'profile_timeout_tokens_systemprompt_APIconfig_credentials_unchanged':True,'no_ping_no_retries':True})
    return target
def main(q):
    assert q in DEFS and not (OWN/'external_stop.json').exists()
    variant=DEFS[q][0];d=OWN/q/variant
    review=json.loads((d/'primary_native_review.json').read_text(encoding='utf-8'))
    assert review['ready_for_exact_two_calls'] is True
    assert not list((d/'tests').glob('quicktest3_*'))
    e=eligibility(q);assert e['eligible'];dump(d/'eligibility_immediately_before_calls.json',e)
    frozen={n:sha(d/n) for n in ['candidate.png','design.json','plugin.json','path_fingerprints.json','design_difference_audit.json','primary_native_review.json']}
    dump(d/'frozen_before_API.json',{'timestamp':datetime.now(timezone.utc).isoformat(),'hashes':frozen,'expected_wrong_answer':DEFS[q][1],'runs':2,'no_controls':'No prior controls found for these8; no repeat or new original control requested here.'})
    hp=install_harness()
    cmd=[sys.executable,'-X','utf8','-B',str(hp),'--branch','PlaneGeometry','--question',q,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
    with (d/'api_stdout.log').open('xb') as out,(d/'api_stderr.log').open('xb') as err:
        child=subprocess.Popen(cmd,cwd=PROJECT,stdout=out,stderr=err,env=os.environ.copy(),creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        dump(d/'api_process.json',{'pid':child.pid,'parent_pid':os.getpid(),'command':cmd,'started_at':datetime.now(timezone.utc).isoformat(),'own_root':str(OWN)})
        print(json.dumps({'qid':q,'pid':child.pid,'command':cmd}),flush=True)
        code=child.wait()
    changed=[n for n,h in frozen.items() if sha(d/n)!=h]
    assert not changed,changed
    summaries=list((d/'tests').glob('quicktest3_*/summary.json'))
    complete=len(summaries)==1 and json.loads(summaries[0].read_text(encoding='utf-8'))['two_completed']
    finish={'pid':child.pid,'exit_code':code,'finished_at':datetime.now(timezone.utc).isoformat(),'two_completed':bool(complete),'frozen_files_unchanged':not changed,'summary':str(summaries[0]) if summaries else None,'process_reaped':True}
    dump(d/'api_process_finished.json',finish)
    if not complete:dump(OWN/'external_stop.json',{'question_id':q,'detail':finish,'policy':'No further API call or retry. Preserve all errors/partial evidence.'})
    print(json.dumps(finish),flush=True)
if __name__=='__main__':main(sys.argv[1])
