from worker_env import *

variants={'Plane194':'r01_fold_axes_to_square_hole','Plane245':'r01_fold_motion_to_square_aperture'}
for qid,var in variants.items():
    folder=OWN/qid/var
    visual={
      'Plane194':'Actual 768px candidate viewed: source first vertical fold guide is red and second horizontal fold guide blue; original dash style is preserved. Only E aperture has two blue horizontal and two red vertical sides, with the same square aperture geometry. A/B/C/D, source cut, all source paper outlines and both discarded-corner ghost traces remain black and unchanged. No extra line, cut or region is introduced. All four possible corner classes remain represented by A/B/C/D.',
      'Plane245':'Actual 768px candidate viewed: upper/destination half of original first folding arrow is red, right/destination half of second folding arrow blue. Source arrowheads retain their black semantic fill. A square aperture horizontal edges are blue and vertical edges red. All source paper boundaries, fold dashes, original actual diagonal cut and discarded-corner ghost legs remain black; B diamond and all other samples retain original geometry and grayscale. The red and blue pieces are contiguous instruction-arrow portions, despite 25 native object IDs per arrow.'}[qid]
    semantic={
      'Plane194':'The fold dashes are operational guide axes, already shown only at the pre-fold construction stage; they are not original sheet edging or a printed picture to transport. A/B/C/D remain fully unchanged. E remains impossible even if its colored aperture sides are regarded as intrinsic edging, since a single straight corner clip cannot yield an axis-aligned central square aperture. The marking does not choose a particular corner. A new instruction legend is unnecessary and was not added.',
      'Plane245':'The source colors are confined to arrows conventionally specifying operations, not the folded material. The material paper remains unchanged black/gray, and B remains exactly its valid unfolding. If A colored hole edges are read as material ink, A still cannot have the required aperture shape, and that reading does not invalidate B. Thus no color-bearing moving physical source feature lacks an output counterpart.'}[qid]
    write(folder/'primary_review.json',{'reviewed_at':now(),'scope':'PRIMARY ONLY, not independent second review',
       'actual_formal_PNG_and_source_JPG_and_candidate_PNG_viewed':True,
       'all_current_nine_C01_PNGs_and_plugins_read':True,'unique_original_mathematics_independently_proved':True,
       'proof_path':str(OWN/qid/'mathematical_audit.json'),'visual_review':visual,'semantic_review':semantic,
       'each_mark_specific_source_receiver_purpose_checked':True,'conciseness':'Only connected direction-bearing source indicators and four existing candidate aperture edges. No ineffective overwritten action, arbitrary object alteration or invented cut.',
       'fresh_schema_defaults_noop_repeat_checked':True,'fresh_independent_process_exact_replay_required_before_request':True,
       'different_from_old_failed_PNG_and_material_hypothesis':True,'expected_wrong_answer':read(folder/'design.json')['expected_wrong_answer'],
       'proceed_to_exact_two_calls':True,'restrictions':['Only two calls to this frozen image','No retesting failed or interrupted exact input','No post-response relabeling','Any two-hit result remains PRIMARY and requires a new parent independent review','No Pass/Collect or delivery']},True)

audit=[]
for q in read(OWN/'assignment.json')['questions']:
    for path,expected in q['frozen_source_files_sha256'].items():
        p=PROJECT/path;item={'path':path,'sha256':sha(p),'matches_assignment':sha(p)==expected}
        if p.suffix=='.json':
            data=read(p);item['fully_read_and_parsed']=True
            if '/items/'+q['question_id']+'/' in path:
                item['content']=data
        audit.append(item)
for relative in ['annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json',
 'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
 'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']:
    p=OLD/relative;v=read(p)
    audit.append({'path':str(p),'sha256':sha(p),'fully_read_and_parsed':True,
       'relevant_objections':{k:x for k,x in v.items() if k in ('decision','rule','blocking_reason','concrete_objections','human_semantics')}})
write(OWN/'supplementary_source_and_semantics_audit.json',audit,True)
write(OWN/'checkpoint.json',{'updated_at':now(),'status':'primary_candidates_frozen_offline_gates_before_testing',
 'questions':{q:{'status':'frozen_primary_pending_two_calls','variant_id':v,'candidate_directory':str(OWN/q/v),'new_API_calls':0} for q,v in variants.items()},
 'new_API_calls':0,'second_review_queue':[],'limitations':['PRIMARY only','No formal data changes']})
print('Both primary reviews persisted; no API calls in this command')
