from tools19 import *
cfg, ad = adapter()
for qid in sys.argv[1:]:
    assert qid in ASSIGNED
    out=HERE/qid
    meta=read(out/'context.json')
    record=ad.records[qid]
    p=ROOT/'PlaneGeometry'/record['original_image']
    if p.exists() and not (out/'source_original.jpg').exists():
        (out/'source_original.jpg').write_bytes(p.read_bytes())
    if not (out/'source_scene_snapshot.json').exists():
        (out/'source_scene_snapshot.json').write_bytes((ROOT/'PlaneGeometry'/record['scene']).read_bytes())
    scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw()
        paths={o['id']:[{k:v for k,v in p.items() if k in ('id','sha256','closed','samples','segments','vertices')} for p in object_paths(scene,o['id'])] for o in meta['objects'] if o['styleable']}
        paths=json.loads(json.dumps(paths,default=lambda x:x.tolist() if hasattr(x,'tolist') else str(x)))
        write(out/'path_index_v2.json', paths)
    finally:scene.close()
    print(qid,flush=True)
    for o in meta['objects']:
        g=o.get('geometry',{}); pts=g.get('points',[])
        if len(pts)>10:pts=[pts[0],pts[-1],f'{len(pts)} points']
        print(json.dumps({'id':o['id'],'kind':o.get('kind'),'pts':pts,**{k:g[k] for k in ('center','radius','width','height','start_deg','end_deg') if k in g}},ensure_ascii=False),flush=True)
