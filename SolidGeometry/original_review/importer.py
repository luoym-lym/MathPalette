"""Strict, non-executing candidate inspection and minimal formal packages."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import threading

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from dataset_tools import catalog
from dataset_tools.answer_schema import validate_answer

RENDER_LOCK = threading.RLock()
SAFE_ID = re.compile(r'[A-Za-z0-9][A-Za-z0-9_-]{0,99}\Z')
FILE_FIELDS = {'original_image': 'original', 'image': 'redraw', 'scene': 'scene',
               'drawing_script': 'draw', 'provenance': 'provenance'}


class ReviewError(ValueError):
    def __init__(self, message, status=400, code='invalid_request'):
        super().__init__(message)
        self.status, self.code = status, code


def parse_json(data):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ReviewError(f'JSON 键重复：{key}')
            result[key] = value
        return result
    def invalid(value):
        raise ReviewError(f'JSON 数值无效：{value}')
    return json.loads(data, object_pairs_hook=pairs, parse_constant=invalid)


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8')


def safe_path(root, relative, *, must_exist=False):
    """Reject absolute/traversal paths and every symlink, including parent links."""
    root = Path(root).resolve()
    if not isinstance(relative, str) or not relative or '\\' in relative or '\x00' in relative:
        raise ReviewError('数据路径无效。', code='unsafe_path')
    part = PurePosixPath(relative)
    if part.is_absolute() or '..' in part.parts or ':' in relative or part == PurePosixPath('.'):
        raise ReviewError(f'不安全的数据路径：{relative}', code='unsafe_path')
    target = root
    for name in part.parts:
        target = target / name
        if target.is_symlink():
            raise ReviewError(f'不允许符号链接：{relative}', code='unsafe_path')
    if not target.resolve().is_relative_to(root):
        raise ReviewError(f'数据路径越界：{relative}', code='unsafe_path')
    if must_exist and not target.is_file():
        raise ReviewError(f'缺少必要文件：{relative}', code='missing_payload')
    return target


def candidate_id(row):
    if not isinstance(row, dict) or not isinstance(row.get('id'), str) or ('candidate_id' in row and not isinstance(row['candidate_id'], str)):
        raise ReviewError('候选题 ID 必须为字符串。', code='invalid_candidate')
    value = row.get('candidate_id', row.get('id', ''))
    if not SAFE_ID.fullmatch(value):
        raise ReviewError('候选题 ID 无效。', code='invalid_candidate')
    if 'id' in row and row['id'] != value:
        raise ReviewError('候选题身份不一致。', code='invalid_candidate')
    return value


def payload_paths(root, row, *, must_exist=True):
    root = Path(root).resolve()
    staging = safe_path(root, 'staging/solidgeo')
    result = {}
    if 'paths' in row and not isinstance(row['paths'], dict):
        raise ReviewError('候选路径集合必须为对象。', code='unsafe_path')
    for field, alias in FILE_FIELDS.items():
        value = row.get(field)
        if value is not None:
            path = safe_path(staging, value, must_exist=must_exist)
            alternate = row.get('paths', {}).get(alias)
            if alternate is not None and safe_path(root, alternate, must_exist=must_exist) != path:
                raise ReviewError(f'候选路径别名不一致：{field}', code='unsafe_path')
        else:
            value = row.get('paths', {}).get(alias)
            if value is None:
                if field in ('drawing_script', 'provenance'):
                    continue
                raise ReviewError(f'缺少必要路径：{field}', code='missing_payload')
            path = safe_path(root, value, must_exist=must_exist)
            if not path.is_relative_to(staging):
                raise ReviewError('候选文件必须在 staging/solidgeo 中。', code='unsafe_path')
        result[field] = path
    return result


def environment():
    from importlib.metadata import version
    return {'python': sys.version.split()[0], **{name: version(name) for name in ('matplotlib', 'numpy', 'Pillow')}}


def fingerprint(root, row):
    """Even broken candidates get a revision token, never a guessed file hash."""
    files, errors = {}, []
    try:
        paths = payload_paths(root, row, must_exist=False)
        for name, path in sorted(paths.items()):
            if path.is_file():
                files[name] = {'path': path.relative_to(root).as_posix(), 'sha256': catalog.file_hash(path)}
            else:
                files[name] = {'path': path.relative_to(root).as_posix(), 'missing': True}
    except ReviewError as error:
        errors.append(str(error))
    dependencies = {}
    for relative in ('SolidGeometry/dataset_generator/common_renderer.py',
                     'SolidGeometry/dataset_generator/protocol.json',
                     'dataset_tools/geometry_dataset.py'):
        dependencies[relative] = catalog.file_hash(safe_path(root, relative, must_exist=True))
    source_notes = row.get('source_notes', {})
    attribution = source_notes.get('dataset_attribution') if isinstance(source_notes, dict) else None
    if isinstance(attribution, str):
        try:
            dependencies['dataset_attribution'] = catalog.file_hash(safe_path(root, attribution, must_exist=True))
        except (ReviewError, OSError) as error:
            errors.append(str(error))
    return catalog.digest({'candidate': row, 'files': files, 'errors': errors,
                           'dependencies': dependencies, 'environment': environment()})


def load_renderer(root):
    path = safe_path(root, 'SolidGeometry/dataset_generator/common_renderer.py', must_exist=True)
    # Only the repository's shared renderer is executed, never a candidate script.
    name = '_original_review_renderer_' + hashlib.sha256(str(root).encode()).hexdigest()[:12]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    try:
        sys.dont_write_bytecode = True
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def _pixels(data):
    from PIL import Image
    with Image.open(io.BytesIO(data)) as image:
        if image.format != 'PNG' or image.size != (768, 768):
            raise ReviewError('重绘图必须是 768×768 PNG。', code='invalid_render')
        rgba = image.convert('RGBA')
        if rgba.getextrema()[3] != (255, 255):
            raise ReviewError('重绘图必须完全不透明。', code='invalid_render')
        return rgba.tobytes()


def eligibility(root, row, *, render=False):
    reasons = []
    checks = row.get('review_checks', {})
    if not isinstance(checks, dict):
        reasons.append('review_checks 必须为对象。')
        checks = {}
    if row.get('user_approved') is True:
        reasons.append('暂存条目含未经本工作台记录的通过状态。')
    if row.get('pass_eligible') is not True:
        reasons.append('此候选尚未完成必要核验。')
    blockers = row.get('pass_blockers', [])
    if not isinstance(blockers, list):
        reasons.append('pass_blockers 必须为列表。')
        blockers = []
    for blocker in blockers:
        reasons.append(blocker.get('message', str(blocker)) if isinstance(blocker, dict) else str(blocker))
    verification = row.get('verification', {})
    if not isinstance(verification, dict):
        reasons.append('verification 必须为对象。')
        verification = {}
    if verification.get('agreement') != 'agreement' or not verification.get('agreement_evidence'):
        reasons.append('来源答案与独立结果的一致性未明确通过核验。')
    if verification.get('status') != 'verified':
        reasons.append('答案尚未有明确的独立核验通过记录。')
    if not isinstance(verification.get('proof'), str) or not verification['proof'].strip() or row.get('independently_verified_answer') in (None, ''):
        reasons.append('缺少独立解答或可核验的证明。')
    for name in ('source', 'content', 'answer', 'render'):
        if not isinstance(checks.get(name), dict) or checks[name].get('status') != 'passed':
            reasons.append(f'{name} 核验尚未通过。')
    contract = row.get('scene_contract', {})
    if not isinstance(contract, dict):
        reasons.append('scene_contract 必须为对象。')
        contract = {}
    if contract.get('valid') is not True:
        reasons.append('场景尚未满足当前 SolidGeometry 协议。')
    expected_environment = checks.get('render', {}).get('environment') if isinstance(checks.get('render'), dict) else None
    if isinstance(expected_environment, dict) and expected_environment:
        actual_environment = {key.lower(): value for key, value in environment().items()}
        if any(actual_environment.get(key.lower()) != value for key, value in expected_environment.items()):
            reasons.append('当前 Python 或绘图库版本与冻结预览环境不一致，请通过原题审核启动器选择匹配环境。')
    scene, paths, redraw = None, {}, None
    try:
        cid = candidate_id(row)
        for metadata in ('source_notes', 'source_record'):
            if metadata in row and not isinstance(row[metadata], dict):
                raise ReviewError(metadata + ' 必须为对象。')
        validate_answer(row)
        content_fields = {key: row[key] for key in ('question', 'answer', 'answer_type', 'choices') if key in row}
        if verification.get('candidate_content_sha256') != catalog.digest(content_fields):
            raise ReviewError('题干、答案或选项与独立核验的冻结指纹不一致。', code='audit_content_mismatch')
        if row.get('source_dataset') != 'SOLIDGEO' or not row.get('source_key'):
            raise ReviewError('必须保留 SOLIDGEO 的真实题源和 source_key。')
        paths = payload_paths(root, row)
        baseline = row.get('payload_sha256', {})
        if not isinstance(baseline, dict) or any(baseline.get(name) != catalog.file_hash(path) for name, path in paths.items()):
            raise ReviewError('候选文件与核验时冻结的哈希不一致，须重新核验。', code='audit_payload_mismatch')
        scene = parse_json(paths['scene'].read_text(encoding='utf-8-sig'))
        if set(scene) != catalog.FORMAL_SCENE_FIELDS['SolidGeometry']:
            raise ReviewError('场景字段必须符合当前正式冻结绘图协议。')
        expected_ids = {cid, 'SolidGeo_' + cid} if cid[0].isalpha() else {'SolidGeo_' + cid}
        if scene.get('id') not in expected_ids or contract.get('scene_id', scene.get('id')) != scene.get('id'):
            raise ReviewError('场景身份与候选题不一致。', code='scene_identity_mismatch')
        if scene.get('source_dataset') != row['source_dataset']:
            raise ReviewError('场景与候选题的来源不一致。')
        source = scene.get('source_image')
        if not isinstance(source, str) or '\\' in source or Path(source).is_absolute():
            raise ReviewError('场景来源图路径无效。')
        # Scene-relative ../ is allowed only after resolving to the declared safe payload.
        if (paths['scene'].parent / source).resolve() != paths['original_image'].resolve():
            raise ReviewError('场景来源图与候选记录不一致。')
        renderer = load_renderer(root)
        renderer.validate_scene(scene)
        _pixels(paths['image'].read_bytes())
        from PIL import Image
        with Image.open(paths['original_image']) as original:
            original.verify()
        if render and not reasons:
            with RENDER_LOCK:
                redraw, _ = renderer.image_bytes(scene)
                second, _ = renderer.image_bytes(scene)
            pixels = _pixels(redraw)
            if pixels != _pixels(second):
                raise ReviewError('当前环境下两次重绘像素不一致。', code='nondeterministic_render')
            if pixels != _pixels(paths['image'].read_bytes()):
                raise ReviewError('暂存重绘与当前冻结场景的实际输出像素不一致。', code='render_mismatch')
    except Exception as error:
        reasons.append(str(error))
    return {'eligible': not reasons, 'reasons': list(dict.fromkeys(reasons)),
            'scene': scene, 'paths': paths, 'redraw': redraw}


def package(root, row, formal_id, inspection, candidate_hash):
    """Construct a minimal package; staging scripts and shared deps are not copied."""
    scene = copy.deepcopy(inspection['scene'])
    source = inspection['paths']['original_image']
    suffix = source.suffix.lower()
    if suffix not in ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.tif', '.tiff'):
        raise ReviewError('来源图文件扩展名无效。')
    scene.update(id=formal_id, status='formal_candidate', source_image=f'../../originals/{formal_id}{suffix}')
    record = {name: copy.deepcopy(row[name]) for name in ('source_dataset', 'source_key', 'question', 'answer', 'answer_type')}
    record = {'id': formal_id, **record, 'image': f'image/{formal_id}.png',
              'original_image': f'originals/{formal_id}{suffix}',
              'scene': f'dataset_generator/scenes/{formal_id}.json',
              'script': f'dataset_generator/solid_plot{int(formal_id[5:]):02d}.py'}
    if 'choices' in row:
        record['choices'] = copy.deepcopy(row['choices'])
    source_notes = copy.deepcopy(row.get('source_notes', {}))
    if not isinstance(source_notes, dict):
        raise ReviewError('source_notes 必须为对象。')
    provenance = {}
    if 'provenance' in inspection['paths']:
        provenance = parse_json(inspection['paths']['provenance'].read_text(encoding='utf-8-sig'))
    if not isinstance(provenance, dict):
        raise ReviewError('候选来源说明必须为对象。')
    if not source_notes.get('geometry_notes') and provenance.get('geometry_notes'):
        source_notes['geometry_notes'] = copy.deepcopy(provenance['geometry_notes'])
    source_notes.pop('geometry_notes_file', None)
    source_notes['source_qa_id'] = copy.deepcopy(row.get('source_qa_id', row.get('source_record', {}).get('qa_id')))
    raw_source = row.get('source_record', {})
    source_notes['source_record'] = {name: copy.deepcopy(raw_source[name]) for name in
        ('question', 'choices', 'answer', 'solution', 'image', 'qa_id', 'source') if name in raw_source}
    if 'source_question' in row:
        source_notes['source_record'].setdefault('question', copy.deepcopy(row['source_question']))
    source_notes['source_record'].setdefault('answer', copy.deepcopy(row.get('source_answer')))
    migration = {name: copy.deepcopy(provenance[name]) for name in
        ('historical_scene_sha256', 'historical_source_record_sha256', 'source_image_sha256',
         'historical_redraw_sha256', 'current_scene_sha256', 'current_redraw_sha256',
         'representation_migration', 'renderer') if name in provenance}
    if migration:
        source_notes['drawing_provenance'] = migration
    source_notes['original_review'] = {'candidate_id': candidate_id(row), 'candidate_sha256': candidate_hash,
        'source_answer': copy.deepcopy(row.get('source_answer')),
        'independently_verified_answer': copy.deepcopy(row.get('independently_verified_answer')),
        'verification': copy.deepcopy(row.get('verification')),
        'render_environment': copy.deepcopy(row.get('review_checks', {}).get('render', {}).get('environment')),
        'current_preview_sha256': row.get('payload_sha256', {}).get('image')}
    script = f'''"""Approved frozen SOLIDGEO question {formal_id}."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class {formal_id}:
    def __init__(self):
        self.id = {formal_id!r}
        self.source_dataset = {row['source_dataset']!r}
        self.query = {row['question']!r}
        self.answer = {row['answer']!r}
        self.answer_type = {row['answer_type']!r}
        self.subject = 'SolidGeometry'
{('        self.choices = ' + repr(row['choices']) + chr(10)) if 'choices' in row else ''}        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / {f'{formal_id}.json'!r}

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print({formal_id}().draw()['image_path'])
'''
    artifacts = {'SolidGeometry/' + record['scene']: json_bytes(scene),
                 'SolidGeometry/' + record['script']: script.encode('utf-8'),
                 'SolidGeometry/' + record['image']: inspection['paths']['image'].read_bytes(),
                 'SolidGeometry/' + record['original_image']: source.read_bytes()}
    attribution = source_notes.get('dataset_attribution')
    if isinstance(attribution, str):
        attribution_path = safe_path(root, attribution, must_exist=True)
        if not attribution_path.is_relative_to(Path(root) / 'staging/solidgeo'):
            raise ReviewError('候选来源许可文件必须在其暂存区内。')
        attribution_bytes = attribution_path.read_bytes()
        target = 'provenance/SOLIDGEO_ATTRIBUTION.md'
        target_path = safe_path(root, target)
        if target_path.exists():
            if target_path.read_bytes() != attribution_bytes:
                raise ReviewError('正式来源许可说明与当前候选不一致，不能覆盖。', 409, 'attribution_mismatch')
        else:
            artifacts[target] = attribution_bytes
        source_notes['dataset_attribution'] = {'path': target, 'sha256': hashlib.sha256(attribution_bytes).hexdigest()}
    for relative in artifacts:
        if safe_path(root, relative).exists():
            raise ReviewError(f'正式目标路径已存在，拒绝覆盖：{relative}', 409, 'formal_collision')
    return record, source_notes, artifacts
