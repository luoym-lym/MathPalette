"""Frozen question Plane427; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane427:

    def __init__(self):
        self.id = 'Plane427'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1890'
        self.question = 'The diagram shows an equilateral triangle RST and also the triangle $T U V$ obtained by rotating triangle $R S T$ about the point $T$. Angle $R T V=70^{\\circ}$. What is angle $R S V$?\nChoices:\nA:$20^{\\circ}$\nB:$25^{\\circ}$\nC:$30^{\\circ}$\nD:$35^{\\circ}$\nE:$40^{\\circ}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$20^{\\circ}$', 'B': '$25^{\\circ}$', 'C': '$30^{\\circ}$', 'D': '$35^{\\circ}$', 'E': '$40^{\\circ}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane427.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.7152349574038777, 12.695553545906007), ylim=(-4.766068655660694, 8.64471984764919), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[3.2678342100901627, 5.032023407672544], [0.0, 0.0], [5.991777208527443, -0.314015737457663], [3.2678342100901627, 5.032023407672544]], [1, 2, 2, 79], id='o0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.2678342100901627, 5.032023407672544], [0.0, 0.0], [5.991777208527443, -0.314015737457663], [3.2678342100901627, 5.032023407672544]], [1, 2, 2, 79], id='o0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.991777208527443, -0.314015737457663], [11.837997597238854, -1.663722063520853], [10.083767368902434, 4.07410647225736], [5.991777208527443, -0.314015737457663]], [1, 2, 2, 79], id='o1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.991777208527443, -0.314015737457663], [11.837997597238854, -1.663722063520853], [10.083767368902434, 4.07410647225736], [5.991777208527443, -0.314015737457663]], [1, 2, 2, 79], id='o1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [10.083767368902434, 4.07410647225736]], id='o2', linestyle=(0.0, [1.0, 1.65]))
            c.path([[6.451230562919279, 0.17868766350802368], [6.35013217093734, 0.27296343921544053], [6.222425620059838, 0.3338763393492824], [6.085536302129011, 0.3531148783531217], [5.948646984198185, 0.37235341735696104], [5.8090976977912065, 0.3490008756741668], [5.685929760524422, 0.28624367707500686]], [1, 4, 4, 4, 4, 4, 4], id='o3', zorder=3, facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[0.5746610791164577, 0.23217814692978084], [0.5509769726548714, 0.2907983674677647], [0.5184620708684249, 0.3454510037453481], [0.47824669678869325, 0.3942361535599471], [0.4380313227089616, 0.44302130337454615], [0.3905869450364467, 0.48536702945805854], [0.33756288361699105, 0.5198012575660242]], [1, 4, 4, 4, 4, 4, 4], id='o4', zorder=3, facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.text('S', (0.0, 0.0), id='lS', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-10, -15), annotation_clip=None)
            c.text('T', (5.991777208527443, -0.314015737457663), id='lT', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-3, -16), annotation_clip=None)
            c.text('R', (3.2678342100901627, 5.032023407672544), id='lR', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
            c.text('V', (10.083767368902434, 4.07410647225736), id='lV', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, 14), annotation_clip=None)
            c.text('U', (11.837997597238854, -1.663722063520853), id='lU', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, 0), annotation_clip=None)
            c.text('70°', (5.991777208527443, -0.314015737457663), id='a70', rotation_mode='default', offset_pt=(5.8452702403227494, 41.591258887145955), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane427().draw(sys.argv[1] if len(sys.argv) > 1 else None))
