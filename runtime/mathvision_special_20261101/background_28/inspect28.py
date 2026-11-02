from tools28 import *
mode=sys.argv[1]
if mode=='reviews':
    for qid in ASSIGNED:
        h=read(TASK/qid/'prior_history_full.json');print('QUESTION',qid)
        for name,txt in h['full_text_records'].items():
            if Path(name).name in ['primary_review.json','primary_prescreen.json','primary_visual_review.json']:
                d=json.loads(txt)
                for k in ['input_freeze','frozen_inputs','eligibility','eligibility_at_assessment','each_marker_role_and_source_binding']:d.pop(k,None)
                print(name,json.dumps(d,ensure_ascii=False))
    cp=read(SHARED/'background_13/checkpoint.json')
    print('checkpoint_keys',list(cp))
    for k,v in cp.items():
        if isinstance(v,list):
            print('Solid143_mentions',k,json.dumps([x for x in v if isinstance(x,dict) and x.get('question_id')=='Solid143'],ensure_ascii=False))
elif mode=='notes':
    notes=read(ROOT/'provenance/source_notes.json')
    for qid in sys.argv[2:]:
        n=notes.get(qid,{})
        print('SOURCE_NOTES',qid,json.dumps({k:n.get(k) for k in ['audit','geometry_notes']},ensure_ascii=False))
elif mode=='edges':
    for qid in sys.argv[2:]:
        s=AD.scenes[qid];print('GEOMETRY',qid,json.dumps(s['projection']),json.dumps(s['ambiguities']))
        print('EDGES',qid,json.dumps([{'id':o['id'],'points':o.get('points'),'visibility':o.get('visibility')} for o in s['objects'] if o['type']=='segment' and (qid!='Solid123' or o['id'].startswith('proto'))],separators=(',',':')))
elif mode=='refs':
    for p in sorted(SHARED.glob('batch_*/manifest.json')):
        d=read(p);print(p.parent.name,json.dumps([{k:c.get(k) for k in ['question_id','mechanism','correct_answer','expected_wrong_answer','tested_final_answers','quality_review','candidate_source']} for c in d.get('candidates',[])],ensure_ascii=False))
