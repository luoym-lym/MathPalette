"""Conservative representation-only adapters for isolated SOLIDGEO candidates.

No renderer/protocol exceptions, geometry reconstruction, visibility inference,
layout fitting, answer decisions, or approval writes occur here. The caller must
validate and render the returned scene with the ordinary shared renderer. Legacy
construction evidence is retained in geometry_notes, never silently discarded.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import re

import numpy as np


FIELDS = frozenset(('id', 'status', 'subject', 'source_dataset', 'source_image',
    'source_note', 'scene_schema_version', 'protocol_version', 'world_unit',
    'points', 'projection', 'visibility', 'view', 'objects', 'dimensions',
    'labels', 'constraints', 'ambiguities'))
QA_FIELDS = frozenset(('query', 'question', 'answer', 'answer_type', 'choices',
                       'level', 'user_approved', 'current', 'answer_verification'))
IDENTITY_CAMERA = {'kind': 'orthographic', 'matrix': [[1, 0, 0], [0, 1, 0]],
                   'origin': [0, 0, 0], 'offset': [0, 0], 'toward_viewer': [0, 0, 1]}


class MigrationBlocked(ValueError):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def _require(condition, code, message):
    if not condition:
        raise MigrationBlocked(code, message)


def _digest(value, compact=True):
    kwargs = {'sort_keys': True, 'ensure_ascii': False, 'allow_nan': False}
    if compact:
        kwargs['separators'] = (',', ':')
    return hashlib.sha256(json.dumps(value, **kwargs).encode()).hexdigest()


def _same(a, b):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    return a.shape == b.shape and np.allclose(a, b, rtol=0, atol=1e-10)


def _project(camera, xyz):
    return ((np.asarray(xyz, dtype=float) - camera['origin']) @
            np.asarray(camera['matrix'], dtype=float).T + camera['offset'])


def _page_anchor(camera, xy):
    """A label/glyph page anchor, never a reconstructed physical model point."""
    matrix = np.asarray(camera['matrix'], dtype=float)
    return (np.asarray(camera['origin']) +
            np.linalg.pinv(matrix) @ (np.asarray(xy) - camera['offset'])).tolist()


def _base(old, camera, unit, note):
    raw_id = str(old['id'])
    sid = raw_id if re.fullmatch('[A-Za-z][A-Za-z0-9_]*', raw_id) else 'SolidGeo_' + raw_id
    return {'id': sid, 'status': 'review_candidate', 'subject': 'SolidGeometry',
            'source_dataset': old['source_dataset'], 'source_image': old['source_image'],
            'source_note': note, 'scene_schema_version': '1.0.0', 'protocol_version': '1.2.0',
            'world_unit': unit, 'points': {}, 'projection': copy.deepcopy(camera),
            'visibility': {'mode': 'frozen_intervals', 'projection_sha256': _digest(camera),
                'note': 'Only frozen legacy visible/hidden fragments are drawn. No new occlusion decisions; see migration provenance.'},
            'view': copy.deepcopy(old['view']), 'objects': [], 'dimensions': [],
            'labels': [], 'constraints': [], 'ambiguities': copy.deepcopy(old.get('ambiguities', []))}


def _put_points(scene, prefix, values):
    names = []
    for i, value in enumerate(values):
        name = f'{prefix}_{i}'
        _require(name not in scene['points'], 'point_id_collision', name)
        point = np.asarray(value, dtype=float)
        _require(point.shape == (3,) and np.isfinite(point).all(), 'invalid_world_point', name)
        scene['points'][name] = list(value)
        names.append(name)
    return names


def _label(scene, old, anchor):
    item = {'id': old['id'], 'type': 'vertex' if old.get('type', old.get('role')) in ('vertex', 'point') else 'text',
            'text': old['text'], 'anchor': copy.deepcopy(anchor),
            'offset_pt': copy.deepcopy(old.get('offset_pt', [0, 0]))}
    for key in ('ha', 'va'):
        if key in old:
            item[key] = old[key]
    scene['labels'].append(item)


def _line(scene, old, points, role, visibility='visible'):
    item = {'id': old['id'], 'type': 'segment' if len(points) == 2 else 'polyline',
            'points': points, 'role': role, 'visibility': visibility}
    _require(old.get('linestyle', 'solid') in ('solid', 'dashed'),
             'unsupported_linestyle', old['id'])
    _require(isinstance(old.get('dashed', False), bool), 'invalid_dash_flag', old['id'])
    dashed = old.get('dashed', False) or old.get('linestyle') == 'dashed'
    if dashed and visibility == 'visible':
        _require(role == 'auxiliary', 'visible_physical_dashed_line',
                 f"{old['id']} ({old.get('role')}) has dashed style but visible physical geometry; no hidden visibility may be inferred.")
        item['linestyle'] = 'dashed'
    scene['objects'].append(item)


def _dimensions(scene, old, kind, embed):
    """Replace already-frozen Plane02 strokes by equivalent canonical dimensions."""
    metadata = old.get('dimensions', [])
    raw_objects = [o for o in old['objects'] if o.get('role') == 'dimension']
    _require(len(raw_objects) == len(metadata) * 3, 'dimension_binding_missing',
             'Legacy distance strokes do not bind one-to-one to the saved distance ranges.')
    consumed_labels = set()
    units_per_pt = (scene['view']['xlim'][1] - scene['view']['xlim'][0]) / 691.2 * 100 / 72
    for i, dim in enumerate(metadata):
        if kind == 'nets':
            ends = np.asarray(dim['endpoints'], float)
            shown = np.asarray(dim['dimension_endpoints'], float)
            xyz = [embed(p) for p in ends]
            projected = ends
            old_label_xy = lambda lab: old['points'][lab['anchor']]
        else:
            xyz = copy.deepcopy(dim['world_endpoints'])
            projected = _project(scene['projection'], xyz)
            shown = projected + dim['projection_offset']
            old_label_xy = lambda lab: _project(scene['projection'], lab['world_anchor'])
        shift = shown[0] - projected[0]
        _require(_same(shown[1] - projected[1], shift), 'dimension_offset_changed', str(i))
        candidates = [lab for lab in old['labels'] if lab['id'] not in consumed_labels
                      and _same(old_label_xy(lab), shown.mean(axis=0))
                      and ('text' not in dim or lab['text'] == dim['text'])]
        _require(len(candidates) == 1, 'dimension_label_binding_missing', str(i))
        lab = candidates[0]
        expected_lines = [(projected[0], shown[0]), (projected[1], shown[1]), (shown[0], shown[1])]
        for obj, expected in zip(raw_objects[i * 3:i * 3 + 3], expected_lines):
            actual = ([old['points'][p] for p in obj['points']] if kind == 'nets'
                      else _project(scene['projection'], obj['world_points']))
            _require(_same(actual, expected), 'dimension_strokes_changed', obj['id'])
        consumed_labels.add(lab['id'])
        value = float(np.linalg.norm(np.asarray(xyz[1]) - xyz[0]))
        if 'value' in dim:
            _require(math.isclose(value, dim['value'], rel_tol=1e-8, abs_tol=1e-8),
                     'dimension_world_value_changed', str(i))
        if 'world_length' in dim:
            _require(math.isclose(value, dim['world_length'], rel_tol=1e-8, abs_tol=1e-8),
                     'dimension_world_value_changed', str(i))
        item = {'id': f'migrated_dimension_{i}', 'type': 'distance', 'points': xyz,
                'value': value, 'unit': scene['world_unit'], 'decimals': 0,
                'text': lab['text'], 'offset_pt': (shift / units_per_pt).tolist(),
                'label_offset_pt': copy.deepcopy(lab.get('offset_pt', [0, 0])),
                'basis': 'Legacy frozen distance endpoint binding; displayed source text is preserved verbatim, including symbolic unknowns. Drawing-only lengths are not asserted as givens.'}
        for key in ('ha', 'va'):
            if key in lab:
                item[key] = lab[key]
        scene['dimensions'].append(item)
    return consumed_labels


def _nets(old, notes, changes):
    _require('planar net' in old.get('representation', ''), 'net_representation_missing',
             'The source does not explicitly identify the drawing as a planar net.')
    components = old.get('solid_components', [])
    _require(len(components) <= 1, 'multiple_net_projections', 'Several independently projected solids need explicit panel support.')
    camera = copy.deepcopy(components[0]['projection'] if components else IDENTITY_CAMERA)
    if components:
        matrix = np.asarray(camera['matrix'], float)
        _require(_same(matrix[:, [0, 2]], np.eye(2)), 'mixed_panel_scale',
                 'The net is drawn at unit scale, but its solid panel projection scales x/z differently. One global camera cannot preserve both world scales without changing geometry.')
        def embed(xy):
            return [xy[0] - camera['offset'][0] + camera['origin'][0],
                    camera['origin'][1], xy[1] - camera['offset'][1] + camera['origin'][2]]
        notes['planar_embedding'] = 'Net (x,y) embeds isometrically in the world x/z plane after a layout translation; the existing solid world coordinates and camera remain unchanged.'
    else:
        def embed(xy):
            return [*xy, 0]
        notes['planar_embedding'] = 'Literal unfolded net coordinates (x,y) become (x,y,0), with identity orthographic projection. This is the flat sheet, not an inferred folded solid. Existing fold frames and dimensions remain in provenance.'
    units = {d['unit'] for d in old.get('dimensions', []) if d.get('unit')}
    _require(len(units) <= 1, 'mixed_units', 'Legacy dimensions use inconsistent world units.')
    scene = _base(old, camera, next(iter(units), 'legacy net units'), notes['planar_embedding'])
    scene['points'] = {key: embed(value) for key, value in old['points'].items()}
    if components:
        component = components[0]
        _require(component.get('visibility', {}).get('mode') == 'frozen_intervals',
                 'visibility_missing', 'The solid panel has no frozen visibility record.')
        for key, point in component['world_points'].items():
            scene['points'][component['id'] + '_' + key] = copy.deepcopy(point)
    for obj in old['objects']:
        role = obj.get('role')
        if role == 'dimension':
            continue
        if role == 'visible_solid_edge':
            component = components[0]
            _require(obj.get('solid_component') == component['id'], 'solid_binding_missing', obj['id'])
            names = [component['id'] + '_' + key for key in obj['world_points']]
            xyz = [scene['points'][key] for key in names]
            _require(_same(_project(camera, xyz), [old['points'][key] for key in obj['points']]),
                     'projected_coordinates_changed', obj['id'])
            _require(obj['world_points'] in component['visibility']['visible_edges'],
                     'visibility_binding_missing', obj['id'])
            _line(scene, obj, names, 'edge')
        elif obj['type'] == 'polygon':
            _require(role == 'source_semantic_shading' and str(obj['fill']).upper() == '#E6E6E6',
                     'unsupported_net_fill', obj['id'])
            scene['objects'].append({'id': obj['id'], 'type': 'face', 'points': copy.deepcopy(obj['points']),
                'role': 'region', 'visibility': 'visible', 'semantic_fill_reason': 'Source semantic shading preserved.'})
        else:
            _require(obj['type'] == 'segment' and role in ('boundary', 'fold_edge', 'net_edge', 'source_direction_arrow'),
                     'unsupported_net_object', f'{obj["id"]}: {role}')
            canonical_role = 'auxiliary' if role in ('fold_edge', 'source_direction_arrow') else 'edge'
            _line(scene, obj, copy.deepcopy(obj['points']), canonical_role)
    consumed = _dimensions(scene, old, 'nets', embed)
    for lab in old['labels']:
        if lab['id'] not in consumed:
            _label(scene, lab, lab['anchor'])
    changes.extend(['Embed explicitly planar net isometrically; preserve folded-model evidence in provenance.',
                    'Map existing boundary/fold/glyph roles; dashed fold marks remain visible auxiliary marks, never hidden edges.',
                    'Bind frozen distance strokes and text to canonical dimensions without fitting or moving the view.'])
    return scene


SPECIAL_ROLES = {'edge': 'edge', 'marked_point': 'given_point', 'semantic_region': 'region',
    'silhouette': 'silhouette', 'cut_section': 'section', 'circular_rim': 'edge',
    'cylinder_tangent_generator': 'silhouette', 'sphere_silhouette': 'silhouette',
    'planar_polygon': 'edge', 'planar_circle': 'edge', 'semantic_planar_region': 'region',
    'ribbon_boundary': 'edge', 'given_rotation_axis': 'auxiliary', 'rotation_axis': 'auxiliary',
    'motion_glyph': 'auxiliary', 'roll_path_square': 'auxiliary', 'roll_arrow': 'auxiliary',
    'bow_glyph': 'auxiliary', 'source_ear_mark': 'auxiliary', 'source_mouth_mark': 'auxiliary',
    'source_ear_stalk': 'auxiliary', 'source_muzzle_mark': 'auxiliary'}


def _special(old, notes, changes):
    camera = old['projection']
    _require(old.get('visibility', {}).get('mode') == 'frozen_intervals', 'visibility_missing', 'No frozen visibility.')
    _require(old['visibility'].get('projection_sha256') in (_digest(camera), _digest(camera, False)),
             'stale_legacy_visibility', 'Legacy projection digest does not bind its frozen visibility.')
    scene = _base(old, camera, old['world_unit'],
                  'Representation migration of frozen world coordinates and projection. Source planar profiles/glyphs remain planar; no new solid reconstruction or visibility inference.')
    for obj in old['objects']:
        if obj['role'] == 'dimension':
            continue
        _require(obj['role'] in SPECIAL_ROLES, 'unsupported_special_role', f"{obj['id']}: {obj['role']}")
        role = SPECIAL_ROLES[obj['role']]
        refs = _put_points(scene, obj['id'] + '_world', obj['world_points'])
        if obj['type'] == 'fill':
            scene['objects'].append({'id': obj['id'], 'type': 'face', 'points': refs, 'role': 'region',
                'visibility': obj['visibility'], 'semantic_fill_reason': 'Frozen source semantic region, not decorative lighting.'})
        elif obj['type'] == 'point':
            _require(len(refs) == 1, 'point_arity', obj['id'])
            scene['objects'].append({'id': obj['id'], 'type': 'point', 'point': refs[0],
                                    'role': 'given_point', 'visibility': obj['visibility']})
        else:
            _require(obj['type'] == 'polyline', 'unsupported_special_object', obj['id'])
            _line(scene, obj, refs, role, obj['visibility'])
    consumed = _dimensions(scene, old, 'special', None)
    for lab in old['labels']:
        if lab['id'] not in consumed:
            _label(scene, lab, lab['world_anchor'])
    changes.extend(['Map existing world_points/world_anchor to canonical points/anchor; all samples, coordinates and visibility values remain frozen.',
                    'Legacy analytic/model/parameter records and construction-check results move intact to provenance; no mathematical re-verification is claimed.',
                    'Rebind unchanged projection to the canonical JSON digest encoding.'])
    return scene


def _views(old, notes, changes):
    solids = old.get('solids', [])
    _require(bool(solids), 'missing_world_model',
             'Only frozen 2D projection panels are available; no underlying 3D model, camera or bound visibility exists. Lifting screen XY to z=0 would invent solid semantics.')
    unbound = [o for o in old['objects'] if 'world_points' not in o and o.get('role') != 'view_direction']
    _require(not unbound, 'unbound_physical_projection',
             'Physical projection objects lack world/visibility bindings: ' + ', '.join(f"{o['id']}:{o.get('role')}" for o in unbound))
    camera = copy.deepcopy(solids[0]['projection'])
    _require(_same(np.asarray(camera['matrix'])[:, [0, 2]], np.eye(2)), 'unsupported_view_embedding',
             'No unchanged x/z page basis for auxiliary glyphs and panel translations.')
    for solid in solids:
        local = solid['projection']
        _require(_same(local['matrix'], camera['matrix']) and _same(local['origin'], camera['origin'])
                 and _same(local['toward_viewer'], camera['toward_viewer']), 'incompatible_panel_projection',
                 'Independent panel cameras differ by more than translation.')
        vis = solid.get('visibility', {})
        _require(vis.get('mode') == 'frozen_intervals' and vis.get('projection_sha256') in (_digest(local), _digest(local, False)),
                 'stale_legacy_visibility', 'A solid panel has missing or stale visibility binding.')
    scene = _base(old, camera, old.get('world_unit', 'legacy model units'),
                  'Existing 3D panel models and frozen visibility fragments are retained. Page-only direction glyphs and label anchors are explicitly display annotations; no missing physical world geometry is fabricated.')
    translations = []
    for obj in old['objects']:
        if 'world_points' not in obj:
            refs = _put_points(scene, obj['id'] + '_page_glyph', [_page_anchor(camera, p) for p in obj['xy']])
            _line(scene, obj, refs, 'auxiliary')
            continue
        xyz = np.asarray(obj['world_points'], float)
        interval = obj.get('parameter_interval')
        _require(xyz.shape == (2, 3) and isinstance(interval, list) and len(interval) == 2
                 and 0 <= interval[0] < interval[1] <= 1, 'invalid_frozen_interval', obj['id'])
        clipped = np.asarray([xyz[0] + t * (xyz[1] - xyz[0]) for t in interval])
        matches = []
        for index, solid in enumerate(solids):
            if not _same(_project(solid['projection'], clipped), obj['xy']):
                continue
            bindings = [v for v in solid['visibility'].get('intervals', [])
                        if _same(v.get('points', []), xyz) and v.get('interval') == obj.get('parameter_interval')]
            if bindings and len({v['visibility'] for v in bindings}) == 1:
                matches.append((index, bindings[0]['visibility']))
        _require(len(matches) == 1, 'world_visibility_binding_missing',
                 f"{obj['id']} has no unique unchanged world/camera/visibility fragment.")
        index, visibility = matches[0]
        delta = np.asarray(solids[index]['projection']['offset']) - camera['offset']
        shift = np.array([delta[0], 0.0, delta[1]])
        # Changing a panel's page offset to the same rigid world translation is
        # representational only; source-local coordinates remain in provenance.
        world = (clipped + shift).tolist()
        _require(_same(_project(camera, world), obj['xy']), 'projected_coordinates_changed', obj['id'])
        refs = _put_points(scene, obj['id'] + '_world', world)
        _require(obj.get('role') in ('visible_cube_edge', 'visible_union_edge'),
                 'unsupported_view_world_role', f"{obj['id']}: {obj.get('role')}")
        _line(scene, obj, refs, 'edge', visibility)
        if np.any(shift):
            translations.append({'object_id': obj['id'], 'solid_index': index, 'rigid_translation': shift.tolist()})
    for lab in old['labels']:
        _label(scene, lab, _page_anchor(camera, lab['xy']))
    notes['page_annotations'] = 'Legacy screen-space labels and view-direction arrows use a canonical page-plane anchor only. These anchors are not evidence of physical 3D points or added geometric constraints.'
    if translations:
        notes['panel_rigid_translations'] = translations
    changes.extend(['Restore frozen world edges from their unique saved per-solid camera/visibility bindings; exact projected XY checked.',
                    'Preserve label and direction-glyph page positions as explicit annotations.',
                    'For identical cameras with separate panel offsets, record the equivalent rigid world translation; no rotation, scaling or shape change.'])
    return scene


def _approved_label_layout(scene, old, batch, notes, changes):
    # These two bounded page-offset repairs were explicitly authorized after
    # unchanged migrations exposed collisions under the current layout checks.
    fixes = {('nets', '2198'): ('t3', 'D', [-12, 8], [-12, 12]),
             ('special', '2878'): ('l23', 'M', [-5, -21], [-5, -23])}
    qid = str(old['id']).removeprefix('SolidGeo_')
    fix = fixes.get((batch, qid))
    if fix is None:
        return
    label_id, text, before, after = fix
    labels = [lab for lab in scene['labels'] if lab['id'] == label_id]
    _require(len(labels) == 1 and labels[0]['text'] == text
             and labels[0]['offset_pt'] == before, 'label_repair_source_changed',
             f'{qid}:{label_id} no longer matches the specifically authorized offset repair.')
    labels[0]['offset_pt'] = copy.deepcopy(after)
    reason = 'Remove label-line collision exposed by current strict layout validation; preserve anchor, text, geometry, projection and frozen visibility.'
    notes['authorized_label_layout_repairs'] = [{'label_id': label_id,
        'text': text, 'before_offset_pt': before, 'after_offset_pt': after,
        'anchor_unchanged': True, 'reason': reason}]
    changes.append(f'Authorized page-offset-only repair {label_id}: {before} -> {after}. {reason}')


def migrate_scene(scene, batch):
    """Return {scene, changes, blockers, geometry_notes}; blocked scenes are None.

    Input is never mutated. Geometry notes include the complete non-QA legacy
    payload needed to trace original semantics, coordinates and visibility.
    This function does not report renderer/layout success or user approval.
    """
    old = copy.deepcopy(scene)
    notes = {'legacy_scene_contract': {k: v for k, v in old.items() if k not in QA_FIELDS},
             'migration_scope': 'Representation only; upstream construction/answer checks do not establish current validation or user approval.'}
    changes = []
    try:
        if batch == 'nets':
            result = _nets(old, notes, changes)
        elif batch == 'special':
            result = _special(old, notes, changes)
        elif batch == 'views':
            result = _views(old, notes, changes)
        else:
            result = {key: copy.deepcopy(value) for key, value in old.items() if key in FIELDS}
        _approved_label_layout(result, old, batch, notes, changes)
        return {'scene': result, 'changes': changes, 'blockers': [], 'geometry_notes': notes}
    except (MigrationBlocked, KeyError, TypeError, ValueError) as error:
        return {'scene': None, 'changes': changes,
                'blockers': [{'code': getattr(error, 'code', 'malformed_legacy_scene'), 'message': str(error)}],
                'geometry_notes': notes}
