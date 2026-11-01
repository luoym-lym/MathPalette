from tools_local import *
q=sys.argv[1];context=json.loads((TASK/q/'context.json').read_text(encoding='utf-8'))
print('projection',AD.scenes[q]['projection'])
for obj in context['objects']:
    if len(sys.argv)<3 or any(obj['id'].startswith(t) for t in sys.argv[2:]):
        print(json.dumps(obj,separators=(',',':')))
