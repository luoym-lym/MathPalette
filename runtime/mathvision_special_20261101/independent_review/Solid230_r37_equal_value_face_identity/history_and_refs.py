from review_env import *
import struct
import zlib

def compact_ref(path):
    obj=read(path)
    keys=['question_id','variant_id','decision','correct_answer','unique_original_answer','mathematical_answer','blocking_reason','concrete_objections','limitations','limits','primary_proof_corrections','scope','annotation_semantics','human_unambiguity','human_clarity','native_visual_review','decision_reason','reason','rationale']
    return {'path':str(path),'sha256':fh(path),'all_top_level_keys':list(obj),'selected_complete_fields':{k:obj[k] for k in keys if k in obj}}
refs=[]
for folder in (SHARED/'independent_review').iterdir():
    if any(x in folder.name for x in ['Solid128','Solid197','Plane192','Plane233','Plane242']):
        p=folder/'independent_review.json'
        if p.is_file():refs.append(compact_ref(p))
for q in ['Solid197','Plane192','Plane233']:
    p=SHARED/'batch_12'/q/'independent_review.json'
    if p.is_file():refs.append(compact_ref(p))
write('reference_review_receipt.json',{'at':now(),'reviews':refs,
    'annotation_lesson':read(SHARED/'annotation_semantics_lesson_plane242_r24_20261102.json'),
    'applies_to_this_task':'Paper-edge ink incompatibility is task-specific. Solid230 asks a dot count, not a resulting color picture after moving physical papers; coloring two existing die edges does not change visible dot counts whether regarded as ink or emphasis. No blanket color prohibition adopted.'})
for ref in refs:
    print('REFERENCE '+str(ref['path']))
    fields=ref['selected_complete_fields']
    print(json.dumps({k:v for k,v in fields.items() if k not in ['concrete_objections','primary_proof_corrections','native_visual_review','blocking_reason']},ensure_ascii=False))

def chunks(path):
    data=Path(path).read_bytes();i=8;result=[];idat=[]
    while i<len(data):
        size=struct.unpack('>I',data[i:i+4])[0];typ=data[i+4:i+8].decode('ascii');body=data[i+8:i+8+size]
        item={'type':typ,'size':size,'sha256':sha(body)}
        if typ in ['tEXt','pHYs']:item['data_repr']=repr(body)
        if typ=='IDAT':idat.append(body)
        result.append(item);i+=size+12
    return {'chunks':result,'inflated_IDAT_sha256':sha(zlib.decompress(b''.join(idat)))}
formal=ROOT/'SolidGeometry/image/Solid230.png';noop=OWN/'independent_noop.png'
png={'formal':chunks(formal),'noop':chunks(noop),'note':'No-op raw RGBA pixel hash matches exactly. Byte identity of original PNG container is not required by no-op protocol. Candidate replay matches tested PNG bytes exactly.'}
write('noop_png_container_audit.json',png)
print('NOOP_CONTAINER '+json.dumps(png,ensure_ascii=False))

# Enumerate actual persisted Solid230 paths to check for extra variants/calls.
found=[]
for folder in SHARED.rglob('Solid230'):
    if folder.is_dir():
        files=[p for p in folder.rglob('*') if p.is_file()]
        found.append({'directory':str(folder),'file_count':len(files),
            'designs':[str(p) for p in files if p.name=='design.json'],
            'started_calls':[str(p) for p in files if p.name.endswith('_started.json')],
            'response_files':[str(p) for p in files if p.name.endswith('_response.json')],
            'incomplete_or_error_files':[str(p) for p in files if any(s in p.name for s in ['incomplete','error','abort'])]})
history=read(OWN/'history_primary_exact_excerpts.json')
write('attempt_inventory.json',{'at':now(),'directories':found,'prior_exact_evidence':history,
    'old_background13_files':{str(p.relative_to(SHARED/'background_13/Solid230')):fh(p) for p in (SHARED/'background_13/Solid230').rglob('*') if p.is_file()},
    'finding':'Background13 screened_no_clean_hypothesis, six snapshot/context files, no design or calls. Exactly one new variant and two completed calls under background37. No original controls, errors, retries, aborted calls, or misses for Solid230 were found in its preserved directories. Other questions\u2019 controls/misses are not evidence for Solid230.'})
print('ATTEMPT_INVENTORY '+json.dumps(found,ensure_ascii=False))

protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
write('protocol_receipt.json',{'at':now(),'full_protocols_read':[{'path':str(ROOT/p),'sha256':fh(ROOT/p),'utf8_characters':len((ROOT/p).read_text(encoding='utf-8-sig'))} for p in protocols],
    'brief':{'path':str(SHARED/'Solid230_r37_equal_value_face_identity_independent_review_brief.txt'),'sha256':fh(SHARED/'Solid230_r37_equal_value_face_identity_independent_review_brief.txt')},
    'scope':'Only assigned fresh review directory is writable. No child agents, threads, worktrees, API calls, retries, controls, design changes, approvals, Pass/Collect, or formal writes.'})
print('PID '+str(os.getpid()))
