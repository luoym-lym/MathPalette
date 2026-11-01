from tools import *
for qid in sys.argv[1:]:
    s=AD.scenes[qid];c=read(TASK/qid/'context.json')
    print(qid,'RECORD',json.dumps(AD.records[qid],ensure_ascii=False))
    print('PROJECTION',s['projection'])
    print('NOTES',json.dumps(read(ROOT/'provenance/source_notes.json').get(qid),ensure_ascii=False))
    for o in c['objects']:
        if o.get('styleable') or o.get('type')=='face':print(o['id'],o['type'],json.dumps(o.get('geometry',{}),ensure_ascii=False,separators=(',',':')))
