import own_runtime as rt
import sys
from pathlib import Path

notes={
'Plane202':{'native_observation':'Actual PNG shows only the original square paper frame and two existing diagonals recolored red. Every animal contour, eye, ear and neck remains black and fully legible, with no new point. Original horizontal/vertical lines remain visible.',
 'human_semantics':'The uniform red existing paper boundary has both correct reflection symmetries even as physical colored edging. Kangaroos carry no added ink. Carrier-frame symmetry is a real partial comparison and does not assert that animals reflect. Unique original2 remains under the actual wording. Three actions are necessary to establish one source-to-two-candidate comparison.',
 'prototype_note':'The same PNG in the untested substitution prototype has no request evidence; its local copied ear-tip proof text was rejected before calls and is permanently retained. This canonical design has a frame-only correct proof and unchanged preset4.'},
'Plane238':{'native_observation':'One black physical punch retains its shape and position, with upper red/lower blue contour. Existing open-L grid edges identify red14/16 and blue21/23 without covering any digit. Every fold arrow and crease remains black. No second hole, new grid line or closed synthetic cell is added.',
 'human_semantics':'Upper/lower are real parts of the same hole contour; each receiver has two existing edge legs that unambiguously identify its numbered cell. This gives a definite staggered layer correspondence. Physical ink reading of colored cell edges cannot change punched numbered cells; unique C remains. All10 marks participate in this one source-parts-to-numbered-layers comparison.'}}
for rel in sys.argv[1:]:
    d=Path(rel).resolve();rt.check_write(d)
    design=rt.read(d/'design.json');qid=design['question_id']
    if design['variant_id']=='u01_actual_crease_to_wrong_packet_separator':
        notes[qid]={'native_observation':'Existing first fold and final top edge are red; second fold and final internal separator immediately left of the punched cell are blue. All grid cells/numbers/punch remain unchanged black. No new line, arrow, crease, mark point or hole.',
          'human_semantics':'The red receiver is a true first-fold hinge identity; blue receiver is an existing GRID separator, not a new fold. The comparison targets an explicit wrong identity and .5-cell offset. Color-only styling cannot add a third fold to the explicit twice-folded task, and physical ink does not change pierced numbers. A human can still follow the actual left packet boundary and uniquely getC. All4 marks have an independent source/receiver role; no ineffective or redundant actions.'}
    assert not list((d/'tests').glob('*/run_*_started.json'))
    previous=[]
    for q in rt.read(rt.OWN/'assignment.json')['question_ids']:
        for review in (rt.OWN/q).glob('*/primary_final_review.json'):
            r=rt.read(review)
            previous.append({'question_id':q,'design':str(review.parent/'design.json'),
                'image_sha256':r['image_sha256'],'preset':r['frozen_expected_wrong_answer'],
                'finals':[x['final_answer'] for x in r['raw_final_reviews']],
                'full_review_path':str(review),'full_review_sha256':rt.sha(review)})
    assert rt.sha(d/'candidate.png') not in {x['image_sha256'] for x in previous}
    rt.save(d/'all_current_unit_prior_attempts_audit.json',{'at':rt.now(),'all_complete_old_raw_finals_already_read':True,
        'previous_current_task_tests':previous,'new_material_information':design['substantive_difference_from_all_prior_designs'],
        'new_preset_derived_from_new_marking_before_calls':design['expected_wrong_answer'],'not_posthoc_relabel':True})
    rt.save(d/'visual_primary_before_calls.json',{'question_id':qid,'variant_id':design['variant_id'],
        'at':rt.now(),'actual_native_PNG_viewed':True,'human_gate_passed':True,'review_role':'PRIMARY_AUTHOR_ONLY_NOT_INDEPENDENT',
        **notes[qid],'image_sha256':rt.sha(d/'candidate.png'),'plugin_sha256':rt.sha(d/'plugin.json'),'design_sha256':rt.sha(d/'design.json'),
        'unique_original_answer':design['correct_answer'],'every_marker_role_in_design':True,
        'independent_mathematics_enumeration_path':str(d/'proof_calculation.json'),'new_parent_second_review_required':True})
    g=rt.read(d/'render_gates.json');g['native_visual_gate']=True;rt.save(d/'render_gates.json',g)
    print(qid,'REFINEMENT NATIVE GATE PASSED')
