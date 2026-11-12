"""Data and drawing regressions; output stays in disposable runtime folders."""
from pathlib import Path
import ast
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from MathPalette_Dataset import draw
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID
import matplotlib
import numpy as np


class DatasetTests(unittest.TestCase):
    def setUp(self):
        runtime = ROOT / '.runtime'
        runtime.mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='dataset-tests-', dir=runtime)
        self.addCleanup(self.temporary.cleanup)
        self.output = Path(self.temporary.name)

    def test_release_is_only_normal_collect_and_has_one_class_per_question(self):
        result = draw.check()
        self.assertEqual((result['questions'], result['specials'], result['samples']), (323, 1140, 1463))
        for row in draw.read_rows(draw.DATASET / 'dataset.jsonl'):
            with self.subTest(qid=row['id']):
                self.assertEqual(row['script'], 'questions/' + row['id'] + '.py')
                self.assertTrue(row['approval']['instruction'])
                self.assertEqual(row['approval']['reviewer'], 'user')
                self.assertTrue(row['collection']['collected_at'])
                tree = ast.parse((draw.DATASET / row['script']).read_text(encoding='utf-8'))
                classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
                self.assertEqual([c.name for c in classes], [row['id']])
                methods = {n.name: n for n in classes[0].body if isinstance(n, ast.FunctionDef)}
                for name in ['draw', *['draw_' + s['slot_id'] for s in row['special_variants']]]:
                    method = methods[name]
                    self.assertTrue(any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                                        and n.func.id == 'Canvas' for n in ast.walk(method)))
                    self.assertFalse(any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                                         and n.func.attr in ('read_bytes', 'read_text', 'imshow', 'get_scene')
                                         for n in ast.walk(method)))

    def test_original_and_special_repeat_on_same_instance(self):
        rows = {r['id']: r for r in draw.read_rows(draw.DATASET / 'dataset.jsonl')}
        for qid in ('Ana01', 'Plane25', 'Solid67'):
            q = draw.load_question(qid)
            row = rows[qid]
            for _ in range(2):
                for variant, expected in [(None, row), *[(v['slot_id'], v) for v in row['special_variants']]]:
                    path = q.draw(self.output / (qid + '_' + str(variant) + '.png'), variant=variant)
                    self.assertEqual(draw.file_hash(path), expected['image_sha256'])
            with self.assertRaises(ValueError): q.draw(self.output / 'bad.png', variant='C999')
        with self.assertRaises(ValueError): draw.load_question('../Ana01')
        with self.assertRaises(ValueError): draw.load_question('Ana590')

    def test_fixed_canvas_projection_state_and_formal_output_protection(self):
        previous = matplotlib.rcParams.copy()
        with Canvas(SOLID, projection=[[1, .4, 0], [0, .3, 1]], origin=[1, 2, 3], offset=[4, 5]) as c:
            np.testing.assert_array_equal(c.project([1, 2, 3]), [4, 5])
            with self.assertRaises(ValueError): c.project([1, float('inf'), 3])
            with self.assertRaises(ValueError): c.save(draw.DATASET / 'images/DO_NOT_WRITE.png')
            with Canvas(ANALYTICS): self.assertEqual(matplotlib.rcParams['font.size'], 12)
            self.assertEqual(matplotlib.rcParams['font.size'], 16)
        self.assertEqual(matplotlib.rcParams, previous)
        for kwargs in ({'xlim': [0, 1], 'ylim': [0, 2]}, {'projection': [[1, 0, 0], [2, 0, 0]]}):
            with self.assertRaises(ValueError): Canvas(SOLID, **kwargs)

    def test_dataset_can_run_without_other_repository_directories(self):
        portable = self.output / 'portable'
        portable.mkdir()
        shutil.copytree(draw.DATASET, portable / 'MathPalette_Dataset', ignore=shutil.ignore_patterns('__pycache__'))
        script = portable / 'MathPalette_Dataset/draw.py'
        result = subprocess.run([sys.executable, '-B', str(script), 'draw', 'Ana01', '--variant', 'C01',
                                 '--output', str(self.output / 'portable.png')], cwd=self.output,
                                capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        for model in ('infer_deepseek.py', 'infer_qwen38_max_0902.py'):
            preflight = subprocess.run([sys.executable, '-B', str(script.parent / model), '--dry-run'],
                                      cwd=self.output, capture_output=True, text=True, timeout=20)
            self.assertEqual(preflight.returncode, 0, preflight.stderr)
            self.assertEqual(json.loads(preflight.stdout)['model_requests_submitted'], 0)


if __name__ == '__main__': unittest.main()
