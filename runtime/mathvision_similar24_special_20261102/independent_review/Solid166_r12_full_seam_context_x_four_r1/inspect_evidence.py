from review_bootstrap import *

def inspect():
    assignment = load(UNIT / 'assignment.json')
    relevant = assignment['questions'][0]
    paths = list(relevant['frozen_source_files_sha256'])
    paths += ['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md',
              'SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md',
              'SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json',
              'SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/renderer_adapter.py',
              'SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/workbench_io.py',
              'SolidGeometry/workbench/config.json','SolidGeometry/workbench/quick_test.py',
              'dataset_tools/catalog.py','dataset_tools/mathvision_workbench.py']
    frozen = [PROJECT / p for p in paths]
    frozen += [p for p in UNIT.rglob('*') if p.is_file()]
    frozen += [p for p in (TASK / 'references/Solid203').rglob('*') if p.is_file()]
    frozen += [p for p in (TASK / 'parent_audits/native_u09').rglob('*') if p.is_file()]
    frozen += [OLD / p for p in ('runtime_isolation.py','delivery_bridge_adapter.py','harness/quicktest3_isolated.py')]
    frozen += [TASK / p for p in ('task.json','reference_style_summary.json','history_index.json',
                                'parent_review_preflight.json','parent_imitation_priority_20261102.txt')]
    frozen += [PROJECT / 'SolidGeometry/special_variant/Solid203' / p for p in ('images/C01.png','plugins/C01.json','recipes.json')]
    hashes = {str(p):sha(p) for p in sorted(set(frozen))}
    if not (OWN/'scoped_preservation_initial.json').exists():
        save('scoped_preservation_initial.json', {'at':now(), 'sha256':hashes,
              'scope':'Solid166 formal dependencies; complete u09 finite evidence; current reference; approved replay helpers; relevant parent audits. Mutable unrelated workspace excluded.'})
    print('Snapshot file count', len(hashes))
    for label, path in [
        ('parent_audit', TASK/'parent_audits/native_u09/audit.json'),
        ('primary_review', CANDIDATE/'primary_review.json'),
        ('history_index',TASK/'history_index.json'),
        ('primary_report',UNIT/'primary_report.json'),
        ('source_preservation',UNIT/'source_preservation_final.json'),
        ('scene',PROJECT/'SolidGeometry'/relevant['formal_record']['scene']),
        ('native_scene',PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Solid166/scene.json'),
    ]:
        v = load(path)
        print(label, 'keys', list(v) if isinstance(v,dict) else 'list ' + str(len(v)))
    print('formal', canonical(relevant['formal_record']))
    print('scenespec', (PROJECT/'SolidGeometry'/relevant['formal_record']['scene']).read_text(encoding='utf-8'))
    print('primary_visual', canonical(load(CANDIDATE/'primary_visual_review.json')))
    print('color_legibility',canonical(load(CANDIDATE/'primary_color_group_legibility.json')))
    print('reference_transfer',canonical(load(CANDIDATE/'reference_transfer.json')))
    print('history_difference',canonical(load(CANDIDATE/'history_difference.json')))

if __name__ == '__main__':
    main(inspect)
