"""Replay an unmodified candidate twice using the portable delivery adapters."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RUNTIME=(ROOT/'runtime').resolve()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--question',required=True)
    parser.add_argument('--candidate',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    source=Path(args.candidate).resolve()
    output=Path(args.output).resolve()
    if not source.is_relative_to(RUNTIME) or not output.is_relative_to(RUNTIME):
        raise ValueError('All candidate and output paths must stay in root runtime')
    output.mkdir(parents=True,exist_ok=True)
    for variable,sub in [('MPLCONFIGDIR','mpl'),('TEMP','tmp'),('TMP','tmp'),('XDG_CACHE_HOME','cache')]:
        p=output/sub;p.mkdir(exist_ok=True);os.environ[variable]=str(p)
    sys.path.insert(0,str(HERE))
    from runtime_isolation import install
    install(output/'render_tmp')
    branch='PlaneGeometry' if args.question.startswith('Plane') else 'SolidGeometry'
    sys.path.insert(0,str(ROOT/branch/'workbench'))
    from workbench_io import load_config
    if branch=='PlaneGeometry':
        from mathvision_adapter import RendererAdapter
        from mathvision_plugins import PluginRenderer
    else:
        from delivery_bridge_adapter import RendererAdapter
        from render_plugins import PluginRenderer
    config=load_config()
    config['runtime_dir']=str(output/'state')
    config['output_dir']=str(output/'output')
    adapter=RendererAdapter(config)
    record=adapter.records[args.question]
    names={record['image'],record['scene'],record['script'],*record.get('runtime_dependencies',[])}
    if record.get('original_image'):
        names.add(record['original_image'])
    before={name:sha(ROOT/branch/name) for name in names}
    plugin=json.loads((source/'plugin.json').read_text(encoding='utf-8-sig'))
    if plugin['question_id']!=args.question:
        raise ValueError('Candidate question mismatch')
    metadata=adapter.inspect_question(args.question)
    renderer=PluginRenderer(config,adapter,{args.question:metadata})
    normalized,image,pixels=renderer.render(plugin,frozen=True)
    assert image==(source/'candidate.png').read_bytes(),'Replay differs from tested PNG'
    normalized2,image2,pixels2=renderer.render(plugin,frozen=True)
    assert normalized2==normalized and image2==image and pixels2==pixels
    assert {name:sha(ROOT/branch/name) for name in names}==before,'Formal inputs changed'
    (output/'reproduced.png').write_bytes(image)
    result={'question_id':args.question,'branch':branch,'formal_noop_baseline_matches':True,
            'matches_tested_png_bytes':True,'two_delivery_replays_identical':True,
            'formal_inputs_unchanged':True,'png_sha256':hashlib.sha256(image).hexdigest(),
            'pixel_sha256':pixels,'plugin_sha256':sha(source/'plugin.json'),
            'new_solver_calls':0,'quality_review':'Not asserted by this replay validator'}
    (output/'replay_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':
    main()
