"""Check candidate completeness, frozen assets, and GitHub Markdown links."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
rows = json.loads((root / 'manifest.json').read_text())
exclusions = json.loads((root / 'language_exclusions.json').read_text())
assert len(rows) == exclusions['active_count']
assert len({row['pid'] for row in rows}) == len(rows)
excluded_ids = {r['pid'] for r in exclusions['excluded']}
assert not excluded_ids.intersection(r['pid'] for r in rows)
assert sum(bool(row['adapted']) for row in rows) == exclusions['active_adaptation_count']
for row in rows:
    assert row['user_approved'] is False
    for key in ('source_question', 'active_question', 'active_choices', 'official_answer'):
        assert not re.search('[\u3400-\u9fff\uf900-\ufaff]', json.dumps(row.get(key), ensure_ascii=False)), (row['pid'], key)
    for path_key, hash_key in (
        ('source_image', 'source_sha256'),
        ('output_image', 'output_sha256'),
        ('adaptation', 'adaptation_sha256'),
    ):
        if row.get(path_key):
            path = root / row[path_key]
            assert path.is_file(), (row['pid'], path_key)
            assert hashlib.sha256(path.read_bytes()).hexdigest() == row[hash_key], (row['pid'], hash_key)
    for key in ('scene', 'reproduction_script', 'report'):
        assert (root / row[key]).is_file(), (row['pid'], key)
    page = (root / row['scene']).parent / 'README.md'
    assert page.is_file(), row['pid']
for page in root.rglob('README.md'):
    for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
        if not target.startswith(('http:', 'https:', '#')):
            assert (page.parent / target).is_file(), (str(page.relative_to(root)), target)
print(f"PASS: {len(rows)} candidates, {sum(bool(r['adapted']) for r in rows)} adaptations, language filter, frozen asset hashes, and Markdown links")
# The offline index and CSV must contain exactly the active manifest IDs.
import csv
html = (root / 'review.html').read_text()
embedded = json.loads(html.split('const data=', 1)[1].split(';const esc=', 1)[0])
assert embedded == rows
with (root / 'review_manifest.csv').open(encoding='utf-8-sig', newline='') as handle:
    csv_ids = [r[0] for r in list(csv.reader(handle))[1:]]
assert csv_ids == [r['pid'] for r in rows]
for pid in excluded_ids:
    assert not any(root.glob(f'*/{pid}/scene.json')), pid
special_source = {r['pid']: r for r in json.loads((root / 'special_source.json').read_text())}
for row in rows:
    parent = (root / row['scene']).parent
    metadata = parent / 'source_metadata.json'
    source = json.loads(metadata.read_text()) if metadata.exists() else special_source[row['pid']]
    for key in ('question', 'query', 'choices', 'answer'):
        assert not re.search('[\u3400-\u9fff\uf900-\ufaff]', json.dumps(source.get(key), ensure_ascii=False)), (row['pid'], key)
for line in (root / 'SHA256SUMS').read_text().splitlines():
    digest, relative = line.split('  ', 1)
    path = root / relative
    assert path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest, relative
print('PASS: offline/CSV indices, excluded directories, source text, and SHA256SUMS')
