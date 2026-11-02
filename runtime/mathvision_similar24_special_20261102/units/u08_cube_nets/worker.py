from pathlib import Path
import os
import sys

OWN = Path(__file__).resolve().parent
PROJECT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = OWN.parent.parent
OLD = PROJECT / 'runtime/mathvision_special_20261101'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[k] = '1'
for k in ('TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME'):
    os.environ[k] = str(OWN / 'cache' / k)
    Path(os.environ[k]).mkdir(parents=True, exist_ok=True)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.dont_write_bytecode = True

def check_write(path):
    if path is None or isinstance(path,int):
        return
    p = Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(OWN):
        raise PermissionError('Strict own_root writeguard: ' + str(p))

def guard(event,args):
    if event == 'open':
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
            check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
sys.addaudithook(guard)
sys.path[:0] = [str(PROJECT),str(OLD),str(PROJECT/'SolidGeometry/workbench')]
import runtime_isolation
ISOLATION = runtime_isolation.install(OWN/'cache/bridge')
import json
import hashlib
from datetime import datetime, timezone

def now(): return datetime.now(timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def save(p,d):
    p=Path(p); check_write(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

ASSIGN=read(OWN/'assignment.json')
QIDS=ASSIGN['question_ids']

def checkpoint(status='in_progress', **kw):
    p=OWN/'checkpoint.json'
    d=read(p) if p.exists() else {'unit_id':ASSIGN['unit_id'],'question_ids':QIDS,'questions':{q:{'status':'not_yet_assessed'} for q in QIDS},'actual_new_api_calls':0,'formal_changes':0,'primary_only':True}
    d.update(status=status,updated_at=now(),**kw);save(p,d)
    if not (OWN/'second_review_queue.json').exists():save(OWN/'second_review_queue.json',[])

def audit():
    checkpoint()
    initial={n:sha(OWN/n) for n in ('brief.txt','assignment.json')}
    save(OWN/'scope_original_bytes.json',initial)
    d=read(TASK/'history_index.json')
    refs=[]
    for p in (TASK/'references').rglob('*'):
        if p.is_file():
            if p.suffix=='.json':read(p)
            refs.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
    save(OWN/'reference_read_ledger.json',refs)
    ledger=[]
    for q in d['questions']:
        if q['question_id'] not in QIDS:continue
        files=set(q['other_scoped_history_file_references'])
        for key in ('independent_review_references','additional_math_manual_history_references'):
            for f in q[key]:
                if isinstance(f,str):files.add(f)
                elif 'path' in f:files.add(f['path'])
        for design in q['designs']:
            files.add(design['design_path']);files.add(design['plugin_path'])
            for p in (PROJECT/design['directory']).rglob('*'):
                if p.is_file():files.add(str(p.relative_to(PROJECT)).replace('\\','/'))
        for f in sorted(files):
            p=PROJECT/f
            if not p.is_file():continue
            entry={'question_id':q['question_id'],'path':f,'sha256':sha(p),'bytes':p.stat().st_size}
            if p.suffix=='.json':
                try:
                    v=read(p)
                    # Parse each actual complete document separately, release request images immediately.
                    if p.name.endswith('_response.json'):
                        entry['response']=v
                    elif p.name=='design.json' or 'review' in p.name or 'proof' in p.name:
                        entry['document']=v
                    elif p.name=='request.json':
                        entry['request_parsed']=True
                except Exception as e:entry['parse_error']=str(e)
            ledger.append(entry)
    save(OWN/'history_actual_files_read.json',ledger)
    save(OWN/'history_scope_index.json',[q for q in d['questions'] if q['question_id'] in QIDS])
    print(json.dumps({'read_history_files':len(ledger),'references':len(refs),'scope_hashes':initial},ensure_ascii=False))

def eligibility(qid,where):
    from dataset_tools.catalog import rows, content, digest
    branch=PROJECT/'SolidGeometry'
    record=next(x for x in rows(branch/'dataset.jsonl') if x['id']==qid)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    current=digest(content(PROJECT,'SolidGeometry',record))
    sv=branch/'special_variant'
    accepted=[];collected=[]
    for fn,result in [('accepted_index.jsonl',accepted),('collected_index.jsonl',collected)]:
        p=sv/fn
        if p.exists():
            for line in p.read_text(encoding='utf-8-sig').splitlines():
                if line.strip():
                    r=json.loads(line)
                    if r.get('question_id',r.get('id'))==qid:result.append(r)
    recipes=read(sv/qid/'recipes.json') if (sv/qid/'recipes.json').exists() else []
    collection=read(sv/qid/'collection.json') if (sv/qid/'collection.json').exists() else None
    assigned=next(x for x in ASSIGN['questions'] if x['question_id']==qid)
    checked={p:{'expected':h,'actual':sha(PROJECT/p)} for p,h in assigned['frozen_source_files_sha256'].items()}
    ok=(record==assigned['formal_record'] and record['source_dataset']=='MathVision' and current==approval['content_sha256']==assigned['current_content_sha256'] and not accepted and not collected and not recipes and collection is None and all(v['expected']==v['actual'] for v in checked.values()))
    result={'checked_at':now(),'eligible':ok,'record':record,'approval':approval,'current_content_sha256':current,'source_checks':checked,'accepted':accepted,'collected':collected,'recipes':recipes,'collection':collection}
    save(where,result)
    if not ok:raise RuntimeError(qid+' current eligibility/source differs')
    return result

def renderer(qid):
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    from workbench_io import load_config
    config=load_config()
    adapter=RendererAdapter(config)
    context=adapter.inspect_question(qid)
    return adapter,PluginRenderer(config,adapter,{qid:context}),context

def setup():
    from partial_style import object_paths
    from renderer_adapter import scene_png
    from workbench_io import environment_versions
    for qid in QIDS:
        d=OWN/qid;d.mkdir(exist_ok=True)
        eligibility(qid,d/'eligibility_initial.json')
        adapter,pr,context=renderer(qid)
        scene=adapter.scene(qid)
        try:
            png,digest=scene_png(scene)
            (d/'noop.png').write_bytes(png)
            assert digest==context['original_pixel_sha256']
            paths={o['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,o['id'])] for o in context['objects'] if o.get('styleable')}
            save(d/'paths.json',paths)
        finally:scene.close()
        save(d/'context.json',context)
        assigned=next(x for x in ASSIGN['questions'] if x['question_id']==qid)
        native=PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/qid/'scene.json'
        save(d/'source_scene_snapshot.json',read(native))
        save(d/'environment.json',{'versions':environment_versions(),'cache':{k:os.environ[k] for k in ('TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},'isolation':ISOLATION,'strict_writeguard':str(OWN),'pid':os.getpid()})
        print(qid,len(context['objects']),len(paths),digest,flush=True)

def render_candidate(qid,variant,replay=False):
    from render_plugins import check_schema
    from workbench_io import environment_versions,pixel_hash
    d=OWN/qid/variant
    eligibility(qid,d/('eligibility_replay.json' if replay else 'eligibility_before_render.json'))
    adapter,pr,context=renderer(qid)
    saved=read(OWN/qid/'context.json')
    assert json.loads(json.dumps(context))==saved,'Fresh context changed'
    plugin=read(d/'plugin.json')
    check_schema(plugin,pr.schema,pr.schema)
    normal=pr.normalize(plugin)
    assert pr.normalize(normal)==normal
    n1,b1,p1=pr.render(normal);n2,b2,p2=pr.render(normal)
    assert n1==n2==normal and b1==b2 and p1==p2
    h=hashlib.sha256(b1).hexdigest()
    if replay:
        assert b1==(d/'candidate.png').read_bytes(),'Independent replay differs'
    else:
        (d/'candidate.png').write_bytes(b1)
        save(d/'normalized_plugin.json',normal)
    # Reject any previous actual image for this formal question; compare pixels too.
    old=next(q for q in read(OWN/'history_scope_index.json') if q['question_id']==qid)
    collisions=[]
    for x in old['designs']:
        path=x.get('frozen_candidate_png_path')
        if path and (PROJECT/path).is_file():
            if sha(PROJECT/path)==h or pixel_hash(PROJECT/path)==p1:collisions.append(path)
    assert not collisions,'Old tested PNG/pixels collision'
    report={'created_at':now(),'qid':qid,'variant':variant,'fresh_schema_check':True,'normalization_idempotent':True,'fresh_context_exact_JSON_normalization_equal':True,'original_noop_pixel_match':context['original_pixel_sha256'],'same_process_two_renders_byte_equal':True,'independent_process_replay':replay,'png_sha256':h,'pixel_sha256':p1,'plugin_sha256':sha(d/'plugin.json'),'normalized_plugin_sha256':sha(d/'normalized_plugin.json'),'design_sha256':sha(d/'design.json'),'source_context_sha256':sha(OWN/qid/'context.json'),'schema_sha256':sha(PROJECT/'SolidGeometry/workbench/plugin.schema.json'),'adapter_sha256':sha(OLD/'delivery_bridge_adapter.py'),'renderer_sha256':sha(PROJECT/'SolidGeometry/workbench/render_plugins.py'),'appearance_changes':pr.appearance_changes(normal),'environment':environment_versions(),'old_question_hash_pixel_collisions':collisions}
    save(d/('independent_replay.json' if replay else 'render_gates.json'),report)
    print(qid,variant,'replay' if replay else 'render',h,flush=True)

def copy_harness():
    import difflib
    src=OLD/'harness/quicktest3_isolated.py';data=src.read_bytes()
    old=b'PROJECT = Path(__file__).resolve().parents[3]'
    new=('PROJECT = Path('+repr(str(PROJECT))+')').encode('utf-8')
    assert data.count(old)==1
    changed=data.replace(old,new)
    assert changed.replace(new,old)==data
    d=OWN/'harness';d.mkdir(exist_ok=True)
    dst=d/'quicktest3_isolated.py';dst.write_bytes(changed)
    diff=''.join(difflib.unified_diff(data.decode().splitlines(True),changed.decode().splitlines(True),fromfile=str(src),tofile=str(dst)))
    (d/'exact.diff').write_text(diff,encoding='utf-8')
    save(d/'copy_audit.json',{'source':str(src),'source_sha256':sha(src),'copy':str(dst),'copy_sha256':sha(dst),'only_local_PROJECT_replacement':True,'original_reverse_replacement_byte_equal':True,'cache_root':'HARNESS already resolves within own_root; no other edit','diff_sha256':sha(d/'exact.diff')})

def test_candidate(qid,variant):
    import runpy
    d=OWN/qid/variant
    assert not list((d/'tests').glob('**/*started.json')),'Actual request already exists; never retry'
    gates=read(d/'render_gates.json');replay=read(d/'independent_replay.json');design=read(d/'design.json')
    assert read(d/'primary_review_before_calls.json')['ready_for_exactly_two_calls']
    assert gates['png_sha256']==replay['png_sha256']==sha(d/'candidate.png')
    assert gates['design_sha256']==replay['design_sha256']==sha(d/'design.json')
    assert gates['plugin_sha256']==replay['plugin_sha256']==sha(d/'plugin.json')
    eligibility(qid,d/'eligibility_immediately_before_calls.json')
    save(d/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'role':'owned synchronous original harness runs2','strict_writeguard':str(OWN)})
    def before_call(event,args):
        if event=='open' and not isinstance(args[0],int) and str(args[0]).endswith('_started.json') and args[2] & os.O_CREAT:
            index=Path(args[0]).stem
            eligibility(qid,d/(index+'_eligibility.json'))
            assert sha(d/'candidate.png')==gates['png_sha256'] and sha(d/'design.json')==gates['design_sha256']
    sys.addaudithook(before_call)
    sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','SolidGeometry','--question',qid,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
    outcome='finished'
    try:runpy.run_path(sys.argv[0],run_name='__main__')
    except BaseException as e:
        outcome=type(e).__name__+': '+str(e)
        raise
    finally:
        save(d/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'outcome':outcome,'request_loop_returned':outcome=='finished','child_processes_started':False})
        starts=list((OWN).glob('Solid*/**/tests/**/run_*_started.json'))
        checkpoint(actual_new_api_calls=len(starts))

def finals(qid,variant,letters,notes):
    import base64
    from workbench_io import pixel_hash
    d=OWN/qid/variant
    summaries=list((d/'tests').glob('*/summary.json'));assert len(summaries)==1
    p=summaries[0];summary=read(p);binding=read(p.parent/'binding.json');design=read(d/'design.json')
    assert len(summary['results'])==2
    rows=[]
    request_path=p.parent/'request.json';payload=read(request_path)
    formal=read(d/'eligibility_immediately_before_calls.json')['record']
    assert payload['messages'][1]['content'][0]['text']==formal['question']
    assert base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(d/'candidate.png').read_bytes()
    assert sha(request_path)==binding['request_body_sha256']
    assert binding['design_sha256']==sha(d/'design.json') and (p.parent/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
    for i,(result,letter) in enumerate(zip(summary['results'],letters),1):
        raw=p.parent/f'run_{i:02d}_response.json';response=read(raw)
        answer=response['choices'][0]['message']['content']
        assert answer==result['answer'] and sha(raw)==result['response_sha256']
        complete=result['status']=='completed' and not result.get('truncated') and response['choices'][0]['finish_reason']=='stop'
        rows.append({'run_index':i,'complete_raw_response_manually_read':True,'raw_path':str(raw),'raw_sha256':sha(raw),'complete_answer_text':answer,'manual_final_letter':letter,'manual_final_value':formal['choices'].get(letter),'complete_nontruncated':complete,'matches_frozen_preset':letter==design['expected_wrong_answer'] and complete,'notes':notes[i-1]})
    hit=all(r['matches_frozen_preset'] for r in rows)
    report={'question_id':qid,'variant_id':variant,'frozen_preset_letter':design['expected_wrong_answer'],'frozen_preset_value':design['expected_wrong_value'],'summary_path':str(p),'summary_sha256':sha(p),'binding_sha256':sha(p.parent/'binding.json'),'request_sha256':sha(request_path),'exact_formal_text_and_png_binding':True,'design_snapshot_exact':True,'runs':rows,'exactly_two_actual_calls':True,'both_hit_frozen_preset':hit,'primary_status':'PRIMARY_CANDIDATE' if hit else 'FAILED_NOT_TWO_HITS','no_retry_or_relabel':True,'mechanism_causal_claim':False}
    save(d/'manual_final_review.json',report)
    save(d/'primary_review.json',report|{'independent_second_review':False,'user_approval':False,'formal_Pass_Collect':False,'source_current':eligibility(qid,d/'eligibility_after_calls.json')['eligible']})
    cp=read(OWN/'checkpoint.json');cp['questions'][qid]={'status':'primary_candidate_pending_new_independent_review' if hit else 'tested_failed_new_hypothesis_needed','candidate':str(d),'observed_finals':list(letters),'preset':design['expected_wrong_answer']};checkpoint(questions=cp['questions'])
    if hit:
        queue=read(OWN/'second_review_queue.json')
        queue.append({'question_id':qid,'variant_id':variant,'candidate_directory':str(d),'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'design_sha256':sha(d/'design.json'),'correct_answer':design['correct_answer'],'frozen_wrong_preset':{'letter':design['expected_wrong_answer'],'value':design['expected_wrong_value']},'two_complete_finals':rows,'summary_path':str(p),'primary_review_path':str(d/'primary_review.json'),'reference_migration_path':str(d/'reference_migration.json'),'restrictions':design['restrictions']})
        save(OWN/'second_review_queue.json',queue)
    print(qid,variant,list(letters),'two_hits',hit)

if __name__=='__main__':
    if sys.argv[1]=='audit':audit()
    elif sys.argv[1]=='setup':setup()
    elif sys.argv[1]=='render':render_candidate(sys.argv[2],sys.argv[3])
    elif sys.argv[1]=='replay':render_candidate(sys.argv[2],sys.argv[3],True)
    elif sys.argv[1]=='harness':copy_harness()
    elif sys.argv[1]=='test':test_candidate(sys.argv[2],sys.argv[3])
