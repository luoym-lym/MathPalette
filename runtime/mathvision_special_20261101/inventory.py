import argparse
import hashlib
import json
import os
import stat
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []

def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def inventory():
    result = {}
    for branch in ['PlaneGeometry', 'SolidGeometry']:
        base = ROOT / branch
        rows = read_jsonl(base / 'dataset.jsonl')
        accepted = read_jsonl(base / 'special_variant/accepted_index.jsonl')
        collected = read_jsonl(base / 'special_variant/collected_index.jsonl')
        passed_ids = {r['question_id'] for r in accepted if r.get('status') == 'passed'}
        collected_ids = {r['question_id'] for r in collected if r.get('status') == 'collected'}
        reasons = {}
        for row in rows:
            qid = row['id']
            folder = base / 'special_variant' / qid
            recipe = folder / 'recipes.json'
            if recipe.exists():
                data = json.loads(recipe.read_text(encoding='utf-8-sig'))
                entries = data if isinstance(data, list) else data.get('recipes', data.get('variants', []))
                if isinstance(entries, dict):
                    entries = list(entries.values())
                if any(e.get('status') == 'passed' or e.get('reviewed_at') for e in entries if isinstance(e, dict)):
                    passed_ids.add(qid)
            collection = folder / 'collection.json'
            if collection.exists():
                data = json.loads(collection.read_text(encoding='utf-8-sig'))
                current = data.get('current', {})
                if current.get('status') == 'collected' or current.get('collected_at') or current.get('special_case'):
                    collected_ids.add(qid)
        targets = []
        excluded = []
        for row in rows:
            if row.get('source_dataset') != 'MathVision':
                continue
            qid = row['id']
            why = (['has_passed_variant'] if qid in passed_ids else []) + (['collected_or_special_completed'] if qid in collected_ids else [])
            if why:
                excluded.append({'question_id': qid, 'reasons': why})
            else:
                targets.append(row)
        result[branch] = {'mathvision_total': len(targets) + len(excluded), 'eligible_count': len(targets), 'excluded': excluded, 'eligible': targets}
        (OUT / (branch + '_eligible.jsonl')).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in targets), encoding='utf-8')
    write_json(OUT / 'inventory.json', result)
    print(json.dumps({k:{'total':v['mathvision_total'],'eligible':v['eligible_count'],'excluded':len(v['excluded'])} for k,v in result.items()},ensure_ascii=False))

def scan():
    found = {}
    for parent, dirs, files in os.walk(ROOT):
        if Path(parent) == ROOT:
            dirs[:] = [d for d in dirs if d not in ['.git', 'runtime']]
        for name in files:
            p = Path(parent) / name
            relative = p.relative_to(ROOT).as_posix()
            try:
                info = p.stat()
                if relative.startswith('.runtime/') or not stat.S_ISREG(info.st_mode):
                    found[relative] = {'metadata_only': True, 'size':info.st_size,'mtime_ns':info.st_mtime_ns}
                    continue
                with p.open('rb') as handle:
                    found[relative] = hashlib.file_digest(handle, 'sha256').hexdigest()
            except PermissionError:
                found[relative] = {'unreadable': True, 'size':p.stat().st_size,'mtime_ns':p.stat().st_mtime_ns}
    return found

def baseline():
    path = OUT / 'existing_files_before.json'
    if path.exists():
        raise SystemExit('Baseline already exists; refusing to overwrite')
    files = scan()
    write_json(path, {'timestamp_utc':datetime.now(timezone.utc).isoformat(),'files':files})
    git = subprocess.run(['git','status','--porcelain=v1','-uall'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', check=True).stdout
    (OUT / 'git_status_before.txt').write_text(git, encoding='utf-8')
    print(f'Baseline saved: {len(files)} existing files outside runtime and .git')

def verify():
    before = json.loads((OUT / 'existing_files_before.json').read_text(encoding='utf-8'))['files']
    after = scan()
    changes = {'changed':[p for p in before.keys() & after.keys() if before[p] != after[p]],'deleted':sorted(before.keys()-after.keys()),'added':sorted(after.keys()-before.keys())}
    write_json(OUT / 'existing_files_verification.json', {'timestamp_utc':datetime.now(timezone.utc).isoformat(),'checked_files':len(before),**changes})
    print(json.dumps(changes, ensure_ascii=False))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['inventory','baseline','verify'])
    args=parser.parse_args()
    globals()[args.action]()
