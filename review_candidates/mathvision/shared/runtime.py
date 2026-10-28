"""Replay frozen MathVision geometry only in an isolated temporary layout.

Reviewed items use the protocol renderer and explicit semantic decisions. Legacy
items use their retained native entrypoints. Neither path constructs a redraw
from a reference PNG or writes into candidate or formal-data input directories.
"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile


def _contained(root, value):
    target = (root / value).resolve()
    if not target.is_relative_to(root.resolve()) or target == root.resolve():
        raise ValueError('Invalid frozen execution path')
    return target


def draw(item, shared, output_path, *, formal_scene=None, original_image=None):
    item, shared, output = Path(item).resolve(), Path(shared).resolve(), Path(output_path).resolve()
    if output.suffix.lower() not in ('.png', '.svg'):
        raise ValueError('Choose a PNG or SVG output path')
    if output.is_relative_to(item) or output.is_relative_to(shared):
        raise ValueError('Redraw output must not overwrite frozen input files')
    if (item / 'protocol_review.json').is_file():
        # The reviewed protocol pipeline is the normal replay path. Frozen
        # historical entrypoints remain available only for historical items.
        renderer_path = Path(__file__).with_name('protocol_renderer.py')
        with tempfile.TemporaryDirectory(prefix='mathvision-strict-replay-') as td:
            replay = Path(td) / 'item'
            replay.mkdir()
            execution = json.loads((item / 'execution.json').read_text(encoding='utf-8'))
            inputs = set(execution['files']) | {'scene.json', 'source_redraw.py', 'execution.json', 'protocol_review.json'}
            # Replay only frozen inputs. Reference PNG/SVG and verification
            # reports are never present in the execution item.
            for name in sorted(inputs):
                destination = _contained(replay, name)
                destination.parent.mkdir(parents=True, exist_ok=True)
                if original_image is not None and name == execution['original_image_name']:
                    shutil.copyfile(original_image, destination)
                else:
                    shutil.copyfile(_contained(item, name), destination)
            if formal_scene is not None:
                candidate = json.loads((replay / 'scene.json').read_text(encoding='utf-8'))
                supplied = json.loads(Path(formal_scene).read_text(encoding='utf-8'))
                # Identity is the actual review candidate, independent of output
                # destination; no formal ID is forged to satisfy native checks.
                supplied['id'] = candidate['id']
                candidate.update(supplied)
                supplied = candidate
                (replay / 'scene.json').write_text(json.dumps(supplied, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            rendered = Path(td) / 'output'
            environment = os.environ.copy()
            environment.update(PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg',
                               MPLCONFIGDIR=str(Path(td) / 'matplotlib'))
            result = subprocess.run([sys.executable, '-B', str(renderer_path), str(replay),
                                     '--output-dir', str(rendered)], env=environment,
                                    capture_output=True, text=True, encoding='utf-8',
                                    errors='replace', timeout=120)
            if result.returncode:
                raise RuntimeError('Strict MathVision redraw failed: ' + result.stderr[-4000:])
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(rendered / ('image' + output.suffix.lower()), output)
        return str(output)
    config = json.loads((item / 'execution.json').read_text(encoding='utf-8'))
    category, source_id = config['source_category'], config['source_id']
    if category not in ('solid_geometry', 'combinatorial_geometry', 'transformation_geometry') or not str(source_id).isdigit():
        raise ValueError('Invalid frozen source identity')
    with tempfile.TemporaryDirectory(prefix='mathvision-redraw-') as temporary:
        temporary = Path(temporary)
        root = temporary / 'MathPalette'
        shutil.copytree(shared / 'geometry', root)
        staging = root / '.runtime/mathvision_redraw_720'
        shutil.copytree(shared / 'helpers', staging, dirs_exist_ok=True)
        native = staging / category / str(source_id)
        native.mkdir(parents=True, exist_ok=True)
        for relative in config['files']:
            destination = _contained(native, relative)
            destination.parent.mkdir(parents=True, exist_ok=True)
            source = Path(original_image) if original_image and relative == config['original_image_name'] else _contained(item, relative)
            shutil.copyfile(source, destination)
        if formal_scene is not None:
            # Preserve renderer-required extras, replacing the canonical drawing
            # fields with the reviewed formal scene. Historical identity fields
            # affect report paths, not geometry, and retain their original values.
            native_scene = json.loads((native / 'scene.json').read_text(encoding='utf-8'))
            native_scene.update(json.loads(Path(formal_scene).read_text(encoding='utf-8')))
            native_scene.update(config['native_scene_metadata'])
            (native / 'scene.json').write_text(json.dumps(native_scene, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        shutil.copyfile(item / 'source_redraw.py', native / 'render.py')
        environment = os.environ.copy()
        environment.update(PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg', MPLCONFIGDIR=str(temporary / 'matplotlib'))
        result = subprocess.run([sys.executable, '-B', str(native / 'render.py')], cwd=root,
                                env=environment, capture_output=True, text=True,
                                encoding='utf-8', errors='replace', timeout=50)
        generated = native / ('image' + output.suffix.lower())
        if result.returncode or not generated.is_file():
            raise RuntimeError('Frozen MathVision redraw failed: ' + result.stderr[-3000:] +
                               ('; this native renderer may not export SVG' if not generated.exists() else ''))
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(generated, output)
    return str(output)
