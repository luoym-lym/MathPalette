"""Exact vector interval styling. Keep this module identical in both geometry workbenches.

An interval addresses a continuous path and a normalized segment parameter, not
screen pixels. Bézier subdivision uses de Casteljau; frozen polylines stay exact.
Only the browser hit-test samples are approximate. MOVETO gaps never get bridged.
"""
from __future__ import annotations

import math
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import to_hex
from matplotlib.path import Path
from matplotlib.patches import Patch, PathPatch

from workbench_io import WorkbenchError, canonical_hash


def split(control, t):
    rows = [np.asarray(control, dtype=float)]
    while len(rows[-1]) > 1:
        rows.append((1 - t) * rows[-1][:-1] + t * rows[-1][1:])
    return np.array([r[0] for r in rows]), np.array([r[-1] for r in rows[::-1]])


def portion(control, start, end):
    left = split(control, end)[0] if end < 1 else np.asarray(control)
    return split(left, start / end)[1] if start > 0 else left


def evaluate(control, t):
    return split(control, t)[0][-1]


def _subpaths(path):
    pieces, current, first = [], None, None
    for vertices, code in path.iter_segments(remove_nans=True, simplify=False, curves=True):
        points = np.asarray(vertices).reshape(-1, 2)
        if code == Path.MOVETO:
            if pieces:
                yield pieces
            pieces, current, first = [], points[0], points[0]
        elif code in (Path.LINETO, Path.CURVE3, Path.CURVE4):
            if current is not None:
                pieces.append(np.vstack([current, points]))
                current = points[-1]
        elif code == Path.CLOSEPOLY and current is not None:
            if not np.array_equal(current, first):
                pieces.append(np.array([current, first]))
            if pieces:
                yield pieces
            pieces, current, first = [], None, None
    if pieces:
        yield pieces


def _style(artist, index):
    if isinstance(artist, LineCollection):
        color = artist.get_colors()[index % len(artist.get_colors())]
        width = artist.get_linewidths()[index % len(artist.get_linewidths())]
        dash = artist.get_linestyles()[index % len(artist.get_linestyles())]
    else:
        color = artist.get_edgecolor() if isinstance(artist, Patch) else artist.get_color()
        width = artist.get_linewidth()
        dash = getattr(artist, '_dash_pattern', (0, None))
    def line_property(name, fallback):
        getter = getattr(artist, 'get_' + name, None)
        return (getter() if getter else None) or fallback
    cap = line_property('capstyle', 'butt')
    join = line_property('joinstyle', 'round')
    return {'color': to_hex(color, keep_alpha=True), 'linewidth_pt': float(width),
            'dash': (float(dash[0]), tuple(dash[1]) if dash[1] is not None else None),
            'solid_cap': line_property('solid_capstyle', cap), 'dash_cap': line_property('dash_capstyle', cap),
            'solid_join': line_property('solid_joinstyle', join), 'dash_join': line_property('dash_joinstyle', join)}


def object_paths(scene, target):
    paths = []
    inverse = scene.ax.transData.inverted()
    for artist in scene.artists[target]:
        source = artist.get_paths() if isinstance(artist, LineCollection) else [artist.get_path()]
        for index, path in enumerate(source):
            data_path = path.transformed(artist.get_transform() + inverse)
            for controls in _subpaths(data_path):
                segments = [{'control': c, 'artist': artist, 'style': _style(artist, index)} for c in controls]
                # Consecutive visibility fragments of the same solid curve share
                # an endpoint. Separate subpaths within one artist stay separate.
                if (paths and paths[-1][-1]['artist'] is not artist and
                        np.allclose(paths[-1][-1]['control'][-1], controls[0][0], rtol=0, atol=1e-10)):
                    paths[-1].extend(segments)
                else:
                    paths.append(segments)
    result = []
    for i, segments in enumerate(paths):
        controls = [s['control'].tolist() for s in segments]
        result.append({'id': f'p{i}', 'segments': segments,
                       'sha256': canonical_hash(controls),
                       'closed': bool(np.allclose(controls[0][0], controls[-1][-1], rtol=0, atol=1e-10))})
    return result


def describe_paths(scene, target):
    """Pixel samples carry exact source parameters for selection and dragging."""
    height = scene.fig.canvas.get_width_height()[1]
    result = []
    for path in object_paths(scene, target):
        samples, count = [], len(path['segments'])
        for i, segment in enumerate(path['segments']):
            control = scene.ax.transData.transform(segment['control'])
            # Dense cubic hit-testing, independent of eventual output subdivision.
            steps = 1 if len(control) == 2 else max(16, min(512, math.ceil(
                np.linalg.norm(np.diff(control, axis=0), axis=1).sum() / 2)))
            for j in range(steps + 1):
                if i and j == 0:
                    continue
                point = evaluate(control, j / steps)
                samples.append([float(point[0]), float(height - point[1]), (i + j / steps) / count])
        result.append({k: path[k] for k in ('id', 'sha256', 'closed')} | {'samples': samples})
    return result


