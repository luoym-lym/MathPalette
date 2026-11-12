"""Frozen question Solid194; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid194:

    def __init__(self):
        self.id = 'Solid194'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1849'
        self.question = 'An $n$-pyramid is defined to be a stack of $n$ layers of balls, with each layer forming a triangular array. The layers of a 3-pyramid are shown in the diagram.\nAn 8-pyramid is now formed where all the balls on the outside of the 8 -pyramid are black (including the base layer) and the balls on the inside are all white. How many layers are there in the white pyramid?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid194.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.410671706775819, 15.410671706775819], ylim=[-8.410671706775819, 8.410671706775819], projection=[[0.5000000000000001, 0.8660254037844386, 0.0], [-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([-0.311867536226639, 0.18005680599195545, 1.6942013417725479]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer0sphere0arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([0.6881324637733612, 1.9121076135608326, 1.6942013417725479]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer0sphere1arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([1.6881324637733615, 3.64415842112971, 1.6942013417725479]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer0sphere2arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([0.5000000000000001, 0.8660254037844386, 0.0]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer0sphere3arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([1.5000000000000004, 2.598076211353316, 0.0]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer0sphere4arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([1.3118675362266392, 1.5519940015769218, -1.6942013417725479]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer0sphere5arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([3.8440662318866816, 7.018231633271487, 0.8471006708862739]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer1sphere0arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([4.844066231886681, 8.750282440840364, 0.8471006708862739]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer1sphere1arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([4.655933768113321, 7.704200231063969, -0.8471006708862739]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer1sphere2arc0')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([7.000000000000002, 12.12435565298214, 0.0]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='layer2sphere0arc0')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid194().draw(sys.argv[1] if len(sys.argv) > 1 else None))
