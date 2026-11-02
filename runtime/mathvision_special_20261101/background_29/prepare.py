import bootstrap
from bootstrap import OWN,ROOT,HISTORY
from pathlib import Path
import json,hashlib
def save(p,v):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source=HISTORY/'solid_explore/bridge_adapter.py'
code=source.read_text(encoding='utf-8')
(OWN/'bridge_adapter.py').write_text(code,encoding='utf-8')
hsource=HISTORY/'harness/quicktest3_isolated.py'
hcode=hsource.read_text(encoding='utf-8')
hcode=hcode.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = next(p for p in Path(__file__).resolve().parents if (p / "MATHPALETTE_PROTOCOL.md").is_file())')
hcode=hcode.replace('def timestamp():','sys.path.insert(0, str(HARNESS.parent))\nimport bootstrap\n\ndef timestamp():',1)
hp=OWN/'harness/quicktest3_isolated.py';hp.parent.mkdir(exist_ok=True);hp.write_text(hcode,encoding='utf-8')
save(OWN/'harness_isolation_audit.json',{'original':str(hsource),'original_sha256':sha(hsource),'copy_sha256':sha(hp),'changes':['project root discovery adjusted for deeper own directory','import bootstrap own-root write guard before any reference-module import'],'request_loop_payload_profiles_timeouts_and_retries':'unchanged','adapter_source_sha256':sha(source),'adapter_copy_sha256':sha(OWN/'bridge_adapter.py')})
from bridge_adapter import RuntimeBridgeAdapter
from dataset_tools import catalog
adapter=RuntimeBridgeAdapter()
assignment=json.loads((HISTORY/'background_29_assignment.json').read_text(encoding='utf-8-sig'))
approvals=json.loads((ROOT/'provenance/approvals.json').read_text(encoding='utf-8-sig'))['approvals']
def lines(p):return [json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()] if p.exists() else []
accepted=lines(ROOT/'SolidGeometry/special_variant/accepted_index.jsonl');collected=lines(ROOT/'SolidGeometry/special_variant/collected_index.jsonl')
notes,_=catalog._source_notes_snapshot(ROOT)
inventory={}
for qid in assignment['question_ids']:
    r=adapter.records[qid];folder=ROOT/'SolidGeometry/special_variant'/qid
    recipes=json.loads((folder/'recipes.json').read_text(encoding='utf-8-sig')) if (folder/'recipes.json').exists() else {}
    collection=json.loads((folder/'collection.json').read_text(encoding='utf-8-sig')) if (folder/'collection.json').exists() else {}
    ar=[x for x in accepted if x.get('question_id')==qid];cr=[x for x in collected if x.get('question_id')==qid]
    content=catalog.digest(catalog.content(ROOT,'SolidGeometry',r,source_notes=notes))
    eligibility={'question_id':qid,'formal_mathvision':r['source_dataset']=='MathVision','accepted_records':ar,'collected_records':cr,'recipes':recipes,'collection':collection,'approval':approvals[qid],'actual_content_sha256':content,'approval_matches':content==approvals[qid]['content_sha256']}
    assert eligibility['approval_matches'] and not ar and not cr and not recipes and not collection,eligibility
    d=OWN/qid;save(d/'eligibility_at_start.json',eligibility);save(d/'formal_record.json',r)
    context=adapter.inspect_question(qid);save(d/'context.json',context);save(d/'frozen_inputs.json',adapter.frozen_inputs(qid))
    old=[]
    for p in HISTORY.rglob('*'):
        if p.is_file() and qid in p.parts and not p.is_relative_to(OWN):old.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'size':p.stat().st_size})
    save(d/'old_evidence_manifest.json',old)
    inventory[qid]={'record':r,'old_file_count':len(old),'old_candidate_files':[x['path'] for x in old if Path(x['path']).name in ['design.json','candidate.png','plugin.json','primary_review.json']]}
save(OWN/'initial_inventory.json',inventory)
print(json.dumps(inventory,ensure_ascii=False,indent=2))
