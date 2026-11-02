from env59 import *
import gc

def prose(value,path=''):
    if isinstance(value,dict):
        return {k:prose(v,path+'.'+k) for k,v in value.items() if not any(s in k.lower() for s in ('sha256','hashes','timestamps_and_immutable','files_checked','reviewed_source_evidence','source_preservation','preservation_checks','frozen_input','fingerprint','artifact_hash','input_files'))}
    if isinstance(value,list): return [prose(v,path) for v in value]
    return value

reports=['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly','Plane263_v01','Plane192_v03','Solid220_false_face_pair']
items=[]
for folder in reports:
    p=BASE/'independent_review'/folder/'independent_review.json'
    if not p.exists(): continue
    value=read(p)
    items.append({'path':str(p),'sha256':sha(p),'full_byte_and_JSON_read':True,'decision':value.get('decision'),'report':prose(value)})
    del value
    gc.collect()
save('cited_rejection_readings.json',items)
batch=[]
for p in sorted(BASE.glob('batch_*/manifest.json')):
    value=read(p)
    batch.append({'path':str(p),'sha256':sha(p),'full_read':True,'manifest':prose(value)})
    del value
    gc.collect()
save('delivered_reference_readings.json',batch)
print('Rejection reports',len(items),'delivered manifests',len(batch))
for item in items:
    rep=item['report']
    print('\nREPORT',item['path'])
    for key in ('decision','reason','concrete_objections','blocking_reason','information_targeting','marker_necessity','every_marker_review','annotation_semantics','human_semantics','why_not_recommended','mark_information_review','verdict','summary','concerns'):
        if key in rep: print(key,json.dumps(rep[key],ensure_ascii=False))
for item in batch:
    print('\nBATCH',Path(item['path']).parent.name,json.dumps(item['manifest'],ensure_ascii=False))
