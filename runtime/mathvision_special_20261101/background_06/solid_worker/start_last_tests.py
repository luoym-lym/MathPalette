from tools_local import *
for q,v,notes in [
('Solid119','white_domino_local_column_binding','Actually viewed exact original and candidate PNG. Source white brick rails/red-blue and cap/green bind to D front white column. White/gray fill, D extra rear white region, every seam and all labels remain clearly visible; no volume or count changes.'),
('Solid137','two_white_domino_local_bindings','Actually viewed exact original and candidate PNG. Two real white source bricks red/blue long edges bind to two actual white2-cell subsets in C. C extra fifth white cube on right side remains unmodified and visible, as do all original fills, seams, brick count and choice labels.')]:
    folder=TASK/q/v
    write(folder/'primary_visual_review.json',{'question_id':q,'variant_id':v,'checked_at':datetime.now(timezone.utc).isoformat(),'actually_viewed_exact_candidate':True,'candidate_sha256':file_hash(folder/'candidate.png'),'notes':notes,'human_gate':'Original unique solution/readable givens preserved; no human performance claim.','independent_review':False})
q='Solid142';folder=TASK/q/'original_control';folder.mkdir(exist_ok=False)
(folder/'original.png').write_bytes(AD.original_paths[q].read_bytes())
write(folder/'design.json',{'question_id':q,'variant_id':'original_control','expected_wrong_answer':'A','formal_correct_answer':'C','role':'Separate optional no-marker original control only; not a candidate, no post-output preset or count selection.','created_at':datetime.now(timezone.utc).isoformat(),'original_png_sha256':file_hash(folder/'original.png')})
