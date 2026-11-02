from worker import *

RED='#DC2626';BLUE='#2563EB'

def make(qid,variant,preset,groups,mechanism,novelty,semantics):
    d=OWN/qid/variant
    if (d/'design.json').exists():raise RuntimeError('Immutable design already exists')
    d.mkdir(parents=True,exist_ok=True)
    eligibility(qid,d/'eligibility_before_design.json')
    context=read(OWN/qid/'context.json');objects={o['id']:o for o in context['objects']}
    actions=[];roles=[]
    for group in groups:
        targets,color,role=group
        for target in targets:
            action={'type':'set_object_style','target':target,'color':color}
            actions.append(action);roles.append({'index':len(roles),'action':action,'source':objects[target],'recipient':role,'purpose':role,'necessity':'One of the explicitly compared existing boundary segments; removing it loses that endpoint/boundary member. No full-option recoloring.'})
    assert len({a['target'] for a in actions})==len(actions)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':variant,'intent':mechanism,'params':{'actions':actions}}
    save(d/'plugin.json',plugin)
    history=read(OWN/'history_scope_index.json');history=next(q for q in history if q['question_id']==qid)
    migration={'reference_question':'Solid176','reference_C01_png_sha256':sha(TASK/'references/Solid176/C01.png'),'reference_plugin_sha256':sha(TASK/'references/Solid176/C01.json'),'actual_current_reference_viewed':True,'method':'Original free boundary segments compare the orientation/placement and eventual closure of actual flaps or holes. D has four red true triangular flap edges; dashed fold lines remain. This is the currently saved reference, not old18 description.','application':mechanism,'does_not_copy_option_or_color_meaning':True,'all9_current_images_viewed':True}
    save(d/'reference_migration.json',migration)
    earlier_new=[]
    for pp in (OWN/qid).glob('*/design.json'):
        previous=read(pp)
        if pp.parent==d:continue
        earlier_new.append({'path':str(pp),'sha256':sha(pp),'preset':previous['expected_wrong_answer'],'mechanism':previous['mechanism_hypothesis'],'manual_review':read(pp.parent/'manual_final_review.json') if (pp.parent/'manual_final_review.json').exists() else None,'do_not_retest':True})
    difference={'new_hypothesis':mechanism,'material_difference':novelty,'old_designs':[{'id':x['variant_id'],'preset':x['predeclared_wrong_answer'],'mechanism':x['mechanism'],'image':x['frozen_candidate_png_sha256'],'do_not_retest':True} for x in history['designs']],'earlier_new_designs':earlier_new,'old_responses_completely_read':True,'old_evidence_read_ledger':str(OWN/'history_actual_files_read.json'),'cosmetic_only':False}
    save(d/'history_difference_audit.json',difference)
    correct=next(x['formal_record']['answer'] for x in ASSIGN['questions'] if x['question_id']==qid)
    record=read(d/'eligibility_before_design.json')['record']
    design={'question_id':qid,'variant_id':variant,'created_at':now(),'expected_wrong_answer':preset,'expected_wrong_value':record['choices'][preset],'correct_answer':correct,'correct_value':record['choices'][correct],'mechanism_hypothesis':mechanism,'preset_basis':'The specifically documented comparison can cause this exact geometric error; this prediction is frozen before any new model output. Output outside this letter/value is a miss.','primary_math_proof':str(OWN/qid/'primary_math_proof.json'),'math_proof_sha256':sha(OWN/qid/'primary_math_proof.json'),'marker_roles':roles,'reference_migration':str(d/'reference_migration.json'),'history_difference_audit':str(d/'history_difference_audit.json'),'human_clarity_and_literal_reading':semantics,'restrictions':['PRIMARY research only','No user Pass or Collect','NEW independent second review by parent required','Exactly two original quicktest3 calls after offline gates','No third call, retry, posthoc preset or selected subset']}
    save(d/'design.json',design)
    print(qid,variant,preset,len(actions))

