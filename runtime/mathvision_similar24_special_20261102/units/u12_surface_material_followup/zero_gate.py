from bootstrap import *
import base64,re,zipfile
entries=read(OWN/'first_pair_candidates.json')
targets={e['question_id']:e['PNG_sha256'] for e in entries}
texts={q:eligibility(q)['formal_record']['question'] for q in targets}
matches=[];errors=[];counts={'JSON_transport_records':0,'request_images_decoded':0,'ZIP_transport_members':0}
pattern=re.compile(r'^(binding|summary|request|run_\d+(?:_started)?)\.json$')
def inspect(blob,path):
 try:d=json.loads(blob.decode('utf-8-sig'))
 except Exception as ex:
  errors.append({'path':path,'error_type':type(ex).__name__,'target_related':any(q in path for q in targets)});return
 counts['JSON_transport_records']+=1
 if not isinstance(d,dict):return
 q=d.get('question_id');fingerprint=d.get('image_sha256',d.get('png_sha256'))
 if q in targets and fingerprint==targets[q]:matches.append({'path':path,'question_id':q,'PNG_sha256':fingerprint,'kind':'binding/start/summary'})
 if 'messages' in d:
  messages=d.get('messages',[])
  for m in messages:
   content=m.get('content') if isinstance(m,dict) else None
   if not isinstance(content,list):continue
   text=''.join(i.get('text','') for i in content if isinstance(i,dict) and i.get('type')=='text')
   q=next((q for q,t in texts.items() if text==t),None)
   if q is None:continue
   for i in content:
    if not isinstance(i,dict) or i.get('type')!='image_url':continue
    url=i.get('image_url',{}).get('url','')
    if not url.startswith('data:image/'):continue
    try:fp=hashlib.sha256(base64.b64decode(url.split(',',1)[1],validate=True)).hexdigest()
    except Exception as ex:errors.append({'path':path,'error_type':type(ex).__name__,'target_related':True});continue
    counts['request_images_decoded']+=1
    if fp==targets[q]:matches.append({'path':path,'question_id':q,'PNG_sha256':fp,'kind':'exact_formal_question_and_image_request'})
for p in (ROOT/'runtime').rglob('*.json'):
 if pattern.fullmatch(p.name):inspect(p.read_bytes(),str(p))
for p in (ROOT/'runtime').rglob('*.zip'):
 try:
  with zipfile.ZipFile(p) as z:
   for n in z.namelist():
    if pattern.fullmatch(Path(n).name):counts['ZIP_transport_members']+=1;inspect(z.read(n),str(p)+'!'+n)
 except zipfile.BadZipFile as ex:errors.append({'path':str(p),'error_type':type(ex).__name__,'target_related':any(q in str(p) for q in targets)})
assert not matches and not any(x['target_related'] for x in errors)
for e in entries:
 d=Path(e['candidate_directory']);assert sha(d/'candidate.png')==e['PNG_sha256'] and sha(d/'design.json')==e['design_sha256']
 r=read(OWN/'fresh_replay'/e['question_id']/'replay_verification.json')
 assert r['two_delivery_replays_identical'] and r['png_sha256']==e['PNG_sha256']
 eligibility(e['question_id'])
save('zero_prior_call_gate.json',{'at_utc':now(),'target_PNG_sha256':targets,'all_target_question_PNG_pairs_have_zero_saved_prior_transport':True,'matches':matches,'scan_counts':counts,'unrelated_parse_or_in_progress_errors_preserved':errors,'scope':'Current saved standard transport/request/start/binding/summary JSON and readable ZIP members under root runtime. Not provider-account/deleted/external history audit.','actual_solver_calls_during_gate':0})
print(json.dumps({'FIRSTpair_gate':'PASS','targets':targets,'counts':counts,'target_prior_matches':len(matches),'unrelated_errors':len(errors)}))
