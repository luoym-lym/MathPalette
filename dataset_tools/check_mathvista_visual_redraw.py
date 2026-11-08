"""Compare baseline and revised MathVista renderers without writing formal PNGs.

Run from any directory: python -X utf8 -B dataset_tools/check_mathvista_visual_redraw.py
The baseline commit must be available locally. Outputs stay in .runtime/.
Published-pixel comparisons are reported, not hidden by the before/after check.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '.runtime/visual_redraw_comparison'
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / '.runtime/mplconfig'))
os.environ.setdefault('XDG_CACHE_HOME', str(ROOT / '.runtime/cache'))
sys.path.insert(0, str(ROOT))

import matplotlib
from matplotlib import ft2font
import numpy
import PIL
from PIL import Image
from dataset_tools import catalog
from dataset_tools.visual_revision_integrity import assert_same_renderer, baseline_bytes, baseline_source


def pixel_hash(path):
    with Image.open(path) as image:
        return hashlib.sha256(image.convert('RGBA').tobytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-published-pixels', action='store_true',
                        help='Fail unless every regenerated PNG matches the published pixels; use in the formal environment.')
    args = parser.parse_args()
    manifest = catalog.read(ROOT / 'provenance/mathvista_visual_dependency_20261108.json')
    OUTPUT.mkdir(parents=True, exist_ok=True)
    results = []
    for revision in manifest['revisions']:
        qid = revision['id']
        relative = f'Analytics/dataset_generator/questions/function_plot{int(qid[3:])}.py'
        path = ROOT / relative
        baseline = baseline_source(ROOT, manifest['base_commit'], relative)
        current = path.read_text(encoding='utf-8')
        assert_same_renderer(baseline, current, qid)
        for preserved, fingerprint in revision['preserved_files'].items():
            if catalog.file_hash(ROOT / preserved) != fingerprint:
                raise ValueError(f'{qid}: frozen asset changed: {preserved}')
        for relative_asset, change in revision.get('revised_files', {}).items():
            if catalog.file_hash(ROOT / relative_asset) != change['current_sha256']:
                raise ValueError(f'{qid}: revised asset hash changed: {relative_asset}')
        hashes = []
        for label, source in [('before', baseline), ('after', current)]:
            namespace = {'__file__': str(path), '__name__': f'redraw_check_{label}_{qid}'}
            exec(compile(source, str(path), 'exec'), namespace)
            if label == 'before' and revision.get('render_change_expected'):
                scene_relative = f'Analytics/dataset_generator/scenes/{qid}.json'
                frozen_scene = OUTPUT / f'{qid}_baseline_scene.json'
                frozen_scene.write_bytes(baseline_bytes(ROOT, manifest['base_commit'], scene_relative))
                namespace['_SCENE_PATH'] = frozen_scene
            output = OUTPUT / f'{qid}_{label}.png'
            namespace[qid]().draw(output_path=output)
            hashes.append(pixel_hash(output))
        results.append({
            'id': qid,
            'before_after_pixels_equal': hashes[0] == hashes[1],
            'render_change_expected': bool(revision.get('render_change_expected')),
            'published_pixels_equal': pixel_hash(ROOT / f'Analytics/image/{qid}.png') == hashes[1],
        })
    report = {
        'environment': {'python': platform.python_version(), 'numpy': numpy.__version__,
                        'matplotlib': matplotlib.__version__, 'pillow': PIL.__version__,
                        'freetype': ft2font.__freetype_version__},
        'before_after_equal_count': sum(r['before_after_pixels_equal'] for r in results),
        'published_equal_count': sum(r['published_pixels_equal'] for r in results),
        'declared_visual_change_count': sum(r['render_change_expected'] for r in results),
        'expected_change_pattern_matches': all(
            r['before_after_pixels_equal'] != r['render_change_expected'] for r in results),
        'results': results,
    }
    (OUTPUT / 'results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in report.items() if key != 'results'}))
    if not report['expected_change_pattern_matches']:
        raise SystemExit('Rendering changes do not match the declared visual revisions')
    if not all(r['published_pixels_equal'] for r in results):
        if args.require_published_pixels:
            raise SystemExit('Regenerated pixels differ from published PNGs')
        print('WARNING: regenerated pixels differ from published PNGs. Check the frozen environment; '
              'the formal images were not overwritten.', file=sys.stderr)


if __name__ == '__main__':
    main()
