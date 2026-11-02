from bootstrap31 import *
import argparse
import shutil
sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from dataset_tools import catalog

def rows(path):
    return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []

def eligibility(qid):
    base = PROJECT/'PlaneGeometry'
    rec = next(r for r in rows(base/'dataset.jsonl') if r['id']==qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'].get(qid,{})
    current = catalog.digest(catalog.content(PROJECT,'PlaneGeometry',rec))
    accepted = [r for r in rows(base/'special_variant/accepted_index.jsonl') if r.get('question_id')==qid]
    collected = [r for r in rows(base/'special_variant/collected_index.jsonl') if r.get('question_id')==qid]
    folder = base/'special_variant'/qid
    recipes = read(folder/'recipes.json') if (folder/'recipes.json').exists() else None
    collection = read(folder/'collection.json') if (folder/'collection.json').exists() else None
    exclusions=[]
    if rec.get('source_dataset')!='MathVision': exclusions.append('not formal MathVision')
    if not (approval.get('reviewer')=='user' and approval.get('instruction') and approval.get('approved_at_utc') and approval.get('content_sha256')==current): exclusions.append('original approval invalid')
    if any(r.get('status')=='passed' for r in accepted): exclusions.append('passed index')
    if any(r.get('status')=='collected' or r.get('special_case') for r in collected): exclusions.append('collected index')
    if recipes:
        entries = recipes if isinstance(recipes,list) else recipes.get('recipes',recipes.get('variants',[]))
        if isinstance(entries,dict): entries=list(entries.values())
        if any(r.get('status')=='passed' or r.get('reviewed_at') for r in entries): exclusions.append('passed recipe')
    if collection:
        c=collection.get('current',{})
        if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'): exclusions.append('special completion')
    delivered=[]
    for p in sorted(SHARED.glob('batch_*/manifest.json')):
        data=read(p)
        if qid in json.dumps(data): delivered.append(str(p))
    if delivered: exclusions.append('runtime delivered')
    paths=[base/'dataset.jsonl', PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json',base/'special_variant/accepted_index.jsonl',base/'special_variant/collected_index.jsonl',folder/'recipes.json',folder/'collection.json']
    return {'question_id':qid,'checked_at':stamp(),'eligible':not exclusions,'reasons':exclusions,'formal_record':rec,'approval':approval,'current_content_sha256':current,'accepted_records':accepted,'collected_records':collected,'recipes':recipes,'collection':collection,'delivered_manifests':delivered,'authoritative_hashes':{str(p.relative_to(PROJECT)):sha(p) if p.exists() else None for p in paths},'mutable_progress_metadata':{p.name:sha(p) for p in [SHARED/'exploration_report.json',SHARED/'remaining_questions.jsonl']}}

def init():
    from workbench_io import load_config, environment_versions
    from mathvision_adapter import RendererAdapter
    config=load_config()
    config.update(runtime_dir=str(OWN/'state'),output_dir=str(OWN/'output'))
    adapter=RendererAdapter(config)
    all_old={}
    for qid in IDS:
        d=OWN/qid
        e=eligibility(qid)
        assert e['eligible'], e['reasons']
        save(d/'eligibility_start.json',e)
        save(d/'formal_record.json',e['formal_record'])
        metadata=adapter.inspect_question(qid)
        save(d/'context.json',metadata)
        rec=e['formal_record']
        base=PROJECT/'PlaneGeometry'
        paths=[base/rec[key] for key in ['image','original_image','scene','script'] if rec.get(key)]
        paths += [base/p for p in rec.get('runtime_dependencies',[])]
        paths += list(adapter.input_files.values())
        sources={str(p.relative_to(PROJECT)):sha(p) for p in paths if p.exists()}
        save(d/'input_fingerprints.json',sources)
        save(d/'source_scene_snapshot.json',read(base/rec['scene']))
        (d/'original.png').write_bytes((base/rec['image']).read_bytes())
        old=[]
        for p in SHARED.rglob('*'):
            if not p.is_file() or p.is_relative_to(OWN): continue
            if qid in p.parts or (qid+'_' in p.name) or p.name==qid+'.png':
                old.append(p)
        old=sorted(set(old))
        all_old[qid]={str(p.relative_to(PROJECT)):sha(p) for p in old}
        # Full old evidence bytes are read, manifests remain separate from semantic notes.
        save(d/'prior_evidence_inventory.json',all_old[qid])
        print(json.dumps({'question_id':qid,'objects':len(metadata['objects']),'old_files':len(old),'source_files':len(sources),'original_approval_valid':True}),flush=True)
    save(OWN/'prior_evidence_hashes_start.json',all_old)
    save(OWN/'isolation.json',{'created_at':stamp(),'isolation':ISOLATION,'strict_unit_write_guard':True,'root':str(OWN),'environment':environment_versions(),'no_child_agents':True})

def reports():
    # Emit every substantive report field, suppress only repetitive audit hash registries.
    for folder in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding']:
        p=SHARED/'independent_review'/folder/'independent_review.json'
        j=read(p)
        print('\nREPORT '+str(p)+' SHA256 '+sha(p))
        for k,v in j.items():
            if k in ('current_authoritative_eligibility','reviewed_source_evidence_hashes','source_evidence_hashes') or 'hashes' in k:
                print(k+': '+json.dumps({'read_in_full':True,'content_bytes':len(json.dumps(v)),'note':'hash/eligibility registry; semantics emitted in other fields'}))
            else:
                print(k+': '+json.dumps(v,ensure_ascii=False))

def prior():
    for qid in IDS:
        print('\nQUESTION '+qid)
        for p in sorted(SHARED.rglob('*')):
            if not p.is_file() or p.is_relative_to(OWN) or p.suffix!='.json': continue
            if qid not in p.parts: continue
            if p.name in ('design.json','primary_review.json','mathematical_audit.json','prescreen.json','prescreen_assessment.json'):
                print(str(p)+': '+json.dumps(read(p),ensure_ascii=False))
            elif p.name.endswith('_response.json'):
                j=read(p)
                print('FULL_RAW_REPLY '+str(p)+': '+json.dumps(j,ensure_ascii=False))

if __name__=='__main__':
    globals()[sys.argv[1]]()
