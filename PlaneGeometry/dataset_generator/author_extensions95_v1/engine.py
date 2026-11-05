"""Reproduce approved Author Designed originals from frozen native vector code.

The canonical scene is the sole frozen geometry input. Family-specific payload
fields are stored inside one named constraint and expanded in a temporary runtime
directory. A real emitted Matplotlib figure is captured before any authoring
reports or duplicate outputs are written. Formal source directories stay read-only.
"""
from __future__ import annotations
from contextlib import redirect_stdout, redirect_stderr
from dataclasses import dataclass
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import runpy
import shutil
import sys
import tempfile
import threading
from unittest.mock import patch

PAYLOAD_TYPE = 'author_extensions95_native_payload'
PROJECT = next(p for p in Path(__file__).resolve().parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
_LOCK = threading.RLock()


class _FigureReady(BaseException):
    pass


@dataclass
class Capture:
    fig: object
    ax: object
    settings: object
    save_kwargs: dict
    artists: dict
    original_scene: dict

    def close(self):
        from matplotlib import pyplot as plt
        plt.close(self.fig)


def _inputs(item):
    item = Path(item).resolve()
    identity = json.loads((item / 'identity.json').read_text(encoding='utf-8'))
    package = item.parent.parent
    branch = package.parent.parent
    canonical = json.loads((branch / identity['scene']).read_text(encoding='utf-8'))
    if canonical['id'] != identity['id'] or canonical['source_dataset'] != 'Author Designed':
        raise ValueError('Frozen identity mismatch')
    scene = copy.deepcopy(canonical)
    payloads = [c for c in scene['constraints'] if c.get('type') == PAYLOAD_TYPE]
    if len(payloads) > 1:
        raise ValueError('Duplicate native payload')
    if payloads:
        scene['constraints'] = [c for c in scene['constraints'] if c.get('type') != PAYLOAD_TYPE]
        payload = payloads[0]['data']
        if set(payload) & set(scene):
            raise ValueError('Native payload collides with a canonical scene field')
        scene.update(payload)
    renderer = (package / identity['native_renderer']).resolve()
    if not renderer.is_relative_to(package / 'renderers'):
        raise ValueError('Invalid native renderer path')
    if hashlib.sha256(renderer.read_bytes()).hexdigest() != identity['native_renderer_sha256']:
        raise ValueError('Native renderer fingerprint mismatch')
    return identity, renderer, scene


def capture(item_directory, *, vector=False):
    with _LOCK:
        identity, renderer, scene = _inputs(item_directory)
        runtime = PROJECT / '.runtime' / 'author_extensions95_native'
        runtime.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=identity['id'] + '_', dir=runtime) as temporary:
            temp = Path(temporary).resolve()
            if not temp.is_relative_to(runtime.resolve()):
                raise ValueError('Runtime directory escaped the workspace')
            shutil.copyfile(renderer, temp / 'render.py')
            (temp / 'scene.json').write_text(json.dumps(scene, ensure_ascii=False), encoding='utf-8')
            mpl = temp / '_cache' / 'matplotlib'
            mpl.mkdir(parents=True)
            env = {'MPLCONFIGDIR': str(mpl), 'TEMP': str(temp), 'TMP': str(temp),
                   'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONUTF8': '1'}
            saved = []
            with patch.dict(os.environ, env):
                import matplotlib
                matplotlib.use('Agg')
                from matplotlib import pyplot as plt
                from matplotlib.figure import Figure

                def intercept(fig, filename, *args, **kwargs):
                    if args:
                        raise ValueError('Unexpected positional savefig options')
                    saved.append((fig, copy.deepcopy(kwargs), matplotlib.rcParams.copy()))
                    raise _FigureReady()

                output = temp / ('capture.svg' if vector else 'capture.png')
                with matplotlib.rc_context(), patch.object(Figure, 'savefig', intercept), \
                        patch.object(plt, 'close', lambda *args, **kwargs: None), \
                        patch.object(sys, 'argv', [str(temp / 'render.py'), '--output', str(output)]), \
                        redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    try:
                        runpy.run_path(str(temp / 'render.py'), run_name='__main__')
                    except _FigureReady:
                        pass
                if len(saved) != 1 or len(saved[0][0].axes) != 1:
                    raise ValueError('Expected exactly one native figure and one drawing axes')
                fig, kwargs, settings = saved[0]
                artists = {}
                for artist in fig.findobj():
                    gid = artist.get_gid()
                    if gid:
                        artists.setdefault(gid, []).append(artist)
                return Capture(fig, fig.axes[0], settings, kwargs, artists, scene)


def render(item_directory, *, vector=False):
    with _LOCK:
        captured = capture(item_directory, vector=vector)
        try:
            import matplotlib
            output = io.BytesIO()
            kwargs = copy.deepcopy(captured.save_kwargs)
            kwargs['format'] = 'svg' if vector else 'png'
            if vector:
                metadata = dict(kwargs.get('metadata') or {})
                software = metadata.pop('Software', None)
                if software and 'Creator' not in metadata:
                    metadata['Creator'] = software
                metadata.setdefault('Date', None)
                kwargs['metadata'] = metadata
            with matplotlib.rc_context(captured.settings):
                captured.fig.savefig(output, **kwargs)
            data = output.getvalue()
            if not vector:
                from PIL import Image
                rgba = Image.open(io.BytesIO(data)).convert('RGBA')
                identity, _, _ = _inputs(item_directory)
                if rgba.size != (768, 768) or rgba.getchannel('A').getextrema() != (255, 255):
                    raise ValueError('Unexpected original image size or transparency')
                if hashlib.sha256(rgba.tobytes()).hexdigest() != identity['approved_rgba_sha256']:
                    raise ValueError('Native redraw differs from the user-approved original pixels')
            return data
        finally:
            captured.close()
