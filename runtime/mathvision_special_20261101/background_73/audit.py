from bootstrap import HERE, TASK, PROJECT, renderer_setup
import json
import hashlib
import sys
import gc
import shutil
from datetime import datetime, timezone

IDS = ['Solid212','Solid222','Solid227','Solid235']
def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()
def save(path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8') as f:
        json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False)
        f.write('\n')
def stamp():
    return datetime.now(timezone.utc).isoformat()
def row(q):
    with (PROJECT/'SolidGeometry/dataset.jsonl').open(encoding='utf-8-sig') as f:
        for line in f:
            r=json.loads(line)
            if r['id']==q:
                return r
    raise ValueError(q)
def eligibility(q, name='eligibility_initial.json'):
    from dataset_tools.catalog import content, digest
    r=row(q)
    a=read(PROJECT/'provenance/approvals.json')['approvals'][q]
    c=content(PROJECT,'SolidGeometry',r)
    indices={}
    for filename in ('accepted_index.jsonl','collected_index.jsonl'):
        p=PROJECT/'SolidGeometry/special_variant'/filename
        entries=[]
        if p.exists():
            with p.open(encoding='utf-8-sig') as f:
                for line in f:
                    if line.strip():
                        entry=json.loads(line)
                        if entry.get('question_id',entry.get('id'))==q:
                            entries.append(entry)
        indices[filename]={'path':str(p),'sha256':sha(p) if p.exists() else None,'entries':entries}
    special={}
    for filename in ('recipes.json','collection.json'):
        p=PROJECT/'SolidGeometry/special_variant'/q/filename
        special[filename]={'path':str(p),'exists':p.exists(),'sha256':sha(p) if p.exists() else None}
    assignment=next(x for x in read(TASK/'background_73_assignment.json')['questions'] if x['question_id']==q)
    source_checks=[]
    for kind, item in assignment['source_assignment_question']['source_inputs'].items():
        from pathlib import Path
        p=Path(item['path'])
        source_checks.append({'kind':kind,**item,'actual_sha256':sha(p),'matches':sha(p)==item['sha256']})
    valid=(r['source_dataset']=='MathVision' and r==assignment['formal_record'] and digest(c)==a['content_sha256'] and a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and not any(v['entries'] for v in indices.values()) and not any(v['exists'] for v in special.values()) and all(x['matches'] for x in source_checks))
    result={'question_id':q,'created_at':stamp(),'eligible':valid,'approval':a,'computed_content_sha256':digest(c),'content':c,'indices':indices,'special_records':special,'source_checks':source_checks}
    save(HERE/q/name,result)
    assert valid, q+' current eligibility/source/approval failed'
    return result

def initial():
    protocol_paths=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
    task_paths=['background_73_brief.txt','background_73_assignment.json','background_61_brief.txt','background_61_assignment.json','continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','selection60_61_parent_eligibility.json','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json','delivery_bridge_adapter.py','runtime_isolation.py','harness/quicktest3_isolated.py']
    manifest=[]
    for p in [PROJECT/x for x in protocol_paths]+[TASK/x for x in task_paths]:
        target=HERE/'snapshots'/str(p.relative_to(PROJECT)).replace('\\','__').replace('/','__')
        target.parent.mkdir(parents=True,exist_ok=True)
        data=p.read_bytes()
        target.write_bytes(data)
        manifest.append({'path':str(p),'snapshot':str(target),'sha256':sha(p),'size':len(data),'complete_utf8_read':bool(data.decode('utf-8-sig'))})
        del data
    a61=read(TASK/'background_61_assignment.json')
    a73=read(TASK/'background_73_assignment.json')
    print('original assignment keys:',list(a61))
    print('scope source key comparison:')
    comparisons=[]
    for q in IDS:
        x=next(v for v in a61['questions'] if v['question_id']==q)
        y=next(v for v in a73['questions'] if v['question_id']==q)['source_assignment_question']
        comparisons.append({'question_id':q,'source_assignment_exact_equal':x==y,'source_keys':list(x)})
    save(HERE/'assignment_full_read_audit.json',{'complete_original_assignment_loaded':True,'full_snapshot_saved':True,'comparisons':comparisons,'current_scope':IDS,'other_source_ids_read_for_context_only':a61.get('question_ids')})
    for p in [TASK/'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',TASK/'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']:
        target=HERE/'snapshots'/str(p.relative_to(PROJECT)).replace('\\','__').replace('/','__')
        target.write_bytes(p.read_bytes())
        manifest.append({'path':str(p),'snapshot':str(target),'sha256':sha(p),'size':p.stat().st_size})
    save(HERE/'snapshot_manifest_initial.json',manifest)
    frozen=[]
    for q in IDS:
        e=eligibility(q)
        save(HERE/q/'formal_record.json',row(q))
        for rel,hashvalue in e['content']['files'].items():
            frozen.append({'path':str((PROJECT/'SolidGeometry'/rel).resolve()),'sha256':hashvalue})
        print(q,'CURRENT eligibility and approval/source hash pass')
    save(HERE/'frozen_sources_initial.json',frozen)
    save(HERE/'environment_audit.json',{'time':stamp(),'python':sys.version,'executable':sys.executable,'argv':sys.argv,'strict_guard_root':str(HERE),'environment':{k:__import__('os').environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},'remote_calls':0,'provider_model_options_overridden':False})

