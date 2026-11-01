from pathlib import Path
import sys
source=Path(__file__).with_name('prepare.py').read_text(encoding='utf-8').split('\nfor qid in sys.argv[1:]')[0]
exec(compile(source,str(Path(__file__).with_name('prepare.py')),'exec'))
for qid in sys.argv[1:]:
    dst=TASK/qid;dst.mkdir(parents=True,exist_ok=False)
    check=eligibility(qid);write(dst/'eligibility.json',check)
    if not check['eligible']:print(qid,'EXCLUDED');continue
    record=adapter.records[qid];write(dst/'formal_record.json',record)
    context=adapter.inspect_question(qid);write(dst/'context.json',context)
    (dst/'original.png').write_bytes(adapter.original_paths[qid].read_bytes())
    scene=adapter.scenes[qid];write(dst/'source_scene_snapshot.json',scene)
    print(json.dumps({'question_id':qid,'objects':[{'id':o['id'],'kind':o.get('kind'),'paths':len(o.get('partial_paths',[]))} for o in context['objects']],'labels':scene.get('labels',[]),'scene_keys':list(scene),'snap_points':context['snap_points'][:15]},ensure_ascii=False),flush=True)
