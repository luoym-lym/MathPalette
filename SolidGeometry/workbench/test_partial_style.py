"""Interval geometry, appearance and saved-recipe regression tests (runtime only)."""
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path as FilePath
from types import SimpleNamespace

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Circle

from partial_style import apply_partial_styles, describe_paths, evaluate, object_paths, portion, validate_interval
from workbench_io import (ROOT, WorkbenchError, canonical_hash, environment_versions, file_hash,
                          load_config, read_json, renderer_fingerprint)
from renderer_adapter import RendererAdapter
from render_plugins import PluginRenderer, render_special_recipe
from drawing_board import describe_scene


def action(scene, target, start=.2, end=.8, wrap=False, **style):
    path = object_paths(scene, target)[0]
    return {'type':'set_object_style', 'target':target, **style, 'interval':{
        'path_id':path['id'],'path_sha256':path['sha256'], 'start':start,'end':end,'wrap':wrap}}


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.fig, self.ax = plt.subplots(figsize=(7.68,7.68),dpi=100)
        self.ax.set(xlim=(-1,11),ylim=(-2,5),aspect='equal')
        self.scene = SimpleNamespace(fig=self.fig,ax=self.ax,artists={})

    def tearDown(self):
        plt.close(self.fig)

    def line(self, name, x, y, **kwargs):
        line, = self.ax.plot(x,y,color='black',linewidth=1,**kwargs)
        self.scene.artists[name] = [line]
        self.fig.canvas.draw()
        return line

    def test_exact_cubic_subdivision_and_neighbor_preservation(self):
        control=np.array([[0.,0.],[3.,4.],[5.,-2.],[10.,2.]])
        patch=PathPatch(Path(control,[1,4,4,4]),fill=False,color='black')
        self.ax.add_patch(patch); self.scene.artists['curve']=[patch]
        neighbor=self.line('neighbor',[0,10],[2,0])
        before=neighbor.get_path().vertices.copy()
        self.fig.canvas.draw()
        change=action(self.scene,'curve',color='#DC2626')
        apply_partial_styles(self.scene,[change])
        patches=self.scene.artists['curve']
        self.assertEqual(len(patches),3)
        red=patches[1].get_path().vertices
        np.testing.assert_allclose(red,portion(control,.2,.8),atol=1e-12)
        for t in np.linspace(0,1,20):
            np.testing.assert_allclose(evaluate(red,t),evaluate(control,.2+.6*t),atol=1e-12)
        np.testing.assert_array_equal(neighbor.get_path().vertices,before)

    def test_continuous_visibility_fragments_color_keeps_dashes(self):
        a=self.line('arc',[0,3,5],[0,1,1],linestyle=(0,[4,3]))
        b,=self.ax.plot([5,8,10],[1,1,0],color='black',linewidth=1)
        self.scene.artists['arc'].append(b)
        self.fig.canvas.draw()
        paths=object_paths(self.scene,'arc')
        self.assertEqual(len(paths),1)
        change=action(self.scene,'arc',start=.25,end=.75,color='#DC2626')
        apply_partial_styles(self.scene,[change])
        patches=self.scene.artists['arc']
        self.assertEqual(len(patches),4)
        self.assertIsNotNone(patches[1]._dash_pattern[1])
        self.assertIsNone(patches[2]._dash_pattern[1])
        self.assertGreater(patches[1]._dash_pattern[0],0)

    def test_gaps_closed_complement_and_invalid_range(self):
        self.line('broken',[0,2,np.nan,6,10],[0,1,np.nan,1,0])
        self.assertEqual(len(object_paths(self.scene,'broken')),2)
        invalid=action(self.scene,'broken',color='#DC2626')['interval']
        for overrides in ({'start':.8,'end':.2},{'start':.2,'end':.2},{'wrap':True},{'path_id':'p999'},{'path_sha256':'0'*64}):
            with self.assertRaises(WorkbenchError):
                validate_interval(invalid|overrides,object_paths(self.scene,'broken'))
        circle=Circle((4,1),2,facecolor='#DDDDDD',edgecolor='black')
        self.ax.add_patch(circle); self.scene.artists['circle']=[circle]; self.fig.canvas.draw()
        before=circle.get_facecolor()
        self.assertTrue(object_paths(self.scene,'circle')[0]['closed'])
        apply_partial_styles(self.scene,[action(self.scene,'circle',wrap=True,color='#DC2626')])
        self.assertEqual(circle.get_facecolor(),before)
        patches=self.scene.artists['circle']
        self.assertEqual(len(patches),3)
        self.assertEqual(patches[0].get_edgecolor(),patches[-1].get_edgecolor())
        self.assertNotEqual(patches[0].get_edgecolor(),patches[1].get_edgecolor())

    def test_overlapping_changes_compose_per_property_and_order(self):
        self.line('line',[0,10],[0,0])
        changes=[action(self.scene,'line',.2,.7,color='#DC2626'),
                 action(self.scene,'line',.4,.9,linewidth_pt=3),
                 {'type':'set_object_style','target':'line','linestyle':'dashed'}]
        apply_partial_styles(self.scene,changes)
        patches=self.scene.artists['line']
        self.assertEqual([p.get_linewidth() for p in patches],[1,1,3,3,1])
        self.assertEqual(patches[1].get_edgecolor(),patches[2].get_edgecolor())
        self.assertTrue(all(p._dash_pattern[1] for p in patches))

    def test_noop_retains_original_artist_and_caps(self):
        artist=self.line('line',[0,10],[0,0],solid_capstyle='round',solid_joinstyle='miter')
        before=np.asarray(self.fig.canvas.buffer_rgba()).copy()
        apply_partial_styles(self.scene,[action(self.scene,'line',color='#000000')])
        self.assertIs(self.scene.artists['line'][0],artist)
        self.fig.canvas.draw()
        np.testing.assert_array_equal(np.asarray(self.fig.canvas.buffer_rgba()),before)
        apply_partial_styles(self.scene,[action(self.scene,'line',color='#DC2626')])
        self.assertTrue(all(p.get_capstyle()=='round' and p.get_joinstyle()=='miter' for p in self.scene.artists['line']))


