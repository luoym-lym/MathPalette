from tools_local import *
for qid in sys.argv[1:]:
    data=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'))
    print('\nQUESTION',qid)
    for o in data['objects']:print(json.dumps(o,ensure_ascii=False))
    print('CANVAS',json.dumps({k:v for k,v in data['canvas'].items() if k!='targets'},ensure_ascii=False))
