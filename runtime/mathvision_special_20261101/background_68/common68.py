from bootstrap import *
import gc
import hashlib
import json
from datetime import datetime, timezone

IDS = ['Plane271', 'Plane367', 'Plane387', 'Plane449']
BRANCH = 'PlaneGeometry'
def now(): return datetime.now(timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p):
    if Path(p).is_file():
        with Path(p).open(encoding='utf-8-sig') as f:
            for line in f:
                if line.strip(): yield json.loads(line)
def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''): h.update(block)
    return h.hexdigest()
def write(p, v):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(v, f, ensure_ascii=False, indent=2, allow_nan=False); f.write('\n')
def eligibility(qid):
    from dataset_tools.catalog import content, digest
    assert qid in IDS
    b = PROJECT/BRANCH
    r = next(r for r in rows(b/'dataset.jsonl') if r['id'] == qid)
    a = read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    c = content(PROJECT, BRANCH, r)
    accepted = [r for r in rows(b/'special_variant/accepted_index.jsonl') if r.get('question_id', r.get('id')) == qid]
    collected = [r for r in rows(b/'special_variant/collected_index.jsonl') if r.get('question_id', r.get('id')) == qid]
    special = b/'special_variant'/qid
    recipe = read(special/'recipes.json') if (special/'recipes.json').is_file() else None
    collection = read(special/'collection.json') if (special/'collection.json').is_file() else None
    files = [str(p) for leaf, glob in [('images','*.png'),('plugins','*.json')] for p in (special/leaf).glob(glob)]
    root = next(r for r in rows(PROJECT/'question_bank.jsonl') if r['id'] == qid)
    valid = a.get('reviewer') == 'user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and digest(c) == a.get('content_sha256')
    return dict(question_id=qid, checked_at=now(), record=r, approval=a, current_content_sha256=digest(c), approval_matches_current=valid,
        no_passed_variant=not accepted and not recipe and not files and not root.get('special_plugins'),
        not_collected=not collected and not (collection and collection.get('current')), accepted=accepted, collected=collected,
        recipe=recipe, collection=collection, formal_special_files=files, root_special_plugins=root.get('special_plugins'),
        authoritative_hashes={str(p.relative_to(PROJECT)):sha(p) for p in [b/'dataset.jsonl', PROJECT/'provenance/approvals.json', b/'special_variant/accepted_index.jsonl', b/'special_variant/collected_index.jsonl']},
        eligible=r['source_dataset'] == 'MathVision' and valid and not accepted and not collected and not recipe and not files and not (collection and collection.get('current')) and not root.get('special_plugins'), frozen_content=c)

def setup():
    sys.path.insert(0, str(PROJECT/BRANCH/'workbench'))
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    cfg = load_config(); cfg['runtime_dir'] = str(HERE/'state'); cfg['output_dir'] = str(HERE/'output')
    return RendererAdapter(cfg), PluginRenderer, cfg
