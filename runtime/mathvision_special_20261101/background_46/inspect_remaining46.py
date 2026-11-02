from tools46 import *
for q in ['Solid104','Solid141','Solid189']:
    sc=read(OWN/q/'native_scene_46.json');ctx=read(OWN/q/'context_46.json')
    print(q, json.dumps({k:v for k,v in sc.items() if k not in ['points','objects','constraints']},ensure_ascii=False))
    print('COUNTS',len(sc.get('points',{})),len(sc.get('objects',[])),len(sc.get('constraints',[])))
    print('SAMPLE_OBJECTS',json.dumps(sc.get('objects',[])[:6],ensure_ascii=False))
    print('CONTEXT_SAMPLE',json.dumps(ctx['objects'][:2],ensure_ascii=False))
