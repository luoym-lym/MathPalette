"""Adversarial schema/render tests on synthetic isolated SOLIDGEO candidates."""
from __future__ import annotations

import copy
import unittest

from importer import ReviewError, candidate_id, eligibility, fingerprint, parse_json, payload_paths, safe_path
from test_support import IsolatedRepository, read_json, write_json


class CandidateValidationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = IsolatedRepository(2)
        self.root = self.fixture.root
        self.row = self.fixture.candidates[0]

    def tearDown(self):
        self.fixture.close()

    def inspect(self, **changes):
        return eligibility(self.root, {**self.row, **changes}, render=False)

    def test_fixture_uses_canonical_renderer_twice_and_exact_pixels(self):
        result = eligibility(self.root, self.row, render=True)
        self.assertTrue(result['eligible'], result['reasons'])
        self.assertTrue(result['redraw'].startswith(b'\x89PNG'))

    def test_each_required_review_gate_blocks_pass_independently(self):
        changes = [{'pass_eligible': False}, {'pass_blockers': ['requires human resolution']},
                   {'user_approved': True}, {'verification': {'status': 'pending'}},
                   {'verification': {**self.row['verification'], 'agreement': 'disagreement'}},
                   {'verification': {**self.row['verification'], 'agreement': 'unknown'}},
                   {'verification': {**self.row['verification'], 'agreement_evidence': None}},
                   {'verification': {'status': 'verified', 'proof': ''}},
                   {'independently_verified_answer': None}, {'scene_contract': {'valid': False}},
                   {'source_dataset': 'NotSOLIDGEO'}, {'source_key': ''}]
        for key in ('source', 'content', 'answer', 'render'):
            checks = copy.deepcopy(self.row['review_checks'])
            checks[key]['status'] = 'pending'
            changes.append({'review_checks': checks})
        for change in changes:
            with self.subTest(change=change):
                self.assertFalse(self.inspect(**change)['eligible'])

    def test_choice_answer_requires_canonical_letter_and_matching_mapping(self):
        valid = {**copy.deepcopy(self.row), 'question': 'Choose.\nChoices:\nA:1\nB:2', 'answer': 'B',
                 'answer_type': 'choice', 'choices': {'A': '1', 'B': '2'}}
        self.fixture.seal(valid)
        self.assertTrue(eligibility(self.root, valid)['eligible'])
        for changes in ({'answer': '2'}, {'choices': {'A': '2', 'B': '1'}}):
            row = {**self.row, 'question': 'Choose.\nChoices:\nA:1\nB:2', 'answer': 'B',
                   'answer_type': 'choice', 'choices': {'A': '1', 'B': '2'}, **changes}
            self.assertFalse(eligibility(self.root, row)['eligible'])

    def test_scene_identity_must_match_candidate(self):
        scene_path = payload_paths(self.root, self.row)['scene']
        scene = read_json(scene_path)
        scene['id'] = self.fixture.candidates[1]['id']
        write_json(scene_path, scene)
        self.fixture.seal(self.row)
        self.assertFalse(self.inspect()['eligible'])

    def test_projection_changes_invalidate_frozen_visibility(self):
        scene_path = payload_paths(self.root, self.row)['scene']
        scene = read_json(scene_path)
        scene['projection']['matrix'][0][0] += 0.1
        write_json(scene_path, scene)
        self.assertFalse(self.inspect()['eligible'])

    def test_candidate_script_is_never_executed(self):
        path = payload_paths(self.root, self.row)['drawing_script']
        marker = self.root / 'executed-candidate-code'
        path.write_text(f'from pathlib import Path\nPath({str(marker)!r}).write_text("BAD")\nraise RuntimeError("BAD")\n')
        self.fixture.seal(self.row)
        result = eligibility(self.root, self.row, render=True)
        self.assertTrue(result['eligible'], result['reasons'])
        self.assertFalse(marker.exists())

    def test_declared_paths_cannot_disagree_with_compatibility_aliases(self):
        row = copy.deepcopy(self.row)
        row['paths']['scene'] = self.fixture.candidates[1]['paths']['scene']
        self.assertFalse(eligibility(self.root, row)['eligible'])

    def test_paths_only_schema_matches_alias_schema(self):
        row = copy.deepcopy(self.row)
        for key in ('scene', 'image', 'original_image', 'drawing_script', 'provenance'):
            del row[key]
        self.assertEqual(payload_paths(self.root, row), payload_paths(self.root, self.row))

    def test_path_traversal_absolute_windows_and_symlinks_rejected(self):
        for path in ('../secret', '/tmp/secret', 'C:/secret', 'a\\secret', '.', '', 'a/../../secret'):
            with self.subTest(path=path), self.assertRaises(ReviewError):
                safe_path(self.root, path)
        marker = self.root.parent / 'outside.txt'
        marker.write_text('do not touch')
        (self.fixture.staging / 'linked').symlink_to(marker)
        with self.assertRaises(ReviewError):
            safe_path(self.root, 'staging/solidgeo/linked')
        (self.fixture.staging / 'linked-dir').symlink_to(marker.parent, target_is_directory=True)
        with self.assertRaises(ReviewError):
            safe_path(self.root, 'staging/solidgeo/linked-dir/outside.txt')
        self.assertEqual(marker.read_text(), 'do not touch')

    def test_fingerprint_covers_every_reviewed_content_and_dependency(self):
        before = fingerprint(self.root, self.row)
        for key, value in [('question', 'Different question'), ('answer', '999'),
                           ('source_answer', 'different source answer'),
                           ('independently_verified_answer', '999'), ('verification', {'status': 'pending'}),
                           ('source_notes', {'new': 'context'})]:
            with self.subTest(field=key):
                self.assertNotEqual(before, fingerprint(self.root, {**self.row, key: value}))
        paths = list(payload_paths(self.root, self.row).values()) + [self.root / path for path in
            ('SolidGeometry/dataset_generator/common_renderer.py', 'SolidGeometry/dataset_generator/protocol.json',
             'dataset_tools/geometry_dataset.py')]
        for path in paths:
            original = path.read_bytes()
            try:
                path.write_bytes(original + b'\n')
                with self.subTest(path=path.name):
                    self.assertNotEqual(before, fingerprint(self.root, self.row))
            finally:
                path.write_bytes(original)
        self.assertEqual(before, fingerprint(self.root, self.row))

    def test_invalid_missing_or_modified_images_block_pass(self):
        image = payload_paths(self.root, self.row)['image']
        original = image.read_bytes()
        image.write_bytes(b'not a PNG')
        self.assertFalse(self.inspect()['eligible'])
        image.write_bytes(original)
        from PIL import Image
        with Image.open(image) as loaded:
            loaded = loaded.convert('RGBA')
            loaded.putpixel((0, 0), (0, 0, 0, 255))
            loaded.save(image)
        self.assertFalse(eligibility(self.root, self.row, render=True)['eligible'])
        image.unlink()
        self.assertFalse(self.inspect()['eligible'])

    def test_duplicate_json_keys_nonfinite_numbers_and_bad_identity_rejected(self):
        for text in ('{"id":1,"id":2}', '{"number":NaN}', '{"number":Infinity}'):
            with self.subTest(text=text), self.assertRaises((ReviewError, ValueError)):
                parse_json(text)
        for row in ({'id': '../Solid17'}, {'id': 'test', 'candidate_id': 'different'}, {'id': ''},
                    {'id': 123}, {'id': True}, {'id': '123', 'candidate_id': 123}):
            with self.subTest(row=row), self.assertRaises(ReviewError):
                candidate_id(row)


if __name__ == '__main__':
    unittest.main()
