from bootstrap import *
import subprocess
argv=[sys.executable,'-X','utf8','-B',str(OWN/'run_pair.py')]
with (OWN/'pair.stdout.txt').open('x',encoding='utf-8') as out,(OWN/'pair.stderr.txt').open('x',encoding='utf-8') as err:
 process=subprocess.Popen(argv,cwd=ROOT,stdout=out,stderr=err)
 save(OWN/'pair_process.json',{'at_utc':now(),'pid':process.pid,'argv':argv,'cwd':str(ROOT)})
 code=process.wait();save(OWN/'pair_reaped.json',{'at_utc':now(),'pid':process.pid,'returncode':code,'reaped':True})
 print(json.dumps({'pid':process.pid,'returncode':code}))
