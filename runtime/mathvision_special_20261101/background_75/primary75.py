import bootstrap75 as boot
from research75 import *
from designs75 import specifications
from math75 import scene,vertices
import os

NOTES={
 'Plane317':'Actual native PNG shows four unchanged black central cells and40 clear white fields. Each black cell has one thin red top edge and blue right edge; no white-region interior or domino partition is marked. The four homologous open corners are easy to compare. All narrow bridge unit boundaries remain visible. Same colors do not require synchronized stone choices; the explicit question still distinguishes a change at any single stone. The prediction2 is the intended error, not a new mathematical condition.',
 'Plane337':'Actual native PNG shows all16 board cells and all4 skew-template cells clearly. The marked source two-edge elbow sits at a concave notch; the receiver elbow is at the convex upper-right board corner. Only these existing perimeter unit segments are colored. They do not close a tetromino in the board, introduce a cut or hide a gridline. The template continues to denote its shape/mirror for cutting, rather than a colored physical picture that must match target ink. The two occupied-side roles are visibly different, leaving unique optimum3 pieces and4 squares.',
 'Plane385':'Actual native PNG shows exactly8 original black dots, including the empty lower-left lattice position. Two thin parallel red segments join existing dot pairs. P12-P21 is a true tilted-square side; P02-P11 is a unit-square diagonal and cannot be completed as a tilted side on these dots. No polygon, extra dot, relation symbol or crossing is drawn. Tiny red strokes meet dot centers, but all original black disks remain plainly identifiable. The requested total covers all possible joining segments, not only these two examples, so the unique original count4 remains readable.'
}

def main():
    old_pngs=[]
    for p in BASE.rglob('*.png'):
        if p.is_relative_to(OWN):continue
        if p.name in ('candidate.png','repeat.png'):
            old_pngs.append({'path':str(p),'sha256':sha(p.read_bytes())})
    put(OWN/'global_old_candidate_png_hash_audit.json',{'created_at':now(),'streamed_one_image_file_at_a_time':True,'all_old_candidate_repeat_pngs':old_pngs,'no_old_image_loaded_as_design_source':True})
    for q in ['Plane317','Plane337','Plane385']:
        n=specifications(q)[0];d=OWN/q/n
        design=read(d/'design.json');context=read(d/'fresh_context.json');bind=read(d/'marker_bindings.json');s=scene(q)
        edges=[]
        for o in s['objects']:
            if o['type']!='polygon':continue
            pts=vertices(s,o)
            for a,b in zip(pts,pts[1:]+pts[:1]):edges.append((o['id'],a,b))
        for b in bind:
            a,c=b['normalized_action']['endpoints']
            b['exact_existing_outline_edges']=[{'object_id':oid,'endpoints':[p,r]} for oid,p,r in edges if (a==p and c==r) or(a==r and c==p)]
            if q!='Plane385':assert b['exact_existing_outline_edges']
            b['native_paths_file']=str(d/'native_paths.json')
            b['native_paths_sha256']=sha((d/'native_paths.json').read_bytes())
        put(d/'marker_bindings.json',bind)
        assert not [v for v in old_pngs if v['sha256']==design['image_sha256']]
        put(d/'primary_review.json',{'review_role':'PRIMARY ONLY, not independent second review','reviewed_at':now(),'actual_source_JPG_viewed':True,'actual_formal_native_PNG_viewed':True,'actual_candidate_native_PNG_viewed':True,'viewed_size':[768,768],'native_readability_and_human_semantics':NOTES[q],'each_mark_review':bind,'new_vs_old_audit':str(d/'design_difference_audit.json'),'unique_original_math_proof':str(d/'math_proof_snapshot.json'),'expected_wrong_answer_predeclared':design['expected_wrong_answer'],'image_sha256':design['image_sha256'],'design_sha256':sha((d/'design.json').read_bytes()),'original_noop_pixels_equal':True,'candidate_repeat_byte_identity':(d/'candidate.png').read_bytes()==(d/'repeat.png').read_bytes(),'fresh_offline_replay_required_before_API':True,'proceed_to_two_calls':True,'global_old_failed_aborted_PNG_exact_hash_collision':False,'no_arbitrary_mark_cap':True,'no_control_correctness_or_causal_gain_hard_gate':True,'limitations':['Prediction is a testable hypothesis, not established solver mechanism.','No causal/statistical gain claimed; no unchanged controls repeated.','Any paired hit remains primary only and needs a NEW parent independent delegate before delivery.']})
        assessment=read(OWN/q/'assessment.json');assessment.update(status='new_design_primary_native_review_complete_pending_offline_replay',candidate_designs_created=1,candidate_directory=str(d),expected_wrong_answer=design['expected_wrong_answer'],candidate_designs_planned=1,status_final_for_assessment=True)
        put(OWN/q/'assessment.json',assessment)
    put(OWN/'global_zero_call_pretest_audit.json',{'created_at':now(),'own_unit_actual_API_calls':len(list(OWN.glob('Plane*/r75_*/tests/quicktest3_*/run_*_started.json'))),'all_candidate_call_directories_scanned':True,'no_connectivity_ping_or_original_control_calls':True,'old_history_calls_not_claimed_zero':True,'local_serialization_failures':[{'type':'TypeError ndarray','stage':'source path audit BEFORE render/PNG/API','recovered_local_output_representation':True},{'type':'TypeError Polygon artist handle','stage':'source path audit BEFORE render/PNG/API','recovered_local_output_representation':True}],'genuine_allocation_import_render_failures':[],'remote_errors':[],'old_draft_failures_preserved':str(OWN/'local_failures/native_path_serialization'),'no_failed_aborted_PNG_or_API_retried':True})
    cp=read(OWN/'checkpoint.json');cp.update(status='three_primary_designs_native_review_complete_offline_replay_pending',updated_at=now(),primary_assessments=[read(OWN/q/'assessment.json') for q in IDS],errors=[{'type':'recoverable_local_path_audit_serialization','count':2,'stage':'before PNG or API','preserved_at':str(OWN/'local_failures/native_path_serialization'),'recovered':True,'no_allocation_import_render_or_remote_failure':True}]);put(OWN/'checkpoint.json',cp)
    print(json.dumps({'primary_native_reviewed':3,'global_old_png_hashes':len(old_pngs),'current_API_calls':0}))

if __name__=='__main__':main()
