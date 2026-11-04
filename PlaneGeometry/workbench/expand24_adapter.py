"""Exact-pixel workbench support for the isolated, approved expand24 originals."""
from __future__ import annotations
import importlib.util
import sys
from pathlib import Path
from matplotlib.patches import Patch
from author_adapter import RendererAdapter as PreviousAuthorAdapter
from renderer_adapter import RENDER_LOCK
from workbench_io import WorkbenchError, contained_path, pixel_hash, read_json

PACKAGE = 'dataset_generator/author_expand24_v1'
SUPPORT = tuple('workbench/' + f for f in ('expand24_adapter.py', 'expand24_plugins.py', 'expand24_replay.py', 'review_store.py', 'replay_archived.py'))

def is_expand24_record(record):
    if not isinstance(record, dict) or record.get('source_dataset') != 'Author Designed':
        return False
    qid = record.get('id', '')
    key = record.get('source_key', '')
    if not key.startswith('author-expand24:'):
        return False
    ancestry = key.removeprefix('author-expand24:').split('/')
    parents = ('Plane189', 'Plane200', 'Plane307', 'Plane348', 'Plane363', 'Plane385', 'Solid94', 'Solid147')
    if len(ancestry) != 2 or ancestry[0] not in parents or ancestry[1] not in ('extension_01', 'extension_02', 'extension_03'):
        return False
    expected = {f'{PACKAGE}/' + f for f in ('engine.py', 'style_executor.py', 'author_partial_style.py')}
    expected.update(f'{PACKAGE}/items/{qid}/' + f for f in ('scene.json', 'render.py', 'drawing_context.json', 'identity.json'))
    return set(record.get('runtime_dependencies', [])) == expected

def frozen_engine(branch):
    path = Path(branch) / PACKAGE / 'engine.py'
    name = '_expand24_workbench_' + Path(branch).name
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

class RendererAdapter(PreviousAuthorAdapter):
    def __init__(self, config, expected_manifest=None):
        super().__init__(config)
        for name in SUPPORT:
            self.input_files[name] = self.branch / name
        self.manifest = self.make_manifest()
        if expected_manifest and self.manifest != expected_manifest:
            raise WorkbenchError('Expand24 workbench inputs changed', 409, 'baseline_changed')

    def is_expand24(self, qid):
        return is_expand24_record(self.records.get(qid))

    def is_author(self, qid):
        return self.is_expand24(qid) or super().is_author(qid)

    def author_dependencies(self, qid):
        if not self.is_expand24(qid):
            return super().author_dependencies(qid)
        return (*('author_runtime/' + p for p in self.records[qid]['runtime_dependencies']), *SUPPORT)

    def scene(self, qid):
        if not self.is_expand24(qid):
            return super().scene(qid)
        item = self.branch / PACKAGE / 'items' / qid
        frozen = read_json(item / 'scene.json')
        identity = read_json(item / 'identity.json')
        if frozen.get('id') != qid or identity.get('id') != qid or frozen.get('source_dataset') != 'Author Designed':
            raise WorkbenchError('Frozen original identity changed', 409, 'baseline_changed')
        with RENDER_LOCK:
            return frozen_engine(self.branch).capture(item)

    def inspect_question(self, qid):
        if not self.is_expand24(qid):
            return super().inspect_question(qid)
        from author_board import describe_captured_scene
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                digest = pixel_hash(frozen_engine(self.branch).png_bytes(scene))
                if digest != pixel_hash(self.original_paths[qid]):
                    raise WorkbenchError('Expand24 original pixels differ', 409, 'baseline_mismatch')
                board = describe_captured_scene(scene, qid)
                return {'original_pixel_sha256': digest, 'objects': scene.objects, 'snap_points': scene.snap_points,
                        'canvas': board, 'xlim': board['xlim'], 'ylim': board['ylim']}
            finally:
                scene.close()

    def highlight(self, qid, oid):
        if not self.is_expand24(qid):
            return super().highlight(qid, oid)
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                if oid not in scene.artists:
                    raise WorkbenchError('Unknown original target')
                for artist in scene.artists[oid]:
                    if isinstance(artist, Patch): artist.set_edgecolor('#E11D48')
                    else: artist.set_color('#E11D48')
                scene.fig.text(.02, .98, f'REFERENCE ONLY: {qid} / {oid}', color='#E11D48', fontsize=11, va='top')
                return frozen_engine(self.branch).png_bytes(scene)
            finally:
                scene.close()
