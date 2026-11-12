"""Frozen question Plane461; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane461:

    def __init__(self):
        self.id = 'Plane461'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2600'
        self.question = 'As indicated by the diagram below, a rectangular piece of paper is folded bottom to top, then left to right, and finally, a hole is punched at X.\nWhat does the paper look like when unfolded?\n\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane461.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.7062057200269791, 28.752569016352158), ylim=(-8.752569016352165, 20.706205720026972), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[10.0, 10.0], [14.0, 10.0], [14.0, 12.0], [10.0, 12.0], [10.0, 10.0]], [1, 2, 2, 2, 79], id='o0', capstyle='butt')
            c.line([[10.0, 11.0], [14.0, 11.0]], id='o1', linestyle=(0.0, [4.0, 3.0]))
            c.path([[9.890380592228745, 11.459619407771257], [9.76852869704526, 11.337767512587773], [9.7, 11.172324602769347], [9.7, 11.0], [9.7, 10.827675397230653], [9.76852869704526, 10.662232487412227], [9.890380592228743, 10.540380592228743]], [1, 4, 4, 4, 4, 4, 4], id='o2', facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[9.890380592228745, 11.459619407771257], [9.657035354437184, 11.339411254969544], [9.770172439427032, 11.226274169979696], [9.890380592228745, 11.459619407771257]], [1, 2, 2, 79], id='o3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.890380592228745, 11.459619407771257], [9.657035354437184, 11.339411254969544], [9.770172439427032, 11.226274169979696], [9.890380592228745, 11.459619407771257]], [1, 2, 2, 79], id='o3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.890380592228745, 11.459619407771257], [13.76852869704526, 11.337767512587773], [13.7, 11.172324602769347], [13.7, 11.0], [13.7, 10.827675397230653], [13.76852869704526, 10.662232487412227], [13.890380592228743, 10.540380592228743]], [1, 4, 4, 4, 4, 4, 4], id='o4', facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[13.890380592228745, 11.459619407771257], [13.657035354437184, 11.339411254969544], [13.770172439427032, 11.226274169979696], [13.890380592228745, 11.459619407771257]], [1, 2, 2, 79], id='o5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.890380592228745, 11.459619407771257], [13.657035354437184, 11.339411254969544], [13.770172439427032, 11.226274169979696], [13.890380592228745, 11.459619407771257]], [1, 2, 2, 79], id='o5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 7.2], [14.0, 7.2], [14.0, 8.2], [10.0, 8.2], [10.0, 7.2]], [1, 2, 2, 2, 79], id='o6', capstyle='butt')
            c.line([[12.0, 7.2], [12.0, 8.2]], id='o7', linestyle=(0.0, [4.0, 3.0]))
            c.path([[12.401503505445731, 7.523406431002295], [12.28384556354232, 7.605791408853304], [12.143633825641658, 7.65], [12.0, 7.65], [11.856366174358342, 7.65], [11.71615443645768, 7.605791408853304], [11.598496494554269, 7.523406431002295]], [1, 4, 4, 4, 4, 4, 4], id='o8', facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[12.401503505445731, 7.523406431002295], [12.242601609281568, 7.732332703633176], [12.1508293794654, 7.601268376546937], [12.401503505445731, 7.523406431002295]], [1, 2, 2, 79], id='o9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.401503505445731, 7.523406431002295], [12.242601609281568, 7.732332703633176], [12.1508293794654, 7.601268376546937], [12.401503505445731, 7.523406431002295]], [1, 2, 2, 79], id='o9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.401503505445731, 8.523406431002293], [12.28384556354232, 8.605791408853303], [12.143633825641658, 8.649999999999999], [12.0, 8.649999999999999], [11.856366174358342, 8.649999999999999], [11.71615443645768, 8.605791408853303], [11.598496494554269, 8.523406431002293]], [1, 4, 4, 4, 4, 4, 4], id='o10', facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[12.401503505445731, 8.523406431002293], [12.242601609281568, 8.732332703633174], [12.1508293794654, 8.601268376546935], [12.401503505445731, 8.523406431002293]], [1, 2, 2, 79], id='o11', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.401503505445731, 8.523406431002293], [12.242601609281568, 8.732332703633174], [12.1508293794654, 8.601268376546935], [12.401503505445731, 8.523406431002293]], [1, 2, 2, 79], id='o11', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 4.7], [14.0, 4.7], [14.0, 5.7], [12.0, 5.7], [12.0, 4.7]], [1, 2, 2, 2, 79], id='o12', capstyle='butt')
            c.circle([12.25, 5.45], 0.22, id='o13', facecolor=(0.0, 0.0, 0.0, 0), fill=False)
            c.line([[12.09, 5.29], [12.41, 5.61]], id='o14')
            c.line([[12.09, 5.61], [12.41, 5.29]], id='o15')
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o16', capstyle='butt')
            c.line([[2.0, 0.0], [2.0, 2.0]], id='o17', linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 1.0], [4.0, 1.0]], id='o18', linestyle=(0.0, [4.0, 3.0]))
            for object_id, center, radius in [('o19', [0.25, 0.75], 0.22), ('o20', [1.75, 1.75], 0.22), ('o21', [2.25, 0.25], 0.22), ('o22', [3.75, 1.25], 0.22)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 0), fill=False)
            c.path([[6.0, 0.0], [10.0, 0.0], [10.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='o23', capstyle='butt')
            c.line([[8.0, 0.0], [8.0, 2.0]], id='o24', linestyle=(0.0, [4.0, 3.0]))
            c.line([[6.0, 1.0], [10.0, 1.0]], id='o25', linestyle=(0.0, [4.0, 3.0]))
            for object_id, center, radius in [('o26', [7.75, 1.75], 0.22), ('o27', [8.25, 1.75], 0.22), ('o28', [7.75, 0.25], 0.22), ('o29', [8.25, 0.25], 0.22)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 0), fill=False)
            c.path([[12.0, 0.0], [16.0, 0.0], [16.0, 2.0], [12.0, 2.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='o30', capstyle='butt')
            c.line([[14.0, 0.0], [14.0, 2.0]], id='o31', linestyle=(0.0, [4.0, 3.0]))
            c.line([[12.0, 1.0], [16.0, 1.0]], id='o32', linestyle=(0.0, [4.0, 3.0]))
            for object_id, center, radius in [('o33', [12.25, 1.75], 0.22), ('o34', [15.75, 1.75], 0.22), ('o35', [12.25, 0.25], 0.22), ('o36', [15.75, 0.25], 0.22)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 0), fill=False)
            c.path([[18.0, 0.0], [22.0, 0.0], [22.0, 2.0], [18.0, 2.0], [18.0, 0.0]], [1, 2, 2, 2, 79], id='o37', capstyle='butt')
            c.line([[20.0, 0.0], [20.0, 2.0]], id='o38', linestyle=(0.0, [4.0, 3.0]))
            c.line([[18.0, 1.0], [22.0, 1.0]], id='o39', linestyle=(0.0, [4.0, 3.0]))
            for object_id, center, radius in [('o40', [19.75, 0.75], 0.22), ('o41', [20.25, 0.75], 0.22), ('o42', [19.75, 1.25], 0.22), ('o43', [20.25, 1.25], 0.22)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 0), fill=False)
            c.path([[24.0, 0.0], [28.0, 0.0], [28.0, 2.0], [24.0, 2.0], [24.0, 0.0]], [1, 2, 2, 2, 79], id='o44', capstyle='butt')
            c.line([[26.0, 0.0], [26.0, 2.0]], id='o45', linestyle=(0.0, [4.0, 3.0]))
            c.line([[24.0, 1.0], [28.0, 1.0]], id='o46', linestyle=(0.0, [4.0, 3.0]))
            for object_id, center, radius in [('o47', [24.25, 0.75], 0.22), ('o48', [24.25, 1.25], 0.22), ('o49', [27.75, 0.75], 0.22), ('o50', [27.75, 1.25], 0.22)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 0), fill=False)
            for object_id, text, anchor in [('t0', '(A)', (2.0, 2.7)), ('t1', '(B)', (8.0, 2.7)), ('t2', '(C)', (14.0, 2.7)), ('t3', '(D)', (20.0, 2.7)), ('t4', '(E)', (26.0, 2.7))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane461().draw(sys.argv[1] if len(sys.argv) > 1 else None))
