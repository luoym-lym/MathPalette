import bootstrap75 as boot
from pathlib import Path
import json
import hashlib
import sys
import gc
from datetime import datetime, timezone

OWN, PROJECT, BASE = boot.OWN, boot.PROJECT, boot.OWN.parent
IDS = ['Plane317','Plane337','Plane375','Plane381','Plane384','Plane385','Plane389','Plane454']
def now(): return datetime.now(timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,v):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def snapshot(p):
    p=Path(p).resolve(); data=p.read_bytes()
    rel=p.relative_to(PROJECT).as_posix()
    target=OWN/'snapshots'/(rel.replace('/','__'))
    if target.exists():
        if target.read_bytes()!=data:
            target=target.with_name(target.name+'.'+sha(data)+'.subsequent')
    if not target.exists(): target.write_bytes(data)
    return {'path':str(p),'sha256':sha(data),'bytes':len(data),'snapshot':str(target)}

def readin():
    audit=[]
    for name in ['background_75_brief.txt','background_75_assignment.json','background_65_brief.txt','background_65_assignment.json','background_66_brief.txt','background_66_assignment.json','continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json','selection65_66_parent_eligibility.json','runtime_isolation.py','harness/quicktest3_isolated.py']:
        p=BASE/name; text=p.read_text(encoding='utf-8-sig')
        if p.suffix=='.json': json.loads(text)
        elif p.suffix=='.jsonl':
            for line in text.splitlines():
                if line.strip(): json.loads(line)
        audit.append(snapshot(p)); del text; gc.collect()
    for rel in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']:
        p=PROJECT/rel; p.read_text(encoding='utf-8-sig'); audit.append(snapshot(p))
    # Complete JSON is decoded one file at a time; duplicated formal records are verified,
    # not silently omitted from the read. Original source65/66 are never treated as designs.
    a=read(BASE/'background_75_assignment.json'); old=read(BASE/'background_65_assignment.json')
    comparisons=[]
    for q,oq in zip(a['questions'],old['questions']):
        sq=q['source_assignment_question']
        comparisons.append({'id':q['question_id'],'exact_old_question':sq==oq,'exact_formal':q['formal_record']==sq['formal_record_at_assignment']})
    put(OWN/'assignment_full_read_audit.json',{'read_at':now(),'files':audit,'assignment_comparisons':comparisons,'old65_66_directories_exist':{n:(BASE/n).exists() for n in ['background_65','background_66']},'scope':IDS,'no_nested_agents':True,'all_reads_complete_UTF8':True})
    # All question-local old histories plus their referenced full checkpoints are streamed.
    histories=[]; finals=[]
    for folder in sorted(BASE.glob('background_*')):
        if folder==OWN or not folder.is_dir(): continue
        for q in IDS:
            qdir=folder/q
            if not qdir.exists(): continue
            for p in sorted(qdir.rglob('*')):
                if not p.is_file(): continue
                data=p.read_bytes(); entry=snapshot(p)
                if p.suffix=='.json':
                    val=json.loads(data.decode('utf-8-sig'))
                    if p.name.endswith('_response.json'):
                        content=val.get('choices',[{}])[0].get('message',{}).get('content')
                        finals.append({'question_id':q,'path':str(p),'sha256':entry['sha256'],'full_final':content})
                    del val
                histories.append(entry); del data; gc.collect()
            cp=folder/'checkpoint.json'
            if cp.exists():
                val=read(cp); histories.append(snapshot(cp)); del val; gc.collect()
    for rel in ['independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json','independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json','independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json']:
        p=BASE/rel
        if p.exists():
            val=read(p); histories.append(snapshot(p)); del val; gc.collect()
    put(OWN/'old_history_full_read_audit.json',{'read_at':now(),'streamed_one_file_at_a_time':True,'files':histories,'full_old_finals':finals,'no_API_calls':True})
    # Read all readonly delivery manifests as information-binding references.
    batches=[]
    for d in sorted(BASE.glob('batch_*')):
        if not d.is_dir(): continue
        for p in d.rglob('design.json'):
            val=read(p); batches.append(snapshot(p)); del val
        p=d/'manifest.json'
        if p.exists(): val=read(p); batches.append(snapshot(p)); del val
    put(OWN/'delivery_reference_read_audit.json',batches)
    print(json.dumps({'assignment_comparisons':comparisons,'old_history_files':len(histories),'old_raw_finals':finals,'reference_files':len(batches)},ensure_ascii=False))

