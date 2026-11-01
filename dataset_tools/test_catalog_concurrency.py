"""Verify simultaneous workbench catalog updates using disposable test records."""
from __future__ import annotations

import json
import multiprocessing
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

import catalog


def concurrent_writer(directory, identity, ready, start, results):
    root = Path(directory)

    def read_test_records(_root):
        marker = root / 'reader_active'
        # The catalog must be read inside the cross-process write lock.
        with marker.open('x'):
            pass
        try:
            time.sleep(0.08)
            return [{'test_fixture': True, 'writer': identity}]
        finally:
            marker.unlink()

    catalog.catalog = read_test_records
    ready.put(identity)
    if not start.wait(15):
        results.put(('error', identity, 'start timeout'))
        return
    try:
        catalog.build(root)
        results.put(('ok', identity))
    except Exception as error:
        results.put(('error', identity, str(error)))


def incremental_writer(directory, branch, qid, start, results):
    if not start.wait(15):
        results.put(('error', qid, 'start timeout'))
        return
    try:
        catalog.update_special_plugins(Path(directory), branch, qid)
        results.put(('ok', qid))
    except Exception as error:
        results.put(('error', qid, str(error)))


class CatalogConcurrencyTests(unittest.TestCase):
    def setUp(self):
        runtime = Path(__file__).resolve().parents[1] / '.runtime'
        runtime.mkdir(exist_ok=True)
        self.sandbox = tempfile.TemporaryDirectory(prefix='catalog_test_', dir=runtime)
        self.root = Path(self.sandbox.name)

    def tearDown(self):
        self.sandbox.cleanup()

    def test_four_processes_serialize_read_and_atomic_replace(self):
        context = multiprocessing.get_context('spawn')
        ready, results, start = context.Queue(), context.Queue(), context.Event()
        workers = [context.Process(target=concurrent_writer,
                   args=(str(self.root), identity, ready, start, results)) for identity in range(4)]
        try:
            for worker in workers:
                worker.start()
            self.assertEqual({ready.get(timeout=15) for _ in workers}, set(range(4)))
            start.set()
            outcomes = [results.get(timeout=15) for _ in workers]
            self.assertEqual(sorted(outcomes), [('ok', identity) for identity in range(4)])
            for worker in workers:
                worker.join(15)
                self.assertEqual(worker.exitcode, 0)
            row = json.loads((self.root / 'question_bank.jsonl').read_text(encoding='utf-8'))
            self.assertTrue(row['test_fixture'])
            self.assertIn(row['writer'], range(4))
            self.assertFalse(list(self.root.glob('*.tmp')))
        finally:
            start.set()
            for worker in workers:
                if worker.is_alive():
                    worker.terminate()
                if worker.pid is not None:
                    worker.join(5)
            ready.close()
            results.close()

    def test_failed_replace_preserves_previous_catalog_and_releases_lock(self):
        target = self.root / 'question_bank.jsonl'
        before = '{"test_fixture": true, "generation": 1}\n'
        target.write_text(before, encoding='utf-8', newline='\n')
        with patch.object(catalog, 'catalog', return_value=[{'test_fixture': True, 'generation': 2}]):
            with patch.object(catalog.os, 'replace', side_effect=OSError('test replacement failure')):
                with self.assertRaisesRegex(OSError, 'test replacement failure'):
                    catalog.build(self.root)
            self.assertEqual(target.read_text(encoding='utf-8'), before)
            self.assertFalse(list(self.root.glob('*.tmp')))
            catalog.build(self.root)
        self.assertEqual(json.loads(target.read_text(encoding='utf-8'))['generation'], 2)

    def test_incremental_updates_preserve_other_workbenches_and_original_fields(self):
        pairs = [('Analytics', 'Ana01'), ('PlaneGeometry', 'Plane01'),
                 ('PlaneGeometry', 'Plane02'), ('SolidGeometry', 'Solid01')]
        records = [{'branch': branch, 'id': qid, 'question': 'TEMPORARY SOFTWARE TEST FIXTURE',
                    'answer': 123, 'base_plugins': [], 'special_plugins': []} for branch, qid in pairs]
        target = self.root / 'question_bank.jsonl'
        target.write_text(''.join(json.dumps(r) + '\n' for r in records), encoding='utf-8')
        for branch, qid in pairs:
            directory = self.root / branch / 'special_variant' / qid
            directory.mkdir(parents=True)
            recipe = {'question_id': qid, 'status': 'passed',
                      'plugin_path': f'special_variant/{qid}/plugins/C01.json'}
            (directory / 'recipes.json').write_text(json.dumps([recipe]), encoding='utf-8')
        context = multiprocessing.get_context('spawn')
        results, start = context.Queue(), context.Event()
        workers = [context.Process(target=incremental_writer,
                   args=(str(self.root), branch, qid, start, results)) for branch, qid in pairs]
        try:
            for worker in workers:
                worker.start()
            start.set()
            self.assertEqual(sorted(results.get(timeout=15) for _ in workers),
                             sorted(('ok', qid) for _, qid in pairs))
            for worker in workers:
                worker.join(15)
                self.assertEqual(worker.exitcode, 0)
            actual = catalog.rows(target)
            for before, after in zip(records, actual):
                self.assertEqual(after, {**before, 'special_plugins': [
                    f"{before['branch']}/special_variant/{before['id']}/plugins/C01.json"]})
            # Deleting the last variant updates just that row, without original
            # approval scans or even reading another question's missing images.
            (self.root / 'PlaneGeometry/special_variant/Plane01/recipes.json').write_text('[]', encoding='utf-8')
            with patch.object(catalog, 'catalog', side_effect=AssertionError('full audit')):
                catalog.update_special_plugins(self.root, 'PlaneGeometry', 'Plane01')
            after_delete = catalog.rows(target)
            self.assertEqual(after_delete[1]['special_plugins'], [])
            self.assertEqual([after_delete[i] for i in (0, 2, 3)], [actual[i] for i in (0, 2, 3)])
        finally:
            start.set()
            for worker in workers:
                if worker.is_alive():
                    worker.terminate()
                if worker.pid is not None:
                    worker.join(5)
            results.close()


if __name__ == '__main__':
    unittest.main()
