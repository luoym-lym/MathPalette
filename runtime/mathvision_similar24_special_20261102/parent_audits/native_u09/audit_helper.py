"""Finite read-only audit. Writes are confined to this helper's directory."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
ROOT = OWN.parents[3]
TASK = ROOT / 'runtime/mathvision_similar24_special_20261102'
UNIT = TASK / 'units/u09_octa_nets'
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key in ('TEMP', 'TMP', 'MPLCONFIGDIR', 'XDG_CACHE_HOME'):
    location = OWN / 'cache' / key
    location.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(location)
sys.dont_write_bytecode = True

def own_path(path):
    if isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Audit write outside own directory blocked')

def writeguard(event, args):
    if event == 'open':
        mode, flags = args[1], args[2]
        if (isinstance(mode, str) and any(x in mode for x in 'wax+')) or (
            isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
        ):
            own_path(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.utime', 'os.truncate'):
        own_path(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        own_path(args[0]); own_path(args[1])
    elif event in ('socket.connect', 'socket.getaddrinfo'):
        raise PermissionError('Network forbidden in this audit')

sys.addaudithook(writeguard)

import json
import hashlib
from datetime import datetime, timezone

def read(path):
    return json.loads(Path(path).read_text('utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def candidates():
    return sorted(p for p in (UNIT / 'Solid166').glob('r*') if p.is_dir() and (p / 'design.json').exists())

def unit_snapshot():
    return {str(p.relative_to(UNIT)).replace('\\', '/'): sha(p)
            for p in UNIT.rglob('*') if p.is_file()}

def baseline():
    target = OWN / 'baseline.json'
    if target.exists():
        raise RuntimeError('Baseline already exists')
    manifests = [read(UNIT / 'read_source_manifest.json'), read(UNIT / 'readonly_execution_source_initial.json')]
    scoped = {}
    for manifest in manifests:
        for name, value in manifest.items():
            expected = value.get('sha256') if isinstance(value, dict) else value
            scoped[name] = {'recorded_sha256': expected, 'audit_start_sha256': sha(ROOT / name)}
    e = read(UNIT / 'eligibility_final.json')
    for item in e.values():
        for key in ('inputs_sha256', 'source_file_checks'):
            for name, value in item[key].items():
                expected = value.get('expected') if isinstance(value, dict) else value
                scoped[name] = {'recorded_sha256': expected, 'audit_start_sha256': sha(ROOT / name)}
    dump(target, {'created_at': datetime.now(timezone.utc).isoformat(), 'unit_files': unit_snapshot(), 'scoped_readonly': scoped})
    print(json.dumps({'baseline_written': True, 'unit_file_count': len(read(target)['unit_files']), 'scoped_count': len(scoped)}))

def raw(start, end, run=None, offset=0, limit=None):
    for p in candidates()[start-1:end]:
        e = next((p / 'tests').glob('quick*/summary.json')).parent
        for n in (1, 2):
            if run and n != run:
                continue
            r = read(e / f'run_{n:02d}_response.json')
            answer = r['choices'][0]['message']['content']
            segment = answer[offset:offset+limit] if limit else answer[offset:]
            print(f'\n===== {p.name} RUN {n} FULL_RAW_CONTENT chars {offset}..{offset+len(segment)} of {len(answer)} =====\n{segment}')

def verify():
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(TASK))
    import publish_batch
    from dataset_tools import catalog
    rows = []
    for p in candidates():
        summary, record, sp = publish_batch.verify_evidence(p)
        e = sp.parent
        design = read(p / 'design.json')
        plugin = read(p / 'plugin.json')
        request = read(e / 'request.json')
        assert summary['requested_runs'] == len(summary['results']) == 2
        assert summary['profile'] == 'quicktest3'
        assert summary['settings']['provider'] == 'mimo'
        assert summary['settings']['model'] == request['model'] == 'mimo-v2.6-flash'
        assert summary['settings']['thinking'] == request['thinking'] == {'type': 'disabled'}
        assert summary['request_body_sha256'] == sha(e / 'request.json')
        assert sha(p / 'design.json') == sha(e / 'design_snapshot.json') == summary['design_sha256']
        assert design['plugin_sha256'] == sha(p / 'plugin.json')
        assert design['created_at'] < min(result['started_at'] for result in summary['results'])
        assert summary['question_record_sha256'] == catalog.digest(record)
        assert summary['dataset_sha256'] == sha(ROOT / summary['branch'] / 'dataset.jsonl')
        assert len(list((p / 'tests').glob('*/summary.json'))) == 1
        assert len(list((p / 'tests').glob('*/request.json'))) == 1
        results = []
        for n, result in enumerate(summary['results'], 1):
            raw_result = read(e / f'run_{n:02d}_response.json')
            assert len(raw_result['choices']) == 1
            choice = raw_result['choices'][0]
            assert choice['finish_reason'] == result['finish_reason'] == 'stop'
            assert choice['message']['content'] == result['answer']
            assert result['request_body_sha256'] == summary['request_body_sha256']
            gate = read(p / 'tests' / f'pre_network_run_{n:02d}.json')
            results.append({'run': n, 'http_status': result['http_status'], 'finish_reason': choice['finish_reason'],
                            'truncated': result['truncated'], 'raw_sha256': sha(e / f'run_{n:02d}_response.json'),
                            'answer_chars': len(result['answer']), 'pre_network_gate': gate})
        rows.append({'variant_id': p.name, 'preset': str(design['expected_wrong_answer']), 'correct_answer': record['answer'],
                     'canonical_verify_evidence': 'passed', 'image_sha256': sha(p / 'candidate.png'),
                     'plugin_sha256': sha(p / 'plugin.json'), 'design_sha256': sha(p / 'design.json'),
                     'request_sha256': sha(e / 'request.json'), 'summary_sha256': sha(sp), 'summary_path': str(sp),
                     'actions': plugin['params']['actions'], 'frozen_before_calls': True,
                     'manual_worker_review': read(p / 'manual_final_review.json'), 'results': results})
    dump(OWN / 'transport_verification.json', rows)
    print(json.dumps({'verified_candidates': len(rows), 'calls': sum(len(x['results']) for x in rows),
                      'unique_pngs': len(set(x['image_sha256'] for x in rows)), 'unique_requests': len(set(x['request_sha256'] for x in rows)),
                      'canonical_helper_sha256': sha(TASK / 'publish_batch.py'),
                      'canonical_helper_matches_previous': sha(TASK / 'publish_batch.py') == sha(ROOT / 'runtime/mathvision_special_20261101/publish_batch.py')}, ensure_ascii=False))

def finish():
    # These are this audit's newly created caches; old unit files remain read-only.
    for name in ('baseline.json', 'transport_verification.json'):
        src = OWN / name
        dst = OWN / 'cache' / name
        if src.exists():
            assert not dst.exists()
            src.rename(dst)
    baseline_data = read(OWN / 'cache/baseline.json')
    verification = read(OWN / 'cache/transport_verification.json')
    sys.path.insert(0, str(ROOT))
    from dataset_tools import catalog
    from PIL import Image
    import ast
    import subprocess

    approvals = read(ROOT / 'provenance/approvals.json')['approvals']
    formal_rows = catalog.rows(ROOT / 'SolidGeometry/dataset.jsonl')
    eligibility = {}
    indices = {name: catalog.rows(ROOT / 'SolidGeometry/special_variant' / name)
               for name in ('accepted_index.jsonl', 'collected_index.jsonl')}
    for qid in ('Solid166', 'Solid240'):
        record = next(row for row in formal_rows if row['id'] == qid)
        current = catalog.digest(catalog.content(ROOT, 'SolidGeometry', record))
        approval = approvals[qid]
        assert current == approval['content_sha256']
        assert approval['reviewer'] == 'user'
        state = {name: [row for row in index if row.get('question_id') == qid]
                 for name, index in indices.items()}
        for name in ('recipes.json', 'collection.json'):
            path = ROOT / 'SolidGeometry/special_variant' / qid / name
            state[name] = read(path) if path.exists() else None
        assert all(not value for value in state.values())
        eligibility[qid] = {'source_dataset': record['source_dataset'], 'correct_answer_unchanged': record['answer'],
                            'approved_at_utc': approval['approved_at_utc'], 'user_approval_current_sha256': current,
                            'approval_is_current': True, 'Special_state': state,
                            'MathVision_no_pass_no_collect': record['source_dataset'] == 'MathVision'}

    qt_ast = ast.parse((ROOT / 'SolidGeometry/workbench/quick_test.py').read_text('utf-8-sig'))
    system_prompt = next(ast.literal_eval(node.value) for node in qt_ast.body
                         if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SYSTEM_PROMPT' for t in node.targets))
    schema = read(ROOT / 'SolidGeometry/workbench/plugin.schema.json')
    context = read(UNIT / 'Solid166/context.json')
    styleable = {o['id'] for o in context['objects'] if o.get('styleable')}
    snap_xy = {tuple(o['xy']) for o in context['snap_points']}
    reference_png = ROOT / 'SolidGeometry/special_variant/Solid203/images/C01.png'
    reference_plugin = ROOT / 'SolidGeometry/special_variant/Solid203/plugins/C01.json'
    assert sha(reference_png) == sha(TASK / 'references/Solid203/C01.png')
    assert sha(reference_plugin) == sha(TASK / 'references/Solid203/C01.json')

    manual = [
        ['1', '4'], ['UNRESOLVED_NO_EDGE_IDENTIFIER', '1'], ['AMBIGUOUS_1_OR_2', '2'],
        ['3', '4'], ['3', '3'], ['2', '5'], ['2', '1'], ['4', '3'], ['3', '5'],
        ['5', 'OTHER_PAIR_1_MEETS_3'], ['MULTIPLE_2_AND_5', '4'], ['4', '4']]
    candidate_reports = []
    for index, p in enumerate(candidates()):
        item = verification[index]
        summary_path = Path(item['summary_path'])
        summary = read(summary_path)
        e = summary_path.parent
        request = read(e / 'request.json')
        plugin = read(p / 'plugin.json')
        assert plugin['plugin_schema_version'] == '1.0.0'
        assert plugin['question_id'] == 'Solid166' and plugin['operation'] == 'C_manual' and plugin['category'] == 'C'
        assert set(plugin) <= {'plugin_schema_version','question_id','category','operation','description','intent','params'}
        assert set(plugin['params']) == {'actions'}
        for action in plugin['params']['actions']:
            if action['type'] == 'set_object_style':
                assert set(action) == {'type','target','color'}
            else:
                assert action['type'] == 'add_point'
                assert set(action) == {'type','id','xy','filled','color','size_pt2','edge_linewidth_pt'}
                assert action['filled'] is True and action['size_pt2'] == 50 and action['edge_linewidth_pt'] == 1
            assert action['color'] in {'#DC2626','#2563EB','#16A34A','#EA580C'}
        assert set(request) == {'model', 'stream', 'thinking', 'messages'}
        assert request['stream'] is False
        assert request['messages'][0] == {'role': 'system', 'content': system_prompt}
        assert summary['reference_quick_test_sha256'] == sha(ROOT / 'SolidGeometry/workbench/quick_test.py')
        assert sha(p / 'candidate.png') == sha(p / 'candidate_repeat.png')
        with Image.open(p / 'candidate.png') as image:
            rgba = image.convert('RGBA')
            assert image.size == (768, 768) and rgba.getextrema()[3] == (255, 255)
            assert hashlib.sha256(b'768x768:RGBA:' + rgba.tobytes()).hexdigest() == summary['pixel_sha256']
        for action in plugin['params']['actions']:
            if action['type'] == 'set_object_style':
                assert action['target'] in styleable
            elif action['type'] == 'add_point':
                assert tuple(action['xy']) in snap_xy
        for n, result in enumerate(summary['results'], 1):
            gate = read(p / 'tests' / f'pre_network_run_{n:02d}.json')
            assert gate['request_index'] == n and gate['source_frozen'] and not gate['credentials_logged']
            assert gate['eligibility']['eligible']
            for key in ('image_sha256', 'design_sha256', 'request_body_sha256'):
                assert gate[key] == summary[key]
            raw_result = read(e / f'run_{n:02d}_response.json')
            assert raw_result['model'] == result['response_model']
        observed = manual[index]
        double_hit = observed == [item['preset'], item['preset']]
        worker = item['manual_worker_review']
        assert worker['double_hit'] == double_hit
        assert worker['actual_calls'] == 2
        candidate_reports.append({k: item[k] for k in ('variant_id','preset','correct_answer','canonical_verify_evidence','image_sha256','plugin_sha256','design_sha256','request_sha256','summary_sha256','summary_path')} | {
            'personally_read_full_raw_responses': True, 'manual_final_values': observed,
            'double_hit': double_hit, 'prior_failure_label_preserved': index < 11,
            'worker_outcome_agrees_with_manual': True, 'exactly_two_HTTP200_stop_nontruncated': True,
            'profile': {'name': 'quicktest3', 'model': 'mimo-v2.6-flash', 'thinking': {'type': 'disabled'}},
            'source_design_plugin_request_pixel_raw_hash_bindings_verified': True,
            'same_frozen_image_both_calls': True, 'repeat_render_png_identical': True,
            'formal_only_question_plus_image_payload': True, 'both_pre_network_gates_valid': True,
            'documented_schema_whitelist_and_existing_object_or_vertex_checks': True,
            'raw_response_sha256': [x['raw_sha256'] for x in item['results']],
            'raw_response_characters': [x['answer_chars'] for x in item['results']]})

    source_final = read(UNIT / 'source_preservation_final.json')
    recorded_checks = {}
    for name, value in source_final['execution_file_hashes'].items():
        recorded_checks[name] = sha(ROOT / name) == value
    for name, value in source_final['all_read_old_evidence_and_current_reference_files'].items():
        expected = value.get('after_sha256', value.get('sha256')) if isinstance(value, dict) else value
        recorded_checks[name] = sha(ROOT / name) == expected
    scoped_now = {}
    for name, value in baseline_data['scoped_readonly'].items():
        actual = sha(ROOT / name)
        scoped_now[name] = {'matches_worker_recorded_sha256': actual == value['recorded_sha256'],
                            'unchanged_during_native_audit': actual == value['audit_start_sha256'], 'sha256': actual}
    unit_now = unit_snapshot()
    assert unit_now == baseline_data['unit_files']
    assert all(row['unchanged_during_native_audit'] for row in scoped_now.values())
    assert all(recorded_checks.values())

    ps_script = r'''[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$cleanup = Get-Content -LiteralPath 'runtime/mathvision_similar24_special_20261102/units/u09_octa_nets/process_cleanup.json' -Raw -Encoding UTF8 | ConvertFrom-Json
$all = Get-CimInstance Win32_Process
$tracked = @($all | Where-Object { $cleanup.tracked_API_and_render_PIDs -contains $_.ProcessId } | Select-Object ProcessId,Name,CommandLine)
$owned = @($all | Where-Object { $_.Name -match '^python(w)?\.exe$' -and $_.CommandLine -like '*mathvision_similar24_special_20261102\units\u09_octa_nets*' } | Select-Object ProcessId,Name,CommandLine)
[pscustomobject]@{ observed_at=[DateTimeOffset]::Now.ToString('o');known_pid_count=$cleanup.tracked_API_and_render_PIDs.Count;current_known_pids=$tracked;exact_unit_python=$owned;read_only=$true } | ConvertTo-Json -Depth 5
'''
    proc = subprocess.run(['powershell', '-NoProfile', '-Command', ps_script], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', check=True)
    process = json.loads(proc.stdout)
    assert not process['current_known_pids'] and not process['exact_unit_python']

    fidelity_rows = []
    descriptions = [
        ('direct_original_edge_pairing', 'Only x and original edge3 are red; directly repeats the current user two-edge comparison method, using a different receiving boundary.'),
        ('direct_original_edge_pairing', 'Only x and original edge4 are red; same two-edge method, receiving location differs from r01 and old edge1 design.'),
        ('direct_original_edge_pairing', 'Only x and original edge2 are red; receiver is a different original upper horizontal boundary.'),
        ('edge_pairing_with_one_true_context_pair', 'Keeps r03 x–2 red comparison; adds true seam1–4 in blue to supply a closure reference.'),
        ('endpoint_method_departure', 'Four colored endpoint dots replace edge coloring. Real blue common vertex and red antipodal pair; departs from the user two-edge method.'),
        ('endpoint_method_departure', 'Four endpoint dots compare x and edge3 through two antipodal-axis classes. Distinct receiver, but endpoint identification is an expanded mechanism.'),
        ('endpoint_method_departure', 'Four endpoint dots compare x and edge2, changing concrete source/receiver vertices from r06.'),
        ('edge_pairing_with_one_true_context_pair', 'Keeps r02 x–4 red comparison and adds verified3–2 blue seam; adds closure information, not color-only repetition.'),
        ('endpoint_method_departure', 'Three endpoint dots encode x–1 with a common blue vertex and a red antipodal comparison; a different method from edge coloring.'),
        ('edge_pairing_with_one_true_context_pair', 'Keeps r01 x–3 red and adds true1–4 seam in blue; enlarges the simple reference.'),
        ('edge_pairing_with_one_true_context_pair', 'x–1 red plus true3–2 seam blue; receiver differs from r08 but context is the same.'),
        ('edge_pairing_with_three_true_context_pairs', 'x–4 red plus blue3–2, green upper-flap closure and orange lower-flap closure: eight original edges in four groups. Considerably expands the user two-red-edge reference.')]
    for p, (classification, description) in zip(candidates(), descriptions):
        actions = read(p / 'plugin.json')['params']['actions']
        fidelity_rows.append({'variant_id': p.name, 'native_png_actually_viewed': True, 'classification': classification,
                              'action_count': len(actions), 'new_point_count': sum(a['type'] == 'add_point' for a in actions),
                              'new_line_count': sum(a['type'] == 'add_line' for a in actions),
                              'recolored_original_edges': [a['target'] for a in actions if a['type'] == 'set_object_style'],
                              'colors': sorted({a['color'] for a in actions}), 'description': description,
                              'native_visibility': 'Labels and original line geometry readable; no added auxiliary lines or new faces. Endpoint drafts visibly add dots; color-only drafts retain the original linework.'})
    fidelity = {
        'audit_type': 'Native parent internal finite audit; not NEW independent second review or approval',
        'latest_user_instruction': '以模仿为主就好，不要探索太多了。',
        'reference': {'question_id': 'Solid203', 'slot': 'C01', 'current_live_PNG_actually_viewed_via_byte_identical_snapshot': True,
                      'live_png_path': str(reference_png), 'live_plugin_path': str(reference_plugin),
                      'png_sha256': sha(reference_png), 'plugin_sha256': sha(reference_plugin),
                      'actual_method': 'Exactly two existing boundaries, x and upper-left C, red; all other edges black. No added points, auxiliary lines or edge-thickness changes.'},
        'candidates': fidelity_rows,
        'r12_vs_r11': {'red_receiver_changed': ['netedge11 (printed1)', 'netedge2 (printed4)'],
                       'blue_pair_unchanged': ['netedge13', 'netedge9'],
                       'new_green_true_seam': ['netedge5', 'netedge14'], 'new_orange_true_seam': ['netedge8', 'netedge16'],
                       'difference': 'Switches red receiver and adds four specifically located original edges for two further true seam pairs. More information than r11; not a width/color/filename-only repeat.'},
        'r12_vs_earlier_preset4': {
            'r02': 'Same red x–4 pair, but r12 additionally displays three true seam pairs (six edges).',
            'r05': 'r05 compares four colored endpoints; r12 colors original boundaries and adds full context. Different representation and geometric information.',
            'r08': 'Same red x–4 and blue3–2 pairs exactly. r12 adds green5–14 and orange8–16 true seam groups. This is the closest earlier candidate and its4/3 failure remains unchanged.',
            'not_cosmetic_only': True,
            'limited_claim': 'These concrete additions establish changed visual information, not model uptake, causal gain, or an independent new mechanism.'},
        'r12_complexity_and_purpose': {
            'original_edge_styles_only': True, 'action_count': 8, 'color_group_count': 4, 'added_points_or_lines': 0,
            'group_geometry': read(UNIT / 'Solid166/r12_full_seam_context_x_four/design.json')['closure_math'],
            'roles': 'Each of the six context edges is one end of one exact source-to-receiver seam pair in all_true_free_seams.json. They are not isolated decorative strokes.',
            'legibility': 'At native768×768 all printed1–5/x labels remain unobscured. Existing triangles and display-solid hidden/solid edges remain readable. Red and orange are adjacent at the lower flap but visibly distinct.',
            'fidelity_limit': 'Four groups/eight edges is materially broader than the user reference of one red pair/two edges. It should be described as an extended imitation, not a close minimal copy.',
            'simplicity_limit': 'No visibly purposeless or stray geometry found, but usefulness does not establish that all three context pairs are necessary. No ablation or further test is performed.',
            'semantic_limit': 'Same colors can suggest pair identities, which is the intended comparison. This audit does not settle the NEW independent review of human interpretation or approve it as a puzzle condition.'},
        'observed_response_limit': 'Neither complete r12 response explains the added green/orange seam roles. Both final answers are4; one explicitly mentions red, while their folding narratives are flawed. Preset mechanism and causal improvement remain unverified.',
        'scope': 'No new designs, ideas, rendered images, solver calls, controls, retries, source amendments or continued exploration. Existing12 candidates only.'}
    dump(OWN / 'method_fidelity.json', fidelity)

    queue = read(UNIT / 'second_review_queue.json')
    audit = {
        'audit_type': 'Native parent internal terminal-evidence audit; no independent recommendation or user approval',
        'completed_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': {'unit': str(UNIT), 'questions': ['Solid166','Solid240'], 'existing_candidate_images': 12,
                  'existing_actual_calls': 24, 'new_calls': 0, 'new_designs': 0, 'new_renders': 0, 'new_replays': 0, 'subagents': 0},
        'result': 'One existing PRIMARY survives transport/outcome audit: Solid166 r12 preset4/observed4/4/correct5. NEW independent review remains required; no candidate approved or delivered by this audit.',
        'candidates': candidate_reports,
        'outcome_notes': {'r02_run2': 'Early text says4, but explicit final is1; kept MISS.',
                          'r03_run1': 'Final1(or2) is ambiguous; kept MISS.',
                          'r09_run1': 'Read all33933 characters; initial1 is reversed and last committed final is3; kept MISS.',
                          'r10_run2': 'Concludes1 meets3, not an answer identifying a seam for x; kept MISS.',
                          'r11_run1': 'Final explicitly2and5; intermediate speculation1 is not accepted as preset1.'},
        'transport': {'canonical_publish_batch_verify_evidence': 'Passed all12 candidate pairs',
                      'canonical_helper_sha256': sha(TASK / 'publish_batch.py'),
                      'canonical_helper_matches_previous_copy': sha(TASK / 'publish_batch.py') == sha(ROOT / 'runtime/mathvision_special_20261101/publish_batch.py'),
                      'full_request_raw_design_plugin_pixel_profile_binding_verified': True,
                      'unique_PNGs': len({c['image_sha256'] for c in candidate_reports}),
                      'unique_request_payloads': len({c['request_sha256'] for c in candidate_reports}),
                      'one_invocation_two_calls_each_no_extra_transport': True,
                      'no_input_or_answer_cherry_pick': 'All24 raw responses personally read; no extraction of early conflicting assertions, no third call or frozen preset changes found.',
                      'no_cosmetic_only_within_unit_repeats': 'Source receiver, mark representation, or concrete true-seam context changes in each design. r12 closest to r08 adds two exact context pairs; causal independence not asserted.'},
        'current_eligibility': eligibility,
        'Solid240_hold': {'status': 'Preserve existing HOLD_ORIGINAL_ORIENTATION_UNIQUENESS', 'calls': 0,
                          'formal_answer_preserved': '1', 'frozen_assumption': 'Q_apex_maps_to_T',
                          'worker_counterexamples': 'Three proper face-stabilizing orientations retain Q face and give neighboring target1,2,6 under the ordinary upright face-identifier reading.',
                          'claimed_limit': 'Treating Q as a physically oriented printed glyph can recover the intended pose/answer1. The worker reports that visible text does not distinguish this from a face identifier; this is a research uniqueness gate hold, not a correction or revocation of user-approved formal data.',
                          'counterexample_file_sha256': sha(UNIT / 'Solid240/orientation_counterexample_explanation.json'),
                          'math_file_sha256': sha(UNIT / 'Solid240/primary_math_and_orientation_hold.json'),
                          'hold_report_sha256': sha(UNIT / 'Solid240/hold_report.json'),
                          'no_new_orientation_research_or_source_fix': True},
        'preservation': {'unit_files_count': len(unit_now), 'unit_tree_unchanged_during_native_audit': True,
                         'scoped_readonly_count': len(scoped_now), 'scoped_sources_and_history_checks': scoped_now,
                         'worker_final_manifest_rechecked_count': len(recorded_checks), 'worker_final_manifest_all_match_current': True,
                         'formal_approval_Source_Special_state_readonly': True,
                         'limits': 'Only worker-scoped sources/history/current reference and the completed unit are checked. This is not a global workspace-unchanged claim.'},
        'process_closure': process,
        'method_fidelity_report': str(OWN / 'method_fidelity.json'),
        'pending_new_independent_review': True, 'Pass_Collect_formal_edits_publication': False,
        'secrets_or_credentials_read_or_printed': False,
        'local_audit_diagnostic': 'Optional jsonschema package was unavailable during report assembly; replaced it with explicit checks of documented plugin shapes, permitted fields/colors, styleable IDs and exact original vertices, without installing a dependency. A manifest-parser assertion then exposed that worker-final values use before_sha256/after_sha256 rather than sha256; corrected only this own helper parser. Neither incident mutated sources or invoked a model.',
        'write_policy': 'Python-B, thread env1, own cache env and writeguard before project/numeric imports. Socket connections blocked. All new outputs confined to this native_u09 directory.'}
    dump(OWN / 'audit.json', audit)
    assert unit_snapshot() == baseline_data['unit_files']
    print(json.dumps({'audit': str(OWN / 'audit.json'), 'fidelity': str(OWN / 'method_fidelity.json'),
                      'candidate_pairs_verified': len(candidate_reports), 'scoped_files': len(scoped_now),
                      'recorded_mismatches': [name for name, row in scoped_now.items() if not row['matches_worker_recorded_sha256']],
                      'unit_files_unchanged': len(unit_now), 'processes_remaining': 0}, ensure_ascii=False))

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'baseline': baseline()
    elif mode == 'raw':
        raw(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv)>4 else None,
            int(sys.argv[5]) if len(sys.argv)>5 else 0, int(sys.argv[6]) if len(sys.argv)>6 else None)
    elif mode == 'verify': verify()
    elif mode == 'finish': finish()
