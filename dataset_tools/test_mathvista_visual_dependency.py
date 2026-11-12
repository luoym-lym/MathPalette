"""Check the explicitly approved MathVista visual-only revisions.

Run: python -X utf8 -B dataset_tools/test_mathvista_visual_dependency.py
The semantic audit is documented per item in the revision manifest. These tests
protect that audit's exact inputs; they are not an automated proof of semantics.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dataset_tools import catalog
from dataset_tools.visual_revision_integrity import (
    assert_same_renderer, baseline_bytes, baseline_source, historical_bytes,
)

MANIFEST = ROOT / 'provenance/mathvista_visual_dependency_20261108.json'


class MathVistaVisualDependencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = catalog.read(MANIFEST)
        cls.migration = catalog.read(ROOT / 'provenance/drawing_protocol_integration_20261112.json')
        cls.source_notes = catalog.read(ROOT / 'provenance/source_notes.json')
        cls.revisions = {item['id']: item for item in cls.manifest['revisions']}
        cls.rows = {row['id']: row for row in catalog.rows(ROOT / 'Analytics/dataset.jsonl')}

    def test_exact_admitted_batch_and_review_status(self):
        admission = catalog.read(ROOT / 'provenance/analytics_renumber_and_mathvista61_20261108.json')
        expected = {row['id'] for row in admission['admitted_mathvista_questions']}
        self.assertEqual(set(self.revisions), expected)
        self.assertEqual(expected, {f'Ana{i}' for i in range(71, 132)})
        self.assertEqual(len(self.manifest['revisions']), 61)
        self.assertEqual(self.manifest['status'], 'user_approved')

    def test_questions_answers_and_script_metadata(self):
        for qid, revision in self.revisions.items():
            with self.subTest(qid=qid):
                row = self.rows[qid]
                catalog.validate_formal_row(ROOT, 'Analytics', row)
                expected = revision['after']
                actual = {key: row[key] for key in ('question', 'answer', 'answer_type', 'choices') if key in row}
                self.assertEqual(actual, expected)
                script = ROOT / 'Analytics' / row['script']
                spec = importlib.util.spec_from_file_location(f'visual_revision_{qid}', script)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                instance = getattr(module, qid)()
                for key, value in expected.items():
                    self.assertEqual(getattr(instance, key), value)
                self.assertEqual(instance.query, row['question'])
                self.assertEqual(hasattr(instance, 'choices'), row['answer_type'] == 'choice')
                baseline = baseline_source(ROOT, self.manifest['base_commit'],
                                           f'Analytics/{row["script"]}')
                proof = self.migration['questions'][qid]
                previous = historical_bytes(ROOT, 'Analytics/' + row['script'], proof['previous_files'][row['script']]).decode('utf-8')
                assert_same_renderer(baseline, previous, qid)
                self.assertEqual(catalog.file_hash(script), proof['new_script_sha256'])

    def test_renderer_comparison_ignores_only_literal_review_metadata(self):
        before = "class Q:\n def __init__(self):\n  self.question = 'before'\n  self.query = self.question\n  self.answer = 1\n  self.scale = 2\n def draw(self):\n  return self.scale\n"
        after = before.replace("'before'", "'after'").replace('self.answer = 1', 'self.answer = 3')
        assert_same_renderer(before, after, 'fixture')
        for changed in (after.replace('self.scale = 2', 'self.scale = 5'),
                        after.replace('return self.scale', 'return -self.scale'),
                        after.replace("'after'", 'change_renderer()')):
            with self.subTest(source=changed), self.assertRaisesRegex(ValueError, 'rendering code changed'):
                assert_same_renderer(before, changed, 'fixture')

    def test_baseline_unavailable_or_unpinned_fails_closed(self):
        for commit, relative in [('master', 'missing.py'),
                                 (self.manifest['base_commit'], '../missing.py')]:
            with self.subTest(commit=commit, relative=relative), self.assertRaises(ValueError):
                baseline_source(ROOT, commit, relative)
        with self.assertRaisesRegex(RuntimeError, 'fetch that commit'):
            baseline_source(ROOT, self.manifest['base_commit'], 'missing-renderer-fixture.py')

    def test_visual_evidence_and_alternative_graph_for_every_item(self):
        for qid, revision in self.revisions.items():
            with self.subTest(qid=qid):
                self.assertTrue(revision['image_inspected'])
                for field in ('removed_shortcut', 'visual_evidence', 'solution'):
                    self.assertTrue(revision[field].strip())
                alternative = revision['counterfactual']
                self.assertTrue(alternative['description'].strip())
                self.assertNotEqual(alternative['answer'], revision['after']['answer'])
                if revision['after']['answer_type'] == 'choice':
                    self.assertIn(alternative['answer'], revision['after']['choices'])
                audit = revision['independent_audit']
                self.assertTrue(audit['inspected_image'])
                self.assertFalse(audit['text_only_unique'])
                self.assertTrue(audit['agrees'])
                self.assertFalse(audit['issue'])
                self.assertEqual(str(audit['image_answer']), str(revision['after']['answer']))
                self.assertTrue(audit['counterfactual_valid'])
                self.assertFalse(audit['global_extrapolation_required'])
                self.assertEqual(audit['question_sha256'], hashlib.sha256(
                    revision['after']['question'].encode()).hexdigest())
                self.assertEqual(audit['image_sha256'],
                                 catalog.file_hash(ROOT / audit['inspected_image']))

    def test_frozen_assets_unchanged_and_png_protocol(self):
        from PIL import Image
        for relative, fingerprint in self.manifest['frozen_runtime_files'].items():
            self.assertEqual(hashlib.sha256(historical_bytes(ROOT, relative, fingerprint)).hexdigest(), fingerprint)
        for qid, revision in self.revisions.items():
            with self.subTest(qid=qid):
                for relative, fingerprint in revision['preserved_files'].items():
                    self.assertEqual(hashlib.sha256(historical_bytes(ROOT, relative, fingerprint)).hexdigest(), fingerprint)
                for relative, change in revision.get('revised_files', {}).items():
                    self.assertEqual(catalog.file_hash(ROOT / relative), change['current_sha256'])
                    self.assertEqual(hashlib.sha256(baseline_bytes(
                        ROOT, self.manifest['base_commit'], relative)).hexdigest(), change['previous_sha256'])
                with Image.open(ROOT / 'Analytics' / self.rows[qid]['image']) as image:
                    self.assertEqual(image.size, (768, 768))
                    self.assertIn(image.mode, ('RGB', 'RGBA'))
                    self.assertEqual(image.convert('RGBA').getchannel('A').getextrema(), (255, 255))

    def test_ana121_visual_revision_removes_only_formula_labels(self):
        changed = {qid for qid, r in self.revisions.items() if r.get('render_change_expected')}
        self.assertEqual(changed, {'Ana121'})
        relative = 'Analytics/dataset_generator/scenes/Ana121.json'
        before = json.loads(baseline_source(ROOT, self.manifest['base_commit'], relative))
        after = catalog.read(ROOT / relative)
        self.assertEqual(len(before['labels']), 3)
        self.assertEqual(after['labels'], [])
        before['labels'] = []
        self.assertEqual(before, after)  # Every frozen curve sample and axis is unchanged.
        self.assertEqual(set(self.revisions['Ana121']['revised_files']), {
            relative, 'Analytics/image/Ana121.png'})

    def test_formal_index_and_explicit_reapproval_are_synchronized(self):
        bank = {row['id']: row for row in catalog.rows(ROOT / 'question_bank.jsonl')}
        approvals = catalog.read(ROOT / 'provenance/approvals.json')['approvals']
        source_notes = catalog.read(ROOT / 'provenance/source_notes.json')
        for branch in catalog.BRANCHES:
            for row in catalog.rows(ROOT / branch / 'dataset.jsonl'):
                with self.subTest(qid=row['id']):
                    expected = {'branch': branch, **row}
                    for key in catalog.PATH_FIELDS:
                        if expected.get(key):
                            expected[key] = f'{branch}/' + expected[key]
                    actual = {key: value for key, value in bank[row['id']].items()
                              if key not in ('base_plugins', 'special_plugins')}
                    self.assertEqual(actual, expected)
                    current = catalog.digest(catalog.content(ROOT, branch, row, source_notes=source_notes))
                    if row['id'] in self.revisions:
                        revision = self.revisions[row['id']]
                        proof = self.migration['questions'][row['id']]
                        self.assertEqual(proof['previous_content_sha256'], revision['proposed_content_sha256'])
                        retained = {k:v for k,v in approvals[row['id']].items() if k not in ('content_sha256','metadata_migrations')}
                        expected_approval = {k:v for k,v in revision['current_approval'].items() if k != 'content_sha256'}
                        self.assertEqual(retained, expected_approval)
                        self.assertEqual(current, approvals[row['id']]['content_sha256'])
                        self.assertEqual(approvals[row['id']]['instruction'], self.manifest['approval_instruction'])
                        prior = (revision.get('approval_history') or [revision['previous_approval']])[-1]
                        self.assertEqual(approvals[row['id']]['previous_content_sha256'], prior['content_sha256'])
                    else:
                        self.assertEqual(current, approvals[row['id']]['content_sha256'])
        self.assertEqual(len(bank), 1516)
        self.assertEqual(catalog.catalog(ROOT), catalog.rows(ROOT / 'question_bank.jsonl'))


if __name__ == '__main__':
    unittest.main()
