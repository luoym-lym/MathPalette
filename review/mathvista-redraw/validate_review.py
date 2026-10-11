"""Check candidate completeness, frozen assets, and GitHub Markdown links."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
rows = json.loads((root / 'manifest.json').read_text())
assert len(rows) == 227
assert len({row['pid'] for row in rows}) == 227
assert sum(bool(row['adapted']) for row in rows) == 11
for row in rows:
    assert row['user_approved'] is False
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
print('PASS: 227 candidates, 11 adaptations, frozen asset hashes, and Markdown links')
