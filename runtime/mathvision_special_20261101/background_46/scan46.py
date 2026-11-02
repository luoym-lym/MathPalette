from bootstrap46 import *
from datetime import datetime, timezone
import base64,re,io
from PIL import Image
def now(): return datetime.now(timezone.utc).isoformat()
assignment=read(TASK/'background_46_assignment.json')
targets={q['question_id']:q['reuse_input']['files_sha256']['candidate.png'] for q in assignment['questions'] if 'reuse_input' in q}
pixel_targets={}
for q in assignment['questions']:
    if 'reuse_input' not in q: continue
    p=Path(q['reuse_input']['source_directory'])/'candidate.png'
    with Image.open(p) as im: pixel_targets[q['question_id']]=hashlib.sha256(im.convert('RGBA').tobytes()).hexdigest()
artifacts=[];matches=[];errors=[];references=[];decoded=0;count=0
for p in sorted(TASK.rglob('*.json')):
    if p.is_relative_to(OWN): continue
    count+=1
    try:
        raw=p.read_bytes(); s=raw.decode('utf-8-sig'); value=json.loads(s)
    except Exception as e:
        errors.append({'path':str(p),'error':str(e)});continue
    name=p.name.lower(); parts=[x.lower() for x in p.relative_to(TASK).parts]
    named=bool(re.fullmatch(r'run_\d+(?:_started|_response|_error)?\.json',name)) or name in {'request.json','binding.json','summary.json','api_process.json','api_process_finished.json'} or any(x in parts for x in ['quick_tests','quicktests'])
    shaped=isinstance(value,dict) and (('messages' in value and 'model' in value) or ('started_at' in value and ('run_index' in value or 'request_body_sha256' in value)))
    actual=named or shaped
    hits=[q for q,h in targets.items() if h in s]
    if not actual:
        if hits:references.append({'path':str(p),'matches':hits,'classification':'non-call design/history/pretest/provenance reference; no actual invocation schema'})
        continue
    item={'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'classification':'actual API artifact','direct_png_sha_matches':hits,'decoded_payloads':[]}
    for payload in re.findall(r'data:image/png;base64,([A-Za-z0-9+/=]+)',s):
        try:
            b=base64.b64decode(payload,validate=True); h=hashlib.sha256(b).hexdigest()
            with Image.open(io.BytesIO(b)) as im: ph=hashlib.sha256(im.convert('RGBA').tobytes()).hexdigest()
            qs=[q for q in targets if h==targets[q] or ph==pixel_targets[q]]
            item['decoded_payloads'].append({'png_sha256':h,'rgba_sha256':ph,'target_matches':qs});decoded+=1
            hits=list(set(hits+qs))
        except Exception as e: errors.append({'path':str(p),'error':'PNG decode: '+str(e)})
    if hits: matches.append({**item,'target_matches':hits})
    artifacts.append(item)
save(OWN/'full_task_api_reuse_scan.json',{'checked_at':now(),'json_files_read':count,'api_artifacts_read':len(artifacts),'decoded_png_payloads':decoded,'targets':targets,'pixel_targets':pixel_targets,'actual_call_matches':matches,'parse_or_decode_errors':errors,'excluded_noncall_references':references,'artifact_manifest':artifacts,'reuse_zero_prior_calls_supported':not matches and not errors,'limitation':'All available local task JSON artifacts scanned, including request/start/binding/run/error/summary and decoded PNG+RGBA. Provider-side unseen calls and deleted artifacts cannot be proven absent.'})
prep=read(TASK/'closure38_40_parent_preparation.json')
checks=[]
for rel,expected in prep['read_only_inputs_sha256'].items():
    p=TASK/rel; checks.append({'path':str(p),'expected':expected,'actual':sha(p) if p.is_file() else None})
save(OWN/'preparation_full_read_hash_verification.json',{'source_sha256':sha(TASK/'closure38_40_parent_preparation.json'),'all_mapping_entries_read':len(checks),'entries':checks,'mismatches':[x for x in checks if x['actual']!=x['expected']]})
print(json.dumps({'json_files':count,'api_artifacts':len(artifacts),'decoded_pngs':decoded,'matches':matches,'errors':errors,'preparation_hash_entries':len(checks),'preparation_mismatches':sum(x['actual']!=x['expected'] for x in checks)},ensure_ascii=False))
