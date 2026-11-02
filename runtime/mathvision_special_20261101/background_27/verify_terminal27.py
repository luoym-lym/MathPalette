from tools27 import *
import numpy as np

q='Plane444';ob={o['id']:o for o in json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'))['objects']}
src=np.array(ob['o2']['points'])-[15,19];c=np.array(ob['o11']['points'])-[40,9]
expected=src[:,[1,0]]+[-5,0]
assert {tuple(p) for p in expected}=={tuple(p) for p in c}
write(HERE/q/'wrong_C_anchor_exact_proof.json',{'all10_vertices_checked':True,'source_local_vertices':src.tolist(),
    'true_transformed_vertices':src[:,[1,0]].tolist(),'C_local_vertices':c.tolist(),'C_translation_from_true':[-5,0],
    'exact_full_set_equality_after_translation':True,'original_origin_fixed_by_all3_requested_operations':True})

q='Plane371';ob={o['id']:o for o in json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'))['objects']}
mapping=[(1,69),(2,67),(3,68),(4,66),(5,65),(6,63),(7,64),(8,61),(9,62),(10,59),(11,60),(12,57),(13,58)]
errors=[]
for i,j in mapping:
    a=np.array(ob[f'o{i}']['points']);b=np.array(ob[f'o{j}']['points'])
    a=a-(a.min(0)+a.max(0))/2;b=b-(b.min(0)+b.max(0))/2
    err=float(np.max(np.linalg.norm(a*[1,-1]-b,axis=1)));assert err<1e-12
    errors.append({'source':f'o{i}','D_target':f'o{j}','centered_ordered_vertex_vertical_flip_error':err})
write(HERE/q/'D_reversed_slots_exact_proof.json',{'all13_glyph_contours_and_white_counters_checked':True,'errors':errors,
    'D_slot_order':'OORAGNAK','source_and_correct_E_slot_order':'KANGAROO','D_local_glyph_transform':'vertical reflection',
    'misconception':'Fails to cancel the two separate word-order reversals while performing the local glyph vertical flips.'})

metadata={}
for filename in ['inventory.json','remaining_questions.jsonl','exploration_report.json']:
    p=BASE/filename
    if p.suffix=='.jsonl':
        d=rows(p);data=[r for r in d if r.get('question_id',r.get('id')) in ASSIGNED]
    else:
        d=json.loads(p.read_text(encoding='utf-8-sig'))
        def relevant(v):
            if isinstance(v,dict):
                if v.get('question_id',v.get('id')) in ASSIGNED:return v
                out={k:relevant(x) for k,x in v.items()};return {k:x for k,x in out.items() if x not in (None,{},[])}
            if isinstance(v,list):return [x for x in (relevant(x) for x in v) if x not in (None,{},[])]
            return None
        data=relevant(d)
    metadata[filename]={'sha256_at_read':file_hash(p),'assigned_question_entries':data,'classification':'mutable diagnostic runtime metadata, never frozen source evidence'}
write(HERE/'focused_runtime_metadata_read.json',metadata)

checkpoint=json.loads((HERE/'checkpoint.json').read_text(encoding='utf-8'))
queue=json.loads((HERE/'second_review_queue.json').read_text(encoding='utf-8'))
assert checkpoint['actual_assessed_question_ids']==ASSIGNED and not checkpoint['unworked_question_ids'] and not queue['candidates']
starts=list(HERE.glob('Plane*/r27_*/tests/quicktest3_*/run_*_started.json'))
responses=list(HERE.glob('Plane*/r27_*/tests/quicktest3_*/run_*_response.json'))
assert len(starts)==len(responses)==12
assert len(list(HERE.glob('Plane*/r27_*/api_process_finished.json')))==6
proc=json.loads((HERE/'process_audit.json').read_text(encoding='utf-8-sig'));assert proc['live_own_python_process_count']==0
assert all(json.loads(p.read_text(encoding='utf-8'))['both_preset_hits'] is False for p in HERE.glob('Plane*/r27_*/manual_final_review.json'))
write(HERE/'terminal_verification.json',{'stage':'material_refinement','verified_at':now(),'all8_assessed':True,'unworked':[],
    'exact6_frozen_designs_12_started_and12_complete_raw_replies':True,'new_raw_full_finals_manually_read':True,
    'zero_credible_doublehits_empty_parent_queue':True,'zero_live_own_API_processes':True,
    'source_and_old_evidence_unchanged_audit':'source_preservation_final.json','additional_exact_geometric_proofs':['Plane444/wrong_C_anchor_exact_proof.json','Plane371/D_reversed_slots_exact_proof.json'],
    'screening_math_correction':'Plane318/primary_math_correction.json','no_pass_collect_approval_publication_or_independent_review_actions':True,
    'checkpoint_sha256':file_hash(HERE/'checkpoint.json'),'queue_sha256':file_hash(HERE/'second_review_queue.json')})
print(json.dumps({'terminal_verified':True,'all8_assessed':True,'calls':12,'queue':0,'live_API':0}))
