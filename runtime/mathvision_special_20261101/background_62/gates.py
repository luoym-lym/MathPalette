from bootstrap import install, OWN, PROJECT, SESSION
install()
import sys, json, hashlib, base64, re, gc
from pathlib import Path
from datetime import datetime, timezone

IDS=['Plane482','Plane488']
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return h.hexdigest()
def load(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def now(): return datetime.now(timezone.utc).isoformat()
def eligibility(q,leaf='qualification.json'):
    from dataset_tools import catalog
    branch=PROJECT/'PlaneGeometry';special=branch/'special_variant'
    row=next(r for r in catalog.rows(branch/'dataset.jsonl') if r['id']==q)
    a=load(PROJECT/'provenance/approvals.json')['approvals'][q]
    content=catalog.content(PROJECT,'PlaneGeometry',row);digest=catalog.digest(content)
    accepted=[r for r in catalog.rows(special/'accepted_index.jsonl') if r.get('question_id',r.get('id'))==q]
    collected=[r for r in catalog.rows(special/'collected_index.jsonl') if r.get('question_id',r.get('id'))==q]
    recipes=special/q/'recipes.json';collection=special/q/'collection.json'
    eligible=row['source_dataset']=='MathVision' and a.get('reviewer')=='user' and bool(a.get('instruction')) and a['content_sha256']==digest and not accepted and not collected and not recipes.exists() and not collection.exists()
    d={'checked_at_utc':now(),'question_id':q,'formal_record':row,'formal_record_sha256':catalog.digest(row),'original_approval':a,'current_content_sha256':digest,'fingerprint_matches':a['content_sha256']==digest,'content':content,'accepted_records':accepted,'collected_records':collected,'recipes_exists':recipes.exists(),'collection_exists':collection.exists(),'eligible':eligible}
    save(OWN/q/leaf,d)
    return d

def scan():
    assignment=load(SESSION/'background_62_assignment.json')
    hashes={q['PNG_sha256']:q['question_id'] for q in assignment['questions']}
    counts={'files':0,'JSON':0,'API_artifacts':0,'embedded_PNGs':0}
    matches=[];refs=[];malformed=[];unknown=[]
    dest=OWN/'scan';dest.mkdir(exist_ok=True)
    def walk(d):
        if isinstance(d,dict):
            for v in d.values():yield from walk(v)
        elif isinstance(d,list):
            for v in d:yield from walk(v)
        elif isinstance(d,str):yield d
    with (dest/'all_file_hashes.jsonl').open('w',encoding='utf-8') as out:
        for p in SESSION.rglob('*'):
            if not p.is_file() or p.is_relative_to(OWN):continue
            if p.suffix.lower() not in ('.json','.jsonl','.txt','.log','.bin'):continue
            counts['files']+=1
            name=p.name.lower();api=bool(re.search(r'^(request|binding|summary|run_\d.*|api_process.*|.*error.*|.*incomplete.*)\.(json|bin|log|txt)$',name)) and ('tests' in p.parts or 'quicktest' in str(p).lower() or name.startswith('api_process'))
            counts['API_artifacts']+=int(api)
            raw=p.read_bytes(); h=hashlib.sha256(raw).hexdigest()
            out.write(json.dumps({'path':str(p),'sha256':h,'bytes':len(raw),'API_artifact':api})+'\n')
            t=raw.decode('utf-8-sig',errors='replace'); direct=[v for v in hashes if v in t]
            related=any(q in str(p) for q in IDS) or any(q in t for q in IDS)
            found=[]
            if p.suffix.lower() in ('.json','.jsonl'):
                try:
                    counts['JSON']+=1
                    docs=[json.loads(t)] if p.suffix.lower()=='.json' else None
                    if docs is None:
                        docs=(json.loads(line) for line in t.splitlines() if line.strip())
                    for d in docs:
                        for s in walk(d):
                            # Includes images nested in preserved request snapshots as well as real requests.
                            for match in re.finditer(r'data:image/png;base64,([A-Za-z0-9+/=\r\n]+)',s):
                                b=base64.b64decode(match.group(1),validate=False)
                                if not b.startswith(b'\x89PNG\r\n\x1a\n'):raise ValueError('embedded image is not PNG')
                                bh=hashlib.sha256(b).hexdigest();counts['embedded_PNGs']+=1
                                if bh in hashes:found.append(bh)
                                del b
                        del d
                    del docs
                except (ValueError,UnicodeError) as e:
                    rec={'path':str(p),'sha256':h,'bytes':len(raw),'error':str(e),'related_by_content_or_path':related,'API_artifact':api,'matching_hashes':direct}
                    bad=dest/'malformed'/str(p.relative_to(SESSION));bad.parent.mkdir(parents=True,exist_ok=True);bad.write_bytes(raw)
                    rec['preserved_exact_copy']=str(bad);malformed.append(rec)
                    if related or direct:unknown.append(rec)
            mh=sorted(set(direct+found))
            if mh:
                rec={'path':str(p),'sha256':h,'matching_PNG_hashes':mh,'embedded_exact_hashes':found,'API_artifact':api}
                (matches if api else refs).append(rec)
            # Actual process launch may name a candidate without embedding its hash.
            if api and related and name.startswith('api_process'):
                for q in assignment['questions']:
                    if q['variant_id'] in t:matches.append({'path':str(p),'reason':'process launch references frozen variant','question_id':q['question_id'],'sha256':h})
            del raw,t
            if counts['files']%500==0:gc.collect()
    result={'checked_at_utc':now(),'scope':str(SESSION),'excluded_own_new_outputs':str(OWN),'counts':counts,'actual_old_exact_PNG_API_matches':matches,'non_API_reference_matches':refs,'malformed_records':malformed,'blocking_unknown_or_malformed':unknown,'zero_old_call_gate_pass':not matches and not unknown,'limits':['Local available evidence only; no provider history assumed. Missing summary is never treated as proof of no invocation.','Bindings, requests with decoded embedded images, starts, raw/error/incomplete records and process launches are independently inventoried; no actual call is inferred from draft review references.']}
    save(OWN/'zero_prior_invocation_scan.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('non_API_reference_matches','malformed_records')},ensure_ascii=False),flush=True)

def reads():
    receipts=[];preserve={};summaries=[]
    def read(p):
        p=Path(p);b=p.read_bytes();t=b.decode('utf-8-sig');h=hashlib.sha256(b).hexdigest()
        preserve[str(p)]=h;receipts.append({'path':str(p),'sha256':h,'bytes':len(b),'full_UTF8_read':True})
        return json.loads(t) if p.suffix=='.json' else t
    for n in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json']:
        read(PROJECT/n)
    for n in ['continuation_brief.txt','background_62_brief.txt','background_62_assignment.json','preparation62.json','draft52_untested_first_call_provenance.json','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json']:
        d=read(SESSION/n)
        if n=='draft52_untested_first_call_provenance.json':print('PRIOR_SCAN',json.dumps(d['all_task_evidence_scan'],ensure_ascii=False))
    for p in (SESSION/'background_52').glob('*.json'):read(p)
    for q in IDS:
        for p in (SESSION/'background_52'/q).rglob('*'):
            if not p.is_file():continue
            preserve[str(p)]=sha(p)
            if p.suffix=='.json':
                d=read(p)
                if p.name=='old_history_read.json':
                    for r in d:
                        actual=Path(r['path']); rd=read(actual)
                        assert preserve[str(actual)]==r['sha256'],('old evidence changed',str(actual))
                        if actual.name.endswith('_response.json'):
                            summaries.append({'path':str(actual),'full_final':rd['choices'][0]['message']['content']})
                        del rd
                elif p.name=='design.json':
                    print('FROZEN_DESIGN',q,json.dumps({k:d[k] for k in ['variant_id','created_at_utc','expected_wrong_answer','hypothesis']},ensure_ascii=False))
                    for r in d['marker_roles']:
                        print('MARKER',q,r['index'],json.dumps({'action':r['action'],'controls':r['exact_native_path'],'role':r['role']},ensure_ascii=False))
                del d
        e=eligibility(q)
        for n in [e['formal_record'][k] for k in ['image','original_image','scene','script']]+e['formal_record']['runtime_dependencies']:
            p=PROJECT/'PlaneGeometry'/n;preserve[str(p)]=sha(p)
            if p.suffix in ('.py','.json'):read(p)
        print('QUALIFICATION',q,e['eligible'],e['current_content_sha256'])
    refs=['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly']
    for n in refs:
        p=SESSION/'independent_review'/n/'independent_review.json'
        if not p.exists():
            ps=list((SESSION/'independent_review').rglob('independent_review.json'))
            p=next(x for x in ps if 'Plane242' in str(x))
        d=read(p)
        print('REJECTION',n,json.dumps({k:v for k,v in d.items() if k in ['decision','reason','blocking_reason','concrete_objections','independent_unique_answer_proof','requirements','primary_proof_corrections']},ensure_ascii=False)[:16000])
        del d
    for p in [PROJECT/'provenance/approvals.json',PROJECT/'PlaneGeometry/dataset.jsonl',PROJECT/'PlaneGeometry/special_variant/accepted_index.jsonl',PROJECT/'PlaneGeometry/special_variant/collected_index.jsonl']:
        preserve[str(p)]=sha(p)
    save(OWN/'read_receipts.json',receipts);save(OWN/'readonly_initial_hashes.json',preserve)
    save(OWN/'old_full_finals.json',summaries)
    print('OLD_FULL_FINALS',json.dumps(summaries,ensure_ascii=False,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='scan':scan()
    if sys.argv[1]=='reads':reads()
