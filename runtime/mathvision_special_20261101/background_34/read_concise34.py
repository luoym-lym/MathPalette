from tools34 import *
for qid in sys.argv[1:]:
    rec=record(qid); root=PROJECT/branch_of(qid)
    scene=read(next(root/p for p in rec['runtime_dependencies'] if '/items/'+qid+'/scene.json' in p))
    print(qid+' KEYS '+str(list(scene)))
    for key in ('points','objects','projection','constraints','ambiguities'):
        value=scene.get(key)
        if qid=='Plane257' and key=='objects':value=[x for x in value if x['id'].startswith(('f2','f3','f4'))]
        if qid=='Solid88' and key in ('points','objects'):continue
        print(qid+' '+key+' '+json.dumps(value,ensure_ascii=False,separators=(',',':')))
    source=read(next(root/p for p in rec['runtime_dependencies'] if '/items/'+qid+'/source.json' in p))
    print(qid+' SOURCE '+json.dumps(source,ensure_ascii=False,separators=(',',':')))
for qid,variant in [('Plane295','inner_ear_shoulder_correspondence'),('Plane342','quarterturn_wedge_edge_binding')]:
    data=read(SHARED/'independent_review'/(qid+'_'+variant)/'independent_review.json')
    print(qid+' REJECTION '+json.dumps({k:data[k] for k in ('decision','reason','human_semantics','concrete_objections','limits') if k in data},ensure_ascii=False,separators=(',',':')))
