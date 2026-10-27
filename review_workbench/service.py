"""Lazy candidate reads and one-item explicit review transactions."""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

from dataset_tools import catalog, question_review
from dataset_tools.answer_schema import validate_answer
from review_workbench.transactions import Transaction, RecoveryRequired, recover, safe_path, sha

PACKAGE = Path('review_candidates/mathverse')
ID_PATTERN = re.compile(r'MV[0-9]{4,8}\Z')
REQUEST_PATTERN = re.compile(r'[A-Za-z0-9][A-Za-z0-9._:-]{7,127}\Z')
PATH_FIELDS = ('image', 'original_image', 'scene', 'script', 'svg', 'original_script', 'provenance', 'verification', 'candidate_path')
PREFIXES = {'Analytics': 'Ana', 'PlaneGeometry': 'Plane', 'SolidGeometry': 'Solid'}
CATALOG_LOCK_TIMEOUT_SECONDS = 120


class ReviewError(ValueError):
    def __init__(self, message, *, status=400, code='invalid_request'):
        super().__init__(message)
        self.status, self.code = status, code


def json_bytes(data):
    return (json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8')


def json_lines(rows):
    return ''.join(json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n' for row in rows).encode('utf-8')


class ReviewService:
    def __init__(self, root, *, fault=None):
        self.root = Path(root).resolve()
        self.package = safe_path(self.root, PACKAGE)
        self.index_path = safe_path(self.root, PACKAGE / 'index.jsonl')
        self.state_path = safe_path(self.root, PACKAGE / 'review_state.json')
        self.fault = fault
        # Recovery does not approve anything and is serialized against all writers.
        with catalog.catalog_write_lock(self.root, timeout=CATALOG_LOCK_TIMEOUT_SECONDS):
            recover(self.root)
            self._index()

    def _index(self):
        rows = catalog.rows(self.index_path)
        ids = [row.get('id') for row in rows]
        if any(not isinstance(qid, str) or not ID_PATTERN.fullmatch(qid) for qid in ids) or len(ids) != len(set(ids)):
            raise ReviewError('Candidate index has invalid or duplicate IDs', code='invalid_package')
        if any(row.get('subject') not in catalog.BRANCHES for row in rows):
            raise ReviewError('Candidate index has an unknown branch', code='invalid_package')
        return rows

    def _state(self):
        if not self.state_path.exists():
            return {'version': 1, 'decisions': {}, 'requests': {}}
        state = catalog.read(self.state_path)
        if state.get('version') != 1 or not isinstance(state.get('decisions'), dict) or not isinstance(state.get('requests'), dict):
            raise RecoveryRequired('Review state is damaged; do not continue writing')
        return state

    @staticmethod
    def _summary(rows, state):
        decisions = list(state['decisions'].values())
        return {'total': len(rows) + len(decisions), 'pending': len(rows),
                'passed': sum(x['status'] == 'passed' for x in decisions),
                'deleted': sum(x['status'] == 'deleted' for x in decisions)}

    def list_candidates(self):
        with catalog.catalog_write_lock(self.root, timeout=CATALOG_LOCK_TIMEOUT_SECONDS):
            recover(self.root)
            rows, state = self._index(), self._state()
            return {'candidates': [{'id': row['id'], 'branch': row['subject'], 'status': 'pending',
                                    'title': row['question'][:160], 'source_key': row.get('source_key'),
                                    'answer_type': row.get('answer_type')} for row in rows] +
                                  [{**decision, 'title': decision.get('title', decision['id']), 'history': True}
                                   for decision in state['decisions'].values()],
                    'summary': self._summary(rows, state)}

    def _load(self, qid, rows=None):
        if not ID_PATTERN.fullmatch(qid):
            raise ReviewError('Unknown candidate', status=404, code='not_found')
        row = next((r for r in (rows if rows is not None else self._index()) if r['id'] == qid), None)
        if row is None:
            raise ReviewError('Candidate is no longer pending', status=404, code='not_pending')
        item = safe_path(self.root, PACKAGE / 'items' / qid)
        path = safe_path(self.root, PACKAGE / 'items' / qid / 'candidate.json')
        if catalog.read(path) != row:
            raise ReviewError('Candidate metadata differs from its index. Reload a repaired package before reviewing.', status=409, code='candidate_changed')
        if row.get('source_dataset') != 'MathVerse' or not row.get('source_key'):
            raise ReviewError('Candidate source identity is missing', code='invalid_package')
        for field in PATH_FIELDS:
            if not row.get(field):
                continue
            target = safe_path(self.root, row[field])
            if not target.is_relative_to(item) or not target.is_file():
                raise ReviewError(f'Invalid candidate {field} path', code='invalid_package')
        for field in ('image', 'original_image', 'scene', 'script', 'provenance', 'verification'):
            if not row.get(field):
                raise ReviewError(f'Candidate is missing {field}', code='invalid_package')
        family = row.get('renderer_family', '')
        if not re.fullmatch('[a-z_]+', family):
            raise ReviewError('Invalid renderer family', code='invalid_package')
        shared = safe_path(self.root, PACKAGE / 'shared' / family)
        if not shared.is_dir():
            raise ReviewError('Renderer family is missing', code='invalid_package')
        return row, item, shared

    def _fingerprint(self, row, item, shared):
        # Read only this candidate and its actual runtime dependencies.
        files = {}
        for directory in (item, shared):
            for path in sorted(directory.rglob('*')):
                relative = path.relative_to(self.root)
                path = safe_path(self.root, relative)
                if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
                    files[relative.as_posix()] = sha(path.read_bytes())
        for relative in (PACKAGE / 'shared/runtime.py', PACKAGE / 'promotion.py'):
            files[relative.as_posix()] = sha(safe_path(self.root, relative).read_bytes())
        if row['subject'] == 'SolidGeometry' and row['renderer_family'] == 'solid':
            for name in ('common_renderer.py', 'protocol.json'):
                relative = Path('SolidGeometry/dataset_generator') / name
                files[relative.as_posix()] = sha(safe_path(self.root, relative).read_bytes())
        return catalog.digest({'record': row, 'files': files}), files

    def detail(self, qid):
        with catalog.catalog_write_lock(self.root, timeout=CATALOG_LOCK_TIMEOUT_SECONDS):
            recover(self.root)
            decision = self._state()['decisions'].get(qid)
            if decision:
                return {**decision, 'history': True, 'images': {}}
            row, item, shared = self._load(qid)
            fingerprint, files = self._fingerprint(row, item, shared)
            provenance = catalog.read(safe_path(self.root, row['provenance']))
            verification = catalog.read(safe_path(self.root, row['verification']))
            return {**row, 'branch': row['subject'], 'status': 'pending', 'fingerprint': fingerprint,
                    'source_question': row.get('original_question'), 'source_answer': row.get('original_answer'),
                    'provenance_data': provenance, 'verification_data': verification,
                    'images': {kind: f'/api/candidates/{qid}/image/{kind}?sha256={files[row[field]]}'
                               for kind, field in [('source', 'original_image'), ('redraw', 'image')]}}

    def image(self, qid, kind, expected_hash):
        if kind not in ('source', 'redraw') or not re.fullmatch('[0-9a-f]{64}', expected_hash or ''):
            raise ReviewError('Invalid image request')
        with catalog.catalog_write_lock(self.root, timeout=CATALOG_LOCK_TIMEOUT_SECONDS):
            row, _, _ = self._load(qid)
            path = safe_path(self.root, row['original_image' if kind == 'source' else 'image'])
            data = path.read_bytes()
            if sha(data) != expected_hash:
                raise ReviewError('Image changed; reload this candidate', status=409, code='candidate_changed')
            return data, path.suffix.lower()

    def _prepare(self, row, qid):
        path = safe_path(self.root, PACKAGE / 'promotion.py')
        spec = importlib.util.spec_from_file_location('_mathverse_promotion', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        formal, writes, notes = module.prepare(self.root, row, qid)
        if formal.get('id') != qid or formal.get('source_key') != row['source_key']:
            raise ReviewError('Promotion changed candidate identity', code='invalid_package')
        validate_answer(formal)
        for relative in writes:
            target = safe_path(self.root, relative)
            if not target.is_relative_to(self.root / row['subject']):
                raise ReviewError('Promotion attempted to write outside its branch', code='invalid_package')
        for relative in formal.get('runtime_dependencies', []):
            if (Path(row['subject']) / relative).as_posix() not in {Path(p).as_posix() for p in writes}:
                raise ReviewError('Promotion runtime dependency is not packaged', code='invalid_package')
        return formal, writes, notes

    def _verify_redraw(self, branch, formal, writes, directory):
        from PIL import Image
        staged = directory / 'render_check'
        for relative, data in writes.items():
            path = safe_path(staged, relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        output = directory / 'verified.png'
        environment = os.environ.copy()
        environment.update(PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg', MPLCONFIGDIR=str(directory / 'matplotlib'))
        script = staged / branch / formal['script']
        try:
            result = subprocess.run([sys.executable, '-B', str(script), str(output)], cwd=staged,
                                    capture_output=True, text=True, encoding='utf-8', errors='replace',
                                    timeout=60, env=environment)
        except subprocess.TimeoutExpired as error:
            raise ReviewError('This candidate redraw exceeded 60 seconds; no review was saved.', status=422, code='redraw_failed') from error
        if result.returncode or not output.exists():
            raise ReviewError('Candidate cannot be independently redrawn: ' + result.stderr[-1200:], status=422, code='redraw_failed')
        with Image.open(staged / branch / formal['image']) as expected, Image.open(output) as actual:
            if expected.size != (768, 768) or actual.size != expected.size or expected.convert('RGBA').tobytes() != actual.convert('RGBA').tobytes():
                raise ReviewError('Formal redraw pixels differ from the reviewed image. Check the pinned Python/rendering dependencies in review_candidates/mathverse/requirements.txt; no review was saved.', status=422, code='redraw_mismatch')
        catalog.validate_formal_row(staged, branch, formal)

    def decide(self, qid, action, fingerprint, request_id):
        if action not in ('pass', 'delete') or not ID_PATTERN.fullmatch(qid):
            raise ReviewError('Unknown review action')
        if not isinstance(fingerprint, str) or not re.fullmatch('[0-9a-f]{64}', fingerprint):
            raise ReviewError('A current candidate fingerprint is required')
        if not isinstance(request_id, str) or not REQUEST_PATTERN.fullmatch(request_id):
            raise ReviewError('A unique request_id (8–128 characters) is required')
        started = time.perf_counter()
        with catalog.catalog_write_lock(self.root, timeout=CATALOG_LOCK_TIMEOUT_SECONDS):
            recover(self.root)
            protected = [self.index_path, self.state_path, self.root / 'provenance/source_notes.json',
                         self.root / 'provenance/approvals.json', self.root / 'question_bank.jsonl']
            protected += [self.root / b / 'dataset.jsonl' for b in catalog.BRANCHES]
            snapshots = {p: p.read_bytes() if p.exists() else None for p in protected}
            rows, state = self._index(), self._state()
            identity = {'id': qid, 'action': action, 'fingerprint': fingerprint}
            previous = state['requests'].get(request_id)
            if previous:
                if previous['identity'] != identity:
                    raise ReviewError('This request_id was already used for a different action', status=409, code='idempotency_conflict')
                return {**previous['result'], 'replayed': True, 'summary': self._summary(rows, state)}
            if qid in state['decisions']:
                raise ReviewError('This candidate was already reviewed in another tab', status=409, code='already_reviewed')
            row, item, shared = self._load(qid, rows)
            current, _ = self._fingerprint(row, item, shared)
            if current != fingerprint:
                raise ReviewError('Candidate changed since it was displayed. Reload it before deciding.', status=409, code='stale_fingerprint')
            formal_id = None
            transaction = Transaction(self.root, fault=self.fault)
            def publish(path, data):
                path = Path(path)
                transaction.write(path, data, expected_before=snapshots[path])
            try:
                if action == 'pass':
                    branch = row['subject']
                    datasets = {b: catalog.rows(self.root / b / 'dataset.jsonl') for b in catalog.BRANCHES}
                    if any(r.get('source_dataset') == row['source_dataset'] and r.get('source_key') == row['source_key']
                           for records in datasets.values() for r in records):
                        raise ReviewError('This source question is already in the formal bank', status=409, code='duplicate_source')
                    prefix = PREFIXES[branch]
                    numbers = [int(r['id'][len(prefix):]) for r in datasets[branch] if re.fullmatch(prefix + r'[0-9]+', r['id'])]
                    # Deleted formal questions still reserve their assigned IDs.
                    numbers += [int(d['formal_id'][len(prefix):]) for d in state['decisions'].values()
                                if d.get('branch') == branch and
                                re.fullmatch(prefix + r'[0-9]+', d.get('formal_id', ''))]
                    formal_id = f'{prefix}{max(numbers, default=0) + 1:02d}'
                    formal, writes, notes = self._prepare(row, formal_id)
                    self._verify_redraw(branch, formal, writes, transaction.directory)
                    # Defend against local edits while the subprocess was rendering.
                    fresh, _, _ = self._load(qid, self._index())
                    if self._fingerprint(fresh, item, shared)[0] != fingerprint:
                        raise ReviewError('Candidate changed during validation', status=409, code='stale_fingerprint')
                    for path, before in snapshots.items():
                        if (path.read_bytes() if path.exists() else None) != before:
                            raise RecoveryRequired(f'File changed outside the workbench during validation: {path.relative_to(self.root)}')
                    for relative, data in writes.items():
                        path = safe_path(self.root, relative)
                        dependency = (relative.startswith(branch + '/dataset_generator/mathverse_renderers/') or
                                      relative in {branch + '/dataset_generator/common_renderer.py',
                                                   branch + '/dataset_generator/protocol.json'})
                        if path.exists() and dependency:
                            if path.read_bytes() != data:
                                raise ReviewError('A formal renderer differs from this candidate. Existing approved dependencies will not be overwritten.', status=409, code='dependency_conflict')
                            continue
                        transaction.write(path, data, exclusive=True)
                    note_path = self.root / 'provenance/source_notes.json'
                    all_notes = catalog.read(note_path) if note_path.exists() else {}
                    if formal_id in all_notes:
                        raise ReviewError('Formal provenance ID is already reserved', status=409, code='id_conflict')
                    notes['review_action'] = {'candidate_id': qid, 'candidate_fingerprint': fingerprint, 'request_id': request_id,
                                            'action': 'Pass', 'scope': 'original question', 'source_key': row['source_key']}
                    all_notes[formal_id] = notes
                    publish(note_path, json_bytes(all_notes))
                    publish(self.root / branch / 'dataset.jsonl', json_lines(datasets[branch] + [formal]))
                    question_review.approve(branch, [formal_id], 'Pass', self.root, catalog_lock_held=True, publish=publish)
                remaining = [r for r in rows if r['id'] != qid]
                publish(self.index_path, json_lines(remaining))
                status = 'passed' if action == 'pass' else 'deleted'
                decision = {'id': qid, 'status': status, 'branch': row['subject'], 'source_key': row['source_key'],
                            'fingerprint': fingerprint, 'request_id': request_id, 'title': row['question'][:160],
                            'decided_at_utc': datetime.now(timezone.utc).isoformat()}
                if formal_id:
                    decision['formal_id'] = formal_id
                state['decisions'][qid] = decision
                result = {'ok': True, **decision, 'summary': self._summary(remaining, state)}
                state['requests'][request_id] = {'identity': identity, 'result': result}
                publish(self.state_path, json_bytes(state))
                if self._fingerprint(row, item, shared)[0] != fingerprint:
                    raise ReviewError('Candidate changed before the review could be committed', status=409, code='stale_fingerprint')
                transaction.remove_item(item)
                transaction.commit()
                return {**result, 'elapsed_ms': round((time.perf_counter() - started) * 1000, 1)}
            except BaseException:
                transaction.rollback()
                raise
