from tools27 import *
idx=json.loads((HERE/'old_evidence_index.json').read_text(encoding='utf-8'))
qid=sys.argv[1]
for name in idx[qid]['files']:
    p=ROOT/name
    if (p.name=='design.json' or p.name=='plugin.json' or p.name.endswith('_response.json')
        or p.name in ('primary_visual_review.json','primary_review.json','manual_final_review.json')
        or ('math_audit' in p.name) or p.name=='full_vector_reflection_audit.json'):
        print('\nFILE '+name+'\n'+p.read_text(encoding='utf-8-sig'))
