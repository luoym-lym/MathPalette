from tools34 import *
for qid in sys.argv[1:] or IDS:
    rec=record(qid); root=PROJECT/branch_of(qid)
    native=next(root/p for p in rec['runtime_dependencies'] if '/items/'+qid+'/scene.json' in p)
    source=next(root/p for p in rec['runtime_dependencies'] if '/items/'+qid+'/source.json' in p)
    scene=read(native)
    print(qid+' SCENE '+json.dumps(scene,ensure_ascii=False,separators=(',',':')))
    print(qid+' SOURCE '+json.dumps(read(source),ensure_ascii=False,separators=(',',':')))
    ctx=read(UNIT/qid/'fresh_context.json')
    print(qid+' OBJECTS '+json.dumps([{'id':x['id'],'geometry':x.get('geometry'),'source_call':x.get('source_call'),'frozen_visibility':x.get('frozen_visibility')} for x in ctx['objects']],ensure_ascii=False,separators=(',',':')))
    print(qid+' SNAP '+json.dumps(ctx['snap_points'],ensure_ascii=False,separators=(',',':')))