class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config=load_config(); cls.adapter=RendererAdapter(cls.config)
        cls.qid='Plane94' if ROOT.parent.name=='PlaneGeometry' else 'Solid14'
        cls.meta=cls.adapter.inspect_question(cls.qid)
        cls.renderer=PluginRenderer(cls.config,cls.adapter,{cls.qid:cls.meta})

    def test_real_preview_normalize_replay_and_source_unchanged(self):
        board=describe_scene(self.adapter,self.qid)
        target=next(t for t in board['targets'] if t['partial_paths'])
        path=target['partial_paths'][0]
        p={'plugin_schema_version':'1.0.0','question_id':self.qid,'category':'C','operation':'C_manual',
           'description':'TEMPORARY SOFTWARE TEST FIXTURE', 'intent':'test', 'params':{'actions':[
            {'type':'set_object_style','target':target['id'],'color':'#DC2626','interval':{
                'path_id':path['id'],'path_sha256':path['sha256'],'start':.23,'end':.81,'wrap':False}}]}}
        before=copy.deepcopy(self.adapter.make_manifest())
        normalized,data,digest=self.renderer.render(p)
        self.assertEqual(self.renderer.render(normalized,frozen=True)[1],data)
        from workbench_io import GENERATOR_VERSION,SCHEMA_VERSION
        recipe={**normalized,'generator_version':GENERATOR_VERSION,'plugin_schema_version':SCHEMA_VERSION,
                'status':'passed','environment':environment_versions(),'renderer_sha256':renderer_fingerprint(),
                'schema_sha256':file_hash(ROOT/'plugin.schema.json'),'baseline_fingerprint':self.adapter.manifest['fingerprint'],
                'question_record_sha256':canonical_hash(self.adapter.records[self.qid]),
                'parameter_key':canonical_hash(normalized),'pixel_sha256':digest,'slot_id':'TEST_ONLY'}
        runtime=ROOT.parents[1]/'.runtime/partial_style_upgrade'
        runtime.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=runtime) as temp:
            result=render_special_recipe(recipe,FilePath(temp)/'test.png')
            self.assertTrue(result['matches_accepted'])
        self.assertEqual(before,self.adapter.make_manifest())
        self.assertEqual(self.meta['original_pixel_sha256'],self.adapter.inspect_question(self.qid)['original_pixel_sha256'])
        malformed=copy.deepcopy(p); malformed['params']['actions'][0]['interval']['start']=True
        with self.assertRaises(WorkbenchError): self.renderer.normalize(malformed)
        malformed=copy.deepcopy(p); malformed['params']['actions'][0]['interval']['path_sha256']='0'*64
        with self.assertRaises(WorkbenchError): self.renderer.normalize(malformed)

    def test_legacy_pair_is_restricted_and_preserves_pixels(self):
        from workbench_io import GENERATOR_VERSION, SCHEMA_VERSION
        target=next(o['id'] for o in self.meta['objects'] if o['styleable'])
        plugin={'plugin_schema_version':SCHEMA_VERSION,'question_id':self.qid,'category':'C','operation':'C_manual',
                'description':'TEMPORARY SOFTWARE TEST FIXTURE','params':{'actions':[
                    {'type':'set_object_style','target':target,'color':'#DC2626'}]}}
        normalized,_,digest=self.renderer.render(plugin)
        recipe={**normalized,**read_json(ROOT/'style_compatibility.json')['whole_object_v1'],
                'generator_version':GENERATOR_VERSION,'status':'passed','environment':environment_versions(),
                'baseline_fingerprint':self.adapter.manifest['fingerprint'],
                'question_record_sha256':canonical_hash(self.adapter.records[self.qid]),
                'parameter_key':canonical_hash(normalized),'pixel_sha256':digest,'slot_id':'TEST_ONLY'}
        runtime=ROOT.parents[1]/'.runtime/partial_style_upgrade'
        runtime.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=runtime) as temp:
            output=FilePath(temp)/'legacy-test.png'
            self.assertTrue(render_special_recipe(recipe,output)['matches_accepted'])
            with self.assertRaises(WorkbenchError):
                render_special_recipe(recipe|{'renderer_sha256':'0'*64},output)
            with self.assertRaises(WorkbenchError):
                render_special_recipe(recipe|{'pixel_sha256':'0'*64},output)

    def test_isolated_local_review_and_cold_restore(self):
        from review_store import Workbench
        from workbench_io import atomic_json
        runtime=ROOT.parents[1]/'.runtime/partial_style_upgrade'
        runtime.mkdir(parents=True,exist_ok=True)
        formal=ROOT.parent
        originals={str(p):file_hash(p) for folder in ('special_variant','image') for p in (formal/folder).rglob('*') if p.is_file()}
        with tempfile.TemporaryDirectory(dir=runtime) as temp:
            root=FilePath(temp)
            config={**self.config,'runtime_dir':str(root/'state'),'output_dir':str(root/'branch/special_variant'),
                    'dataset_root':str(root/'branch'),'config_path':str(root/'config.json')}
            atomic_json(root/'config.json',config)
            bench=Workbench(config)
            try:
                bench.navigate(self.qid)
                board=describe_scene(bench.adapter,self.qid)
                target=next(t for t in board['targets'] if t['partial_paths'])
                path=target['partial_paths'][0]
                plugin={'plugin_schema_version':'1.0.0','question_id':self.qid,'category':'C','operation':'C_manual',
                        'description':'TEMPORARY SOFTWARE TEST FIXTURE; NOT USER APPROVAL','params':{'actions':[
                    {'type':'set_object_style','target':target['id'],'color':'#DC2626','interval':{
                        'path_id':path['id'],'path_sha256':path['sha256'],'start':.15,'end':.62,'wrap':False}}]}}
                preview=bench.drawing_preview(plugin,bench.context_token())
                candidate=bench.drawing_submit(plugin,bench.context_token(),None,preview['pixel_sha256'],preview['parameter_key'])['candidate']
                bench.review(self.qid,candidate['candidate_id'],'pass',bench.context_token(),
                             candidate['pixel_sha256'],candidate['parameter_key'],'TEMPORARY SOFTWARE TEST FIXTURE; NOT USER APPROVAL')
                recipe=read_json(root/f'branch/special_variant/{self.qid}/recipes.json')[0]
                self.assertEqual(recipe['params']['actions'][0]['interval'],plugin['params']['actions'][0]['interval'])
                self.assertTrue(render_special_recipe(recipe,root/'test.png',root/'config.json')['matches_accepted'])
                bench.close()
                config['runtime_dir']=str(root/'cold-state'); atomic_json(root/'config.json',config)
                bench=Workbench(config); bench.navigate(self.qid)
                self.assertEqual(bench.snapshot()['accepted'][0]['pixel_sha256'],recipe['pixel_sha256'])
            finally:
                bench.close()
        self.assertEqual(originals,{str(p):file_hash(p) for folder in ('special_variant','image') for p in (formal/folder).rglob('*') if p.is_file()})


if __name__=='__main__': unittest.main()
