from bootstrap import *
import subprocess
import shutil
from dataset_tools.catalog import content,digest

qid=sys.argv[1];assert qid in ('Solid206','Solid207')
q=next(q for q in read(BASE/'background_63_assignment.json')['questions'] if q['question_id']==qid)
d=HERE/qid/q['variant_id']
assert not (d/'tests').exists() and not (d/'process_launch.json').exists()
assert not list(HERE.rglob('*incomplete_response.bin'))
for summary in HERE.glob('Solid*/*/tests/*/summary.json'):
    assert read(summary)['two_completed'],'Previous API error/incomplete prevents any following calls'
record=next(r for r in rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']==qid)
approval=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
current=digest(content(PROJECT,'SolidGeometry',record))
assert current==approval['content_sha256']==read(HERE/qid/'fresh_eligibility_and_approval.json')['current_content_sha256']
for name,expected in q['frozen_files_sha256'].items(): assert sha(d/name)==expected==sha(Path(q['source_directory'])/name)
assert read(HERE/'zero_prior_invocation_qualified.json')['zero_visible_exact_prior_invocations']
assert read(HERE/qid/'fresh_schema_native_replay.json')['fresh_replay_exactly_equals_frozen']
for index in ('accepted_index.jsonl','collected_index.jsonl'):
    assert not any(r.get('question_id',r.get('id'))==qid for r in rows(PROJECT/'SolidGeometry/special_variant'/index))
assert not (PROJECT/'SolidGeometry/special_variant'/qid).exists()
write(d/'eligibility_at_launch.json',{'checked_at':now(),'current_original_content_sha256':current,'eligible':True,'all_frozen_bytes_exact':True})
harness=HERE/'harness/quicktest3_isolated.py'
if not harness.exists():
    harness.parent.mkdir()
    shutil.copyfile(BASE/'background_55/harness/quicktest3_isolated.py',harness)
    write(HERE/'harness_routing_audit.json',dict(source=str(BASE/'harness/quicktest3_isolated.py'),source_sha256=sha(BASE/'harness/quicktest3_isolated.py'),existing_routed_source=str(BASE/'background_55/harness/quicktest3_isolated.py'),own_routed_sha256=sha(harness),byte_identical_to_existing_routed_harness=True,routing_only='Identical existing55 harness; project depth and bootstrap import resolve to own63. No API/profile/system/model/thinking/credentials/token/timeout changes.',existing_routing_audit=read(BASE/'background_55/harness_routing_audit.json')))
assert sha(harness)==sha(BASE/'background_55/harness/quicktest3_isolated.py')
cmd=[sys.executable,'-X','utf8','-B',str(harness),'--branch','SolidGeometry','--question',qid,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
with (d/'api_stdout.log').open('x',encoding='utf-8') as out,(d/'api_stderr.log').open('x',encoding='utf-8') as err:
    p=subprocess.Popen(cmd,cwd=PROJECT,env=os.environ.copy(),stdout=out,stderr=err)
    write(d/'process_launch.json',dict(started_at=now(),pid=p.pid,parent_pid=os.getpid(),command=cmd,process_environment={k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},no_timeout_or_remote_profile_override=True))
    print(qid,'owned API pid',p.pid,flush=True)
    result=p.wait()
write(d/'process_completed.json',dict(finished_at=now(),pid=p.pid,returncode=result,process_closed=True))
summaries=list((d/'tests').glob('*/summary.json'))
assert len(summaries)==1
s=read(summaries[0]);print(qid,'two_completed',s['two_completed'],'evidence',str(summaries[0]),flush=True)
if not s['two_completed']: sys.exit(2)
