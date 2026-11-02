from research import *
import base64

args=sys.argv[1:]
if args[0]=='history':
    qid=args[1]
    items=read(OWN/'history_inventory.json')['histories'][qid]
    for item in items:
        p=Path(item['path'])
        if p.name not in {'design.json','plugin.json','primary_prescreen.json','assessment.json','process_cleanup.json','run_02_aborted.json'} and not p.name.endswith('_response.json'):
            continue
        print('\nFILE',str(p),'SHA',sha(p))
        raw=p.read_text(encoding='utf-8-sig')
        try: value=json.loads(raw)
        except json.JSONDecodeError:
            print('BAD_JSON_PRESERVED',raw)
        else: print(json.dumps(value,ensure_ascii=False,separators=(',',':')))
elif args[0]=='source':
    for qid in args[1:]:
        record=eligibility(qid)['record']
        print(qid,'FORMAL',json.dumps(record,ensure_ascii=False,separators=(',',':')))
        for rel in [record['scene'],record['script'],*[x for x in record['runtime_dependencies'] if '/items/' in x]]:
            p=BRANCH/rel
            print('SOURCE',rel,'SHA',sha(p))
            text=p.read_text(encoding='utf-8-sig')
            try: print(json.dumps(json.loads(text),ensure_ascii=False,separators=(',',':')))
            except json.JSONDecodeError: print(text)
        print('SOURCE_NOTES',json.dumps(read(PROJECT/'provenance/source_notes.json').get(qid),ensure_ascii=False,separators=(',',':')))
elif args[0]=='report':
    p=SHARED/'independent_review'/args[1]/'independent_review.json'
    value=read(p)
    keys=list(value)
    start=int(args[2]);end=int(args[3])
    for key in keys[start:end]:
        print(key,json.dumps(value[key],ensure_ascii=False,separators=(',',':')))
elif args[0]=='context':
    from delivery_bridge_adapter import RendererAdapter
    from workbench_io import load_config
    from renderer_adapter import scene_png
    config=load_config()
    config['runtime_dir']=str(OWN/'state');config['output_dir']=str(OWN/'output')
    adapter=RendererAdapter(config)
    for qid in args[1:]:
        metadata=adapter.inspect_question(qid)
        dump(OWN/qid/'context.json',metadata)
        scene=adapter.scene(qid)
        try:
            png,pixels=scene_png(scene)
            (OWN/qid/'baseline.png').write_bytes(png)
            dump(OWN/qid/'baseline_check.json',{'noop_pixel_equals_formal':pixels==metadata['original_pixel_sha256'],'png_sha256':sha(OWN/qid/'baseline.png'),'pixel_sha256':pixels,'isolation':ISOLATION})
        finally: scene.close()
        print(qid,json.dumps({'original_pixel_sha256':metadata['original_pixel_sha256'],'snap_points':metadata['snap_points'],'canvas':metadata['canvas'],'objects':[{'id':x['id'],'kind':x.get('type'),'styleable':x.get('styleable'),'paths':[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed']} for p in x.get('partial_paths',[])]} for x in metadata['objects']]},ensure_ascii=False,separators=(',',':')))
elif args[0]=='scene':
    for qid in args[1:]:
        record=eligibility(qid)['record']
        print(qid,json.dumps(read(BRANCH/record['scene']),ensure_ascii=False,separators=(',',':')))
