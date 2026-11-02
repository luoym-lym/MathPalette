import own_runtime as rt
from pathlib import Path
import json
import sys

task = rt.OWN.parents[1]
assignment = rt.read(rt.OWN/'assignment.json')
index = rt.read(task/'history_index.json')
audit = []
refs = {}
for qid, entry in rt.read(task/'reference_manifest.json').items():
    d = task/entry['directory']
    values = {}
    for name in ('C01.json','recipes.json','reference.json'):
        p=d/name
        values[name]=rt.read(p)
        audit.append({'path':str(p),'sha256':rt.sha(p),'bytes':p.stat().st_size,'fully_parsed':True})
    assert rt.sha(d/'C01.png') == entry['png_sha256']
    assert rt.sha(d/'C01.json') == entry['plugin_sha256']
    refs[qid]=values
rt.save(rt.OWN/'reference_read_audit.json',{'files':audit,'data':refs})

def paths(node):
    if isinstance(node,dict):
        for k,v in node.items():
            yield from paths(v)
    elif isinstance(node,list):
        for v in node: yield from paths(v)
    elif isinstance(node,str):
        s=node.split('#')[0]
        if s.startswith('runtime/') and (rt.PROJECT/s).is_file(): yield s

history={}
all_files=[]
for q in index['questions']:
    if q['question_id'] not in assignment['question_ids']: continue
    data=[]
    for rel in sorted(set(paths(q))):
        p=rt.PROJECT/rel
        record={'path':rel,'sha256':rt.sha(p),'bytes':p.stat().st_size}
        if p.suffix == '.json':
            try:
                obj=rt.read(p)
                record['fully_parsed']=True
                # Request image is checked without retaining huge base64 in the reading report.
                if p.name=='request.json':
                    import base64,hashlib
                    for msg in obj.get('messages',[]):
                        if isinstance(msg.get('content'),list):
                            for item in msg['content']:
                                if item.get('type')=='image_url':
                                    raw=base64.b64decode(item['image_url']['url'].split(',',1)[1])
                                    item['image_url']={'decoded_image_sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
                                    del raw
                record['content']=obj
            except (ValueError,UnicodeError) as e:
                record['parse_error_preserved']=str(e)
        data.append(record)
        all_files.append({k:v for k,v in record.items() if k!='content'})
    history[q['question_id']]={'index':q,'fully_read_files':data}
rt.save(rt.OWN/'history_read_audit.json',{'created_at':rt.now(),'questions':history,'file_count':len(all_files)})
rt.save(rt.OWN/'readonly_inputs_initial.json',{'files':audit+all_files,'assignment_sha256':rt.sha(rt.OWN/'assignment.json'),'brief_sha256':rt.sha(rt.OWN/'brief.txt')})
mode=sys.argv[1] if len(sys.argv)>1 else 'summary'
if mode=='references':
    for q,v in refs.items():
        print(q,json.dumps(v,ensure_ascii=False))
elif mode=='history':
    for q,v in history.items():
        print('\nQUESTION',q)
        for item in v['fully_read_files']:
            p=Path(item['path'])
            if (p.name=='design.json' or p.name.endswith('_response.json') or
                ('review' in p.name and 'context' not in p.name) or 'proof' in p.name or
                'aborted' in p.name or 'blocked' in p.name):
                print(item['path'],json.dumps(item.get('content',item),ensure_ascii=False))
else:
    for q,v in history.items():
        ix=v['index']
        print(q,'designs',len(ix['designs']),'read_files',len(v['fully_read_files']))
        for d in ix['designs']:
            print('DESIGN',d['variant_id'],'preset',d.get('predeclared_wrong_answer'),'calls',d.get('unique_started_call_count_from_saved_records'))
        print('REVIEW REFERENCES',json.dumps(ix.get('independent_review_references'),ensure_ascii=False))
    print('refs fully read:',len(refs),'history fully read:',len(all_files))
