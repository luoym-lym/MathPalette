from tools_local import *
for s in sorted(HERE.glob('Plane*/*/tests/*/summary.json')):
    d=json.loads(s.read_text(encoding='utf-8'));print('\nEVIDENCE',str(s.parent),'PRESET',d['expected_wrong_answer'])
    if len(sys.argv)>1 and d['question_id'] not in sys.argv[1:]:continue
    for r in d['results']:
        print('RUN',r['run_index'],'STATUS',r['status'])
        print(r.get('answer',r.get('text',r)))
