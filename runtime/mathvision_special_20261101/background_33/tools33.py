import os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = HERE.parent
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
for key, name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache','XDG_CONFIG_HOME':'config','PYTHONPYCACHEPREFIX':'pycache'}.items():
    path = HERE/name
    path.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(path)
def own_guard(event, args):
    def check(path):
        if path is None or isinstance(path, int): return
        if not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):
            raise PermissionError('background_33 write outside own root: '+str(path))
    if event == 'open':
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'): check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'): check(args[0]); check(args[1])
sys.addaudithook(own_guard)
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(HERE/'render_tmp')
import json, hashlib, copy
from datetime import datetime, timezone
sys.path.insert(0, str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config, canonical_hash, pixel_hash, file_hash, environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools import catalog
ASSIGNED = json.loads((BASE/'background_33_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
BRANCH = 'PlaneGeometry'
def now(): return datetime.now(timezone.utc).isoformat()
def write(path, value):
    path = Path(path); assert path.resolve().is_relative_to(HERE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False); f.write('\n')
def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def rows(path): return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    br = ROOT/BRANCH
    record = next((r for r in rows(br/'dataset.jsonl') if r['id']==qid), None)
    reasons=[]
    if not record or record.get('source_dataset')!='MathVision': reasons.append('not_formal_MathVision')
    approval=read(ROOT/'provenance/approvals.json')['approvals'].get(qid,{})
    current=catalog.digest(catalog.content(ROOT, BRANCH, record)) if record else None
    if approval.get('reviewer')!='user' or not approval.get('instruction') or current!=approval.get('content_sha256'):
        reasons.append('original_approval_missing_or_changed')
    paths=[br/'dataset.jsonl', ROOT/'provenance/approvals.json']
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p=br/'special_variant'/name; paths.append(p)
        if any(r.get('question_id',r.get('id'))==qid for r in rows(p)): reasons.append(name)
    for name in ['recipes.json','collection.json']:
        p=br/'special_variant'/qid/name; paths.append(p)
        if p.exists():
            d=read(p)
            if name=='recipes.json' and d: reasons.append('existing_recipes')
            if name=='collection.json' and d.get('current'): reasons.append('collection_or_special_completion')
    for p in BASE.glob('batch_*/manifest.json'):
        paths.append(p)
        if qid in p.read_text(encoding='utf-8-sig'): reasons.append('delivered:'+p.parent.name)
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),
            'formal_record':record,'original_approval':approval,'current_original_content_sha256':current,
            'original_approval_fingerprint_matches':current==approval.get('content_sha256'),
            'authoritative_state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},
            'diagnostic_mutable_progress_hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in [BASE/'remaining_questions.jsonl',BASE/'exploration_report.json']}}
def adapter():
    cfg=load_config(); cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg, RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid]; br=ROOT/BRANCH
    paths=[br/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths+=list(ad.input_files.values())
    paths+=[ROOT/p for p in ['MATHPALETTE_PROTOCOL.md','AGENTS.md','dataset_tools/mathvision_workbench.py','dataset_tools/geometry_dataset.py']]
    paths+=[br/p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/config.json','workbench/plugin.schema.json','workbench/render_plugins.py','workbench/mathvision_adapter.py','workbench/mathvision_plugins.py','workbench/partial_style.py','workbench/renderer_adapter.py','workbench/workbench_io.py']]
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all():
    cfg,ad=adapter()
    for q in ASSIGNED:
        out=HERE/q; check=eligibility(q); write(out/'eligibility_start.json',check)
        assert check['eligible'], check
        before=inputs(ad,q); ctx=ad.inspect_question(q)
        write(out/'context.json',ctx);write(out/'formal_record.json',ad.records[q]);write(out/'input_fingerprints.json',before)
        (out/'original.png').write_bytes(ad.original_paths[q].read_bytes())
        br=ROOT/BRANCH;r=ad.records[q]
        (out/'source_scene_snapshot.json').write_bytes((br/r['scene']).read_bytes())
        if r.get('original_image'): (out/'source_original.jpg').write_bytes((br/r['original_image']).read_bytes())
        assert before==inputs(ad,q)
        write(out/'baseline_check.json',{'fresh_inspect_question':True,'no_op_pixel_equal_to_formal':True,'inputs_unchanged':True,'isolation':ISOLATION})
        print(q,'objects',len(ctx['objects']),'snaps',len(ctx['snap_points']),flush=True)
if __name__=='__main__': inspect_all()
