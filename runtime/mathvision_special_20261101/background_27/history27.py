from tools27 import *

# Read only old same-question evidence; record exact immutable file bindings.
index = {}
for qid in ASSIGNED:
    roots = []
    for p in BASE.rglob(qid):
        if p.is_dir() and not p.is_relative_to(HERE) and not any(x.startswith('batch_') for x in p.relative_to(BASE).parts):
            roots.append(p)
    files = sorted({p for root in roots for p in root.rglob('*') if p.is_file()})
    # Independent reviews may use a combined question/variant folder name.
    for root in (BASE/'independent_review').glob(qid+'*'):
        files.extend(p for p in root.rglob('*') if p.is_file())
    files = sorted(set(files))
    index[qid] = {'roots':[str(p.relative_to(ROOT)) for p in roots],
                  'files':{str(p.relative_to(ROOT)):file_hash(p) for p in files},
                  'designs':[str(p.relative_to(ROOT)) for p in files if p.name in ('design.json','design_snapshot.json')],
                  'pngs':[str(p.relative_to(ROOT)) for p in files if p.suffix.lower()=='.png'],
                  'raw_replies':[str(p.relative_to(ROOT)) for p in files if p.name.endswith('_response.json')],
                  'reviews':[str(p.relative_to(ROOT)) for p in files if 'review' in p.name or 'assessment' in p.name or 'audit' in p.name]}
write(HERE/'old_evidence_index.json',index)
for qid,item in index.items():
    print(json.dumps({'qid':qid, 'roots':item['roots'], 'pngs':item['pngs'], 'designs':[p for p in item['designs'] if not p.endswith('design_snapshot.json')], 'reviews':item['reviews'], 'raw_reply_count':len(item['raw_replies'])},ensure_ascii=False))
