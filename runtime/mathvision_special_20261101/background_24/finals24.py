from tools24 import *
for q in sys.argv[1:]:
    for p in sorted((HERE/q).glob('r24_*/tests/**/run_*_response.json')):
        d=read(p);print('\nRAW_FINAL',str(p.relative_to(HERE)),d['choices'][0].get('finish_reason'));print(d['choices'][0]['message'].get('content',''))
