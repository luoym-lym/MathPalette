from review_bootstrap import *
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('paths', nargs='+')
args=parser.parse_args()
for arg in args.paths:
    p=(PROJECT/arg).resolve()
    if not p.is_file():
        print(json.dumps({'path':arg,'exists':False}));continue
    obj=read(p)
    if p.name=='request.json':
        for message in obj.get('messages',[]):
            if isinstance(message.get('content'),list):
                for item in message['content']:
                    if item.get('type')=='image_url':
                        import base64
                        raw=base64.b64decode(item['image_url']['url'].split(',',1)[1],validate=True)
                        item['image_url']['url']={'omitted_binary':True,'decoded_length':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'equals_exact_candidate_bytes':raw==(CAND/'candidate.png').read_bytes()}
    if p.name in ('adapter_input_hashes.json','input_fingerprints.json','source_hashes_before.json'):
        print(json.dumps({'path':arg,'sha256':sha(p),'type':type(obj).__name__,'entries':len(obj),'sample':list(obj.items())[:3] if isinstance(obj,dict) else obj[:2]},ensure_ascii=False,indent=2))
    else:
        print(json.dumps({'path':arg,'sha256':sha(p),'full_json':obj},ensure_ascii=False,indent=2))
