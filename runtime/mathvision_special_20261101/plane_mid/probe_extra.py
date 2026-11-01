from design import HERE,RendererAdapter,load_config,json
config=load_config()
config['runtime_dir']=str(HERE/'render_runtime')
config['output_dir']=str(HERE/'render_output')
adapter=RendererAdapter(config)
for qid in ['Plane248','Plane266','Plane234','Plane296','Plane277','Plane263','Plane224']:
    m=adapter.inspect_question(qid)
    (HERE/(qid+'_context.json')).write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
    print(qid,[(o['id'],o['kind']) for o in m['objects']],flush=True)