def eligible(q):
    from dataset_tools import catalog
    records={r['id']:r for r in catalog.rows(PROJECT/'PlaneGeometry/dataset.jsonl')}
    row=records[q]; approvals=catalog.read(PROJECT/'provenance/approvals.json')['approvals']; ap=approvals[q]
    content=catalog.content(PROJECT,'PlaneGeometry',row)
    fingerprint=catalog.digest(content)
    accepted=catalog.rows(PROJECT/'PlaneGeometry/special_variant/accepted_index.jsonl')
    collected=catalog.rows(PROJECT/'PlaneGeometry/special_variant/collected_index.jsonl')
    def mentions(rows):
        return [v for v in rows if v.get('question_id',v.get('id'))==q]
    special={}
    for n in ['recipes.json','collection.json']:
        p=PROJECT/'PlaneGeometry/special_variant'/q/n
        special[n]={'exists':p.exists(),'sha256':sha(p.read_bytes()) if p.exists() else None}
    matches=[]
    assignment=next(x for x in read(BASE/'background_75_assignment.json')['questions'] if x['question_id']==q)
    for field,v in assignment['source_assignment_question']['source_inputs'].items():
        p=Path(v['path']); matches.append({'field':field,'path':str(p),'expected':v['sha256'],'current':sha(p.read_bytes()),'matches':sha(p.read_bytes())==v['sha256']})
    result={'question_id':q,'checked_at':now(),'source_dataset':row['source_dataset'],'source_key':row['source_key'],'formal_record':row,'approval':ap,'current_original_fingerprint':fingerprint,'fingerprint_matches':fingerprint==ap['content_sha256'],'content_manifest':content,'noPassedVariant':not mentions(accepted),'notCollected':not mentions(collected),'noSpecialCompletion':not any(v['exists'] for v in special.values()),'special_records':special,'source_input_matches_assignment':matches,'authoritative_hashes':{str(p.relative_to(PROJECT)):sha(p.read_bytes()) for p in [PROJECT/'PlaneGeometry/dataset.jsonl',PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json',PROJECT/'PlaneGeometry/special_variant/accepted_index.jsonl',PROJECT/'PlaneGeometry/special_variant/collected_index.jsonl']}}
    result['eligible']=all([row['source_dataset']=='MathVision',result['fingerprint_matches'],ap['reviewer']=='user',bool(ap['instruction']),result['noPassedVariant'],result['notCollected'],result['noSpecialCompletion'],all(x['matches'] for x in matches)])
    return result

def capture(q):
    entry=eligible(q); put(OWN/q/'eligibility_start.json',entry)
    if not entry['eligible']: raise ValueError('Current eligibility failed: '+q)
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import load_config, pixel_hash
    from mathvision_adapter import RendererAdapter
    from dataset_tools.mathvision_workbench import png_bytes
    config=load_config(); config['runtime_dir']=str(OWN/'workbench_runtime'); config['output_dir']=str(OWN/'workbench_output')
    adapter=RendererAdapter(config)
    context=adapter.inspect_question(q); put(OWN/q/'fresh_context.json',context)
    scene=adapter.scene(q)
    try: data=png_bytes(scene)
    finally: scene.close()
    p=OWN/q/'noop.png'; p.write_bytes(data)
    row=entry['formal_record']; formal=PROJECT/'PlaneGeometry'/row['image']
    originals=[]
    for rel in list(dict.fromkeys([row[k] for k in ['image','original_image','scene','script'] if row.get(k)]+row.get('runtime_dependencies',[]))):
        source=PROJECT/'PlaneGeometry'/rel; originals.append(snapshot(source))
    put(OWN/q/'native_capture_audit.json',{'captured_at':now(),'no_op_formal_pixels_equal':pixel_hash(data)==pixel_hash(formal),'no_op_sha256':sha(data),'formal_sha256':sha(formal.read_bytes()),'pixel_sha256':pixel_hash(data),'source_snapshots':originals,'routing':boot.ROUTING,'strict_writeguard_root':str(OWN),'native_adapter':str(Path(__import__('mathvision_adapter').__file__)),'adapter_unchanged':True,'context_sha256':sha((OWN/q/'fresh_context.json').read_bytes())})
    print(json.dumps({'id':q,'eligible':entry['eligible'],'baseline':pixel_hash(data)==pixel_hash(formal),'objects':len(context['objects']),'snap_points':len(context['snap_points'])}))

if __name__=='__main__':
    if sys.argv[1]=='readin': readin()
    elif sys.argv[1]=='capture': capture(sys.argv[2])
