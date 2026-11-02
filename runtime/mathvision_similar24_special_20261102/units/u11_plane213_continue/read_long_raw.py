from bootstrap import *
d=OWN/'Plane213'/sys.argv[1];i=int(sys.argv[2]);offset=int(sys.argv[3]);length=int(sys.argv[4])
f=next(d.rglob(f'run_{i:02d}_response.json'));r=read(f);answer=r['choices'][0]['message']['content']
print(json.dumps({'raw_path':str(f),'raw_sha256':sha(f),'full_content_characters':len(answer),'slice_offset':offset,'slice_end':min(offset+length,len(answer)),'finish_reason':r['choices'][0]['finish_reason']}))
print(answer[offset:offset+length])
