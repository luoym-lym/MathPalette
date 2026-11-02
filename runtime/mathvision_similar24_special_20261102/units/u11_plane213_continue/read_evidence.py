from bootstrap import *
import argparse
p=argparse.ArgumentParser();p.add_argument('mode');p.add_argument('--index',type=int,default=0);args=p.parse_args()
roots=[OLD/'background_09/Plane213/open_notch_local_global_binding',TASK/'root_213/Plane213/user233_boundary_spine_foot_transfer_v1',TASK/'units/u10_plane213_refine/Plane213/user233_exterior_concave_corner_to_B_v2',OLD/'background_23/Plane233/r23_exterior_notch_correspondence']
if args.mode=='init':
    e=eligibility();save('eligibility_initial.json',e)
    save('second_review_queue.json',[])
    save('checkpoint.json',{'at_utc':now(),'scope':['Plane213'],'status':'reading_full_evidence','new_API_calls':0,'second_review_queue':[]})
    tracked={}
    for base in roots:
        for f in base.rglob('*'):
            if f.is_file(): tracked[str(f)]=sha(f)
    for q in read(TASK/'reference_manifest.json'):
        for f in (TASK/'references'/q).rglob('*'):
            if f.is_file():tracked[str(f)]=sha(f)
    for f in (ROOT/'PlaneGeometry/workbench').glob('*.py'):tracked[str(f)]=sha(f)
    for f in [ROOT/'AGENTS.md', ROOT/'MATHPALETTE_PROTOCOL.md', ROOT/'provenance/approvals.json',ROOT/'PlaneGeometry/dataset.jsonl',OLD/'runtime_isolation.py',OLD/'harness/quicktest3_isolated.py']:
        tracked[str(f)]=sha(f)
    for f,h in e['frozen_source_files_sha256'].items():tracked[str(ROOT/f)]=h
    save('readonly_initial_sha256.json',tracked)
    print(json.dumps({'eligible':True,'tracked_readonly_files':len(tracked),'evidence_roots':[str(x) for x in roots]}))
elif args.mode=='history':
    q=next(x for x in read(TASK/'history_index.json')['questions'] if x['question_id']=='Plane213')
    # Full history entry, excluding only repeated request aliases for the unmarked other question.
    q.pop('formal_original_png_prior_transport_records',None)
    print(json.dumps(q,ensure_ascii=False,indent=2))
elif args.mode=='raw':
    for f in sorted(roots[args.index].rglob('*_response.json')):
        print(str(f));print(f.read_text(encoding='utf-8-sig'))
elif args.mode=='reviews':
    for f in roots[args.index].glob('*.json'):
        if f.name in ('context.json','harness_context.json','fresh_context.json','eligibility_before_design.json','eligibility_immediately_before_calls.json'):continue
        print(str(f));print(f.read_text(encoding='utf-8-sig'))
elif args.mode=='reference':
    q=list(read(TASK/'reference_manifest.json'))[args.index]
    seen={}
    # Read every full file and losslessly represent duplicate JSON subtrees by their canonical SHA.
    def compact(v):
        if isinstance(v,(dict,list)):
            raw=json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':'))
            h=hashlib.sha256(raw.encode()).hexdigest()
            if len(raw)>200 and h in seen:return {'identical_to_previous_subtree':h}
            seen[h]=True
            return {k:compact(x) for k,x in v.items()} if isinstance(v,dict) else [compact(x) for x in v]
        return v
    for n in ('C01.json','recipes.json','reference.json'):
        f=TASK/'references'/q/n
        print(q+'/'+n);print(json.dumps(compact(read(f)),ensure_ascii=False,indent=2))
