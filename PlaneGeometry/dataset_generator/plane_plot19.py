"""Frozen question Plane19; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane19:

    def __init__(self):
        self.id = 'Plane19'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/48'
        self.question = 'Find $m \\angle 3$.\nChoices:\nA: 28\nB: 38\nC: 52\nD: 62'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '28', 'B': '38', 'C': '52', 'D': '62'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane19.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5189953294675353, 8.62531105397429], ylim=[-1.4186130059201867, 7.725693377521639], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 6.250285012053739], [8.0, 6.250285012053739], [8.0, 0.0], [0.0, 0.0], [0.0, 6.250285012053739]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.0], [8.0, 6.250285012053739]], id='o2')
            c.line([[0.0, 6.250285012053739], [3.032312417601329, 2.3691021069497533]], id='o3')
            for object_id, points in [('o4', [[7.83462987587815, 6.250285012053739], [7.83462987587815, 6.084914887931889]]), ('o4', [[7.83462987587815, 6.084914887931889], [8.0, 6.084914887931889]]), ('o5', [[8.0, 0.16537012412185015], [7.83462987587815, 0.16537012412185015]]), ('o5', [[7.83462987587815, 0.16537012412185015], [7.83462987587815, 0.0]]), ('o6', [[0.0, 0.16537012412185015], [0.16537012412185015, 0.16537012412185015]]), ('o6', [[0.16537012412185015, 0.16537012412185015], [0.16537012412185015, 0.0]]), ('o7', [[2.9305004030096837, 2.4994155430830496], [2.8001869668763875, 2.397603528491404]]), ('o7', [[2.8001869668763875, 2.397603528491404], [2.901998981468033, 2.267290092358108]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, vertices, codes in [('o8', [[0.23166833090363784, 0.18099913705181422], [0.2041731526908221, 0.2161913603309652], [0.16901707501156987, 0.244660190705387], [0.12887731725501783, 0.2642376586603968], [0.0887375594984658, 0.28381512661540653], [0.04465957237014384, 0.29399133177217807], [1.800177717159327e-17, 0.29399133177217807]], [1, 4, 4, 4, 4, 4, 4]), ('o9', [[0.29399133177217807, 0.0], [0.29399133177217807, 0.03257134094300673], [0.2885784566147855, 0.06491740741767824], [0.277974265255776, 0.09571421531146967], [0.2673700738967665, 0.12651102320526111], [0.25172125072194435, 0.15533257012933402], [0.23166833090363784, 0.18099913705181422]], [1, 4, 4, 4, 4, 4, 4]), ('o10', [[-5.400533151477981e-17, 5.956293680281561], [0.03257134094300669, 5.956293680281561], [0.06491740741767836, 5.961706555438954], [0.0957142153114698, 5.972310746797963], [0.12651102320526122, 5.982914938156973], [0.15533257012933407, 5.998563761331795], [0.18099913705181428, 6.018616681150101]], [1, 4, 4, 4, 4, 4, 4]), ('o11', [[0.18099913705181428, 6.018616681150101], [0.21619136033096525, 6.0461118593629175], [0.24466019070538697, 6.08126793704217], [0.2642376586603967, 6.121407694798721], [0.2838151266154065, 6.161547452555273], [0.29399133177217807, 6.205625439683596], [0.29399133177217807, 6.250285012053739]], [1, 4, 4, 4, 4, 4, 4]), ('o12', [[7.706008668227822, 6.250285012053739], [7.706008668227822, 6.217713671110732], [7.711421543385215, 6.1853676046360615], [7.722025734744224, 6.15457079674227], [7.732629926103233, 6.123773988848479], [7.748278749278056, 6.094952441924406], [7.768331669096362, 6.069285875001925]], [1, 4, 4, 4, 4, 4, 4]), ('o13', [[7.768331669096362, 6.069285875001925], [7.795826847309178, 6.034093651722774], [7.83098292498843, 6.005624821348352], [7.871122682744982, 5.986047353393342], [7.911262440501534, 5.9664698854383325], [7.9553404276298565, 5.956293680281561], [8.0, 5.956293680281561]], [1, 4, 4, 4, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('T', [0.0, 6.250285012053739], id='l1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, 9], annotation_clip=None)
            c.text('W', [8.0, 6.250285012053739], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 9], annotation_clip=None)
            c.text('X', [8.0, 0.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, -9], annotation_clip=None)
            c.text('Y', [0.0, 0.0], id='l4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -9], annotation_clip=None)
            c.text('Z', [3.032312417601329, 2.3691021069497533], id='l5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, -5], annotation_clip=None)
            c.text('52°', [0.0, 0.0], id='l6', rotation_mode='default', offset_pt=[20.60344389908664, 42.24332017606085], annotation_clip=None)
            c.text('38°', [0.0, 0.0], id='l7', rotation_mode='default', offset_pt=[44.43937305316789, 15.301703259486365], annotation_clip=None)
            c.text('1', [0.0, 6.250285012053739], id='l8', rotation_mode='default', offset_pt=[10.418180942629014, -30.25659441917814], annotation_clip=None)
            c.text('4', [0.0, 6.250285012053739], id='l9', rotation_mode='default', offset_pt=[28.761409481573345, -14.027876697250477], annotation_clip=None)
            c.text('3', [8.0, 6.250285012053739], id='l10', rotation_mode='default', offset_pt=[-34.038668721575405, -11.720453560457642], annotation_clip=None)
            c.text('2', [8.0, 6.250285012053739], id='l11', rotation_mode='default', offset_pt=[-15.781361284406787, -32.356585666770016], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane19().draw(sys.argv[1] if len(sys.argv) > 1 else None))
