"""Check the explicitly approved MathVista visual-only revisions.

Run: python -X utf8 -B dataset_tools/test_mathvista_visual_dependency.py
The semantic audit is documented per item in the revision manifest. These tests
protect that audit's exact inputs; they are not an automated proof of semantics.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dataset_tools import catalog

MANIFEST = ROOT / 'provenance/mathvista_visual_dependency_20261108.json'
METADATA_FIELDS = {'question', 'query', 'answer', 'answer_type', 'choices'}


def renderer_fingerprint(source):
    """Ignore only question/answer metadata, not any executable drawing input."""
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == '__init__':
            node.body = [statement for statement in node.body if not (
                isinstance(statement, ast.Assign)
                and len(statement.targets) == 1
                and isinstance(statement.targets[0], ast.Attribute)
                and isinstance(statement.targets[0].value, ast.Name)
                and statement.targets[0].value.id == 'self'
                and statement.targets[0].attr in METADATA_FIELDS)]
    return hashlib.sha256(ast.dump(tree, include_attributes=False).encode()).hexdigest()


class MathVistaVisualDependencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = catalog.read(MANIFEST)
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
                self.assertEqual(renderer_fingerprint(script.read_text(encoding='utf-8')),
                                 revision['renderer_ast_sha256'])

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
            self.assertEqual(catalog.file_hash(ROOT / relative), fingerprint)
        for qid, revision in self.revisions.items():
            with self.subTest(qid=qid):
                for relative, fingerprint in revision['preserved_files'].items():
                    self.assertEqual(catalog.file_hash(ROOT / relative), fingerprint)
                with Image.open(ROOT / 'Analytics' / self.rows[qid]['image']) as image:
                    self.assertEqual(image.size, (768, 768))
                    self.assertIn(image.mode, ('RGB', 'RGBA'))
                    self.assertEqual(image.convert('RGBA').getchannel('A').getextrema(), (255, 255))

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
                        self.assertEqual(current, revision['proposed_content_sha256'])
                        self.assertEqual(approvals[row['id']], revision['current_approval'])
                        self.assertEqual(current, approvals[row['id']]['content_sha256'])
                        self.assertEqual(approvals[row['id']]['instruction'], self.manifest['approval_instruction'])
                        self.assertEqual(approvals[row['id']]['previous_content_sha256'],
                                         revision['previous_approval']['content_sha256'])
                    else:
                        self.assertEqual(current, approvals[row['id']]['content_sha256'])
        self.assertEqual(len(bank), 1018)
        self.assertEqual(catalog.catalog(ROOT), catalog.rows(ROOT / 'question_bank.jsonl'))


if __name__ == '__main__':
    unittest.main()
