from pathlib import Path
from datetime import datetime,timezone
import json

OUT=Path(__file__).resolve().parent
answers={
'Solid148/false_roll_pair':['A','D'],'Solid148/paired_bars':['A','B'],
'Solid155/projected_diagonal_count':['10','10'],'Solid165/red_quadrilateral':['180','C'],
'Solid175/false_roll_pair':['B','B'],'Solid176/false_flap_pair':['D','D'],
'Solid176/minimal_top_pair':['D','E'],'Solid176/two_color_lid_pairing':['D','A'],
'Solid180/bounding_dimension_capture':['273','216'],'Solid183/projected_diagonal_count':['10','11'],
'Solid202/red_quadrilateral':['B'],'Solid208/triangle_section_capture':['7','29'],
'Solid210/height_slant_pair':['C','C'],'Solid217/false_face_pair':['C','C'],
'Solid218/cut_pyramid_capture':['B','D'],'Solid219/quarter_cut_capture':['E','D'],
'Solid220/false_face_pair':['A','A'],'Solid220/separate_face_dot_pair':['E','E'],
'Solid220/separate_face_edge_pair':['E','E'],'Solid221/invalid_position_capture':['2','6'],
'Solid223/large_face_group':['14','14'],'Solid228/false_net_edge_pair':['A','D'],
'Solid228/stair_end_pair':['E','B'],'Solid229/false_face_pair':['A','D'],
'Solid229/paired_bars':['A','A'],'Solid229/two_color_opposite_pairing':['A','A'],
'Solid237/false_projected_face_pair':['A','C'],'Solid237/green_face_capture':['A','A'],
'Solid243/equal_color_diagonal':['45','45'],'Solid243/equilateral_capture':['45','45'],
'Solid244/rectangular_base_capture':['120','120'],'Solid248/diameter_completion':['5','5'],
'Solid80/removed_vertex_marker':['10','10'],'Solid84/false_cross_pair':['C','C'],
'Solid84/symbol_similarity_capture':['E','D'],'Solid95/pillar_height_capture':['80','24']}
rows=[]
for design_file in sorted(OUT.glob('Solid*/*/design.json')):
    folder=design_file.parent;key=folder.relative_to(OUT).as_posix();design=json.loads(design_file.read_text(encoding='utf-8'))
    expected=str(design['expected_wrong_answer']);observed=answers.get(key,[])
    jobs=[]
    for job_file in sorted((folder/'tests').glob('*/run_0[12].json')):
        job=json.loads(job_file.read_text(encoding='utf-8'))
        jobs.append({'path':str(job_file),'status':job.get('status'),'finish_reason':job.get('finish_reason'),'truncated':job.get('truncated'),'elapsed_seconds':job.get('elapsed_seconds')})
    complete=len(jobs)==2 and all(j['status']=='completed' for j in jobs)
    hit_count=sum(a==expected for a in observed)
    if key=='Solid220/false_face_pair':status='HOLD_QUALITY_shared_edge_frames_only_Z'
    elif key=='Solid176/false_flap_pair':status='TWO_HITS_SECOND_REVIEW_RECOMMENDED_by_parent_team'
    elif key=='Solid202/red_quadrilateral':status='DISQUALIFIED_run1_correct_run2_aborted_after_long_wait'
    elif complete:status='DISQUALIFIED_not_two_predeclared_hits'
    elif (folder/'candidate.png').is_file():status='PREPARED_NOT_TESTED'
    else:status='RENDER_FAILED_GENERIC_SOLID_ADAPTER_no_API'
    row={'candidate':key,'question_id':design['question_id'],'expected_wrong_answer':expected,'observed_final_answers_agent_reviewed':observed,'completed_two_runs':complete,'predeclared_hits':hit_count,'strict_two_hit_condition':complete and hit_count==2,'quality_status':status,'design_path':str(design_file),'plugin_path':str(folder/'plugin.json') if (folder/'plugin.json').is_file() else None,'image_path':str(folder/'candidate.png') if (folder/'candidate.png').is_file() else None,'tests':jobs,'approval_status':'No user Pass/Collect; runtime only.'}
    rows.append(row)
controls=[]
for folder,answer in [('Solid220/false_face_pair','E'),('Solid176/false_flap_pair','B')]:
    controls.append({'candidate':folder,'original_image_control_answer':answer,'formal_correct': 'E' if '220' in folder else 'C','evidence':[str(f) for f in (OUT/folder/'baseline_control/tests').glob('*/summary.json')]})
baseline_file=OUT/'bridge_baseline_inventory.json'
baseline=json.loads(baseline_file.read_text(encoding='utf-8')) if baseline_file.is_file() else None
report={'written_at':datetime.now(timezone.utc).isoformat(),'candidate_count':len(rows),'rendered_candidate_count':sum(r['image_path'] is not None for r in rows),'completed_two_run_candidates':sum(r['completed_two_runs'] for r in rows),'raw_two_hit_candidates':sum(r['strict_two_hit_condition'] for r in rows),'independent_review_delivery_candidate':'Solid176/false_flap_pair','held_raw_two_hit_candidate':'Solid220/false_face_pair','pending_bridge_candidates':[r['candidate'] for r in rows if r['quality_status']=='PREPARED_NOT_TESTED'],'controls':controls,'dedicated_bridge_baseline_totals':{k:baseline[k] for k in ['total','baseline_ok','baseline_failed']} if baseline else 'in_progress','candidates':rows,'continuation':'No running API processes at checkpoint. Do not re-use any old two-hit response for a changed PNG/plugin. Do not repeat a failed same-image request to obtain a more favorable pair. For a new candidate, predeclare wrong answer, render with baseline/frozen-input guards, run independent quicktest3 twice, compare final answers, run one original-image control after two hits, and submit to independent second review. No Pass/Collect or library writes.'}
(OUT/'CHECKPOINT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['candidates','controls']},ensure_ascii=False))
