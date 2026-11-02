from tools26 import *
for q in sys.argv[1:]:
    for p in sorted((HERE/q).glob('r26_*/tests/*/run_*_response.json')):
        raw=read(p);print(str(p.relative_to(HERE)))
        for c in raw['choices']:print('FINISH '+str(c['finish_reason'])+'\n'+str(c['message'].get('content')))
