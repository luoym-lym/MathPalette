from pathlib import Path
import json,time
from bridge_adapter import RuntimeBridgeAdapter

OUT=Path(__file__).resolve().parent
adapter=RuntimeBridgeAdapter()
eligible=[json.loads(line) for line in (OUT.parent/'SolidGeometry_eligible.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
results=[];start=time.monotonic()
for index,record in enumerate(eligible):
    qid=record.get('id',record.get('question_id'))
    try:
        metadata=adapter.inspect_question(qid)
        result={'question_id':qid,'baseline_matches_formal':True,'pixel_sha256':metadata['original_pixel_sha256'],'object_count':len(metadata['objects']),'styleable_object_count':sum(bool(o.get('styleable')) for o in metadata['objects']),'snap_point_count':len(metadata['snap_points'])}
    except Exception as error:result={'question_id':qid,'baseline_matches_formal':False,'error':str(error)}
    results.append(result)
    if (index+1)%20==0:print(json.dumps({'processed':index+1,'total':len(eligible),'elapsed_seconds':round(time.monotonic()-start,1)},ensure_ascii=False),flush=True)
report={'total':len(results),'baseline_ok':sum(r['baseline_matches_formal'] for r in results),'baseline_failed':sum(not r['baseline_matches_formal'] for r in results),'elapsed_seconds':round(time.monotonic()-start,1),'results':results,'mode':'Existing dedicated MathVision bridge, runtime-only path redirection and write guard. Generic Solid baseline_inventory.json is retained separately.'}
(OUT/'bridge_baseline_inventory.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='results'},ensure_ascii=False),flush=True)
