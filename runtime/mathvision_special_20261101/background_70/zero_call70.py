from env70 import *
from design70 import NAMES,directory
import base64
import binascii
import gc

targets={qid:sha(directory(qid)/'candidate.png') for qid in NAMES}
png_matches={qid:[] for qid in targets}; request_matches={qid:[] for qid in targets}
malformed=[]; errors=[]; malformed_embedded=[]; embedded_count=0; json_count=0; png_count=0
read_bindings=[]
started=now()

def inspect(value,path,jpath=''):
    global embedded_count
    if isinstance(value,dict):
        for k,v in value.items():inspect(v,path,jpath+'/'+k)
    elif isinstance(value,list):
        for i,v in enumerate(value):inspect(v,path,jpath+'/'+str(i))
    elif isinstance(value,str) and value.startswith('data:image/png;base64,'):
        encoded=value.split(',',1)[1]
        try:
            data=base64.b64decode(encoded,validate=True)
        except binascii.Error as exc:
            item={'path':str(path),'json_path':jpath,'file_sha256':sha(path),
                  'encoded_length':len(encoded),'encoded_sha256':hashlib.sha256(encoded.encode()).hexdigest(),
                  'error':str(exc),'prefix':encoded[:60],'suffix':encoded[-60:]}
            malformed_embedded.append(item)
            print(json.dumps({'malformed_embedded':item}),flush=True)
            return
        digest=hashlib.sha256(data).hexdigest();del data
        embedded_count+=1
        for qid,target in targets.items():
            if digest==target:request_matches[qid].append({'path':str(path),'json_path':jpath,'sha256':sha(path)})

for p in BASE.rglob('*'):
    if p.is_relative_to(OWN) or not p.is_file():continue
    if p.suffix.lower()=='.png':
        png_count+=1;digest=sha(p)
        for qid,target in targets.items():
            if digest==target:png_matches[qid].append(str(p))
    elif p.suffix.lower()=='.json':
        json_count+=1
        try:
            value=read(p);inspect(value,p)
            if p.name=='binding.json':
                read_bindings.append({'path':str(p),'sha256':sha(p),'question_id':value.get('question_id'),
                                      'image_sha256':value.get('image_sha256')})
            del value
        except (json.JSONDecodeError,UnicodeDecodeError) as exc:
            malformed.append({'path':str(p),'sha256':sha(p),'error':str(exc),'preserved_readonly':True})
        except FileNotFoundError as exc:
            errors.append({'path':str(p),'error':str(exc),'classification':'concurrent runtime file disappeared; no restoration'})
        gc.collect()
report={'started_at':started,'finished_at':now(),'scope':'Entire task runtime outside OWNROOT, one JSON/PNG at a time. Embedded PNGs decoded and released immediately.',
        'new_frozen_PNG_hashes':targets,'JSON_files_fully_read':json_count,'PNG_files_hashed':png_count,
        'embedded_PNGs_decoded':embedded_count,'same_PNG_old_files':png_matches,'same_PNG_old_JSON':request_matches,
        'all_old_bindings':read_bindings,'malformed_JSON_preserved':malformed,'concurrent_diagnostic_errors':errors,
        'malformed_embedded_PNG_strings_preserved':malformed_embedded,
        'zero_exact_old_PNG_requests_and_files':not any(png_matches.values()) and not any(request_matches.values()),
        'limitation':'Filesystem evidence cannot certify absence of unrecorded external calls. This is a time-bounded scan; current pre-call checks also bind own files and authoritative eligibility.'}
save('global_new_PNG_zero_call_audit.json',report)
assert report['zero_exact_old_PNG_requests_and_files']
print(json.dumps({k:report[k] for k in ('JSON_files_fully_read','PNG_files_hashed','embedded_PNGs_decoded','zero_exact_old_PNG_requests_and_files')}))
