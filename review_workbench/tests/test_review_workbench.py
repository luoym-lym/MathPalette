"""All review mutations below use temporary independent copies, never ROOT."""
from __future__ import annotations
import hashlib
import http.client
import json
import multiprocessing
import os
from pathlib import Path
import shutil
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

from dataset_tools import catalog
from review_workbench.service import ReviewService, ReviewError, PACKAGE
from review_workbench.server import ReviewHTTPServer
from review_workbench.transactions import Transaction, RecoveryRequired, recover

ROOT = Path(__file__).resolve().parents[2]
IGNORE = shutil.ignore_patterns('.git', '.env', '.runtime', '__pycache__', '*.pyc', '*.tmp', '*.lock')


def copy_fixture(destination, *, all_candidates=False):
    destination = Path(destination)
    destination.mkdir(parents=True)
    for name in ('Analytics', 'PlaneGeometry', 'SolidGeometry', 'provenance', 'dataset_tools', 'review_workbench'):
        shutil.copytree(ROOT / name, destination / name, ignore=IGNORE)
    shutil.copy2(ROOT / 'question_bank.jsonl', destination / 'question_bank.jsonl')
    package = destination / PACKAGE
    package.mkdir(parents=True)
    for file in (ROOT / PACKAGE).iterdir():
        if file.is_file() and file.name != 'review_state.json':
            shutil.copy2(file, package / file.name)
    shutil.copytree(ROOT / PACKAGE / 'shared', package / 'shared', ignore=IGNORE)
    rows = catalog.rows(ROOT / PACKAGE / 'index.jsonl')
    if not all_candidates:
        selected, counts = [], {}
        for row in rows:
            family = row['renderer_family']
            if counts.get(family, 0) < (3 if family == 'plane' else 1):
                selected.append(row)
                counts[family] = counts.get(family, 0) + 1
        rows = selected
        (package / 'index.jsonl').write_bytes(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows).encode())
    for row in rows:
        shutil.copytree(ROOT / PACKAGE / 'items' / row['id'], package / 'items' / row['id'], ignore=IGNORE)
    return rows


