from design_tools import *
q='Solid94';old=TASK/q/'full_cut_to_shallow_corner_binding'
write(old/'primary_review.json',{'question_id':q,'actual_candidate_png_viewed':True,'proceed_to_API':False,'status':'rejected_before_API','reason':'The added top cut segment DE passes near/through original A label. The letter remains recognizable but a cleaner vertex-only hypothesis avoids this human-readability risk. No calls on this image.'})
c=json.loads((TASK/q/'context.json').read_text(encoding='utf-8'));sn={s['label']:s['xy'] for s in c['snap_points']}
paths=path_bindings(q,['optionC1516','optionC1517','optionC1617'])
edge15=paths['optionC1516'][0]['controls'][0];edge17=paths['optionC1517'][0]['controls'][0]
# Source D->C15; E->C16; B->C17. Retrieve exact scene snap coords, never the rounded drawing coordinates.
def exact_snap(approx):
 m=[s for s in c['snap_points'] if np.allclose(s['xy'],approx,atol=1e-12,rtol=0)];assert len(m)==1;return m[0]
vertices=[('D',exact_snap(edge15[0]),RED),('E',exact_snap(edge15[1]),GREEN),('B',exact_snap(edge17[1]),BLUE)]
a=[];roles=[]
for name,receiver,col in vertices:
 a.extend([{'type':'add_point','id':'source_'+name,'xy':sn[name],'color':col},{'type':'add_point','id':'receiver_'+name,'xy':receiver['xy'],'color':col}]);roles.extend([f'Actual named adjacent vertex {name}, one of DBE. Source for the corresponding corner-triangle vertex in C.',f'Existing C corner triangle vertex {receiver["id"]}, falsely aligned to {name}. All three point pairs are needed to encode ordered DBE rather than just option salience.'])
proof=json.loads((TASK/q/'primary_math_proof.json').read_text(encoding='utf-8'))['proof']
save_candidate(q,'full_cut_vertices_to_shallow_corner','C',a,roles,'Ordered red D, green E, blue B source vertices bind to three actual vertices of the shallow triangular corner in C; invites truncation-depth confusion without adding source cut contours.',proof,TASK/q/'primary_math_proof.json')
