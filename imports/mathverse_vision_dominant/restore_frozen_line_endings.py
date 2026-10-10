"""Restore LF only when it exactly matches the existing frozen Base hash.

The Windows checkout introduced CRLF in old sources; no AST/content edits are
allowed here. Preserve the pre-restoration bytes and record both fingerprints.
"""
from pathlib import Path
import hashlib
import json

IMPORT = Path(__file__).resolve().parent
ROOT = IMPORT.parents[1]/'Analytics'/'fine_grained_dataset'
sha = lambda b: hashlib.sha256(b).hexdigest()
audit = []
proposed = []
for number in range(1,21):
    qid = f'Ana{number:02d}'
    source = ROOT/'dataset_generator'/'dataset_generator'/f'function_plot{number:02d}.py'
    relative = source.relative_to(ROOT).as_posix()
    recipes = json.loads((ROOT/'base_variant'/qid/'recipes.json').read_text(encoding='utf-8'))
    expected = {r['baseline']['files'][relative] for r in recipes}
    assert len(expected)==1
    expected = expected.pop()
    before = source.read_bytes()
    normalized = before.replace(b'\r\n',b'\n')
    if sha(before) != expected:
        assert sha(normalized)==expected, f'{qid}: mismatch is not solely CRLF; stop'
        proposed.append((source,before,normalized))
    audit.append({'id':qid,'path':relative,'before_sha256':sha(before),
                  'after_sha256':expected,'change':'CRLF to frozen LF' if sha(before)!=expected else 'unchanged',
                  'only_line_endings_changed':True})
for path,before,normalized in proposed:
    backup = IMPORT/'line_endings_before'/path.name
    backup.parent.mkdir(exist_ok=True)
    if backup.exists():
        assert backup.read_bytes()==before
    else:
        backup.write_bytes(before)
    path.write_bytes(normalized)
target = IMPORT/'line_endings_restoration.json'
if proposed or not target.exists():
    target.write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
print(f'Restored {len(proposed)} old sources to their exact existing recipe hash; mathematical content unchanged.')
