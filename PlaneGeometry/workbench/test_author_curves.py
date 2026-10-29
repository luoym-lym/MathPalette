"""Check formal author curves through the actual Special renderer; no Pass/Collect."""
from collections import Counter
from pathlib import Path
import copy
import unittest
from unittest.mock import patch
import numpy as np
from matplotlib.colors import to_hex
from mathvision_adapter import RendererAdapter
from renderer_adapter import scene_png
from mathvision_plugins import PluginRenderer
from workbench_io import load_config, pixel_hash


class AuthorCurveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config=load_config()
        cls.adapter=RendererAdapter(cls.config)
        cls.ids=[qid for qid,row in cls.adapter.records.items() if row.get('renderer_family')=='author_curves']
        if not cls.ids:
            raise AssertionError('No imported author curve questions')
        cls.metadata={qid:cls.adapter.inspect_question(qid) for qid in cls.ids}
        cls.renderer=PluginRenderer(cls.config,cls.adapter,cls.metadata)

    def test_hidden_junctions_and_complete_selectable_paths(self):
        for qid in self.ids:
            frozen=self.adapter.frozen_scenes[qid]
            meta=self.metadata[qid]
            ids={o['id'] for o in frozen['objects']}
            self.assertEqual(ids,{o['id'] for o in meta['canvas']['targets']})
            self.assertTrue(all(t['paths'] and all(len(p)>1 for p in t['paths']) for t in meta['canvas']['targets']))
            degrees=Counter(p for o in frozen['objects'] for p in o['points'])
            self.assertEqual(set(degrees),set(frozen['points']))
            for name,degree in degrees.items():
                self.assertEqual(degree,4 if name.startswith('J') else 1)
            self.assertEqual({p['id'] for p in meta['snap_points']},set(frozen['points']))
            self.assertFalse(any(label['point'].startswith('J') for label in frozen['labels']))
            scene=self.adapter.scene(qid)
            try:
                self.assertEqual(len(scene.ax.collections),0)  # no hidden junction symbol
                self.assertEqual(len(scene.ax.patches),len(ids))
                self.assertEqual(len(scene.ax.texts),len(frozen['labels']))
                self.assertEqual(scene_png(scene)[1],meta['original_pixel_sha256'])
            finally:scene.close()

    def test_each_segment_changes_independently_and_restores(self):
        for qid in self.ids:
            for target in self.metadata[qid]['canvas']['targets']:
                with self.subTest(qid=qid,target=target['id']):
                    scene=self.adapter.scene(qid)
                    before={key:[a.get_path().vertices.copy() for a in values] for key,values in scene.artists.items()}
                    labels=[(t.get_text(),t.get_position(),t.get_color()) for t in scene.ax.texts]
                    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
                            'description':'TEMPORARY SOFTWARE TEST FIXTURE','params':{'actions':[{
                            'type':'set_object_style','target':target['id'],'color':'#DC2626','linestyle':'dashed'}]}}
                    with patch.object(self.adapter,'scene',return_value=scene):
                        _,data,digest=self.renderer.render(plugin)
                    self.assertNotEqual(digest,self.metadata[qid]['original_pixel_sha256'])
                    for key,artists in scene.artists.items():
                        for index,artist in enumerate(artists):
                            self.assertEqual(to_hex(artist.get_edgecolor()).upper(),'#DC2626' if key==target['id'] else '#000000')
                            np.testing.assert_array_equal(artist.get_path().vertices,before[key][index])
                            if key != target['id']:self.assertEqual(artist.get_linestyle(),'solid')
                    self.assertEqual(labels,[(t.get_text(),t.get_position(),t.get_color()) for t in scene.ax.texts])
            self.assertEqual(self.adapter.inspect_question(qid)['original_pixel_sha256'],self.metadata[qid]['original_pixel_sha256'])

    def test_self_crossing_is_one_point_visited_twice(self):
        candidates=[q for q in self.ids if self.adapter.records[q]['source_key']=='smooth-curve:08']
        self.assertEqual(len(candidates),1)
        scene=self.adapter.frozen_scenes[candidates[0]]
        self.assertTrue(any(any(count==4 for name,count in Counter(
            p for o in scene['objects'] if o['curve_id']==c['curve_id'] for p in o['points']).items() if name.startswith('J'))
            for c in scene['constraints']))

    def test_existing_formal_baselines_remain_identical(self):
        for qid in self.adapter.records:
            if qid not in self.ids:
                with self.subTest(qid=qid):
                    self.adapter.inspect_question(qid)


if __name__=='__main__':unittest.main(verbosity=2)
