"""Disposable original-review fixtures. Never approve or delete delivery candidates."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

PROJECT = Path(__file__).resolve().parents[2]
TEST_NOTE = 'TEMPORARY AUTOMATED TEST FIXTURE; NOT USER APPROVAL'


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def read_rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()]


def write_json(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_rows(path, values):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in values), encoding='utf-8')


def file_hashes(root, *, include_staging=True):
    """Hash durable data and ownership, excluding locks/journals/cache timestamps."""
    root = Path(root)
    result = {}
    for path in root.rglob('*'):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(root)
        if any(part in ('.git', '.env', '.runtime', '__pycache__') for part in rel.parts):
            continue
        if not include_staging and rel.parts[0] == 'staging':
            continue
        result[rel.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


class IsolatedRepository:
    def __init__(self, count=2):
        self.temporary = tempfile.TemporaryDirectory(prefix='mathpalette-original-review-test-')
        self.root = Path(self.temporary.name) / 'repository'
        # Staging is deliberately excluded: real pending candidates can never be
        # passed by this suite, even after the delivery manifest has been added.
        shutil.copytree(PROJECT, self.root, ignore=shutil.ignore_patterns(
            '.git', '.env', '.runtime', 'staging', '__pycache__', '*.pyc', '*.lock'))
        self.staging = self.root / 'staging/solidgeo'
        self.manifest = self.staging / 'candidates.jsonl'
        self.candidates = [self.make_candidate(index + 1) for index in range(count)]
        for row in self.candidates:
            self.seal(row)
        self.save()
        # A local, disposable Git history supplies recoverable candidate assets.
        # No operation ever references the delivery checkout's Git directory.
        self.git('init', '-q')
        self.commit_candidates()

    def git(self, *arguments):
        return subprocess.run(['git', '-C', str(self.root), *arguments], check=True,
                              capture_output=True, text=True)

    def commit_candidates(self):
        self.git('add', '--', 'staging/solidgeo')
        self.git('-c', 'user.name=Automated fixture', '-c', 'user.email=fixture@example.invalid',
                 'commit', '-qm', 'Synthetic test candidates only')

    def close(self):
        self.temporary.cleanup()

    def save(self):
        write_rows(self.manifest, self.candidates)

    def make_candidate(self, number):
        cid = f'SOLIDGEO_TEST_{number:03d}'
        folder = self.staging / 'candidates' / cid
        folder.mkdir(parents=True)
        scene = read_json(self.root / 'SolidGeometry/dataset_generator/scenes/Solid01.json')
        scene.update(id=cid, source_dataset='SOLIDGEO', source_image='source.png')
        write_json(folder / 'scene.json', scene)
        shutil.copy2(self.root / 'SolidGeometry/image/Solid01.png', folder / 'redraw.png')
        shutil.copy2(self.root / 'SolidGeometry/originals/Solid01.png', folder / 'source.png')
        (folder / 'draw.py').write_text(
            '"""' + TEST_NOTE + '; this staging script is never executed by Pass."""\n', encoding='utf-8')
        write_json(folder / 'provenance.json', {'test_fixture': True, 'description': TEST_NOTE})
        row = {
            'id': cid, 'candidate_id': cid, 'source_dataset': 'SOLIDGEO',
            'source_key': f'test-only-{number}',
            'question': 'Find the diagonal y, correct to two decimal places.',
            'answer': '21.61', 'answer_type': 'number',
            'source_answer': '21.61', 'independently_verified_answer': '21.61',
            'verification': {'status': 'verified', 'proof': TEST_NOTE, 'agreement': 'agreement',
                             'agreement_evidence': {'basis': TEST_NOTE}},
            'source_notes': {'test_fixture': True, 'review_note': TEST_NOTE},
            'pass_eligible': True, 'pass_blockers': [], 'user_approved': False,
            'scene_contract': {'valid': True},
            'review_checks': {name: {'status': 'passed'} for name in ('source', 'content', 'answer', 'render')},
        }
        for key, filename in [('scene', 'scene.json'), ('image', 'redraw.png'),
                              ('original_image', 'source.png'), ('drawing_script', 'draw.py'),
                              ('provenance', 'provenance.json')]:
            row[key] = f'candidates/{cid}/{filename}'
        row['paths'] = {alias: f'staging/solidgeo/{row[key]}' for key, alias in
                        [('scene', 'scene'), ('image', 'redraw'), ('original_image', 'original'),
                         ('drawing_script', 'draw'), ('provenance', 'provenance')]}
        row['owned_files'] = list(row['paths'].values())
        return row

    def seal(self, row):
        """Freeze a synthetic fixture's independent-verification baseline."""
        fields = {key: row[key] for key in ('question', 'answer', 'answer_type', 'choices') if key in row}
        row['verification']['candidate_content_sha256'] = hashlib.sha256(json.dumps(
            fields, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
        row['payload_sha256'] = {key: hashlib.sha256((self.staging / row[key]).read_bytes()).hexdigest()
                                 for key in ('scene', 'image', 'original_image', 'drawing_script', 'provenance')}
        return row

    def edit(self, index, changes):
        self.candidates[index].update(copy.deepcopy(changes))
        self.save()
        return self.candidates[index]
