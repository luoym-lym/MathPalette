from tools45 import *

def excerpts(v,q):
    if isinstance(v,dict):
        if v.get('question_id',v.get('id'))==q:return [v]
        found=[]
        for k,x in v.items():
            if k==q:found.append({k:x})
            else:found+=excerpts(x,q)
        return found
    if isinstance(v,list):return [z for x in v for z in excerpts(x,q)]
    return []

if sys.argv[1]=='history':
    inventory={}; reviews={}
    for q in IDS:
        entries=[]
        for p in OLD[q].rglob('*'):
            if not p.is_file():continue
            b=p.read_bytes();entry={'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
            if p.suffix=='.json':
                try:
                    v=json.loads(b.decode('utf-8-sig'));entry['parsed']=True
                    if p.name in ['design.json','plugin.json','primary_review.json','primary_prescreen.json','prescreen.json','primary_visual_review.json','manual_result_review.json','exact_colored_tiling_audit.json'] or p.name.endswith('_response.json'):
                        if p.name.endswith('_response.json'):v=v['choices'][0]['message']
                        reviews.setdefault(q,[]).append({'path':str(p),'content':v})
                except Exception as e:entry.update(parsed=False,error_type=type(e).__name__,preserve_verbatim=True)
            entries.append(entry)
        inventory[q]=entries
    for p in [SHARED/'solid_explore/checkpoint.json',SHARED/'background_05/checkpoint.json',SHARED/'background_06/checkpoint.json',SHARED/'background_07/checkpoint.json',SHARED/'background_17/checkpoint.json',SHARED/'exploration_report.json']:
        v=read(p)
        for q in IDS:
            for x in excerpts(v,q):reviews.setdefault(q,[]).append({'path':str(p),'content':x})
    write(TASK/'history_inventory_complete.json',inventory);write(TASK/'old_full_review_material_complete.json',reviews)
    print(json.dumps({q:{'files':len(inventory[q]),'review_sections':len(reviews.get(q,[])),'parse_failures':[x for x in inventory[q] if x.get('parsed') is False]} for q in IDS},ensure_ascii=False))
elif sys.argv[1]=='show':
    data=read(TASK/'old_full_review_material_complete.json')
    for q in sys.argv[2:]:
        print(q)
        print(json.dumps(data.get(q,[]),ensure_ascii=False,indent=2))
elif sys.argv[1]=='source':
    for q in sys.argv[2:]:
        r=AD.records[q];p=ROOT/'SolidGeometry'/r['runtime_dependencies'][0];item=p.parent
        print(q, r['question'])
        for n in ['scene.json','source_redraw.py','renderer.py']:
            p=item/n
            if p.exists():print(str(p),p.read_text(encoding='utf-8-sig'))
elif sys.argv[1]=='objects':
    for q in sys.argv[2:]:
        ctx=read(TASK/q/'context.json')
        print(q)
        for x in ctx['objects']:
            print(json.dumps({k:v for k,v in x.items() if k!='partial_paths'},ensure_ascii=False))
