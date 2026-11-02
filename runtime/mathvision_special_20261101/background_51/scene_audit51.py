from tools51 import *
import numpy as np
from collections import Counter

for qid in IDS:
    e=eligibility(qid); s=read(PROJECT/BRANCH/e['record']['scene'])
    item=read(PROJECT/BRANCH/next(x for x in e['record']['runtime_dependencies'] if x.endswith('/scene.json')))
    differences=[k for k in set(s)|set(item) if s.get(k)!=item.get(k)]
    report=dict(question_id=qid,all_scene_bytes_read=True,formal_and_dependency_differing_keys=differences,
        projection=s['projection'],visibility=s['visibility'],view=s['view'],dimensions=s['dimensions'],
        labels=s['labels'],constraints=s['constraints'],ambiguities=s.get('ambiguities'),
        object_type_counts=dict(Counter(o['type'] for o in s['objects'])),
        objects_full_precision_canonical_sha256=digest(s['objects']),point_count=len(s['points']))
    extra={k:v for k,v in item.items() if k not in ['objects','points','projection','view','visibility','labels','dimensions','constraints']}
    report['dependency_extra_fields']=extra
    write(HERE/qid/'scene_read_audit.json',report)
    print(qid,'scene keys',list(s),'item extra',json.dumps(extra,ensure_ascii=False,separators=(',',':')))
    print('objects',report['object_type_counts'],'differing',differences)
    if qid=='Solid153':
        print('PROFILE OBJECTS',[(o['id'],o['type'],len(o.get('points',[]))) for o in s['objects']])
        print('dependency keys:',list(item))
    if qid=='Solid182':
        print('MESH FACES',[(o['id'],len(o.get('points',[])),o.get('semantic_material')) for o in s['objects'] if o['type']=='face'])
    if qid=='Solid185':
        print('ROUTE',[(o['id'],o['points']) for o in s['objects'] if o['id'].startswith('route')])
