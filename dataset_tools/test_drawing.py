"""Unified drawing protocol regression tests; never writes formal data."""
from pathlib import Path
import ast
import hashlib
import io
import json
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
import matplotlib
import numpy as np
from PIL import Image
from dataset_tools.drawing import Canvas,ANALYTICS,PLANE,SOLID
from dataset_tools.draw_question import load_question
from dataset_tools.unified_workbench import pixel_hash


class DrawingTests(unittest.TestCase):
    def setUp(self):
        runtime=ROOT/'.runtime/drawing_tests';runtime.mkdir(parents=True,exist_ok=True)
        self.temporary=tempfile.TemporaryDirectory(dir=runtime)
        self.addCleanup(self.temporary.cleanup)
        self.output=Path(self.temporary.name)

    def test_primitives_fixed_canvas_and_repeatability(self):
        for protocol in (ANALYTICS,PLANE,SOLID):
            outputs=[]
            for i in range(2):
                with Canvas(protocol,xlim=(-4,4),ylim=(-4,4)) as c:
                    c.fill([[-2,-2],[2,-2],[0,2]],id='region')
                    c.line([[-2,-2],[2,-2],[0,2],[-2,-2]],id='outline')
                    c.point([[0,0]],filled=False,id='point')
                    c.circle([0,0],1,id='circle')
                    c.arc([0,0],2,0,90,id='arc')
                    c.path([[-3,0],[-2,3],[2,3],[3,0]],[1,4,4,4],id='bezier')
                    c.text('A',[0,2],offset_pt=(0,12),vertex=True)
                    p=Path(c.save(self.output/f'{protocol.name}_{i}.png'))
                with Image.open(p) as im:
                    self.assertEqual(im.size,(768,768))
                    self.assertEqual(im.convert('RGBA').getextrema()[3],(255,255))
                outputs.append(p.read_bytes())
            self.assertEqual(*outputs)

    def test_projection_and_invalid_geometry(self):
        matrix=np.array([[1,.4,0],[0,.3,1]])
        with Canvas(SOLID,projection=matrix,origin=[1,2,3],offset=[4,5]) as c:
            p=np.array([[1,2,3],[4,6,9]])
            np.testing.assert_array_equal(c.project(p),(matrix@(p-[1,2,3]).T).T+[4,5])
            with self.assertRaises(ValueError):c.project([[1,float('inf'),3]])
        for kwargs in ({'xlim':(0,2),'ylim':(0,3)}, {'projection':[[1,0,0],[2,0,0]]},
                       {'projection':[[1,2],[3,4]]}, {'origin':[0,0]}):
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):Canvas(SOLID,**kwargs)

    def test_ambient_style_isolation_and_formal_output_protection(self):
        original=matplotlib.rcParams.copy()
        with matplotlib.rc_context({'font.size':42,'path.simplify':False,'lines.scale_dashes':True}):
            outside=matplotlib.rcParams.copy()
            with Canvas(PLANE) as c:
                self.assertEqual(matplotlib.rcParams['font.size'],16)
                with Canvas(ANALYTICS):self.assertEqual(matplotlib.rcParams['font.size'],12)
                self.assertEqual(matplotlib.rcParams['font.size'],16)
                with self.assertRaises(ValueError):c.save(ROOT/'PlaneGeometry/image/DO_NOT_WRITE.png')
            self.assertEqual(matplotlib.rcParams,outside)
        self.assertEqual(matplotlib.rcParams,original)

    def test_representative_classes_use_the_verified_protocol(self):
        proof=json.loads((ROOT/'provenance/drawing_protocol_integration_20261112.json').read_text())
        for branch,qids in {'Analytics':['Ana01','Ana31','Ana132','Ana560'],
                            'PlaneGeometry':['Plane01','Plane94','Plane225','Plane491','Plane595'],
                            'SolidGeometry':['Solid01','Solid158','Solid249','Solid289']}.items():
            for qid in qids:
                with self.subTest(qid=qid):
                    question=load_question(branch,qid)
                    path=question.draw(self.output/(qid+'.png'))
                    self.assertEqual(pixel_hash(path),proof['questions'][qid]['render_pixel_sha256'])

    def test_every_formal_class_has_one_construction_and_matching_metadata(self):
        count=0
        for branch in ('Analytics','PlaneGeometry','SolidGeometry'):
            for row in map(json.loads,(ROOT/branch/'dataset.jsonl').read_text().splitlines()):
                count+=1
                with self.subTest(qid=row['id']):
                    tree=ast.parse((ROOT/branch/row['script']).read_text())
                    classes=[n for n in tree.body if isinstance(n,ast.ClassDef)]
                    self.assertEqual([n.name for n in classes],[row['id']])
                    cls=classes[0];draw=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='draw')
                    self.assertTrue(any(isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='Canvas' for n in ast.walk(draw)))
                    self.assertFalse(any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr in ('get_scene','read_text','read_bytes','imshow') for n in ast.walk(draw)))
                    init=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='__init__')
                    values={n.targets[0].attr:ast.literal_eval(n.value) for n in init.body
                            if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Attribute)
                            and n.targets[0].attr in ('id','question','answer','source_dataset','answer_type','choices')}
                    for key in ('id','question','answer','source_dataset','answer_type','choices'):
                        self.assertEqual(values.get(key),row.get(key))
                    self.assertEqual(row['drawing_protocol_version'],'2.0.0')
                    self.assertTrue(all('/contexts/' in p for p in row['runtime_dependencies']))
        self.assertEqual(count,1516)


if __name__=='__main__':unittest.main()
