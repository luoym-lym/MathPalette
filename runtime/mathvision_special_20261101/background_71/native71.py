from env71 import *
import gc

try:
    result=install_render()
    save('render_isolation.json',result)
    from delivery_bridge_adapter import RendererAdapter
    from workbench_io import load_config,pixel_hash
    from dataset_tools.mathvision_workbench import png_bytes
    from partial_style import object_paths
    adapter=RendererAdapter(load_config())
    for q in QIDS:
        context=adapter.inspect_question(q)
        save(f'{q}/context.json',context)
        capture=adapter.scene(q)
        try:
            png=png_bytes(capture)
            paths={o['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[{'control':s['control'].tolist(),'style':s['style']} for s in p['segments']]} for p in object_paths(capture,o['id'])] for o in context['objects'] if o['styleable']}
        finally: capture.close()
        assert pixel_hash(png)==context['original_pixel_sha256']
        (OWN/q/'no_op.png').write_bytes(png)
        save(f'{q}/frozen_paths.json',paths)
        scene=read(PROJECT/f'SolidGeometry/dataset_generator/scenes/{q}.json')
        save(f'{q}/native_summary.json',{'scene':scene,'objects':context['objects'],'named_snap_points':[p for p in context['snap_points'] if not p['id'].startswith('vertex_')],'baseline_pixels_exact':True,'no_op_sha256':sha(OWN/q/'no_op.png'),'context_sha256':sha(OWN/q/'context.json'),'frozen_paths_sha256':sha(OWN/q/'frozen_paths.json')})
        print(q,'fresh native no-op matches formal pixels;',len(context['objects']),'objects',flush=True)
        del png,context,capture,paths,scene
        gc.collect()
except BaseException as exc:
    save('local_failure.json',{'at':now(),'stage':'fresh_native_inspection','type':type(exc).__name__,'error':str(exc),'API_calls':0,'stop_subsequent_calls':True})
    raise
