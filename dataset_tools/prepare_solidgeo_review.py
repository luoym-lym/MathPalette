"""Prepare the isolated SOLIDGEO review payload, never the formal question bank.

Run with the repository-pinned Python 3.13.9 environment. Source inputs are read
only. Mathematical conclusions come from the independent full-coverage audit,
not from equality with an upstream answer. Unsupported scene contracts remain
blocked; this script does not reconstruct missing 3D geometry.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import platform
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / 'staging/solidgeo'
EXCLUDED = frozenset('1770 1801 1830 1877 1919 1935 1946 1962 1986 2001 2015 2067 2208 2235 2290 2376 2404 2441 2530 2580 2623 2729 2796 2931 3043 3074 3088'.split())
QA_KEYS = frozenset(('question', 'query', 'answer', 'answer_type', 'choices', 'level',
                     'user_approved', 'review_status', 'current', 'answer_verification'))
SCENE_FIELDS = frozenset(('id', 'status', 'subject', 'source_dataset', 'source_image',
    'source_note', 'scene_schema_version', 'protocol_version', 'world_unit', 'points',
    'objects', 'labels', 'constraints', 'ambiguities', 'projection', 'visibility',
    'view', 'dimensions'))
EXPRESSION_IDS = frozenset('1851 1882 1938 1963 2013 2061 2088 2123 2177 2181 2250 2252 2273 2274 2291 2301 2347 2350 2421 2442 3046 3058 3069 3092 3108'.split())
TEXT_IDS = frozenset('2264 2296 2804 2841 2863 3102'.split())
# These are answer-presentation normalizations, backed by the audit's full proof.
ANSWER_NORMALIZATIONS = {'1932': '14/3 m', '2889': '6', '3070': '100.48 dm³'}


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def sha(value):
    if isinstance(value, Path):
        value = value.read_bytes()
    return hashlib.sha256(value).hexdigest()


def bind_payload(row):
    content = {key: row[key] for key in ('question', 'answer', 'answer_type', 'choices') if key in row}
    row['verification']['candidate_content_sha256'] = sha(json.dumps(content, ensure_ascii=False,
        sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8'))
    row['payload_sha256'] = {key: sha(STAGING / row[key]) for key in
        ('original_image', 'image', 'scene', 'drawing_script', 'provenance')}
    row['scene_contract']['scene_id'] = f"SolidGeo_{row['id']}"


def save_rows(rows):
    (STAGING / 'candidates.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False, allow_nan=False) + '\n' for r in rows), encoding='utf-8')


def record_visual_review(path):
    """Record an actual inspection, bound to exact displayed PNG bytes.

    The input must identify inspected candidate IDs, PNG SHA-256 and scope. This
    command performs no inspection and cannot stand in for the reviewer.
    """
    report = read(path)
    rows = [json.loads(line) for line in (STAGING / 'candidates.jsonl').read_text(encoding='utf-8').splitlines() if line]
    lookup = {row['id']: row for row in rows}
    for item in report['records']:
        row = lookup[item['id']]
        if item['png_sha256'] != sha(STAGING / row['image']) or item.get('status') != 'passed' or not item.get('scope'):
            raise ValueError(f"{item['id']}: visual review is missing, failed or stale")
        visual = {'status': 'passed', 'scope': item['scope'], 'png_sha256': item['png_sha256'],
                  'method': item['method'], 'reviewed_at': report['reviewed_at']}
        row['review_checks']['render']['visual_inspection'] = visual
        row['pass_blockers'] = [b for b in row['pass_blockers'] if b['code'] != 'TARGET_VISUAL_REVIEW_PENDING']
        row['pass_eligible'] = not row['pass_blockers']
        provenance = read(STAGING / row['provenance'])
        provenance['target_render']['visual_inspection'] = visual
        write(STAGING / row['provenance'], provenance)
    for row in rows:
        bind_payload(row)
    save_rows(rows)
    manifest = read(STAGING / 'manifest.json')
    manifest['pass_eligible_count'] = sum(row['pass_eligible'] for row in rows)
    manifest['target_visual_reviewed_count'] = sum(row['review_checks']['render'].get('visual_inspection', {}).get('status') == 'passed' for row in rows)
    write(STAGING / 'manifest.json', manifest)
    print(json.dumps({'candidate_count': len(rows), 'eligible': manifest['pass_eligible_count']}))


def clean_qa(value):
    if isinstance(value, dict):
        return {k: clean_qa(v) for k, v in value.items() if k not in QA_KEYS}
    if isinstance(value, list):
        return [clean_qa(v) for v in value]
    return value


def compact_geometry_notes(notes, scene):
    """Keep construction semantics without duplicating frozen render samples."""
    notes = copy.deepcopy(notes)
    legacy = notes.pop('legacy_scene_contract', None)
    # Display coordinates are already frozen in the scene and can be projected
    # from its canonical points. These are not independent construction facts.
    notes.pop('projected_points', None)
    if legacy is None:
        return notes
    notes['legacy_scene_identity'] = {key: legacy[key] for key in
        ('id', 'scene_schema_version', 'protocol_version', 'subject', 'source_dataset', 'world_unit') if key in legacy}
    if legacy.get('projection') and legacy['projection'] != scene.get('projection'):
        notes['legacy_projection'] = legacy['projection']
    if legacy.get('visibility', {}).get('projection_sha256') != scene.get('visibility', {}).get('projection_sha256'):
        notes['legacy_visibility_projection_sha256'] = legacy.get('visibility', {}).get('projection_sha256')
    object_ids = {obj['id'] for obj in scene.get('objects', [])}
    notes['object_representation_mapping'] = []
    dimension_index = 0
    for obj in legacy.get('objects', []):
        item = {key: value for key, value in obj.items() if key not in ('world_points', 'points', 'xy')}
        item['canonical_id'] = obj['id'] if obj['id'] in object_ids else None
        if obj.get('role') == 'dimension':
            item['canonical_id'] = f'migrated_dimension_{dimension_index // 3}'
            dimension_index += 1
        notes['object_representation_mapping'].append(item)
    if legacy.get('constraints') and legacy['constraints'] != scene.get('constraints'):
        notes['legacy_construction_checks'] = legacy['constraints']
    if legacy.get('dimensions'):
        notes['legacy_dimension_binding'] = legacy['dimensions']
    notes['label_identity_mapping'] = 'Label IDs are retained; labels consumed by canonical distance ranges are documented by the legacy dimension binding. Approved offset repairs are recorded separately.'
    notes['render_sample_storage'] = 'Frozen point and curve samples, label text and current anchors, viewport, projection and visibility live only in the canonical scene. Analytic primitives, fold/model evidence, source semantic roles and representation mappings remain here. The original scene SHA-256 is recorded at provenance root.'
    return notes


def canonical_question(qid, question, is_choice):
    if not is_choice:
        return question, None, []
    if qid == '2388':
        # Pictorial options remain in the unchanged diagram, including their labels.
        choices = {letter: f'Diagram labeled {letter} in the supplied image' for letter in 'ABCD'}
        return question.rstrip() + '\n\nChoices:\n' + '\n'.join(f'{k}: {v}' for k, v in choices.items()), choices, ['Pictorial choice references made explicit; the four option diagrams remain unchanged in the image.']
    if qid == '2434':
        start = question.index('$\\begin{array}')
        choices = {'A': 'Front View', 'B': 'Top View', 'C': 'Side View', 'D': 'None of the above'}
        return question[:start].rstrip() + '\n\nChoices:\n' + '\n'.join(f'{k}: {v}' for k, v in choices.items()), choices, ['Existing LaTeX array options converted to the canonical letter-to-content mapping without changing option content.']
    matches = list(re.finditer(r'^\s*([A-D])\.\s*', question, flags=re.MULTILINE))
    if [m.group(1) for m in matches] != list('ABCD'):
        raise ValueError(f'{qid}: cannot recover all four source choices unambiguously')
    choices = {}
    for i, match in enumerate(matches):
        value = question[match.end():matches[i + 1].start() if i + 1 < len(matches) else None].strip()
        if i == 3:
            value = re.sub(r'\s*##\s*$', '', value).rstrip()
        choices[match.group(1)] = value
    q = question[:matches[0].start()].rstrip() + '\n\nChoices:\n' + '\n'.join(f'{k}: {v}' for k, v in choices.items())
    return q, choices, ['Existing A./B./C./D. option labels normalized to Choices: A:/B:/C:/D:; option contents preserved; trailing source ## delimiter removed.']


def independent_answer(qid, active, audit):
    result = audit.get('independently_expected_result')
    content = audit.get('content_audit_record', {})
    if result is None:
        result = content.get('independent_result')
    proof = audit.get('independent_proof') or content.get('proof')
    if (not isinstance(result, (str, int, float)) or not proof or audit['math_verdict'] != 'pass'
            or audit.get('answer_verdict') not in ('pass', 'pass_mathematical_content')
            or audit.get('final_result_verdict') != 'pass' or audit.get('source_integrity') != 'pass'):
        raise ValueError(f'{qid}: no separately justified answer and proof')
    is_choice = active['answer_type'] == 'choice'
    result = str(result)
    answer = ANSWER_NORMALIZATIONS.get(qid, result)
    if is_choice:
        match = re.fullmatch(r'([A-Z])(?::.*)?', result, flags=re.DOTALL)
        if match is None:
            raise ValueError(f'{qid}: independent answer has no unambiguous option letter: {result!r}')
        answer, kind = match.group(1), 'choice'
    elif qid in EXPRESSION_IDS:
        kind = 'expression'
    elif qid in TEXT_IDS:
        kind = 'text'
    else:
        kind = 'number'
    return answer, kind, result, proof


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prepare_helpers(source):
    folder = STAGING / 'shared'
    folder.mkdir(parents=True, exist_ok=True)
    inputs = {'nets': ('nets/renderer.py', 'def metrics'),
              'views': ('views/renderer.py', 'def bbox'),
              'special': ('special/support.py', 'def bbox')}
    result = {}
    for batch, (name, stop) in inputs.items():
        original = (source / name).read_text(encoding='utf-8')
        text = original[:original.index(stop)]
        # Rendering never needs the source question bank or constructors.
        text = '\n'.join(line for line in text.splitlines() if not line.startswith(('ROOT=', 'SOURCE='))) + '\n'
        target = folder / f'{batch}_renderer.py'
        target.write_text('"""Frozen preview-only renderer; not a SolidGeometry contract validator."""\n' + text, encoding='utf-8')
        result[batch] = {'upstream_renderer': name, 'upstream_sha256': sha(source / name),
                         'extraction': 'Imports and original pure rendering function only; construction and source-bank dependency removed.',
                         'preview_renderer_sha256': sha(target)}
    runtime = '''"""Read-only scene reproduction for isolated review candidates."""
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[3]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def draw(scene_path, output_path, renderer):
    scene_path, output_path = Path(scene_path), Path(output_path)
    if output_path.suffix.lower() not in ('.png', '.svg'):
        raise ValueError('Output must be PNG or SVG')
    if output_path.resolve().is_relative_to(ROOT) and not output_path.resolve().is_relative_to(ROOT / '.runtime'):
        raise ValueError('Write reproductions under .runtime or outside the repository')
    scene = json.loads(scene_path.read_text(encoding='utf-8'))
    vector = output_path.suffix.lower() == '.svg'
    if renderer == 'SolidGeometry':
        module = load('_solidgeo_current', ROOT / 'SolidGeometry/dataset_generator/common_renderer.py')
        data = module.image_bytes(scene, vector=vector)[0]
    else:
        module = load('_solidgeo_' + renderer, Path(__file__).with_name(renderer + '_renderer.py'))
        if renderer == 'nets':
            data = module.image_bytes(scene, 'svg' if vector else 'png')
        elif renderer == 'special':
            data = module.render(scene, vector=vector)[0]
        else:
            data = module.render(scene, vector=vector)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)
    return str(output_path)
'''
    (folder / 'runtime.py').write_text(runtime, encoding='utf-8')
    return result


def payload_script(batch, canonical=False):
    renderer = 'SolidGeometry' if canonical or batch in ('blocks', 'cylinders') else batch
    return f'''"""Reproduce this candidate; no writes occur on import."""
from pathlib import Path
import importlib.util

HERE = Path(__file__).resolve().parent

def draw(output_path=None):
    helper = HERE.parents[1] / 'shared/runtime.py'
    spec = importlib.util.spec_from_file_location('_candidate_runtime', helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = output_path or HERE.parents[3] / '.runtime/solidgeo-reproduced' / (HERE.name + '.png')
    return module.draw(HERE / 'scene.json', output, {renderer!r})

if __name__ == '__main__':
    import sys
    print(draw(sys.argv[1] if len(sys.argv) > 1 else None))
'''


def image_metrics(data, historical):
    import numpy as np
    from PIL import Image
    now = np.asarray(Image.open(io.BytesIO(data)).convert('RGBA'))
    before = np.asarray(Image.open(io.BytesIO(historical)).convert('RGBA'))
    changed = np.any(now != before, axis=2)
    ys, xs = np.where(np.any(now[:, :, :3] < 250, axis=2))
    bbox = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
    return {'size': [int(now.shape[1]), int(now.shape[0])],
        'opaque': bool((now[:, :, 3] == 255).all()), 'historical_pixels_equal': bool(not changed.any()),
        'changed_pixels': int(changed.sum()), 'changed_pixel_fraction': float(changed.mean()),
        'maximum_channel_delta': int(np.max(np.abs(now.astype(int) - before.astype(int)))),
        'content_bbox_px': bbox, 'long_side_fraction': max(bbox[2] - bbox[0], bbox[3] - bbox[1]) / 768,
        'center_error_px': [abs((bbox[0] + bbox[2]) / 2 - 384), abs((bbox[1] + bbox[3]) / 2 - 384)],
        'minimum_margin_px': min(bbox[0], bbox[1], 768 - bbox[2], 768 - bbox[3])}


def prepare(args):
    os.environ.setdefault('MPLCONFIGDIR', '/tmp/solidgeo-review-mpl')
    import matplotlib
    import numpy
    import PIL
    from answer_schema import validate_answer
    from solidgeo_scene_migration import migrate_scene
    source = args.source.resolve()
    originals = args.originals.resolve() / 'english_single_image_new_clean'
    upstream = read(originals / 'SolidGeo.json')
    manifest = read(source / 'manifest.json')
    active = read(source / 'active_bank/redraw_dataset.json')
    audits = {r['id']: r for r in read(source / 'remaining_audit.json')['records']}
    records = manifest['records']
    ids = {r['id'] for r in records}
    if len(records) != 168 or len(ids) != 168 or ids != set(active) or ids & EXCLUDED:
        raise ValueError('The candidate scope must be exactly the 168 retained IDs, never an excluded ID')
    if set((STAGING / 'candidates').glob('*')) and not args.rebuild:
        raise ValueError('Payload exists. Use --rebuild only before review state exists.')
    for state_path in (STAGING / 'review_state.json', ROOT / '.runtime/solidgeo-original-review/state.json'):
        if args.rebuild and state_path.exists() and read(state_path).get('reviews'):
            raise ValueError('Do not rebuild over saved review decisions')
    env = {'python': platform.python_version(), 'matplotlib': matplotlib.__version__,
           'numpy': numpy.__version__, 'pillow': PIL.__version__}
    expected = {'python': '3.13.9', 'matplotlib': '3.11.2', 'numpy': '2.5.3', 'pillow': '12.3.0'}
    if env != expected:
        raise ValueError(f'Use the exact target environment {expected}; found {env}')
    helpers = prepare_helpers(source)
    renderer = load_module('_solidgeo_review_current', ROOT / 'SolidGeometry/dataset_generator/common_renderer.py')
    rows = []
    for entry in records:
        qid, batch = entry['id'], entry['batch']
        record, audit = read(source / entry['record']), audits[qid]
        old_scene = read(source / entry['scene'])
        source_record = active[qid]['source_record']
        if source_record != record['source']:
            raise ValueError(f'{qid}: retained source records disagree')
        if source_record != upstream.get(qid):
            raise ValueError(f'{qid}: source question/answer differs from the original retained upstream record')
        folder = STAGING / 'candidates' / qid
        folder.mkdir(parents=True, exist_ok=True)
        source_bytes = (source / entry['source_image']).read_bytes()
        historical_bytes = (source / entry['redraw']).read_bytes()
        if sha(source_bytes) != entry['source_image_sha256'] or sha(historical_bytes) != entry['render_sha256']:
            raise ValueError(f'{qid}: input image hash changed')
        local_original = (source / entry['scene']).with_name('original.jpg')
        if local_original.read_bytes() != source_bytes:
            raise ValueError(f'{qid}: original copy does not match the source image')
        original_source_path = originals / source_record['image'][0].replace('\\', '/')
        if original_source_path.read_bytes() != source_bytes:
            raise ValueError(f'{qid}: original image differs from the original retained upstream image')
        (folder / 'original.jpg').write_bytes(source_bytes)
        migration = migrate_scene(old_scene, batch) if batch not in ('blocks', 'cylinders') else None
        migrated = migration is not None and migration['scene'] is not None
        scene = clean_qa(migration['scene'] if migrated else {k: v for k, v in old_scene.items() if k in SCENE_FIELDS})
        scene.update(id=f'SolidGeo_{qid}', source_dataset='SOLIDGEO', source_image='original.jpg', status='review_candidate')
        if 'source_note' not in scene:
            scene['source_note'] = 'Retained SOLIDGEO source image; legacy drawing contract retained where not compatible with the current SolidGeometry renderer.'
        geometry_notes = clean_qa({k: v for k, v in old_scene.items() if k not in SCENE_FIELDS and k not in QA_KEYS})
        if migrated:
            geometry_notes.update(clean_qa(migration['geometry_notes']))
        elif migration:
            geometry_notes['migration_blockers'] = migration['blockers']
        geometry_notes = compact_geometry_notes(geometry_notes, scene)
        write(folder / 'scene.json', scene)
        valid, error, checks = False, None, []
        try:
            checks = renderer.validate_scene(scene)
            valid = True
        except (ValueError, KeyError, TypeError, IndexError) as exc:
            error = f'{type(exc).__name__}: {exc}'
        (folder / 'draw.py').write_text(payload_script(batch, canonical=valid or migrated), encoding='utf-8')
        blockers = copy.deepcopy(migration['blockers']) if migration and not migrated else []
        render_evidence = {'status': 'blocked', 'current_renderer_valid': valid, 'validator_error': error,
            'environment': env, 'historical_environment': record.get('dependencies', {}),
            'historical_png_sha256': sha(historical_bytes), 'checks': checks}
        preview_bytes = historical_bytes
        if valid:
            try:
                first, checks_first = renderer.image_bytes(scene)
                second, _ = renderer.image_bytes(scene)
                svg_first, _ = renderer.image_bytes(scene, vector=True)
                svg_second, _ = renderer.image_bytes(scene, vector=True)
                metrics = image_metrics(first, historical_bytes)
                render_evidence.update(status='passed', png_bytes_repeat_equal=first == second,
                    svg_bytes_repeat_equal=svg_first == svg_second, metrics=metrics, checks=checks_first,
                    mathematical_geometry_and_visibility_semantics_unchanged=True,
                    coordinate_representation_changed=migrated,
                    change_reason='Repository-pinned target environment preview; any representation mapping is documented separately and preserves mathematical geometry and frozen visibility semantics. Historical pixel equality is not assumed.',
                    visual_inspection={'status': 'pending', 'scope': 'Target preview must be inspected before Pass eligibility.'})
                preview_bytes = first
                if migrated:
                    # Legacy preview imports can change rcParams; isolate them so
                    # they cannot contaminate current-renderer reproducibility.
                    with matplotlib.rc_context():
                        legacy = load_module('_preview_' + batch, STAGING / f'shared/{batch}_renderer.py')
                        legacy_bytes = (legacy.image_bytes(old_scene) if batch == 'nets' else
                                        legacy.render(old_scene)[0] if batch == 'special' else legacy.render(old_scene))
                    render_evidence['same_environment_legacy_comparison'] = image_metrics(first, legacy_bytes)
                if not first == second or not svg_first == svg_second:
                    blockers.append({'code': 'RENDER_NONDETERMINISTIC', 'message': 'Two renders differ in the pinned target environment.'})
                if (metrics['size'] != [768, 768] or not metrics['opaque'] or
                        metrics['minimum_margin_px'] < 38.4 or max(metrics['center_error_px']) > 2 or
                        abs(metrics['long_side_fraction'] - .86) > .01):
                    blockers.append({'code': 'TARGET_LAYOUT_FAILED', 'message': 'Target preview does not meet the frozen canvas, margin, centering or occupancy guard.', 'evidence': metrics})
                blockers.append({'code': 'TARGET_VISUAL_REVIEW_PENDING', 'message': 'Target-environment preview awaits actual visual inspection; historical visual review is not substituted.'})
            except (ValueError, KeyError, TypeError) as exc:
                error = f'{type(exc).__name__}: {exc}'
                render_evidence.update(status='blocked', render_error=error)
                blockers.append({'code': 'TARGET_RENDER_FAILED', 'message': error})
        else:
            blockers.append({'code': 'CURRENT_SOLID_RENDERER_INCOMPATIBLE', 'message': error})
            for issue in audit.get('all_issues', []):
                if issue.get('code') in {'MISSING_SOLID_SCENE_FIELDS', 'WRONG_SCENE_SUBJECT', 'UNSUPPORTED_SCENE_SCHEMA',
                    'NON_3D_WORLD_POINTS', 'NET_SOLID_SCENE_FREEZE_MISSING', 'NONVALIDATING_FROZEN_CONSTRAINT_RESULTS',
                    'DIMENSION_WORLD_BINDING_MISSING', 'CONTENT_SOLID_READY_COMPLIANCE_1', 'VISIBILITY_HASH_FORMAT_INCOMPATIBLE'}:
                    blockers.append({'code': issue['code'], 'message': issue.get('evidence', ''),
                                     'required_action': issue.get('recommended_fix', ''), 'rule': issue.get('rule', '')})
        (folder / 'redraw.png').write_bytes(preview_bytes)
        render_evidence['current_png_sha256'] = sha(preview_bytes)
        answer, kind, expected_result, proof = independent_answer(qid, active[qid], audit)
        question, choices, transforms = canonical_question(qid, active[qid]['question'], kind == 'choice')
        relative = f'candidates/{qid}'
        visual = copy.deepcopy(audit.get('visual_inspection') or audit.get('content_audit_record', {}).get('visual_inspection', {}))
        for key in list(visual):
            if isinstance(visual[key], str) and visual[key].startswith(('/workspace/', '/tmp/')):
                del visual[key]
        verification = {'status': 'verified', 'origin': 'historical_independent_audit_2026-10-11',
            'new_review': False, 'method': 'Independent mathematical derivation plus separate source/redraw visual audit.',
            'proof': proof, 'independently_expected_result': expected_result,
            'agreement': 'agreement', 'agreement_evidence': {
                'basis': 'Historical independent audit explicitly reports source/current mathematical answer and final result pass; original source fields retained. This is not a string-equality inference.',
                'answer_verdict': audit['answer_verdict'], 'final_result_verdict': audit['final_result_verdict'],
                'source_integrity': audit['source_integrity']},
            'evidence': {'audit_file_sha256': sha(source / 'remaining_audit.json'), 'audit_record_id': qid,
                'math_verdict': audit['math_verdict'], 'answer_verdict': audit['answer_verdict'],
                'source_answer_string_equality_used_as_verification': False}}
        provenance = {'source_dataset': 'SOLIDGEO', 'source_key': qid, 'source_qa_id': entry.get('source_qa_id'),
            'geometry_notes': geometry_notes, 'historical_scene_sha256': entry['scene_sha256'],
            'historical_source_record_sha256': sha(source / entry['record']),
            'source_image_sha256': sha(source_bytes), 'historical_redraw_sha256': sha(historical_bytes),
            'current_scene_sha256': sha(folder / 'scene.json'), 'current_redraw_sha256': sha(preview_bytes),
            'representation_migration': {'removed_scene_qa_fields': sorted(set(old_scene) & QA_KEYS),
                'source_dataset_normalized_from': old_scene.get('source_dataset'),
                'mathematical_geometry_and_visibility_semantics_changed': False,
                'coordinate_representation_changed': migrated,
                'legacy_contract_reconstructed': False,
                'scene_representation_changes': migration['changes'] if migration else [],
                'canonical_question_transformations': transforms},
            'renderer': {'current': {'renderer': 'SolidGeometry/dataset_generator/common_renderer.py',
                'renderer_sha256': sha(ROOT / 'SolidGeometry/dataset_generator/common_renderer.py'),
                'protocol_sha256': sha(ROOT / 'SolidGeometry/dataset_generator/protocol.json')} if valid else None,
                'legacy_preview': helpers.get(batch)},
            'target_render': render_evidence}
        write(folder / 'provenance.json', provenance)
        row = {'id': qid, 'candidate_id': qid, 'source_dataset': 'SOLIDGEO', 'source_key': qid,
            'source_qa_id': entry.get('source_qa_id'), 'batch': batch, 'subject': 'SolidGeometry',
            'question': question, 'answer': answer, 'answer_type': kind,
            'source_question': source_record['question'], 'source_answer': source_record['answer'],
            'source_record': source_record, 'independently_verified_answer': answer,
            'verification': verification, 'image': relative + '/redraw.png',
            'original_image': relative + '/original.jpg', 'scene': relative + '/scene.json',
            'drawing_script': relative + '/draw.py', 'provenance': relative + '/provenance.json',
            'paths': {k: f'staging/solidgeo/{relative}/{v}' for k, v in {'original': 'original.jpg',
                'redraw': 'redraw.png', 'scene': 'scene.json', 'draw': 'draw.py', 'provenance': 'provenance.json'}.items()},
            'source_notes': {'dataset_attribution': 'staging/solidgeo/ATTRIBUTION.md',
                'geometry_notes_file': relative + '/provenance.json', 'canonical_question_transformations': transforms,
                'answer_normalization': 'Independent audited conclusion rendered canonically; unmodified source answer and solution retained in source_record.'},
            'review_checks': {'source': {'status': 'passed', 'original_sha256': sha(source_bytes),
                'source_record_preserved': True, 'source_image_bytes_preserved': True,
                'original_upstream_record_and_image_rechecked': True},
                'answer': {'status': 'passed', 'independent': True, 'proof_reference': 'verification.proof'},
                'content': {'status': 'passed', 'origin': 'historical_full_coverage_audit',
                    'question_verdict': audit['question_verdict'], 'image_verdict': audit['image_verdict'],
                    'visual_inspection': visual}, 'render': render_evidence},
            'scene_contract': {'valid': valid, 'renderer': 'SolidGeometry' if valid else f'legacy_{batch}', 'error': error},
            'pass_eligible': not blockers, 'pass_blockers': blockers, 'user_approved': False}
        if choices is not None:
            row['choices'] = choices
        validate_answer(row)
        bind_payload(row)
        rows.append(row)
        print(f'{qid}: {kind}, current scene {valid}, {len(blockers)} blockers', flush=True)
    STAGING.mkdir(parents=True, exist_ok=True)
    save_rows(rows)
    write(STAGING / 'manifest.json', {'schema_version': '1.0.0', 'source_dataset': 'SOLIDGEO',
        'candidate_count': 168, 'candidate_ids': sorted(ids, key=int), 'excluded_ids': sorted(EXCLUDED, key=int),
        'source_manifest_sha256': sha(source / 'manifest.json'), 'historical_audit_sha256': sha(source / 'remaining_audit.json'),
        'original_upstream_record_file_sha256': sha(originals / 'SolidGeo.json'),
        'environment': env, 'formal_bank_modified': False, 'user_approved_count': 0,
        'scene_compatible_count': sum(r['scene_contract']['valid'] for r in rows),
        'pass_eligible_count': sum(r['pass_eligible'] for r in rows),
        'pass_eligibility_note': 'Eligibility is technical readiness for explicit user Pass, never user approval.'})
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path('/workspace/shared/solidgeo_redraw_filtered'))
    parser.add_argument('--originals', type=Path, default=Path('/workspace/shared/solidgeo'))
    parser.add_argument('--rebuild', action='store_true')
    parser.add_argument('--record-visual-review', type=Path,
        help='Record actual reviewer results with exact image hashes; does not perform visual review')
    args = parser.parse_args()
    if args.record_visual_review:
        record_visual_review(args.record_visual_review)
    else:
        prepare(args)
