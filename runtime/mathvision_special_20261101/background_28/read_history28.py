from tools28 import *
for qid in ASSIGNED:
    h=read(TASK/qid/'prior_history_full.json')
    print('\nQUESTION',qid)
    for name,txt in h['full_text_records'].items():
        leaf=Path(name).name
        if any(s in leaf for s in ['prescreen','primary_review','primary_visual_review','manual_final_review','pretest_visual']):
            d=json.loads(txt)
            # Repeated immutable hash maps are audited by file manifest; preserve all semantic review fields.
            for k in ['input_freeze','frozen_inputs','eligibility','eligibility_at_assessment','manual_results']:
                d.pop(k,None)
            print(name,json.dumps(d,ensure_ascii=False))
    if qid in ['Solid143','Solid103']:
        for cp in [SHARED/'background_13/checkpoint.json']:
            d=read(cp)
            def mentions(v):
                if isinstance(v,dict):
                    if v.get('question_id')==qid:return v
                    return [x for s in v.values() if (x:=mentions(s))]
                if isinstance(v,list):return [x for s in v if (x:=mentions(s))]
                return None
            print('checkpoint_mentions',json.dumps(mentions(d),ensure_ascii=False))
notes=read(ROOT/'provenance/source_notes.json')
for qid in ASSIGNED:
    print('SOURCE_NOTES',qid,json.dumps(notes.get(qid),ensure_ascii=False))
for qid in ['Solid123','Solid109','Solid125','Solid86','Solid129']:
    s=AD.scenes[qid]
    print('GEOMETRY',qid,'projection',json.dumps(s['projection']),'ambiguities',json.dumps(s['ambiguities']))
    print('EDGES',qid,json.dumps([{'id':o['id'],'points':o.get('points'),'visibility':o.get('visibility')} for o in s['objects'] if o['type']=='segment'],separators=(',',':')))
for manifest in sorted(SHARED.glob('batch_*/manifest.json')):
    d=read(manifest)
    print('DELIVERED_REFERENCE',str(manifest),json.dumps({k:v for k,v in d.items() if k not in ['files','archive_files','supplemental_files']},ensure_ascii=False))
