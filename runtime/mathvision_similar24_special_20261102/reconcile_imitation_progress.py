"""Reconcile delivered terminal evidence without polling active delegates."""
from datetime import datetime, timezone
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
units = {
 'u01_fold_locations': {'questions':['Plane202','Plane238','Plane461'], 'tested_images':6, 'complete_calls':12, 'partial_calls':0, 'primary_candidates':['Plane461'], 'parent_audit':'parent_audits/native_u01_u04/audit.json'},
 'u02_pieces': {'questions':['Plane218','Plane398'], 'tested_images':4, 'complete_calls':6, 'partial_calls':1, 'primary_candidates':[], 'parent_audit':'recovery_u02_preparation/recovery_assignment.json', 'note':'One preserved IncompleteRead; two existing p03 drafts remain untested. Recovery is offline preparation, not independent review.'},
 'u03_points': {'questions':['Plane211','Plane364','Plane423'], 'tested_images':7, 'complete_calls':14, 'partial_calls':0, 'primary_candidates':[], 'parent_audit':'parent_audits/native_u03_u06/audit.json'},
 'u04_angles': {'questions':['Plane321','Plane490'], 'tested_images':4, 'complete_calls':8, 'partial_calls':0, 'primary_candidates':['Plane321'], 'parent_audit':'parent_audits/native_u01_u04/audit.json'},
 'u05_surface': {'questions':['Solid186','Solid226'], 'tested_images':4, 'complete_calls':8, 'partial_calls':0, 'primary_candidates':[], 'parent_audit':'parent_audits/u05_surface.json'},
 'u06_fold_cut': {'questions':['Solid146','Solid174','Solid239','Plane220'], 'tested_images':7, 'complete_calls':14, 'partial_calls':0, 'primary_candidates':[], 'parent_audit':'parent_audits/native_u03_u06/audit.json'},
 'u07_corner_cut': {'questions':['Plane194','Plane245'], 'tested_images':6, 'complete_calls':12, 'partial_calls':0, 'primary_candidates':[], 'parent_audit':'parent_audits/native_u07_u08/audit.json'},
 'u08_cube_nets': {'questions':['Solid187','Solid193','Solid228'], 'tested_images':8, 'complete_calls':16, 'partial_calls':0, 'primary_candidates':[], 'parent_audit':'parent_audits/native_u07_u08/audit.json'},
 'u09_octa_nets': {'questions':['Solid166','Solid240'], 'tested_images':12, 'complete_calls':24, 'partial_calls':0, 'primary_candidates':['Solid166'], 'parent_audit':'parent_audits/native_u09/audit.json', 'note':'Solid240 HOLD for orientation uniqueness, zero calls; do not repair or explore it.'},
 'root_and_native_Plane213': {'questions':['Plane213'], 'tested_images':2, 'complete_calls':4, 'partial_calls':0, 'primary_candidates':[], 'note':'Exact current user233 image transfer B/C missed preset C; separate existing-exterior-notch imitation B/E missed preset B. Separate u11 continuation is cancellation requested, not counted here.'},
 'u12_surface_material_followup': {'questions':['Solid186','Solid226'], 'tested_images':2, 'complete_calls':4, 'partial_calls':0, 'primary_candidates':[], 'parent_audit':'parent_audits/u12_surface_material_followup.json', 'note':'Two previously prepared drafts tested once each pair before latest narrowing; no more surface alternatives.'},
}
for unit, value in units.items():
    value['status'] = 'COMPLETED_PRIMARY_ONLY' if value['primary_candidates'] else 'COMPLETED_UNQUALIFIED_OR_HELD'
    value['further_research'] = 'NONE_SCHEDULED_AFTER_IMITATION_STEERING'
units['u11_plane213_continue'] = {'questions':['Plane213'], 'status':'CANCEL_REQUESTED_PENDING_TERMINAL_CALLBACK', 'complete_calls':None, 'tested_images':None,
                               'note':'Do not poll. Reconcile only when terminal result is delivered. No replacement research task.'}
complete = sum(v.get('complete_calls') or 0 for v in units.values())
partial = sum(v.get('partial_calls') or 0 for v in units.values())
images = sum(v.get('tested_images') or 0 for v in units.values())
assert complete == 122 and partial == 1 and images == 62
task = json.loads((HERE/'task.json').read_text(encoding='utf-8-sig'))
question_rows = []
for qid in task['scope']:
    primary = qid in ['Plane461','Plane321','Solid166']
    question_rows.append({'question_id':qid, 'status':'PRIMARY_PENDING_NEW_INDEPENDENT_REVIEW' if primary else ('UNRESOLVED_CANCELLATION_RECONCILIATION_PENDING' if qid=='Plane213' else 'NO_QUALIFIED_DELIVERY'),
                          'qualified_delivered':False, 'Pass_or_Collect_performed':False})
outcomes = {'updated_at_utc':now, 'units':units, 'question_outcomes':question_rows,
            'latest_user_instruction':'以模仿为主就好，不要探索太多了。',
            'new_research_tasks_scheduled_after_latest_steering':0,
            'new_solver_calls_scheduled_after_latest_steering':0,
            'qualification_note':'Three paired-hit PRIMARY candidates still require NEW independent second review. Failed variants remain failures.'}
(HERE/'unit_outcomes.json').write_text(json.dumps(outcomes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
progress = {'updated_at_utc':now, 'scope_count':24, 'current_reference_count':9,
            'terminal_units_consumed':['u01_fold_locations','u02_pieces','u03_points','u04_angles','u05_surface','u06_fold_cut','u07_corner_cut','u08_cube_nets','u09_octa_nets'],
            'remaining_research_continuation':'u11_plane213_continue cancellation requested; no polling or replacement',
            'known_completed_new_calls_excluding_unreconciled_u11':complete,
            'known_partial_calls_excluding_unreconciled_u11':partial,
            'known_requests_excluding_unreconciled_u11':complete+partial,
            'known_tested_images_excluding_unreconciled_u11':images,
            'known_pending_independent_reviews':['Plane461','Plane321','Solid166'],
            'independent_review_dispatch_status':'PREPARED_NOT_LAUNCHED; parent finishing finite native audits',
            'qualified_delivered_this_task':0, 'new_research_tasks_scheduled':0,
            'latest_user_steering_applied':True,
            'untested_prepared_drafts':'Plane218 p03 held for imitation distance; Plane398 p03 first pair deferred to reduce exploration',
            'old_general_exploration_remains_paused':True, 'no_formal_state_writes':True,
            'counts_limitation':'These are known counts from consumed terminal units and the parent, not a complete count for an unreconciled continuation.'}
(HERE/'latest_progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (HERE/'continuation.txt').open('a',encoding='utf-8') as stream:
    stream.write('\n'+now+' Latest imitation-first steering applied. No replacement exploration or new solver calls. Existing PRIMARY Plane461, Plane321, Solid166 evidence preflight passed; NEW independent reviews prepared, pending launch after native finite audits. u11 cancellation requested; do not poll. Two u02 p03 drafts remain untested. Known consumed counts 122 complete + 1 partial, excluding unreconciled u11.\n')
print(json.dumps({'known_complete_calls':complete, 'known_partial_calls':partial, 'PRIMARY':['Plane461','Plane321','Solid166'], 'qualified':0, 'new_solver_calls':0}))