def checksum(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mutation_worker(root, qid, action, request_id, queue=None, start=None, fault_label=None):
    def fault(label):
        if label == fault_label:
            os._exit(83)
    try:
        service = ReviewService(root, fault=fault if fault_label else None)
        fingerprint = service.detail(qid)['fingerprint']
        if start:
            start.wait(20)
        result = service.decide(qid, action, fingerprint, request_id)
        if queue:
            queue.put(('ok', result))
    except Exception as error:
        if queue:
            queue.put(('error', type(error).__name__, str(error)))
        else:
            raise


class WorkbenchTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='mathverse-review-test-')
        self.root = Path(self.temporary.name) / 'project'
        self.rows = copy_fixture(self.root)
        self.service = ReviewService(self.root)
        self.original_count = len(catalog.rows(self.root / 'question_bank.jsonl'))

    def tearDown(self):
        self.temporary.cleanup()

    def test_list_is_lazy_and_detail_never_renders(self):
        with patch.object(self.service, '_fingerprint', side_effect=AssertionError('full hash not allowed')):
            result = self.service.list_candidates()
        self.assertEqual(result['summary']['pending'], len(self.rows))
        with patch.object(self.service, '_verify_redraw', side_effect=AssertionError('GET rendered')):
            detail = self.service.detail(self.rows[0]['id'])
        self.assertEqual(len(detail['fingerprint']), 64)
        self.assertIn('sha256=', detail['images']['source'])
        self.assertFalse((self.root / PACKAGE / 'review_state.json').exists())
        self.assertEqual(len(catalog.catalog(self.root)), self.original_count)

    def test_full_catalog_reads_notes_once_but_rechecks_on_every_call(self):
        notes_path = self.root / 'provenance/source_notes.json'
        original_read = catalog.read
        reads = []
        def tracked(path):
            if Path(path) == notes_path:
                reads.append(path)
            return original_read(path)
        with patch.object(catalog, 'read', side_effect=tracked):
            self.assertEqual(catalog.catalog(self.root), catalog.rows(self.root / 'question_bank.jsonl'))
        self.assertEqual(len(reads), 1)
        notes = catalog.read(notes_path)
        notes['Ana01']['test_change_after_previous_build'] = True
        notes_path.write_text(json.dumps(notes), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'approved content changed'):
            catalog.catalog(self.root)

    def test_delete_is_local_idempotent_and_removes_files(self):
        first, second = self.rows[:2]
        detail = self.service.detail(first['id'])
        original = checksum(self.root / 'question_bank.jsonl')
        other = checksum(self.root / second['image'])
        with patch.object(self.service, '_verify_redraw', side_effect=AssertionError('Delete rendered')):
            result = self.service.decide(first['id'], 'delete', detail['fingerprint'], 'delete-request-1')
            replay = self.service.decide(first['id'], 'delete', detail['fingerprint'], 'delete-request-1')
        self.assertTrue(replay['replayed'])
        self.assertEqual(result['summary']['deleted'], 1)
        self.assertFalse((self.root / PACKAGE / 'items' / first['id']).exists())
        self.assertEqual(original, checksum(self.root / 'question_bank.jsonl'))
        self.assertEqual(other, checksum(self.root / second['image']))
        self.assertEqual(ReviewService(self.root).detail(first['id'])['status'], 'deleted')
        with self.assertRaises(ReviewError) as conflict:
            self.service.decide(first['id'], 'pass', detail['fingerprint'], 'delete-request-1')
        self.assertEqual(conflict.exception.code, 'idempotency_conflict')

    def test_stale_dependencies_and_source_images_are_rejected(self):
        row = self.rows[0]
        detail = self.service.detail(row['id'])
        runtime = self.root / PACKAGE / 'shared/runtime.py'
        runtime.write_bytes(runtime.read_bytes() + b'\n# changed after display\n')
        with self.assertRaises(ReviewError) as caught:
            self.service.decide(row['id'], 'delete', detail['fingerprint'], 'stale-request-1')
        self.assertEqual(caught.exception.code, 'stale_fingerprint')
        source_hash = detail['images']['source'].split('sha256=')[1]
        original = self.root / row['original_image']
        original.write_bytes(original.read_bytes() + b'changed')
        with self.assertRaises(ReviewError) as caught:
            self.service.image(row['id'], 'source', source_hash)
        self.assertEqual(caught.exception.code, 'candidate_changed')

    def test_all_seven_families_promote_and_catalog_is_full_build_equivalent(self):
        before = catalog.read(self.root / 'provenance/approvals.json')['approvals']
        seen = set()
        for row in self.rows:
            family = row['renderer_family']
            if family in seen:
                continue
            seen.add(family)
            detail = self.service.detail(row['id'])
            result = self.service.decide(row['id'], 'pass', detail['fingerprint'], 'family-pass-' + family)
            self.assertEqual(result['status'], 'passed')
            qid = result['formal_id']
            formal = next(r for r in catalog.rows(self.root / row['subject'] / 'dataset.jsonl') if r['id'] == qid)
            self.assertEqual(formal['source_key'], row['source_key'])
            if family == 'solid':
                self.assertNotIn('runtime_dependencies', formal)
                self.assertNotIn('renderer_family', formal)
            else:
                self.assertTrue(formal['runtime_dependencies'])
            self.assertNotIn('review_candidates', (self.root / row['subject'] / formal['script']).read_text())
            scene = catalog.read(self.root / row['subject'] / formal['scene'])
            self.assertEqual(scene['id'], qid)
            self.assertEqual(catalog.catalog(self.root), catalog.rows(self.root / 'question_bank.jsonl'))
        self.assertEqual(len(seen), 7)
        approvals = catalog.read(self.root / 'provenance/approvals.json')['approvals']
        for key, entry in before.items():
            self.assertEqual(approvals[key], entry)
        self.assertEqual(len(catalog.catalog(self.root)), self.original_count + 7)

    def test_solid_uses_canonical_renderer_transactionally(self):
        row = next(row for row in self.rows if row['renderer_family'] == 'solid')
        renderer = self.root / 'SolidGeometry/dataset_generator/common_renderer.py'
        before = renderer.read_bytes()
        approvals = catalog.read(self.root / 'provenance/approvals.json')['approvals']
        detail = self.service.detail(row['id'])
        renderer.write_bytes(before + b'\n')
        try:
            with self.assertRaises(ReviewError) as caught:
                self.service.decide(row['id'], 'pass', detail['fingerprint'], 'native-solid-stale')
            self.assertEqual(caught.exception.code, 'stale_fingerprint')
        finally:
            renderer.write_bytes(before)
        result = self.service.decide(row['id'], 'pass', detail['fingerprint'], 'native-solid-pass')
        formal = next(record for record in catalog.rows(self.root / 'SolidGeometry/dataset.jsonl')
                      if record['id'] == result['formal_id'])
        self.assertNotIn('runtime_dependencies', formal)
        self.assertNotIn('renderer_family', formal)
        self.assertFalse((self.root / 'SolidGeometry/dataset_generator/mathverse_renderers').exists())
        self.assertEqual(renderer.read_bytes(), before)
        after = catalog.read(self.root / 'provenance/approvals.json')['approvals']
        self.assertTrue(all(after[qid] == approval for qid, approval in approvals.items()))
        self.assertEqual(catalog.catalog(self.root), catalog.rows(self.root / 'question_bank.jsonl'))

    def test_existing_formal_damage_cannot_be_laundered_by_pass(self):
        row = self.rows[0]
        detail = self.service.detail(row['id'])
        formal = self.root / 'Analytics/image/Ana01.png'
        formal.write_bytes(formal.read_bytes() + b'changed')
        dataset_before = (self.root / row['subject'] / 'dataset.jsonl').read_bytes()
        approvals_before = (self.root / 'provenance/approvals.json').read_bytes()
        with self.assertRaisesRegex(ValueError, 'approved content changed'):
            self.service.decide(row['id'], 'pass', detail['fingerprint'], 'damaged-request-1')
        self.assertEqual(dataset_before, (self.root / row['subject'] / 'dataset.jsonl').read_bytes())
        self.assertEqual(approvals_before, (self.root / 'provenance/approvals.json').read_bytes())
        self.assertTrue((self.root / PACKAGE / 'items' / row['id']).exists())
        self.assertFalse((self.root / row['subject'] / 'image/Plane72.png').exists())

    def test_external_edit_during_render_is_preserved(self):
        row = self.rows[0]
        detail = self.service.detail(row['id'])
        index = self.root / PACKAGE / 'index.jsonl'
        changed = index.read_bytes() + b'\n'
        def edit(*args):
            index.write_bytes(changed)
        with patch.object(self.service, '_verify_redraw', side_effect=edit):
            with self.assertRaises(RecoveryRequired):
                self.service.decide(row['id'], 'pass', detail['fingerprint'], 'external-edit-1')
        self.assertEqual(index.read_bytes(), changed)
        self.assertEqual(len(catalog.catalog(self.root)), self.original_count)

    def test_failure_after_candidate_move_rolls_back_everything(self):
        row = self.rows[0]
        initial_index = (self.root / PACKAGE / 'index.jsonl').read_bytes()
        initial_catalog = (self.root / 'question_bank.jsonl').read_bytes()
        initial_approvals = (self.root / 'provenance/approvals.json').read_bytes()
        def fail(label):
            if label == 'after_move':
                raise RuntimeError('injected failure')
        self.service.fault = fail
        detail = self.service.detail(row['id'])
        with self.assertRaisesRegex(RuntimeError, 'injected'):
            self.service.decide(row['id'], 'pass', detail['fingerprint'], 'failure-request-1')
        self.assertEqual(initial_index, (self.root / PACKAGE / 'index.jsonl').read_bytes())
        self.assertEqual(initial_catalog, (self.root / 'question_bank.jsonl').read_bytes())
        self.assertEqual(initial_approvals, (self.root / 'provenance/approvals.json').read_bytes())
        self.assertTrue((self.root / PACKAGE / 'items' / row['id']).exists())
        self.assertFalse((self.root / PACKAGE / 'review_state.json').exists())

    def test_two_processes_assign_unique_formal_ids(self):
        context = multiprocessing.get_context('spawn')
        queue, start = context.Queue(), context.Event()
        candidates = [r for r in self.rows if r['renderer_family'] == 'plane'][:2]
        workers = [context.Process(target=mutation_worker, args=(str(self.root), row['id'], 'pass', 'concurrent-' + row['id'], queue, start)) for row in candidates]
        try:
            for worker in workers:
                worker.start()
            start.set()
            results = [queue.get(timeout=90) for _ in workers]
            self.assertTrue(all(result[0] == 'ok' for result in results), results)
            self.assertEqual({result[1]['formal_id'] for result in results}, {'Plane72', 'Plane73'})
            for worker in workers:
                worker.join(10)
                self.assertEqual(worker.exitcode, 0)
            self.assertEqual(catalog.catalog(self.root), catalog.rows(self.root / 'question_bank.jsonl'))
        finally:
            for worker in workers:
                if worker.is_alive():
                    worker.terminate()
                worker.join(10)
            queue.close()

    def test_restart_recovers_hard_exit_before_commit_and_keeps_commit(self):
        context = multiprocessing.get_context('spawn')
        row = self.rows[0]
        for label in ('after_write:provenance/approvals.json', 'after_move', 'after_commit'):
            with self.subTest(label=label):
                worker = context.Process(target=mutation_worker, args=(str(self.root), row['id'], 'pass', 'crash-request-' + str(len(label)), None, None, label))
                worker.start()
                worker.join(90)
                if worker.is_alive():
                    worker.terminate()
                    worker.join(5)
                    self.fail('Crash test worker timed out')
                self.assertEqual(worker.exitcode, 83)
                restarted = ReviewService(self.root)
                if label == 'after_commit':
                    self.assertEqual(restarted.detail(row['id'])['status'], 'passed')
                    self.assertEqual(len(catalog.catalog(self.root)), self.original_count + 1)
                else:
                    self.assertEqual(restarted.detail(row['id'])['status'], 'pending')
                    self.assertEqual(len(catalog.catalog(self.root)), self.original_count)

    def test_http_security_and_path_containment(self):
        server = ReviewHTTPServer(('127.0.0.1', 0), self.service)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        host, port = server.server_address
        def request(method, path, body=None, headers=None):
            connection = http.client.HTTPConnection(host, port, timeout=10)
            connection.request(method, path, body=body, headers=headers or {})
            response = connection.getresponse()
            data = response.read()
            status = response.status
            connection.close()
            return status, data
        try:
            self.assertEqual(request('GET', '/api/candidates')[0], 200)
            self.assertEqual(request('GET', '/../../.env')[0], 404)
            self.assertEqual(request('GET', '/%2e%2e/.env')[0], 404)
            self.assertEqual(request('GET', '/api/candidates', headers={'Host': 'attacker.example'})[0], 403)
            body = json.dumps({'fingerprint': '0' * 64, 'request_id': 'security-request'})
            base = {'Content-Type': 'application/json', 'X-Review-Workbench': '1'}
            for headers in ({'Content-Type': 'application/json'}, {**base, 'Origin': 'https://attacker.example'}, {**base, 'Sec-Fetch-Site': 'cross-site'}):
                self.assertEqual(request('POST', '/api/candidates/MV0001/delete', body, headers)[0], 403)
            self.assertEqual(self.service.list_candidates()['summary']['pending'], len(self.rows))
        finally:
            server.shutdown()
            server.server_close()
            thread.join(5)


if __name__ == '__main__':
    unittest.main()
