from tools_local import *
from math_audits import grid_cells,edge
RED='#DC2626';BLUE='#2563EB'
def style(target,color,interval=None):
    a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':2}
    if interval:a['interval']=interval
    return a
def render(qid,vid):
    check=eligibility(qid);assert check['eligible'],check
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid);objects={o['id']:o for o in meta['objects']};scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in meta['objects']}
    finally:scene.close()
    actions=[];roles=[];overlay_bindings=[]
    def whole(oid,color,role):actions.append(style(oid,color));roles.append({'action_index':len(actions)-1,'target':oid,'role':role})
    def part(oid,start,end,color,role):
        p=paths[oid][0];interval={'path_id':p['id'],'path_sha256':p['sha256'],'start':start/len(p['segments']),'end':end/len(p['segments']),'wrap':False}
        actions.append(style(oid,color,interval));roles.append({'action_index':len(actions)-1,'target':oid,'segment_start':start,'segment_end':end,'role':role})
    def overlay_polygon(oid,color,role):
        pts=objects[oid]['geometry']['points']
        for i in range(len(pts)):
            aid='Binding_'+str(len(actions));xy=[pts[i],pts[(i+1)%len(pts)]]
            actions.append({'type':'add_line','id':aid,'endpoints':xy,'color':color,'linestyle':'solid','linewidth_pt':1})
            roles.append({'action_index':len(actions)-1,'id':aid,'source_object':oid,'edge_index':i,'role':role+' This action traces original contour edge '+str(i)+'.'})
            overlay_bindings.append({'action_id':aid,'object_id':oid,'edge_index':i,'exact_context_endpoints':xy})
    if (qid,vid)==('Plane220','arc_star_copy_binding'):
        part('o0',54,60,RED,'Source zigzag cut boundary; anchor the original star-tip feature.')
        part('o0',4,53,BLUE,'Source lower circular cut arc; first half of the curved feature.')
        part('o0',61,110,BLUE,'Source upper circular cut arc; second half of the same curved feature.')
        part('o11',50,56,RED,'Option C single right-hand zigzag feature proposed as a direct copy of the source star-tip.')
        part('o11',0,49,BLUE,'Option C oval feature proposed as completion of the source circular cut arc; this ignores that reflection also duplicates the star to the other side.')
        expected='C';mechanism='Bind the actual source star-tip and circular cut-arc features to the single star-tip and oval features of C using red and blue. Targets copying the cut profile into an oval-with-one-tail rather than reflecting the whole cut boundary through the fold. The original contour and dotted candidate fold remain visible; C is not highlighted in isolation.'
        math='Unfolding across the left folded edge reflects the entire cut boundary. The source opening meets that fold at both ends of the circular arc, so its reflected cut is one connected opening, with one continuous central rounded region and matching star-like tips on both sides. D alone has this connected, bilaterally symmetric topology. A and B are two separate circle/tip openings; E has two separate smaller double-tip openings; C has a single right-hand tip and cannot be invariant under reflection about its shown vertical fold. Therefore D remains unique. The red and blue outlines confer no equality or new cut edge, and neither the existing fold nor original boundary is moved.'
        human='All marks are 2pt partial boundary color overrides. No new line, hole, label, fold or region is introduced. The complete original paper boundary, all five option contours and dotted folds remain distinguishable.'
    elif (qid,vid)==('Plane231','swapped_triangle_correspondence'):
        overlay_polygon('-1_blue',RED,'Source equilateral triangle is the first input feature in the proposed correspondence.')
        overlay_polygon('1_yellow',RED,'B scalene triangle is falsely paired with the source equilateral triangle.')
        overlay_polygon('-1_yellow',BLUE,'Source scalene triangle is the second input feature in the proposed correspondence.')
        overlay_polygon('1_blue',BLUE,'B equilateral triangle is falsely paired with the source scalene triangle; the two swaps invite rejecting B from colored-part identity.')
        expected='B';mechanism='Swap the input-to-B identities of the equilateral and scalene triangles using two contour-color pairs. The source equilateral is paired with B scalene and source scalene with B equilateral. Targets treating these proposed part correspondences as fixed identities and rejecting a legal rotation of B; all original triangle shapes and the unmistakable square in C remain visible.'
        math='The input multiset contains two congruent disks, one thin rectangle, one small right triangle, one scalene triangle and one equilateral triangle. A, B, D and E each contain exactly that multiset under planar rigid motions (their original piece contours remain independently visible even when touching/overlapping in the drawing). C instead has a four-sided square where the small right triangle is required, while keeping the other five pieces. It cannot be formed from all six input pieces without cutting/replacing a piece. Thus C is the only impossible figure. The overlays trace existing edges exactly; they neither add a piece nor remove any original contour or fill.'
        human='Twelve legal 1pt solid auxiliary overlays lie exactly on the four selected triangle contours, with exact context vertices. No new puzzle boundary is introduced. Source triangles, B triangles, C square, bar, all disks and option letters remain readable. The colored triangle pairs deliberately differ in side structure, which remains a visible way to reject the false correspondence.'
    elif (qid,vid)==('Plane233','local_cross_global_tiling'):
        source={(12,8),(11,9),(12,9),(13,9),(12,10)};target=grid_cells(meta,'E_')
        def boundary(cells):
            counts={}
            for x,y in cells:
                for e in [edge((x,y),(x+1,y)),edge((x+1,y),(x+1,y+1)),edge((x+1,y+1),(x,y+1)),edge((x,y+1),(x,y))]:counts[e]=counts.get(e,0)+1
            return {e for e,n in counts.items() if n==1}
        for prefix,cells,role in [('given_',source,'Actual five-cell cross subset of the source board; red contour presents a locally valid placement.'),('E_',target,'The congruent five-cell cross in E; red contour supplies its concrete source-to-option part counterpart.')]:
            boundary_edges=boundary(cells)
            matched=set()
            for o in meta['objects']:
                if o['id'].startswith(prefix) and o['kind']=='segment' and edge(*o['geometry']['points']) in boundary_edges:
                    whole(o['id'],RED,role+' This action marks one necessary external unit edge.');matched.add(edge(*o['geometry']['points']))
            assert matched==boundary_edges
        expected='E';mechanism='Match the full boundary of one actual X-shaped five-cell subset in the source board with the congruent X-shaped pentomino E. Targets the local-to-global error that one legal placement establishes a three-copy partition. Every red edge participates in the same concrete cross correspondence; uncolored internal grid edges remain intact.'
        math='All options have area five, so the 15-cell board needs three congruent copies. Exhaustively enumerate all placements under all eight square-grid isometries and all unordered disjoint triples. The frozen board is a 4x4 square minus its lower-right unit cell. The original A pentomino has two complete tilings, while B,C,D,E each have zero; saved mathematical_enumeration.json records every shape, placement count, solution count and A witnesses. In particular an X-shaped patch can occur locally but three X shapes cannot cover the board. Therefore A remains the unique option. Appearance colors do not impose mandatory cut lines or change the available grid cells.'
        human='Twenty-four original unit boundary segments receive 2pt red style, 12 enclosing a genuine source-board cross and 12 enclosing E. All interior grid edges remain black and visible, as do the full 4x4-minus-corner outline, all five option shapes and letters. No line is added/removed, so no cell count or cut target changes.'
    elif (qid,vid)==('Plane209','rectangle_component_migrations'):
        for oid in ['door0','base1','door3','garage4']:whole(oid,RED,'The actual large 1-by-2 rectangular block, appearing vertically or horizontally in houses 1,2,4,5; a concrete component correspondence.')
        for oid in ['orange0','orange1','orange3','orange4']:whole(oid,BLUE,'The actual slender rectangular block, appearing as inset/roof chimney in houses 1,2,4,5; a second component correspondence. Source width differences remain visible; no exact equality asserted.')
        expected='E';mechanism='Use two actual rectangular-component families to link houses 1,2,4,5, despite their differing remaining blocks. Targets inferring the same complete inventory from two repeated movable rectangle parts and overlooking the small body of house 2 and flatter roof of house 5. Each color marks a specified input component, rather than an option-letter cue.'
        math='House 1 and house 4 share the complete inventory: a large square body, tall isosceles roof, one 1x2 rectangular block, one slender rectangular block and three congruent small right-isosceles triangles (the third triangle is rotated over the door in house 4). House 2 has a smaller square body and only two small triangles. House 3 has four small triangles and a much smaller rectangular chimney instead of the 1x2 block. House 5 has a flatter triangular roof. These visible shape/count differences exclude every pair/group except houses 1 and 4, which is A. Colors identify two repeated components only; their boundaries and all distinguishing bodies, roofs and triangles remain unchanged.'
        human='Only eight existing rectangle contours receive 2pt red/blue style. The complete source house bodies, roof slopes, all small triangles, number badges and every option text remain readable. No relation mark or new building block is added.'
    else:raise ValueError((qid,vid))
    out=HERE/qid/vid;out.mkdir(parents=True,exist_ok=False)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer '+expected,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:meta});normalized,png,pixels=pr.render(plugin);n2,png2,pixels2=pr.render(normalized,frozen=True)
    assert normalized==n2 and png==png2 and pixels==pixels2
    assert before==inputs(ad,qid)
    used={a['target'] for a in actions if a['type']=='set_object_style'}|{b['object_id'] for b in overlay_bindings}
    safe_paths={o:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[o]] for o in sorted(used)}
    write(out/'eligibility_before_design.json',check);write(out/'context.json',meta);write(out/'path_fingerprints.json',safe_paths)
    write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':expected,'correct_answer':ad.records[qid]['answer'],'mechanism':mechanism,'mathematical_solution':math,'human_gate':human,'marker_roles':roles,'overlay_bindings':overlay_bindings,'review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
    write(out/'render_check.json',{'question_id':qid,'baseline_pixel_match':True,'baseline_pixel_sha256':meta['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True})
    print(json.dumps({'qid':qid,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png'),'rendered':True}),flush=True)
if __name__=='__main__':render(sys.argv[1],sys.argv[2])
