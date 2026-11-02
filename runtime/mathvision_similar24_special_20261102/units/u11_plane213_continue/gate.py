from bootstrap import *
import base64,difflib,zipfile
vid=sys.argv[1];d=OWN/'Plane213'/vid;png=sha(d/'candidate.png')
assert read(d/'primary_review_before_calls.json')['proceed_to_API']
r=read(OWN/'replays'/vid/'replay_verification.json')
assert r['matches_tested_png_bytes'] and r['two_delivery_replays_identical'] and r['png_sha256']==png
e=eligibility();question=e['formal_record']['question']
matches=[];cross=[];errors=[];count=0;images=0;zip_members=0
def inspect(data,name):
    global count,images
    count+=1
    if count%1000==0:
        save(d/'history_scan_progress.json',{'at_utc':now(),'records_fully_inspected_before_current':count-1,'current_record':name,'new_API_calls':0},replace=True)
    try:obj=json.loads(data.decode('utf-8-sig'))
    except Exception as exc:errors.append({'path':name,'error':type(exc).__name__});return
    if not isinstance(obj,dict):return
    if obj.get('image_sha256')==png:
        (matches if obj.get('question_id')=='Plane213' else cross).append({'path':name,'question_id':obj.get('question_id'),'kind':'transport_metadata'})
    if Path(name).name=='request.json':
        try:
            msg=obj['messages'][1]['content'];text=next(x['text'] for x in msg if x.get('type')=='text');url=next(x['image_url']['url'] for x in msg if x.get('type')=='image_url')
            im=base64.b64decode(url.split(',',1)[1]);h=hashlib.sha256(im).hexdigest();images+=1;del im
            if h==png:(matches if text==question else cross).append({'path':name,'kind':'embedded_request','formal_question_exact':text==question})
        except (KeyError,TypeError,ValueError,StopIteration):pass
def wanted(name):
    return name in ('binding.json','summary.json','request.json') or (name.startswith('run_') and name.endswith('_started.json'))
for base in [ROOT/'runtime',ROOT/'.runtime']:
    if not base.exists():continue
    for parent,dirs,files in os.walk(base):
        dirs[:]=[v for v in dirs if v not in ('.git','__pycache__','node_modules')]
        for name in files:
            p=Path(parent)/name
            if wanted(name) or (base.name=='.runtime' and name.endswith('.json')):inspect(p.read_bytes(),str(p))
            elif name.endswith('.zip'):
                try:
                    with zipfile.ZipFile(p) as z:
                        for member in z.namelist():
                            if wanted(Path(member).name):zip_members+=1;inspect(z.read(member),str(p)+'!'+member)
                except zipfile.BadZipFile:errors.append({'path':str(p),'error':'BadZipFile'})
save(d/'zero_prior_call_scan.json',{'at_utc':now(),'question_id':'Plane213','PNG_sha256':png,'records_scanned':count,'embedded_images_decoded':images,'zip_members_scanned':zip_members,'same_question_exact_PNG_matches':matches,'cross_question_same_PNG_matches':cross,'parse_errors_preserved':errors,'scope':'All saved standard requests/start/binding/summary in runtime including ZIPs, and .runtime JSON; no claim about provider-side or deleted history.','zero_prior_saved_same_question_exact_PNG_calls':not matches,'new_API_calls':0})
assert not matches and not cross,'Previously transported frozen image; no retry permitted.'
assert not errors,'Preserved offline scan ambiguity; investigate before any call.'
source=OLD/'harness/quicktest3_isolated.py';raw=source.read_bytes();before=b'PROJECT = Path(__file__).resolve().parents[3]';after=('PROJECT = Path('+repr(ROOT.as_posix())+')').encode()
assert raw.count(before)==1
local=raw.replace(before,after);assert local.replace(after,before)==raw
harness=OWN/'harness';harness.mkdir(exist_ok=True);hp=harness/'quicktest3_isolated.py'
if hp.exists():assert hp.read_bytes()==local
else:
    hp.write_bytes(local)
    save('harness_relocation_audit.json',{'at_utc':now(),'canonical_source':str(source),'canonical_sha256':sha(source),'local_copy':str(hp),'local_sha256':sha(hp),'inverse_byte_replacement_exact':True,'only_change':'Local PROJECT resolution. Remote payload/model/thinking/system/token/timeout/credential/retry logic remains byte-identical.'})
    (OWN/'harness_relocation.patch').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),local.decode().splitlines(True))),encoding='utf-8')
tracked=read(OWN/'readonly_initial_sha256.json');changed=[p for p,h in tracked.items() if sha(p)!=h];assert not changed
context=read(d/'fresh_context.json');targets={o['id']:o for o in context['objects']}
save(d/'path_fingerprints.json',{'at_utc':now(),'fresh_context_sha256':sha(d/'fresh_context.json'),'targets':[targets[a['target']] for a in read(d/'plugin.json')['params']['actions']],'environment_and_noop_sha256':sha(OWN/'environment_and_noop.json')})
frozen={str(p):sha(p) for p in d.glob('*') if p.is_file()}
save(d/'prelaunch_gate.json',{'at_utc':now(),'question_id':'Plane213','zero_prior_saved_same_question_or_cross_question_PNG_calls':True,'PNG_sha256':png,'design_sha256':sha(d/'design.json'),'wrong_preset':read(d/'design.json')['expected_wrong_answer'],'current_eligibility':e,'frozen_candidate_artifact_hashes':frozen,'exact_fresh_process_replay_sha256':sha(OWN/'replays'/vid/'replay_verification.json'),'readonly_sources_checked':len(tracked),'permitted_calls':2,'retry_or_extra_call':False})
checkpoint=read(OWN/'checkpoint.json')
checkpoint.update(at_utc=now(),status='gates_passed_pending_exact_pair',candidate_directory=str(d),current_pair_actual_calls_started=0,second_review_queue=read(OWN/'second_review_queue.json'))
save('checkpoint.json',checkpoint,replace=True)
print(json.dumps({'FIRSTPAIR_GATE':'PASS','records_scanned':count,'same_question_matches':len(matches),'cross_question_matches':len(cross),'PNG_sha256':png}))
