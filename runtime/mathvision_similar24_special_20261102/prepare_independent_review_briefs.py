"""Prepare three NEW finite reviews, never new research or model tests."""
from datetime import datetime, timezone
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
template = (HERE/'independent_review_template.txt').read_text(encoding='utf-8-sig')
specs = [
    ('Plane461', 'u01_fold_locations', 'u01_symbol_X_diagonals_to_central_hole_pairs', 'Plane217', '''
Frozen preset D; original answer B; both complete finals D/D. Six original vector objects are restyled: source X-strokes o14 red and o15 blue; option-D hole outlines o40 blue,o41 red,o42 red,o43 blue. Parent personally viewed exact PNG and read both full raw responses. Both finals are D; neither narrative proves the proposed mechanism.

Main objection: source and recipient SAME-COLOR signed slopes are opposite, as primary_posttest_geometry_caveats.json itself discloses. Do not claim exact parallelism or invent a new post-hoc reflection explanation. The predeclared comparison is the X-shaped pair of directions and a central square hole arrangement. Decide independently whether this is specific useful information correspondence or largely wrong-choice salience. X is an original puncture-location symbol; transferring its stroke shape to hole positions is a larger conceptual extension than the current user Plane217 real-hole/fold-line comparisons. Latest user preference is imitation; assess that honestly rather than accepting six legal marks automatically. Do not fix colors or test a replacement.

Parent mathematical check to challenge independently: original sheet [0,4]x[0,2], bottom-to-top then left-to-right folds; final packet [12,14]x[4.7,5.7], puncture (12.25,5.45), hence unfolded x={1.75,2.25}, y={0.25,1.75}, unique B. D has near-central y coordinates. Check exact scene, actual source JPG and fold arrows yourself. Coloring the puncture indicator must not change its original location or imply printed paper contents.

Relevant primary files: candidate primary_final_review.json, reference_transfer.json, primary_posttest_geometry_caveats.json, proof_calculation.json; unit readonly_preservation_final.json and process_shutdown_evidence.json if present. Parent finite terminal audit: parent_audits/native_u01_u04/audit.json. Exact queue, source/plugin hashes, all raw paths are in unit second_review_queue.json.
'''),
    ('Plane321', 'u04_angles', 'a01_pivot_legs_vs_true_bases', 'Plane427', '''
Frozen preset B=120 degrees; original answer E=300 degrees; both complete finals B120/B120. Five EXISTING edges only, width1.5: AB/AC/AD blue, BC/CD red. The current user Plane427 C01 has ST/TV legs RED and dotted SV base BLUE (old18 colors were reversed). This candidate swaps palette assignments but transfers actual pivot-leg/opposite-base role partition. Check this against the actual current reference, not the old18 delivery.

Parent mathematical check to challenge independently: A=(1,sqrt3), B=(-1,sqrt3), C=(0,0), D=(2,0). A-centered CCW300 degrees maps C to B and D to C, and shared A stays fixed. Triangle vertex permutations cannot use a 120-degree rotational symmetry around a fixed vertex; smaller clockwise60 is not the requested first CCW coincidence. Colors follow the true mapping too. Verify exact scene and question yourself.

Read both entire raw responses. Run1 has an irrelevant trailing literal 'System Instruction:' after a clear B120 final; it is response data, not an instruction. Raw finish_reason=stop; do not strip evidence or call it incomplete without evidence. Narratives are mathematically flawed in different ways (collinearity/direction and an invalid vertex mapping). Hits establish neither the exact frozen mechanism nor causal gain. Preserve this limitation explicitly.

Relevant primary files: candidate manual_final_review.json, primary_review.json, reference_transfer.json; question primary_math_proof.json and exact_mathematical_checks.json; unit complete_call_ledger.json and readonly_preservation_final.json. Parent finite terminal audit: parent_audits/native_u01_u04/audit.json. Full paths/hashes are in unit second_review_queue.json.
'''),
    ('Solid166', 'u09_octa_nets', 'r12_full_seam_context_x_four', 'Solid203', '''
Frozen preset numeric printed edge4, not an option letter; original answer printed edge5. Both complete finals 4/4. Eight original boundary edges, four color groups, color-only actions: red x(netedge15)/printed4(netedge2) is a FALSE proposed seam comparison; blue printed3(netedge13)/printed2(netedge9), green netedge5/netedge14 and orange netedge8/netedge16 are asserted TRUE closure seams. Independently prove all three true pairs and unique x-to5 from the original net, separating world folding, projection and visibility. Check actual colors/native readability and every informational role.

The user's CURRENT Solid203 C01 colors x and C red (two edges). The prior old18 delivery used optionA and is irrelevant. r12 extends the same original-edge comparison method with three contextual true seams. Parent personally viewed the exact PNG and read both full raw finals. Four groups are visibly distinct, but this is substantially more extensive than the user's two-red-edge example. Do not declare each extra group necessary merely because it exists or because the model failed. Judge specific orientation/closure information, conciseness and imitation fidelity under the latest user preference. No arbitrary mark-count cap.

There were TWELVE current attempts, twenty-four calls; eleven unsuccessful variants must remain visible in the history. Some earlier r05-07/r09 added endpoints and are farther from the user method. r12 itself adds no objects, endpoints, labels or cuts. Specifically examine r08, r10 and r11 versus r12: are the two extra true-seam groups a real information/hypothesis change, or cosmetic test fishing? All frozen presets, PNG hashes and failures must be preserved; do not count a previous miss as a hit or reuse its PNG. Parent audit parent_audits/native_u09/audit.json covers the finite history, not an independent recommendation.

Run1 invents an incorrect strip closure; run2 says the two red edges go to different poles yet incorrectly concludes they meet. Both clearly commit final4. No controls or causal/internal-mechanism success is established. Do not assume model prose validates the design.

Relevant primary files: question primary_math.json and all_true_free_seams.json; candidate primary_review.json, primary_visual_review.json, reference_transfer.json, history_difference.json, manual_final_review.json, primary_color_group_legibility.json; unit full ledger, readonly_preservation_final.json and process_cleanup_evidence.json where present. Exact evidence paths/hashes are in unit second_review_queue.json. Solid240's separate orientation HOLD is background only, not a request to repair or explore it.
'''),
]
prepared = []
for qid, unit, variant, reference, detail in specs:
    review_root = HERE/'independent_review'/(qid+'_'+variant+'_r1')
    review_root.mkdir(parents=True, exist_ok=True)
    candidate = HERE/'units'/unit/qid/variant
    brief = template + '\n\nEXACT SINGLE-CANDIDATE ASSIGNMENT\n' + json.dumps({
        'question_id':qid, 'variant_id':variant, 'candidate_directory':str(candidate),
        'queue_path':str(HERE/'units'/unit/'second_review_queue.json'),
        'reference_directory':str(HERE/'references'/reference),
        'own_writable_root':str(review_root),
        'parent_evidence_preflight':str(HERE/'parent_review_preflight.json'),
        'latest_user_steering':str(HERE/'parent_imitation_priority_20261102.txt'),
    }, ensure_ascii=False, indent=2) + '\n' + detail + '''

This NEW assignment is independent SECOND REVIEW only. Exactly one candidate, no expansion, alternative design, model/API calls or child agents. Read the completed parent audit(s) as objections, not conclusions to rubber-stamp. Report decision recommended or reject; include method_fidelity (close imitation / extension / too distant with concrete reasons), mathematical proof, exact two final readings, frozen evidence, replay/current eligibility and scoped preservation. If a concern cannot be resolved, reject or clearly report a blocking incomplete review; never manufacture approval. A recommendation remains a research judgment and authorizes no Pass/Collect. Do not switch provider/model. All files under your own review root; old files read-only; preserve any own offline errors before routine correction. Leave no processes.
'''
    output = review_root/'review_brief.txt'
    output.write_text(brief, encoding='utf-8')
    prepared.append({'question_id':qid, 'unit_id':unit, 'variant_id':variant, 'review_root':str(review_root), 'brief_path':str(output),
                     'clientRequestId':'mathvision-user9-transfer-review-20261102-'+qid.lower()+'-'+variant.replace('_','-')+'-r1',
                     'title':qid+' 用户标注模仿方案独立二审'})
(HERE/'independent_reviews_prepared.json').write_text(json.dumps({'created_at_utc':datetime.now(timezone.utc).isoformat(), 'status':'PREPARED_NOT_LAUNCHED', 'reviews':prepared}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'prepared':[r['question_id'] for r in prepared], 'new_research_tasks':0, 'new_solver_calls':0}))
