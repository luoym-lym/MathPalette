from env56 import *

manifest = read(OWN/'old_history_manifest.json')
records=[]
for q, entries in manifest.items():
    print('\nHISTORY', q)
    for e in entries:
        p=PROJECT/e['path']
        data=p.read_bytes()
        record={**e,'complete_bytes_read':True}
        if p.suffix.lower() in ('.json','.txt','.log','.bin'):
            try:
                txt=data.decode('utf-8-sig')
                record['utf8_valid']=True
                if p.suffix=='.json':
                    obj=json.loads(txt)
                    record['json_valid']=True
                    if p.name.endswith('_response.json'):
                        print('FULL RAW RESPONSE',str(p.relative_to(BASE)))
                        for ch in obj.get('choices',[]): print(json.dumps(ch,ensure_ascii=False))
                    elif p.name in ('assessment.json','prescreen.json','prescreen_assessment.json','primary_prescreen.json','primary_math_audit.json','refinement_assessment.json','tiling_math_audit.json'):
                        print(str(p.relative_to(BASE)),json.dumps(obj,ensure_ascii=False))
                    elif p.name=='design.json':
                        print('DESIGN',str(p.relative_to(BASE)))
                        print(json.dumps({k:v for k,v in obj.items() if k not in ('marker_roles','overlay_bindings')},ensure_ascii=False))
                        for m in obj.get('marker_roles',[]): print('MARK',json.dumps(m,ensure_ascii=False))
                    elif ('incomplete' in p.name or 'abort' in p.name or 'error' in p.name):
                        print('ERROR/ABORT',str(p.relative_to(BASE)),txt)
            except (UnicodeDecodeError,json.JSONDecodeError) as err:
                record['malformed']=str(err)
                print('MALFORMED PRESERVED',record)
        records.append(record)
save('old_evidence_full_byte_read.json',records)

def narratives(obj, path=''):
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k in ('historical_relevant_source_comparisons','evidence','supporting_new_review_files','full_precision_geometry','all_choice_feature_comparison','reviewed_evidence_manifest','read_only_files','preservation','artifact_bindings','frozen_inputs','evidence_bindings'): continue
            yield from narratives(v,path+'/'+k)
    elif isinstance(obj,list):
        for i,v in enumerate(obj): yield from narratives(v,path+'/'+str(i))
    elif isinstance(obj,str) and (len(obj)>90 or path.split('/')[-1] in ('decision','reason','finding','code')) and not ('sha256' in path or ':\\' in obj or obj.startswith(('http','C:/'))):
        yield path,obj

for rel in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly','Plane263_v01','Plane192_v03','Plane233_two_U_partial_partition_binding','Solid220_false_face_pair']:
    p=BASE/'independent_review'/rel/'independent_review.json'
    print('\nCITED REVIEW',rel)
    for k,v in narratives(read(p)): print(k,v)

