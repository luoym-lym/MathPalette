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


if __name__ == '__main__':
    unittest.main()