def first():
    make('Solid187','C01_opposite_face_window_substitution','E',[
        (['Eboundary22','Eboundary33','Eboundary58','Eboundary65'],RED,'Compare the two side borders of each actual interior rectangular window on the two opposite E faces. All four red segments delimit the same pair-of-opposite-face portal relation; top and bottom black window edges retain the closed-hole topology.')],
        'Two genuinely opposite face windows in E are grouped by four original short side borders. Predict substituting opposite-window placement for the required opposite-edge cutouts, choosing E while overlooking that each target hole straddles two faces.',
        'Old B/D designs paired target half-notches to exterior notch partners; old A split one target opening into two. This has no target marks and no cap or half-notch partner claim: it compares two fully interior windows, whose opposite face normals are true but whose codimension on the shell is wrong. E was never an old tested marked recipient.',
        'Only E, already invalid by window-versus-edge topology, carries ink. A/B/C/D and the target remain unchanged, so the unique correct C remains color-compatible even if every new red border is interpreted as physical ink. E is still geometrically invalid regardless of ink, and cannot become a valid match; no ambiguity or new cut is introduced. Four short borders leave gray material, closed holes and all net fold lines readable.')
    make('Solid193','C01_flap_count_versus_destination','A',[
        (['net2triangle2side0','net2triangle2side1','net2triangle3side0','net2triangle3side1'],BLUE,'The upper/lower triangular flaps in net3 that land on occupied full faces: two complete V contours expose the actual collision pair.'),
        ([f'net4triangle{j}side{s}' for j in range(4) for s in range(2)],RED,'The four actual quarter-triangle flaps of net5 form a visual complete set, inviting cardinality-four closure even though its top flap folds onto an occupied face. Each V edge is a true cut boundary.')],
        'Contrast net3 two visibly opposed colliding flaps with net5 visually complete four-quarter set. Predict accepting net5 on count alone, rejecting net1 strip as unable to close, and hence invalid1and3 -> A. The actual destination audit proves net1 valid and net5 invalid.',
        'Old193 paired source red/blue diagonals to four alternating half-sides in nets1/3 with preset B. This leaves source and every valid net1/2/4 black; marks complete offending Vs in3 and all actual flaps in5, isolates count-vs-destination rather than diagonal seam matching, and freezes A (1and3).',
        'Only already-invalid nets3 and5 are colored. Source and all three valid nets1/2/4 remain identical, hence a literal physical-edge-color reading also leaves those three valid and cannot repair geometry of3 or5. Original correct E (3and5) is unchanged. All 12 retained actions identify actual flap cut sides; there are no new faces or cuts and no overpainting. Blue two Vs diagnose real overlap; red four Vs expose actual count, with one wrong destination still visibly testable.')
    make('Solid228','C01_staggered_wing_seam_pair','E',[
        (['line_90','line_92'],RED,'Compare the free outer edges of E upper and lower wings. They bound faces with opposite normals and cannot be the same cube seam, but apparent same-color closure may be incorrectly demanded.'),
        (['line_79','line_87'],BLUE,'Compare the actual free strip endpoints of E. These two edges really close together as the length-four strip wraps, supplying the true comparison anchor for the misleading wing pairing.')],
        'The blue ends of E length-four belt really close. The same-color red outer edges of its staggered top/bottom wings do not meet because their faces are opposite. Predict overgeneralizing the true blue same-color closure into a mandatory red closure, declaring E impossible.',
        'Old A designs marked staircase terminal edges/face rims. Old B borrowed D repeated-face overlap with eight edges. This uses E staggered-wing free-edge seam incidence with a true strip-closing pair and a false wing-closing pair, not repeated-face overlap or A staircase geometry. It is a new four-edge mapping on untested recipient E, not a color/width swap.',
        'The question asks only whether identical square geometry folds to any cube, with no colored target, gluing rule or same-color seam requirement. Physical red/blue ink stays on its own four original edges through any legal fold and never changes squares, hinges or foldability. E can be explicitly assembled by the six-face map with blue ends coincident and red edges on opposite faces; no rule requires same colors to meet. Thus all color-preserving constructions retain unique invalid D. Four open boundary edges do not add a cut, partition or face.')

