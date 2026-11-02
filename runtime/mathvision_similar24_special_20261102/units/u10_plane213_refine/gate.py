from bootstrap import *
import base64,difflib,zipfile
d=OWN/'Plane213/user233_exterior_concave_corner_to_B_v2';png=sha(d/'candidate.png')
assert read(d/'native_review.json')['actual_candidate_png_viewed']
assert read(d/'native_review.json')['proceed_to_API']
r=read(OWN/'offline_replay/replay_verification.json');assert r['matches_tested_png_bytes'] and r['two_delivery_replays_identical'] and r['png_sha256']==png
e=eligibility();question=e['formal_record']['question']
matches=[];cross=[];errors=[];count=0;images=0;zip_members=0
def inspect(data,name):
 global count,images
 count+=1
 try:obj=json.loads(data.decode('utf-8-sig'))
 except Exception as exc:errors.append({'path':name,'error':type(exc).__name__});return
 if not isinstance(obj,dict):return
 if obj.get('image_sha256')==png:
  (matches if obj.get('question_id')=='Plane213' else cross).append({'path':name,'question_id':obj.get('question_id'),'kind':'metadata'})
 if Path(name).name=='request.json':
  try:
   msg=obj['messages'][1]['content'];text=next(x['text'] for x in msg if x.get('type')=='text');url=next(x['image_url']['url'] for x in msg if x.get('type')=='image_url')
   im=base64.b64decode(url.split(',',1)[1]);h=hashlib.sha256(im).hexdigest();images+=1;del im
   if h==png:(matches if text==question else cross).append({'path':name,'kind':'embedded_request','formal_question_exact':text==question})
  except (KeyError,TypeError,ValueError,StopIteration):pass
def wanted(name):
 return name in ['binding.json','summary.json','request.json'] or (name.startswith('run_') and name.endswith('_started.json'))
for parent,dirs,files in os.walk(ROOT/'runtime'):
 dirs[:]=[v for v in dirs if v not in ['.git','__pycache__','node_modules']]
 for name in files:
  p=Path(parent)/name
  if wanted(name):inspect(p.read_bytes(),str(p))
  elif name.endswith('.zip'):
   try:
    with zipfile.ZipFile(p) as z:
     for member in z.namelist():
      if wanted(Path(member).name):zip_members+=1;inspect(z.read(member),str(p)+'!'+member)
   except zipfile.BadZipFile:errors.append({'path':str(p),'error':'BadZipFile'})
audit={'at_utc':now(),'question_id':'Plane213','PNG_sha256':png,'records_scanned':count,'embedded_images_decoded':images,'zip_members_scanned':zip_members,'same_question_exact_PNG_matches':matches,'cross_question_same_PNG_matches':cross,'parse_errors_preserved':errors,'scope':'Existing saved standard transport/start/request/binding/summary files under runtime, including ZIP members; not provider-side or deleted-history audit.','zero_prior_saved_same_question_exact_PNG_calls':not matches,'new_API_calls':0}
save(OWN/'zero_prior_call_scan.json',audit)
assert not matches and not cross, 'Frozen image already transported; no retry/cross-ID old failed image copy.'
assert not errors, 'Resolve offline scan ambiguity before FIRST call.'
source=OLD/'harness/quicktest3_isolated.py';raw=source.read_bytes();before=b'PROJECT = Path(__file__).resolve().parents[3]';after=('PROJECT = Path('+repr(ROOT.as_posix())+')').encode()
assert raw.count(before)==1
local=raw.replace(before,after);assert local.replace(after,before)==raw
harness=OWN/'harness';harness.mkdir(exist_ok=False);(harness/'quicktest3_isolated.py').write_bytes(local)
save(OWN/'harness_relocation_audit.json',{'at_utc':now(),'canonical_source':str(source),'canonical_sha256':sha(source),'local_copy':str(harness/'quicktest3_isolated.py'),'local_sha256':sha(harness/'quicktest3_isolated.py'),'inverse_byte_replacement_exact':True,'only_change':'Local PROJECT resolution, all remote request/profile/thinking/system/token/timeout/credential/retry behavior untouched.'})
(OWN/'harness_relocation.patch').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),local.decode().splitlines(True))),encoding='utf-8')
tracked={}
for p in [ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'PlaneGeometry/REDRAW_PROTOCOL.md',ROOT/'PlaneGeometry/workbench/README.md',ROOT/'PlaneGeometry/workbench/agent_prompt.md',ROOT/'PlaneGeometry/workbench/plugin.schema.json',source,OLD/'runtime_isolation.py',OLD/'validate_candidate_replay.py',TASK/'references/Plane233/C01.png',TASK/'references/Plane233/C01.json']:
 tracked[str(p)]=sha(p)
for p,h in e['frozen_source_files_sha256'].items():tracked[str(ROOT/p)]=h
for src in [OLD/'background_09/Plane213/open_notch_local_global_binding',TASK/'root_213/Plane213/user233_boundary_spine_foot_transfer_v1',OLD/'background_23/Plane233/r23_exterior_notch_correspondence']:
 for p in src.rglob('*'):
  if p.is_file():tracked[str(p)]=sha(p)
save(OWN/'readonly_before_calls.json',tracked)
save(OWN/'prelaunch_gate.json',{'at_utc':now(),'question_id':'Plane213','same_question_exact_PNG_zero_prior_actual_calls_proved':True,'PNG_sha256':png,'design_sha256':sha(d/'design.json'),'wrong_preset':'B','current_eligibility':e,'zero_prior_scan_sha256':sha(OWN/'zero_prior_call_scan.json'),'exact_replay_sha256':sha(OWN/'offline_replay/replay_verification.json'),'permitted_calls':2,'retry_or_extra_call':False})
print(json.dumps({'FIRSTPAIR_GATE':'PASS','records':count,'same_question_matches':0,'cross_question_matches':0,'image':png}))
