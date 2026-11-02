from tools26 import *
q=sys.argv[1];assert q in ASSIGNED
inventory=read(HERE/'history_inventory.json')[q]
for relative in inventory:
    p=ROOT/relative;d=p.parent
    if len(sys.argv)>2 and d.name not in sys.argv[2:]:continue
    print('\nDESIGN '+relative+'\n'+p.read_text(encoding='utf-8-sig'))
    for name in ['plugin.json','primary_review.json','primary_review.md','primary_math_audit.json','error.txt']:
        path=d/name
        if path.exists():print('\nFILE '+str(path.relative_to(ROOT))+'\n'+path.read_text(encoding='utf-8-sig'))
    for path in sorted(d.rglob('run_*_response.json')):
        raw=read(path)
        print('\nFULL RAW RESPONSE '+str(path.relative_to(ROOT))+'\n'+json.dumps(raw,ensure_ascii=False))
    for path in sorted(d.rglob('run_*.json')):
        if '_response' in path.name or '_started' in path.name:continue
        obj=read(path)
        if obj.get('status')!='completed':print('\nFAILURE '+str(path.relative_to(ROOT))+'\n'+json.dumps(obj,ensure_ascii=False))
for path in (BASE/'independent_review').rglob('*'):
    if path.suffix in ('.json','.md','.txt') and q in str(path):print('\nINDEPENDENT '+str(path.relative_to(ROOT))+'\n'+path.read_text(encoding='utf-8-sig'))
