"""Opt-in, complete staged-batch import and Special renderer compatibility.

Run with MATHPALETTE_FULL_DELIVERY_QA=1. All packaging and test-only approval
records exist only in a disposable complete repository copy. This test NEVER
passes a candidate or changes any approval in the delivery checkout.
"""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import time
import unittest

from importer import eligibility, fingerprint, package, payload_paths, safe_path
from dataset_tools import catalog, question_review
from test_support import PROJECT, TEST_NOTE, read_json, read_rows, write_json, write_rows


@unittest.skipUnless(os.environ.get('MATHPALETTE_FULL_DELIVERY_QA') == '1',
                     'Full staged-batch compatibility is opt-in; set MATHPALETTE_FULL_DELIVERY_QA=1.')
class CompleteDeliveryCompatibility(unittest.TestCase):
    def test_every_staged_candidate_and_all_eligible_imports_match_special_renderer(self):
        started = time.monotonic()
        source_rows = read_rows(PROJECT / 'staging/solidgeo/candidates.jsonl')
        expected_total = int(os.environ.get('MATHPALETTE_EXPECTED_CANDIDATES', '168'))
        expected_eligible = int(os.environ.get('MATHPALETTE_EXPECTED_ELIGIBLE', '135'))
        self.assertEqual(len(source_rows), expected_total)
        watched = {PROJECT / 'staging/solidgeo/candidates.jsonl', PROJECT / 'question_bank.jsonl',
                   PROJECT / 'SolidGeometry/dataset.jsonl', PROJECT / 'provenance/approvals.json',
                   PROJECT / 'provenance/source_notes.json'}
        for row in source_rows:
            watched.update(payload_paths(PROJECT, row).values())
        before = {p.relative_to(PROJECT).as_posix(): catalog.file_hash(p) for p in watched}
        report = {'test_fixture_only': True, 'delivery_candidates': len(source_rows),
                  'source_manifest_sha256': before['staging/solidgeo/candidates.jsonl'],
                  'eligible_imports': [], 'blocked': [], 'source_changed': []}
        try:
            with tempfile.TemporaryDirectory(prefix='mathpalette-complete-delivery-QA-') as directory:
                root = Path(directory) / 'repository'
                shutil.copytree(PROJECT, root, ignore=shutil.ignore_patterns(
                    '.git', '.env', '.runtime', '__pycache__', '*.pyc', '*.lock'))
                self.assertNotEqual(root.resolve(), PROJECT.resolve())
                records = read_rows(root / 'staging/solidgeo/candidates.jsonl')
                existing = catalog.catalog(root)
                formal = read_rows(root / 'SolidGeometry/dataset.jsonl')
                notes = read_json(root / 'provenance/source_notes.json')
                next_number = max(int(row['id'][5:]) for row in formal) + 1
                imported = []
                for index, candidate in enumerate(records):
                    checked = eligibility(root, candidate, render=True)
                    declared = candidate.get('pass_eligible') is True and not candidate.get('pass_blockers')
                    self.assertEqual(checked['eligible'], declared,
                                     f"{candidate['id']}: declared/live eligibility mismatch: {checked['reasons']}")
                    if not checked['eligible']:
                        report['blocked'].append({'candidate_id': candidate['id'], 'reasons': checked['reasons']})
                        continue
                    qid = f'Solid{next_number + len(imported):02d}'
                    row, source_notes, artifacts = package(root, candidate, qid, checked, fingerprint(root, candidate))
                    for relative, data in artifacts.items():
                        target = safe_path(root, relative)
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.write_bytes(data)
                    formal.append(row)
                    notes[qid] = source_notes
                    imported.append((candidate, row))
                    if len(imported) % 15 == 0:
                        print(f'Validated and packaged {len(imported)} eligible candidates ({index + 1}/{len(records)} scanned).', flush=True)
                self.assertEqual(len(imported), expected_eligible)
                self.assertEqual(len(report['blocked']), expected_total - expected_eligible)
                write_rows(root / 'SolidGeometry/dataset.jsonl', formal)
                write_json(root / 'provenance/source_notes.json', notes)
                # These approvals mark isolated software fixtures only. They are
                # never copied back or delivered as user approval records.
                question_review.approve('SolidGeometry', [row['id'] for _, row in imported], TEST_NOTE, root)
                complete = catalog.catalog(root)
                self.assertEqual(len(complete), len(existing) + expected_eligible)
                self.assertEqual(complete, read_rows(root / 'question_bank.jsonl'))
                self.assertEqual(complete[:len(existing)], existing)
                sys.path.insert(0, str(root / 'SolidGeometry/workbench'))
                from workbench_io import load_config
                from renderer_adapter import RendererAdapter
                from drawing_board import describe_scene
                adapter = RendererAdapter(load_config(root / 'SolidGeometry/workbench/config.json'))
                for index, (candidate, row) in enumerate(imported):
                    qid = row['id']
                    # The production Special adapter itself verifies no-op pixel
                    # equality with the formal PNG for every imported scene.
                    metadata = adapter.inspect_question(qid)
                    board = describe_scene(adapter, qid)
                    self.assertEqual((board['width'], board['height']), (768, 768))
                    self.assertTrue(board['targets'], qid)
                    self.assertEqual(adapter.records[qid]['question'], candidate['question'])
                    self.assertEqual(adapter.records[qid]['answer'], candidate['answer'])
                    scene = read_json(root / 'SolidGeometry' / row['scene'])
                    self.assertEqual(set(scene), catalog.FORMAL_SCENE_FIELDS['SolidGeometry'])
                    spec = importlib.util.spec_from_file_location('delivery_fixture_' + qid,
                                                                 root / 'SolidGeometry' / row['script'])
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    question = getattr(module, qid)()
                    self.assertEqual(question.query, row['question'])
                    self.assertEqual(question.answer, row['answer'])
                    self.assertEqual(question.answer_type, row['answer_type'])
                    self.assertEqual(question.get_scene(), scene)
                    report['eligible_imports'].append({'candidate_id': candidate['id'], 'fixture_formal_id': qid,
                        'canonical_answer_type': row['answer_type'], 'no_op_pixels_match': True,
                        'pixel_sha256': metadata['original_pixel_sha256'], 'special_targets': len(board['targets']),
                        'source_image_sha256': catalog.file_hash(root / 'SolidGeometry' / row['original_image'])})
                    if (index + 1) % 15 == 0:
                        print(f'Special adapter/no-op pixels verified for {index + 1}/{len(imported)} imports.', flush=True)
                report['isolated_catalog_count'] = len(complete)
                report['all_eligible_imports_match'] = True
        finally:
            report['elapsed_seconds'] = round(time.monotonic() - started, 3)
            report['source_changed'] = [relative for relative, digest in before.items()
                                        if catalog.file_hash(PROJECT / relative) != digest]
            destination = os.environ.get('MATHPALETTE_DELIVERY_QA_REPORT')
            if destination:
                write_json(destination, report)
        self.assertEqual(report['source_changed'], [])
        self.assertEqual(len(report['eligible_imports']), expected_eligible)
        print(json.dumps({'candidates_checked': expected_total, 'eligible_imports': expected_eligible,
                          'blocked': len(report['blocked']), 'source_files_unchanged': len(before),
                          'seconds': report['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    unittest.main()
