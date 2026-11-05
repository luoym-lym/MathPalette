"""Native workbench regression on approved originals; no review actions or API calls.

Run each branch in a separate process because workbench modules use local imports:
python -X utf8 -B dataset_tools/test_extensions95_workbench.py PlaneGeometry
python -X utf8 -B dataset_tools/test_extensions95_workbench.py SolidGeometry
"""
from __future__ import annotations

import copy
import json
import math
import re
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
BRANCH = sys.argv.pop(1)
if BRANCH not in ('PlaneGeometry', 'SolidGeometry'):
    raise ValueError('Choose a geometry branch')
sys.path.insert(0, str(PROJECT / BRANCH / 'workbench'))
sys.path.insert(0, str(PROJECT))

from extensions95_adapter import RendererAdapter
from extensions95_plugins import PluginRenderer
from partial_style import object_paths
from workbench_io import (GENERATOR_VERSION, SCHEMA_VERSION, WorkbenchError, canonical_hash,
                          environment_versions, file_hash, load_config, pixel_hash, renderer_fingerprint)


def plugin(qid, actions):
    return {'plugin_schema_version': '1.0.0', 'question_id': qid, 'category': 'C',
            'operation': 'C_manual', 'description': 'Software regression only; no approval',
            'intent': '', 'params': {'actions': actions}}


class NativeWorkbenchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        cls.adapter = RendererAdapter(cls.config)
        cls.ids = [qid for qid in cls.adapter.records if cls.adapter.is_extensions95(qid)]
        cls.metadata = {}
        for qid in cls.ids:
            cls.metadata[qid] = cls.adapter.inspect_question(qid)
        cls.renderer = PluginRenderer(cls.config, cls.adapter, cls.metadata)

    def test_every_new_original_uses_native_pixels_and_contours(self):
        self.assertEqual(len(self.ids), 70 if BRANCH == 'PlaneGeometry' else 25)
        for qid, meta in self.metadata.items():
            with self.subTest(qid=qid):
                self.assertEqual(meta['original_pixel_sha256'], pixel_hash(self.adapter.original_paths[qid]))
                self.assertTrue(meta['objects'])
                self.assertTrue(all(re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]{0,63}', o['id'])
                                    for o in meta['objects']))
                self.assertEqual(len(meta['objects']), len(meta['canvas']['targets']))
                self.assertEqual((meta['canvas']['width'], meta['canvas']['height']), (768, 768))
                for snap in meta['snap_points']:
                    self.assertTrue(all(math.isfinite(v) for v in snap['xy']))
                if qid == 'Plane595':
                    snap = next(s for s in meta['snap_points'] if s['id'] == 'I_point_4')
                    self.assertEqual(snap['xy'], [0.5, 0.5])

    def test_style_fill_protection_and_deterministic_partial_edit_each_family(self):
        for qid in self.ids[::5]:
            with self.subTest(qid=qid):
                meta = self.metadata[qid]
                oid = meta['objects'][0]['id']
                scene = self.adapter.scene(qid)
                try:
                    scene.fig.canvas.draw()
                    path = object_paths(scene, oid)[0]
                    before_fills = [(p, copy.deepcopy(p.get_facecolor())) for p in scene.ax.patches
                                    if p.get_facecolor()[3] > 0]
                    action = {'type': 'set_object_style', 'target': oid,
                              'color': '#2563EB', 'linewidth_pt': 2.0, 'linestyle': 'dashed',
                              'interval': {'path_id': path['id'], 'path_sha256': path['sha256'],
                                           'start': 0.15, 'end': 0.7, 'wrap': False}}
                    with patch.object(self.adapter, 'scene', return_value=scene):
                        normalized, data, digest = self.renderer.render(plugin(qid, [action]))
                    # Partial strokes may insert transparent patches between
                    # original artists. Compare the actual semantic fills by
                    # identity, rather than assuming the patch order is fixed.
                    for original, fill in before_fills:
                        self.assertIn(original, scene.ax.patches)
                        self.assertEqual(fill, original.get_facecolor())
                finally:
                    scene.close()
                self.assertNotEqual(digest, meta['original_pixel_sha256'])
                self.assertEqual(self.renderer.render(normalized, frozen=True)[1:], (data, digest))
                # Frozen path hashes must fail closed if parameters were altered.
                bad = copy.deepcopy(normalized)
                bad['params']['actions'][0]['interval']['path_sha256'] = '0' * 64
                with self.assertRaises(WorkbenchError):
                    self.renderer.render(bad, frozen=True)
                with self.assertRaises(WorkbenchError):
                    self.renderer.normalize(plugin(qid, [{'type': 'set_object_style',
                        'target': 'not_an_editable_contour', 'color': '#DC2626'}]))

    def test_added_points_and_lines_each_family(self):
        for qid in self.ids[::5]:
            with self.subTest(qid=qid):
                points = self.metadata[qid]['snap_points']
                p = points[0]['xy']
                q = next(item['xy'] for item in points if item['xy'] != p)
                actions = [{'type': 'set_object_style', 'target': self.metadata[qid]['objects'][0]['id'],
                            'color': '#DC2626', 'linewidth_pt': 1.5},
                           {'type': 'add_point', 'id': 'regression_point', 'xy': p},
                           {'type': 'add_line', 'id': 'regression_line', 'endpoints': [p, q],
                            'linestyle': 'solid'}]
                normalized, data, digest = self.renderer.render(plugin(qid, actions))
                self.assertNotEqual(digest, self.metadata[qid]['original_pixel_sha256'])
                self.assertEqual(self.renderer.render(normalized, frozen=True)[1:], (data, digest))

    def test_representative_archived_recipes_still_replay(self):
        from replay_archived import render_special_recipe
        seen = set()
        for qid, record in self.adapter.records.items():
            kind = ('expand24' if self.adapter.is_expand24(qid) else
                    'author' if self.adapter.is_author(qid) else
                    'mathvision' if record['source_dataset'] == 'MathVision' else 'legacy')
            recipes_path = Path(self.config['output_dir']) / qid / 'recipes.json'
            if kind in seen or not recipes_path.is_file():
                continue
            recipes = json.loads(recipes_path.read_text(encoding='utf-8'))
            if not recipes:
                continue
            seen.add(kind)
            recipe = recipes[0]
            result = render_special_recipe(recipe)
            self.assertTrue(result['matches_accepted'])
            self.assertEqual(result['pixel_sha256'], recipe['pixel_sha256'])
        self.assertEqual(seen, {'legacy', 'mathvision', 'author', 'expand24'})

    def test_native_offline_recipe_in_isolated_fixture(self):
        import extensions95_replay
        qid = self.ids[0]
        actions = [{'type': 'set_object_style', 'target': self.metadata[qid]['objects'][0]['id'],
                    'color': '#16A34A'}]
        normalized, data, digest = self.renderer.render(plugin(qid, actions))
        # A clearly labelled software fixture lives only in .runtime. This does
        # not call Pass/Collect or write a recipe to the formal Special folder.
        fixture_root = PROJECT / '.runtime/extensions95_workbench_fix'
        fixture_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='recipe_fixture_', dir=fixture_root) as temp:
            directory = Path(temp)
            config = {**self.config, 'dataset_root': str(directory / 'dataset'),
                      'output_dir': str(directory / 'dataset/special_variant'),
                      'runtime_dir': str(directory / 'runtime')}
            image = Path(config['output_dir']) / qid / 'images/C01.png'
            image.parent.mkdir(parents=True)
            image.write_bytes(data)
            recipe = {**normalized, 'status': 'passed', 'slot_id': 'C01',
                      'fixture_note': 'AUTOMATED SOFTWARE TEST ONLY; NO USER APPROVAL',
                      'generator_version': GENERATOR_VERSION, 'plugin_schema_version': SCHEMA_VERSION,
                      'environment': environment_versions(), 'renderer_sha256': renderer_fingerprint(),
                      'schema_sha256': file_hash(PROJECT / BRANCH / 'workbench/plugin.schema.json'),
                      'question_record_sha256': canonical_hash(self.adapter.records[qid]),
                      'baseline_fingerprint': self.adapter.manifest['fingerprint'],
                      'parameter_key': canonical_hash(normalized), 'pixel_sha256': digest,
                      'image_path': image.relative_to(directory / 'dataset').as_posix(),
                      'png_sha256': file_hash(image)}
            with patch.object(extensions95_replay, 'load_config', return_value=config):
                result = extensions95_replay.render_special_recipe(recipe)
                self.assertTrue(result['matches_accepted'])
                self.assertEqual(pixel_hash(result['image_path']), digest)
                # A corrupted PNG must be refused even if render parameters match.
                image.write_bytes(b'corrupted fixture image')
                with self.assertRaises(WorkbenchError):
                    extensions95_replay.render_special_recipe(recipe)


if __name__ == '__main__':
    unittest.main(verbosity=2)
