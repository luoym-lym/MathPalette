"""Compare a visual revision with its Git baseline in one Python interpreter.

``ast.dump`` is not a portable serialization: even CPython 3.12 and 3.13 differ
in whether empty fields are displayed. Never compare these fingerprints with
one persisted by a different interpreter. Parse both source versions here.
"""
from __future__ import annotations

import ast
from functools import lru_cache
import hashlib
from pathlib import Path
import re
import subprocess

METADATA_FIELDS = {'question', 'query', 'answer', 'answer_type', 'choices'}


def _is_review_metadata(statement):
    if not (isinstance(statement, ast.Assign) and len(statement.targets) == 1):
        return False
    target = statement.targets[0]
    if not (isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name)
            and target.value.id == 'self' and target.attr in METADATA_FIELDS):
        return False
    value = statement.value
    if (target.attr == 'query' and isinstance(value, ast.Attribute)
            and isinstance(value.value, ast.Name) and value.value.id == 'self'
            and value.attr == 'question'):
        return True
    # A call or another executable expression must not disappear just because
    # it was assigned to a field normally used for literal review metadata.
    try:
        ast.literal_eval(value)
    except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
        return False
    return True


def renderer_fingerprint(source):
    """Return a same-interpreter comparison key, not a persistent file hash."""
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for method in node.body:
                if isinstance(method, ast.FunctionDef) and method.name == '__init__':
                    method.body = [statement for statement in method.body
                                   if not _is_review_metadata(statement)]
    return hashlib.sha256(ast.dump(tree, include_attributes=False).encode()).hexdigest()


@lru_cache(maxsize=128)
def baseline_bytes(root, base_commit, relative):
    """Read a pinned Git blob; missing history fails visibly, never skips QA."""
    if not re.fullmatch(r'[0-9a-f]{40}', base_commit):
        raise ValueError('The visual-revision baseline must be a full commit SHA')
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts or '\\' in relative:
        raise ValueError(f'Invalid baseline source path: {relative}')
    try:
        return subprocess.check_output(
            ['git', 'show', f'{base_commit}:{relative}'], cwd=root, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            f'Cannot read {relative} at baseline {base_commit}; '
            'fetch that commit before running the visual-revision checks') from error


def baseline_source(root, base_commit, relative):
    return baseline_bytes(root, base_commit, relative).decode('utf-8')


def assert_same_renderer(baseline, current, identity):
    """Compare both parsed sources using the caller's interpreter and schema."""
    if renderer_fingerprint(baseline) != renderer_fingerprint(current):
        raise ValueError(f'{identity}: rendering code changed relative to the Git baseline')

@lru_cache(maxsize=128)
def historical_bytes(root, relative, expected_sha256):
    """Read a pinned pre-integration source from active files or the v1 archive."""
    import json,tarfile
    root=Path(root)
    path=root/relative
    if path.is_file():
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()==expected_sha256:return data
    manifest=json.loads((root/'provenance/drawing_protocol_v1.json').read_text())
    archive=root/manifest['archive']
    if (manifest['files'].get(relative)!=expected_sha256 or
            hashlib.sha256(archive.read_bytes()).hexdigest()!=manifest['archive_sha256']):
        raise ValueError('Historical drawing archive does not match pinned source')
    with tarfile.open(archive,'r:gz') as tar:data=tar.extractfile(relative).read()
    if hashlib.sha256(data).hexdigest()!=expected_sha256:
        raise ValueError('Historical drawing source changed: '+relative)
    return data
