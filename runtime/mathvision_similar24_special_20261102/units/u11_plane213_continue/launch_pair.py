from bootstrap import *
import subprocess
vid=sys.argv[1];d=OWN/'Plane213'/vid
argv=[sys.executable,'-X','utf8','-B',str(OWN/'run_pair.py'),vid]
with (d/'pair.stdout.txt').open('x',encoding='utf-8') as out,(d/'pair.stderr.txt').open('x',encoding='utf-8') as err:
    process=subprocess.Popen(argv,cwd=ROOT,stdout=out,stderr=err)
    save(d/'pair_process.json',{'at_utc':now(),'pid':process.pid,'launcher_pid':os.getpid(),'argv':argv,'cwd':str(ROOT)})
    code=process.wait()
    save(d/'pair_reaped.json',{'at_utc':now(),'pid':process.pid,'returncode':code,'reaped':True})
    print(json.dumps({'variant_id':vid,'pid':process.pid,'returncode':code}))
