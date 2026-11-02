from bootstrap import *
import subprocess
for q in ['Solid186','Solid226']:
 argv=[sys.executable,'-X','utf8','-B',str(OWN/'run_pair.py'),q]
 with (OWN/(q+'.stdout.txt')).open('x',encoding='utf-8') as out,(OWN/(q+'.stderr.txt')).open('x',encoding='utf-8') as err:
  p=subprocess.Popen(argv,cwd=ROOT,stdout=out,stderr=err)
 save(OWN/(q+'_process.json'),{'at_utc':now(),'pid':p.pid,'argv':argv})
 code=p.wait();save(OWN/(q+'_process_reaped.json'),{'at_utc':now(),'pid':p.pid,'returncode':code,'reaped':True});print(q,code,flush=True)
 entry=next(e for e in read(OWN/'first_pair_candidates.json') if e['question_id']==q)
 summaries=list((Path(entry['candidate_directory'])/'tests').glob('*/summary.json'))
 if code!=0 or len(summaries)!=1 or not read(summaries[0])['two_completed']:
  save('execution_stop.json',{'at_utc':now(),'question_id':q,'returncode':code,'remaining_calls_not_launched':True,'no_API_retry':True})
  break
