"""Start the local original-review server in its exact, frozen render environment.

This launcher deliberately uses only Python's standard library. It never installs
packages, accesses model services, or changes an existing environment.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
REQUIRED_PYTHON = '3.13.9'
PACKAGES = ('matplotlib', 'numpy', 'pillow')
PROBE = '''
import json, platform
from importlib.metadata import PackageNotFoundError, version
result = {'python': platform.python_version()}
for name in ('matplotlib', 'numpy', 'pillow'):
    try:
        result[name] = version(name)
    except PackageNotFoundError:
        result[name] = None
print(json.dumps(result))
'''


def required_environment(root=PROJECT):
    required = {'python': REQUIRED_PYTHON}
    for line in (Path(root) / 'requirements.txt').read_text(encoding='utf-8-sig').splitlines():
        name, separator, version = line.split('#', 1)[0].strip().partition('==')
        if separator and name.strip().lower() in PACKAGES:
            required[name.strip().lower()] = version.strip()
    if set(required) != {'python', *PACKAGES}:
        raise ValueError('requirements.txt 必须固定 matplotlib、numpy、pillow 的版本。')
    return required


def python_candidates(root=PROJECT):
    override = os.environ.get('MATHPALETTE_PYTHON')
    if override:
        path = Path(override).expanduser()
        if not path.is_file():
            raise ValueError('MATHPALETTE_PYTHON 不存在，请填写 python.exe 的完整路径（环境变量内容不要额外加引号）。')
        return [path.absolute()]
    paths = [Path(sys.executable)]
    prefixes = [Path(root) / '.venv', Path(root) / 'venv']
    if os.environ.get('CONDA_PREFIX'):
        prefixes.append(Path(os.environ['CONDA_PREFIX']))
    prefixes.extend(Path.home() / name for name in ('miniconda3', 'anaconda3'))
    registry = Path.home() / '.conda' / 'environments.txt'
    if registry.is_file():
        prefixes.extend(Path(line.strip()) for line in registry.read_text(encoding='utf-8-sig').splitlines() if line.strip())
    for prefix in prefixes:
        paths.extend(prefix / name for name in ('python.exe', 'Scripts/python.exe', 'bin/python'))
    for directory in os.get_exec_path():
        if directory:
            paths.extend(Path(directory) / name for name in ('python.exe', 'python3', 'python'))
    if os.name == 'nt':
        try:
            result = subprocess.run(['py', '-0p'], capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', timeout=8)
            for line in result.stdout.splitlines():
                # The Windows py launcher prefixes each full path with a version tag.
                position = line.lower().find(':\\')
                if position > 0:
                    paths.append(Path(line[position - 1:].strip().rstrip('*').strip()))
        except (OSError, subprocess.TimeoutExpired):
            pass
    return list(dict.fromkeys(path.absolute() for path in paths if path.is_file()))


def select_python(required, root=PROJECT):
    checked = []
    for path in python_candidates(root):
        try:
            result = subprocess.run([str(path), '-X', 'utf8', '-B', '-c', PROBE],
                                    capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=12)
            environment = json.loads(result.stdout) if result.returncode == 0 else {}
        except (OSError, ValueError, subprocess.TimeoutExpired):
            environment = {}
        checked.append(f'  {path}: {json.dumps(environment, ensure_ascii=False)}')
        if all(environment.get(name) == version for name, version in required.items()):
            return path, environment
    setup = ('\n一次性准备（在项目根目录执行，先安装 Python ' + REQUIRED_PYTHON + '）：\n'
             '  py -3.13 -m venv .venv\n'
             '  .venv\\Scripts\\python.exe -m pip install -r requirements.txt\n'
             '  SolidGeometry\\start_original_review.cmd\n'
             '已有匹配环境时，设置 MATHPALETTE_PYTHON 为该环境 python.exe 的完整路径。\n'
             '启动器不会自动下载、安装或更改依赖。')
    raise ValueError('未找到匹配的原题重绘环境。\n需要：' + json.dumps(required, ensure_ascii=False)
                     + '\n已检查：\n' + ('\n'.join(checked) or '  没有找到可执行 Python。') + setup)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=PROJECT, help='Repository root; defaults to this checkout.')
    parser.add_argument('--port', type=int, default=8770, help='Loopback-only port (default: 8770).')
    parser.add_argument('--check', action='store_true', help='Check the frozen environment without starting a service.')
    parser.add_argument('--no-browser', action='store_true', help='Do not open a browser automatically.')
    args = parser.parse_args(argv)
    if not 1 <= args.port <= 65535:
        parser.error('--port 必须在 1 到 65535 之间。')
    root = args.root.resolve()
    python, environment = select_python(required_environment(root), root)
    print(f'SOLIDGEO 原题审核 Python: {python}', flush=True)
    print('冻结环境: ' + json.dumps(environment, ensure_ascii=False), flush=True)
    if args.check:
        print('环境检查通过；没有启动服务或写入审核记录。', flush=True)
        return 0
    arguments = [str(python), '-X', 'utf8', '-B', str(HERE / 'server.py'), '--root', str(root), '--port', str(args.port)]
    if not args.no_browser:
        arguments.append('--open-browser')
    print(f'本机地址: http://127.0.0.1:{args.port}/\n请保持本窗口打开；按 Ctrl+C 停止服务。', flush=True)
    try:
        code = subprocess.call(arguments, cwd=root)
    except KeyboardInterrupt:
        print('\n原题审核已停止。已确认保存的记录保留在本机。', flush=True)
        return 0
    if code:
        print('服务未正常启动或已退出。若端口被占用，请关闭之前的启动窗口，或添加 --port 8771。', file=sys.stderr)
    return code


if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
