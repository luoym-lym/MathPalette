from tools57 import *
import re
import gc
RELATED=['Solid112','Solid177']
ALL=IDS+RELATED
old={};textual=[];errors=[];sources={}
for p in sorted((PROJECT/'runtime').rglob('*')):
    if not p.is_file() or p.is_relative_to(HERE): continue
    names=[q for q in ALL if re.search(r'(^|[/\\])'+q+r'([/\\_.]|$)',str(p.relative_to(PROJECT/'runtime')))]
    if not names: continue
    b=p.read_bytes();item=dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),question_ids=names)
    if p.suffix.lower() in ['.json','.jsonl','.txt','.log','.py']:
        try:
            t=b.decode('utf-8-sig');item['complete_utf8_read']=True
            if p.suffix.lower()=='.json':
                j=json.loads(t)
                if p.name in ['design.json','assessment.json','primary_prescreen.json','prescreen.json','manual_final_review.json','visibility_skip_audit.json','primary_math_audit.json','history_audit.json'] or re.fullmatch(r'run_\d+(_response)?\.json',p.name):
                    textual.append(dict(path=str(p),sha256=item['sha256'],data=j))
            elif p.suffix.lower()=='.jsonl':
                for line in t.splitlines():
                    if line.strip(): json.loads(line)
        except (UnicodeDecodeError,json.JSONDecodeError) as e: item['malformed_preserved']=str(e);errors.append(item)
    old[str(p)]=item
write(HERE/'old_evidence_inventory.json',dict(created_at=now(),scope=ALL,files=old,malformed=errors,all_bytes_preserved=True))
write(HERE/'old_complete_relevant_records.json',textual)
# Read all complete source documents and retain exact question-local notes and geometry.
notes=read(PROJECT/'provenance/source_notes.json')
for q in IDS:
    d=HERE/q;d.mkdir(exist_ok=True)
    e=eligibility(q);write(d/'eligibility_assessment.json',e);assert e['eligible']
    if not (d/'source_hashes_initial.json').exists(): write(d/'source_hashes_initial.json',frozen_files(e['record']))
    if not (d/'formal_record.json').exists(): write(d/'formal_record.json',e['record'])
    docs={}
    for rel in [e['record']['scene'],e['record']['script'],*e['record']['runtime_dependencies']]:
        p=PROJECT/BRANCH/rel;b=p.read_bytes();t=b.decode('utf-8-sig')
        info=dict(sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),complete_utf8_read=True)
        if p.suffix=='.json':
            j=json.loads(t);info['top_level_keys']=list(j)
            if p.name in ['scene.json','source.json','protocol_review.json','execution.json']:
                docs[rel]=j
        sources[str(p)]=info
    write(d/'source_documents_full.json',docs)
    write(d/'source_notes.json',notes.get(q,{}))
    print(q,'source documents fully read / eligible / approval current',flush=True)
write(HERE/'source_read_receipts.json',sources)
references=['background_57_brief.txt','background_57_assignment.json','continuation_brief.txt','selection56_57_parent_eligibility.json','preparation56_57.json','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json']
reference_audit={p:dict(sha256=sha(BASE/p),full_utf8_read=True) for p in references if (BASE/p).read_text(encoding='utf-8-sig')}
for folder in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly']:
    p=BASE/'independent_review'/folder/'independent_review.json'
    if p.exists():
        j=read(p)
        reference_audit[str(p)]=dict(sha256=sha(p),full_json_read=True,decision=j.get('decision'),semantic_objections={k:v for k,v in j.items() if any(x in k.lower() for x in ['semanti','objection','blocking','reason','limit','decision'])})
for n in range(1,15):
    p=BASE/f'batch_{n:02d}'/'manifest.json'
    if p.exists():
        j=read(p);reference_audit[str(p)]=dict(sha256=sha(p),full_json_read=True)
write(HERE/'references_read_audit.json',reference_audit)
write(HERE/'offline_errors_initial.json',[
 dict(stage='initial repeated bridge adapter construction after Solid79/Solid214 success',error='MemoryError in catalog.validate_formal_row Path.read_text',api_calls=0,own_exec_session=99853,process_exited=True),
 dict(stage='separate Solid216 bridge initialization',error='MemoryError in catalog._source_notes_snapshot Path.read_bytes',api_calls=0,process_exited=True)])
print('old files',len(old),'important complete records',len(textual),'malformed preserved',len(errors),flush=True)
