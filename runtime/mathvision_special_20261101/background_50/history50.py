from env50 import *
from inspect50 import IDS
from dataset_tools.catalog import read
out={}
for q in IDS:
    records=read(OWN/q/'old_file_manifest.json'); parsed=[]; texts=[]; images=[]; errors=[]
    for item in records:
        p=Path(item['path']);b=p.read_bytes()
        if p.suffix.lower()=='.json':
            try:
                data=json.loads(b.decode('utf-8-sig'));parsed.append({'path':str(p),'sha256':item['sha256'],'top_keys':list(data) if isinstance(data,dict) else 'list'})
                if any(v in p.name for v in ['assessment','prescreen','primary_audit']):texts.append({'path':str(p),'content':data})
            except Exception as x:errors.append({'path':str(p),'error':str(x),'sha256':item['sha256'],'not_repaired':True})
        elif p.suffix.lower() in ['.jpg','.png']:images.append(item)
    out[q]={'all_old_files_loaded':parsed,'all_old_images':images,'malformed_preserved':errors,'complete_old_assessments':texts,'old_designs':[i for i in records if Path(i['path']).name=='design.json'],'old_raw_responses':[i for i in records if 'response' in Path(i['path']).name]}
    print(json.dumps({'qid':q,'assessments':texts,'designs':out[q]['old_designs'],'raw_responses':out[q]['old_raw_responses'],'parse_errors':errors},ensure_ascii=False))
dump(OWN/'history_read_audit.json',out)
# Read exact independent reports in full; emit their prose evidence, preserving hash manifests as referenced source data.
reports=[]
for p in (ROOT/'independent_review').rglob('independent_review.json'):
    if any(q in str(p) for q in ['Plane295_inner_ear','Plane342_quarterturn','Plane242_r24','Plane242_r24_disconnected']):
        obj=read(p)
        prose={k:v for k,v in obj.items() if k not in ['source_and_evidence_preservation','source_and_evidence_audit','source_hashes','evidence_binding_audit','supporting_new_review_files','frozen_evidence_bindings','binding_audit','evidence_audit']}
        reports.append({'path':str(p),'sha256':sha(p),'top_keys':list(obj)})
        dump(OWN/('lesson_report_'+p.parent.name+'.json'),prose)
        print('LESSON_REPORT',str(p),'KEYS',list(obj))
dump(OWN/'independent_lessons_read.json',reports)
for q in IDS:
    s=read(OWN/q/'formal_scene_snapshot.json')
    if q in ['Plane176','Plane197']:
        print(q,json.dumps({'points':s['points'],'objects':[o for o in s['objects'] if q=='Plane197' or o.get('semantic_fill')],'constraints':s['constraints'] if q=='Plane176' else []},ensure_ascii=False))
