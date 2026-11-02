from tools18 import *
p=HERE/'checkpoint.json';original=p.read_bytes();data=json.loads(original)
(HERE/'checkpoint_initial_snapshot.json').write_bytes(original)
for c in data['candidates']:
    c['complete_manual_finals_review']=json.loads(Path(c['manual_complete_finals']).read_text(encoding='utf-8'))
    c['primary_math_visual_marker_review']=json.loads(Path(c['primary_review']).read_text(encoding='utf-8'))
    c['source_audit_record']=json.loads(Path(c['source_audit']).read_text(encoding='utf-8'))
    for rel,sha in c['file_hashes'].items():assert file_hash(HERE/rel)==sha,rel
data['prior_own_checkpoint_snapshot']=str(HERE/'checkpoint_initial_snapshot.json')
data['complete_final_answers_visual_findings_source_audits_embedded']=True
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='''background_18 — finite primary exploration complete.

20/20 assigned questions assessed; no unworked IDs.
6 designs across 4 questions; 6 complete pairs / 12 actual Quick Test 3 calls.
0 credible paired hits; 0 API errors, aborts, retries or original controls.

Complete finals, compared manually with immutable presets:
Plane366 directed_endpoint_binding: only Y / D; preset D.
Solid239 single_unfold_triangle_binding: E / E; preset D.
Solid239 crease_axes_as_hole_edges: E / E; preset C.
Solid145 front_strand_identity_transfer: D / B; preset C.
Solid145 free_end_upper_side_binding: C / B; preset A.
Solid164 upright_yes_face_alias: A / C (5/9); preset A.

All full finals were read manually and preserved, with exact raw request/response,
PNG, plugin and pre-call design bindings. No incidental option mention counts.
All 20 individual frozen MathVision input / current approval / eligibility audits
pass. Whole-workspace equality is not claimed. All own output and cache paths
are below this unit directory. No formal writes or review API actions occurred.

checkpoint.json embeds full manual finals, primary math/visual/marker reviews,
source audits, raw bindings and evidence paths. second_review_queue.json is empty.
No candidate approved or published. Parent must start a NEW independent second
reviewer before any eventual delivery. No human, statistical or per-marker causal
effectiveness claim; no original controls. Do not retest unchanged failed images.
process_audit.json records final no-live-own-API verification.
'''
(HERE/'report.txt').write_text(report,encoding='utf-8')
print(json.dumps({'all_candidate_evidence_hashes_valid':True,'full_manual_finals_embedded':True,'question_count':len(data['assessed_question_ids']),'designs':len(data['candidates']),'credible_paired_hits':0,'checkpoint':str(p)}))
