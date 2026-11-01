"""Frozen renderer for user-admitted, authored grid and cut-piece questions.

The three explicit profiles preserve reviewed coordinates, caps, fills, text,
and layering. They do not fit layouts or regenerate mathematical constructions.
Workbench overlays continue to use the shared, unchanged PluginRenderer.
"""
from __future__ import annotations

import io
import json
import math
from pathlib import Path

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.patches import Polygon, Circle


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def point(scene, value):
    xy = scene['points'][value] if isinstance(value, str) else value
    if len(xy) != 2 or not all(math.isfinite(v) for v in xy):
        raise ValueError(f'Invalid point: {value!r}')
    return xy


def validate_scene(scene):
    profile = scene['view']['layout']['authored_render_profile']
    if profile not in {'cut', 'grid', 'quick'}:
        raise ValueError('Unknown frozen render profile')
    if scene['constraints']:
        raise ValueError('Construction proofs belong to the frozen provenance ledger')
    x0, x1 = scene['view']['xlim']
    y0, y1 = scene['view']['ylim']
    if not (x1 > x0 and y1 > y0 and math.isclose(x1-x0, y1-y0, abs_tol=1e-10)):
        raise ValueError('A finite square view is required')
    ids = [obj['id'] for obj in scene['objects']]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate object ID')
    for name in scene['points']:
        point(scene, name)
    for obj in scene['objects']:
        if obj['type'] not in {'polygon', 'region', 'segment', 'point', 'circle', 'arrow'}:
            raise ValueError(f"Unsupported object: {obj['type']}")
        for value in obj.get('points', []):
            point(scene, value)
        if obj['type'] == 'point':
            if point(scene, obj['point']) != obj['xy']:
                raise ValueError('Point reference and frozen coordinate disagree')
    return [{'check': 'frozen_view_and_object_references', 'status': 'passed'}]


def render_scene(scene):
    checks = validate_scene(scene)
    profile = scene['view']['layout']['authored_render_profile']
    with matplotlib.rc_context({'font.family': 'DejaVu Sans', 'svg.fonttype': 'path'}):
        fig = Figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
        FigureCanvasAgg(fig)
        ax = fig.add_axes([.05, .05, .90, .90])
        ax.set_aspect('equal')
        ax.set_xlim(scene['view']['xlim'])
        ax.set_ylim(scene['view']['ylim'])
        ax.axis('off')
        ax.set_autoscale_on(False)
        # The legacy adapter captures artists against this frame's `item` ID.
        for item in scene['objects']:
            coords = [point(scene, value) for value in item.get('points', [])]
            typ = item['type']
            color = item.get('color', '#000000')
            width = item.get('linewidth_pt', 1)
            linestyle = item.get('linestyle', 'solid')
            if profile == 'quick':
                linestyle = '-' if linestyle == 'solid' else (0, tuple(item.get('dash_pattern_pt', [4, 3])))
            if profile == 'cut':
                if typ in {'polygon', 'region'}:
                    ax.add_patch(Polygon(coords, closed=True,
                        fill=item.get('semantic_fill', False), facecolor='#D0D0D0',
                        alpha=.45 if item.get('semantic_fill', False) else 1,
                        edgecolor=color if item.get('outline', True) else 'none',
                        linewidth=width, linestyle=linestyle, joinstyle='round'))
                elif typ == 'segment':
                    ax.plot(*zip(*coords), color=color, linewidth=width,
                            linestyle=linestyle, solid_capstyle='round')
                else:
                    raise ValueError(f'Unsupported cut object: {typ}')
            else:
                kwargs = {'linewidth': width, 'linestyle': linestyle,
                          'antialiased': True, 'zorder': item.get('zorder', 2)}
                if typ in {'polygon', 'region'}:
                    ax.add_patch(Polygon(coords, closed=True, edgecolor=color,
                                         facecolor=item.get('fill', 'none'), **kwargs))
                elif typ == 'segment':
                    ax.plot(*zip(*coords), color=color, solid_capstyle='round', **kwargs)
                elif typ == 'point':
                    ax.scatter(*point(scene, item['point']), s=item.get('size_pt2', 36),
                               facecolors=color, edgecolors=color, linewidths=1, zorder=4)
                elif typ == 'circle':
                    ax.add_patch(Circle(point(scene, item['center']), item['radius'],
                                        edgecolor=color, facecolor=item.get('fill', 'none'), **kwargs))
                elif typ == 'arrow':
                    ax.annotate('', xy=coords[1], xytext=coords[0],
                                arrowprops={'arrowstyle': '-|>', 'color': color,
                                            'lw': width, 'mutation_scale': 17}, zorder=3)
                else:
                    raise ValueError(f'Unsupported object: {typ}')
        for label in scene['labels']:
            if profile == 'cut':
                ax.text(*label['xy'], label['text'], ha='center', va='center',
                        fontsize=label.get('fontsize', 16), fontfamily='DejaVu Sans', color='black')
            elif profile == 'grid':
                ax.text(*label['anchor'], label['text'], ha='center', va='center',
                        fontsize=label.get('size_pt', 16), fontfamily='DejaVu Sans',
                        color='black', zorder=5)
            else:
                vertex = label.get('role') == 'vertex'
                ax.annotate(label['text'], label['xy'], xytext=label.get('offset_pt', [0, 0]),
                            textcoords='offset points', ha=label.get('ha', 'center'),
                            va=label.get('va', 'center'), fontsize=18 if vertex else 16,
                            fontstyle='italic' if vertex else 'normal', color='black', zorder=5)
    return fig, checks


def image_bytes(scene, vector=False):
    fig, checks = render_scene(scene)
    output = io.BytesIO()
    fig.savefig(output, format='svg' if vector else 'png', dpi=100,
                facecolor='white', transparent=False)
    return output.getvalue(), checks


def draw(scene_path, output_path=None):
    if output_path is None:
        raise ValueError('An explicit output path is required')
    output_path = Path(output_path)
    if output_path.suffix.lower() not in {'.png', '.svg'}:
        raise ValueError('Output must be PNG or SVG')
    data, _ = image_bytes(read(scene_path), vector=output_path.suffix.lower() == '.svg')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)
    return str(output_path)
