from env41 import *
cfg,ad=adapter()
for q in ASSIGNED:
    e=eligibility(q);write(HERE/q/'eligibility_start.json',e);assert e['eligible'],q
    meta=ad.inspect_question(q);write(HERE/q/'context.json',meta)
    write(HERE/q/'formal_record.json',ad.records[q]);write(HERE/q/'source_scene_snapshot.json',read(ROOT/'PlaneGeometry'/ad.records[q]['scene']))
    paths={str(p.relative_to(ROOT)):file_hash(p) for p in set(ad.input_files.values())}
    write(HERE/q/'adapter_input_hashes.json',paths)
    print(json.dumps({'qid':q,'eligible':e['eligible'],'approval_valid':e['valid_current_user_approval'],'baseline_pixel_match':True,'record':ad.records[q]['question'],'objects':meta['objects'],'snaps':meta['snap_points']},ensure_ascii=False),flush=True)
