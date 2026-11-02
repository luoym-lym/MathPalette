import task_env
from task_env import OWN,PROJECT
from prepare import read,write,hashfile
import json

records=[]
for n in range(1,14):
    p=OWN.parent/f'batch_{n:02d}/manifest.json'
    m=read(p);entries=[]
    for x in m['candidates']:
        entries.append(x)
    records.append({'batch':f'batch_{n:02d}','manifest_path':str(p),'sha256':hashfile(p),'candidates':entries})
write(OWN/'delivered_references_read.json',records)
for x in records:
    print(x['batch'],json.dumps(x['candidates'],ensure_ascii=False,separators=(',',':'))[:6500])
