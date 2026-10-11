"""Durable local original review, serialized with the formal catalog writer.

The journal stores pre-images before touching either formal data or candidate files.
A process interruption rolls back on next startup; a durable commit is retained.
No Git mutation, network operation, or candidate-provided code is executed.
"""
from __future__ import annotations

import ast
import base64
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import subprocess
import threading
from urllib.parse import quote
import uuid

try:
    from .importer import (ROOT, ReviewError, candidate_id, eligibility, fingerprint,
                           json_bytes, package, parse_json, payload_paths, safe_path)
except ImportError:
    from importer import (ROOT, ReviewError, candidate_id, eligibility, fingerprint,
                          json_bytes, package, parse_json, payload_paths, safe_path)
from dataset_tools import catalog, question_review


def next_after_removal(records, cid):
    order = list(records)
    index = order.index(cid)
    remaining = [key for key in order if key != cid]
    return remaining[min(index, len(remaining) - 1)] if remaining else None


def _now():
    return datetime.now(timezone.utc).isoformat()


def _fsync_directory(path):
    if os.name != 'nt':
        descriptor = os.open(path, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def atomic_write(path, data, *, transaction_id=None, exclusive=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name('.' + path.name + '.' + (transaction_id or uuid.uuid4().hex) + '.tmp')
    try:
        with temporary.open('xb') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if exclusive:
            # Atomic no-clobber publication: a user-created target wins the race.
            os.link(temporary, path)
            temporary.unlink()
        else:
            os.replace(temporary, path)
        _fsync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


class ReviewStore:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.staging = safe_path(self.root, 'staging/solidgeo')
        self.manifest = safe_path(self.root, 'staging/solidgeo/candidates.jsonl')
        self.runtime = safe_path(self.root, '.runtime/solidgeo-original-review')
        self.state_path = safe_path(self.root, '.runtime/solidgeo-original-review/state.json')
        self.journal_path = safe_path(self.root, '.runtime/solidgeo-original-review/transaction.json')
        self.runtime.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()
        self.review_token, self.session_id = secrets.token_urlsafe(32), uuid.uuid4().hex
        self.failpoint = lambda stage: None
        self.validation_cache = {}
        self._active_journal_id = None
        self._journal = None
        self._planned_delete_hashes = {}
        with self.lock, catalog.catalog_write_lock(self.root):
            self._recover()
            self._read_state()
            self._read_candidates()

    def _read_state(self):
        if not self.state_path.exists():
            self.state = {'schema_version': 1, 'current_candidate_id': None,
                          'reviews': {}, 'requests': {}, 'next_solid_number': 1}
        else:
            self.state = parse_json(self.state_path.read_text(encoding='utf-8'))
            if self.state.get('schema_version') != 1 or not isinstance(self.state.get('reviews'), dict) or not isinstance(self.state.get('requests'), dict):
                raise ReviewError('审核状态格式无效；请先保留并检查状态文件。', 500, 'invalid_state')
        return self.state

    def _read_candidates(self):
        if not self.manifest.is_file():
            raise ReviewError('缺少 staging/solidgeo/candidates.jsonl。', 500, 'missing_manifest')
        self._manifest_bytes = self.manifest.read_bytes()
        records = [parse_json(line) for line in self._manifest_bytes.decode('utf-8-sig').splitlines() if line.strip()]
        result = {}
        for row in records:
            cid = candidate_id(row)
            if cid in result:
                raise ReviewError(f'候选 ID 重复：{cid}', 500, 'duplicate_candidate')
            result[cid] = row
        return result

    def _reload(self):
        self._recover()
        self._read_state()
        return self._read_candidates()

    def _recover(self):
        if not self.journal_path.exists():
            return
        journal = parse_json(self.journal_path.read_text(encoding='utf-8'))
        if journal.get('version') != 1 or not isinstance(journal.get('before'), dict):
            raise ReviewError('事务恢复记录无效，已停止写入。', 500, 'recovery_required')
        if journal.get('status') != 'committed':
            # catalog_write_lock is held; recover the entire transaction, not only
            # its last visible mutation. Empty backups represent newly made files.
            for relative, encoded in journal['before'].items():
                path = safe_path(self.root, relative)
                if relative in journal.get('preserve_on_rollback', []):
                    continue
                current = path.read_bytes() if path.is_file() else None
                original = base64.b64decode(encoded, validate=True) if encoded is not None else None
                planned_write = journal.get('writes', {}).get(relative)
                if planned_write is not None and current != original and (current is None or hashlib.sha256(current).hexdigest() != planned_write):
                    continue  # Another editor owns bytes different from both snapshots.
                if relative in journal.get('operation', {}).get('new_paths', []) and planned_write is None and current is not None:
                    continue  # Not yet written by this transaction: preserve user creation.
                if encoded is None:
                    if path.exists():
                        if not path.is_file():
                            raise ReviewError('恢复目标不是普通文件。', 500, 'recovery_required')
                        path.unlink()
                        _fsync_directory(path.parent)
                else:
                    original = base64.b64decode(encoded, validate=True)
                    # Candidate payloads are only unlinked, never overwritten by
                    # this workbench. Different surviving bytes belong to an
                    # external editor and must not be destroyed by rollback.
                    owner_prefix = 'staging/solidgeo/candidates/' + str(journal.get('operation', {}).get('candidate_id', '')) + '/'
                    if relative.startswith(owner_prefix) and path.is_file() and path.read_bytes() != original:
                        continue
                    atomic_write(path, original)
        # Remove only temporaries bearing this transaction's unguessable ID.
        transaction_id = journal.get('id', '')
        if re.fullmatch(r'[0-9a-f]{32}', transaction_id):
            for relative in journal['before']:
                path = safe_path(self.root, relative)
                temporary = path.with_name('.' + path.name + '.' + transaction_id + '.tmp')
                if temporary.is_symlink():
                    raise ReviewError('事务临时文件被替换为链接。', 500, 'recovery_required')
                temporary.unlink(missing_ok=True)
        self.journal_path.unlink()
        _fsync_directory(self.runtime)
        self._active_journal_id = None
        self._journal = None
        self.validation_cache.clear()

    def _prepare(self, paths, operation):
        if self.journal_path.exists():
            raise ReviewError('仍有未完成事务，拒绝交叠写入。', 409, 'transaction_pending')
        before = {}
        for relative in sorted(set(paths)):
            path = safe_path(self.root, relative)
            if path.exists() and not path.is_file():
                raise ReviewError(f'写入目标不是普通文件：{relative}')
            original = path.read_bytes() if path.exists() else None
            if relative == 'staging/solidgeo/candidates.jsonl' and (original is None or hashlib.sha256(original).hexdigest() != operation.get('manifest_sha256')):
                raise ReviewError('候选清单在事务准备期间改变，请刷新后重试。', 409, 'stale_candidate')
            if relative in operation.get('new_paths', []) and original is not None:
                raise ReviewError('正式目标在事务准备期间出现，拒绝覆盖：' + relative, 409, 'formal_collision')
            if relative in self._planned_delete_hashes and (original is None or hashlib.sha256(original).hexdigest() != self._planned_delete_hashes[relative]):
                raise ReviewError('清理准备期间候选文件改变，请重新查看：' + relative, 409, 'stale_candidate')
            before[relative] = base64.b64encode(original).decode('ascii') if original is not None else None
        journal = {'version': 1, 'id': uuid.uuid4().hex, 'status': 'prepared',
                   'operation': operation, 'created_at_utc': _now(), 'before': before, 'writes': {}, 'preserve_on_rollback': []}
        atomic_write(self.journal_path, json_bytes(journal))
        self._active_journal_id = journal['id']
        self._journal = journal
        self.failpoint('prepared')
        return journal

    def _write(self, relative, data):
        self.failpoint('before_write:' + relative)
        path = safe_path(self.root, relative)
        encoded = self._journal['before'][relative]
        before = base64.b64decode(encoded, validate=True) if encoded is not None else None
        current = path.read_bytes() if path.is_file() else None
        if current != before:
            self._journal['preserve_on_rollback'].append(relative)
            atomic_write(self.journal_path, json_bytes(self._journal))
            code = 'formal_collision' if relative in self._journal['operation'].get('new_paths', []) else 'stale_candidate'
            raise ReviewError('写入目标在事务期间改变，已保留本地文件：' + relative, 409, code)
        self._journal['writes'][relative] = hashlib.sha256(data).hexdigest()
        atomic_write(self.journal_path, json_bytes(self._journal))
        try:
            atomic_write(path, data, transaction_id=self._active_journal_id,
                         exclusive=relative in self._journal['operation'].get('new_paths', []))
        except FileExistsError:
            self._journal['preserve_on_rollback'].append(relative)
            atomic_write(self.journal_path, json_bytes(self._journal))
            raise ReviewError('正式目标已被创建，已保留该文件：' + relative, 409, 'formal_collision')
        self.failpoint('after_write:' + relative)

    def _unlink(self, relative):
        self.failpoint('before_unlink:' + relative)
        path = safe_path(self.root, relative)
        if not path.is_file() or catalog.file_hash(path) != self._planned_delete_hashes.get(relative):
            raise ReviewError('候选文件在清理前改变；已停止删除并保留本地更改，请重新查看：' + relative, 409, 'stale_candidate')
        path.unlink()
        _fsync_directory(path.parent)
        self.failpoint('after_unlink:' + relative)

    def _commit(self, journal):
        journal['status'], journal['committed_at_utc'] = 'committed', _now()
        atomic_write(self.journal_path, json_bytes(journal))
        self.failpoint('committed')
        self.journal_path.unlink()
        _fsync_directory(self.runtime)
        self._active_journal_id = None
        self._journal = None

    def _inspect(self, row, *, render=False):
        digest = fingerprint(self.root, row)
        key = (candidate_id(row), digest)
        cached = self.validation_cache.get(key)
        if cached is None:
            cached = eligibility(self.root, row, render=False)
            cached['render_checked'] = False
            self.validation_cache[key] = cached
        if render and cached['eligible'] and not cached['render_checked']:
            checked = eligibility(self.root, row, render=True)
            checked['render_checked'] = True
            self.validation_cache[key] = cached = checked
        return digest, cached

    def _snapshot_locked(self, records=None):
        records = records if records is not None else self._read_candidates()
        current = self.state.get('current_candidate_id')
        if current not in records:
            current = next((cid for cid in records if self.state['reviews'].get(cid, {}).get('status') != 'passed'), next(iter(records), None))
        candidates = []
        for cid, row in records.items():
            review = self.state['reviews'].get(cid, {})
            if review.get('status') == 'deleted':
                raise ReviewError('已删除候选重新出现，须先核对恢复操作。', 409, 'candidate_reappeared')
            digest, inspection = self._inspect(row, render=(cid == current and review.get('status') != 'passed'))
            reasons = list(inspection['reasons'])
            eligible = inspection['eligible'] and inspection['render_checked']
            if not inspection['render_checked'] and inspection['eligible']:
                reasons.append('打开此题后将执行当前协议的两次重绘校验。')
            item = copy.deepcopy(row)
            item.update(candidate_id=cid, id=cid, status=review.get('status', 'pending'),
                        content_sha256=digest, eligible=eligible, pass_eligible=eligible,
                        ineligible_reasons=reasons, validation_pending=not inspection['render_checked'],
                        source_image_url=f'/api/image/{quote(cid)}/source',
                        redraw_image_url=f'/api/image/{quote(cid)}/redraw')
            if review.get('status') == 'passed':
                item.update(formal_id=review['formal_id'], eligible=False, pass_eligible=False,
                            approved_at_utc=review['approved_at_utc'], ineligible_reasons=['原题已通过并收录。'])
            candidates.append(item)
        return {'ok': True, 'session_id': self.session_id, 'review_token': self.review_token,
                'current_candidate_id': current, 'candidates': candidates,
                'completed_reviews': [copy.deepcopy(review['result']) for review in self.state['reviews'].values()],
                'counts': {'total': len(candidates), 'pending': sum(c['status'] == 'pending' for c in candidates),
                           'passed': sum(r['status'] == 'passed' for r in self.state['reviews'].values()),
                           'deleted': sum(r['status'] == 'deleted' for r in self.state['reviews'].values())}}

    def snapshot(self):
        with self.lock, catalog.catalog_write_lock(self.root):
            return self._snapshot_locked(self._reload())

    def navigate(self, cid):
        with self.lock, catalog.catalog_write_lock(self.root):
            records = self._reload()
            if cid not in records:
                raise ReviewError('候选题不存在。', 404, 'not_found')
            self.state['current_candidate_id'] = cid
            atomic_write(self.state_path, json_bytes(self.state))
            return self._snapshot_locked(records)

    def image(self, cid, kind):
        with self.lock, catalog.catalog_write_lock(self.root):
            records = self._reload()
            if cid not in records or kind not in ('source', 'redraw'):
                raise ReviewError('图片不存在。', 404, 'not_found')
            paths = payload_paths(self.root, records[cid])
            path = paths['original_image' if kind == 'source' else 'image']
            import mimetypes
            return path.read_bytes(), mimetypes.guess_type(path.name)[0] or 'application/octet-stream'

    def _request(self, action, cid, digest, request_id, records):
        if not isinstance(request_id, str) or not re.fullmatch(r'[A-Za-z0-9_-]{8,128}', request_id):
            raise ReviewError('每次审核须提供独立的 request_id。', code='invalid_request_id')
        if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest):
            raise ReviewError('缺少有效内容指纹。', code='invalid_fingerprint')
        signature = {'action': action, 'candidate_id': cid, 'content_sha256': digest}
        prior = self.state['requests'].get(request_id)
        if prior:
            if prior['signature'] != signature:
                raise ReviewError('此请求 ID 已用于不同操作。', 409, 'request_conflict')
            return signature, prior['result']
        previous = self.state['reviews'].get(cid, {})
        if previous:
            if previous['status'] == ('passed' if action == 'pass' else 'deleted') and previous['content_sha256'] == digest:
                self.state['requests'][request_id] = {'signature': signature, 'result': previous['result']}
                atomic_write(self.state_path, json_bytes(self.state))
                return signature, previous['result']
            raise ReviewError('此候选已审核；不能再次执行不同操作。', 409, 'already_reviewed')
        if cid not in records:
            raise ReviewError('候选题不存在或已删除。', 404, 'not_found')
        actual = fingerprint(self.root, records[cid])
        if actual != digest:
            raise ReviewError('题目或文件已经改变；请刷新并重新查看后审核。', 409, 'stale_candidate')
        return signature, None

    def _record_result(self, action, cid, digest, request_id, signature, result):
        self.state['reviews'][cid] = {'status': 'passed' if action == 'pass' else 'deleted',
            'content_sha256': digest, 'approved_at_utc': result['at_utc'],
            'formal_id': result.get('formal_id'), 'result': result}
        self.state['requests'][request_id] = {'signature': signature, 'result': result}
        self._write(self.state_path.relative_to(self.root).as_posix(), json_bytes(self.state))

    def _assert_recoverable_record(self, cid, row):
        committed = subprocess.run(['git', '-C', str(self.root), 'show',
                                    'HEAD:staging/solidgeo/candidates.jsonl'],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            head_rows = [parse_json(line) for line in committed.stdout.decode('utf-8-sig').splitlines() if line.strip()] if committed.returncode == 0 else []
            head = next((record for record in head_rows if candidate_id(record) == cid), None)
        except (ValueError, UnicodeError):
            head = None
        if head is None or catalog.digest(head) != catalog.digest(row):
            raise ReviewError('此候选记录含尚未保存到 Git 历史的更改，不能安全移除。请自行提交或另存题目记录后重试：' + cid,
                              409, 'dirty_candidate_record')

    def _assert_manifest_unchanged(self):
        if self.manifest.read_bytes() != self._manifest_bytes:
            raise ReviewError('候选清单在审核期间改变，请刷新并重新审核。', 409, 'stale_candidate')

    def pass_candidate(self, cid, digest, request_id):
        with self.lock, catalog.catalog_write_lock(self.root):
            records = self._reload()
            signature, prior = self._request('pass', cid, digest, request_id, records)
            if prior:
                return {**self._snapshot_locked(records), 'result': prior}
            row = records[cid]
            delete, shared, untracked = self._deletion_paths(cid, row, records)
            remaining = {key: value for key, value in records.items() if key != cid}
            actual, inspection = self._inspect(row, render=True)
            if not inspection['eligible']:
                raise ReviewError('不能通过：' + '；'.join(inspection['reasons']), 422, 'ineligible_candidate')
            self._assert_recoverable_record(cid, row)
            # Recheck under the same catalog lock immediately before package creation.
            if fingerprint(self.root, row) != digest:
                raise ReviewError('校验期间候选文件改变，请重新审核。', 409, 'stale_candidate')
            catalog.catalog(self.root)  # Never silently refresh any existing approval.
            dataset_path = self.root / 'SolidGeometry/dataset.jsonl'
            formal = catalog.rows(dataset_path)
            if [r['id'] for r in formal] != [f'Solid{i:02d}' for i in range(1, len(formal) + 1)]:
                raise ReviewError('正式 Solid 题号不连续，普通工作台无法读取；请先核对正式清单。', 409, 'formal_numbering_conflict')
            if any(r['source_dataset'] == row['source_dataset'] and r.get('source_key') == row['source_key'] for r in formal):
                raise ReviewError('此来源题已在正式数据集中，拒绝重复导入。', 409, 'duplicate_source')
            numbers = [int(r['id'][5:]) for r in formal if re.fullmatch(r'Solid\d+', r['id'])]
            approvals = catalog.read(self.root / 'provenance/approvals.json')['approvals']
            numbers += [int(qid[5:]) for qid in approvals if re.fullmatch(r'Solid\d+', qid)]
            number = max(max(numbers, default=0) + 1, int(self.state.get('next_solid_number', 1)))
            if number != len(formal) + 1:
                raise ReviewError('本机审核状态的编号领先于正式题库，可能恢复过 Git 文件；请先核对审核状态与正式记录，不能跳号或复用旧号。', 409, 'formal_numbering_conflict')
            formal_id = f'Solid{number:02d}'
            record, notes, artifacts = package(self.root, row, formal_id, inspection, digest)
            if fingerprint(self.root, row) != digest:
                raise ReviewError('准备导入时文件改变，请重新审核。', 409, 'stale_candidate')
            all_notes = catalog.read(self.root / 'provenance/source_notes.json')
            if formal_id in all_notes:
                raise ReviewError('正式题号已有来源记录，拒绝覆盖。', 409, 'formal_collision')
            all_notes[formal_id] = notes
            manifest_relative = self.manifest.relative_to(self.root).as_posix()
            if safe_path(self.root, 'provenance/approvals.json.tmp').exists():
                raise ReviewError('存在未处理的审核临时文件，请先核对并另存。', 409, 'preexisting_temporary')
            touched = [*artifacts, *delete, manifest_relative, 'SolidGeometry/dataset.jsonl', 'provenance/source_notes.json',
                       'provenance/approvals.json', 'provenance/approvals.json.tmp', 'question_bank.jsonl', self.state_path.relative_to(self.root).as_posix()]
            self._assert_manifest_unchanged()
            journal = None
            try:
                journal = self._prepare(touched, {'action': 'pass', 'candidate_id': cid, 'formal_id': formal_id, 'new_paths': list(artifacts), 'manifest_sha256': hashlib.sha256(self._manifest_bytes).hexdigest()})
                for relative, data in artifacts.items():
                    self._write(relative, data)
                self._write('SolidGeometry/dataset.jsonl', dataset_path.read_bytes().rstrip(b'\r\n') + b'\n' + json.dumps(record, ensure_ascii=False, allow_nan=False).encode('utf-8') + b'\n')
                self._write('provenance/source_notes.json', json_bytes(all_notes))
                self.failpoint('files_written')
                # This is the user's explicit ORIGINAL Pass, never a Special pass.
                # The shared approval helper has its own atomic writes. Guard its
                # inputs and bind its completed outputs into this larger journal.
                for relative in ('provenance/approvals.json', 'provenance/approvals.json.tmp', 'question_bank.jsonl'):
                    target = safe_path(self.root, relative)
                    current = target.read_bytes() if target.is_file() else None
                    encoded = journal['before'][relative]
                    original = base64.b64decode(encoded, validate=True) if encoded is not None else None
                    if current != original:
                        journal['preserve_on_rollback'].append(relative)
                        atomic_write(self.journal_path, json_bytes(journal))
                        raise ReviewError('审核或目录文件在操作期间改变，已保留本地更改：' + relative, 409, 'stale_candidate')
                question_review.approve('SolidGeometry', [formal_id], 'Pass (原题通过)', self.root, catalog_lock_held=True)
                for relative in ('provenance/approvals.json', 'question_bank.jsonl'):
                    journal['writes'][relative] = catalog.file_hash(safe_path(self.root, relative, must_exist=True))
                atomic_write(self.journal_path, json_bytes(journal))
                self.failpoint('catalog_built')
                approval = catalog.read(self.root / 'provenance/approvals.json')['approvals'][formal_id]
                result = {'action': 'pass', 'candidate_id': cid, 'formal_id': formal_id,
                          'at_utc': approval['approved_at_utc'], 'candidate_sha256': digest,
                          'deleted_files': delete, 'preserved_shared_files': shared, 'preserved_untracked_files': untracked}
                self._write(manifest_relative, b''.join(json.dumps(candidate, ensure_ascii=False, allow_nan=False).encode('utf-8') + b'\n' for candidate in remaining.values()))
                for relative in delete:
                    self._unlink(relative)
                self.state['next_solid_number'] = number + 1
                self.state['current_candidate_id'] = next_after_removal(records, cid)
                self._record_result('pass', cid, digest, request_id, signature, result)
                self._commit(journal)
            except Exception:
                self._recover()
                self._read_state()
                raise
            return {**self._snapshot_locked(remaining), 'result': result}

    def _deletion_paths(self, cid, row, records):
        """Git-tracked files confined to this owner directory, minus all references.

        Untracked files, shared dependency directories, symlinks and formal paths
        are never deletion candidates. All declared cross-candidate references
        (including references inside JSON payloads) protect the referenced file.
        """
        self._planned_delete_hashes = {}
        owner = safe_path(self.staging, f'candidates/{cid}')
        own_relative = owner.relative_to(self.root).as_posix()
        result = subprocess.run(['git', '-C', str(self.root), 'ls-files', '-z', '--', own_relative + '/'],
                                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        tracked = []
        for raw in result.stdout.split(b'\x00'):
            if not raw:
                continue
            relative = raw.decode('utf-8')
            path = safe_path(self.root, relative)
            if path.is_file() and path.is_relative_to(owner):
                tracked.append(path)
        untracked = [path.relative_to(self.root).as_posix() for path in owner.rglob('*')
                     if (path.is_file() or path.is_symlink()) and path not in tracked] if owner.is_dir() else []
        protected = set()
        def references(value, bases):
            if isinstance(value, dict):
                for child in value.values():
                    references(child, bases)
            elif isinstance(value, list):
                for child in value:
                    references(child, bases)
            elif isinstance(value, str) and len(value) < 4096 and '\x00' not in value:
                for base in bases:
                    try:
                        path = (base / value).resolve()
                        if path in tracked:
                            protected.add(path)
                        elif path.is_dir():
                            protected.update(item for item in tracked if item.is_relative_to(path))
                    except (OSError, ValueError):
                        continue
        for other_id, other in records.items():
            if other_id == cid:
                continue
            references(other, [self.root, self.staging])
            # A malformed competing record must never cause more deletion.
            try:
                other_paths = payload_paths(self.root, other, must_exist=False)
            except ReviewError:
                return [], [p.relative_to(self.root).as_posix() for p in tracked], untracked
            for path in other_paths.values():
                if path in tracked:
                    protected.add(path)
                if path.is_file() and path.suffix.lower() == '.json':
                    try:
                        references(parse_json(path.read_text(encoding='utf-8-sig')), [self.root, self.staging, path.parent])
                    except (ValueError, UnicodeError):
                        return [], [p.relative_to(self.root).as_posix() for p in tracked], untracked
                elif path.is_file() and path.suffix.lower() == '.py':
                    try:
                        tree = ast.parse(path.read_text(encoding='utf-8-sig'))
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                                references(node.value, [self.root, self.staging, path.parent])
                    except (SyntaxError, ValueError, UnicodeError):
                        return [], [p.relative_to(self.root).as_posix() for p in tracked], untracked
        deletable = [p for p in tracked if p not in protected]
        self._planned_delete_hashes = {}
        # Git tracking alone is insufficient: preserve uncommitted unique bytes.
        for path in deletable:
            relative = path.relative_to(self.root).as_posix()
            committed = subprocess.run(['git', '-C', str(self.root), 'show', 'HEAD:' + relative],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            actual_bytes = path.read_bytes()
            if committed.returncode or committed.stdout != actual_bytes:
                raise ReviewError('此候选含尚未保存到 Git 历史的文件更改，不能安全删除。请自行提交或另存这些更改后重试：' + relative, 409, 'dirty_candidate_payload')
            self._planned_delete_hashes[relative] = hashlib.sha256(actual_bytes).hexdigest()
        return ([p.relative_to(self.root).as_posix() for p in deletable],
                [p.relative_to(self.root).as_posix() for p in tracked if p in protected], untracked)

    def delete_candidate(self, cid, digest, request_id):
        with self.lock, catalog.catalog_write_lock(self.root):
            records = self._reload()
            signature, prior = self._request('delete', cid, digest, request_id, records)
            if prior:
                return {**self._snapshot_locked(records), 'result': prior}
            self._assert_recoverable_record(cid, records[cid])
            delete, shared, untracked = self._deletion_paths(cid, records[cid], records)
            self._assert_manifest_unchanged()
            if fingerprint(self.root, records[cid]) != digest:
                raise ReviewError('引用核对期间候选文件改变，请刷新并重新审核。', 409, 'stale_candidate')
            remaining = {key: value for key, value in records.items() if key != cid}
            manifest_relative = self.manifest.relative_to(self.root).as_posix()
            touched = [*delete, manifest_relative, self.state_path.relative_to(self.root).as_posix()]
            try:
                journal = self._prepare(touched, {'action': 'delete', 'candidate_id': cid, 'manifest_sha256': hashlib.sha256(self._manifest_bytes).hexdigest()})
                self._write(manifest_relative, b''.join(json.dumps(row, ensure_ascii=False, allow_nan=False).encode('utf-8') + b'\n' for row in remaining.values()))
                for relative in delete:
                    self._unlink(relative)
                self.failpoint('files_written')
                result = {'action': 'delete', 'candidate_id': cid, 'at_utc': _now(),
                          'deleted_files': delete, 'preserved_shared_files': shared, 'preserved_untracked_files': untracked,
                          'recovery': 'Git can restore tracked candidate files and candidates.jsonl; no Git history was changed.'}
                if self.state.get('current_candidate_id') == cid:
                    self.state['current_candidate_id'] = next_after_removal(records, cid)
                self._record_result('delete', cid, digest, request_id, signature, result)
                self._commit(journal)
            except Exception:
                self._recover()
                self._read_state()
                raise
            return {**self._snapshot_locked(remaining), 'result': result}
