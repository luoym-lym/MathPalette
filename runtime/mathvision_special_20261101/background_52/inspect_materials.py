from bootstrap import install, OWN, PROJECT, SESSION
install()
from research import load, save, sha, IDS
import sys,json

for qid in sys.argv[1:]:
    row=load(OWN/qid/'formal_record.json')
    scene=load(PROJECT/'PlaneGeometry'/row['scene'])
    material=[]
    for rel in [row['scene'],row['script']]+[p for p in row['runtime_dependencies'] if '/items/' in p]:
        p=PROJECT/'PlaneGeometry'/rel
        s=p.read_text(encoding='utf-8-sig')
        material.append({'path':str(p),'sha256':sha(p),'content':json.loads(s) if p.suffix=='.json' else s})
    save(OWN/qid/'full_source_materials.json',material)
    sources=[x['content'] for x in material if x['path'].endswith('source.json')]
    reviews=[x['content'] for x in material if x['path'].endswith('protocol_review.json')]
    print(json.dumps({'qid':qid,'formal_scene':scene,'upstream_full':sources,'source_protocol_review':reviews},ensure_ascii=False,separators=(',',':')))
