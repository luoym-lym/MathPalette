from bootstrap import *
import json,subprocess
from datetime import datetime,timezone
cmd=[sys.executable,'-X','utf8','-B',str(HERE/'run_pair77.py')]
with (HERE/'api_stdout.log').open('xb') as out,(HERE/'api_stderr.log').open('xb') as err:
    proc=subprocess.Popen(cmd,cwd=str(PROJECT),stdout=out,stderr=err)
    with (HERE/'process_launch.json').open('x',encoding='utf-8') as f:json.dump({'started_at':datetime.now(timezone.utc).isoformat(),'pid':proc.pid,'command':cmd,'requested_runs':2,'no_timeout_profile_override_retry':True},f,ensure_ascii=False,indent=2)
    code=proc.wait()
    with (HERE/'process_finished.json').open('x',encoding='utf-8') as f:json.dump({'finished_at':datetime.now(timezone.utc).isoformat(),'pid':proc.pid,'returncode':code,'process_wait_returned':True,'actual_termination':False,'retry':False},f,ensure_ascii=False,indent=2)
print(json.dumps({'pid':proc.pid,'returncode':code,'closed':True}))
raise SystemExit(code)
