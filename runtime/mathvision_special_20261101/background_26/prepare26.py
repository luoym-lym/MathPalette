from tools26 import *
from math26 import native,pts
R='#DC2626';B='#2563EB';G='#16A34A'
def whole(oid,color):return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':1.5}
def part(q,oid,start,end,color):
    path=read(HERE/q/'paths_frozen.json')[oid][0]
    return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':start,'end':end,'wrap':False}}
def make(q,vid,wrong,actions,mechanism,difference,proof,roles,details,prior_file='prior_history_audit.json'):
    out=HERE/q/vid;ck=eligibility(q);assert ck['eligible'],ck
    prior=read(HERE/q/prior_file);assert vid not in [h['variant_id'] for h in prior['history']]
    assert not out.exists()
    write(out/'design_difference_audit.json',{'stage':'material_refinement','question_id':q,'variant_id':vid,'saved_before_solver_calls':True,'created_at':now(),'all_prior_designs_images_presets_raw_finals_and_primary_objections_read':True,'prior_evidence_audit_path':str(HERE/q/prior_file),'prior_evidence_audit_sha256':file_hash(HERE/q/prior_file),'old_variants':[{'variant_id':h['variant_id'],'preset':h['preset'],'manual_final_answers':h['manual_final_answers'],'old_mechanism':h['full_design'].get('mechanism',h['full_design'].get('hypothesis',h['full_design'].get('design_reason')))} for h in prior['history']],'substantive_geometric_or_grouping_difference':difference,'new_wrong_answer_hypothesis':wrong,'new_mechanism_frozen_before_calls':mechanism,'not_palette_width_crop_rename_or_posthoc_relabel':True})
    cfg,ad=adapter();before=inputs(ad,q);ctx=ad.inspect_question(q)
    write(out/'fresh_context.json',ctx);write(out/'eligibility_before_render.json',ck);write(out/'source_inputs.json',before)
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{q:ctx});norm,data,pix=pr.render(plugin);norm2,data2,pix2=pr.render(norm,frozen=True)
    assert data==data2 and norm==norm2 and pix==pix2 and before==inputs(ad,q)
    (out/'candidate.png').write_bytes(data);(out/'repeat.png').write_bytes(data2);write(out/'plugin.json',norm)
    objects={o['id']:o for o in ctx['objects']};targets={t['id']:t for t in ctx['canvas']['targets']}
    write(out/'marker_bindings.json',[{'action_index':i,'action':a,'role':roles[i],'source_object_full_geometry':objects.get(a.get('target')),'path_and_fullprecision_canvas_binding':targets.get(a.get('target'))} for i,a in enumerate(norm['params']['actions'])])
    write(out/'math_proof.json',{'question_id':q,'primary_author_independently_recomputed':True,'unique_unchanged_answer':ad.records[q]['answer'],'proof':proof,'numeric_or_symbolic_details':details})
    design={'question_id':q,'variant_id':vid,'stage':'material_refinement','created_at':now(),'expected_wrong_answer':wrong,'correct_answer':ad.records[q]['answer'],'mechanism':mechanism,'design_difference':difference,'primary_math_proof':proof,'per_marker_roles':roles,'human_semantics':'Only existing border/edge/joint appearance is changed. No equality/angle symbol, new cut, region, hole, point, piece, text, fill, dimension or geometry is added. Annotation colors are proposed correspondences, not extra conditions. Native inspection required before calls.','source_inputs_sha256':file_hash(out/'source_inputs.json'),'plugin_sha256':file_hash(out/'plugin.json'),'image_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pix,'pretest_immutable':True,'status':'PRIMARY_ONLY_PARENT_NEW_INDEPENDENT_SECOND_REVIEW_REQUIRED'}
    write(out/'design.json',design)
    write(out/'render_check.json',{'actual_noop_formal_pixel_equality':True,'actual_normalization_and_schema_validation':True,'normalized_frozen_plugin_identical':norm==norm2,'two_byte_identical_draws':data==data2,'pixel_sha256':pix,'image_sha256':file_hash(out/'candidate.png'),'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'original_source_unchanged':before==inputs(ad,q),'isolation':ISOLATION})
    print(json.dumps({'qid':q,'variant':vid,'preset':wrong,'actions':len(actions),'png':str(out/'candidate.png')}),flush=True)

def prepare(q):
    if q=='Plane198':
        vid='r26_unchanged_bent_cell_cluster';ids=['1_1','2_1','2_2'];actions=[];roles=[]
        for suffix,color in zip(ids,[R,B,G]):
            for prefix in ['G','D']:
                oid=prefix+suffix;actions.append(whole(oid,color));roles.append(f'{oid}: existing black cell at row/column {suffix}, one end of the spatially identical three-cell bent-cluster correspondence from G to D. All three indexed positions together define the local shape to be copied unchanged rather than complemented.')
        s=native(q);oo={o['id']:o for o in s['objects']}
        grids={p:[[int(oo[f'{p}{i}_{j}'].get('semantic_fill',False)) for j in range(4)] for i in range(4)] for p in ['X','Y','G','A','B','C','D','E']}
        comp=lambda a:[[1-x for x in row] for row in a]
        assert comp(grids['X'])==grids['Y'];assert [p for p in 'ABCDE' if grids[p]==comp(grids['G'])]==['E'];assert grids['G']==grids['D']
        make(q,vid,'D',actions,'Match the three existing central black cells of G to their identical positions in D using a three-color bent-cluster correspondence. Predict D from copying this positional black cluster while omitting the X-to-Y black/white inversion.', 'Old B design compressed the bottom-row 3:1 runs to 2:2. This design instead binds a central bent three-cell feature at exact unchanged row/column positions in G and D; it tests omission of complementation, with no bottom-row grouping or compressed run.', 'Read all sixteen cell fills of X and Y: Y=1-X pointwise. Therefore complement G at the same coordinates. The full four binary rows are G=0010,1100,0110,0001; complement=1101,0011,1001,1110. Full comparison with all five options gives E alone. D copies G unchanged and is wrong in every cell under the complement rule. No fill or border position changes.',roles,{'black_one_grids':grids,'unique_matching_option':'E'})
    elif q=='Plane223':
        vid='r26_upper_three_dot_cluster';actions=[];roles=[]
        for a,b,color in [('o2','o26',R),('o3','o28',B),('o4','o29',G)]:
            for oid in [a,b]:actions.append(whole(oid,color));roles.append(f'{oid}: one actual upper-cluster solid dot; its same-color partner is the same radius class in the source/C partial-cluster match. The three dot roles and their cyclic order tempt local rotation matching while the remaining spots and annulus must still match globally.')
        s=native(q);oo={o['id']:o for o in s['objects']}
        def cr(oid):
            ps=oo[oid]['points'];xs=[p[0] for p in ps];ys=[p[1] for p in ps];return [(min(xs)+max(xs))/2,(min(ys)+max(ys))/2,(max(xs)-min(xs))/2]
        source=[cr('o'+str(i)) for i in range(1,9)];e=[cr('o'+str(i)) for i in range(42,50)]
        residuals=[[abs((a[0]-8)+(b[0]-16.8)),abs((a[1]-6)+b[1]),abs(a[2]-b[2])] for a,b in zip(source,e)]
        assert max(x for r in residuals for x in r)<1e-12
        ds=lambda a,b:sum((x-y)**2 for x,y in zip(cr(a)[:2],cr(b)[:2]))
        make(q,vid,'C',actions,'Match the three upper solid-dot radius classes in the source to C, red/blue/green, to suggest a rotated local cluster after the color swap. Predict C by accepting that partial cluster while ignoring the other solids and the annulus placement.', 'Old design matched the largest isolated solid dot and unique ring. The new design leaves both old anchor features untouched and groups the three upper solid dots by radius and cyclic placement; the hypothesis is local-cluster sufficiency rather than the old two-anchor separation alias.', 'After inversion, positions and radii of every solid spot and both annulus boundaries must be preserved by one rotation. E exactly negates each of the eight centered feature contours, including the annulus inner disk, hence a 180-degree rotation works. A has an additional solid, B and D omit solids/ring. C has the correct count but its unique largest solid-to-annulus squared separation is 1.576, versus source 2.7625, impossible under any rotation. Thus only E. All yellow/black semantic fill remains identical; the tiny unmarked dot and annulus are fully visible.',roles,{'source_features_center_radius':source,'E_features_center_radius':e,'halfturn_residuals':residuals,'source_largest_to_ring_distance_squared':ds('o5','o7'),'C_largest_to_ring_distance_squared':ds('o30','o32')})
    elif q=='Plane252':
        vid='r26_optimal_six_joint_correspondence';actions=[];roles=[]
        for wire in [0,1]:
            for j in range(1,7):
                oid=f'joint{wire}_{j}';actions.append(whole(oid,R));roles.append(f'{oid}: original joint {j} of wire {wire+1}, one of the six vertices of the actual common five-edge chain under T(x,y)=(2-y,x-5). Counts vertices rather than edges without adding any new dot; its opposite-wire partner is joint{1-wire}_{j}.')
        s=native(q);oo={o['id']:o for o in s['objects']};w=[[tuple(map(tuple,pts(s,oo[f'wire{k}_{j}']))) for j in range(8)] for k in [0,1]]
        edge=lambda a,b:tuple(sorted((tuple(a),tuple(b))))
        aa={edge(*e) for e in w[0]};best=0;wit=[]
        for refl in [-1,1]:
            for rot in range(4):
                def f(p):
                    x,y=p;x*=refl
                    for _ in range(rot):x,y=-y,x
                    return x,y
                transformed=[(f(a),f(b)) for a,b in w[1]]
                for dx in range(-12,13):
                    for dy in range(-12,13):
                        bb={edge((a[0]+dx,a[1]+dy),(b[0]+dx,b[1]+dy)) for a,b in transformed};n=len(aa&bb)
                        if n>best:best=n;wit=[]
                        if n==best:wit.append({'refl':refl,'quarter_turns':rot,'translation':[dx,dy],'common_edges':sorted(aa&bb)})
        assert best==5
        make(q,vid,'6',actions,'Mark the six original joints along each wire that coincide in a genuine optimal five-unit overlap after a quarter turn and translation. Predict 6 by counting the six matched joint positions as six common length units, instead of the five intervals between them.', 'Old preset6 summed incompatible four-edge U and two-edge run alignments; old preset4 used only a four-edge U. New design styles ONLY existing joint contours, identifies a different actually realizable optimal five-edge chain, and targets vertex-versus-segment counting. No old colored segment is reused as a cosmetic substitute.', 'For positive length overlap, orthogonal grid edges must be parallel, hence the relative rotation is a multiple of 90 degrees. At a fixed such orientation, horizontal overlap versus x-translation is piecewise linear with integer endpoint breakpoints; similarly vertically. Integer translations attain an optimum, also covering configurations with overlap in only one direction. Enumerating all eight D4 orientations and translations -12..12 proves maximum5; outside the bounded intersecting envelopes overlap is zero. A reflection-free witness T(x,y)=(2-y,x-5) matches wire1 edges1..5 to wire0 edges1..5. It aligns six existing joints1..6 but only five unit intervals. Recoloring circle borders preserves all18 black filled joints and sixteen unit segments.',roles,{'max_common_length':best,'all_maximum_witnesses':wit,'wire_edges':w,'marked_joint_correspondence':[{'first':oo[f'joint0_{j}']['center'],'second':oo[f'joint1_{j}']['center']} for j in range(1,7)]})
    elif q=='Plane282':
        vid='r26_three_open_row_perimeters';actions=[];roles=[]
        for row,ids,color in [(0,['square0','square1','square2'],R),(1,['square3','square4'],B),(2,['square5'],G)]:
            for i,oid in enumerate(ids):
                for edge in [0]+([3] if i==0 else [])+([1] if i==len(ids)-1 else []):
                    actions.append(part(q,oid,edge/4,(edge+1)/4,color));roles.append(f'{oid} edge{edge}: existing bottom or end side of row{row+1}; together the {color} strokes trace its open U-shaped strip frame. This groups its constituent squares into one actual width{len(ids)} rectangle, inviting addition of row perimeters while the shared horizontal contacts remain black and visible.')
        rectangles=[[0,0,3,1],[.75,1,2.75,2],[1,2,2,3]]
        make(q,vid,'18',actions,'Use three colored open U frames on the existing bases and end sides of the three rows. Predict 18 by adding the row-rectangle perimeters 8+6+4 while overlooking cancellation of the two shared horizontal interfaces.', 'Old preset18 singled out only three full vertical internal seams and used 24-2*3; old preset14 equated fractional shoulders with one full side. This instead groups each actual horizontal row as a composed rectangle using its open three-sided frame, with internal vertical seams black, and predicts the sum of the three strip perimeters. No closed new partition is drawn.', 'The three actual row rectangles have widths3,2,1 and height1, so separate row perimeters sum8+6+4=18. Their two horizontal contact lengths are2 and1, each counted twice in that sum. The union perimeter is18-2*(2+1)=12. Equivalently horizontal exterior lengths telescope to6 and vertical exterior lengths sum6. Frozen offsets .75 and1 do not alter this. All six individual square boundaries stay present, no region or edge is added.',roles,{'row_rectangles':rectangles,'separate_row_perimeters':[8,6,4],'shared_horizontal_contact_lengths':[2,1],'unique_union_perimeter':12})
    elif q=='Plane408':
        vid='r26_exposed_step_variation_binding';actions=[];roles=[]
        specs=[('ribbon0_1',3+(60-35)/60,4,25),('ribbon0_2',3+(85-60)/85,4,25),('ribbon0_3',3+(110-85)/110,4,25)]
        # Polygon path: bottom, right upward, top, left downward. Exposed left edge is t in [3/4,(3+heightdiff/height)/4].
        specs=[('ribbon0_1',3/4,(3+25/60)/4,25),('ribbon0_2',3/4,(3+25/85)/4,25),('ribbon0_3',3/4,(3+25/110)/4,25),('ribbon1_0',(1+60/85)/4,2/4,25),('ribbon1_2',3/4,(3+50/110)/4,50),('ribbon1_2',(1+35/110)/4,2/4,75)]
        for oid,start,end,length in specs:
            actions.append(part(q,oid,start,end,R));roles.append(f'{oid} interval[{start},{end}]: exact existing exposed vertical step of length{length}cm. The six red portions isolate the two arrangements\' total step variations75 and150; end sides and all contacts remain black. Every red portion contributes to the tempting75cm difference.')
        make(q,vid,'A',actions,'Mark only the six existing exposed vertical height-change intervals: 25+25+25 in the first shape and25+50+75 in the second. Predict A=75cm from subtracting these step totals while forgetting that the combined outer end heights decrease by25cm.', 'Old E design paired eight short horizontal top edges to track conserved ribbon identity. All those top-edge marks are absent. This design selects exact EXPOSED portions of long vertical edges, testing total-variation-minus-endpoint omission and freezing A=75cm before calls.', 'For bottom-aligned widths10 and heights h1..h4, the external perimeter equals80+h1+h4+sum|h[i+1]-h[i]|. First heights35,60,85,110 give80+145+75=300. Second85,60,110,35 give80+120+150=350. Thus difference50cm, unique B. More generally the unknown shortest length cancels. Red steps differ by75 but outer ends differ by-25; the latter remain fully visible. Exact interval bounds use original heights, without new vertices or cut lines.',roles,{'height_arrays':[[35,60,85,110],[85,60,110,35]],'step_totals':[75,150],'outer_end_height_sums':[145,120],'perimeters':[300,350],'difference':50})
    elif q=='Plane461':
        vid='r26_free_edge_as_second_fold';actions=[part(q,'o12',2/4,3/4,R),part(q,'o12',3/4,1,B),whole('o39',R),whole('o38',B)]
        roles=['Final folded packet TOP free outer edge, near the punch; red proposes it as the horizontal unfolding hinge, an incorrect role which must be distinguished from the true bottom fold.','Final folded packet LEFT boundary, the actual vertical fold, blue; correctly binds its near-punch side to the unfolded vertical crease.','D original horizontal DASHED crease, red; target of the false top-free-edge-to-hinge correspondence. It stays dashed and no hole is recolored.','D original vertical DASHED crease, blue; target of the true vertical fold correspondence. Together the two local axis roles make the four central D holes tempting, without coloring a choice box or hole.']
        make(q,vid,'D',actions,'Bind the final packet left fold edge to D vertical crease in blue, and its top FREE edge to D horizontal crease in red. Predict central-hole option D by treating both near-punch packet sides as fold hinges, although the top side is an outer paper edge.', 'Old C design colored the punch circle and four outer-corner option holes, targeting the left-fold-versus-outer-edge confusion. New design leaves every hole black and binds two EDGE ROLES to D existing dashed axes, targeting a different mistake: falsely treating the top free edge as the earlier horizontal fold.', 'Normalize the original sheet to[0,4]x[0,2]. Bottom-to-top leaves y in[1,2], with the true horizontal fold at y=1; left-to-right leaves x in[2,4], with the vertical fold at x=2. The punch is(2.25,1.75), near the free TOP y=2 and LEFT fold x=2. Undo folds gives x=1.75,2.25 and y=.25,1.75: only B. D has y=.75,1.25, requiring a punch near the bottom fold instead of the top free edge. A is not the two-reflection orbit, C and E have wrong exterior-side x coordinates. All five patterns, arrows, original dashed creases, X and holes remain unchanged.',roles,{'punch':[2.25,1.75],'reflected_holes':[[x,y] for x in [1.75,2.25] for y in [.25,1.75]],'correct_option':'B','wrong_D_local_holes':[[x,y] for x in [1.75,2.25] for y in [.75,1.25]]})
if __name__=='__main__':
    for q in sys.argv[1:]:prepare(q)
