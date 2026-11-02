from bootstrap import install, OWN, PROJECT, SESSION
ISOLATION = install()
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

IDS = ['Plane480','Plane481','Plane482','Plane483','Plane484','Plane488','Plane489','Plane490']
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def read(path, start=0, end=None):
    path = Path(path)
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    print(json.dumps({'path':str(path.resolve()), 'sha256':sha(path), 'lines':len(lines)}, ensure_ascii=False))
    print('\n'.join(f'{i+1}: {line}' for i,line in enumerate(lines) if i >= start and (end is None or i < end)))
def inventory():
    files = []
    for p in SESSION.rglob('*'):
        if not p.is_file() or p.is_relative_to(OWN):
            continue
        if any(q in p.parts for q in IDS) or p.name in ['checkpoint.json','second_review_queue.json']:
            if any(q in p.parts for q in IDS):
                files.append({'path':str(p.relative_to(PROJECT)), 'size':p.stat().st_size, 'sha256':sha(p)})
    save(OWN/'history_inventory.json', files)
    print(json.dumps(files, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('command', choices=['read','inventory'])
    p.add_argument('path', nargs='?')
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--end',type=int)
    a=p.parse_args()
    if a.command=='read': read(PROJECT/a.path,a.start,a.end)
    if a.command=='inventory': inventory()
