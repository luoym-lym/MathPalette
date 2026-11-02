import own_runtime as rt
import sys

p=rt.OWN/'checkpoint.json';checkpoint=rt.read(p)
checkpoint['updated_at_utc']=rt.now()
checkpoint['stage']=sys.argv[1] if len(sys.argv)>1 else 'OFFLINE_GATES'
calls=0
for qid in rt.read(rt.OWN/'assignment.json')['question_ids']:
    d=rt.OWN/qid
    designs=list(d.glob('*/design.json'))
    starts=list(d.glob('*/tests/*/run_*_started.json'))
    complete=list(d.glob('*/tests/*/run_??.json'))
    calls+=len(starts)
    checkpoint['questions'][qid]={'status':'offline_prepared' if designs else 'in_progress',
        'designs':[str(x.parent) for x in designs],'actual_request_starts':len(starts),
        'completed_or_error_records':len(complete),'notes':'PRIMARY only; no independent second review or formal approval'}
checkpoint['new_model_calls']=calls
rt.save(p,checkpoint)
print(checkpoint['stage'],calls)
