from review_env import *
import struct, zlib
from PIL import Image
from dataset_tools.catalog import rows, content, digest
BASE=ROOT/'runtime/mathvision_special_20261101';BRANCH=ROOT/'SolidGeometry'
baseline=read(OUT/'read_only_inputs_before.json')
comparison={p:{'before_sha256':v['sha256'],'after_sha256':sha(ROOT/p),'byte_identical':sha(ROOT/p)==v['sha256'],'mtime_identical':(ROOT/p).stat().st_mtime_ns==v['mtime_ns']} for p,v in baseline['files'].items()}
row=next(r for r in rows(BRANCH/'dataset.jsonl') if r['id']=='Solid126')
paths=[row[k] for k in ('image','original_image','script','scene') if row.get(k)] +row['runtime_dependencies']+['dataset_generator/common_renderer.py','dataset_generator/protocol.json']
independent_content={'branch':'SolidGeometry','record':row,'files':{p:sha(BRANCH/p) for p in paths},'source_notes':read(ROOT/'provenance/source_notes.json').get('Solid126',{})}
independent_content['files']['../dataset_tools/geometry_dataset.py']=sha(ROOT/'dataset_tools/geometry_dataset.py')
independent_fingerprint=hashlib.sha256(json.dumps(independent_content,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
approval=read(ROOT/'provenance/approvals.json')['approvals']['Solid126']
idx={name:{'sha256':sha(BRANCH/'special_variant'/name),'matching_records':[r for r in rows(BRANCH/'special_variant'/name) if r.get('id')=='Solid126' or r.get('question_id')=='Solid126']} for name in ('accepted_index.jsonl','collected_index.jsonl')}
delivered=[]
manifests={}
for p in BASE.glob('batch_*/manifest.json'):
    records=read(p)
    matches=[x for x in records.get('candidates',[]) if x.get('question_id')=='Solid126']
    manifests[str(p.relative_to(ROOT))]={'sha256':sha(p),'Solid126_entries':matches}
    if matches:delivered.append(str(p))
special_paths={str(BRANCH/'special_variant/Solid126'/name):{'exists':(BRANCH/'special_variant/Solid126'/name).exists()} for name in ('recipes.json','collection.json')}
eligibility={'checked_at':stamp(),'source_dataset':row['source_dataset'],'source_key':row['source_key'],'approval':approval,'independent_manual_content_sha256':independent_fingerprint,'catalog_content_sha256':digest(content(ROOT,'SolidGeometry',row)),'manual_content_equals_catalog':independent_content==content(ROOT,'SolidGeometry',row),'approval_matches_current':independent_fingerprint==approval['content_sha256'],'indexes':idx,'special_paths':special_paths,'special_directory_exists':(BRANCH/'special_variant/Solid126').exists(),'all_existing_batch_manifest_checks':manifests,'delivered_manifests_with_this_question':delivered}
eligibility['eligible']=row['source_dataset']=='MathVision' and eligibility['approval_matches_current'] and all(not v['matching_records'] for v in idx.values()) and all(not v['exists'] for v in special_paths.values()) and not delivered
def chunks(path):
    raw=Path(path).read_bytes();pos=8;out=[]
    while pos<len(raw):
        size=struct.unpack('>I',raw[pos:pos+4])[0];kind=raw[pos+4:pos+8].decode();data=raw[pos+8:pos+8+size]
        out.append({'kind':kind,'data_sha256':hashlib.sha256(data).hexdigest(),'size':size,'text':data.decode('latin1') if kind=='tEXt' else None});pos+=12+size
    return out
formalchunks=chunks(BRANCH/'image/Solid126.png');replaychunks=chunks(OUT/'baseline_reproduced.png')
pngmeta={'formal_chunks':formalchunks,'no_op_replay_chunks':replaychunks,'all_chunks_except_text_identical':[{k:v for k,v in x.items() if k!='text'} for x in formalchunks if x['kind']!='tEXt']==[{k:v for k,v in x.items() if k!='text'} for x in replaychunks if x['kind']!='tEXt']}
late_paths=[BASE/'background_37'/name for name in ('tools37.py','design37.py','review37.py','quality37.py','old_history_audit.json','source_and_history_audit_final.json','delivered_reference_study.json','artifact_manifest.json')]+[BASE/'background_14/primary_math_audit.json']
late={str(p.relative_to(ROOT)):{'sha256':sha(p),'size':p.stat().st_size} for p in late_paths}
history=read(BASE/'background_37/old_history_audit.json')
def select(x):
    if isinstance(x,dict):
        if x.get('question_id')=='Solid126':return x
        return {k:select(v) for k,v in x.items() if k=='Solid126' or (isinstance(v,(dict,list)) and 'Solid126' in json.dumps(v,ensure_ascii=False))}
    if isinstance(x,list):return [select(v) for v in x if isinstance(v,(dict,list)) and 'Solid126' in json.dumps(v,ensure_ascii=False)]
    return x
save('additional_read_only_sources.json',{'checked_at':stamp(),'files':late,'scope':'These additional sources were read after the initial baseline snapshot; not represented as initially snapshotted.'})
save('selected_old_history_audit.json',select(history))
save('source_preservation_and_final_eligibility.json',{'checked_at':stamp(),'pid':os.getpid(),'tracked_input_count':len(comparison),'all_initially_tracked_bytes_unchanged':all(v['byte_identical'] for v in comparison.values()),'all_initially_tracked_mtimes_unchanged':all(v['mtime_identical'] for v in comparison.values()),'changes':[p for p,v in comparison.items() if not v['byte_identical']],'comparisons':comparison,'final_authoritative_eligibility':eligibility,'baseline_png_metadata_difference':pngmeta,'isolation':ISOLATION,'blocked':BLOCKED,'all_input_images':{str(p):{'sha256':sha(p),'size':list(Image.open(p).size)} for p in [BRANCH/'originals/Solid126.jpg',BRANCH/'image/Solid126.png',BASE/'background_37/Solid126/r37_local_area_replacement/candidate.png',BASE/'background_14/Solid126/remaining_height_to_cut_binding/candidate.png']}})
print(json.dumps({'pid':os.getpid(),'tracked_input_count':len(comparison),'changed_inputs':[p for p,v in comparison.items() if not v['byte_identical']],'all_mtimes_unchanged':all(v['mtime_identical'] for v in comparison.values()),'eligible':eligibility['eligible'],'approval_fingerprint':independent_fingerprint,'all_chunks_except_text_identical':pngmeta['all_chunks_except_text_identical'],'text_metadata':[[x for x in z if x['kind']=='tEXt'] for z in (formalchunks,replaychunks)],'old_history':select(history),'blocked':BLOCKED},ensure_ascii=False,indent=2))
