"""Author hit targets, including the actual scatter markers."""
import copy
import math
import numpy as np
from matplotlib.collections import PathCollection
from matplotlib.colors import to_hex
from matplotlib.patches import Patch
from drawing_board import PRESETS, _pixel_paths
from partial_style import describe_paths
from renderer_adapter import RENDER_LOCK


def describe_scene(adapter, qid):
    with RENDER_LOCK:
        scene = adapter.scene(qid)
        try: return describe_captured_scene(scene, qid)
        finally: scene.close()


def describe_captured_scene(scene, qid):
    scene.fig.canvas.draw()
    width, height = scene.fig.canvas.get_width_height()
    bbox = scene.ax.get_window_extent()
    forward = np.array([[1, 0, 0], [0, -1, height], [0, 0, 1]]) @ scene.ax.transData.get_affine().get_matrix()
    targets = []
    for obj in scene.objects:
        paths, styles = [], []
        point = obj['kind'] == 'point'
        for artist in scene.artists[obj['id']]:
            if isinstance(artist, PathCollection):
                # Matplotlib's marker path is in marker coordinates, not data
                # coordinates. Its real offsets and size give a selectable ring.
                for offset, size in zip(artist.get_offsets(), artist.get_sizes()):
                    px, py = artist.get_offset_transform().transform(offset)
                    radius = math.sqrt(float(size)) * scene.fig.dpi / 72 / 2
                    paths.append([[float(px + radius * math.cos(t)), float(height - py - radius * math.sin(t))]
                                  for t in np.linspace(0, 2 * math.pi, 25)])
                color = to_hex(artist.get_facecolors()[0]).upper()
                lw = float(artist.get_linewidths()[0])
                dashed = False
            else:
                paths.extend(_pixel_paths(artist.get_path(), artist.get_transform(), width, height))
                color = to_hex(artist.get_edgecolor() if isinstance(artist, Patch) else artist.get_color()).upper()
                lw = float(artist.get_linewidth())
                dashed = bool(getattr(artist, '_dash_pattern', (0, None))[1]) if not isinstance(artist, Patch) else artist.get_linestyle() not in ('-', 'solid')
            styles.append({'color': color, 'linewidth_pt': lw, 'linestyle': 'dashed' if dashed else 'solid'})
        targets.append({'id': obj['id'], 'kind': obj['kind'], 'paths': paths,
                        'partial_paths': [] if point else describe_paths(scene, obj['id']),
                        'source_call': obj['source_call'], 'frozen_visibility': obj['frozen_visibility'],
                        **styles[0], 'fragment_styles': styles,
                        'fragment_linestyles': [s['linestyle'] for s in styles]})
    return {'question_id': qid, 'branch': 'PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry',
            'width': width, 'height': height,
            'plot_bounds': [float(bbox.x0), float(height-bbox.y1), float(bbox.x1), float(height-bbox.y0)],
            'data_to_pixel': forward.tolist(), 'pixel_to_data': np.linalg.inv(forward).tolist(),
            'xlim': list(scene.ax.get_xlim()), 'ylim': list(scene.ax.get_ylim()),
            'coordinate_system': 'frozen_projected_2d', 'targets': targets,
            'snap_points': [{**copy.deepcopy(p), 'pixel': (forward @ [*p['xy'], 1])[:2].tolist()} for p in scene.snap_points],
            'presets': copy.deepcopy(PRESETS)}
