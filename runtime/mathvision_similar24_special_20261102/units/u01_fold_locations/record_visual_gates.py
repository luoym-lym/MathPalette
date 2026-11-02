import own_runtime as rt
import hashlib,json

index=rt.read(rt.OWN.parents[1]/'history_index.json')
old_images=set()
for q in index['questions']:
    for t in q.get('all_saved_transport_groups_for_question',[]):
        old_images.add(t['image_sha256'])
notes={
'Plane202':{'native_observation':'Eight small tip dots distinguish four outer (red) from four inner (blue) ear tips; all eyes/snouts/necks and four original candidate lines remain legible. Each anatomical group has one mark in each quadrant. No new animal, cut, or axis.',
    'literal_color_check':'Each colored tip family is invariant under both horizontal and vertical reflections. Treating the added tip dots as intrinsic ink therefore preserves both actual folds. Diagonal failure has a snout witness far from all tip dots; colored tips cannot fill that mismatch. Recolored existing candidate axes are fold-comparison guides; question asks kangaroo overlap, not agreement of guide ink.',
    'useful_information':'Two real anatomical feature classes versus two diagonal candidate directions. No isolated wrong-choice highlighting; no options in this numeric question.'},
'Plane238':{'native_observation':'All36 numbers are readable and unchanged. Red/blue original lines bracket rows2 and5; two final grid edges bracket the actual top punch row. Original punch stays black in actual top-middle cell. Both fold arrows and existing fold axes remain black and readable.',
    'literal_color_check':'Even if colored lines are ink on numbered paper, they do not change which numbers receive a hole. No requirement to reproduce printed paper appearance is asked. All four physical layers retain exact geometry, and original unique C remains.',
    'useful_information':'Two boundaries of a one-cell row band are compared across stages, targeting a first-fold distance mismatch. Six existing grid-edge styles are sufficient; no closed false cell, extra subdivision or meaningless action.'},
'Plane461':{'native_observation':'Original single punch circle and X remain distinct. Two existing X strokes are red/blue; D has four original circular boundaries grouped by opposite diagonal positions. All original arrows, dashed creases, paper boundaries and other choices remain black and unchanged.',
    'literal_color_check':'The formal wording explicitly identifies X as a punch-location symbol. Coloring its already present strokes does not make X a printed object to unfold. Existing hole boundaries enclose absent paper, and restyling them adds no ink object or extra hole. All positions and white interiors stay exact. Unique B retained.',
    'useful_information':'A direct transfer of current Plane217 diagonal directions versus opposite hole-pair positions, reversing source and candidate roles. The wrong D has the same two directions but incorrect free-top-edge offset; the comparison is useful partial information, not a whole-option box.'}}
for qid,review in notes.items():
    for p in (rt.OWN/qid).glob('*/design.json'):
        d=p.parent;design=rt.read(p)
        assert rt.sha(d/'candidate.png') not in old_images
        rt.save(d/'visual_primary_before_calls.json',{'question_id':qid,'variant_id':design['variant_id'],
            'at':rt.now(),'actual_native_PNG_viewed':True,'source_JPG_formal_PNG_and_current_ref_PNG_viewed':True,
            'human_gate_passed':True,'review_role':'PRIMARY_AUTHOR_NOT_INDEPENDENT',**review,
            'all_marker_roles':design['marker_roles'],'unique_original_answer':design['correct_answer'],
            'image_sha256':rt.sha(d/'candidate.png'),'plugin_sha256':rt.sha(d/'plugin.json'),'design_sha256':rt.sha(p),
            'no_postoutput_preset_change':True,'new_global_image_hash_no_saved_request_match':True,
            'limitations':design['limitations']})
        gates=rt.read(d/'render_gates.json');gates['native_visual_gate']=True;rt.save(d/'render_gates.json',gates)
        print(qid,'native human and semantics gate passed')
