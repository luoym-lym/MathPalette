from own_bootstrap import *

def eligibility(qid):
    from dataset_tools import catalog
    a=next(q for q in load(OWN/'assignment.json')['questions'] if q['question_id']==qid)
    record=next(r for r in catalog.rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']==qid)
    catalog.validate_formal_row(PROJECT,'SolidGeometry',record)
    approval=load(PROJECT/'provenance/approvals.json')['approvals'][qid]
    c=catalog.content(PROJECT,'SolidGeometry',record)
    fingerprint=catalog.digest(c)
    special=PROJECT/'SolidGeometry/special_variant'
    entries={}
    for f in ('accepted_index.jsonl','collected_index.jsonl'):
        entries[f]=[r for r in catalog.rows(special/f) if r.get('question_id',r.get('id'))==qid]
    for f in ('recipes.json','collection.json'):
        p=special/qid/f
        entries[f]=load(p) if p.exists() else None
    source={p:{'expected':h,'actual':sha(PROJECT/p)} for p,h in a['frozen_source_files_sha256'].items()}
    clean=all(v['actual']==v['expected'] for v in source.values())
    okay=(record['source_dataset']=='MathVision' and record==a['formal_record'] and approval==a['approval']
          and fingerprint==approval['content_sha256'] and clean and not any(entries.values()))
    result={'question_id':qid,'checked_at':now(),'record':record,'approval':approval,
        'current_content_sha256':fingerprint,'content_snapshot':c,'source_file_checks':source,
        'special_records':entries,'eligible':okay,
        'inputs_sha256':{p:sha(PROJECT/p) for p in ('SolidGeometry/dataset.jsonl','provenance/approvals.json',
           'provenance/source_notes.json','SolidGeometry/special_variant/accepted_index.jsonl','SolidGeometry/special_variant/collected_index.jsonl')},
        'no_approval_or_state_mutation':True}
    if not okay:
        save(OWN/qid/('HOLD_eligibility_'+now().replace(':','-')+'.json'),result)
        raise ValueError(qid+' eligibility/source changed; hold')
    return result

def render_setup(qid):
    isolation=bridge_setup()
    from delivery_bridge_adapter import RendererAdapter
    from workbench_io import load_config
    from render_plugins import PluginRenderer
    config=load_config(PROJECT/'SolidGeometry/workbench/config.json')
    adapter=RendererAdapter(config)
    context=adapter.inspect_question(qid)
    renderer=PluginRenderer(config,adapter,{qid:context})
    return adapter,renderer,context,isolation

def snapshot():
    paths=('AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json',
       'SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json',
       'SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/renderer_adapter.py',
       'SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/workbench_io.py','SolidGeometry/workbench/config.json',
       'SolidGeometry/workbench/quick_test.py','dataset_tools/mathvision_workbench.py','dataset_tools/catalog.py',
       'runtime/mathvision_special_20261101/runtime_isolation.py','runtime/mathvision_special_20261101/delivery_bridge_adapter.py',
       'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py')
    return {p:sha(PROJECT/p) for p in paths}

if __name__=='__main__':
    save(OWN/'readonly_execution_source_initial.json',snapshot(),exclusive=True)
    for qid in ('Solid166','Solid240'):
        e=eligibility(qid)
        save(OWN/qid/'eligibility_initial.json',e,exclusive=True)
        adapter,renderer,context,isolation=render_setup(qid)
        save(OWN/qid/'context.json',context,exclusive=True)
        from renderer_adapter import scene_png
        capture=adapter.scene(qid)
        try:
            raw,digest=scene_png(capture)
        finally:
            capture.close()
        from workbench_io import pixel_hash,environment_versions
        assert digest==context['original_pixel_sha256']==pixel_hash(PROJECT/'SolidGeometry/image'/f'{qid}.png')
        (OWN/qid/'noop.png').write_bytes(raw)
        save(OWN/qid/'initial_render_gate.json',{'baseline_pixel_sha256':digest,'formal_png_sha256':sha(PROJECT/'SolidGeometry/image'/f'{qid}.png'),
             'noop_png_sha256':sha(OWN/qid/'noop.png'),'environment':environment_versions(),'isolation':isolation,
             'strict_writeguard':str(OWN),'threads':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},
             'source':snapshot(),'no_formal_writes':True},exclusive=True)
        print(qid, 'eligibility OK; no-op pixels OK; context saved',len(context['objects']))
