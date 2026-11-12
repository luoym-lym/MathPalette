"""Interactive action regressions using real renderers and isolated test output.

Run once per branch, e.g. python -X utf8 -B dataset_tools/test_workbench_actions.py PlaneGeometry.
No user review API or paid model calls are made.
"""
from __future__ import annotations

import copy
import json
from http.server import ThreadingHTTPServer
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.request import ProxyHandler, Request, build_opener

PROJECT = Path(__file__).resolve().parents[1]
BRANCH = sys.argv.pop(1)
if BRANCH not in ('Analytics', 'PlaneGeometry', 'SolidGeometry'):
    raise ValueError('A formal branch name is required')
sys.path.insert(0, str(PROJECT / BRANCH / 'workbench'))
sys.path.insert(0, str(PROJECT))
import review_store
from workbench_io import WorkbenchError, atomic_json, canonical_hash, file_hash, load_config, read_json

TEST_NOTE = 'TEMPORARY SOFTWARE TEST FIXTURE; NOT USER APPROVAL'


class ActionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        cls.adapter = review_store.RendererAdapter(cls.config)
        # Real input validation and manifests; only two real scenes need rendering
        # to exercise navigation, review, deletion and collection transactions.
        cls.adapter.records = dict(list(cls.adapter.records.items())[:2])

    def setUp(self):
        runtime = PROJECT / '.runtime' / 'workbench_action_tests'
        runtime.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix=BRANCH + '-', dir=runtime)
        self.root = Path(self.temporary.name).resolve()
        config = {**self.config, 'runtime_dir': str(self.root / 'runtime'),
                  'dataset_root': str(self.root / BRANCH),
                  'output_dir': str(self.root / BRANCH / 'special_variant')}
        with patch.object(review_store, 'RendererAdapter', return_value=self.adapter):
            self.bench = review_store.Workbench(config)
        self.qid = self.bench.context()['question_id']
        context = self.bench.context()
        points = context.get('snap_points', [])
        self.plugin = {'plugin_schema_version': '1.0.0', 'question_id': self.qid,
                       'category': 'C', 'operation': 'C_manual', 'description': TEST_NOTE,
                       'intent': TEST_NOTE, 'params': {'actions': [
                           {'type': 'add_point', 'id': 'test_point',
                            'xy': points[0]['xy'] if points else [0, 0]}]}}

    def tearDown(self):
        self.bench.close()
        self.temporary.cleanup()

    def submit(self, color='#DC2626'):
        plugin = copy.deepcopy(self.plugin)
        plugin['params']['actions'][0]['color'] = color
        token = self.bench.context_token()
        preview = self.bench.drawing_preview(plugin, token)
        return self.bench.drawing_submit(plugin, token, None,
            preview['pixel_sha256'], preview['parameter_key'])['candidate']

    def review(self, candidate, decision='pass'):
        return self.bench.review(self.qid, candidate['candidate_id'], decision,
            self.bench.context_token(), candidate['pixel_sha256'], candidate['parameter_key'], TEST_NOTE)

    def delete(self, recipe):
        return self.bench.delete_accepted(self.qid, recipe['candidate_id'], recipe['slot_id'],
            self.bench.context_token(), recipe['pixel_sha256'], recipe['parameter_key'])

    def test_preview_submit_and_review_do_not_scan_or_render_again(self):
        with patch.object(self.adapter, 'assert_baseline', side_effect=AssertionError('full scan')):
            with patch.object(self.bench.renderer, 'render', wraps=self.bench.renderer.render) as render:
                candidate = self.submit()
                self.assertEqual(render.call_count, 1)
                self.review(candidate)
                self.assertEqual(render.call_count, 1)
        self.assertEqual(len(self.bench.snapshot()['accepted']), 1)
        recipe = self.bench.snapshot()['accepted'][0]
        self.assertEqual(file_hash(self.bench._accepted_path(recipe['image_path'])), candidate['png_sha256'])
        self.assertTrue(self.review(candidate)['idempotent'])

    def test_no_pass_needs_neither_baseline_scan_nor_png(self):
        candidate = self.submit()
        self.bench._package_file(candidate, 'image.png').unlink()
        with patch.object(self.bench, '_assert_current_inputs', side_effect=AssertionError('input scan')):
            self.review(candidate, 'reject')
        self.assertIsNone(self.bench.snapshot()['candidate'])
        self.assertEqual(self.bench.snapshot()['accepted'], [])
        self.assertEqual(self.bench.context()['last_review']['note'], TEST_NOTE)

    def test_corrupt_pass_fails_before_transaction_and_can_be_rejected(self):
        candidate = self.submit()
        self.bench._package_file(candidate, 'image.png').write_bytes(b'corrupt test PNG')
        with self.assertRaises(WorkbenchError):
            self.review(candidate)
        self.assertFalse((self.bench.state_dir / 'pending_transaction.json').exists())
        self.review(candidate, 'reject')

    def test_delete_only_copies_affected_slots_and_recovers(self):
        for color in ('#DC2626', '#2563EB', '#16A34A'):
            self.review(self.submit(color))
        before = copy.deepcopy(self.bench.snapshot()['accepted'])
        first_image = self.bench._accepted_path(before[0]['image_path'])
        first_mtime = first_image.stat().st_mtime_ns
        with patch.object(self.bench, '_assert_current_inputs', side_effect=AssertionError('input scan')):
            with patch.object(self.bench, '_apply_transaction', side_effect=OSError('test interruption')):
                with self.assertRaises(OSError):
                    self.delete(before[1])
            transaction = read_json(self.bench.state_dir / 'pending_transaction.json')
            self.assertEqual(len(transaction['affected_recipes']), 2)
            self.bench._recover()
        after = self.bench.snapshot()['accepted']
        self.assertEqual([r['slot_id'] for r in after], ['C01', 'C02'])
        self.assertEqual(after[1]['candidate_id'], before[2]['candidate_id'])
        self.assertEqual(after[1]['pixel_sha256'], before[2]['pixel_sha256'])
        self.assertEqual(file_hash(self.bench._accepted_path(after[1]['image_path'])), before[2]['png_sha256'])
        self.assertEqual(first_image.stat().st_mtime_ns, first_mtime)
        self.assertFalse(self.bench._accepted_path(before[2]['image_path']).exists())
        for recipe in reversed(after):
            self.delete(recipe)
        self.assertEqual(self.bench.snapshot()['accepted'], [])

    def test_current_input_check_reads_no_other_question_artifacts(self):
        paths = []
        def record(path):
            paths.append(Path(path))
            return file_hash(path)
        with patch.object(review_store, 'file_hash', side_effect=record):
            self.bench._assert_current_inputs(self.qid)
        other = next(q for q in self.adapter.records if q != self.qid)
        self.assertNotIn(self.adapter.original_paths[other], paths)
        self.assertIn(self.adapter.original_paths[self.qid], paths)
        with patch.object(review_store, 'file_hash', return_value='changed'):
            with self.assertRaises(WorkbenchError) as error:
                self.bench._assert_current_inputs(self.qid)
        self.assertEqual(error.exception.code, 'baseline_changed')

    def test_http_review_returns_updated_state_in_one_response(self):
        from server import make_handler
        candidate = self.submit()
        class LocalQuickTests:
            def snapshot(self, state):
                return {'test_fixture': True, 'candidate_id': (state.get('candidate') or {}).get('candidate_id')}
        server = ThreadingHTTPServer(('127.0.0.1', 0), make_handler(self.bench, LocalQuickTests()))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            body = {'question_id': self.qid, 'candidate_id': candidate['candidate_id'],
                    'decision': 'reject', 'context_token': self.bench.context_token(),
                    'pixel_sha256': candidate['pixel_sha256'], 'parameter_key': candidate['parameter_key'],
                    'note': TEST_NOTE}
            request = Request(f'http://127.0.0.1:{server.server_port}/api/review',
                              data=json.dumps(body).encode(), headers={'Content-Type': 'application/json',
                              'X-Review-Token': self.bench.review_token})
            with build_opener(ProxyHandler({})).open(request, timeout=10) as response:
                result = json.load(response)
            self.assertEqual(result['candidate']['status'], 'rejected')
            self.assertIsNone(result['state']['candidate'])
            self.assertIsNone(result['state']['quick_test']['candidate_id'])
        finally:
            server.shutdown()
            server.server_close()
            thread.join(5)

    def test_same_protocol_restart_keeps_pending_candidate_and_metadata_cache(self):
        candidate = self.submit()
        old = copy.deepcopy(self.adapter.manifest)
        old['fingerprint'] = canonical_hash({'files': old['files'], 'environment': old['environment']})
        progress = copy.deepcopy(self.bench.progress)
        progress['signature']['baseline_fingerprint'] = old['fingerprint']
        published = progress['candidates'][candidate['candidate_id']]
        published['baseline_fingerprint'] = old['fingerprint']
        atomic_json(self.bench._package_file(published, 'manifest.json'), published)
        atomic_json(self.bench.state_dir / 'baseline_manifest.json', old)
        atomic_json(self.bench.state_dir / 'progress.json', progress)
        cache = read_json(self.bench.state_dir / 'scene_metadata.json')
        cache['signature'] = copy.deepcopy(progress['signature'])
        atomic_json(self.bench.state_dir / 'scene_metadata.json', cache)
        config = self.bench.config
        self.bench.close()
        with patch.object(review_store, 'RendererAdapter', return_value=self.adapter):
            with patch.object(self.adapter, 'inspect_question', side_effect=AssertionError('unnecessary redraw')):
                self.bench = review_store.Workbench(config)
        self.assertEqual(self.bench.snapshot()['candidate']['candidate_id'], candidate['candidate_id'])
        self.assertEqual(read_json(self.bench.state_dir / 'scene_metadata.json')['signature'], self.bench.signature)


if __name__ == '__main__':
    unittest.main()
