from bootstrap import HERE
from audit import read, save, sha, eligibility, now
import hashlib
import json
import os
from pathlib import Path
import runpy
import sys

def arg(flag): return sys.argv[sys.argv.index(flag)+1]
q=arg('--question')
image=Path(arg('--image')).resolve()
design=Path(arg('--design')).resolve()
output=Path(arg('--output')).resolve()
assert arg('--runs')=='2'
assert image.is_relative_to(HERE) and design.parent==image.parent and output.parent==image.parent
assert not output.exists() or not list(output.rglob('*started*')), 'Never retry a previously started frozen image'
reuse=read(image.parent/'reuse_provenance.json')
assert reuse['question_id']==q
for item in reuse['copies']:
    assert sha(item['original_path'])==item['original_sha256']
    assert sha(item['copied_path'])==item['copied_sha256']
eligibility(q,'before_api')
launch={'question_id':q,'pid':os.getpid(),'parent_pid':os.getppid(),'started_at_utc':now(),'command_argv':sys.argv,'image_path':str(image),'image_sha256':sha(image),'design_sha256':sha(design),'original_harness_relocated_only_PROJECT':True,'environment':{key:os.environ[key] for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},'strict_OWNROOT_writeguard_active':True,'exactly_two_requested_calls':True,'retry_allowed':False}
save(image.parent/'api_process_started.json',launch)
transport_count=0
def transport_gate(event,args):
    global transport_count
    if event!='urllib.Request': return
    # Inspect no headers or credentials. This read-only gate does not mutate the
    # existing harness request, provider settings, transport or timeout.
    transport_count+=1
    assert transport_count<=2
    eligibility(q,'before_actual_call_'+str(transport_count))
    payload=json.loads(args[1])
    frozen=list(output.glob('quicktest3_*/binding.json'))
    assert len(frozen)==1
    binding=read(frozen[0])
    assert hashlib.sha256(args[1]).hexdigest()==binding['request_body_sha256']
    assert payload['model']==binding['settings']['model']=='mimo-v2.6-flash'
    assert payload['thinking']=={'type':'disabled'}
    assert payload['messages'][0]=={'role':'system','content':binding['system_prompt']}
    assert payload['messages'][1]['content'][0]=={'type':'text','text':binding['question']}
    save(image.parent/('transport_gate_'+str(transport_count)+'.json'),{'question_id':q,'transport_index':transport_count,'checked_at_utc':now(),'pid':os.getpid(),'original_approval_and_source_hashes_current':True,'exact_harness_request_body_sha256':binding['request_body_sha256'],'request_or_headers_mutated':False,'credentials_inspected_or_logged':False})
sys.addaudithook(transport_gate)
failure=None
try:
    runpy.run_path(str(HERE/'harness/quicktest3_isolated.py'),run_name='__main__')
except BaseException as error:
    failure=type(error).__name__
    raise
finally:
    save(image.parent/'api_process_finished.json',{'question_id':q,'pid':os.getpid(),'finished_at_utc':now(),'exception_type':failure,'transport_gates_passed':transport_count,'harness_returned':failure is None,'process_exit_follows':True})