def history(q):
    assert q in IDS
    files=[]
    for p in TASK.rglob('*'):
        if p.is_file() and not p.is_relative_to(HERE) and q in p.parts and p.suffix.lower() in ('.json','.png','.jpg','.txt','.log','.bin','.py'):
            files.append({'path':str(p),'sha256':sha(p),'size':p.stat().st_size})
    save(HERE/q/'old_evidence_manifest.json',files)
    import base64
    from pathlib import Path
    full=[]
    requests=[]
    for item in files:
        p=Path(item['path'])
        if p.suffix!='.json':
            continue
        data=read(p)
        if p.name=='request.json':
            # Keep full hash-bound request immutable; expose safe shape only.
            requests.append({'path':str(p),'sha256':item['sha256'],'top_keys':list(data),'question_id':q})
        elif p.name.endswith('_response.json') or ('review' in p.name and 'context' not in p.name) or p.name in ('design.json','design_difference_audit.json','plugin.json','summary.json','binding.json','offline_failure_01.json','noop_check.json'):
            full.append({'path':str(p),'sha256':item['sha256'],'content':data})
        del data
        gc.collect()
    save(HERE/q/'history_full_relevant.json',full)
    save(HERE/q/'old_request_audit.json',requests)
    print(q,'all',len(files),'old files hashed; relevant JSONs read',len(full),'requests',len(requests))
    print('RAW FILES')
    for entry in full:
        if entry['path'].endswith('_response.json'):
            data=entry['content']
            print(entry['path'])
            print(json.dumps(data,ensure_ascii=False))

def inspect(q):
    assert q in IDS
    renderer_setup()
    from delivery_bridge_adapter import RendererAdapter
    from renderer_adapter import scene_png
    import matplotlib.pyplot as plt
    adapter=RendererAdapter({'dataset_file':str(PROJECT/'SolidGeometry/dataset.jsonl')})
    c=adapter.inspect_question(q)
    save(HERE/q/'context_fresh.json',c)
    scene=adapter.scene(q)
    try:
        png,pix=scene_png(scene)
        (HERE/q/'noop.png').write_bytes(png)
        save(HERE/q/'noop_check.json',{'pixel_sha256':pix,'formal_pixel_sha256':c['original_pixel_sha256'],'matches':pix==c['original_pixel_sha256'],'png_sha256':sha(HERE/q/'noop.png')})
    finally:
        scene.close()
        plt.close('all')
    print(q,'fresh native context/no-op pass',pix==c['original_pixel_sha256'])

if __name__=='__main__':
    action=sys.argv[1]
    if action=='initial':initial()
    elif action=='history':history(sys.argv[2])
    elif action=='inspect':inspect(sys.argv[2])
    elif action=='eligibility':eligibility(sys.argv[2],sys.argv[3])
