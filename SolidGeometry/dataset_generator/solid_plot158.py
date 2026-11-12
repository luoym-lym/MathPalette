"""Frozen question Solid158; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid158:

    def __init__(self):
        self.id = 'Solid158'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1319'
        self.question = 'A 3-pyramid is a stack of the 3 layers of balls shown. A 4-pyramid, a 5-pyramid, and so on are defined in the same way. All the outside balls of an 8-pyramid are removed. What figure do the remaining balls form?\nChoices:\nA:3-pyramid\nB:4-pyramid\nC:5-pyramid\nD:6-pyramid\nE:7-pyramid'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '3-pyramid', 'B': '4-pyramid', 'C': '5-pyramid', 'D': '6-pyramid', 'E': '7-pyramid'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid158.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.6930085051841903, 26.693008505184196], ylim=[-14.193009211948745, 14.193007798419643], projection=[[0.5000000000000001, 0.8660254037844386, 0.0], [-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]], origin=[0, 0, 0], offset=[0, 0]) as c:
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
            for object_id, points in [('layer2sphere0arc0', c.project(xyz)), ('arrow0', c.project([[8.000000000000002, 13.856406460551018, 0.0], [9.000000000000002, 15.588457268119894, 0.0]])), ('arrow1', c.project([[9.000000000000002, 15.588457268119894, 0.0], [8.799792047161127, 15.299902195152583, 0.1369406641027328]])), ('arrow2', c.project([[9.000000000000002, 15.588457268119894, 0.0], [8.850207952838876, 15.270794558438098, -0.1369406641027328]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(82.78515420164942, 282.29765237694005, 401))
            xyz = np.asarray([10.701151696118554, 18.070398493571215, -1.0927443028767685]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere0arc1')
            t = np.radians(np.linspace(82.78515420164942, 246.735610317267, 329))
            xyz = np.asarray([11.701151696118554, 18.64774876276084, 0.5402488589786836]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere1arc1')
            t = np.radians(np.linspace(0.0, 246.735610317267, 495))
            xyz = np.asarray([12.701151696118554, 19.225099031950467, 2.1732420208341354]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere2arc0')
            t = np.radians(np.linspace(293.2643896827686, 360.0, 135))
            xyz = np.asarray([12.701151696118554, 19.225099031950467, 2.1732420208341354]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere2arc2')
            t = np.radians(np.linspace(0.0, 97.21484579836243, 196))
            xyz = np.asarray([12.701151696118554, 20.379799570329716, 0.5402488589786836]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere4arc0')
            t = np.radians(np.linspace(293.2643896827686, 360.0, 135))
            xyz = np.asarray([12.701151696118554, 20.379799570329716, 0.5402488589786836]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere4arc2')
            t = np.radians(np.linspace(0.0, 97.21484579836243, 196))
            xyz = np.asarray([12.701151696118554, 21.53450010870897, -1.0927443028767685]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere5arc0')
            t = np.radians(np.linspace(257.70234762303824, 360.0, 206))
            xyz = np.asarray([12.701151696118554, 21.53450010870897, -1.0927443028767685]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere5arc2')
            t = np.radians(np.linspace(82.78515420164942, 282.29765237694005, 401))
            xyz = np.asarray([12.701151696118554, 18.070398493571215, -1.0927443028767685]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere6arc1')
            t = np.radians(np.linspace(0.0, 246.735610317267, 495))
            xyz = np.asarray([13.701151696118554, 18.64774876276084, 0.5402488589786836]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere7arc0')
            t = np.radians(np.linspace(293.2643896827686, 360.0, 135))
            xyz = np.asarray([13.701151696118554, 18.64774876276084, 0.5402488589786836]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere7arc2')
            t = np.radians(np.linspace(0.0, 97.21484579836243, 196))
            xyz = np.asarray([13.701151696118554, 19.802449301140093, -1.0927443028767685]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere8arc0')
            t = np.radians(np.linspace(257.70234762303824, 360.0, 206))
            xyz = np.asarray([13.701151696118554, 19.802449301140093, -1.0927443028767685]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere8arc2')
            t = np.radians(np.linspace(0.0, 360.0, 721))
            xyz = np.asarray([14.701151696118554, 18.070398493571215, -1.0927443028767685]) + 1 * (np.cos(t)[:, None] * np.array([0.5000000000000001, 0.8660254037844386, 0.0]) + np.sin(t)[:, None] * np.array([-0.1800568059919554, 0.1039558454088797, 0.9781476007338057]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='assembledsphere9arc0')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid158().draw(sys.argv[1] if len(sys.argv) > 1 else None))
