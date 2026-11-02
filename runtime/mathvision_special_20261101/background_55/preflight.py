from bootstrap import *
import json, hashlib
from dataset_tools.catalog import content, digest, read, rows

IDS=['Solid195','Solid200','Solid205','Solid206','Solid207','Solid208','Solid209','Solid210']
RELATED=['Solid96','Solid163']
BRANCH=PROJECT/'SolidGeometry'

def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def eligible(qid):
    record=next(r for r in rows(BRANCH/'dataset.jsonl') if r['id']==qid)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    current=content(PROJECT,'SolidGeometry',record)
    special=BRANCH/'special_variant'/qid
    recipes=read(special/'recipes.json') if (special/'recipes.json').is_file() else []
    collections=[]
    for path in [special/'collection.json',BRANCH/'special_variant/collected_index.jsonl']:
        if path.is_file():
            collections.append({'path':str(path),'sha256':file_hash(path),'content':path.read_text(encoding='utf-8-sig') if path.name=='collection.json' else [r for r in rows(path) if r.get('question_id',r.get('id'))==qid]})
    valid=record['source_dataset']=='MathVision' and approval.get('reviewer')=='user' and bool(approval.get('instruction')) and digest(current)==approval['content_sha256'] and not recipes and not any(c['path'].endswith('collection.json') or c['content'] for c in collections)
    return {'question_id':qid,'eligible':valid,'record':record,'approval':approval,'current_content_sha256':digest(current),'scoped_files':current['files'],'special_recipes':recipes,'collections':collections}

if __name__=='__main__':
    audit={}
    for qid in IDS:
        value=eligible(qid); assert value['eligible'],qid
        audit[qid]=value
        save(HERE/qid/'eligibility_start.json',value)
        save(HERE/qid/'formal_record.json',value['record'])
    save(HERE/'eligibility_start.json',audit)
    evidence={}
    for qid in IDS+RELATED:
        found=[]
        for path in BASE.rglob('*'):
            if not path.is_file() or path.is_relative_to(HERE): continue
            if qid in path.parts or path.name.startswith(qid+'_'):
                if not any(x in path.parts for x in ('cache','mpl_cache','mplcache','tmp','render_tmp')):
                    found.append({'path':str(path.relative_to(PROJECT)),'sha256':file_hash(path),'bytes':path.stat().st_size})
        evidence[qid]=found
    save(HERE/'old_evidence_inventory.json',evidence)
    print(json.dumps({'eligibility':{k:v['eligible'] for k,v in audit.items()},'old_file_counts':{k:len(v) for k,v in evidence.items()}},ensure_ascii=False))
