"""Reject ambiguous choice conversions and inconsistent formal answer records."""
import unittest
from pathlib import Path
from unittest.mock import patch

import catalog
from answer_schema import extract_choices, option_letter, validate_answer


class AnswerSchemaTests(unittest.TestCase):
    def test_existing_option_formats(self):
        self.assertEqual(extract_choices('Compare. choice: (A) less (B) more'), {'A': 'less', 'B': 'more'})
        self.assertEqual(extract_choices(r'\[Find x.' + '\nChoices:\nA:4\nB:8' + r'\]'), {'A': '4', 'B': '8'})

    def test_option_text_is_not_mistaken_for_a_letter(self):
        choices = {'A': 'd', 'B': 'a', 'C': 'b', 'D': 'c'}
        self.assertEqual(option_letter('d', choices, answer_is_option_text=True), 'A')
        self.assertEqual(option_letter('B', choices, answer_is_option_text=False), 'B')

    def test_ambiguous_or_missing_answer_is_rejected(self):
        for answer, choices in [('2', {'A': '2', 'B': '2'}), ('3', {'A': '1', 'B': '2'})]:
            with self.assertRaises(ValueError):
                option_letter(answer, choices, answer_is_option_text=True)

    def test_malformed_options_are_rejected(self):
        for question in ['Choices: (A) one (A) two', 'Choices:\nA:1\nC:2', 'Choices:\nA:1\nB:']:
            with self.assertRaises(ValueError):
                extract_choices(question)

    def test_choice_record_requires_consistent_letter_and_mapping(self):
        row = {'id': 'Example', 'question': 'Find x.\nChoices:\nA:2\nB:3',
               'answer': 'A', 'answer_type': 'choice', 'choices': {'A': '2', 'B': '3'}}
        validate_answer(row)
        for change in ({'answer': '2'}, {'answer_type': 'number'}, {'choices': {'A': '3', 'B': '2'}}):
            with self.assertRaises(ValueError):
                validate_answer({**row, **change})

    def test_canonical_categories_preserve_exact_values_and_units(self):
        for kind, answer in [('number', 0), ('number', r'\frac{5}{8}'), ('number', '95°'),
                             ('expression', 'y=x+1'), ('expression', '[-2,2]'), ('text', 'southwest')]:
            validate_answer({'id': 'Example', 'question': 'Find the requested result.',
                             'answer': answer, 'answer_type': kind})
        for kind, answer in [('numeric', '1'), ('number', True), ('number', float('nan')), ('text', '')]:
            with self.assertRaises(ValueError):
                validate_answer({'id': 'Example', 'question': 'Find the requested result.',
                                 'answer': answer, 'answer_type': kind})

    def test_scene_cannot_duplicate_or_contradict_the_formal_record(self):
        row = {'id': 'Plane01', 'question': 'Find the length.', 'answer': '2',
               'answer_type': 'number', 'source_dataset': 'MathVista', 'scene': 'scene.json'}
        scene = {key: [] for key in catalog.FORMAL_SCENE_FIELDS['PlaneGeometry']}
        scene.update(id='Plane01', source_dataset='MathVista')
        with patch.object(catalog, 'read', return_value=scene):
            catalog.validate_formal_row(Path.cwd(), 'PlaneGeometry', row)
        for changed in ({**scene, 'query': 'A stale question'}, {**scene, 'source_dataset': 'Unknown'}):
            with patch.object(catalog, 'read', return_value=changed), self.assertRaises(ValueError):
                catalog.validate_formal_row(Path.cwd(), 'PlaneGeometry', row)
        with self.assertRaises(ValueError):
            catalog.validate_formal_row(Path.cwd(), 'Analytics', {**row, 'source_dataset': ''})


if __name__ == '__main__':
    unittest.main()
