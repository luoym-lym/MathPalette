from tools09 import *
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
def render(qid,vid):
    ck=eligibility(qid);assert ck['eligible'],ck
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid)
    sc=ad.scene(qid)
    try:
        sc.fig.canvas.draw();paths={o['id']:object_paths(sc,o['id']) for o in meta['objects']}
    finally:sc.close()
    actions=[];roles=[]
    def whole(oid,color,role):
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2});roles.append({'action_index':len(actions)-1,'target':oid,'role':role})
    def part(oid,start,end,color,role):
        p=paths[oid][0]
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start/len(p['segments']),'end':end/len(p['segments']),'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':oid,'segment_start':start,'segment_end':end,'role':role})
    if (qid,vid)==('Plane252','incompatible_local_overlap_sum'):
        for k in [0,1,2,3]:whole('wire0_'+str(k),RED,'First wire lower four-unit U, one side of the concrete local U correspondence.')
        for k in [4,5,6,7]:whole('wire1_'+str(k),RED,'Second wire lower four-unit U, congruent with the red first-wire U under translation, considered alone.')
        for k in [6,7]:whole('wire0_'+str(k),BLUE,'First wire upper two-unit horizontal run, the second local overlap feature.')
        for k in [2,3]:whole('wire1_'+str(k),BLUE,'Second wire middle two-unit horizontal run. Matching the blue pair requires a different translation from the red pair.')
        wrong='6'
        mechanism='Red binds the actual four-unit U features and blue binds the actual two-unit horizontal runs. Intended mistake: sum the four red units and two blue units to get six coinciding units, overlooking that these local correspondences require incompatible rigid placements. Each color is a proposed local match, not an asserted positional constraint.'
        math='The exact unit-edge enumeration in primary_math_audit.json includes all D4 orientations and translations and establishes maximum5 with explicit witnesses; see its argument for completeness over continuous rigid motions. Both wires remain exactly8 unit segments and no point or edge is added.'
    elif (qid,vid)==('Plane252','single_U_contiguous_overlap'):
        for k in [0,1,2,3]:whole('wire0_'+str(k),RED,'First wire lower four-unit U, one side of a genuine contiguous overlap correspondence.')
        for k in [4,5,6,7]:whole('wire1_'+str(k),RED,'Second wire lower four-unit U, exactly congruent under a single translation; each red unit supplies one unit of this real overlap witness.')
        wrong='4'
        mechanism='Show only a genuine four-unit contiguous U-to-U correspondence, leaving both other arms black. Targets reporting the longest immediately visible single connected coincidence as the maximum total common length, overlooking an optimal placement with5 total units. This is a different hypothesis from adding incompatible red and blue correspondences; no second blue pairing is present.'
        math='The saved exact exhaustive wire audit confirms maximum5 over all rigid placements, with explicit witnesses. The red U has4 common units under a legal translation, so it is only a lower-bound witness and does not limit the total maximum. Eight original unit segments and all joints of each wire remain unchanged.'
    elif (qid,vid)==('Plane391','right_angle_size_alias'):
        part('piece2',0,2,RED,'Two adjacent sides of the source unit square establish the source right-angle size template.')
        part('piece5',0,2,RED,'Two adjacent sides of the first assembled unit square; a valid size correspondence with the source square.')
        part('piece9',0,2,RED,'Two adjacent sides of the second assembled unit square; another valid source-square correspondence.')
        part('piece7',0,2,RED,'Two perpendicular legs of the large assembled triangle; shares a right-angle feature but has twice the source-square side length. This is the deliberate incomplete size correspondence.')
        part('piece1',2,3,BLUE,'Source small right triangle hypotenuse establishes the half-unit area family.')
        for oid,seg in [('piece4',0),('piece6',1),('piece8',1),('piece10',1)]:part(oid,seg,seg+1,BLUE,'Hypotenuse of one of the four assembled small triangles; a true source-to-assembly half-unit correspondence.')
        wrong='5'
        mechanism='Bind the source unit square to two true assembled squares and the large assembled right triangle by red right-angle legs, while blue correctly groups the four small triangles with a source small triangle. Targets assigning unit area to all three red pieces, giving3+4/2=5, and ignoring the factor2 in the large triangle legs.'
        math='Shoelace audit gives source areas2,0.5,1,0.5 totaling4; assembled areas0.5,1,0.5,2,0.5,1,0.5 totaling6. All region contours remain visible; the red large-triangle legs are visibly twice the unit-square side, and its hypotenuse remains black. Therefore6 is unique.'
    elif (qid,vid)==('Plane391','whole_square_frame_to_triangle'):
        part('piece0',0,2,RED,'The full left and top exterior sides of the source4cm2 square; an open outer-size frame also shared by its large triangular piece.')
        part('piece7',0,2,RED,'The two same-length perpendicular legs of the assembled large triangle; falsely transferring whole-square area4 to the half-square triangle through its matching outer-size frame.')
        part('piece2',0,2,BLUE,'Two sides of the source1cm2 square establish the independent small-square size family.')
        part('piece5',0,2,BLUE,'Two sides of one genuine assembled1cm2 square, matched to the source small square.')
        part('piece9',0,2,BLUE,'Two sides of the other genuine assembled1cm2 square, matched to the source small square.')
        wrong='8'
        mechanism='Red matches the full-size source square outer L frame to the congruent two-leg frame of the assembled large triangle; blue correctly matches the source small square to both assembled small squares. Targets transferring the whole original square area4 through the red frame to the triangular piece instead of halving, giving4+2+4/2=8. Diagonal closure and all four small triangles remain visible.'
        math='The exact shoelace audit proves the source large triangle area2, not the whole source-square area4. Assembly has that2cm2 triangle, two1cm2 squares and four0.5cm2 small triangles, total6. Red frame lengths do match geometrically but do not imply equal areas for different enclosed shapes; no equality symbol, boundary or label is added.'
    elif (qid,vid)==('Plane348','fold_to_middle_cut_alias'):
        whole('o1',RED,'Original first vertical fold, source member of the false vertical fold-to-cut correspondence; dotted style remains.')
        whole('o109',RED,'Final folded-paper vertical middle cut, falsely paired with the first fold by orientation.')
        whole('o53',BLUE,'Second horizontal fold in the intermediate rectangle, source member of the horizontal fold-to-cut correspondence.')
        whole('o110',BLUE,'Final folded-paper horizontal middle cut, falsely paired with the second fold by orientation.')
        wrong='9'
        mechanism='Pair the two source fold axes with the final middle cuts by orientation. Targets treating fold and cut grids as equally spaced on the unfolded paper and counting every one of nine pieces as square; the actual unequal1:2:1 spacing and all four source/final lines remain recoverable from the unchanged folding diagram.'
        math='The midpoint cuts of the twice-folded quarter square unfold to x,y=1/4,3/4. Resulting width intervals are1/4,1/2,1/4. Only four corner pieces and the central piece are squares; the other four are1/4 by1/2 rectangles. Answer5 is unique. Original folds retain dotted style and scissor cuts retain their source dash style; colors introduce neither folds nor cuts.'
    elif (qid,vid)==('Plane415','arc_inventory_perimeter_alias'):
        for oid in ['leftbigupper','leftbiglower','rightbigright','rightbigleft']:
            part(oid,1,181,RED,'One external large quarter-circle arc; red pairs the two equal-radius arc inventories across the two rearrangements. Only curved portions are marked.')
        for oid in ['leftsmallleft','leftsmallright','rightsmallleft','rightsmallright']:
            part(oid,1,181,BLUE,'One external small quarter-circle arc; blue pairs the smaller-radius arc inventories across the rearrangements. Original straight exposed radii stay black.')
        wrong='0'
        mechanism='Match the complete external curved-boundary inventory of the two arrangements: two large quarter arcs in red and two small quarter arcs in blue in each. Targets cancelling those equal visible arc sums and concluding equal perimeters, overlooking the different exposed straight-radius portions. Every mark serves an explicit cross-diagram radius-family correspondence.'
        math='Each arrangement has curved boundary pi*(10+5)=15pi cm. The left has exposed straight radii10+10+5+5=30 cm; all four sides of its5x10 rectangle are internal. The right has only the10cm bottom rectangle side exposed; the remaining radial sides are seams between pieces. Perimeters are15pi+30 and15pi+10, with unique difference20. The unchanged black straight boundary remains readable.'
    elif (qid,vid)==('Plane276','exposed_cut_edge_migration'):
        whole('o1',RED,'The actual12cm source cut, newly exposing two congruent cut edges while retaining its dashed source style.')
        # Rectangle ordered bottom,right,top,left. Half-segment parameters preserve exact path order.
        part('o4',2.5,3,RED,'Top-left12cm half of the assembled rectangle, one actual exposed copy of the original cut edge.')
        part('o4',0.5,1,RED,'Bottom-right12cm half of the assembled rectangle, the other exposed copy of the source cut edge.')
        wrong='E'
        mechanism='Bind the original cut to its two genuine exposed copies on the rearranged rectangle using red. Targets adding twice the12cm cut length to the original48cm perimeter, giving72cm(E), without subtracting the12cm of former exterior edges hidden by the new seam. All marked edges are actual part migrations, no false length or cut is introduced.'
        math='Square side12cm; each half12x6cm; rectangle24x6cm has perimeter60cm(D). The cut adds24cm to the separate halves, while joining along a6cm seam removes12cm, so48+24-12=60. Red top-left and bottom-right12cm boundary segments are a consistent placement of the two former cut sides. The6cm seam stays black dashed.'
    elif (qid,vid)==('Plane213','open_notch_local_global_binding'):
        def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
        selected={edge((12,11),(12,10)),edge((12,10),(13,10)),edge((13,10),(13,11))}
        selectedB={edge((7,2),(7,1)),edge((7,1),(8,1)),edge((8,1),(8,2))}
        for prefix,es,role in [('given_',selected,'One existing source-grid edge in the open three-edge notch of a locally placeable U pentomino. This marks one possible local feature, no complete piece contour or fixed global partition.'),('B_',selectedB,'One actual inward-notch edge of optionB; the three-edge red chain is congruent to the source red chain, supplying a specific local-to-option correspondence.')]:
            found=set()
            for o in meta['objects']:
                if o['id'].startswith(prefix) and o['kind']=='segment' and edge(*o['geometry']['points']) in es:
                    whole(o['id'],RED,role);found.add(edge(*o['geometry']['points']))
            assert found==es
        wrong='B'
        mechanism='Match only the three-edge open inward notch of an actual locally placeable U pentomino in the source grid to the congruent notch in optionB. Targets inferring that one local placement supplies a full three-copy partition. The source is prospective(to be split); no complete colored piece boundary or incompatible fixed partition is drawn.'
        math='The15-cell source is4x4 minus its lower-right corner. Each option has5 cells. Exact cover under all8 square-lattice isometries finds A tilings and zero B,C,D,E tilings; saved primary_math_audit.json includes shapes, counts and A witnesses. Thus A stays unique. The red chain is only an existing internal-grid local feature; no missing source cell, mandatory cut or new puzzle piece is asserted.'
    elif (qid,vid)==('Plane301','terminal_feature_transfer'):
        whole('wire1_0',RED,'One-unit terminal edge at the first end of the actually joinable wireB; source for the terminal-feature correspondence.')
        whole('wire2_0',RED,'One-unit terminal edge at the first end of wireC; paired to B by equal local vertical edge geometry.')
        whole('wire1_7',BLUE,'One-unit edge at the other end of wireB; completes its two-end local feature description.')
        whole('wire2_11',BLUE,'One-unit edge at the other end of wireC; paired to B despite a different global winding and relative endpoint direction.')
        wrong='C'
        mechanism='Transfer the two local terminal-edge features of the genuinely joinable wireB to C with red first-end and blue second-end pairs. Targets accepting C by matching terminal edge lengths/directions without checking the whole rigid copy for interior crossings. Both wires and their complete global winding remain visible; no synthetic second wire is added.'
        math='The saved exact rational audit enumerates all4 endpoint-set-preserving plane isometries for an identical second copy. B alone admits a simple closed join. A,C,D,E each have an interior contact or a positive-length overlap for every possible endpoint identification. This remains true even if turning the wire over is allowed; colors do not affect any endpoint or crossing.'
    elif (qid,vid)==('Plane398','wrong_corner_L_transfer'):
        for k in range(4):
            part('cellpiece20'+str(k),2,3,RED,'One top boundary unit of the given L-piece; red defines its four-unit horizontal arm.')
            part('cellC0'+str(k),2,3,RED,'One top boundary unit of C; proposed counterpart of the source L horizontal arm in an unsuitable top-right placement.')
        for k in range(4):
            oid='cellpiece2'+str(k)+'0'
            part(oid,3,4,BLUE,'One left boundary unit of the given L-piece; blue defines its perpendicular four-unit arm.')
            part('cellC'+str(k)+'3',1,2,BLUE,'One right boundary unit of C; proposed reflected counterpart of the source vertical arm. This corner placement fails the actual black-white pattern, although a different orientation succeeds.')
        wrong='C'
        mechanism='Map the source seven-cell L-piece horizontal and vertical arms onto the top and right borders of C using red and blue. This explicitly selects one locally tempting but pattern-incompatible placement and targets treating that failed placement as proof C cannot be formed, overlooking its valid alternative orientation. Original black-white semantic fills are preserved.'
        math='Exact placement enumeration of both frozen colored cell sets under all8 grid isometries and translations gives solutions for A,B,C,D and none for E. Saved primary_math_audit.json provides every solution count and witnesses. The coloring only changes outer cell-border portions; black/white pattern and every cell boundary remain unchanged. Thus E stays unique.'
    else:raise ValueError((qid,vid))
    out=HERE/qid/vid;out.mkdir(parents=True,exist_ok=False)
    mechanism=mechanism[:1000]
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'','params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:meta});p,png,pix=pr.render(plugin);p2,png2,pix2=pr.render(p,frozen=True)
    assert p==p2 and png==png2 and pix==pix2 and before==inputs(ad,qid)
    used=sorted({a['target'] for a in actions})
    pathdata={o:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[o]] for o in used}
    write(out/'eligibility_before_design.json',ck);write(out/'context.json',meta);write(out/'path_fingerprints.json',pathdata)
    write(out/'plugin.json',p);(out/'candidate.png').write_bytes(png)
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':wrong,'correct_answer':ad.records[qid]['answer'],'mechanism':mechanism,'primary_math_proof':math,'marker_roles':roles,'human_semantics':'Only original open line portions or existing fold/cut lines are recolored. No closed new source partition, no added piece/label/line, original semantic fill and text preserved. Colors do not assert new equalities. Actual PNG still requires manual viewing before calls.','status':'PRIMARY_ONLY_PARENT_NEW_INDEPENDENT_REVIEW_REQUIRED'})
    write(out/'render_check.json',{'baseline_pixel_match':True,'baseline_pixel_sha256':meta['original_pixel_sha256'],'schema_default_normalized':True,'twice_byte_identical':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'own_directory_guard':True})
    print(json.dumps({'qid':qid,'variant':vid,'actions':len(actions),'expected_wrong_answer':wrong,'rendered':True}),flush=True)
if __name__=='__main__':render(*sys.argv[1:3])
