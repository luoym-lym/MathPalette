"""Combined MathVerse/MathVision review; all decisions run in disposable copies."""
from __future__ import annotations
import hashlib
import http.client
import json
import os
from pathlib import Path
import shutil
import tempfile
import threading
import unittest
from unittest.mock import patch

from dataset_tools import catalog
from review_workbench.service import MultiSourceReviewService, ReviewService, ReviewError
from review_workbench.server import ReviewHTTPServer
from review_workbench.tests.test_review_workbench import copy_fixture, IGNORE

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = Path('review_candidates/mathvision')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mathvision_fixture(root):
    """Select distinct source categories and both formal target protocols."""
    package = root / PACKAGE
    package.mkdir(parents=True)
    for file in (ROOT / PACKAGE).iterdir():
        if file.is_file() and file.name != 'review_state.json':
            shutil.copy2(file, package / file.name)
    shutil.copytree(ROOT / PACKAGE / 'shared', package / 'shared', ignore=IGNORE)
    rows, selected, seen = catalog.rows(ROOT / PACKAGE / 'index.jsonl'), [], set()
    for row in rows:
        key = (row['source_category'], row['subject'])
        if key not in seen:
            seen.add(key)
            selected.append(row)
            shutil.copytree(ROOT / PACKAGE / 'items' / row['id'], package / 'items' / row['id'], ignore=IGNORE)
    (package / 'index.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in selected), encoding='utf-8')
    return selected


class MultiSourceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='mathpalette_MATHVISION_TEST_ONLY_')
        self.root = Path(self.temporary.name) / 'project'
        self.mathverse = copy_fixture(self.root)
        self.mathvision = mathvision_fixture(self.root)
        (self.root / 'TEST_FIXTURE_ONLY.txt').write_text('Synthetic isolated QA. Not user approvals. Never copy these decisions into real data.')
        self.service = MultiSourceReviewService(self.root)

    def tearDown(self):
        self.temporary.cleanup()

    def protected(self):
        paths = [self.root / 'provenance/approvals.json', self.root / 'provenance/source_notes.json', self.root / 'question_bank.jsonl']
        paths += [self.root / b / 'dataset.jsonl' for b in catalog.BRANCHES]
        return {str(path): digest(path) for path in paths}

    def test_combined_queue_reads_and_images_do_not_approve(self):
        before = self.protected()
        result = self.service.list_candidates()
        self.assertEqual(result['summary']['pending'], len(self.mathverse) + len(self.mathvision))
        self.assertEqual(result['datasets']['MathVision']['pending'], len(self.mathvision))
        for row in (self.mathverse[0], *self.mathvision):
            with patch.object(self.service.services[row['source_dataset']], '_verify_redraw', side_effect=AssertionError('GET rendered')):
                detail = self.service.detail(row['id'])
            self.assertEqual(detail['status'], 'pending')
            self.assertEqual(detail['source_dataset'], row['source_dataset'])
            for kind in ('source', 'redraw'):
                sha = detail['images'][kind].rsplit('=', 1)[1]
                data, suffix = self.service.image(row['id'], kind, sha)
                self.assertEqual(hashlib.sha256(data).hexdigest(), sha)
                self.assertIn(suffix, ('.png', '.jpg', '.jpeg'))
        self.assertEqual(before, self.protected())
        self.assertFalse((self.root / PACKAGE / 'review_state.json').exists())

    def test_source_dispatch_does_not_accept_other_prefix(self):
        with self.assertRaises(ReviewError):
            self.service.services['MathVerse'].detail(self.mathvision[0]['id'])
        for value in ('../MVI0011', 'MVI11', 'unknown', None):
            with self.assertRaises(ReviewError):
                self.service.detail(value)

    def test_delete_is_scoped_and_replayed_after_restart(self):
        row = self.mathvision[0]
        before = self.protected()
        old_index = digest(self.root / 'review_candidates/mathverse/index.jsonl')
        detail = self.service.detail(row['id'])
        result = self.service.decide(row['id'], 'delete', detail['fingerprint'], 'mathvision-delete-test-1')
        self.assertEqual(result['status'], 'deleted')
        restarted = MultiSourceReviewService(self.root)
        replay = restarted.decide(row['id'], 'delete', detail['fingerprint'], 'mathvision-delete-test-1')
        self.assertTrue(replay['replayed'])
        self.assertEqual(replay['summary']['pending'], len(self.mathverse) + len(self.mathvision) - 1)
        self.assertFalse((self.root / PACKAGE / 'items' / row['id']).exists())
        self.assertEqual(old_index, digest(self.root / 'review_candidates/mathverse/index.jsonl'))
        self.assertEqual(before, self.protected())

    def test_stale_mathvision_content_and_bad_image_hash_are_rejected(self):
        row = self.mathvision[0]
        detail = self.service.detail(row['id'])
        scene = self.root / row['scene']
        scene.write_bytes(scene.read_bytes() + b'\n')
        with self.assertRaisesRegex(ReviewError, 'changed since'):
            self.service.decide(row['id'], 'delete', detail['fingerprint'], 'mathvision-stale-test-1')
        with self.assertRaisesRegex(ReviewError, 'Image changed'):
            self.service.image(row['id'], 'redraw', '0' * 64)
        self.assertEqual(self.service.detail(row['id'])['status'], 'pending')

    def test_mathvision_pass_preserves_native_pixels_and_formal_contract(self):
        old_index = digest(self.root / 'review_candidates/mathverse/index.jsonl')
        original_count = len(catalog.rows(self.root / 'question_bank.jsonl'))
        for row in self.mathvision:
            with self.subTest(candidate=row['id']):
                detail = self.service.detail(row['id'])
                image = (self.root / row['image']).read_bytes()
                original = (self.root / row['original_image']).read_bytes()
                result = self.service.decide(row['id'], 'pass', detail['fingerprint'], 'mathvision-pass-' + row['id'])
                formal = next(r for r in catalog.rows(self.root / row['subject'] / 'dataset.jsonl') if r['id'] == result['formal_id'])
                self.assertEqual(formal['source_dataset'], 'MathVision')
                self.assertEqual(formal['source_key'], row['source_key'])
                self.assertEqual((self.root / row['subject'] / formal['image']).read_bytes(), image)
                self.assertEqual((self.root / row['subject'] / formal['original_image']).read_bytes(), original)
                catalog.validate_formal_row(self.root, row['subject'], formal)
                self.assertTrue(formal.get('runtime_dependencies'))
                self.assertTrue(all('review_candidates' not in dependency for dependency in formal['runtime_dependencies']))
                replay = self.service.decide(row['id'], 'pass', detail['fingerprint'], 'mathvision-pass-' + row['id'])
                self.assertTrue(replay['replayed'])
                self.assertEqual(replay['formal_id'], result['formal_id'])
        self.assertEqual(len(catalog.catalog(self.root)), original_count + len(self.mathvision))
        self.assertEqual(old_index, digest(self.root / 'review_candidates/mathverse/index.jsonl'))

    def test_bad_source_renderer_fails_without_saving_decision(self):
        row = self.mathvision[0]
        detail = self.service.detail(row['id'])
        before = self.protected()
        with patch.dict(os.environ, {'MATHPALETTE_MATHVISION_PYTHON': str(self.root / 'absent-python')}):
            with self.assertRaisesRegex(ReviewError, 'MATHPALETTE_MATHVISION_PYTHON'):
                self.service.decide(row['id'], 'pass', detail['fingerprint'], 'mathvision-bad-env-test')
        self.assertEqual(before, self.protected())
        self.assertEqual(self.service.detail(row['id'])['status'], 'pending')
        self.assertFalse((self.root / PACKAGE / 'review_state.json').exists())

    def test_http_mathvision_routes_and_combined_list(self):
        try:
            server = ReviewHTTPServer(('127.0.0.1', 0), self.service)
        except PermissionError as error:
            self.skipTest('Loopback socket blocked by this executor: ' + str(error))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            connection = http.client.HTTPConnection('127.0.0.1', server.server_port, timeout=10)
            connection.request('GET', '/api/candidates')
            response = connection.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(json.loads(response.read())['datasets']['MathVision']['pending'], len(self.mathvision))
            connection.request('GET', '/api/candidates/' + self.mathvision[0]['id'])
            response = connection.getresponse()
            self.assertEqual(response.status, 200)
            detail = json.loads(response.read())
            connection.request('GET', detail['images']['source'])
            response = connection.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), (self.root / self.mathvision[0]['original_image']).read_bytes())
            connection.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == '__main__':
    unittest.main()