def validate_interval(interval, paths):
    path = next((p for p in paths if p['id'] == interval['path_id']), None)
    if not path or path['sha256'] != interval['path_sha256']:
        raise WorkbenchError('局部区间路径已改变，请重新选择原对象。', 409, 'object_changed')
    if not 0 <= interval['start'] < interval['end'] <= 1:
        raise WorkbenchError('局部区间须满足 0 ≤ start < end ≤ 1。')
    if interval['wrap'] and (not path['closed'] or interval['end'] - interval['start'] == 1):
        raise WorkbenchError('只有闭合曲线的非空区间可选择另一段。')
    return path


def _covered(interval, path, u):
    if interval is None:
        return True
    if interval['path_id'] != path['id']:
        return False
    inside = interval['start'] < u < interval['end']
    return not inside if interval['wrap'] else inside


def _vector_path(controls):
    vertices, codes = [controls[0][0]], [Path.MOVETO]
    for control in controls:
        vertices.extend(control[1:])
        codes.extend([{2: Path.LINETO, 3: Path.CURVE3, 4: Path.CURVE4}[len(control)]] * (len(control) - 1))
    return Path(vertices, codes)


def _length_pt(scene, control):
    pixel = scene.ax.transData.transform(control)
    samples = np.array([evaluate(pixel, t) for t in np.linspace(0, 1, 33)]) if len(control) > 2 else pixel
    return float(np.linalg.norm(np.diff(samples, axis=0), axis=1).sum() * 72 / scene.fig.dpi)


def apply_partial_styles(scene, actions):
    """Replace affected outlines in place; keep fills, labels and draw order.

Whole-only targets continue through the original renderer, preserving its bytes.
Overlapping actions compose in order, per property. Color never changes dashes.
"""
    targets = {a['target'] for a in actions if a['type'] == 'set_object_style' and 'interval' in a}
    for target in targets:
        changes = [a for a in actions if a['type'] == 'set_object_style' and a['target'] == target]
        paths = object_paths(scene, target)
        for action in changes:
            if 'interval' in action:
                validate_interval(action['interval'], paths)
        replacements = {artist: [] for artist in scene.artists[target]}
        changed_artists = set()
        for path in paths:
            count, runs, travelled = len(path['segments']), [], {}
            for i, segment in enumerate(path['segments']):
                artist, control = segment['artist'], segment['control']
                offset = travelled.get(artist, 0)
                cuts = {0.0, 1.0}
                for action in changes:
                    interval = action.get('interval')
                    if interval and interval['path_id'] == path['id']:
                        cuts.update(u * count - i for u in (interval['start'], interval['end']) if i < u * count < i + 1)
                cuts = sorted(cuts)
                for low, high in zip(cuts, cuts[1:]):
                    style = dict(segment['style'])
                    for action in changes:
                        if _covered(action.get('interval'), path, (i + (low + high) / 2) / count):
                            for key in ('color', 'linewidth_pt'):
                                if key in action:
                                    style[key] = to_hex(action[key], keep_alpha=True) if key == 'color' else action[key]
                            if 'linestyle' in action:
                                style['dash'] = (0, (3.7, 1.6) if action['linestyle'] == 'dashed' else None)
                    if style != segment['style']:
                        changed_artists.add(artist)
                    part = portion(control, low, high)
                    if runs and runs[-1]['artist'] is artist and runs[-1]['style'] == style:
                        runs[-1]['controls'].append(part)
                    else:
                        runs.append({'artist': artist, 'style': style, 'controls': [part],
                                     'offset': offset + (_length_pt(scene, portion(control, 0, low)) if low else 0)})
                travelled[artist] = offset + _length_pt(scene, control)
            for run in runs:
                artist, style = run['artist'], run['style']
                offset, dash = style['dash']
                patch = PathPatch(_vector_path(run['controls']), fill=False, transform=scene.ax.transData,
                                  edgecolor=style['color'], linewidth=style['linewidth_pt'],
                                  capstyle=style['dash_cap' if dash else 'solid_cap'],
                                  joinstyle=style['dash_join' if dash else 'solid_join'], zorder=artist.get_zorder(),
                                  alpha=artist.get_alpha(), clip_on=artist.get_clip_on(),
                                  antialiased=True)
                # Dashes in points retain their phase across a color-only split.
                import matplotlib as mpl
                with mpl.rc_context({'lines.scale_dashes': False}):
                    patch.set_linestyle((offset + run['offset'], dash) if dash else 'solid')
                patch.set_clip_box(artist.get_clip_box())
                patch.set_clip_path(artist.get_clip_path())
                replacements[artist].append(patch)
        for artist, patches in replacements.items():
            if artist not in changed_artists:
                replacements[artist] = [artist]
                continue
            position = scene.ax._children.index(artist)
            if isinstance(artist, Patch) and artist.get_fill():
                artist.set_edgecolor('none')
                position += 1
            else:
                artist.remove()
            for patch in patches:
                scene.ax.add_patch(patch)
                scene.ax._children.remove(patch)
            scene.ax._children[position:position] = patches
        scene.artists[target] = [patch for patches in replacements.values() for patch in patches]
    return targets
