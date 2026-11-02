from bootstrap import *
import json
import hashlib
import shutil
from datetime import datetime, timezone
from dataset_tools.catalog import content, digest

IDS = ['Solid153', 'Solid158', 'Solid180', 'Solid182', 'Solid183', 'Solid185', 'Solid194', 'Solid202']
BRANCH = 'SolidGeometry'
def now(): return datetime.now(timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p): return [json.loads(x) for x in Path(p).read_text(encoding='utf-8-sig').splitlines() if x.strip()] if Path(p).is_file() else []
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, value):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False); f.write('\n')
def eligibility(qid):
    assert qid in IDS
    branch = PROJECT / BRANCH
    record = next(r for r in rows(branch/'dataset.jsonl') if r['id'] == qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'].get(qid, {})
    payload = content(PROJECT, BRANCH, record)
    accepted = [r for r in rows(branch/'special_variant/accepted_index.jsonl') if r.get('question_id', r.get('id')) == qid]
    collected = [r for r in rows(branch/'special_variant/collected_index.jsonl') if r.get('question_id', r.get('id')) == qid]
    special = branch/'special_variant'/qid
    plugins = list((special/'plugins').glob('*.json'))
    images = list((special/'images').glob('*.png'))
    collection = read(special/'collection.json') if (special/'collection.json').is_file() else None
    rootrow = next(r for r in rows(PROJECT/'question_bank.jsonl') if r['id'] == qid)
    valid = approval.get('reviewer') == 'user' and bool(approval.get('instruction')) and bool(approval.get('approved_at_utc')) and digest(payload) == approval.get('content_sha256')
    eligible = record['source_dataset'] == 'MathVision' and valid and not accepted and not collected and not plugins and not images and not (collection and collection.get('current')) and not rootrow.get('special_plugins')
    return dict(checked_at=now(), question_id=qid, branch=BRANCH, record=record,
                question_record_sha256=digest(record), approval=approval, current_content_sha256=digest(payload),
                approval_matches_current=valid, accepted_records=accepted, collected_records=collected,
                formal_plugin_files=[str(p) for p in plugins], formal_special_images=[str(p) for p in images],
                collection=collection, root_index_special_plugins=rootrow.get('special_plugins'), eligible=eligible, frozen_content=payload)
def frozen_files(record):
    branch = PROJECT/BRANCH
    paths = [branch/p for p in content(PROJECT,BRANCH,record)['files']]
    paths += [PROJECT/'provenance/approvals.json', PROJECT/'MATHPALETTE_PROTOCOL.md',
              PROJECT/'dataset_tools/mathvision_workbench.py', BASE/'delivery_bridge_adapter.py', BASE/'runtime_isolation.py', BASE/'harness/quicktest3_isolated.py']
    paths += list((branch/'workbench').glob('*.py'))
    paths += [branch/'workbench/plugin.schema.json', branch/'workbench/config.json']
    return {str(p.relative_to(PROJECT)).replace('\\','/'):sha(p) for p in paths}
def setup():
    sys.path.insert(0,str(PROJECT/BRANCH/'workbench'))
    from workbench_io import load_config
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    cfg=load_config(); cfg['runtime_dir']=str(HERE/'state'); cfg['output_dir']=str(HERE/'output')
    return RendererAdapter(cfg), PluginRenderer, cfg
def inspect(qid):
    adapter,_,_=setup()
    from PIL import Image
    from partial_style import object_paths
    from dataset_tools.mathvision_workbench import png_bytes
    d=HERE/qid; d.mkdir(parents=True,exist_ok=True)
    e=eligibility(qid); write(d/'eligibility_initial.json',e); assert e['eligible']
    record=e['record']; write(d/'source_hashes_initial.json',frozen_files(record)); write(d/'formal_record.json',record)
    context=adapter.inspect_question(qid); write(d/'context.json',context)
    scene=adapter.scene(qid)
    try:
        data=png_bytes(scene); (d/'baseline.png').write_bytes(data)
        with Image.open(PROJECT/BRANCH/record['image']) as a, Image.open(d/'baseline.png') as b:
            assert a.size==b.size==(768,768) and a.convert('RGBA').tobytes()==b.convert('RGBA').tobytes()
        scene.fig.canvas.draw()
        paths={}
        for obj in context['objects']:
            if obj.get('styleable'):
                paths[obj['id']]=[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,obj['id'])]
        write(d/'exact_paths.json',paths)
    finally: scene.close()
    write(d/'baseline_check.json',dict(no_op_pixel_equal=True,baseline_sha256=sha(d/'baseline.png'),formal_png_sha256=sha(PROJECT/BRANCH/record['image']),isolation=ISOLATION))
    print(qid, 'eligible; exact no-op; objects',len(context['objects']),flush=True)
def render(spec):
    adapter,Renderer,cfg=setup()
    from workbench_io import environment_versions
    qid=spec['question_id']; assert qid in IDS
    d=HERE/qid/spec['name']; d.mkdir(parents=True,exist_ok=False)
    write(d/'design_difference_audit.json',spec['difference_audit'])
    e=eligibility(qid);write(d/'eligibility_before_render.json',e);assert e['eligible']
    context=adapter.inspect_question(qid);write(d/'context.json',context)
    plugin=dict(plugin_schema_version='1.0.0',question_id=qid,category='C',operation='C_manual',description=spec['description'],intent=spec['mechanism'],params={'actions':spec['actions']})
    renderer=Renderer(cfg,adapter,{qid:context})
    normalized,data,pixels=renderer.render(plugin)
    normalized2,data2,pixels2=renderer.render(normalized,frozen=True)
    assert normalized==normalized2 and data==data2 and pixels==pixels2
    (d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2);write(d/'plugin.json',normalized)
    design={k:v for k,v in spec.items() if k not in ('actions','difference_audit')}
    design.update(created_at=now(),plugin_sha256=sha(d/'plugin.json'),png_sha256=sha(d/'candidate.png'),pixel_sha256=pixels,approval_status='PRIMARY ONLY; parent NEW independent review required; no Pass/Collect')
    write(d/'design.json',design)
    write(d/'render_check.json',dict(actual_schema_and_normalization=True,twice_byte_identical=True,pixel_sha256=pixels,environment=environment_versions(),frozen_source_files=frozen_files(e['record'])))
    print(qid,spec['name'],sha(d/'candidate.png'),flush=True)
if __name__ == '__main__':
    if sys.argv[1]=='inspect':
        for qid in sys.argv[2:]: inspect(qid)
    elif sys.argv[1]=='render': render(read(sys.argv[2]))
