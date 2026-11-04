"""Capture an immutable author original and apply the existing Special whitelist.

Original rendering runs with its original rc settings. savefig is intercepted in
memory; no original code, geometry, fill or text is rewritten. Every style target
is a real emitted artist belonging to an explicit frozen original object.
"""
from __future__ import annotations
import copy
import importlib.util
import io
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from unittest.mock import patch

PROJECT = next(p for p in Path(__file__).resolve().parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
os.environ.setdefault('MPLCONFIGDIR', str(PROJECT / '.runtime/collect8_expand24_20261103/cache/matplotlib'))
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


@dataclass
class Capture:
    fig: object
    ax: object
    objects: list
    artists: dict
    snap_points: list
    settings: dict
    family: str
    save_kwargs: dict
    native: bool = True

    def close(self):
        plt.close(self.fig)


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def capture(item_directory):
    item = Path(item_directory).resolve()
    identity = json.loads((item / 'identity.json').read_text(encoding='utf-8'))
    original = json.loads((item / 'scene.json').read_text(encoding='utf-8-sig'))
    context = json.loads((item / 'drawing_context.json').read_text(encoding='utf-8-sig'))
    saved = []

    def intercept(fig, filename, *args, **kwargs):
        if args:
            raise ValueError('Unexpected positional savefig arguments')
        saved.append((fig, copy.deepcopy(kwargs), matplotlib.rcParams.copy()))

    before = set(plt.get_fignums())
    try:
        with matplotlib.rc_context(), patch.object(Figure, 'savefig', intercept), \
                patch.object(plt, 'close', lambda *a, **k: None), \
                patch.object(sys, 'argv', ['frozen-render', '--output', str(item / '__memory_capture.png')]):
            module = load_module(item / 'render.py', '_expand24_original_' + identity['id'])
            module.main()
        if len(saved) != 1 or len(saved[0][0].axes) != 1:
            raise ValueError('Expected one frozen figure with one drawing axes')
        fig, kwargs, settings = saved[0]
        ax = fig.axes[0]
        parent = identity['parent_id']
        artists, objects = {}, []

        def own(oid, artist, visibility='visible'):
            if oid in artists:
                raise ValueError('Duplicate stable original ID: ' + oid)
            artists[oid] = [artist]
            objects.append({'id': oid, 'kind': 'outline', 'styleable': True,
                            'source_call': {'frozen_object_id': oid},
                            'frozen_visibility': visibility})

        if parent in ('Plane189', 'Plane200'):
            if len(original['objects']) != len(ax.patches):
                raise ValueError('Frozen patch/object count mismatch')
            eligible_key = next(k for k in ('editable_original_objects', 'original_editable_objects') if k in context)
            eligible = {o['id'] for o in context[eligible_key]}
            for obj, artist in zip(original['objects'], ax.patches):
                if obj['id'] in eligible:
                    own(obj['id'], artist)
        elif parent in ('Plane307', 'Plane348'):
            segments = [o for o in original['objects'] if o['type'] == 'segment']
            if len(segments) != len(ax.lines):
                raise ValueError('Frozen line/object count mismatch')
            for obj, artist in zip(segments, ax.lines):
                own(obj['id'], artist)
        elif parent in ('Plane363', 'Plane385'):
            # Existing dot fills are semantic and remain protected. They are
            # available for exact snapping and may receive separate added marks.
            pass
        elif parent == 'Solid94':
            segments = sorted(original['objects'], key=lambda x: x['visibility'] == 'visible')
            if len(segments) != len(ax.lines):
                raise ValueError('Frozen solid line/object count mismatch')
            for obj, artist in zip(segments, ax.lines):
                own(obj['id'], artist, obj['visibility'])
        elif parent == 'Solid147':
            faces = [f for g in original['groups'] for f in g['faces']]
            if len(faces) != len(ax.patches):
                raise ValueError('Frozen voxel face/patch count mismatch')
            for face, artist in zip(faces, ax.patches):
                # Only actual emitted face outlines, preserving semantic fills
                # and the exact existing painter order/occlusion. Derived edge
                # overlays cannot override a solid line's dash pattern safely.
                own(face['id'], artist, face['visibility'])
        else:
            raise ValueError('Unknown frozen author family')
        snaps = []
        for index, p in enumerate(context.get('snap_points', [])):
            p = copy.deepcopy(p)
            p.setdefault('label', '')
            p['kind'] = 'original_point'
            p.setdefault('source', 'frozen_scene')
            p.setdefault('id', 'snap_' + str(index))
            snaps.append(p)
        return Capture(fig, ax, objects, artists, snaps, settings,
                       'delete_points' if parent in ('Plane363', 'Plane385') else parent, kwargs)
    except BaseException:
        for number in set(plt.get_fignums()) - before:
            plt.close(number)
        raise


def png_bytes(scene):
    kwargs = copy.deepcopy(scene.save_kwargs)
    kwargs.pop('format', None)
    with matplotlib.rc_context(scene.settings):
        output = io.BytesIO()
        scene.fig.savefig(output, format='png', **kwargs)
        return output.getvalue()


def apply(scene, plugin, schema):
    executor = load_module(Path(__file__).with_name('style_executor.py'), '_expand24_style_executor')
    executor.apply(scene, plugin, schema)


def render(item_directory, plugin=None, schema=None):
    scene = capture(item_directory)
    try:
        if plugin is not None:
            identity = json.loads((Path(item_directory) / 'identity.json').read_text(encoding='utf-8'))
            if plugin.get('question_id') != identity['id']:
                raise ValueError('Plugin identity mismatch')
            if schema is None:
                raise ValueError('Exact branch schema is required')
            apply(scene, plugin, schema)
        return png_bytes(scene)
    finally:
        scene.close()
