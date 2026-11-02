from design_tools import *
for q in sys.argv[1:]:
    r=AD.records[q];p=next(ROOT/'SolidGeometry'/s for s in r['runtime_dependencies'] if s.endswith('/scene.json'))
    sc=json.loads(p.read_text(encoding='utf-8-sig'));print(q)
    print(json.dumps({k:v for k,v in sc.items() if k in ('voxel_model','net_cells','metadata','construction','face_colors','constraints','ambiguities')},ensure_ascii=False,indent=2))
    print('visibility keys',list(sc.get('visibility',{})))
    print(json.dumps({k:v for k,v in sc.get('visibility',{}).items() if k in ('models','surface_models','nets','cells')},ensure_ascii=False,indent=2))
    if q in ('Solid170','Solid187','Solid228','Solid111'):
        for o in sc['objects']:
            if o.get('type')!='face' and (o['id'].startswith(('Eboundary','hole','B','D')) or q=='Solid228'):print(o['id'],o.get('points'),o.get('visibility'))
