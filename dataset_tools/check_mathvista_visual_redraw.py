"""Compare baseline and revised MathVista renderers without writing formal PNGs.

Run from any directory: python -X utf8 -B dataset_tools/check_mathvista_visual_redraw.py
The baseline commit must be available locally. Outputs stay in .runtime/.
Published-pixel comparisons are reported, not hidden by the before/after check.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
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
from dataset_tools.test_mathvista_visual_dependency import renderer_fingerprint


def pixel_hash(path):
    with Image.open(path) as image:
        return hashlib.sha256(image.convert('RGBA').tobytes()).hexdigest()


def main():
    manifest = catalog.read(ROOT / 'provenance/mathvista_visual_dependency_20261108.json')
    OUTPUT.mkdir(parents=True, exist_ok=True)
    results = []
    for revision in manifest['revisions']:
        qid = revision['id']
        relative = f'Analytics/dataset_generator/questions/function_plot{int(qid[3:])}.py'
        path = ROOT / relative
        baseline = subprocess.check_output(
            ['git', 'show', f"{manifest['base_commit']}:{relative}"],
            cwd=ROOT, text=True, encoding='utf-8')
        current = path.read_text(encoding='utf-8')
        expected = revision['renderer_ast_sha256']
        if renderer_fingerprint(baseline) != expected or renderer_fingerprint(current) != expected:
            raise ValueError(f'{qid}: rendering code changed')
        for preserved, fingerprint in revision['preserved_files'].items():
            if catalog.file_hash(ROOT / preserved) != fingerprint:
                raise ValueError(f'{qid}: frozen asset changed: {preserved}')
        hashes = []
        for label, source in [('before', baseline), ('after', current)]:
            namespace = {'__file__': str(path), '__name__': f'redraw_check_{label}_{qid}'}
            exec(compile(source, str(path), 'exec'), namespace)
            output = OUTPUT / f'{qid}_{label}.png'
            namespace[qid]().draw(output_path=output)
            hashes.append(pixel_hash(output))
        results.append({
            'id': qid,
            'before_after_pixels_equal': hashes[0] == hashes[1],
            'published_pixels_equal': pixel_hash(ROOT / f'Analytics/image/{qid}.png') == hashes[1],
        })
    report = {
        'environment': {'python': platform.python_version(), 'numpy': numpy.__version__,
                        'matplotlib': matplotlib.__version__, 'pillow': PIL.__version__,
                        'freetype': ft2font.__freetype_version__},
        'before_after_equal_count': sum(r['before_after_pixels_equal'] for r in results),
        'published_equal_count': sum(r['published_pixels_equal'] for r in results),
        'results': results,
    }
    (OUTPUT / 'results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in report.items() if key != 'results'}))
    if not all(r['before_after_pixels_equal'] for r in results):
        raise SystemExit('Rendering changed relative to baseline in the same environment')
    if not all(r['published_pixels_equal'] for r in results):
        print('WARNING: regenerated pixels differ from published PNGs. Check the frozen environment; '
              'the formal images were not overwritten.', file=sys.stderr)


if __name__ == '__main__':
    main()
