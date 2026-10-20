"""Isolated promotion checks using the master formal schema and renderers.

No real approval, formal manifest, source image, recipe, or candidate is changed.
The temporary fixture approvals are explicitly synthetic test-only records.
Run with the dependency versions in review_candidates/mathverse/validation_summary.json.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from dataset_tools import catalog
from review_candidates.mathverse.promotion import prepare


def _json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


class PromotionCompatibility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='mathverse_TEST_FIXTURE_ONLY_')
        cls.root = Path(cls.temp.name)
        (cls.root / 'TEST_FIXTURE_ONLY.txt').write_text(
            'Synthetic isolated QA records. These are not user approvals. Never copy into a dataset.\n')
        cls.real_protected = [ROOT / 'provenance/approvals.json', ROOT / 'provenance/source_notes.json',
                              ROOT / 'question_bank.jsonl', *(ROOT / b / 'dataset.jsonl' for b in catalog.BRANCHES)]
        cls.before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in cls.real_protected}
        shutil.copytree(ROOT / 'dataset_tools', cls.root / 'dataset_tools',
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        candidates = catalog.rows(ROOT / 'review_candidates/mathverse/index.jsonl')
        families = sorted({row['renderer_family'] for row in candidates})
        selected = [next(row for row in candidates if row['renderer_family'] == family) for family in families]
        # Cover native semantic fill and ellipse extensions, beyond easy first-family examples.
        for kind in ('region', 'curved_region', 'ellipse'):
            extra = next((row for row in candidates if row['subject'] == 'PlaneGeometry' and any(
                obj.get('type') == kind for obj in catalog.read(ROOT / row['scene'])['objects'])), None)
            if extra is not None and extra not in selected:
                selected.append(extra)
        cls.cases, branch_rows, notes = [], {b: [] for b in catalog.BRANCHES}, {}
        for branch in catalog.BRANCHES:
            target = cls.root / branch
            helper = target / 'dataset_generator'
            helper.mkdir(parents=True, exist_ok=True)
            for name in ('common_renderer.py', 'protocol.json'):
                shutil.copy2(ROOT / branch / 'dataset_generator' / name, helper / name)
        prefixes = {'Analytics': 'Ana', 'PlaneGeometry': 'Plane', 'SolidGeometry': 'Solid'}
        for row in selected:
            branch = row['subject']
            qid = f'{prefixes[branch]}{len(branch_rows[branch]) + 1:02d}'
            snapshot = json.dumps(row, sort_keys=True)
            formal, writes, source_notes = prepare(ROOT, row, qid)
            assert json.dumps(row, sort_keys=True) == snapshot
            for relative, data in writes.items():
                path = (cls.root / relative).resolve()
                assert path.is_relative_to(cls.root.resolve())
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            branch_rows[branch].append(formal)
            notes[qid] = source_notes
            cls.cases.append((row, branch, formal))
        for branch, rows in branch_rows.items():
            (cls.root / branch / 'dataset.jsonl').write_text(
                ''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')
        _json(cls.root / 'provenance/source_notes.json', notes)
        approvals = {}
        for _, branch, row in cls.cases:
            approvals[row['id']] = {'reviewer': 'user',
                'instruction': 'TEST FIXTURE ONLY. Synthetic approval for loader tests, not a user decision.',
                'approved_at_utc': '2000-01-01T00:00:00Z', 'test_fixture_only': True,
                'content_sha256': catalog.digest(catalog.content(cls.root, branch, row))}
        _json(cls.root / 'provenance/approvals.json', {'approvals': approvals, 'test_fixture_only': True})

    @classmethod
    def tearDownClass(cls):
        try:
            for path, digest in cls.before.items():
                assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, str(path)
        finally:
            cls.temp.cleanup()

    def test_formal_schema_identity_and_source(self):
        self.assertFalse((self.root / 'review_candidates').exists())
        for candidate, branch, row in self.cases:
            with self.subTest(candidate=candidate['id']):
                catalog.validate_formal_row(self.root, branch, row)
                self.assertFalse({'candidate_id', 'legacy_id', 'status', 'user_approved'} & row.keys())
                for field in ('source_dataset', 'source_key', 'question', 'answer', 'answer_type', 'choices'):
                    self.assertEqual(row.get(field), candidate.get(field))
                scene_path = self.root / branch / row['scene']
                scene = catalog.read(scene_path)
                self.assertEqual(scene['id'], row['id'])
                self.assertEqual(scene['status'], 'user_approved')
                self.assertFalse({'question', 'query', 'answer', 'answer_type', 'user_approved', 'level'} & scene.keys())
                self.assertEqual((scene_path.parent / scene['source_image']).resolve(),
                                 (self.root / branch / row['original_image']).resolve())
                for field in ('image', 'original_image'):
                    self.assertEqual((self.root / branch / row[field]).read_bytes(), (ROOT / candidate[field]).read_bytes())
                script = (self.root / branch / row['script']).read_text()
                self.assertNotIn('review_candidates', script)
                if branch == 'SolidGeometry':
                    self.assertNotIn('renderer_family', row)
                    self.assertNotIn('runtime_dependencies', row)
                    self.assertNotIn('mathverse_renderers', script)
                    self.assertFalse((self.root / branch / 'dataset_generator/mathverse_renderers').exists())
                self.assertTrue(any(isinstance(node, ast.ClassDef) and node.name == row['id']
                                    for node in ast.parse(script).body))

    def test_formal_scripts_redraw_without_review_directory(self):
        from PIL import Image
        for candidate, branch, row in self.cases:
            with self.subTest(candidate=candidate['id']):
                path = self.root / branch / row['script']
                spec = importlib.util.spec_from_file_location('_promotion_test_' + row['id'], path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                question = getattr(module, row['id'])()
                self.assertEqual(question.query, row['question'])
                self.assertEqual(question.answer, row['answer'])
                output = self.root / '.redrawn' / (row['id'] + '.png')
                output.parent.mkdir(exist_ok=True)
                question.draw(output_path=output)
                with Image.open(output) as image, Image.open(ROOT / candidate['image']) as expected:
                    self.assertEqual(image.size, (768, 768))
                    self.assertEqual(image.convert('RGBA').getextrema()[3], (255, 255))
                    self.assertEqual(image.convert('RGB').tobytes(), expected.convert('RGB').tobytes())

    def test_rejects_candidate_and_wrong_branch_ids(self):
        for candidate, branch, _ in self.cases:
            wrong = 'Plane72' if branch == 'Analytics' else 'Ana47'
            for identity in (candidate['id'], wrong, '../Plane72', 'Plane0', 'Solid00', 'Ana1'):
                with self.subTest(branch=branch, identity=identity), self.assertRaises(ValueError):
                    prepare(ROOT, candidate, identity)

    def test_solid_rejects_different_canonical_renderer(self):
        candidate = next((row for row, branch, _ in self.cases if branch == 'SolidGeometry'), None)
        if candidate is None:
            self.skipTest('No pending SolidGeometry candidates remain')
        original_read = Path.read_bytes
        for name in ('common_renderer.py', 'protocol.json'):
            target = ROOT / 'SolidGeometry/dataset_generator' / name
            def changed_read(path):
                data = original_read(path)
                return data + b'\n' if path == target else data
            with self.subTest(dependency=name), patch.object(Path, 'read_bytes', changed_read):
                with self.assertRaisesRegex(ValueError, 'differs from the canonical renderer'):
                    prepare(ROOT, candidate, 'Solid50')


if __name__ == '__main__':
    unittest.main()
