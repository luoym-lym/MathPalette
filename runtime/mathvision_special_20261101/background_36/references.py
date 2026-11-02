from tools_local import *
rows=[]
for i in range(1,12):
    batch=TASK.parent/f'batch_{i:02d}'
    for p in batch.rglob('design.json'):
        d=json.loads(p.read_text(encoding='utf-8-sig'))
        fields={k:v for k,v in d.items() if any(w in k.lower() for w in ['mechanism','intent','description','marker','information','wrong','hypothesis']) and k not in ['marker_path_bindings']}
        rows.append({'batch':batch.name,'question_id':d.get('question_id'),'path':str(p),'sha256':file_hash(p),'binding_fields_read':fields})
write(TASK/'delivered_references_read.json',{'readonly_references':rows,'lesson_applied':'Every own matched mark has a specified actual donor/receiver, fixed source geometry and predeclared misconception; arbitrary wrong option salience is insufficient. Numerical count semantics do not transform or count added ink. Native inspection and a unique unchanged human answer are separate gates from exact target hits.'})
for r in rows:
    f=r['binding_fields_read']
    print(r['batch'],r['question_id'],json.dumps({k:v for k,v in f.items() if isinstance(v,(str,int,float))},ensure_ascii=False)[:1300])
