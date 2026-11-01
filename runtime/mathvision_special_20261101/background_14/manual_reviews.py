from tools import *
known={
('Solid125','three_plane_area_binding'):[('8/3 kg',False,'Explicit final8/3kg; not predeclared4.5. Narrative invents4tunnel walls, so wrong but a preset miss.'),('12 kg',False,'Explicit final12kg; not4.5. Unit-face versus full-face arithmetic error; preset remains unchanged.')],
('Solid147','white_terminal_tripod_binding'):[('E',True,'Explicit finalE and bodyE; matches immutableE preset. It cites red/blue source-to-option correspondence, but does not prove causal impact.'),('B',False,'Explicit finalB; describes a3cubeL despite stated4cubes. E is only discussed as rejected option, not final. Miss.')],
('Solid86','white_face_identity_swap'):[('14',False,'Explicit final14; wrong source depth and visible count, not preset3.'),('1',False,'Read entire lengthy self-correcting final answer. Final1 repeats12-11=1. Earlier9/12/3 counts are incidental; not preset3.')],
('Solid190','vertical_column_ownership_binding'):[('D',False,'Explicit finalD; mislabels choiceD as straight bar. It is not predeclaredB.'),('C',False,'Explicit finalC agrees formal answer, though narrative invents3x3x2and2voids. No presetB final.')],
('Solid160','contact_plane_multiplicity_merge'):[('64 cm2 (B)',False,'Read the complete long answer, including intermediate80andoptionA. It ultimately recalculates16exposedfaces and explicitly concludes64cm2, matchingB and not presetA.'),('B (64 cm2)',False,'Explicit Correct AnswerB with16faces*4=64, notA.')],
('Solid126','remaining_height_to_cut_binding'):[('A (0%)',False,'Explicit finalA and0percent. PredeclaredC remains unchanged even though both independent answers agreedA.'),('A (0%)',False,'Explicit finalA and0percent. It mistakes remaining width3for cutwidth, then uses corner cancellation. Wrong but notpresetC.')],
('Solid226','three_new_face_visibility_binding'):[('C (the same)',False,'Explicit finalC and0net area, formal correct; narrative calls it corner but final agrees. MisspresetE.'),('D (1 more)',False,'Explicit Answer1more maps unambiguously toD. It is not presetE/2more. No inconsistent letter/value pair in the final.')],
('Solid196','visible_face_unit_binding'):[('64 cm2',False,'Read complete answer; final64cm2. Intermediate24/16face recounts do not make preset32a final.'),('64 cm2',False,'Final64cm2; alternative calculation briefly reaches72then corrects4interfaces. Misspreset32.')]
}
for (q,v),interpretations in known.items():
    folder=TASK/q/v;dest=folder/'manual_final_review.json'
    if dest.exists():continue
    paths=sorted(folder.glob('tests/*/run_??.json'));assert len(paths)==2,(q,len(paths))
    results=[]
    for p,(final,hit,note) in zip(paths,interpretations):
        r=read(p);assert r['status']=='completed' and not r.get('truncated')
        results.append({'run_path':str(p),'run_sha256':file_hash(p),'raw_response_path':str(p.with_name(p.stem+'_response.json')),'raw_response_sha256':r['response_sha256'],'complete_answer_read_manually':True,'complete_final_answer_text':r['answer'],'manually_extracted_final':final,'matches_predeclared_wrong_answer':hit,'interpretation':note,'finish_reason':r['finish_reason']})
    write(dest,{'question_id':q,'variant_id':v,'image_sha256':file_hash(folder/'candidate.png'),'design_sha256':file_hash(folder/'design.json'),'preset':read(folder/'design.json')['expected_wrong_answer'],'manual_results':results,'credible_paired_hit':all(r['matches_predeclared_wrong_answer'] for r in results),'status':'paired_preset_miss','preset_changed_after_outputs':False,'no_retry':True,'approval_status':'No approval/publication.'})
print('Saved manual reviews for8complete pairs.')
