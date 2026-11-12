"""Workbench hit targets derived from the actual unified Matplotlib artists."""
from __future__ import annotations

import copy
import numpy as np
from matplotlib.collections import LineCollection, PathCollection
from matplotlib.colors import to_hex
from matplotlib.lines import Line2D
from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from matplotlib.transforms import Affine2D

from dataset_tools.unified_workbench import RENDER_LOCK

PRESETS = {
    "point": {"type": "add_point", "filled": True, "color": "#DC2626",
              "size_pt2": 50, "edge_linewidth_pt": 1.0},
    "line": {"type": "add_line", "color": "#2563EB", "linestyle": "dashed",
             "linewidth_pt": 1.0, "dash_pattern_pt": [3.7, 1.6]},
    "colors": ["#DC2626", "#2563EB", "#16A34A", "#EA580C"],
    "object_colors": ["#DC2626", "#2563EB", "#16A34A", "#EA580C", "#000000"],
}


def _pixel_paths(path, transform, width, height):
    paths, current = [], []
    for vertices, code in path.transformed(transform).iter_segments(
            remove_nans=True, clip=(0, 0, width, height), simplify=False, curves=False):
        if code == Path.MOVETO:
            if len(current) > 1:
                paths.append(current)
            current = [[float(vertices[0]), float(height - vertices[1])]]
        elif code == Path.LINETO:
            current.append([float(vertices[0]), float(height - vertices[1])])
        elif code == Path.CLOSEPOLY and current:
            current.append(current[0][:])
    if len(current) > 1:
        paths.append(current)
    return paths


def _artist_paths(artist, width, height, dpi):
    if isinstance(artist, PathCollection):
        for i, offset in enumerate(artist.get_offsets()):
            transform = Affine2D(artist.get_transforms()[i % len(artist.get_transforms())])
            transform.translate(*artist.get_offset_transform().transform(offset))
            yield from _pixel_paths(artist.get_paths()[i % len(artist.get_paths())], transform, width, height)
    elif isinstance(artist, Line2D) and artist.get_linestyle() in ('None', 'none', '', None):
        marker = MarkerStyle(artist.get_marker())
        for point in artist.get_transform().transform(artist.get_xydata()):
            transform = marker.get_transform() + Affine2D().scale(artist.get_markersize() * dpi / 72).translate(*point)
            yield from _pixel_paths(marker.get_path(), transform, width, height)
    else:
        source = artist.get_paths() if isinstance(artist, LineCollection) else [artist.get_path()]
        for path in source:
            yield from _pixel_paths(path, artist.get_transform(), width, height)


def _style(artist):
    if isinstance(artist, PathCollection):
        colors = artist.get_edgecolors()
        if not len(colors):
            colors = artist.get_facecolors()
        color, width, dashed = colors[0], artist.get_linewidths()[0], False
    elif isinstance(artist, LineCollection):
        color, width = artist.get_colors()[0], artist.get_linewidths()[0]
        dashed = artist.get_linestyles()[0][1] is not None
    else:
        color = artist.get_color() if hasattr(artist, 'get_color') else artist.get_edgecolor()
        width = artist.get_linewidth()
        dashed = bool(getattr(artist, '_dash_pattern', (0, None))[1])
    return {'color': to_hex(color).upper(), 'linewidth_pt': float(width),
            'linestyle': 'dashed' if dashed else 'solid'}


def describe_captured_scene(scene, qid, branch):
    scene.fig.canvas.draw()
    width, height = scene.fig.canvas.get_width_height()
    bbox = scene.ax.get_window_extent()
    forward = np.array([[1, 0, 0], [0, -1, height], [0, 0, 1]]) @ scene.ax.transData.get_affine().get_matrix()
    targets = []
    for obj in scene.objects:
        if not obj['styleable']:
            continue
        owned = scene.artists[obj['id']]
        owned = owned if isinstance(owned, list) else [owned]
        styles = [_style(a) for a in owned]
        if not styles:
            raise ValueError('Missing editable object: ' + obj['id'])
        partial = []
        if branch != 'Analytics' and obj['kind'] != 'point':
            from partial_style import describe_paths
            partial = describe_paths(scene, obj['id'])
        targets.append({**copy.deepcopy(obj), 'paths': [p for a in owned for p in _artist_paths(a, width, height, scene.fig.dpi)],
                        'partial_paths': partial, **styles[0], 'fragment_styles': styles,
                        'fragment_linestyles': [s['linestyle'] for s in styles]})
    return {'question_id': qid, 'branch': branch, 'width': width, 'height': height,
            'plot_bounds': [float(bbox.x0), float(height-bbox.y1), float(bbox.x1), float(height-bbox.y0)],
            'data_to_pixel': forward.tolist(), 'pixel_to_data': np.linalg.inv(forward).tolist(),
            'xlim': list(scene.ax.get_xlim()), 'ylim': list(scene.ax.get_ylim()), 'targets': targets,
            'snap_points': [{**copy.deepcopy(p), 'pixel': (forward @ [*p['xy'], 1])[:2].tolist()} for p in scene.snap_points],
            'coordinate_system': 'frozen_projected_2d', 'presets': copy.deepcopy(PRESETS)}


def describe_scene(adapter, qid):
    with RENDER_LOCK:
        scene = adapter.scene(qid)
        try:
            return describe_captured_scene(scene, qid, adapter.branch_name)
        finally:
            scene.close()
