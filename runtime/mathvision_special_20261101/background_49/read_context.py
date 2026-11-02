import research_env as env
import json,sys
from inspect_sources import save,sha,QIDS
for q in sys.argv[1:] or QIDS:
    ctx=json.loads((env.ROOT/q/'context.json').read_text(encoding='utf-8'))
    scene=json.loads((env.ROOT/q/'formal_scene.json').read_text(encoding='utf-8'))
    print('\n'+q)
    print(json.dumps({k:v for k,v in scene.items() if k!='objects'},ensure_ascii=False,separators=(',',':')))
    for o in ctx['objects']:
        print(json.dumps(o,ensure_ascii=False,separators=(',',':')))
    print('SNAPS',json.dumps(ctx['snap_points'],ensure_ascii=False,separators=(',',':')))
