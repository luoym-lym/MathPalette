from pathlib import Path
from datetime import datetime, timezone
import base64,hashlib,json,os,sys,zipfile
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
OUT=HERE/'plane213_ebc0b106_prior_call_scan.json'
assert not OUT.exists()
TARGET='ebc0b106f0c272dba6277b1464d5feadf4ffcfc6cdda792db0196e1ff55695c6'
records=[json.loads(s) for s in (ROOT/'PlaneGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
questions={r['id']:r['question'] for r in records}
qtext=questions['Plane213']
started_at=datetime.now(timezone.utc).isoformat()
same=[];cross=[];errors=[];scanned=0;requests=0;zipmembers=0
def digest(raw):return hashlib.sha256(raw).hexdigest()
def inspect(raw,label):
 global scanned,requests
 scanned+=1
 try:d=json.loads(raw.decode('utf-8-sig'))
 except Exception as exc:
  errors.append({'path':label,'error':type(exc).__name__+': '+str(exc)[:160]});return
 if not isinstance(d,dict):return
 sha=d.get('image_sha256')
 q=d.get('question_id')
 if sha==TARGET:
  entry={'path':label,'question_id':q,'path_sha256':digest(raw),'image_sha256':sha,'requested_runs':d.get('requested_runs'),'run_index':d.get('run_index'),'run_id':d.get('run_id'),'status':d.get('status'),'results_status':[r.get('status') for r in d.get('results',[]) if isinstance(r,dict)]}
  if q=='Plane213' or ('Plane213' in Path(label.replace('::','/')).parts and q in (None,'Plane213')):same.append(entry)
  else:cross.append(entry)
 for msg in d.get('messages',[]):
  if not isinstance(msg,dict) or not isinstance(msg.get('content'),list):continue
  parts=msg['content'];texts=[p.get('text') for p in parts if isinstance(p,dict) and p.get('type')=='text']
  for part in parts:
   if not isinstance(part,dict) or part.get('type')!='image_url':continue
   image=part.get('image_url',{})
   url=image.get('url','') if isinstance(image,dict) else ''
   if not url.startswith('data:image/') or ',' not in url:continue
   requests+=1
   try:sha=digest(base64.b64decode(url.split(',',1)[1],validate=True))
   except Exception as exc:
    errors.append({'path':label,'error':type(exc).__name__+': '+str(exc)[:160]});continue
   if sha!=TARGET:continue
   qids=[q for q,text in questions.items() if texts and text==texts[0]]
   entry={'path':label,'request_file_sha256':digest(raw),'image_sha256':sha,'question_ids_by_exact_formal_text':qids,'exact_Plane213_formal_text':bool(texts and texts[0]==qtext)}
   if entry['exact_Plane213_formal_text']:same.append(entry)
   else:cross.append(entry)
def wanted(name):
 return name in ('summary.json','binding.json','request.json') or (name.startswith('run_') and name.endswith('.json') and not name.endswith('_response.json'))
for p in (ROOT/'runtime').rglob('*.json'):
 if wanted(p.name):inspect(p.read_bytes(),p.relative_to(ROOT).as_posix())
for z in (ROOT/'runtime').rglob('*.zip'):
 try:
  with zipfile.ZipFile(z) as archive:
   for name in archive.namelist():
    if wanted(Path(name).name):
     zipmembers+=1;inspect(archive.read(name),z.relative_to(ROOT).as_posix()+'::'+name)
 except Exception as exc:errors.append({'path':z.relative_to(ROOT).as_posix(),'error':type(exc).__name__+': '+str(exc)[:160]})
data={'started_at_utc':started_at,'finished_at_utc':datetime.now(timezone.utc).isoformat(),'question_id':'Plane213','frozen_PNG_sha256':TARGET,'scope':'Current saved standard request/start/run/binding/summary JSON under root runtime/, including all readable ZIP members. Does not claim provider-side or deleted-history absence.','records_scanned':scanned,'embedded_request_images_decoded':requests,'ZIP_members_scanned':zipmembers,'same_question_exact_PNG_transport_matches':same,'cross_question_same_PNG_provenance_only':cross,'parse_errors_not_repaired':errors,'no_saved_same_question_exact_PNG_transport_record':not same,'new_API_calls':0,'cross_ID_image_identity_not_automatic_failure':True}
OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'output':str(OUT),'records':scanned,'requests':requests,'ZIPmembers':zipmembers,'same_Q_exact_PNG_matches':len(same),'cross_Q_matches':len(cross),'parse_errors':len(errors)},ensure_ascii=False))
