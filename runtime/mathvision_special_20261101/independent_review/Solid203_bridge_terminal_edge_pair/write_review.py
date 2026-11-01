"""Record the independent review reached after manual image/response inspection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
TASK = ROOT / 'runtime/mathvision_special_20261101'
CAND = TASK / 'background_03/solid_worker/Solid203/bridge_terminal_edge_pair'
audit = json.loads((OUT / 'technical_audit.json').read_text(encoding='utf-8'))
assert audit['all_checks_pass']
for path, expected in audit['protected_input_hashes'].items():
    assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path

review = {
    'decision': 'recommended',
    'question_id': 'Solid203',
    'candidate_directory': CAND.relative_to(TASK).as_posix(),
    'candidate_directory_base': 'runtime/mathvision_special_20261101',
    'candidate_path': (CAND / 'candidate.png').relative_to(ROOT).as_posix(),
    'candidate_path_base': str(ROOT),
    'reviewed_at_utc': datetime.now(timezone.utc).isoformat(),
    'review_role': 'New independent second reviewer; reviewed exactly this one proposal; no design contribution or subagents.',
    'recommendation_scope': 'Independent recommendation only. No publication, qualification entry, user approval, Pass, Collect, workbench state update, or formal edit.',
    'checks': {
        'hard_criteria': {
            'eligible_formal_MathVision_without_Pass_or_Collect': {
                'result': 'pass',
                'source_dataset': 'MathVision',
                'source_key': 'test:1943',
                'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a',
                'formal_record': 'SolidGeometry/dataset.jsonl',
                'current_indices': audit['eligibility'],
                'question_special_variant_directory_exists': False,
                'original_user_approval_fingerprint': audit['approval'],
                'explanation': 'Read the actual formal record, current accepted/collected indices and original approval; recomputed the current original approval content fingerprint. Neither index contains Solid203, and its special_variant directory is absent.'
            },
            'two_separate_quicktest3_calls_same_frozen_image_hit_predeclared_A': {
                'result': 'pass',
                'manual_candidate_finals': ['A', 'A'],
                'model': 'mimo-v2.6-flash',
                'thinking': {'type': 'disabled'},
                'finish_reasons': ['stop', 'stop'],
                'truncated': [False, False],
                'details': 'Manually read BOTH complete raw response bodies (1975 and 3039 bytes), including all intermediate mistakes. Run 1 ends with Correct Answer: A; run 2 ends with Final Answer: A:A. Verified distinct run IDs, response IDs and timestamps, exact raw-response SHA-256 values, HTTP 200, complete parsed bodies, and matching result/summary/start records. The second request starts after the first finishes; neither request contains prior assistant content.'
            },
            'predeclaration_and_payload_integrity': {
                'result': 'pass',
                'details': 'design_snapshot.json is byte-identical to current design.json and the prepared-copy hash. It declares expected_wrong_answer A. Binding creation precedes both recorded starts; the read-only inspected harness writes binding/request/snapshot before the loop and checks image/design bytes before each independent call. Both starts/results bind the same design/image/request hashes. Decoded the actual request data URL and compared exact bytes with candidate.png. The only messages are the unchanged existing solver system prompt and a user message containing exactly the current formal question plus this PNG. No answer, intent, plugin, design, source image, history, token cap or extra instruction is present.'
            },
            'unique_correct_mathematics': {
                'result': 'pass',
                'answer': 'E',
                'details': 'Independently propagated octahedron vertex identities across all eight triangles from the actual formal scene, starting at face0 with a different seed from the primary proof. Verified eight distinct folded faces, six physical vertices, twelve edges with two face incidences each, unit equilateral triangles, and exact labelled-edge endpoint matching. Only E matches x.'
            },
            'human_readability_and_unambiguous_edge_binding': {
                'result': 'pass',
                'actually_viewed_paths': [
                    (CAND / 'candidate.png').relative_to(ROOT).as_posix(),
                    'SolidGeometry/image/Solid203.png',
                    'SolidGeometry/originals/Solid203.jpg'
                ],
                'details': 'Viewed the actual candidate, formal redraw and source separately. A is next to the upper red diagonal and x next to the lower red diagonal; B,C,D,E and the reference octahedron are readable and unobscured. All eight net faces and original hinges remain visible. The common red vertex is the existing n8, with no added dot, bridge, label or geometrical intersection. Red/2pt styling leaves the normal folding question and its unique answer intact; no legend promotes color to a mathematical constraint.'
            },
            'every_mark_useful_concise_and_geometrically_targeted': {
                'result': 'pass',
                'details': 'The two identically styled original free edges form an explicit target/partner pair at the terminal end of the net. Their common vertex n8 and the hinge n6-n8 between face6 and face7 make the local V suggest closing the two terminal edges together. This is a specific false seam correspondence x~A. It is visibly more specific than highlighting an option label alone. Both edge roles are needed to express this particular two-member visual code; no incidental marks remain. This is a semantic necessity assessment, not a measured ablation claim.'
            },
            'permitted_operations_and_frozen_inputs': {
                'result': 'pass',
                'details': 'Read the actual plugin and schema. Exactly line_20 and line_24 receive #DC2626, 2pt; neither action supplies linestyle or interval. Validated against the applicable schema keywords and exact action whitelist. Formal and captured source IDs/endpoints agree. Recomputed every recorded frozen input hash, including the checked-in MathVision bridge, schema, plugin executor, scene, source, formal renderer and scripts. All match. The pixel difference is confined to the two selected edges; geometry, projection, frozen visibility and labels are preserved.'
            }
        },
        'protocols_read': [
            'AGENTS.md', 'MATHPALETTE_PROTOCOL.md', 'SolidGeometry/REDRAW_PROTOCOL.md',
            'SolidGeometry/workbench/README.md', 'SolidGeometry/workbench/agent_prompt.md',
            'SolidGeometry/workbench/plugin.schema.json', 'SolidGeometry/dataset_generator/protocol.json'
        ],
        'independently_recomputed_technical_checks': audit['checks'],
        'technical_check_count': len(audit['checks']),
        'technical_audit_path': (OUT / 'technical_audit.json').relative_to(ROOT).as_posix(),
        'actual_images_and_hashes': audit['images'],
        'formal_label_source_bindings': audit['label_source_bindings'],
        'test_and_control_fingerprints': audit['tests'],
        'delivery_replay': {
            'report': 'runtime/mathvision_special_20261101/delivery_validation/Solid203/replay_verification.json',
            'reproduced_png': 'runtime/mathvision_special_20261101/delivery_validation/Solid203/reproduced.png',
            'reviewer_checked_report_and_actual_reproduced_bytes': True,
            'candidate_replay_and_delivery_PNGs_byte_identical': True,
            'parent_report_records_two_identical_replays_and_formal_noop_match': True,
            'rerendered_by_this_reviewer': False,
            'explanation': 'Read the validation driver and portable delivery adapter. They use the checked-in dedicated bridge plus existing PluginRenderer; the driver asserts formal no-op identity and two exact tested-byte replays. Independently verified the saved reproduced PNG bytes and hashes against the tested request image and primary replay. No extra rendering or solver call was needed for this review.'
        }
    },
    'mathematical_proof': {
        'method': 'Represent a regular octahedron by vertices +/-e1,+/-e2,+/-e3, up to irrelevant uniform scale. A face has one vertex from each opposite pair. Adjacent faces sharing an edge must have antipodal third vertices. The connected net therefore fixes all vertex identities from any seed face, up to a global symmetry.',
        'independent_derivation': audit['mathematics'],
        'human_readable_conclusion': 'With seed (n0,n1,n2)=(e1,e2,e3), propagation gives n3=-e2, n4=-e1, n5=e2, n6=-e3, n7=e1, n8=-e2, n9=-e1. Thus x=n8-n9 has endpoints {-e2,-e1}, and E=n3-n4 has exactly those endpoints. A=n7-n8 and D=n0-n3 have {e1,-e2}; B=n5-n7 and C=n0-n1 have {e1,e2}. E is the only labelled match. In particular, n7 and n9 are antipodal, not coincident: the common planar endpoint n8 of A and x does not make their other endpoints glue. At n8 the two distinct folded red-edge rays have a 90-degree angle, not zero. Global rotation/reflection changes no edge coincidence.'
    },
    'marker_necessity': [
        {
            'target': 'line_20', 'label': 'x', 'formal_endpoints': ['n8', 'n9'],
            'source_binding': 'SolidGeometry/dataset_generator/scenes/Solid203.json objects.line_20; label_5 anchored at labx, the exact edge midpoint. Captured source_call scene_object_id and native_object_id are both line_20.',
            'style': {'color': '#DC2626', 'linewidth_pt': 2},
            'role': 'Query-side member of the proposed seam pair; marks the lower free edge of terminal face7 and explicitly binds the shared red code to the requested x.',
            'removal_assessment': 'Without this mark, only the wrong option edge A is red, leaving a standalone salience cue instead of the two-sided x~A correspondence.',
            'useful': True, 'ambiguous_or_useless': False,
            'assessment_scope': 'Semantic/visual role established; no single-mark ablation was performed.'
        },
        {
            'target': 'line_24', 'label': 'A', 'formal_endpoints': ['n7', 'n8'],
            'source_binding': 'SolidGeometry/dataset_generator/scenes/Solid203.json objects.line_24; label_4 anchored at labA, the exact edge midpoint. Captured source_call scene_object_id and native_object_id are both line_24.',
            'style': {'color': '#DC2626', 'linewidth_pt': 2},
            'role': 'Proposed partner member of the same seam pair; marks the upper free edge of face6, adjacent to face7 across n6-n8. Its matching red stroke completes the existing outer V at n8 and suggests the false local terminal closure.',
            'removal_assessment': 'Without this mark, x alone is emphasized and no specific wrong partner is encoded. The mark changes the actual geometric edge rather than the answer text.',
            'useful': True, 'ambiguous_or_useless': False,
            'assessment_scope': 'Semantic/visual role established; its independent empirical contribution is not identifiable from the available tests.'
        }
    ],
    'manually_read_test_finals': ['A', 'A'],
    'manually_read_original_control_finals': ['A', 'B'],
    'issues': [
        {
            'severity': 'nonblocking_documentation',
            'location': 'design.json and tests/quicktest3_20261101T113921_5c07ba30a1ea/design_snapshot.json',
            'finding': 'PREPARED_NOT_TESTED, pending second review and the human_solvability sentence reflect the pretest preparation timestamp. Complete subsequent test evidence establishes A/A. Frozen source text was preserved; this report records the present recommendation separately.'
        },
        {
            'severity': 'evidence_strength_limitation',
            'location': 'control_tests/quicktest3_20261101T114107_ebe8657e7600',
            'finding': 'Original controls are A/B: both are wrong and one already reaches target A. No causal or statistical increment from the red pair may be claimed. Correct controls were not introduced as an additional hard requirement.'
        },
        {
            'severity': 'nonblocking_inherited_metadata',
            'location': 'SolidGeometry/dataset_generator/scenes/Solid203.json source_note; frozen item protocol_review.json',
            'finding': 'Historical no-formal-approval/user_approved:false wording survives in inherited scene/review metadata. The authoritative current dataset and explicit original approval with recomputed matching content fingerprint establish formal eligibility. These historical strings were not changed or treated as Special approval.'
        }
    ],
    'rationale': 'Recommended because the specified hard criteria are met for this single frozen candidate: two separately recorded complete Quick Test 3 calls return the predeclared A, all request/design/image/response/question bindings hold, an independent eight-face proof establishes unique E, and the actual readable PNG contains precisely two useful original-edge marks encoding a specific false terminal seam. The recommendation does not rely on a quota, a correct control, identical verbal reasoning, or a causal/statistical benefit claim.',
    'limitations': [
        'Two observed hits on a fixed image/preset establish the required repeat observation, not a reliability estimate, generalization result or statistical improvement. Original A/B controls preclude causal increment claims.',
        'Both candidate answers contain substantial geometric mistakes, including wrong face layouts/counts. Run 1 expressly mentions the V and red segments; run 2 describes the wrong local closure with additional topology errors. This is compatible with the proposed mechanism but does not prove a shared internal reasoning process. Identical reasoning is not a hard gate.',
        'No per-edge or color/width ablation exists. Each mark has an independently identifiable role in the two-member geometric code, but neither its empirical necessity nor the specific contribution of 2pt width is established.',
        'Independent calls here means two separate stateless request/response events using the same frozen payload; run 2 reports 640 cached prompt tokens. Prefix caching does not insert the earlier answer into the request, but stochastic independence is not established.',
        'Historical execution/predeclaration order is supported by saved binding/start timestamps, distinct response IDs, complete raw bodies, hashes and the inspected harness. This offline review did not contact the provider or independently witness the historical calls.',
        'This reviewer verified actual replay artifact identity and inspected the parent replay implementation without reexecuting rendering. The parent report records the two replay executions; checked-in bridge/plugin/formal-renderer fingerprints remain unchanged.',
        'jsonschema is absent from the local interpreter. The audit therefore used a dependency-free validator against the actual schema and all applicable keywords, plus an exact check of the two permitted style actions; no package installation was performed.'
    ],
    'preservation': {
        'writes_only_within_review_directory': True,
        'protected_original_evidence_and_formal_input_hashes_unchanged': True,
        'new_API_calls': 0, 'browser_actions': 0, 'subagents_or_background_delegates': 0,
        'formal_edits': 0, 'Pass_or_Collect_actions': 0,
        'dot_runtime_dot_git_dot_env_changes': False
    }
}
path = OUT / 'independent_review.json'
with path.open('x', encoding='utf-8', newline='\n') as stream:
    json.dump(review, stream, ensure_ascii=False, indent=2)
    stream.write('\n')
print(json.dumps({'decision': review['decision'], 'report': str(path), 'manual_test_finals': review['manually_read_test_finals'], 'manual_control_finals': review['manually_read_original_control_finals'], 'technical_checks': len(audit['checks'])}, ensure_ascii=False))