def second():
    make('Solid187','C02_shared_face_notch_ownership','A',[
        (['Aboundary9','Aboundary56'],RED,'Half-notch bases in the left and right lateral cells of A. Their supporting faces are truly opposite after folding; compare their genuine face-normal opposition.'),
        (['Aboundary28','Aboundary39'],BLUE,'Two half-notch bases in the very same central A cell. Their shared-face ownership is the countercheck: target four affected faces cannot be reduced to three. Blue marks identify a single shared panel rather than a second opening.')],
        'Group A half-notch boundaries by face ownership: red bases belong to genuinely opposite side faces, blue bases both belong to one central face. Predict promoting the true opposition of red supporting faces into opposition of complete edge openings and choosing A; the shared blue panel shows exactly why this is false.',
        'Unlike oldA split-one-target-hole counting (source marks and two full A hole contours), this leaves target black and groups four bases by supporting FACE, not by hole identity. Unlike oldD local-complete-hole versus global edge placement, it distinguishes three affected faces from four, with common-panel ownership explicit. C01 E used interior windows and had no half-notch face-sharing relation. Same old output/preset is never substituted; this is a different annotated input and different information partition.',
        'Only invalid A carries colored bases. Target and valid C remain unchanged, so physical ink on A cannot add or remove the unique compatible C. Red ink does not create a tunnel or require gluing red bases; blue two bases stay on the same original square. Four selected existing cut bases remain open comparison segments with the original small black returns, hole count, fold edges and gray cardboard intact.')
    # Compute a truthful full diagonal seam correspondence on EVERY valid net.
    from fractions import Fraction as F
    proof=read(OWN/'Solid193/primary_math_proof.json')
    valid_groups=[];net1_indices=[]
    for n in (1,2,4):
        panel=proof['panels'][str(n)];missing=tuple(map(F,panel['missing_face_normal']))
        vertices={tuple(map(F,t['folded_vertices'][0])) for t in panel['triangles']}|{tuple(map(F,t['folded_vertices'][1])) for t in panel['triangles']}
        first=min(vertices);opposite=tuple(m-x for m,x in zip(missing,first));assert opposite in vertices
        targets=[]
        for t in panel['triangles']:
            for s in (0,1):
                if tuple(map(F,t['folded_vertices'][s])) in (first,opposite):targets.append(f'net{n-1}triangle{t["index"]}side{s}')
        assert len(targets)==4
        if n==1:net1_indices=[x.replace('net0','net4',1) for x in targets]
        valid_groups.append((targets,RED,f'Net{n}: both copies of each of two opposite corner-to-center cut half-seams. Under the explicit cube map these four sides close to exactly one diagonal, matching source cutdiagonal0 after a cube rotation. This preserves physical ink compatibility of every valid net.'))
    make('Solid193','C02_truthful_diagonal_with_false_strip_analogy','B',[
        (['cutdiagonal0'],RED,'One complete original diagonal cut on the source cube. It is the geometric receiving seam for the accurate quarter-side pairs in every valid net.'),
        *valid_groups,
        (net1_indices,RED,'Net5 cut sides at the same triangle-index/side pattern as the four-triangle strip in net1. This is a planar structural analogy, not a valid folded mapping; its top triangle still lands on an occupied face.')],
        'Accurately group a full red diagonal seam on all valid nets1,2,4. Copy the strip-side pattern from1 to5, inviting a false equivalence of the two four-triangle strips and the judgment that both fail while cross nets succeed: invalid1and5 -> B. The genuine seam closure of1 remains fully provable.',
        'Old193 B used two source colors with four isolated alternating half-sides on1 and3 and false source pairing. C01 used count-vs-destination on invalid3/5 and immutable A, which stays failed despite B/B outputs. New design has one source diagonal, a computed TRUE four-edge seam on each valid1/2/4, and a new planar analogy solely from1 to5. B is the old independent seam-pairing research hypothesis, now instantiated by this new correspondence; it is not a relabel of C01 or its preset and no C01 pixel is reused.',
        'Every valid net1/2/4 has both cut-edge copies of the two opposite red radial halves, so after the constructive fold a cube rotation aligns its red full diagonal with source cutdiagonal0; the other full diagonal remains black. Thus even literal physical seam color preserves all three valid nets. Invalid3 is unchanged and invalid5 cannot be repaired by edge ink. Unique invalid pair remains3and5 (E). No same-color gluing rule is added. Every one of the17 marks traces an actual source cut or its two-sided receiving seam; no full-panel or irrelevant edge coloring.')
    make('Solid228','C02_moving_hinge_axis_accumulation','A',[
        (['line_1','line_9','line_15'],RED,'The three actual vertical shared hinge segments along A staircase, in chain order. Parallel on the page, they have moving three-dimensional hinge axes after intervening folds.'),
        (['line_4','line_12'],BLUE,'The two actual horizontal shared hinge segments separating the three red folds in A. These are the necessary intermediate rotations that prevent scalar accumulation about one fixed axis.')],
        'Trace all five A hinges by their original planar direction: red E,E,E moves interleaved with blue south moves. Predict incorrectly adding the three parallel-page folds about a fixed spatial axis, concluding A overlaps/leaves a face open. The exact propagated axes are moving, and the six face normals are distinct.',
        'Old A hypotheses marked terminal free-edge pairs or terminal face rims. C01 E marked strip/wing free seams and remains failed against E even if outputs choose A. This marks only the five INTERNAL shared hinges of A and tests noncommuting moving-axis rotations, not seam-end matching or repeated-face transfer. The old A prior hypothesis predates C01 outputs; new preset A follows these five new hinge roles, not C01 relabeling.',
        'Identical-square foldability to any cube has no target artwork or color-matching rule. Existing red/blue hinge ink rotates with the original paper; every valid net including A still has its explicit six-face cube construction and D still overlaps. All six squares and all free outer boundaries remain black and readable. Each of the five marks is one step of the full hinge path; omitting either blue turn would hide the moving-axis explanation.')

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='second':second()
    else:first()
