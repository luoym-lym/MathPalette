"""Workbench bridge for the approved extensions95 native vector renderers.

Keep canonical scenes and content-addressed renderers read-only. Only contours
explicitly listed in each frozen authoring context become editable targets.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import io
import re
import sys
from functools import lru_cache
from fractions import Fraction
from pathlib import Path

import matplotlib
from matplotlib.patches import Patch
from expand24_adapter import RendererAdapter as PreviousAdapter, frozen_engine
from renderer_adapter import RENDER_LOCK
from workbench_io import WorkbenchError, contained_path, pixel_hash, read_json

PACKAGE = 'dataset_generator/author_extensions95_v1'
SUPPORT = tuple('workbench/' + name for name in (
    'extensions95_adapter.py', 'extensions95_plugins.py', 'extensions95_replay.py',
    'author_board.py', 'review_store.py', 'replay_archived.py'))
STYLE_SUPPORT = tuple('dataset_generator/author_expand24_v1/' + name for name in (
    'engine.py', 'style_executor.py', 'author_partial_style.py'))
TARGET_KEYS = ('modifiable_objects', 'editable_outlines', 'editable_original_contours',
               'editable_contours', 'original_editable_outlines',
               'modifiable_original_objects', 'editable_objects', 'original_outline_objects')


def is_extensions95_record(record):
    if not isinstance(record, dict) or record.get('source_dataset') != 'Author Designed':
        return False
    key = record.get('source_key', '')
    if not key.startswith('author-extensions95-v1:'):
        return False
    parts = key.removeprefix('author-extensions95-v1:').split('/')
    if len(parts) != 2 or parts[1] not in {f'extension_{i:02}' for i in range(1, 6)}:
        return False
    qid = record['id']
    expected = {f'{PACKAGE}/engine.py', f'{PACKAGE}/items/{qid}/identity.json',
                f'{PACKAGE}/items/{qid}/drawing_context.json'}
    deps = record.get('runtime_dependencies', [])
    native = [p for p in deps if p.startswith(f'{PACKAGE}/renderers/') and p.endswith('.py')]
    return len(native) == 1 and len(deps) == 4 and set(deps) == expected | set(native)


@lru_cache(maxsize=None)
def native_engine(branch):
    name = '_extensions95_workbench_' + Path(branch).name
    spec = importlib.util.spec_from_file_location(name, Path(branch) / PACKAGE / 'engine.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def png_bytes(scene):
    kwargs = copy.deepcopy(scene.save_kwargs)
    kwargs['format'] = 'png'
    with matplotlib.rc_context(scene.settings):
        output = io.BytesIO()
        scene.fig.savefig(output, **kwargs)
    return output.getvalue()


def snap_points(context, targets, frozen):
    values = context.get('exact_snap_points', context.get('snap_points', []))
    if isinstance(values, dict):
        values = [{'id': key, 'xy': value} for key, value in values.items()]
    values = copy.deepcopy(values)
    # Curved pieces store their actual knots locally; translate exactly as the
    # native renderer does. Control handles and inferred intersections stay out.
    for target in targets:
        translation = frozen[target.get('id', target.get('object_id'))].get('display_translation', [0, 0])
        for point in target.get('snap_points', []):
            xy = point['position']
            values.append({**point, 'xy': [xy[i] + translation[i] for i in range(2)]})
    result = []
    for index, value in enumerate(values):
        xy = next((value[k] for k in ('xy', 'page_xy', 'projected_xy', 'point_2d',
                                     'screen_position', 'position', 'point') if k in value), None)
        if xy is None or len(xy) != 2:
            raise WorkbenchError('Invalid frozen extensions95 snap point', 409, 'object_changed')
        result.append({**value, 'id': value.get('id', f'extension_snap_{index}'),
                       'label': value.get('label', ''), 'xy': [float(Fraction(v)) for v in xy],
                       'kind': 'original_point', 'source': 'frozen_scene'})
    return result


class RendererAdapter(PreviousAdapter):
    def __init__(self, config, expected_manifest=None):
        super().__init__(config)
        if any(self.is_extensions95(qid) for qid in self.records):
            for name in (*SUPPORT, *STYLE_SUPPORT):
                self.input_files[name] = contained_path(self.branch, name)
        self.manifest = self.make_manifest()
        if expected_manifest and self.manifest != expected_manifest:
            raise WorkbenchError('Extensions95 inputs changed', 409, 'baseline_changed')

    def is_extensions95(self, qid):
        return is_extensions95_record(self.records.get(qid))

    def is_author(self, qid):
        return self.is_extensions95(qid) or super().is_author(qid)

    def author_dependencies(self, qid):
        if not self.is_extensions95(qid):
            return super().author_dependencies(qid)
        return (*('author_runtime/' + p for p in self.records[qid]['runtime_dependencies']),
                *SUPPORT, *STYLE_SUPPORT)

    def scene(self, qid):
        if not self.is_extensions95(qid):
            return super().scene(qid)
        item = self.branch / PACKAGE / 'items' / qid
        identity = read_json(item / 'identity.json')
        record = self.records[qid]
        if (identity['id'] != qid or identity['scene'] != record['scene'] or
                identity['native_renderer'] != next(p.removeprefix(PACKAGE + '/')
                    for p in record['runtime_dependencies'] if '/renderers/' in p)):
            raise WorkbenchError('Extensions95 identity mismatch', 409, 'baseline_changed')
        context = read_json(item / 'drawing_context.json')
        targets = next((context[k] for k in TARGET_KEYS if k in context), None)
        if targets is None:
            raise WorkbenchError('Missing frozen editable contours', 409, 'object_changed')
        with RENDER_LOCK:
            captured = native_engine(self.branch).capture(item)
            try:
                frozen = {obj['id']: obj for obj in captured.original_scene['objects']}
                artists, objects = {}, []
                for target in targets:
                    oid = target.get('id', target.get('object_id'))
                    # Native IDs may contain dots or exceed the established
                    # plugin ID limit. Bind a deterministic workbench alias;
                    # never alter the frozen ID or relax the shared schema.
                    target_id = oid if re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]{0,63}', oid or '') else (
                        'native_' + hashlib.sha256(oid.encode('utf-8')).hexdigest()[:48])
                    if target_id in artists or oid not in captured.artists or oid not in frozen:
                        raise WorkbenchError('Unmapped frozen original contour: ' + str(oid), 409, 'object_changed')
                    actual = captured.artists[oid]
                    if any(isinstance(a, Patch) and a.get_edgecolor()[3] == 0 for a in actual):
                        raise WorkbenchError('Semantic fill cannot be a contour target', 409, 'object_changed')
                    artists[target_id] = actual
                    objects.append({'id': target_id, 'kind': 'outline', 'type': 'curve', 'styleable': True,
                                    'source_call': {'frozen_object_id': oid},
                                    'frozen_visibility': frozen[oid].get('visibility', 'visible')})
                captured.objects, captured.artists = objects, artists
                captured.snap_points = snap_points(context, targets, frozen)
                captured.family, captured.native = 'extensions95', True
                return captured
            except BaseException:
                captured.close()
                raise

    def inspect_question(self, qid):
        if not self.is_extensions95(qid):
            return super().inspect_question(qid)
        from author_board import describe_captured_scene
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                digest = pixel_hash(png_bytes(scene))
                if digest != pixel_hash(self.original_paths[qid]):
                    raise WorkbenchError(f'{qid} native original pixels differ', 409, 'baseline_mismatch')
                board = describe_captured_scene(scene, qid)
                return {'original_pixel_sha256': digest, 'objects': scene.objects,
                        'snap_points': scene.snap_points, 'canvas': board,
                        'xlim': board['xlim'], 'ylim': board['ylim']}
            finally:
                scene.close()

    def highlight(self, qid, oid):
        if not self.is_extensions95(qid):
            return super().highlight(qid, oid)
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                if oid not in scene.artists:
                    raise WorkbenchError('Unknown original target')
                for artist in scene.artists[oid]:
                    if isinstance(artist, Patch):
                        artist.set_edgecolor('#E11D48')
                    else:
                        artist.set_color('#E11D48')
                return png_bytes(scene)
            finally:
                scene.close()
