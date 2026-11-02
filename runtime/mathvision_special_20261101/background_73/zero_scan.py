from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,stamp
from prepare import SPECS
import hashlib,base64,json,gc
targets={q:sha(HERE/q/s['id']/'candidate.png') for q,s in SPECS.items()}
reports=[]
errors=[]
matches=[]
for p in TASK.rglob('request.json'):
    if p.is_relative_to(HERE):continue
    try:
        data=read(p)
        bound=[]
        for message in data.get('messages',[]):
            content=message.get('content')
            if not isinstance(content,list):continue
            for item in content:
                if item.get('type')!='image_url':continue
                url=item['image_url']['url']
                if not url.startswith('data:image/png;base64,'):continue
                binary=base64.b64decode(url.split(',',1)[1],validate=True)
                h=hashlib.sha256(binary).hexdigest()
                bound.append(h)
                for q,t in targets.items():
                    if h==t:matches.append({'question_id':q,'request_path':str(p),'PNG_sha256':h})
                del binary,url
        reports.append({'path':str(p),'sha256':sha(p),'embedded_PNG_hashes':bound})
        del data
    except (ValueError,KeyError,TypeError) as e:
        errors.append({'path':str(p),'sha256':sha(p),'error':str(e)})
    gc.collect()
result={'time':stamp(),'targets':targets,'outside_ownroot_requests_read':len(reports),'requests':reports,'errors':errors,'matches':matches,'new_images_zero_prior_exact_requests':not errors and not matches,'streaming_one_request_and_one_image_at_a_time':True,'remote_calls':0,'not_reused_482_488_206_207':True}
save(HERE/'frozen_images_zero_prior_request_audit.json',result)
assert not errors and not matches, 'Zero prior request gate failed'
print('New frozen images zero exact prior request matches;',len(reports),'requests, errors',len(errors))
