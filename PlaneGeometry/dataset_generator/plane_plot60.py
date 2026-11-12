"""Frozen question Plane60; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane60:

    def __init__(self):
        self.id = 'Plane60'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/776'
        self.question = 'Find $JQ$ if $Q$ is the incenter of $\\triangle JLN$.  Rounded to the nearest hundredth.\nChoices:\nA: 16.50\nB: 18.79\nC: 20.32\nD: 25.50'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '16.50', 'B': '18.79', 'C': '20.32', 'D': '25.50'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane60.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.5293673180043967, 37.24029192045133], ylim=[-26.49632144968667, 13.273337788769055], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[18.010640629467627, -5.372785508111222], [16.139435412107794, 3.4305428984930293]], id='segment6')
            c.line([[15.435937930082032, 3.281009892570115], [15.585470936004945, 2.577512410544354]], id='right_angle7', zorder=3)
            c.line([[15.585470936004945, 2.577512410544354], [16.28896841803071, 2.727045416467268]], id='right_angle7', zorder=3)
            c.line([[18.010640629467627, -5.372785508111222], [11.622188997644853, -11.712161325008415]], id='segment11')
            c.line([[11.115592546982342, -11.201643094919543], [11.626110777071213, -10.695046644257031]], id='right_angle12', zorder=3)
            c.line([[11.626110777071213, -10.695046644257031], [12.132707227733725, -11.205564874345903]], id='right_angle12', zorder=3)
            c.line([[18.010640629467627, -5.372785508111222], [25.957168965197965, -9.598029573184244]], id='segment16')
            c.line([[26.29481950183968, -8.963001272883783], [25.659791201539218, -8.625350736242071]], id='right_angle17', zorder=3)
            c.line([[25.659791201539218, -8.625350736242071], [25.322140664897503, -9.260379036542531]], id='right_angle17', zorder=3)
            for object_id, points in [('segment20', [[0.0, 0.0], [35.01823410358901, 7.443355436814789]]), ('segment21', [[35.01823410358901, 7.443355436814789], [20.22399638468588, -20.380558975751228]]), ('segment22', [[20.22399638468588, -20.380558975751228], [0.0, 0.0]]), ('segment23', [[0.0, 0.0], [18.010640629467627, -5.372785508111222]]), ('segment24', [[35.01823410358901, 7.443355436814789], [18.010640629467627, -5.372785508111222]]), ('segment25', [[20.22399638468588, -20.380558975751228], [18.010640629467627, -5.372785508111222]])]:
                c.line(points, id=object_id)
            c.line([[-1.561621510001122, -1.5496251996859804], [10.06056748764373, -13.261786524694395]], id='segment28', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [-1.561621510001122, -1.5496251996859804]], id='segment29')
            c.line([[11.622188997644853, -11.712161325008415], [10.06056748764373, -13.261786524694395]], id='segment30')
            c.text('J', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13, 5], annotation_clip=None)
            c.text('Q', [18.010640629467627, -5.372785508111222], id='label2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15.426902632476946, 18.385066634855473], annotation_clip=None)
            c.text('L', [35.01823410358901, 7.443355436814789], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 10], annotation_clip=None)
            c.text('N', [20.22399638468588, -20.380558975751228], id='label4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -16], annotation_clip=None)
            c.text('K', [16.139435412107794, 3.4305428984930293], id='label5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-2, 15], annotation_clip=None)
            c.text('P', [11.622188997644853, -11.712161325008415], id='label10', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16.0, 1.959434878635765e-15], annotation_clip=None)
            c.text('M', [25.957168965197965, -9.598029573184244], id='label15', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, -4], annotation_clip=None)
            c.text('16.5', [4.249472988821305, -7.405705862190188], id='text32', rotation_mode='default', offset_pt=[-15.61621510001122, -15.496251996859804], annotation_clip=None)
            c.text('9', [21.983904797332798, -7.485407540647733], id='text37', rotation_mode='default', offset_pt=[0, 14], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane60().draw(sys.argv[1] if len(sys.argv) > 1 else None))
