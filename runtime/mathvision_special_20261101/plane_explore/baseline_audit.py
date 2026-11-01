import json,time,traceback
from pathlib import Path
from make_candidates import HERE,ROOT,load_config,RendererAdapter

config=load_config()
config['runtime_dir']=str(HERE/'audit_state')
config['output_dir']=str(HERE/'audit_output')
adapter=RendererAdapter(config)
eligible=[json.loads(line) for line in (HERE.parent/'PlaneGeometry_eligible.jsonl').read_text(encoding='utf8').splitlines() if line]
output=HERE/'baseline_compatibility.jsonl'
done={}
if output.exists():
    for line in output.read_text(encoding='utf8').splitlines():
        if line: 
            row=json.loads(line)
            done[row['question_id']]=row
for index,row in enumerate(eligible):
    qid=row.get('question_id') or row['id']
    if qid in done:continue
    started=time.time()
    try:
        metadata=adapter.inspect_question(qid)
        result={'question_id':qid,'baseline_compatible':True,'original_pixel_sha256':metadata['original_pixel_sha256'],
                'object_count':len(metadata['objects']),'snap_point_count':len(metadata['snap_points'])}
    except Exception as exc:
        result={'question_id':qid,'baseline_compatible':False,'error_type':type(exc).__name__,'error':str(exc)}
    result['elapsed_seconds']=round(time.time()-started,3)
    with output.open('a',encoding='utf8') as stream:stream.write(json.dumps(result,ensure_ascii=False)+'\n')
    done[qid]=result
    print(qid,'OK' if result['baseline_compatible'] else result['error'],flush=True)
summary={'total_eligible':len(eligible),'inspected':len(done),'compatible':sum(r['baseline_compatible'] for r in done.values()),
         'incompatible':sum(not r['baseline_compatible'] for r in done.values()),'results_file':str(output),
         'note':'Only unchanged adapter.inspect_question; native replay temp path redirected in memory into root runtime.'}
(HERE/'baseline_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(summary,ensure_ascii=False),flush=True)
