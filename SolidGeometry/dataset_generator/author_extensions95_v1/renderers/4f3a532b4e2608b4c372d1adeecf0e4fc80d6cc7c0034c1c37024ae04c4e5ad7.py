"""Data-only redraw. Importing this module neither creates files nor renders.

Local authoring renderer; frozen 3D points, one projection and visibility intervals.
Usage: python -X utf8 -B render.py --output baseline.png
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def read_scene():
    return json.loads(Path(__file__).with_name('scene.json').read_text(encoding='utf-8'))


def project(scene, xyz):
    p = scene['projection']
    return [sum(row[j] * (xyz[j] - p['origin'][j]) for j in range(3)) + p['offset'][i]
            for i, row in enumerate(p['matrix'])]


def curve_points(scene, obj, interval):
    if obj['type'] == 'segment':
        return [project(scene, scene['points'][name]) for name in obj['points']]
    c = scene['points'][obj['center']]
    lo, hi, n = interval['start_deg'], interval['end_deg'], interval['samples']
    out = []
    for i in range(n):
        a = math.radians(lo + (hi - lo) * i / (n - 1))
        xyz = [c[j] + obj['radius'] * (math.cos(a) * obj['u'][j] + math.sin(a) * obj['v'][j])
               for j in range(3)]
        out.append(project(scene, xyz))
    return out


def make_figure(scene):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 16,
                     'mathtext.fontset': 'dejavusans', 'svg.fonttype': 'path',
                     'svg.hashsalt': 'Solid210-author-originals-v1',
                     'lines.linewidth': 1.0, 'savefig.transparent': False,
                     'path.simplify': False})
    fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
    ax = fig.add_axes(scene['view']['layout']['axes_position'])
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(scene['view']['xlim'])
    ax.set_ylim(scene['view']['ylim'])
    ax.set_autoscale_on(False)
    ax.set_axis_off()
    artists = []
    fragments = []
    for obj in scene['objects']:
        intervals = obj.get('intervals', [{'visibility': obj.get('visibility', 'visible')}])
        for i, interval in enumerate(intervals):
            dash = interval['visibility'] == 'hidden' or obj.get('linestyle') == 'dashed'
            fragments.append((not dash, obj, interval, i, dash))
    # Hidden/semantic auxiliary dashes first; visible contours above them.
    fragments.sort(key=lambda entry: entry[0])
    for _, obj, interval, i, dash in fragments:
        xy = curve_points(scene, obj, interval)
        line, = ax.plot([p[0] for p in xy], [p[1] for p in xy], color='black',
                        linewidth=1.0, linestyle=(0, (4, 3)) if dash else '-',
                        solid_capstyle='round', dash_capstyle='butt',
                        antialiased=True, clip_on=False)
        line.set_gid(obj['id'] + (f'__{i}' if len(obj.get('intervals', [])) > 1 else ''))
        artists.append(line)
    for label in scene['labels']:
        anchor = project(scene, scene['points'][label['anchor']])
        t = ax.annotate(label['text'], anchor, xytext=label['offset_pt'],
                        textcoords='offset points', ha=label.get('ha', 'center'),
                        va=label.get('va', 'center'), fontsize=16,
                        fontfamily='DejaVu Sans', color='black',
                        annotation_clip=False, clip_on=False)
        t.set_gid(label['id'])
        artists.append(t)
    return fig, ax, artists


def content_bbox(fig, artists):
    from matplotlib.transforms import Bbox
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bounds = []
    for artist in artists:
        b = artist.get_window_extent(renderer)
        if b.width == 0 and b.height == 0:
            continue
        bounds.append(b.padded(0.7) if hasattr(artist, 'get_linewidth') else b)
    return Bbox.union(bounds)


def fit_once(scene):
    """Authoring-only explicit fit; default rendering never updates the scene."""
    import matplotlib.pyplot as plt
    for _ in range(12):
        fig, ax, artists = make_figure(scene)
        bbox = content_bbox(fig, artists)
        x, y = ax.transData.inverted().transform([(bbox.x0 + bbox.x1) / 2,
                                               (bbox.y0 + bbox.y1) / 2])
        old = scene['view']['xlim'][1] - scene['view']['xlim'][0]
        span = old * max(bbox.width, bbox.height) / (768 * .86)
        scene['view']['xlim'] = [float(x - span / 2), float(x + span / 2)]
        scene['view']['ylim'] = [float(y - span / 2), float(y + span / 2)]
        plt.close(fig)
    # Text extents include unused font ascent/descent. Freeze the actual ink box
    # too, so the PNG itself, including theta and digits, is centered within 2px.
    import numpy as np
    for _ in range(10):
        fig, ax, artists = make_figure(scene)
        fig.canvas.draw()
        rgba = np.asarray(fig.canvas.buffer_rgba())
        rows, cols = np.where(np.any(rgba[:, :, :3] < 255, axis=2))
        x0, x1, y0, y1 = int(cols.min()), int(cols.max())+1, int(rows.min()), int(rows.max())+1
        x, y = ax.transData.inverted().transform([(x0+x1)/2, 768-(y0+y1)/2])
        old = scene['view']['xlim'][1]-scene['view']['xlim'][0]
        span = old*max(x1-x0, y1-y0)/(768*.86)
        scene['view']['xlim'] = [float(x-span/2), float(x+span/2)]
        scene['view']['ylim'] = [float(y-span/2), float(y+span/2)]
        plt.close(fig)
    fig, _, artists = make_figure(scene)
    b = content_bbox(fig, artists)
    scene['view']['layout']['artist_bbox_px_bottom_origin'] = list(b.extents)
    rgba = np.asarray(fig.canvas.buffer_rgba())
    rows, cols = np.where(np.any(rgba[:, :, :3] < 255, axis=2))
    x0, x1, y0, y1 = int(cols.min()), int(cols.max())+1, int(rows.min()), int(rows.max())+1
    scene['view']['layout']['ink_bbox_px_top_origin'] = [x0, y0, x1, y1]
    scene['view']['layout']['content_center_deviation_px'] = [(x0+x1)/2-384, (y0+y1)/2-384]
    plt.close(fig)


def drawing_context(scene):
    editable = []
    attachments = []
    for obj in scene['objects']:
        if obj['role'] in ('edge', 'silhouette', 'sheet_boundary'):
            intervals = obj.get('intervals', [{'visibility': obj.get('visibility', 'visible')}])
            fragments = []
            for interval in intervals:
                xy = curve_points(scene, obj, interval)
                fragments.append({'visibility': interval['visibility'], 'page_polyline': xy})
            editable.append({'id': obj['id'], 'type': obj['type'], 'role': obj['role'],
                             'independent_contour': True, 'fragments': fragments})
    for name, xyz in scene['points'].items():
        if name.endswith(('_O', '_A', '_L', '_T', '_R')) or name.startswith('sector_') and name in (
                'sector_O', 'sector_start', 'sector_end'):
            attachments.append({'id': name, 'world_xyz': xyz, 'page_xy': project(scene, xyz)})
    return {'scene_id': scene['id'], 'coordinates': 'projected page data before final viewport',
            'editable_objects': editable, 'snap_points': attachments,
            'excluded': 'Text, fills, angle marks, and dimension/measurement auxiliary lines are not editable contours.',
            'geometry_projection_visibility_frozen': True,
            'future_special_adapter_deferred': True}


def main():
    import matplotlib.pyplot as plt
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='baseline.png')
    parser.add_argument('--fit', action='store_true')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    scene = read_scene()
    if args.fit:
        fit_once(scene)
        (here / 'scene.json').write_text(json.dumps(scene, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        (here / 'drawing_context.json').write_text(json.dumps(drawing_context(scene), indent=2) + '\n', encoding='utf-8')
    fig, _, artists = make_figure(scene)
    b = content_bbox(fig, artists)
    out = Path(args.output)
    if not out.is_absolute():
        out = here / out
    if out.suffix.lower() == '.svg':
        fig.savefig(out, format='svg', facecolor='white', metadata={'Date': None})
    else:
        fig.savefig(out, format='png', dpi=100, facecolor='white',
                    metadata={'Software': 'MathPalette staged Author Designed renderer v1'})
    plt.close(fig)
    print(json.dumps({'output': str(out), 'file_sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
                      'content_bbox_px_bottom_origin': list(b.extents), 'fit': args.fit}))


if __name__ == '__main__':
    main()
