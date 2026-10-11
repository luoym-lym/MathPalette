from pathlib import Path
import json,subprocess,sys,hashlib,os
P=Path(__file__).resolve().parent
rows=json.loads((P/'manifest.json').read_text())
env=os.environ.copy();env.setdefault('MPLCONFIGDIR',str(P/'.matplotlib_cache'));env.setdefault('OPENBLAS_NUM_THREADS','1')
failed=[]
for r in rows:
 if not r['output_image']:continue
 result=subprocess.run([sys.executable,str(P/r['reproduction_script'])],cwd=P,env=env,capture_output=True,text=True)
 actual=hashlib.sha256((P/r['output_image']).read_bytes()).hexdigest()
 ok=result.returncode==0 and actual==r['output_sha256']
 print(r['pid'],'PASS' if ok else 'FAIL',flush=True)
 if not ok:failed.append({'pid':r['pid'],'exit':result.returncode,'stderr':result.stderr,'hash':actual})
(P/'reproduction_result.json').write_text(json.dumps({'failed':failed,'checked':sum(bool(r['output_image']) for r in rows)},indent=2))
if failed:sys.exit(1)
