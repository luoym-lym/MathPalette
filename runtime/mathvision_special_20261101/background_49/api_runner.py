import research_env as env
import os,sys,json,runpy,traceback
from inspect_sources import save,sha,now,eligibility

q=sys.argv[1]
d=next((env.ROOT/q).glob('r49_*'))
assert (d/'primary_review.json').is_file()
assert not (d/'tests').exists(),'Never rerun a candidate, including failed/incomplete calls.'
assert not list(env.ROOT.glob('**/external_failure_stop.json')),'External failure is terminal for this work unit.'
e=eligibility(q);save(d/'eligibility_immediately_before_calls.json',e);assert e['eligible']
design=json.loads((d/'design.json').read_text(encoding='utf-8'))
assert sha(d/'candidate.png')==design['candidate_png_sha256'] and sha(d/'plugin.json')==design['plugin_sha256']
review=json.loads((d/'primary_review.json').read_text(encoding='utf-8'))
assert review['proceed_to_exact_two_calls'] and sha(d/'design.json')==review['design_sha256']
argv=[str(env.ROOT/'harness/quicktest3_isolated.py'),'--branch','SolidGeometry','--question',q,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
save(d/'api_process.json',{'pid':os.getpid(),'started_at_utc':now(),'python_executable':sys.executable,'runner_argv':sys.argv[:],'harness_argv':argv,'isolation':env.ISOLATION,'strict_own_root_write_guard':True})
print(json.dumps({'question_id':q,'own_pid':os.getpid(),'harness':argv[0]}),flush=True)
sys.argv=argv
try:
 runpy.run_path(argv[0],run_name='__main__')
 summaries=list((d/'tests').glob('*/summary.json'))
 assert len(summaries)==1
 result=json.loads(summaries[0].read_text(encoding='utf-8'))
 if not result['two_completed']:
  save(d/'external_failure_stop.json',{'at_utc':now(),'reason':'Incomplete/error provider pair: no retry and stop whole unit','summary':str(summaries[0]),'results':result['results']})
finally:
 save(d/'api_process_finished.json',{'pid':os.getpid(),'finished_at_utc':now(),'harness_returned':True,'process_exits_after_record':True})
