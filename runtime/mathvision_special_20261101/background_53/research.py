from bootstrap import *
import hashlib
import json
from datetime import datetime, timezone

IDS = ['Solid238','Solid241','Solid242','Solid243','Solid244','Solid245','Solid246','Solid248']
BRANCH = PROJECT / 'SolidGeometry'

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False,default=lambda x:x.tolist() if hasattr(x,'tolist') else x.item())+'\n',encoding='utf-8')

def now():
    return datetime.now(timezone.utc).isoformat()

def eligibility(qid, output=None):
    from dataset_tools.catalog import rows, content, digest, validate_formal_row
    record = next(r for r in rows(BRANCH/'dataset.jsonl') if r['id']==qid)
    validate_formal_row(PROJECT,'SolidGeometry',record)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    snapshot = content(PROJECT,'SolidGeometry',record)
    fingerprint = digest(snapshot)
    accepted = [r for r in rows(BRANCH/'special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collected = [r for r in rows(BRANCH/'special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    folder = BRANCH/'special_variant'/qid
    specials = {str(p.relative_to(PROJECT)):read(p) for p in folder.rglob('*.json')} if folder.exists() else {}
    passed = any('recipes.json' in p or '/plugins/' in p for p in specials)
    complete = any('collection.json' in p for p in specials)
    eligible = record['source_dataset']=='MathVision' and approval.get('reviewer')=='user' and bool(approval.get('instruction')) and fingerprint==approval['content_sha256'] and not (accepted or collected or passed or complete)
    result = {'question_id':qid,'checked_at_utc':now(),'eligible':eligible,'record':record,'approval':approval,'current_content_sha256':fingerprint,'approval_matches':fingerprint==approval['content_sha256'],'accepted_records':accepted,'collected_records':collected,'special_records':specials,'formal_input_binding':snapshot,'authoritative_hashes':{str(p.relative_to(PROJECT)):sha(p) for p in [BRANCH/'dataset.jsonl',BRANCH/'special_variant/accepted_index.jsonl',BRANCH/'special_variant/collected_index.jsonl',PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json']}}
    if output: dump(output,result)
    return result

def inventory():
    histories = {qid:[] for qid in IDS}
    for p in SHARED.rglob('*'):
        if not p.is_file() or p.is_relative_to(OWN):
            continue
        for qid in IDS:
            if qid in p.parts or p.name.startswith(qid+'_'):
                histories[qid].append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
    reports=[]
    for label in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly']:
        p=SHARED/'independent_review'/label/'independent_review.json'
        reports.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'keys':list(read(p))})
    dump(OWN/'history_inventory.json',{'created_at':now(),'histories':histories,'semantic_rejects':reports})
    print(json.dumps({'history_files':{q:len(v) for q,v in histories.items()},'reports':reports},ensure_ascii=False))
    for qid in IDS:
        out=OWN/qid
        result=eligibility(qid,out/'eligibility_initial.json')
        print(qid,'eligible',result['eligible'],'files',len(result['formal_input_binding']['files']))
        print('HISTORY',json.dumps([x['path'].replace(str(SHARED),'') for x in histories[qid] if not x['path'].endswith('.png')],ensure_ascii=False))

if __name__=='__main__':
    inventory()
