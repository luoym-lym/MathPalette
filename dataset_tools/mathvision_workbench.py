"""Read-only MathVision vector capture for the existing Special workbenches.

Frozen question renderers, scenes and protocols are inputs, never rewritten.
Only real emitted outlines become style targets; labels and face fills remain
on the original figure. Workbench schemas and marking presets stay unchanged.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import threading

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import to_rgba
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np

LOCK = threading.RLock()
_RENDERERS = {}
_MISSING = object()
PLANE_OUTLINES = {'segment', 'polyline', 'circle', 'arc', 'angle_arc', 'polygon',
                  'closed_arc_path', 'ellipse', 'open_cubic_path', 'open_arc_path',
                  'sector', 'native_artwork_instance', 'bezier_arrow',
                  'right_angle', 'equal_tick', 'parallel_mark'}
SOLID_OUTLINES = {'segment', 'polyline', 'circular_arc'}


def is_mathvision(record):
    return record.get('source_dataset') == 'MathVision'


def _read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def _contained(root, relative):
    root = Path(root).resolve()
    value = (root / relative).resolve()
    if value == root or not value.is_relative_to(root):
        raise ValueError('MathVision dependency path escapes its frozen branch')
    return value


def _renderer(path):
    key = (str(path), hashlib.sha256(path.read_bytes()).hexdigest())
    module = _RENDERERS.get(key)
    if module is None:
        spec = importlib.util.spec_from_file_location('_mathvision_workbench_' + key[1][:16], path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        _RENDERERS[key] = module
    return module


def _outline(artist):
    alpha = artist.get_alpha()
    if not artist.get_visible() or alpha is not None and not np.any(np.asarray(alpha) > 0):
        return False
    if isinstance(artist, Line2D):
        return (artist.get_visible() and artist.get_linewidth() > 0
                and artist.get_linestyle() not in ('None', 'none', '', ' ')
                and to_rgba(artist.get_color())[3] > 0
                and len(artist.get_path().vertices) > 1)
    if isinstance(artist, LineCollection):
        return (artist.get_visible() and len(artist.get_paths()) > 0
                and any(width > 0 for width in artist.get_linewidths())
                and any(color[3] > 0 for color in artist.get_edgecolors()))
    if isinstance(artist, Patch):
        return (artist.get_visible() and artist.get_linewidth() > 0
                and artist.get_edgecolor()[3] > 0 and len(artist.get_path().vertices) > 1)
    return False


def _visible_artist(artist):
    if _outline(artist):
        return True
    alpha = artist.get_alpha()
    if not artist.get_visible() or alpha is not None and not np.any(np.asarray(alpha) > 0):
        return False
    if isinstance(artist, Patch):
        return artist.get_facecolor()[3] > 0
    if hasattr(artist, 'get_facecolors'):
        colors = artist.get_facecolors()
        return bool(len(colors) and np.any(colors[:, 3] > 0))
    return False


def _snap_points(scene, visible_objects, branch):
    points = scene.get('points', {})
    labels = scene.get('labels', [])
    found = {}
    projection = scene.get('projection', {})

    def locate(value):
        return points[value] if isinstance(value, str) and value in points else value

    def add(value, reason, label=None):
        world = locate(value)
        if not isinstance(world, (list, tuple)) or len(world) not in (2, 3):
            return
        world = np.asarray(world, dtype=float)
        if not np.isfinite(world).all():
            return
        if len(world) == 3:
            matrix = np.asarray(projection.get('matrix'), dtype=float)
            if matrix.shape != (2, 3):
                return
            xy = matrix @ (world - np.asarray(projection.get('origin', [0, 0, 0]), dtype=float))
            xy += np.asarray(projection.get('offset', [0, 0]), dtype=float)
        else:
            xy = world
        coordinates = world.tolist()
        name = value if isinstance(value, str) else 'vertex_' + hashlib.sha256(
            json.dumps(coordinates, separators=(',', ':')).encode('utf-8')).hexdigest()[:16]
        if name in found:
            if reason not in found[name]['reasons']:
                found[name]['reasons'].append(reason)
            if label is not None:
                found[name]['label'] = str(label)
            return
        found[name] = {'id': name, 'label': str(label) if label is not None else name,
                       'xy': xy.tolist(), 'kind': 'original_point', 'source': 'frozen_scene',
                       'reasons': [reason]}
        if len(world) == 3:
            found[name]['world_xyz'] = coordinates

    for obj in visible_objects:
        if obj.get('role') == 'dimension' or obj.get('visibility') == 'occluded':
            continue
        kind = obj['type']
        if kind == 'segment':
            for value in obj.get('points', []):
                add(value, 'visible_edge_endpoint')
        elif kind == 'polyline':
            values = obj.get('points', [])
            # A closed sampled curve has no distinguished endpoint. Its first
            # tessellation sample is not an existing geometric vertex.
            if len(values) > 16 and np.allclose(locate(values[0]), locate(values[-1]), rtol=0, atol=1e-10):
                continue
            if len(values) <= 16:
                for value in values:
                    add(value, 'visible_polyline_vertex')
            else:
                for value in values[:1] + values[-1:]:
                    add(value, 'visible_curve_endpoint')
        elif kind == 'polygon' and len(obj.get('points', [])) <= 16:
            for value in obj['points']:
                add(value, 'visible_vertex')
        elif kind == 'face' and branch == 'SolidGeometry' and len(obj.get('points', [])) <= 16:
            # Dense curved fills contain rendering samples, not snap vertices.
            # Explicitly named points remain available through vertex labels.
            for value in obj.get('points', []):
                add(value, 'visible_face_vertex')
        elif kind == 'point':
            add(obj.get('point', obj.get('anchor')), 'point_symbol')
        elif kind == 'circular_arc':
            for interval in obj.get('intervals', []):
                if interval.get('visibility') == 'occluded':
                    continue
                for key in ('start_point', 'end_point'):
                    if interval.get(key) is not None:
                        add(interval[key], 'visible_curve_endpoint')
    for label in labels:
        if label.get('type') == 'vertex':
            value = label.get('point', label.get('anchor'))
            if value is not None:
                add(value, 'named_point', label.get('text'))
    return list(found.values())


def _native_cube_targets(scene, ax):
    """Bind real cube edges from explicit native extras, never artist order.

    A retained cube-artwork renderer keeps its geometry in ``cubes`` and
    ``visibility.visible_edges`` rather than canonical ``objects``. Match the
    actual projected line to those frozen endpoints and page transforms.
    """
    if scene.get('objects') or not scene.get('cubes'):
        return [], {}, []
    edges = scene.get('visibility', {}).get('visible_edges', [])
    matrix = np.asarray(scene.get('projection', {}).get('matrix'), dtype=float)
    if not edges or matrix.shape != (2, 3):
        return [], {}, []
    objects, artists, snaps = [], {}, {}
    available = [artist for artist in ax.lines if artist.get_gid() is None and _outline(artist)]
    claimed = set()
    for cube_index, cube in enumerate(scene['cubes']):
        cube_id = str(cube.get('id', 'cube_' + str(cube_index)))
        scale = float(cube['page_scale'])
        origin = np.asarray(cube['page_origin'], dtype=float)
        center = np.asarray(cube['world_center'], dtype=float)
        for edge_index, edge in enumerate(edges):
            world = np.asarray(edge, dtype=float)
            xy = scale * ((world - center) @ matrix.T) + origin
            matched = [artist for artist in available if artist not in claimed
                       and artist.get_xydata().shape == xy.shape
                       and np.allclose(artist.get_xydata(), xy, rtol=0, atol=1e-12)]
            if len(matched) != 1:
                raise ValueError('Frozen native cube edge has no unique projected artist')
            artist = matched[0]
            claimed.add(artist)
            identity = f'native_cube_{cube_id}_edge_{edge_index:02d}'
            artists[identity] = [artist]
            objects.append({'id': identity, 'type': 'curve', 'kind': 'segment', 'role': 'edge',
                            'styleable': True,
                            'source_call': {'native_cube_id': cube_id, 'visible_edge_index': edge_index},
                            'geometry': {'world_points': world.tolist(), 'projected_points': xy.tolist()},
                            'frozen_visibility': 'visible', 'artist_count': 1})
            for point, screen in zip(world, xy):
                point_id = f'native_cube_{cube_id}_vertex_' + hashlib.sha256(
                    json.dumps(point.tolist(), separators=(',', ':')).encode('utf-8')).hexdigest()[:16]
                snaps[point_id] = {'id': point_id, 'label': point_id, 'kind': 'original_point',
                                   'source': 'frozen_native_cube', 'xy': screen.tolist(),
                                   'world_xyz': point.tolist(), 'reasons': ['visible_edge_endpoint']}
    return objects, artists, list(snaps.values())


@dataclass
class Capture:
    fig: object
    ax: object
    objects: list
    artists: dict
    snap_points: list
    settings: dict
    native: bool = True

    def close(self):
        plt.close(self.fig)


def build_scene(branch_root, record):
    branch_root = Path(branch_root).resolve()
    if not is_mathvision(record):
        raise ValueError('The MathVision bridge only accepts MathVision records')
    dependencies = record.get('runtime_dependencies', [])
    endings = f'/items/{record["id"]}/execution.json'
    executions = [value for value in dependencies if value.endswith(endings)]
    if len(executions) != 1:
        raise ValueError('MathVision frozen execution mapping is missing or ambiguous')
    item = _contained(branch_root, executions[0]).parent
    helpers = [value for value in dependencies if value.endswith('/protocol_renderer.py')]
    if len(helpers) != 1:
        raise ValueError('MathVision protocol renderer dependency is missing or ambiguous')
    renderer_path = _contained(branch_root, helpers[0])
    helper = renderer_path.parent
    canonical = _read(_contained(branch_root, record['scene']))
    native = _read(item / 'scene.json')
    old_id = native['id']
    native.update(canonical)
    native['id'] = old_id
    config = _read(item / 'execution.json')
    original = _contained(branch_root, record['original_image'])
    branch = branch_root.name
    allowed = SOLID_OUTLINES if branch == 'SolidGeometry' else PLANE_OUTLINES
    temporary_root = branch_root.parent / '.runtime/mathvision_workbench'
    temporary_root.mkdir(parents=True, exist_ok=True)
    fig = None
    with LOCK:
        previous = sys.modules.get('protocol_renderer', _MISSING)
        settings = dict(matplotlib.rcParamsDefault)
        settings['backend'] = 'Agg'
        try:
            with matplotlib.rc_context(settings):
                renderer = _renderer(renderer_path)
                sys.modules['protocol_renderer'] = renderer
                renderer._active(None)
                with tempfile.TemporaryDirectory(prefix=record['id'] + '-', dir=temporary_root) as directory:
                    replay = Path(directory)
                    inputs = set(config['files']) | {'execution.json', 'source_redraw.py', 'protocol_review.json', 'scene.json'}
                    for name in sorted(inputs):
                        destination = _contained(replay, name)
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        source = original if name == config['original_image_name'] else _contained(item, name)
                        shutil.copyfile(source, destination)
                    (replay / 'scene.json').write_text(json.dumps(native, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
                    review = _read(replay / 'protocol_review.json')
                    protocol = renderer.read(renderer.machine_protocol(branch))
                    with renderer.native_environment(replay) as (target, _):
                        fig, checks = renderer.figure(target, native)
                        if any(check.get('passed') is False for check in checks):
                            raise ValueError('Frozen MathVision geometric check failed')
                        renderer.normalize(fig, native, review, protocol)
                actual_settings = dict(matplotlib.rcParams)
                actual_settings['backend'] = 'Agg'
                if len(fig.axes) != 1:
                    raise ValueError('MathVision workbench requires one canonical drawing axes')
                ax = fig.axes[0]
                owned = {obj['id']: [] for obj in native['objects']}
                emitted = {obj['id']: [] for obj in native['objects']}
                for artist in list(ax.lines) + list(ax.patches) + list(ax.collections):
                    identity = artist.get_gid()
                    if identity in owned:
                        if _visible_artist(artist):
                            emitted[identity].append(artist)
                        if _outline(artist):
                            owned[identity].append(artist)
                objects, artists = [], {}
                for obj in native['objects']:
                    oid, kind = obj['id'], obj['type']
                    styleable = kind in allowed and bool(owned[oid]) and obj.get('role') != 'dimension'
                    artists[oid] = owned[oid] if styleable else []
                    objects.append({'id': oid, 'type': 'curve' if styleable else kind, 'kind': kind,
                                    'role': obj.get('role'), 'styleable': styleable,
                                    'source_call': {'scene_object_id': oid, 'native_object_id': oid},
                                    'geometry': copy.deepcopy(obj),
                                    'frozen_visibility': copy.deepcopy(obj.get('intervals', obj.get('visibility'))),
                                    'artist_count': len(artists[oid])})
                visible = [obj for obj in native['objects'] if emitted[obj['id']]]
                cube_objects, cube_artists, cube_snaps = _native_cube_targets(native, ax)
                objects.extend(cube_objects)
                artists.update(cube_artists)
                return Capture(fig, ax, objects, artists,
                               _snap_points(native, visible, branch) + cube_snaps, actual_settings)
        except BaseException:
            if fig is not None:
                plt.close(fig)
            raise
        finally:
            if previous is _MISSING:
                sys.modules.pop('protocol_renderer', None)
            else:
                sys.modules['protocol_renderer'] = previous


def png_bytes(scene):
    stream = io.BytesIO()
    with LOCK, matplotlib.rc_context(scene.settings):
        scene.fig.savefig(stream, format='png', dpi=100, facecolor='#FFFFFF', transparent=False,
                          bbox_inches=None, pad_inches=0,
                          metadata={'Software': 'MathPalette MathVision workbench'})
    return stream.getvalue()
