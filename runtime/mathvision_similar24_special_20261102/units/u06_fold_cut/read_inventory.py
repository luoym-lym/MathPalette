from local_env import *
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['start','history','refs','assignment'])
parser.add_argument('--qid')
args = parser.parse_args()
a = read_json(OWN/'assignment.json')
if args.mode == 'start':
    files = {str(OWN/x):sha(OWN/x) for x in ['assignment.json','brief.txt']}
    checks = {}
    for q in a['questions']:
        changed = []
        for rel, digest in q['frozen_source_files_sha256'].items():
            actual = sha(PROJECT/rel)
            if actual != digest:
                changed.append({'path':rel,'expected':digest,'actual':actual})
        checks[q['question_id']] = {'frozen_source_hashes_match':not changed,'changed':changed}
    save(OWN/'source_start.json', {'created_at':now(),'assignment_brief_original_hashes':files,'questions':checks}, True)
    save(OWN/'checkpoint.json', {'updated_at':now(),'unit_id':'u06_fold_cut','phase':'reading','new_actual_calls':0,'questions':{q['question_id']:{'status':'reading','reason':'math/reference/history gates pending'} for q in a['questions']},'formal_changes':False})
    save(OWN/'second_review_queue.json', [])
    print(json.dumps(checks,ensure_ascii=False,indent=2))
elif args.mode == 'assignment':
    for q in a['questions']:
        if args.qid is None or q['question_id']==args.qid:
            print(json.dumps(q,ensure_ascii=False,indent=2))
elif args.mode == 'refs':
    manifest=read_json(TASK/'reference_manifest.json')
    log=[]
    for qid, entry in manifest.items():
        root=TASK/entry['directory']
        for f in sorted(root.rglob('*')):
            if f.is_file():
                log.append({'path':str(f),'sha256':sha(f)})
                if f.suffix=='.json':
                    print(str(f.relative_to(TASK)))
                    print(f.read_text(encoding='utf-8-sig'))
    save(OWN/'reference_read_inventory.json',log)
elif args.mode == 'history':
    h=read_json(TASK/'history_index.json')
    for q in h['questions']:
        if q['question_id']!=args.qid:
            continue
        save(OWN/args.qid/'history_index_excerpt.json',q)
        print(json.dumps(q,ensure_ascii=False,indent=2))
