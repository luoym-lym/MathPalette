from own_bootstrap import *
from unit_tools import eligibility

directory=OWN/'Solid166/r01_terminal_x_three'
directory.mkdir(parents=True,exist_ok=False)
e=eligibility('Solid166')
save(directory/'eligibility_before_design.json',e,exclusive=True)
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
        'description':'Compare the existing x edge with the existing edge labelled 3 using one shared color.',
        'intent':'Track two concrete terminal-flap boundaries while retaining all original fold geometry.',
        'params':{'actions':[{'type':'set_object_style','target':'netedge15','color':'#DC2626'},
                             {'type':'set_object_style','target':'netedge13','color':'#DC2626'}]}}
save(directory/'plugin.json',plugin,exclusive=True)
transfer={'reference_question_id':'Solid203','reference_directory':str(TASK/'references/Solid203'),
    'actual_current_C01_png_viewed':True,'all_nine_current_PNGs_viewed':True,
    'reference_png_sha256':sha(TASK/'references/Solid203/C01.png'),
    'reference_plugin_sha256':sha(TASK/'references/Solid203/C01.json'),
    'current_actions':'line_20 (x) and line_8 (upper-left C) red, default 1pt; no blue, no highlighted A.',
    'migration':'Rebind the two separated terminal-flap outer edges to the actual Solid166 context: x=netedge15 and upper-left numbered 3=netedge13. Both represent named candidate seam boundaries on the original net. Independently recomputed all eight folds; actual coincident edge is 5.',
    'independent_formal_problem':'Solid166 is a number-answer question with labels1..5, source MathVision test:1433; reference is a different choice question test:1943 with A..E. Current reference suggests a pair to inspect, not a correct seam or evidence of a model effect.',
    'not_legacy_delivered_method':'Old18 Solid203 used another option; current frozen user C01 explicitly uses C. No old18 color/option preset is imported.',
    'roles':[{'action_index':0,'source':'actual target edge x','target':'netedge15','use':'Defines the queried boundary as the comparison source.'},
             {'action_index':1,'source':'red comparison source x','target':'netedge13, edge3','use':'Identifies a particular boundary on the opposite terminal flap for candidate seam comparison; paired source prevents isolated option salience.'}],
    'human_readability':'Only two existing entire edges recolored. No extra cuts, line dashes, nodes, labels, filled regions or equality symbols. 3 and x remain legible. Color as printed paper edging leaves the physical fold and requested edge identity unchanged; colors are not a required matching rule.',
    'minimality':'Two actions, one per distinct original edge; neither redundant nor covered, no arbitrary line count rule.'}
save(directory/'reference_transfer.json',transfer,exclusive=True)
hist=load(OWN/'history_selected.json')
audit={'question_id':'Solid166','all_known_old_designs':[],
       'all_saved_unique_old_started_calls':2,'full_raw_read':True,'old_manual_finals':['3','4'],'old_preset':'1','old_hit_count':0,
       'old_aborted_failed_transport_count':0,'no_saved_independent_special_review':True,
       'disposition':'Never retest old x–1 PNG a31f8ad7...; retain aliases as one two-call attempt.',
       'new_material_difference':'Receiver boundary changes from upper-right edge1 (netedge11) to upper-left terminal-flap edge3 (netedge13). This changes endpoint identity and the proposed seam correspondence; it is not a color/linewidth-only repeat.',
       'cross_question_authorized_transfer':'Current user9 reference edge correspondence is explicitly authorized for this new formal problem. No history response is counted for Solid166 r01.',
       'new_png_hash_check_pending_render':True}
for q in hist:
    if q['question_id']=='Solid166':
        audit['all_known_old_designs']=[{'path':d['design_path'],'sha256':d['design_sha256'],'variant':d['variant_id'],
            'preset':d['predeclared_wrong_answer'],'png':d['frozen_candidate_png_sha256'],'started_calls':d['unique_started_call_count_from_saved_records'],
            'new_correspondence_differs':True} for d in q['designs']]
save(directory/'history_difference.json',audit,exclusive=True)
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':'r01_terminal_x_three','created_at':now(),
    'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number',
    'expected_wrong_answer':'3','preset_semantics':{'letter':None,'value':'3','meaning':'The edge bearing identifier 3, not the third edge encountered or a length.'},
    'information_hypothesis':'The shared-red pairing of target x and the opposite upper-left flap boundary3 may be mistaken for a seam correspondence, yielding edge3. That proposed identity is false: propagation gives x endpoints {-e1,+e3}, edge3 endpoints {+e1,-e3}.',
    'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
    'primary_unique_correctness':'All five labelled candidates exhaustively compared in primary_math.json; only edge5 has both folded endpoints equal to x. Global rigid orientation or folding the paper to its other side preserves equality.',
    'plugin_sha256':sha(directory/'plugin.json'),'reference_transfer_path':str(directory/'reference_transfer.json'),
    'reference_transfer_sha256':sha(directory/'reference_transfer.json'),'history_difference_path':str(directory/'history_difference.json'),
    'history_difference_sha256':sha(directory/'history_difference.json'),
    'eligibility_sha256':sha(directory/'eligibility_before_design.json'),
    'human_semantics_and_mark_roles':transfer['roles'],
    'paper_edge_reading':'Colored ink on the boundary does not impose a seam constraint or change the convex octahedron; the question never says to match colors and contains no result-picture alternatives. Answer remains5 under literal colored-paper folding.',
    'two_run_rule':'Exactly two original isolated quicktest3 calls after all offline gates; both full final values must be3, no other numeral/choice substitution, no third call or relabelling.',
    'scope':'PRIMARY research only; no independent second review, approval, Pass, Collect or delivery.'}
save(directory/'design.json',design,exclusive=True)
cp=load(OWN/'checkpoint.json');cp.update(phase='offline_candidate_gates',updated_at=now())
cp['questions']['Solid166']={'status':'r01_design_frozen','candidate_directory':str(directory),'preset':'3','calls':0}
cp['questions']['Solid240']={'status':'HOLD_ORIGINAL_ORIENTATION_UNIQUENESS','calls':0,
    'reason':'One marked face leaves three proper orientations; right neighbor1/2/6. Frozen metadata assumes Q_apex_maps_to_T but no vertex binding is visible.',
    'evidence':str(OWN/'Solid240/primary_math_and_orientation_hold.json')}
cp['holds']=['Solid240'];save(OWN/'checkpoint.json',cp)
print('Design/plugin/roles/history/preset frozen',str(directory))
