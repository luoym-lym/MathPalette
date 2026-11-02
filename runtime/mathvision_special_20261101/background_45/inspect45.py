from tools45 import *
mode=sys.argv[1]
if mode=='scenes':
    notes=read(ROOT/'provenance/source_notes.json')
    for q in sys.argv[2:]:
        r=AD.records[q];p=(ROOT/'SolidGeometry'/r['runtime_dependencies'][0]).parent
        v=read(p/'scene.json')
        print(q,'FORMAL QUESTION',r['question'])
        n=notes.get(q,{})
        print('NOTES',json.dumps({'original_record':n.get('original_record'),'audit':n.get('audit'),'geometry_extras':n.get('geometry_notes',{}).get('additional_model_evidence')},ensure_ascii=False))
        print('SCENE_NONOBJECT',json.dumps({k:x for k,x in v.items() if k not in ['objects','labels','points','visibility']},ensure_ascii=False))
        print('POINTS',json.dumps(v.get('points'),ensure_ascii=False))
        print('LABELS',json.dumps(v.get('labels'),ensure_ascii=False))
        if '--objects' in sys.argv:print('OBJECTS',json.dumps(v.get('objects'),ensure_ascii=False))
elif mode=='semantic_review':
    p=SHARED/'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json'
    v=read(p)
    print(json.dumps({k:x for k,x in v.items() if k not in ['two_complete_final_answers','preservation','supporting_new_review_files','timestamp_binding','exact_frozen_hashes']},ensure_ascii=False,indent=2))
elif mode=='old98':
    d=read(OLD['Solid98']/'front_row_color_correspondence/design.json')
    print(json.dumps({k:x for k,x in d.items() if k!='marker_roles'},ensure_ascii=False,indent=2))
    for x in d['marker_roles']:print(x['action_index'],x['action'],x['role'])
elif mode=='receipts':
    paths=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
    paths += [str(p.relative_to(ROOT)) for p in [SHARED/'background_45_brief.txt',SHARED/'background_45_assignment.json',SHARED/'continuation_brief.txt',SHARED/'annotation_semantics_lesson_plane242_r24_20261102.json',SHARED/'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json']]
    receipt={p:{'sha256':file_hash(ROOT/p),'bytes_read':len((ROOT/p).read_bytes())} for p in paths}
    write(TASK/'protocol_read_receipt.json',receipt)
    refs=[]
    for p in sorted(SHARED.glob('batch_*/manifest.json')):
        v=read(p)
        for x in v['candidates']:
            refs.append({k:z for k,z in x.items() if k in ['question_id','mechanism','intent','candidate_path','source_candidate','expected_wrong_answer']})
    write(TASK/'delivered_reference_study.json',refs)
    print(json.dumps(refs,ensure_ascii=False))
