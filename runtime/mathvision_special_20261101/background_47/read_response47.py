from env47 import *
import json
qid=sys.argv[1];index=int(sys.argv[2]);offset=int(sys.argv[3]);limit=int(sys.argv[4])
root=next((OWN/qid).glob('r47_*'))
p=next((root/'tests').glob(f'*/run_{index:02d}_response.json'))
d=json.loads(p.read_text(encoding='utf-8'))
s=d['choices'][0]['message']['content']
print(json.dumps({'path':str(p),'sha256':sha(p),'full_content_chars':len(s),'show_offset':offset,'show_length':min(limit,len(s)-offset),'finish_reason':d['choices'][0]['finish_reason']}))
print(s[offset:offset+limit])
