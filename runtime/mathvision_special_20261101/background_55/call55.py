from tools55 import *
import subprocess

qid=sys.argv[1];assert qid in ['Solid195','Solid206','Solid207']
spec=read(HERE/qid/'spec_r55.json');d=HERE/qid/spec['name']
assert not (d/'process_launch.json').exists(),'Never repeat this frozen candidate call.'
e=eligibility(qid);assert e['eligible'];write(d/'eligibility_at_launch.json',e)
image=d/'candidate.png';design=d/'design.json';frozen=read(design)
assert sha(image)==frozen['png_sha256']
assert (d/'primary_visual_marker_review.json').is_file()
cmd=[sys.executable,'-X','utf8','-B',str(HERE/'harness/quicktest3_isolated.py'),'--branch',BRANCH,'--question',qid,'--image',str(image),'--design',str(design),'--output',str(d/'tests'),'--runs','2']
with (d/'api_stdout.log').open('xb') as out,(d/'api_stderr.log').open('xb') as err:
 p=subprocess.Popen(cmd,cwd=PROJECT,stdout=out,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 write(d/'process_launch.json',dict(pid=p.pid,parent_pid=os.getpid(),command=cmd,started_at=now(),image_sha256=sha(image),design_sha256=sha(design)))
 print(json.dumps(dict(question_id=qid,pid=p.pid,started=True)),flush=True)
 rc=p.wait()
write(d/'process_completed.json',dict(pid=p.pid,returncode=rc,finished_at=now(),process_closed=True))
print((d/'api_stdout.log').read_text(encoding='utf-8'))
if rc:
 print((d/'api_stderr.log').read_text(encoding='utf-8'));raise SystemExit(rc)
summaries=list((d/'tests').glob('*/summary.json'));assert len(summaries)==1
summary=read(summaries[0]);print(json.dumps(dict(question_id=qid,two_completed=summary['two_completed'],statuses=[r['status'] for r in summary['results']])))
