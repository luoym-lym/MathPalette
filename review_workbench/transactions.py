"""Write-ahead filesystem transactions, recovered only under the catalog lock.

Each intent (including exact before and after hashes) is fsynced before a target
can change. Unexpected external bytes stop recovery rather than being lost.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
import uuid


class RecoveryRequired(RuntimeError):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sync_directory(path):
    if os.name != 'nt':
        descriptor = os.open(path, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def atomic_write(path, data, *, exclusive=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix='.' + path.name + '.', suffix='.tmp', dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, 'wb') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if exclusive:
            if os.name == 'nt':
                # Windows rename is atomic and fails when the destination exists.
                # It also works on removable drives that do not support hard links.
                os.rename(temporary, path)
            else:
                # POSIX rename would clobber; a hard link publishes exclusively.
                os.link(temporary, path)
                temporary.unlink()
        else:
            os.replace(temporary, path)
        sync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


def safe_path(root, relative):
    root = Path(root).resolve()
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError(f'Unsafe path: {relative}')
    path = root / relative
    if path == root:
        raise ValueError('An item path is required')
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f'Symlinks are not allowed in review data: {relative}')
    if not path.resolve().is_relative_to(root):
        raise ValueError(f'Path escapes the repository: {relative}')
    return path


def tree_hash(path):
    path = Path(path)
    if not path.is_dir() or path.is_symlink():
        raise ValueError('Candidate item must be an ordinary directory')
    hashes = []
    for file in sorted(path.rglob('*')):
        if file.is_symlink():
            raise ValueError('Candidate item contains a symlink')
        if file.is_file():
            hashes.append((file.relative_to(path).as_posix(), sha(file.read_bytes())))
    return sha(json.dumps(hashes, ensure_ascii=False, separators=(',', ':')).encode())


_UNSET = object()


class Transaction:
    def __init__(self, root, *, existing=None, fault=None):
        self.root = Path(root).resolve()
        self.fault = fault
        self.directory = existing or (self.root / '.runtime/review_workbench/transactions' / uuid.uuid4().hex)
        if existing:
            self.manifest = json.loads((self.directory / 'journal.json').read_text(encoding='utf-8'))
        else:
            self.directory.mkdir(parents=True)
            self.manifest = {'version': 1, 'status': 'active', 'operations': []}
            self.save()

    def save(self):
        atomic_write(self.directory / 'journal.json', (json.dumps(self.manifest, ensure_ascii=False, indent=2) + '\n').encode())

    def signal(self, label):
        if self.fault:
            self.fault(label)

    def write(self, path, data, *, exclusive=False, expected_before=_UNSET):
        path = Path(path)
        if not path.is_absolute():
            path = self.root / path
        relative = path.relative_to(self.root).as_posix()
        path = safe_path(self.root, relative)
        previous = path.read_bytes() if path.exists() else None
        if expected_before is not _UNSET and previous != expected_before:
            raise RecoveryRequired(f'File changed outside the workbench: {relative}')
        if exclusive and previous is not None:
            raise FileExistsError(f'Will not replace an existing formal file: {relative}')
        if previous == data:
            return
        index = len(self.manifest['operations'])
        backup = f'before-{index}.bin' if previous is not None else None
        if backup:
            atomic_write(self.directory / backup, previous)
        operation = {'kind': 'write', 'path': relative, 'before': sha(previous) if previous is not None else None,
                     'after': sha(data), 'backup': backup}
        self.manifest['operations'].append(operation)
        self.save()
        self.signal('before_write:' + relative)
        # Recheck after journaling. External edits never get silently overwritten.
        current = sha(path.read_bytes()) if path.exists() else None
        if current != operation['before']:
            raise RecoveryRequired(f'File changed outside the workbench: {relative}')
        atomic_write(path, data, exclusive=previous is None)
        self.signal('after_write:' + relative)

    def remove_item(self, path):
        path = Path(path)
        relative = path.relative_to(self.root).as_posix()
        path = safe_path(self.root, relative)
        destination = self.directory / 'candidate'
        operation = {'kind': 'move', 'path': relative, 'stash': 'candidate', 'hash': tree_hash(path)}
        self.manifest['operations'].append(operation)
        self.save()
        self.signal('before_move')
        if tree_hash(path) != operation['hash']:
            raise RecoveryRequired('Candidate changed during removal')
        os.replace(path, destination)
        sync_directory(path.parent)
        sync_directory(self.directory)
        self.signal('after_move')

    def commit(self):
        self.signal('before_commit')
        self.manifest['status'] = 'committed'
        self.save()
        self.signal('after_commit')
        self.cleanup()

    def cleanup(self):
        # A committed journal is proof of success even if Windows keeps a file open.
        try:
            shutil.rmtree(self.directory)
        except OSError:
            return

    def rollback(self):
        if self.manifest['status'] == 'committed':
            self.cleanup()
            return
        for operation in reversed(self.manifest['operations']):
            if operation.get('rolled_back'):
                continue
            path = safe_path(self.root, operation['path'])
            if operation['kind'] == 'write':
                current = sha(path.read_bytes()) if path.exists() else None
                if current not in (operation['before'], operation['after']):
                    raise RecoveryRequired(f'Recovery stopped to preserve external changes: {operation["path"]}')
                if current == operation['before']:
                    operation['rolled_back'] = True
                    self.save()
                    continue
                if operation['before'] is None:
                    path.unlink()
                    sync_directory(path.parent)
                else:
                    backup = self.directory / operation['backup']
                    data = backup.read_bytes()
                    if sha(data) != operation['before']:
                        raise RecoveryRequired('Transaction backup is damaged')
                    atomic_write(path, data)
            else:
                stash = self.directory / operation['stash']
                if stash.exists():
                    if path.exists() or tree_hash(stash) != operation['hash']:
                        raise RecoveryRequired('Candidate recovery conflicts with external changes')
                    path.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(stash, path)
                    sync_directory(path.parent)
                    sync_directory(self.directory)
                elif not path.exists() or tree_hash(path) != operation['hash']:
                    raise RecoveryRequired('Candidate recovery data is missing or changed')
            operation['rolled_back'] = True
            self.save()
        self.manifest['status'] = 'rolled_back'
        self.save()
        self.cleanup()


def recover(root):
    """Caller must hold catalog.catalog_write_lock for recovery and later writes."""
    directory = Path(root) / '.runtime/review_workbench/transactions'
    if not directory.exists():
        return
    for item in sorted(directory.iterdir()):
        if not item.is_dir():
            continue
        journal = item / 'journal.json'
        if not journal.exists():
            # No published intent means this directory cannot own changed data.
            shutil.rmtree(item)
            continue
        transaction = Transaction(root, existing=item)
        if transaction.manifest['status'] in ('committed', 'rolled_back'):
            transaction.cleanup()
        else:
            transaction.rollback()
