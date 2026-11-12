"""Frozen question Plane181; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane181:

    def __init__(self):
        self.id = 'Plane181'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:247'
        self.question = "A rectangular piece of paper $A B C D$ with the measurements $4 \\mathrm{~cm} \\times 16 \\mathrm{~cm}$ is folded along the line $\\mathrm{MN}$ so that point $C$ coincides with point $A$ as shown. How big is the area of the quadrilateral ANMD'?\nChoices:\nA:$28 \\mathrm{~cm}^{2}$\nB:$30 \\mathrm{~cm}^{2}$\nC:$32 \\mathrm{~cm}^{2}$\nD:$48 \\mathrm{~cm}^{2}$\nE:$56 \\mathrm{~cm}^{2}$"
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$28 \\mathrm{~cm}^{2}$', 'B': '$30 \\mathrm{~cm}^{2}$', 'C': '$32 \\mathrm{~cm}^{2}$', 'D': '$48 \\mathrm{~cm}^{2}$', 'E': '$56 \\mathrm{~cm}^{2}$'}
        self.query = self.question
        self._geometry_01 = [('o11', [[16.0, 4.0], [15.638009049773755, 4.331897443706739]]),
         ('o12', [[15.638009049773755, 4.331897443706739], [15.27601809954751, 4.6622293176864025]]),
         ('o13', [[15.27601809954751, 4.6622293176864025], [14.914027149321267, 4.989440205532357]]),
         ('o14', [[14.914027149321267, 4.989440205532357], [14.552036199095022, 5.311994931630663]]),
         ('o15', [[14.552036199095022, 5.311994931630663], [14.190045248868778, 5.628388517363031]]),
         ('o16', [[14.190045248868778, 5.628388517363031], [13.828054298642535, 5.937155941470672]]),
         ('o17', [[13.828054298642535, 5.937155941470672], [13.46606334841629, 6.23688164127933]]),
         ('o18', [[13.46606334841629, 6.23688164127933], [13.104072398190047, 6.526208693166425]]),
         ('o19', [[13.104072398190047, 6.526208693166425], [12.742081447963802, 6.803847612731435]]),
         ('o20', [[12.742081447963802, 6.803847612731435], [12.380090497737557, 7.068584717597055]]),
         ('o21', [[12.380090497737557, 7.068584717597055], [12.018099547511312, 7.319289998605136]]),
         ('o22', [[12.018099547511312, 7.319289998605136], [11.656108597285067, 7.554924448359702]]),
         ('o23', [[11.656108597285067, 7.554924448359702], [11.294117647058824, 7.77454679958861]]),
         ('o24', [[11.294117647058824, 7.77454679958861], [10.932126696832578, 7.977319629623002]]),
         ('o25', [[10.932126696832578, 7.977319629623002], [10.570135746606335, 8.16251479140466]]),
         ('o26', [[10.570135746606335, 8.16251479140466], [10.20814479638009, 8.329518135799095]]),
         ('o27', [[10.20814479638009, 8.329518135799095], [9.846153846153847, 8.477833494588342]]),
         ('o28', [[9.846153846153847, 8.477833494588342], [9.484162895927604, 8.607085898312262]]),
         ('o29', [[9.484162895927604, 8.607085898312262], [9.122171945701357, 8.717024008089368]]),
         ('o30', [[9.122171945701357, 8.717024008089368], [8.760180995475114, 8.80752174564593]]),
         ('o31', [[8.760180995475114, 8.80752174564593], [8.39819004524887, 8.878579110981946]]),
         ('o32', [[8.39819004524887, 8.878579110981946], [8.036199095022624, 8.930322182371146]]),
         ('o33', [[8.036199095022624, 8.930322182371146], [7.6742081447963795, 8.963002298695022]]),
         ('o34', [[7.6742081447963795, 8.963002298695022], [7.3122171945701355, 8.976994429413711]]),
         ('o35', [[7.3122171945701355, 8.976994429413711], [6.9502262443438925, 8.972794742745174]]),
         ('o36', [[6.9502262443438925, 8.972794742745174], [6.588235294117648, 8.951017387823905]]),
         ('o37', [[6.588235294117648, 8.951017387823905], [6.226244343891403, 8.912390511708118]]),
         ('o38', [[6.226244343891403, 8.912390511708118], [5.864253393665159, 8.857751537066674]]),
         ('o39', [[5.864253393665159, 8.857751537066674], [5.502262443438914, 8.788041731171717]]),
         ('o40', [[5.502262443438914, 8.788041731171717], [5.140271493212671, 8.704300101419218]]),
         ('o41', [[5.140271493212671, 8.704300101419218], [4.778280542986426, 8.60765665696733]]),
         ('o42', [[4.778280542986426, 8.60765665696733], [4.416289592760181, 8.499325080193358]]),
         ('o43', [[4.416289592760181, 8.499325080193358], [4.0542986425339365, 8.380594855497822]]),
         ('o44', [[4.0542986425339365, 8.380594855497822], [3.692307692307692, 8.252822906503303]]),
         ('o45', [[3.692307692307692, 8.252822906503303], [3.330316742081449, 8.117424795884055]]),
         ('o46', [[3.330316742081449, 8.117424795884055], [2.9683257918552046, 7.9758655448988725]]),
         ('o47', [[2.9683257918552046, 7.9758655448988725], [2.60633484162896, 7.829650132166042]]),
         ('o48', [[2.60633484162896, 7.829650132166042], [2.244343891402715, 7.680313733299499]]),
         ('o49', [[2.244343891402715, 7.680313733299499], [1.8823529411764706, 7.529411764705882]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane181.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.1495935972020357, 17.11111623818239], ylim=[-4.919114551988977, 13.34159528339545], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 4.0], [7.5, 0.0], [8.5, 4.0], [1.8823529411764706, 7.529411764705882], [0.0, 4.0]], [1, 2, 2, 2, 79], id='o0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 4.0], [7.5, 0.0], [8.5, 4.0], [1.8823529411764706, 7.529411764705882], [0.0, 4.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('o1', [[0.0, 4.0], [0.0, 0.0]]), ('o2', [[0.0, 0.0], [7.5, 0.0]]), ('o3', [[0.0, 4.0], [8.5, 4.0]]), ('o4', [[0.0, 4.0], [7.5, 0.0]]), ('o5', [[7.5, 0.0], [8.5, 4.0]]), ('o6', [[8.5, 4.0], [1.8823529411764706, 7.529411764705882]]), ('o7', [[1.8823529411764706, 7.529411764705882], [0.0, 4.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('o8', [[7.5, 0.0], [16.0, 0.0]]), ('o9', [[16.0, 0.0], [16.0, 4.0]]), ('o10', [[16.0, 4.0], [8.5, 4.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[6.226244343891403, 8.912390511708118], [6.535161281427627, 8.844786327642039], [6.513940404360031, 9.043657326976989], [6.226244343891403, 8.912390511708118]], [1, 2, 2, 79], id='o50', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.226244343891403, 8.912390511708118], [6.535161281427627, 8.844786327642039], [6.513940404360031, 9.043657326976989], [6.226244343891403, 8.912390511708118]], [1, 2, 2, 79], id='o50', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.text('A', [0.0, 4.0], id='labelA', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13, 7], annotation_clip=None)
            c.text('B', [0.0, 0.0], id='labelB', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -12], annotation_clip=None)
            c.text('C', [16.0, 0.0], id='labelC', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, -12], annotation_clip=None)
            c.text('D', [16.0, 4.0], id='labelD', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 9], annotation_clip=None)
            c.text('N', [7.5, 0.0], id='labelN', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -13], annotation_clip=None)
            c.text('M', [8.5, 4.0], id='labelM', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8, 12], annotation_clip=None)
            c.text('D′', [1.8823529411764706, 7.529411764705882], id='labelDp', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-6, 14], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane181().draw(sys.argv[1] if len(sys.argv) > 1 else None))
