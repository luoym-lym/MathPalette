"""Replay one reviewed runtime candidate without changing formal files.

Usage: python -X utf8 -B runtime/.../batch_01/replay_candidate.py Solid176
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
RUNTIME=(ROOT/'runtime').resolve()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('question_id')
    parser.add_argument('--output')
    args=parser.parse_args()
    manifest=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
    item=next(x for x in manifest['candidates'] if x['question_id']==args.question_id)
    output=Path(args.output).resolve() if args.output else HERE/'reproduced'/(args.question_id+'.png')
    if not output.is_relative_to(RUNTIME):
        raise ValueError('Output must stay within root runtime/')
    for relative,expected in item['input_files'].items():
        if sha(ROOT/relative)!=expected:
            raise ValueError('Frozen input changed: '+relative)
    cache=HERE/'replay_cache'
    for variable,sub in [('MPLCONFIGDIR','mpl'),('TEMP','tmp'),('TMP','tmp'),('XDG_CACHE_HOME','cache')]:
        path=cache/sub;path.mkdir(parents=True,exist_ok=True);os.environ[variable]=str(path)
    sys.path.insert(0,str(HERE))
    from runtime_isolation import install
    install(cache/'render_tmp')
    branch=item['branch']
    sys.path.insert(0,str(ROOT/branch/'workbench'))
    from workbench_io import load_config
    if branch=='PlaneGeometry':
        from mathvision_adapter import RendererAdapter
        from mathvision_plugins import PluginRenderer
    else:
        from delivery_bridge_adapter import RendererAdapter
        from render_plugins import PluginRenderer
    config=load_config()
    config['runtime_dir']=str(cache/'state')
    config['output_dir']=str(cache/'output')
    adapter=RendererAdapter(config)
    qid=args.question_id
    record=adapter.records[qid]
    digest=hashlib.sha256(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
    if digest!=item['record_sha256']:
        raise ValueError('Formal question record changed')
    plugin_path=HERE/qid/'plugin.json'
    if sha(plugin_path)!=item['plugin_sha256']:
        raise ValueError('Reviewed plugin changed')
    metadata=adapter.inspect_question(qid)
    renderer=PluginRenderer(config,adapter,{qid:metadata})
    plugin=json.loads(plugin_path.read_text(encoding='utf-8-sig'))
    normalized,image,pixels=renderer.render(plugin,frozen=True)
    if hashlib.sha256(image).hexdigest()!=item['candidate_sha256']:
        raise ValueError('Replayed PNG differs from reviewed/tested PNG')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes(image)
    print(json.dumps({'question_id':qid,'output':str(output),'matches_tested_png':True,'pixel_sha256':pixels},ensure_ascii=False))

if __name__=='__main__':
    main()
