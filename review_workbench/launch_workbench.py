"""Standard-library-only launcher. It selects, but never installs, an environment."""
from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {'python': '3.13.9', 'numpy': '2.5.3', 'matplotlib': '3.11.2', 'pillow': '12.3.0', 'freetype': '2.14.3'}
MATHVISION_REQUIRED = {'python': '3.12', 'numpy': '2.3.5', 'matplotlib': '3.10.8', 'pillow': '12.3.0', 'freetype': '2.6.1'}

def matching_sources(found):
    matched = []
    if found == REQUIRED:
        matched.append('MathVerse')
    if str(found.get('python', '')).startswith('3.12.') and all(found.get(key) == value for key, value in MATHVISION_REQUIRED.items() if key != 'python'):
        matched.append('MathVision')
    return matched
PROBE = '''
import json, platform
from importlib.metadata import version
from matplotlib.ft2font import __freetype_version__
print(json.dumps(dict(python=platform.python_version(), numpy=version("numpy"), matplotlib=version("matplotlib"), pillow=version("pillow"), freetype=__freetype_version__)))
'''


def candidates():
    override = os.environ.get('MATHPALETTE_PYTHON')
    if override:
        return [Path(override).expanduser()]
    paths = [Path(sys.executable)]
    paths.extend(Path(os.environ[key]).expanduser() for key in ('MATHPALETTE_MATHVISION_PYTHON', 'MATHPALETTE_MATHVERSE_PYTHON') if os.environ.get(key))
    prefixes = [ROOT / name for name in ('.venv', 'venv', '.venv-mathvision', '.venv-mathverse')]
    if os.environ.get('CONDA_PREFIX'):
        prefixes.append(Path(os.environ['CONDA_PREFIX']))
    conda = Path.home() / '.conda/environments.txt'
    if conda.is_file():
        prefixes.extend(Path(line.strip()) for line in conda.read_text(encoding='utf-8-sig').splitlines() if line.strip())
    for prefix in prefixes:
        paths.extend(prefix / name for name in ('Scripts/python.exe', 'python.exe', 'bin/python'))
    for directory in os.get_exec_path():
        paths.extend(Path(directory) / name for name in ('python.exe', 'python3', 'python'))
    return list(dict.fromkeys(path.resolve() for path in paths if path.is_file()))


def select_python():
    checked = []
    for path in candidates():
        try:
            result = subprocess.run([str(path), '-X', 'utf8', '-B', '-c', PROBE], capture_output=True,
                                    text=True, encoding='utf-8', errors='replace', timeout=15)
            found = json.loads(result.stdout) if result.returncode == 0 else {}
        except (OSError, ValueError, subprocess.TimeoutExpired):
            found = {}
        checked.append(f'{path}: {json.dumps(found, ensure_ascii=False)}')
        if matching_sources(found):
            return path, found
    raise ValueError('没有找到匹配的重绘环境。\n需要：' + json.dumps({'MathVerse': REQUIRED, 'MathVision': MATHVISION_REQUIRED}) +
                     '\n已检查：\n' + '\n'.join(checked) +
                     '\n请按 review_workbench/README.md 准备环境，或设置 MATHPALETTE_PYTHON 为匹配的 python.exe 路径。\n未修改候选、正式题库或批准记录。')


def main():
    python, found = select_python()
    print('MathPalette Python: ' + str(python), flush=True)
    print('Render environment: ' + json.dumps(found), flush=True)
    print('Matching redraw source(s): ' + ', '.join(matching_sources(found)), flush=True)
    print('Browsing is available for both sources. A different source may need its own MATHPALETTE_MATHVERSE_PYTHON or MATHPALETTE_MATHVISION_PYTHON; Pass always verifies exact pixels.', flush=True)
    arguments = sys.argv[1:]
    if '--check' in arguments:
        print(json.dumps({'environment_matches': True, 'matching_sources': matching_sources(found), 'mutations': 0}))
        return
    raise SystemExit(subprocess.call([str(python), '-X', 'utf8', '-B', str(ROOT / 'review_workbench/server.py'), *arguments], cwd=ROOT))


if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
