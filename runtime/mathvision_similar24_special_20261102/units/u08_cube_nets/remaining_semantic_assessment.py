from worker import *

save(OWN/'Solid228/remaining_semantic_assessment.json',{
    'created_at':now(),
    'status':'UNRESOLVED_NO_PRIMARY_CANDIDATE',
    'not_an_impossibility_claim':True,
    'original_proved_unique':'D, repeated destination +y for cells(1,2)and(3,0); A/B/C/E each six distinct face normals',
    'new_tested_hypotheses':[
        {'variant':'C01_staggered_wing_seam_pair','preset':'E','observed_complete_finals':['A','A'],'result':'miss/miss; unchanged E preset'},
        {'variant':'C03_exact_moving_hinge_axis_path','preset':'A','observed_complete_finals':['D','B'],'result':'miss/miss; unchanged A preset'}
    ],
    'pretest_error_preserved':'C02_moving_hinge_axis_accumulation: incorrect local target IDs, rejected without render or request; C03 implements exact intended hinges with new immutable evidence',
    'earlier_history':'Three older tested frozen images remain forbidden: staircase free-edge pairing, staircase terminal rims, B repeated-face transfer from D. Full raw responses read and preserved by hash.',
    'remaining_directions_examined':[
        {'idea':'Shift the E free-wing same-color pairing to C','disposition':'No new information hypothesis: both are staggered wings on an intact four-square belt; merely changing recipient does not fix the failed false seam-equality premise. Not created or called.'},
        {'idea':'Re-highlight B opposite wings as same-face overlaps','disposition':'Duplicates old r25 same-face-overlap transfer; no material new mapping. Not created or called.'},
        {'idea':'More terminal A perimeter segments or color/line-width swaps','disposition':'Same old endpoint closure hypothesis or cosmetic retest. Not created or called.'},
        {'idea':'Added points or closed auxiliary cells to make C appear incompatible','disposition':'No justified existing-point correspondence that predicts one wrong answer without imposing color equality or a fake partition. This would substitute unsupported salience/new givens for information. Not created or called.'},
        {'idea':'Highlight D actual overlapping-face pair','disposition':'Valid explanatory comparison supports the true answer D, but supplies no credible specified wrong-answer hypothesis for this Special objective. Not used as a forced test.'}
    ],
    'why_unfinished':'Both genuinely new targeted hypotheses failed. At this checkpoint there is no further independently justified useful correspondence distinct from these or the three old failures. This is not proof that no future Special exists; retain unresolved for parent research. No arbitrary candidate-count limit or quota-saving rule applied.',
    'actual_new_calls':4,'errors_or_aborts':0,'independent_second_review':False,'formal_actions':0
})
cp=read(OWN/'checkpoint.json')
cp['questions']['Solid228']={'status':'unresolved_no_primary','reason_path':str(OWN/'Solid228/remaining_semantic_assessment.json'),'actual_new_api_calls':4,'pretest_rejections':1}
checkpoint(questions=cp['questions'])
