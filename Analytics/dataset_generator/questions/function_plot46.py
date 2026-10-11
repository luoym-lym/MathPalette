"""Frozen MathVista testmini/671; user-reviewed import."""
from pathlib import Path
import sys
import numpy as np
_HELPERS = Path(__file__).resolve().parents[1]
if str(_HELPERS) not in sys.path: sys.path.insert(0, str(_HELPERS))
from common_renderer import open_canvas, plot_curve, scatter_points, label, fill_region, fill_polygon, finalize
SCENE = {'id': 'Ana46', 'view': {'xlim': [-8, 8], 'ylim': [-8, 8], 'aspect': 'equal'}, 'protocol_version': '1.0.0', 'sampling': 'frozen deterministic linspace; no random sampling', 'objects': [{'type': 'semicircle', 'center': [3, 0], 'radius': 3, 'theta_deg': [0, 180], 'samples': 721}, {'type': 'region', 'x_interval': [3, 6], 'upper': 'sqrt(9-(x-3)^2)', 'lower': 0, 'samples': 721}], 'labels': [{'xy': [3.1, 4], 'text': '$f(x)=\\sqrt{9-(x-3)^2}$'}], 'constraints': ['Semicircle center (3,0), radius 3, upper branch; shaded region is x=3 to x=6.']}

class Ana46:
    def __init__(self):
        self.id = 'Ana46'
        self.source_dataset = 'MathVista'
        self.query = 'What is the size of the semicircle rounded to 2 decimal places?'
        self.answer = '14.14'
        self.answer_type = 'number'
        self.subject = 'Analytics'
        self.level = 'high_school'

    def draw(self, num=0, output_path=None):
        fig, ax = open_canvas()
        for obj in SCENE['objects']:
            kind = obj['type']
            if kind in ('circle', 'semicircle'):
                t = np.linspace(*np.deg2rad(obj.get('theta_deg', [0, 360])), obj['samples'])
                c, r = obj['center'], obj['radius']
                plot_curve(ax, c[0]+r*np.cos(t), c[1]+r*np.sin(t))
            elif kind == 'polygon':
                p = np.array(obj['points'])
                if obj.get('semantic_fill'): fill_polygon(ax, p[:, 0], p[:, 1])
                q = np.vstack([p, p[0]])
                plot_curve(ax, q[:, 0], q[:, 1])
            elif kind == 'region':
                x = np.linspace(*obj['x_interval'], obj['samples'])
                fill_region(ax, x, np.sqrt(np.maximum(0, 9-(x-3)**2)), 0)
            elif kind == 'points':
                p = np.array(list(obj['points'].values()))
                scatter_points(ax, p[:, 0], p[:, 1])
                ax.collections[-1].set_clip_on(False)
            elif kind == 'line':
                p = np.array(obj['points'])
                plot_curve(ax, p[:, 0], p[:, 1])
            else:
                raise ValueError('Unsupported frozen analytic object: '+kind)
        for entry in SCENE['labels']: label(ax, *entry['xy'], entry['text'])
        target = Path(output_path) if output_path else _HELPERS.parents[1]/'.runtime/reproduced/Analytics'/f'{self.id}.png'
        return finalize(fig, target)
