from tools37 import *
for q in sys.argv[1:]:
    print('\nQUESTION',q)
    for p in sorted((TASK/q).glob('*/tests/*/run_*_response.json')):
        d=read(p);print('\nRAW',p.name,'SHA256',file_hash(p),'FINISH',d['choices'][0]['finish_reason']);print(d['choices'][0]['message']['content'])
