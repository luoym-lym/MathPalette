from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,IDS,stamp
from pathlib import Path
import json,sys,subprocess,gc

def scan():
    report={}
    for q in IDS:
        query=read(HERE/q/'formal_record.json')['question'].splitlines()[0].split('$')[0].split('\\')[0][:140]
        found=[]
        for pattern,globs in [(q,['*started*.json','binding.json','design.json','summary.json','*review*.json','*reject*.json','*hold*.json']), (query,['request.json'])]:
            args=['rg','-l','-F',pattern,str(TASK)]
            for g in globs:args+=['-g',g]
            result=subprocess.run(args,capture_output=True,text=True,encoding='utf-8')
            assert result.returncode in (0,1),result.stderr
            found.extend(Path(p) for p in result.stdout.splitlines() if p.strip())
        entries=[]
        raw=[]
        for p in sorted(set(found)):
            if p.is_relative_to(HERE):continue
            data=read(p)
            entries.append({'path':str(p),'sha256':sha(p),'size':p.stat().st_size,'complete_json_read':True})
            if p.name=='request.json':
                import base64,hashlib
                payload=data
                user=payload.get('messages',[{},{}])[1]
                texts=[x['text'] for x in user.get('content',[]) if x.get('type')=='text']
                images=[x['image_url']['url'] for x in user.get('content',[]) if x.get('type')=='image_url']
                assert texts==[read(HERE/q/'formal_record.json')['question']],p
                png=base64.b64decode(images[0].split(',',1)[1])
                binding=read(p.with_name('binding.json'))
                assert hashlib.sha256(png).hexdigest()==binding['image_sha256']
                raw.append({'request_path':str(p),'image_sha256':binding['image_sha256'],'design_sha256':binding['design_sha256'],'expected_wrong_answer':binding['expected_wrong_answer'],'requested_runs':binding['requested_runs'],'full_raw_paths':[str(x) for x in p.parent.glob('*response*')],'actual_started':[str(x) for x in p.parent.glob('*started.json')],'question_exact':True,'image_binding_exact':True})
                del png,payload,user,texts,images,binding
            del data
            gc.collect()
        report[q]={'files':entries,'observed_prior_invocations':raw,'scope_note':'Global task-root exact-ID binding/start/design/review search and exact-formal-question request search. Missing summaries are not zero-call evidence; every matching request separately decoded and hashed. Historical reused snapshots do not create invocations.'}
    save(HERE/'global_old_call_and_objection_scan_v2.json',report)
    print(json.dumps({q:{'files':len(x['files']),'prior_requests':len(x['observed_prior_invocations']),'prior_calls_started':sum(len(a['actual_started']) for a in x['observed_prior_invocations'])} for q,x in report.items()},indent=2))

def sources():
    for q in IDS:
        r=read(HERE/q/'formal_record.json')
        report=[]
        for rel in [r['scene'],r['script']]+r['runtime_dependencies']:
            p=PROJECT/'SolidGeometry'/rel
            text=p.read_text(encoding='utf-8-sig')
            entry={'path':str(p),'sha256':sha(p),'complete_utf8_read':True}
            if p.suffix=='.json':
                d=json.loads(text)
                entry['keys']=list(d)
                entry['semantics']={k:v for k,v in d.items() if k in ('projection','visibility','dimensions','labels','constraints','ambiguities','world_unit','protocol_version','source_key','source_dataset','source_note','subject','notes')}
                entry['point_count']=len(d.get('points',{}))
                entry['object_count']=len(d.get('objects',[]))
            report.append(entry)
            del text
            gc.collect()
        save(HERE/q/'source_native_complete_read_audit.json',report)
        print(q)
        for entry in report:
            if entry['path'].endswith('items\\'+q+'\\scene.json'):
                print(json.dumps(entry,ensure_ascii=False,indent=2))

def dimensions(q):
    c=read(HERE/q/'context_fresh.json')
    points={p['id']:p for p in c['snap_points']}
    for obj in c['objects']:
        g=obj.get('geometry',{})
        names=g.get('points',[])
        xyz=[points[name]['world_xyz'] for name in names if name in points]
        print(obj['id'],g.get('type'),names,xyz)

def prescreen():
    out=[]
    def walk(v,path=''):
        if isinstance(v,dict):
            if v.get('question_id',v.get('id')) in IDS:
                out.append({'json_path':path,'content':v})
            else:
                for k,x in v.items():walk(x,path+'/'+k)
        elif isinstance(v,list):
            for i,x in enumerate(v):walk(x,path+'/'+str(i))
    for filename in ['background_03/checkpoint.json','background_03/solid_worker/checkpoint.json','background_03/solid_worker/prescreen_rejections.json','background_15/checkpoint.json','background_16/checkpoint.json']:
        p=TASK/filename
        d=read(p)
        start=len(out)
        walk(d)
        for e in out[start:]:e.update(source_path=str(p),source_sha256=sha(p))
        del d
    save(HERE/'old_prescreen_checkpoint_scoped_full.json',out)
    for e in out:
        if 'screen' in e['json_path'] or 'prescreen' in e['source_path']:
            print(json.dumps(e,ensure_ascii=False,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='scan':scan()
    elif sys.argv[1]=='sources':sources()
    elif sys.argv[1]=='dimensions':dimensions(sys.argv[2])
    elif sys.argv[1]=='prescreen':prescreen()
