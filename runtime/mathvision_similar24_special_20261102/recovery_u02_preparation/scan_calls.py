from bootstrap import *
import re,zipfile,base64
gate=read(OWN/'initial_gate.json');targets={d['question_id']:d['image_sha256'] for d in gate['drafts']}
questions={q:read(OWN/q/'eligibility_initial.json')['formal_record']['question'] for q in targets}
standard=re.compile(r'^(?:binding|summary|request)\.json$|^run_\d+(?:_started)?\.json$|(?:start|binding|request|summary).*\.json$',re.I)
records=[];errors=[];archives=[];counts={'filesystem_standard_files':0,'zip_standard_members':0,'requests_decoded':0}
allq=[];matched=[]
def inspect(label,b,kind):
 counts[kind]+=1
 try:d=json.loads(b.decode('utf-8-sig'))
 except Exception as e:
  related=any(q.encode() in b or h.encode() in b for q,h in targets.items()) or any(q in label for q in targets)
  errors.append({'path':label,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'error':repr(e),'target_related':related});return
 if not isinstance(d,dict):return
 q=d.get('question_id');textq=d.get('question');im=d.get('image_sha256');body=False
 if 'messages' in d:
  body=True;ims=[];texts=[]
  for m in d['messages']:
   if m.get('role')!='user':continue
   c=m.get('content',[])
   if isinstance(c,str):texts.append(c);continue
   for a in c:
    if a.get('type')=='text':texts.append(a.get('text',''))
    if a.get('type')=='image_url':
     url=a.get('image_url',{}).get('url','')
     if url.startswith('data:') and ';base64,' in url:
      try:ims.append(hashlib.sha256(base64.b64decode(url.split(';base64,',1)[1],validate=True)).hexdigest());counts['requests_decoded']+=1
      except Exception as e:errors.append({'path':label,'error':'image decode '+repr(e),'target_related':any(x in label for x in targets)})
  textq='\n'.join(texts)
  for q0,t in questions.items():
   if textq==t:q=q0
  if len(ims)==1:im=ims[0]
  elif any(x in targets.values() for x in ims):im=next(x for x in ims if x in targets.values())
 if q not in targets and textq not in questions.values() and im not in targets.values():return
 if textq in questions.values() and q not in targets:q=next(q0 for q0,t in questions.items() if t==textq)
 rec={'path':label,'question_id':q,'exact_formal_question_text_match':textq==questions.get(q),'image_sha256':im,'record_sha256':hashlib.sha256(b).hexdigest(),'request_body':body,'results_present':bool(d.get('results')),'transport_started':bool(re.search(r'run_\d+(?:_started)?\.json$',label)),'exact_target_image':im in targets.values()}
 allq.append(rec)
 if im in targets.values():
  targetq=next(q0 for q0,h in targets.items() if h==im)
  rec['image_owner_question']=targetq;rec['same_formal_question']=q==targetq or textq==questions[targetq];matched.append(rec)

for p in (ROOT/'runtime').rglob('*'):
 if not p.is_file() or p.is_relative_to(OWN):continue
 if p.suffix.lower()=='.zip':archives.append(p);continue
 if standard.match(p.name):
  try:inspect(str(p),p.read_bytes(),'filesystem_standard_files')
  except Exception as e:errors.append({'path':str(p),'read_error':repr(e),'target_related':any(q in str(p) for q in targets)})
for p in archives:
 try:
  with zipfile.ZipFile(p) as z:
   for n in z.namelist():
    if standard.match(n.rsplit('/',1)[-1]):inspect(str(p)+'::'+n,z.read(n),'zip_standard_members')
 except Exception as e:errors.append({'path':str(p),'zip_error':repr(e),'target_related':True})
bad=[r for r in matched if r['same_formal_question']]
report={'at_utc':now(),'scope':'Every extant standard saved request/binding/start/run/summary JSON below current root runtime and every ZIP member with those standard names. Exact embedded data-URL PNG bytes decoded and hashed. Own preparation outputs excluded. No provider ledger, unsaved/deleted requests or external directories asserted.','targets':targets,'counts':counts,'zip_archives_scanned':[{'path':str(p),'sha256':sha(p)} for p in archives],'same_question_same_exact_PNG_records':bad,'cross_question_exact_PNG_records':[r for r in matched if not r['same_formal_question']],'all_target_question_transport_metadata':allq,'parse_or_read_errors':errors,'zero_saved_prior_actual_calls_proven':not bad and not any(e.get('target_related') for e in errors),'new_API_calls':0}
save('zero_prior_call_scan.json',report)
print(json.dumps({'counts':counts,'zip_archives':len(archives),'same_question_same_image_records':len(bad),'cross_question_records':len(matched)-len(bad),'parse_errors':len(errors),'target_related_errors':sum(bool(e.get('target_related')) for e in errors),'zero_prior':report['zero_saved_prior_actual_calls_proven']}))
